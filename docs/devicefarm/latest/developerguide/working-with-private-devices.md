# Private devices in AWS Device Farm

A private device is a physical mobile device that AWS Device Farm deploys on your behalf in an Amazon data center.
This device is exclusive to your AWS account.

###### Note

Currently, private devices are available only in the AWS US West (Oregon) Region (`us-west-2`).

If you have a private device fleet, you can create remote access sessions and schedule test runs with your
private devices. For more information, see [Creating a test run or starting a remote access
session in AWS Device Farm](create-test-run-using-private-devices.md "create-test-run-using-private-devices.md"). You can also create instance profiles to control
the behavior of your private devices during a remote access session or a test run. For more information, see
[Creating an instance profile in AWS Device Farm](set-up-private-devices-account-settings.md "set-up-private-devices-account-settings.md"). Optionally, you can request that certain Android
private devices be deployed as rooted devices.

You can also create an Amazon Virtual Private Cloud endpoint service to test private apps that your company has access to, but
are not reachable through the internet. For example, you might have a web application running in your VPC that
you want to test on mobile devices. For more information, see [Using Amazon VPC endpoint services with Device Farm - Legacy
(not recommended)](amazon-vpc-endpoints.md "amazon-vpc-endpoints.md").

If you're interested in using a fleet of private devices, [contact us](mailto:aws-devicefarm-support@amazon.com "mailto:aws-devicefarm-support@amazon.com"). The Device Farm team must work with you to set
up and deploy a fleet of private devices for your AWS account.

###### Topics

- [Creating an instance profile in AWS Device Farm](set-up-private-devices-account-settings.md "set-up-private-devices-account-settings.md")
- [Request additional private devices in AWS Device Farm](managing-private-device-instance.md "managing-private-device-instance.md")
- [Creating a test run or starting a remote access
  session in AWS Device Farm](create-test-run-using-private-devices.md "create-test-run-using-private-devices.md")
- [Selecting private
  devices in a device pool in AWS Device Farm](selecting-private-devices.md "selecting-private-devices.md")
- [Skipping app re-signing on private devices in
  AWS Device Farm](skip-app-re-signing-on-private-devices.md "skip-app-re-signing-on-private-devices.md")
- [Amazon VPC across AWS Regions in AWS Device Farm](amazon-vpc-cross-region.md "amazon-vpc-cross-region.md")
- [Terminating private devices in Device Farm](terminate-private-device.md "terminate-private-device.md")
