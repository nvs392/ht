set now=%DATE: =0% %TIME: =0%
for /f "tokens=1-7 delims=/-:., " %%a in ( "%now%" ) do (
    set now=%%c-%%b-%%a_%%d_%%e
)

echo %now%
