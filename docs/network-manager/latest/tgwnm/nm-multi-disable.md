# Disable trusted access in an AWS global network

Disabling trusted access removes the trust relationship between the Network Manager service
access and your organization. Network Manager is no longer able to perform actions within your
organization or access information about your organization. Trusted access remains for AWS CloudFormation
StackSets in the event that your organization is using that service outside of Network Manager. For
more information on disabling AWS CloudFormation StackSets, see [Disabling trusted access with AWS CloudFormation Stacksets](../../../organizations/latest/userguide/services-that-can-integrate-cloudformation.md#integrate-disable-ta-cloudformation "../../../organizations/latest/userguide/services-that-can-integrate-cloudformation.md#integrate-disable-ta-cloudformation") in the _AWS Organizations User
Guide_.

Transit gateways from other accounts are deregistered from global networks owned by the
management account and can no longer provide access to their attached resources. For more
information about disabling trusted access, see [Disable trusted access](nm-multi-account.md#nm-how-it-works-disable "nm-multi-account.md#nm-how-it-works-disable").

You must first deregister all delegated administrators before you can disable trusted
access. If you have registered delegated administrators, you will be prompted to deregister
them during the disable trusted access process.

You can enable trusted access again after disabling it. However you will need to set up
the list of delegated administrators again.

###### To disable trusted access

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home") with the management account.
2. Under **Connectivity**, choose **Global Networks**.
3. In the navigation pane, choose **Settings**.
4. In the **Trusted Access** section, choose **Disable trusted
   access**.
5. If you have any registered delegated administrators, you can deregister them by
   choosing **Deregister delegated administrators**.
6. Choose **Disable trusted access** on the confirmation dialog box to
   confirm that you want to disable trusted access.

Depending on the size of your organization, it might take several minutes or longer to
disable trusted access. The **State** displays **Disabling in
progress**. During this time you won't be able to re-enable trusted access.
When finished, the Status changes to **Disabled**.
