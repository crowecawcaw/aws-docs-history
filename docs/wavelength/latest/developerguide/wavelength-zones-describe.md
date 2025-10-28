# Find your AWS Wavelength Zones

The number and mapping of Wavelength Zones per Region might vary between AWS accounts. The
following procedures demonstrate how to find the Wavelength Zones that are available to your
account.

###### To find your Wavelength Zones using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation bar, choose the **Regions** selector and then
   choose the Region.
3. On the navigation pane, choose **EC2 Dashboard**.
4. In the upper-right corner of the page, choose **Account attributes**,
   **Zones**.

###### To find your Wavelength Zones using the AWS CLI

- Use the [describe-availability-zones](../../../cli/latest/reference/ec2/describe-availability-zones.md "../../../cli/latest/reference/ec2/describe-availability-zones.md") command as follows to describe the Wavelength Zones
  within the specified Region that are enabled for your account.

```
`aws ec2 describe-availability-zones --region `region-name``
```

- Use the [describe-availability-zones](../../../cli/latest/reference/ec2/describe-availability-zones.md "../../../cli/latest/reference/ec2/describe-availability-zones.md") command as follows to describe the Wavelength Zones
  regardless of the opt-in status.

```
`aws ec2 describe-availability-zones --all-availability-zones`
```
