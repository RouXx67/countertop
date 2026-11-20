# What's new in Countertop

Each version gets a section here. The newest is on top. Install a version from the [releases page](https://github.com/kizit/countertop/releases); Docker and Unraid use the `ghcr.io/kizit/countertop` image with the same tag.

## v0.4.0 (2026-11-20)

### New
- **Home Assistant tiles.** Connect Home Assistant in Controls → Setup with its address and an access token, then add a **Home** tile (lights, switches, doors and sensors, with on/off switches and Run buttons for scenes) or a **Sensor** tile (one reading in big type). Locks, garage doors and alarms are shown but can't be changed from the screen. See [Home Assistant](docs/home-assistant.md).

### Changed
- The diagnostics file now removes every private field from Setup, including Home Assistant tokens, and anything else that looks like a token.

## v0.3.1 (2026-11-20)

### Fixed
- **The Mac app no longer freezes on its first start** when it opens from the folder it was downloaded to. It now asks you to move it to Applications.
- **Moving from the old Kitchen Dashboard app keeps your settings.** The downloaded app copies them in and runs its own server, instead of running the old folder.
- **Reminders Sync problems show in the menu.** The menu used to say everything was working while the icon was orange. Reminders Sync also checks the server address when you set it up.

### Changed
- When the server runs on the same Mac, the Reminders Sync menu points you to the simpler choice: Apple Reminders in Controls > Setup > Lists.

## v0.3.0 (2026-11-20)

### New
- **A Countertop app for Mac you can download.** Each release now includes a ready-made app with the server and everything it needs inside: no Xcode, Terminal or Python needed. It sits in the menu bar, shows whether everything is working, installs new versions with one click, and keeps your settings in Application Support.
- **Reminders Sync is part of the Mac app.** It replaces the separate List Sync helper, and it fills in the sync key for you when the server runs on the same Mac. It also works with a server on Docker or Unraid.

### Changed
- The menu bar app is now called Countertop (it was Kitchen Dashboard) and its menu is shorter. Building it from the source is now `zsh mac/build.sh`. It takes over from the old app, its login item and the old List Sync helper.
- The server only starts HTTPS when a certificate exists, instead of failing to start.

### Fixed
- **Shorter clock and weather boxes keep their text size.** Making a Clock or Weather now box shorter takes away its empty space first; the text only gets smaller once it no longer fits. Before, a tile made with the designer shrank all its text with the box, and the plain styles often shrank more than they needed to.

## v0.2.0 (2026-11-20)

### New
- **A setup guide for new installs.** The first time you open Controls, it asks for your town, a calendar and where your grocery list lives, then shows the addresses to open on the Echo and on your phone. You can run it again from Controls → Status.
- **Status in Controls.** See at a glance whether the screen is checking in, when the weather, calendars and list last loaded, and anything that needs a look.
- **Update notices.** Controls tells you when a new version is out, with a link to what changed and how to update. Countertop asks GitHub for the newest version number twice a day and sends nothing about your setup. Turn it off in Status.
- **Download diagnostics.** One button saves a zip with your settings, version and recent logs to attach to a bug report. Private links, sync keys, your location and network addresses are removed first.
- **Show your Apple Reminders list without a Mac server.** A list can be "Sent from another app": an iPhone Shortcut or the new Countertop List Sync helper for Mac sends it to Countertop, wherever the server runs. See [list sync](docs/list-sync.md).
- **Read a list from a web address.** Point a list at a published text file, Markdown checklist, JSON or iCal to-dos, and Countertop reads it every five minutes.
- **Edit the screen by touch on the Echo.** Controls on the Echo has an "Edit the screen" button, the editor has a ⚙ Settings button, and dragging tiles works better with fingers. The screen no longer reloads while you're editing.

### Fixed
- Controls on the Echo no longer jumps back to the dashboard about 30 seconds after you save a change.

## v0.1.0 (2026-11-19)

The first public release.

- The kitchen dashboard for the Echo Show 15 and other browser screens: clock, weather, calendars, the shared grocery list, sports, photos, deals and more than 30 tiles.
- Controls with an on-screen editor, looks, effects, pages and a night page.
- Docker images for amd64 and arm64, a Docker Compose file, and an Unraid template.
