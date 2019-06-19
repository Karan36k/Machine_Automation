@if (@CodeSection == @Batch) @then


@echo off

rem Use %SendKeys% to send keys to the keyboard buffer
set SendKeys=CScript //nologo //E:JScript "%~F0"

rem Start the other program in the same Window
start "" /B cmd

%SendKeys% "echo off{ENTER}"

set /P "=Wait and send a command: " < NUL
ping -n 5 -w 1 127.0.0.1 > NUL
%SendKeys% "echo Hello, world!{ENTER}"

set /P "=Wait and send an Up Arrow key: [" < NUL
ping -n 5 -w 1 127.0.0.1 > NUL
%SendKeys% "{UP}"

set /P "=] Wait and send an Enter key:" < NUL
ping -n 5 -w 1 127.0.0.1 > NUL
%SendKeys% "{ENTER}"

%SendKeys% "exit{ENTER}"

goto :EOF


@end
