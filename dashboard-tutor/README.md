# Dashboard Tutor — automatic Academy integration

This folder adds the Tinitiate AI interactive lesson recorder to the **unmodified** MasterClass Academy pages.

**Start here:** [`../README_DASHBOARD_TUTOR.md`](../README_DASHBOARD_TUTOR.md).

Run `../START_DASHBOARD_TUTOR.cmd` from Windows (or `npm ci`, `npx playwright install chromium`, `node cli.js serve` on another platform). The local server detects an eligible dashboard when the page is opened and injects the shared recorder into the HTTP response. No manual HTML editing, per-lesson JavaScript, scan, or install step is required.

- CLI: `node cli.js check`, `node cli.js scan` (optional report), `node cli.js serve`, and `node cli.js record foundational/python/print.html --silent --limit 3` for a non-publishing preview.
- Recordings: `../assets/dashboard-tutorials/<page-id>.mp4` with JSON metadata.
- Backend: localhost-only Node HTTP API, Playwright, ElevenLabs, FFmpeg.
- Frontend: `client/auto-tour.js` and `client/auto-tour.css`.
- Tests: `npm test`.

This source archive has **no `print-v2.html`**. Its existing `foundational/python/print.html` and the Academy's original navigation are preserved.

The Node server is for local authoring; a static host such as GitHub Pages cannot initiate recordings. New advanced/complex dashboards may still require a dedicated recording plan or layout repair.
