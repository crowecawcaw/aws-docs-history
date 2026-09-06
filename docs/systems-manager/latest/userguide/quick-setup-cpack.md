

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Deploy AWS Config conformance pack using Quick Setup
<a name="quick-setup-cpack"></a>

A conformance pack is a collection of AWS Config rules and remediation actions. With Quick Setup, you can deploy a conformance pack as a single entity in an account and an AWS Region or across an organization in AWS Organizations. This helps you manage configuration compliance of your AWS resources at scale, from policy definition to auditing and aggregated reporting, by using a common framework and packaging model. 

To deploy conformance packs, perform the following tasks in the AWS Systems Manager Quick Setup console.

**Note**  
You must enable AWS Config recording before deploying this configuration. For more information, see [Conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) in the *AWS Config Developer Guide*.

**To deploy conformance packs with Quick Setup**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Quick Setup**.

1. On the **Conformance Packs** card, choose **Create**.
**Tip**  
If you already have one or more configurations in your account, first choose the **Library** tab or the **Create** button in the **Configurations** section to view the cards.

1. In the **Choose conformance packs** section, choose the conformance packs you want to deploy.

1. In the **Schedule** section, choose how frequently you want Quick Setup to remediate changes made to resources that differ from your configuration. The **Default** option runs once. If you don't want Quick Setup to remediate changes made to resources that differ from your configuration, choose **Disabled** under **Custom**.

1. In the **Targets** section, choose whether to deploy conformance packs to your entire organization, some AWS Regions, or the account you're currently logged in to.

   If you choose **Entire organization**, continue to step 8.

   If you choose **Custom**, continue to step 7.

1. In the **Target Regions** section, select the check boxes of the Regions you want to deploy conformance packs to.

1. Choose **Create**.