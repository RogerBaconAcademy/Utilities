@echo off
set /p sourceDir=Which directory structure would you like to copy?
set /p outputDir=Please name the new directory tree?
xcopy %sourceDir%\ %outputDir%\ /t /e
