DASHBOARD TUTOR — SCENE 32 LONG-OUTPUT LAYOUT FIX
================================================
This fix is for the narrated Python Print failure where #py-term extends to
about y=1280 while the safe recording frame ends at y=974.

REPLACE EXACTLY TWO FILES (no installer, no full project re-extraction):

1. Stop the running Dashboard Tutor server with Ctrl+C.
2. Open THIS ZIP in File Explorer.
3. From the ZIP, copy stage.js to:
   C:\Code\masterclass-interactive-web-training-center\dashboard-tutor\lib\stage.js
   Choose Replace. First rename your current stage.js to stage.before-scene32.js.
4. From the ZIP, copy validate-scene32.js to:
   C:\Code\masterclass-interactive-web-training-center\dashboard-tutor\validate-scene32.js
   Put both files in their specified locations. Do NOT create another folder.

VALIDATE WITHOUT ELEVENLABS COST:
CMD WINDOW 1 (leave running):
  cd /d C:\Code\masterclass-interactive-web-training-center\dashboard-tutor
  node --env-file=.env cli.js serve

CMD WINDOW 2:
  cd /d C:\Code\masterclass-interactive-web-training-center\dashboard-tutor
  node validate-scene32.js

Expected output:
  PASS: Scene 32 stress check; long editor/output fit within the capture frame.

It writes a screenshot to dashboard-tutor\work\scene32-layout-check.png.
This check simulates an extended editor and 16-line output on slide 10, exactly
before the failed scene, and tests the real Chromium recording layout.
It does not send any requests to ElevenLabs or create a new video.

AFTER IT PASSES:
- Use the lesson page Record Tutorial button to retry the narrated video, or
  run this in CMD WINDOW 2:
    node --env-file=.env cli.js record foundational/python/print.html
- The video still needs visual review, especially long-output topics.

WHAT WAS CHANGED:
- Preserves the earlier Scene 1 layout and blank-video fixes.
- Adds a third, conditional recording-only layout fallback when compact layout
  still clips the Python source editor or terminal output.
- Keeps long source/output in scrollable regions; no source text is deleted.
- Keeps clipping and spotlight audits enabled; genuinely invalid layouts still fail.
- Does not modify normal lesson HTML, student-visible appearance, or ElevenLabs.

VALIDATION RUN LOCALLY:
- Playwright Chromium stress fixture: baseline clips near y=1319;
  standard refit clips near y=1301; long-output refit reports zero invalid boxes.
- Tested a taller CodeMirror-like editor plus multiline Python output.
- Project Node unit tests: 19 passed, 0 failed, 2 skipped (browser-dependent).
- Full narrated Windows recording: NOT yet verified with this replacement.
