• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Create an AWS Config configuration recorder

using Quick Setup

With Quick Setup, a tool in AWS Systems Manager, you can quickly create a configuration
recorder powered by AWS Config. Use the configuration recorder to detect changes in your
resource configurations and capture the changes as configuration items. If you're
unfamiliar with AWS Config, we recommend learning more about the service by reviewing the
content in the _AWS Config Developer Guide_ before creating a
configuration with Quick Setup. For more information about AWS Config, see [What
is AWS Config?](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") in the _AWS Config Developer Guide_.

By default, the configuration recorder records all supported resources in the
AWS Region where AWS Config is running. You can customize the configuration so that only
the resource types you specify are recorded. For more information, see [Selecting which resources AWS Config records](../../../config/latest/developerguide/select-resources.md "../../../config/latest/developerguide/select-resources.md") in the
_AWS Config Developer Guide_.

You're charged service usage fees when AWS Config starts recording configurations. For
pricing information, see [AWS Config
pricing](https://aws.amazon.com/config/pricing/ "https://aws.amazon.com/config/pricing/").

###### Note

If you've already created a configuration recorder, Quick Setup doesn't stop
recording or make any changes to resource types that you're already recording.
If you choose to record additional resource types using Quick Setup, the service
appends them to your existing recorder groups. Deleting the Quick Setup
**Config recording** configuration type doesn't stop the
configuration recorder. Changes continue to be recorded, and service usage fees
apply until you stop the configuration recorder. To learn more about managing
the configuration recorder, see [Managing the
Configuration Recorder](../../../config/latest/developerguide/stop-start-recorder.md "../../../config/latest/developerguide/stop-start-recorder.md") in the
_AWS Config Developer Guide_.

To set up AWS Config recording, perform the following tasks in the AWS Systems Manager
console.

###### To set up AWS Config recording with Quick Setup

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Quick Setup**.
3. On the **Config Recording** card, choose
   **Create**.

###### Tip

If you already have one or more configurations in your account, first
choose the **Library** tab or the
**Create** button in the
**Configurations** section to view the
cards. 4. In the **Configuration options** section, do the
following:

    1. For **Choose the AWS resource types to
     record**, specify whether to record all supported resources
     or only the resource types you choose.
    2. For **Delivery settings, specify whether to create a new
     Amazon Simple Storage Service (Amazon S3) bucket, or choose an existing bucket to send
     configuration snapshots to.**
    3. For **Notification options**, choose the
     notification option you prefer. AWS Config uses Amazon Simple Notification Service (Amazon SNS) to
     notify you about important AWS Config events related to your resources. If
     you choose the **Use existing SNS topics** option,
     you must provide the AWS account ID and name of the existing Amazon SNS
     topic in that account you want to use. If you target multiple
     AWS Regions, the topic names must be identical in each
     Region.

5. In the **Schedule** section, choose how frequently you
   want Quick Setup to remediate changes made to resources that differ from your
   configuration. The **Default** option runs once. If you
   don't want Quick Setup to remediate changes made to resources that differ from
   your configuration, choose **Disable remediation** under
   **Custom**.
6. In the **Targets** section, choose one of the following
   to identify the accounts and Regions for recording.

###### Note

If you are working in a single account, options for working with
organizations and organizational units (OUs) are not available. You can
choose whether to apply this configuration to all AWS Regions in your
account or only the Regions you select.

    * **Entire organization** – All accounts and
     Regions in your organization.
    * **Custom** – Only the OUs and Regions that
     you specify.




    	+ In the **Target OUs** section, select the
    	 OUs where you want to allow recording.
    	+ In the **Target Regions** section, select
    	 the Regions where you want to allow recording.
    * **Current account** – Only the Regions you
     specify in the account you are currently signed into are targeted.
     Choose one of the following:




    	+ **Current Region** – Only managed
    	 nodes in the Region selected in the console are targeted.
    	+ **Choose Regions** – Choose the
    	 individual Regions to apply the recording configuration
    	 to.

7. Choose **Create**.
