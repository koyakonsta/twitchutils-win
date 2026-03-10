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
    powershell -Command "Start-Process -Wait -FilePath '%0' -Verb RunAs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
	

start /b "" cmd /c "taskkill /F /IM streamlink.exe /T & streamlink --player-external-http --player-external-http-port 80 https://www.twitch.tv/%~n0 best"

vlc --one-instance --loop --video-title-timeout 0 http://localhost :meta-title="➤ ԷᴡɪԷᴄʜ: %~n0 " --qt-minimal-view --video-on-top --zoom=0.25 --autoscale --no-video-deco
