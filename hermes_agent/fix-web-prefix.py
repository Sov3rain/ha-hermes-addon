"""Adapt the pinned Vite bundle to Home Assistant's dynamic ingress prefix.

The upstream HTML/API prefix support does not cover Vite's lazy preload helper.
Fail at build time if that helper changes. Rename JS assets and their references
so browsers cannot reuse the immutable, unpatched bundles from an older app.
"""
from pathlib import Path

root = Path('/opt/hermes/hermes_cli/web_dist')
assets = sorted((root / 'assets').glob('*.js'))
needle = 'function(e){return`/`+e}'
replacement = 'function(e){return(window.__HERMES_BASE_PATH__||``)+`/`+e}'
count = sum(p.read_text().count(needle) for p in assets)
if count != 1:
    raise SystemExit(f'Expected one Vite preload URL helper, found {count}; review upstream bundle')

names = {p.name: p.stem + '.haos2.js' for p in assets}
for path in [root / 'index.html', *assets]:
    content = path.read_text().replace(needle, replacement)
    for old, new in names.items():
        content = content.replace(old, new)
    path.write_text(content)
for path in assets:
    path.rename(path.with_name(names[path.name]))
print('Patched ingress preload URLs and versioned JavaScript assets')
