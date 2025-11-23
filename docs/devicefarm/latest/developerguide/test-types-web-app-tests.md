# Web app tests in AWS Device Farm

Device Farm provides testing with Appium for web applications. For more information on setting up your Appium tests
on Device Farm, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md").

## Rules for metered and unmetered devices

Metering refers to billing for devices. By default, Device Farm devices are metered and you are
charged per minute after the free trial minutes are used up. You can also choose to purchase
unmetered devices, which allow unlimited testing for a flat monthly fee. For more information
about pricing, see [AWS Device Farm Pricing](https://aws.amazon.com/device-farm/ "https://aws.amazon.com/device-farm/").

If you choose to start a run with a device pool that contains both iOS and Android
devices, there are rules for metered and unmetered devices. For example, if you have five
unmetered Android devices and five unmetered iOS devices, your web test runs use your
unmetered devices.

Here is another example: Suppose you have five unmetered Android devices and 0 unmetered iOS
devices. If you select only Android devices for your web run, your unmetered devices are
used. If you select both Android and iOS devices for your web run, the billing method
is metered, and your unmetered devices are not used.
