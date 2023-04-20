Sao lưu bản quyền:

- Lệnh sẽ lưu thư mục "SAOLUUBANQUYEN" vào 3 ổ D,E,F (nếu có) trên máy các bạn, sau đó ẩn đi. Chỉ có thể nhìn thấy khi tích vào duyệt file ẩn, tránh cho các bạn xoá nhầm.

- Chạy Command Prompt bằng quyền Administrator, dán lệnh vào.

for %i in (D,E,F) DO MKDIR %i:SAOLUUBANQUYEN && if exist %i:\SAOLUUBANQUYEN (attrib +h "%i:\SAOLUUBANQUYEN")

cd C:\Windows\System32

net stop sppsvc

for %i in (D,E,F) DO xcopy "%windir%\system32\spp\store" "%i:\SAOLUUBANQUYEN" /e /i /h

exit

===========================================================

- Với máy chỉ có duy nhất ổ C, chúng ta sẽ lưu vào Desktop, sau đó cất vào USB hay Onedrive cho an toàn.

MKDIR "%USERPROFILE%/DESKTOP/SAOLUUBANQUYEN"

cd C:\Windows\System32

net stop sppsvc

xcopy "%windir%\system32\spp\store" "%USERPROFILE%/DESKTOP/SAOLUUBANQUYEN" /e /i /h

exit

===========================================================

Khôi phục bản quyền:

cd C:\Windows\System32

net stop sppsvc

if %errorlevel% == 2 echo The Software Protection service is not started.

if %errorlevel% == 0 echo The Software Protection service was stopped successfully.

echo Errorlevel: %errorlevel%

for %i in (D,E,F) DO xcopy "%i:\SAOLUUBANQUYEN" "%windir%\system32\spp\store" /e /i /h

exit

- Với máy chỉ có duy nhất ổ C thì copy thư mục sao lưu vào Desktop trước.

cd C:\Windows\System32

net stop sppsvc

if %errorlevel% == 2 echo The Software Protection service is not started.

if %errorlevel% == 0 echo The Software Protection service was stopped successfully.

echo Errorlevel: %errorlevel%

xcopy "%USERPROFILE%/DESKTOP/SAOLUUBANQUYEN" "%windir%\system32\spp\store" /e /i /h

exit
