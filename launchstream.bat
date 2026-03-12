@echo off
chcp 65001 >nul
if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dpnx0" %*
goto :EOF

:minimized
:: Check for Administrator privileges
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    powershell -WindowStyle Hidden -Command "Start-Process -FilePath '%0' -Verb RunAs"
    exit /b

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
	


start "" vlc --one-instance --loop http://localhost :meta-title="➤ ԷᴡɪԷᴄʜ: %~n0 " --qt-minimal-view --video-on-top --zoom=0.5 --autoscale --no-video-deco --qt-video-autoresize
powershell -WindowStyle Hidden -Command "taskkill /F /IM streamlink.exe; streamlink --player-external-http --player-external-http-port 80 https://www.twitch.tv/%~n0 best"
