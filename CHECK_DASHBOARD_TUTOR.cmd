@echo off
setlocal
cd /d "%~dp0dashboard-tutor" || exit /b 1
if exist ".env" (node --env-file=.env cli.js check) else (node cli.js check)
call npm test
endlocal
