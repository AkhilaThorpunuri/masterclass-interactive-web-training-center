DASHBOARD TUTOR — BLANK VIDEO / INVISIBLE LESSON FIX
=======================================================

Verified cause:
The old stage.js appended #tutor-backdrop to <html> at z-index 99.
Your Academy page places its lesson in nested stacking contexts under <body>.
As a result, the backdrop covered the lesson, while the mouse spotlight
and title remained visible. The published MP4 appeared empty.

This replacement:
- Moves the recording backdrop inside <body> and BELOW the <main> lesson.
- Keeps the earlier Scene 1 clipping layout correction.
- Checks that Python dashboard topics/slides initialized; errors instead
  of publishing an empty tutorial when they fail to load.
- Does not change the normal student-facing lesson HTML or other files.

INSTALL — ONE FILE ONLY
1. Stop the Dashboard Tutor server by pressing Ctrl+C.
2. Open C:\Code\masterclass-interactive-web-training-center\dashboard-tutor\lib
3. Rename stage.js to stage.before-blank-fix.js (backup).
4. Extract stage.js from this ZIP directly into the same lib directory.
   Your final file path MUST be:
   C:\Code\masterclass-interactive-web-training-center\dashboard-tutor\lib\stage.js
   No new subfolder is needed.

RESTART (CMD)
  cd /d C:\Code\masterclass-interactive-web-training-center\dashboard-tutor
  node --env-file=.env cli.js serve

TEST WITHOUT ELEVENLABS COST (SECOND CMD WINDOW)
  cd /d C:\Code\masterclass-interactive-web-training-center\dashboard-tutor
  node cli.js record foundational/python/print.html --silent --limit 3

The silent test creates a PREVIEW file, not a published video. Look for
"previewOutput" in the resulting JSON and open that MP4 to verify the
Python topic cards and slide player are visible.

The previously generated blank MP4 is not automatically repaired. After
confirming the silent preview, click Record Tutorial again to make a NEW
narrated MP4. Hard-refresh (Ctrl+Shift+R) if the old video is cached.

VALIDATED
- Reproduced the blank recording backdrop over the actual Python lesson.
- Reproduced visible dashboard (17 topics) and first Python code slide
  after the fix in Chromium at 1920x1080.
- Both capture regions passed stage.focus() clipping checks.
- Existing Node tests: 19 passed, 0 failed, 2 skipped.
- Actual full ElevenLabs recording on Windows has NOT been retested here.
