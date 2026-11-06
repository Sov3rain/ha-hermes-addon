# Hermes Agent for Home Assistant OS — Sov3rain fork

Home Assistant app wrapping the official Nous Research Hermes Docker image.
Current release: Hermes **v0.23.0**, app **0.23.0-1**.

Add this repository in **Settings → Apps → App store → Repositories**:

```text
https://github.com/Sov3rain/ha-hermes-addon
```

Install **Hermes Agent (Sov3rain)**, configure your model and API key, and use
**Open Web UI**. State lives in the app's persistent `/data` directory.
The dashboard and terminal are available only through authenticated Home Assistant ingress.

Updates are installed through Home Assistant. The Hermes dashboard's source
updater does not update Docker images. New app releases pin and test a specific
upstream version; no moving `latest` tag is used.

This is a community fork of [diegaccio/ha-hermes-addon](https://github.com/diegaccio/ha-hermes-addon),
not an official Nous Research or Home Assistant app.
See [configuration and migration notes](hermes_agent/DOCS.md).
