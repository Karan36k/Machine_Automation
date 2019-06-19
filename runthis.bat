@echo off
cls
:start
echo.
echo 1. Komodo 
echo 2. IntelliJ IDEA Community Edition 2019.1.2
echo 3. PHP Storm x86 (PAID SOFTWARE)
echo 4. WebStorm (PAID SOFTWARE)
echo 5. Visual Studio(devenv)
echo 6. Net Beans
echo 7. eclipse PHP Version 
echo 8. eclipse Java Version
echo 9. Ruby
echo 10.Pycharm
echo 11. I'm Done
echo.
echo.
set /p x=Pick:
IF '%x%' == '%x%' GOTO Item_%x%

:Item_1
start /MIN /D"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\ActiveState Komodo IDE 11" Komodo IDE 11.exe
GOTO Start

:Item_2
start /MIN /D"C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2019.1.2\bin" idea64.exe
GOTO Start

:Item_3
start /MIN /D"C:\Program Files\JetBrains\PhpStorm 2019.1.2\bin" phpstorm64.EXE
GOTO Start

:Item_4
start /MIN /D"C:\Program Files\JetBrains\WebStorm 2019.1.2\bin" webstorm64.EXE
GOTO Start

:Item_5
start /MIN /D"C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\Common7\IDE" devenv.exe
GOTO Start

:Item_6
start /MIN /D"C:\Program Files\NetBeans 8.0\bin" netbeans64.exe
GOTO Start

:Item_7
start /MIN /D"D:\eclipse-php" eclipse.exe
GOTO Start 

:Item_8
start /MIN /D"D:\Eclipse-java" eclipse.exe
GOTO Start

:Item_9
start /MIN /D"C:\Ruby25-x64\bin" ruby.exe
GOTO Start

:Item_10
start /MIN /D"C:\Program Files\JetBrains\PyCharm Community Edition 2017.3.1\bin" pycharm64.exe
GOTO Start 



:Item_8
exit