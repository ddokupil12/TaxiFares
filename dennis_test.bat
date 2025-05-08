setlocal EnableDelayedExpansion
REM filepath: c:\Users\denni\OneDrive\Desktop\TaxiFares\dennis_test.bat


SET EPOCH=10
SET H1=10
SET H2=10
SET H3=10


FOR /L %%i IN (1,1,20) DO (
    echo Running iteration %%i
    
    set /a H1TMP=H1 * %%i
    set /a H2TMP=H2 * %%i
    set /a H3TMP=H3 * %%i

    c:\Users\denni\OneDrive\Desktop\TaxiFares\taxi_fare_venv\Scripts\python.exe c:\Users\denni\OneDrive\Desktop\TaxiFares\main.py -e %EPOCH% -h1 !H1TMP! -h2 !H2TMP! -h3 !H3TMP! -t .33
)