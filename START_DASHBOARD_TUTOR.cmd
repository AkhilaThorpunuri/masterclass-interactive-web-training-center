@echo off
setlocal
cd /d "%~dp0dashboard-tutor" || exit /b 1
where node >nul 2>nul || (echo ERROR: Install Node.js 20 or newer. & exit /b 1)
if not exist "node_modules\playwright\package.json" (
  echo Installing Dashboard Tutor dependencies...
  call npm ci || exit /b 1
  call npx playwright install chromium || exit /b 1
)
if exist ".env" (
  node --env-file=.env cli.js serve
) else (
  echo Note: .env not found. Lesson browsing and recorder UI will work; narrated recording needs your .env.
  node cli.js serve
)
endlocal
