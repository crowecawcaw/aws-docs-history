# Find supported macOS versions for your Amazon EC2 Mac Dedicated Host

You can view the latest macOS versions supported by your Amazon EC2 Mac Dedicated Host. With this functionality, you can validate whether your Dedicated Host can support instance launches with your preferred macOS versions.

Each macOS version requires a minimum firmware version on the underlying Apple Mac to
successfully boot. The Apple Mac firmware version can become outdated if an allocated
Mac Dedicated Host has remained idle for an extended period of time or if it has a long
running instance on it.

To ensure supportability for the latest macOS versions, you can stop or terminate
instances on your allocated Mac Dedicated Host. This triggers the host scrubbing
workflow and updates the firmware on the underlying Apple Mac to support the latest
macOS versions. A Dedicated Host with a long running instance will automatically be
updated when you stop or terminate a running instance.

For more information about the scrubbing workflow, see [Stop or terminate your Amazon EC2 Mac instance](mac-instance-stop.md "mac-instance-stop.md").

For more information about launching Mac instances, see [Launch a Mac instance using the AWS Management Console or the AWS CLI](mac-instance-launch.md "mac-instance-launch.md").

You can view information about the latest macOS versions supported on your allocated
Dedicated Host using the Amazon EC2 console or the AWS CLI.

Console

###### To view Dedicated Host firmware information using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Dedicated Hosts**.
3. On the **Dedicated Hosts details** page, under
   **Latest supported macOS versions**, you can
   see the latest macOS versions that the host can support.

AWS CLI

###### To view Dedicated Host firmware information using the AWS CLI

Use the [`describe-mac-hosts`](../../../cli/latest/reference/ec2/describe-mac-hosts.md "../../../cli/latest/reference/ec2/describe-mac-hosts.md")
command, replacing `region` with the appropriate AWS Region.

```
`$` aws ec2 describe-mac-hosts --region `us-east-1``{
 "MacHosts": [
 {
 "HostId": "h-07879acf49EXAMPLE",
 "MacOSLatestSupportedVersions": [
 "14.3",
 "13.6.4",
 "12.7.3"
 ]
 }
 ]`
  }
```
