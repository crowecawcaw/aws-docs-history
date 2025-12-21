# Create a patch maintenance window using CloudFormation for AMS Accelerate

To create an AMS Accelerate patch maintenance window using AWS CloudFormation, first log into your Accelerate account and select the AWS Region
where your target instances reside. Then follow these steps on the [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/"):

1.  Select one of two custom Accelerate patching CloudFormation templates.

        * Patch Tuesday Scheduling: Microsoft releases patches for its operating systems on the second Tuesday of each month, also know as Patch Tuesday, to
         schedule patch maintenance windows on the first or second weekends after Patch Tuesday: Once logged into the Accelerate console, use this link
         [PatchTuesdayScheduling CloudFormation template](https://console.aws.amazon.com/cloudformation/home?#/stacks/create/parameters?templateURL=https://ams-patch-templates-us-east-1.s3.amazonaws.com/AmsPatchMaintenanceWindowTemplatePatchTuesdayScheduling.yml "https://console.aws.amazon.com/cloudformation/home?#/stacks/create/parameters?templateURL=https://ams-patch-templates-us-east-1.s3.amazonaws.com/AmsPatchMaintenanceWindowTemplatePatchTuesdayScheduling.yml")
         .
        * CRON Scheduling: To create patch maintenance windows using CRON to define the start day, use this link
         [CRONScheduling CloudFormation template](https://console.aws.amazon.com/cloudformation/home?#/stacks/create/parameters?templateURL=https://ams-patch-templates-us-east-1.s3.amazonaws.com/AmsPatchMaintenanceWindowTemplateCronScheduling.yml "https://console.aws.amazon.com/cloudformation/home?#/stacks/create/parameters?templateURL=https://ams-patch-templates-us-east-1.s3.amazonaws.com/AmsPatchMaintenanceWindowTemplateCronScheduling.yml").

         Remember that Systems Manager CRON numbers days 1-7 (for details on Systems Manager CRON, see
         [Reference: Cron and rate expressions for Systems Manager](../../../systems-manager/latest/userguide/reference-cron-and-rate-expressions.md "../../../systems-manager/latest/userguide/reference-cron-and-rate-expressions.md")).

    Choosing one of these links causes the template to load automatically on the CloudFormation console. Then click **Next**.

2.  On the **Specify stack details** page (step 2 of the Create Stack pages), enter a stack name and template parameters
    (default parameters shown are AMS recommended defaults, select day and times for your use case). When finished, click **Next**.
3.  Configure Stack Options (Optional). For information on the options, see
    [Setting AWS CloudFormation stack options](../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md").
    When finished, click **Next**.
4.  Review your stack values (Optional). For information on reviewing stack details to estimate costs, see
    [Reviewing your stack and estimating stack cost](../../../AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-review.md "../../../AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-review.md").
    When ready, click **Create stack**.

The stack may take up to a minute to create. Once the stack is created successfully, your patch maintenance window runs at the specified time.
You can make changes to your patch maintenance window by creating and executing a CloudFormation change set (recommended) (for details on doing this, see
[Creating stacks using changesets](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stacks-changesets.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stacks-changesets.md")),
or by updating the patch maintenance window on the Systems Manager **Maintenance window** console
([https://console.aws.amazon.com/systems-manager/maintenance-windows](https://console.aws.amazon.com/systems-manager/maintenance-windows "https://console.aws.amazon.com/systems-manager/maintenance-windows")).
