# Dashboard Tutor — integrated into this Academy

This ZIP is an entire Academy website plus the `dashboard-tutor/` recorder. The input archive has **no `print-v2.html`**; the original `foundational/python/print.html` is kept unchanged. **No per-page install scripts are necessary.**

## Windows quick start (CMD)

1. Extract the ZIP to `C:\Code` to get **exactly** `C:\Code\masterclass-interactive-web-training-center\` (one root folder, not a nested copy). Do not overwrite a different Academy checkout without a backup.
2. Keep your existing local credentials safe: copy your own `dashboard-tutor\.env` into this project's `dashboard-tutor\` directory. This ZIP has no private credentials.
3. Open CMD and run these lines, pressing Enter after each:

```bat
cd /d C:\Code\masterclass-interactive-web-training-center
call START_DASHBOARD_TUTOR.cmd
```

4. Open the **exact URL** (no asterisks or query suffix):
   `http://127.0.0.1:4173/foundational/python/print.html`

For the 3-scene *silent preview*, keep server CMD open and use a second CMD:

```bat
cd /d C:\Code\masterclass-interactive-web-training-center\dashboard-tutor
node --env-file=.env cli.js record foundational/python/print.html --silent --limit 3
```

The preview is stored in `dashboard-tutor/work/` and **does not** replace published MP4s. Click the `Record Tutorial` button in the page for the full narrated recording. That uses your ElevenLabs API key and will consume credits.

## Automatic lesson detection

The local server analyzes every requested HTML lesson and adds the recorder controls to a supported interactive dashboard **in the HTTP response only**. Adding `foundational/python/new-lesson.html` does not require `scan`, `install`, page-specific JavaScript, or a server restart. The original HTML is not edited. Recorded MP4s and JSON metadata are saved to `assets/dashboard-tutorials/<page-slug>.mp4` and `.json`.

On a **static host such as GitHub Pages**, no live Node API exists and this server-side injection does not run. Publish an existing generated video by embedding or injecting its player during deployment, and run recordings only in the local authoring server. The automatic recorder UI and endpoints will not appear on a static host by themselves.

## Folder layout

- `dashboard-tutor/cli.js` — scan/check/serve/record
- `dashboard-tutor/lib/server.js` — local server and recording API
- `dashboard-tutor/lib/scanner.js` — detects dashboards per request
- `dashboard-tutor/lib/plan.js` — lesson-specific and generic walkthroughs
- `dashboard-tutor/lib/recorder.js` — Playwright and FFmpeg
- `dashboard-tutor/client/auto-tour.js` — automatic record button and video player
- `dashboard-tutor/test/` — regression tests

## Diagnostics

```bat
cd /d C:\Code\masterclass-interactive-web-training-center\dashboard-tutor
node --env-file=.env cli.js check
npm test
node cli.js scan
```

If `node --env-file=.env` says `.env` not found, create `.env` from `.env.example` and supply your own ElevenLabs settings locally. The ZIP contains no API keys. Full recording requires Playwright Chromium, FFmpeg and ElevenLabs; silent preview does not need ElevenLabs. Some advanced dashboards may need a custom capture adapter or layout fixes before a full video succeeds.
