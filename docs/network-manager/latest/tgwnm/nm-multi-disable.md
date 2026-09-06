

# Disable trusted access in an AWS global network
<a name="nm-multi-disable"></a>

 Disabling trusted access removes the trust relationship between the Network Manager service access and your organization. Network Manager is no longer able to perform actions within your organization or access information about your organization. Trusted access remains for CloudFormation StackSets in the event that your organization is using that service outside of Network Manager. For more information on disabling CloudFormation StackSets, see [Disabling trusted access with AWS CloudFormation Stacksets](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html#integrate-disable-ta-cloudformation) in the *AWS Organizations User Guide*.

Transit gateways from other accounts are deregistered from global networks owned by the management account and can no longer provide access to their attached resources. For more information about disabling trusted access, see [Disable trusted access](nm-multi-account.md#nm-how-it-works-disable).

You must first deregister all delegated administrators before you can disable trusted access. If you have registered delegated administrators, you will be prompted to deregister them during the disable trusted access process.

You can enable trusted access again after disabling it. However you will need to set up the list of delegated administrators again. 

**To disable trusted access**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home) with the management account.

1. Under **Connectivity**, choose **Global Networks**.

1. In the navigation pane, choose **Settings**.

1. In the **Trusted Access** section, choose **Disable trusted access**.

1. If you have any registered delegated administrators, you can deregister them by choosing **Deregister delegated administrators**.

1. Choose **Disable trusted access** on the confirmation dialog box to confirm that you want to disable trusted access. 

   Depending on the size of your organization, it might take several minutes or longer to disable trusted access. The **State** displays **Disabling in progress**. During this time you won't be able to re-enable trusted access. When finished, the Status changes to **Disabled**.