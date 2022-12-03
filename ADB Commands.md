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

```
adb shell pm enable --user 0 <packagename>
```

- Uninstall app

```
pm uninstall –k –user 0 <packagename>
```

-Reinstall app

```
adb shell cmd package install-existing <packagename>
```

## Doze Android command

- Buttery powered state

```
adb shell dumpsys battery | grep powered
```

- Unplug battery

```
adb shell dumpsys battery unplug
```

- Reset battery

```
adb shell dumpsys battery reset
```

- Dump Doze mode info

```
adb shell dumpsys deviceidle
```

- Enable Doze mode (may be required on Android Emulator)

```
adb shell dumpsys deviceidle enable
```

- Get status of Light Doze mode

```
adb shell dumpsys deviceidle get light
```

- Get status of Deep Doze mode

```
adb shell dumpsys deviceidle get deep
```

- Enter Light Doze mode (should be called several times to pass all phases)

```
adb shell dumpsys deviceidle step light
```

- Enter Deep Doze mode (should be called several times to pass all phases)

```
adb shell dumpsys deviceidle step deep
```
