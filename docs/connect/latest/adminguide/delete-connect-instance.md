# Delete your Amazon Connect instance

If you no longer need your Amazon Connect instance, you can delete it. Here's what happens when
you delete it:

- Its claimed phone number is released back to inventory.
- When customers call the phone number that you've released, they'll get a
  message that it's not a working phone number.

## Important things to know

- You can't restore a deleted Amazon Connect instance or access its settings, data,
  metrics, and reports.
- Due to GDPR compliance, scheduling data is retained for 30 days and you
  are be billed for usage during this time. For information about GDPR
  compliance and Amazon Connect forecasting, capacity planning, and scheduling, see this [FAQ](https://aws.amazon.com/connect/optimization/#topic-0 "https://aws.amazon.com/connect/optimization/#topic-0").
- If you have [enabled Amazon Connect flow
  logging](contact-flow-logs.md "contact-flow-logs.md"), you need to delete the CloudWatch log groups manually if they
  are no longer needed. You can do this by using the CloudWatch console. For
  programmatic instructions, see [Use DeleteLogGroup with an AWS SDK or
  CLI](../../../AmazonCloudWatch/latest/logs/example_cloudwatch-logs_DeleteLogGroup_section.md "../../../AmazonCloudWatch/latest/logs/example_cloudwatch-logs_DeleteLogGroup_section.md").

## Delete your instance

You must have the appropriate AWS permissions to delete an Amazon Connect. If your
organization is using IAM, see [Required permissions for using
custom IAM policies to manage access to the Amazon Connect console](security-iam-amazon-connect-permissions.md "security-iam-amazon-connect-permissions.md").

1. Open the Amazon Connect console at
   [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/").
2. Select the radio button for the instance.
3. Choose **Delete**.
   If you don't see the
   **Delete** button, you don't have permissions to delete
   instances. Contact your AWS administrator for help.

![The Amazon Connect virtual contact center instances page, the delete button.](images/instance-delete.png) 4. When prompted, enter the name of the instance and then choose
**Delete**.

## Error message: "Region Unsupported. Amazon Connect is

not available in [Region]"

If you get this error message, it means that you selected a Region in the
AWS Management Console that is not the Region in which you created the Amazon Connect instance, and Amazon Connect
isn't available in that Region.

###### To switch Regions and delete your Amazon Connect instance

1. From the navigation bar, open the Region selector. Select the Region in
   which you created the Amazon Connect instance.

![The list of Regions in the Region selector.](images/aws-management-console-region.png) 2. From the navigation bar, choose **Amazon Connect** from the list
of services to open the Amazon Connect console. If you don't see the instance, keep
selecting from the supported Regions until you find your instance. 3. Select the radio button for the instance. 4. Choose **Delete**.
If you don't see the
**Delete** button, you don't have permissions to delete
instances. Contact your AWS administrator for help. 5. When prompted, enter the name of the instance and then choose
**Delete**.
