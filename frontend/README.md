# Optional Hermes sidebar logo

This module registers `hermes:logo` with Home Assistant's frontend. It uses the
monochrome Nous Research logo shipped by the official Hermes image, with its
SVG path preserved and its original transform expressed by the icon viewBox.
See [the original asset](https://github.com/NousResearch/hermes-agent/blob/v0.23.0/assets/nous-girl-black.svg)
and [its MIT license](LICENSE-NousResearch).

The module is an optional **Home Assistant customization**, separate from the
Hermes app. Installing or updating the app does not install it automatically.
The app's default `mdi:robot-outline` remains usable without this module.

## Install

1. Copy [`hermes-icons.js`](hermes-icons.js) to `/config/www/hermes-icons.js`
   in Home Assistant. Create `www` if needed.
2. Add the module to the existing `frontend` section of `configuration.yaml`:

   ```yaml
   frontend:
     # Keep existing frontend options, including themes.
     extra_module_url:
       - /local/hermes-icons.js?v=1
   ```

   Merge with an existing `extra_module_url` list rather than replacing it.
   Do not add a second `frontend` section.
3. Check the Home Assistant configuration, restart Home Assistant Core, then
   reload the browser page. HAOS and the Hermes app do not need restarting.
4. Set the Hermes sidebar entry's icon to `hermes:logo` using Home Assistant's
   sidebar customization. This is a saved Home Assistant panel override, so an
   app update does not overwrite it.

Administrators can also set the panel override through Home Assistant's frontend
WebSocket API. For this fork, the equivalent browser-console command on a logged-in
Home Assistant page is:

```javascript
await document.querySelector("home-assistant").hass.callWS({
  type: "frontend/update_panel",
  url_path: "3487b525_hermes_agent",
  icon: "hermes:logo",
});
```

A different repository URL produces a different panel path. Do not change
permissions or expose the Hermes container to install an icon.

## Updates and removal

The installed copy under `/config/www` is not synchronized with GitHub. To update
it, copy the new module and increment the URL query version in the configuration
(for example, `?v=2`), then restart Core and reload the browser.

To remove the customization, first restore the panel icon to
`mdi:robot-outline` (or use `icon: null` in the API command to restore the app's
default). Remove this module's `extra_module_url` entry, restart Core, and remove
the copied file. Preserve any other frontend modules and settings.

This module was verified in the Home Assistant sidebar, including after a Core
restart. Adding it to this repository does not require an app version bump.
