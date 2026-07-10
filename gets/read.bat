@echo off
setlocal enabledelayedexpansion

if not exist "%~dp0post.txt" (
    exit /b 
)

for /r %%E in ("%~dp0post.txt") do (
    set "postdata=%%E"
    set "url=%%~nE"
)
curl --data "%postdata%" --url "%url%"
endlocal
