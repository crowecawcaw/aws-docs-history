

# Request additional private devices in AWS Device Farm
<a name="managing-private-device-instance"></a>

In AWS Device Farm, you can request an additional private device instances to be added to your fleet. You can also view and change the settings of existing private device instances in your fleet. For more information about private devices, see [Private devices in AWS Device Farm](working-with-private-devices.md).

**To request additional private devices or change their settings**

1. Open the Device Farm console at [https://console.aws.amazon.com/devicefarm/](https://console.aws.amazon.com/devicefarm/).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Private devices**.

1. Choose **Device instances**. The **Device instances** tab displays a table of the private devices that are in your fleet. To quickly search or filter the table, enter search terms in the search bar above the columns.

1. To request a new private device instance, choose **Request device instance** or [contact us](mailto:aws-devicefarm-support@amazon.com). Private devices require additional setup with help from the Device Farm team.

1. In the table of device instances, choose the toggle option next to the instance that you want to view information about or manage, then choose **Edit**.  
![Settings for a device instance](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-edit-device-instance.png)

1. To attach an instance profile to the device instance, choose it from the **Profile** drop-down list. Attaching an instance profile can be helpful if you want to always exclude a specific app package from cleanup tasks, for example. For more information about using instance profiles with devices, see [Creating an instance profile in AWS Device Farm](set-up-private-devices-account-settings.md).

1. (Optional) Under **Labels**, choose **Add new** to add a label to the device instance. Labels can help you categorize your devices and find specific devices more easily.

1. Choose **Save**.