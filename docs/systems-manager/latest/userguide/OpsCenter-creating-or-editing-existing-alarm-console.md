AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Configuring a CloudWatch alarm to create OpsItems (console)

You can manually create an alarm or update an existing alarm to create OpsItems
from Amazon CloudWatch.

###### To create a CloudWatch alarm and configure Systems Manager as a target of that

alarm

1. Complete steps 1–9 as specified in [Create a CloudWatch alarm based on a
   static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") in the
   _Amazon CloudWatch User Guide_.
2. In the **Systems Manager action** section, choose
   **Add Systems Manager OpsCenter action**.
3. Choose **OpsItems**.
4. For **Severity**, choose from 1 to 4.
5. (Optional) For **Category**, choose a category for
   the OpsItem.
6. Complete steps 11–13 as specified in [Create a CloudWatch alarm based on a
   static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") in the
   _Amazon CloudWatch User Guide_.
7. Choose **Next** and complete the wizard.

###### To edit an existing alarm and configure Systems Manager as a target of that

alarm

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**.
3. Select the alarm, and then choose **Actions**,
   **Edit**.
4. (Optional) Change settings in the **Metrics** and
   **Conditions** sections, and then choose
   **Next**.
5. In the **Systems Manager** section, choose **Add Systems Manager
   OpsCenter action**.
6. For **Severity**, choose a number.

###### Note

Severity is a user-defined value. You or your organization
determine what each severity value means and any service-level
agreement associated with each severity. 7. (Optional) For **Category**, choose an option. 8. Choose **Next** and complete the wizard.
