# Setting a device PIN when running tests in

Device Farm

Some applications require that you set a PIN on the device. Device Farm does not support setting a PIN on devices
natively. However, this is possible with the following caveats:

- The device must be running Android 8 or above.
- The PIN must be removed after the test is complete.
  To set the PIN in your tests, use the `pre_test` and `post_test` phases to set and
  remove the PIN, as shown following:

```

phases:
    pre_test:
      - # ... among your pre_test commands
      - DEVICE_PIN_CODE="1234"
      - adb shell locksettings set-pin "$DEVICE_PIN_CODE"
    post_test:
      - # ... Among your post_test commands
      - adb shell locksettings clear --old "$DEVICE_PIN_CODE"

```

When your test suite begins, the PIN 1234 is set. After your test suite exits, the PIN is removed.

###### Warning

If you don't remove the PIN from the device after the test is complete, the device and your account will be
quarantined.

For more ways to extend your test suite and optimize your tests, see [Extending custom test environments in Device Farm](custom-test-environments-extending.md "custom-test-environments-extending.md").
