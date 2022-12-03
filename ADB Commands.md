- Trust overlay app in Android 12, fix Facebook Messenger mod chat head too

```
adb shell settings put global block_untrusted_touches 0
```

- Allow app to open direct link

```
adb shell pm set-app-links --package [replace package name] 1 all
```
