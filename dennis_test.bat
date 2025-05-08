setlocal EnableDelayedExpansion
REM filepath: c:\Users\denni\OneDrive\Desktop\TaxiFares\dennis_test.bat


SET EPOCH=10
SET H1=256
SET H2=144
SET H3=32
SET TR=0.1

FOR /L %%i IN (1,1,10) DO (
    echo Running iteration %%i
    
 
    for /f "usebackq delims=" %%A in (`powershell -Command "[math]::Round(%%i * %TR%, 2)"`) do (
        set TRTMP=%%A
    )

    c:\Users\denni\OneDrive\Desktop\TaxiFares\taxi_fare_venv\Scripts\python.exe c:\Users\denni\OneDrive\Desktop\TaxiFares\main.py -e %EPOCH% -h1 %H1% -h2 %H2% -h3 %H3% -t !TRTMP!
)