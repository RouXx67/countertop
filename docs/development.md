# Developing Countertop

You can work on Countertop on the same computer that runs your real dashboard. Keep two copies apart:

| | Everyday copy | Development copy |
|---|---|---|
| What runs it | The Countertop app (or Docker) | A git clone of this repo |
| Port | 8090 | 8091 (or any free port) |
| Settings and lists | The app's own data folder | The clone's `work/` folder |
| Changes when | You install a release | You edit files or switch branches |

The two copies never share settings, so trying something out can't break the screen in your kitchen.

## Run the development copy

```sh
git clone https://github.com/kizit/countertop.git
cd countertop
python3 tools/countertop.py --port 8091
```

Open `http://localhost:8091/control`. The first time you do this, the setup guide walks you through the basics. To start with a copy of your real settings instead, copy the app's data folder into `work/` first. On a Mac it's `~/Library/Application Support/Countertop` (in the app menu, **Show Settings Folder**). `work/` is ignored by git, so your settings stay out of commits.

To keep development data somewhere else, set `COUNTERTOP_DATA`:

```sh
COUNTERTOP_DATA=~/countertop-dev-data python3 tools/countertop.py --port 8091
```

Press Ctrl-C to stop the server. After you change `tools/countertop.py`, restart it. Changes to the pages and tiles in `tools/` take effect the next time you reload them.

## Preview without the real screen

The preview in Controls shows the dashboard as the screen will show it. To try a change on the real screen, point the device at the development copy (`http://<this computer>:8091/dash`) and point it back at port 8090 when you're done.

Select **Portrait** in Controls to preview a 1080×1920 display. To capture the wall display, tablet, calendar, night page and Controls preview with the bundled demo data, run `node demo/capture-readme.js portrait` with Playwright and Chromium installed. Set `OUT` to choose a screenshot folder.

Run `node demo/capture-readme.js manual-portrait` to simulate a browser that keeps reporting 1920×1080 on a vertically mounted display. It saves the setting from a separate Controls browser, checks the open dashboard at its normal address, verifies touch gestures and persistence after a reload, and captures the native landscape framebuffer for each mount.

## Work on the Mac app

`zsh mac/build.sh` builds `~/Applications/Countertop.app` from the clone, so the app runs the server from your clone. `zsh mac/package.sh` makes a downloadable build like the ones attached to releases, in `dist/`.

Only one Countertop app can run at a time, and both use port 8090. On a Mac where you also run the everyday app, `build.sh` quits it, so open your everyday app again when you're done testing.

## Ship a change

Open a pull request against `main`, and add a one-line note under [changes/](../changes/README.md) if people will notice the change. Once it is merged, a release puts it in front of everyone, including your own everyday copy. See [releasing](releasing.md).
