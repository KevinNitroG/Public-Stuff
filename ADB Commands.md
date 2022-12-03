- Trust overlay app in Android 12, fix Facebook Messenger mod chat head too

```
adb shell settings put global block_untrusted_touches 0
```

- Allow app to open direct link

```
adb shell pm set-app-links --package <packagename> 1 all
```

- Disable app

```
adb shell pm disable-user --user 0 <packagename>
```

- Enable app

```adb shell pm enable --user 0 <packagename>

- Uninstall app

```
pm uninstall –k –user 0 <packagename>
```

-Reinstall app

```
adb shell cmd package install-existing <packagename>
