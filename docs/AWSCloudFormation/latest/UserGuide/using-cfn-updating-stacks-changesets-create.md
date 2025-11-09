# Create a change set for a CloudFormation stack

To create a change set for a running stack, submit the changes that you want to make by
providing a modified template, new input parameter values, or both. CloudFormation generates a
change set by comparing your stack with the changes you submitted.

You can either modify a template before creating the change set or during change set
creation.

Create a change set (console)

###### To create a change set

1. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. On the **Stacks** page, choose the running stack you want to
   create a change set for.
4. In the stack details pane, choose **Stack actions**, and then
   choose **Create a change set**.
5. On the **Create change set for
   `stack-name`** page, do one of the following to
   modify input parameter values, specify the location of an updated template, or
   modify the template:

| Task                                           | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| To modify input parameter values               | Choose **Use existing template**, and then choose<br>\*_Next_<br>• to proceed to enter or modify input parameter<br>values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| To specify the location of an updated template | If you've modified the template, choose **Replace existing<br>template**, and then do one of the following:<br>• For a template stored in an Amazon S3 bucket, choose **Amazon S3<br>URL**. Enter or paste the URL for the template, and then<br>choose **Next**.<br>If you have a template in a versioning-enabled bucket, you can<br>specify a specific version of the template by appending<br>`?versionId=`version-id`` to<br>the URL. For more information, see [Working with<br>objects in a versioning-enabled bucket](../../../AmazonS3/latest/userguide/manage-objects-versioned-bucket.md "../../../AmazonS3/latest/userguide/manage-objects-versioned-bucket.md") in the<br>_Amazon Simple Storage Service User Guide_.<br>• For a template stored locally on your computer, choose<br>**Upload a template file**. Choose **Choose<br>File\*<br>• to navigate to the file and select it, and then<br>choose **Next\*\*. |
| To modify the template                         | If you haven't modified the template, choose **Edit template in<br>Infrastructure Composer**, and then choose **Edit in Infrastructure Composer**.<br>You're redirected to the AWS Infrastructure Composer. Once you've modified the template,<br>choose **Create change set\*<br>• and then **Confirm and<br>continue to CloudFormation*<br>• to return to the \*\*Create change<br>set for `stack-name`*<br>• page, and then<br>choose **Next**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

6. On the **Specify stack details** page, specify a name for the
   change set and optionally specify a description of the change set to identify its
   purpose in the **Overview** section. If your template contains
   parameters, on the **Specify stack details** page, enter or modify
   applicable input parameter values, and then choose **Next**.

If you're reusing the stack's template, CloudFormation populates each parameter with
the current value in the stack, with the exception of parameters declared with the
`NoEcho` attribute. To use existing values for those parameters, select
**Use existing value**.

For more information about using `NoEcho` to mask sensitive
information, and using dynamic parameters to manage secrets, see the [Do not embed credentials in your templates](security-best-practices.md#creds "security-best-practices.md#creds") best practice. 7. On the **Configure stack options** page, update the stack's
tags, IAM service role, stack policy, rollback configuration, Amazon SNS notification
topic (if applicable), or change sets.

###### Note

Change sets for nested stacks are **Enabled** by default,
which will create change sets for all nested stacks specified in your template. To
create a change set for the current stack only, choose
**Disabled**. For more information about change sets for nested
stacks, see [Change sets for nested stacks](change-sets-for-nested-stacks.md "change-sets-for-nested-stacks.md"). 8. If the template includes IAM resources, for **Capabilities**,
choose **I acknowledge that CloudFormation might create IAM
resources**. IAM resources can modify permissions in your AWS
account; review these resources to ensure that you're permitting only the actions
that you intend. For more information, see [Acknowledging IAM resources in CloudFormation
templates](control-access-with-iam.md#using-iam-capabilities "control-access-with-iam.md#using-iam-capabilities"). 9. Choose **Next** to continue. 10. On the **Review `stack-name`** page,
review the changes for this change set. 11. Choose **Submit**.

You're redirected to the **Changes** tab of the change set's
details page. While CloudFormation generates the change set, the status of the change
set is `CREATE_PENDING`. After it has created the change set, CloudFormation
sets the status to `CREATE_COMPLETE`. In the **Changes**
section, CloudFormation lists all of the changes that it will make to your stack. For
more information, see [View a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-view.md "using-cfn-updating-stacks-changesets-view.md").

Choose **View details** in the **Property-level
changes** column to view changes made at the property-level.

If CloudFormation fails to create the change set (reports `FAILED`
status), fix the error displayed in the **Status** field, and then
recreate the change set. 12. After confirming the changes look correct, choose **Execute change
set**

Create a change set for nested stacks (console)

###### To create a change set for nested stacks

1. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. On the **Stacks** page, select the running stack you want to
   create a change set for.
4. In the stack details pane, choose **Stack actions**, and then
   choose **Create a change set**.
5. On the **Create change set for
   `stack-name`** page, do one of the following to
   modify input parameter values, specify the location of an updated template, or
   modify the template:

| Task                                           | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| To modify input parameter values               | Choose **Use existing template**, and then choose<br>\*_Next_<br>• to proceed to enter or modify input parameter<br>values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| To specify the location of an updated template | If you've modified the template, choose **Replace existing<br>template**, and then do one of the following:<br>• For a template stored in an Amazon S3 bucket, choose **Amazon S3<br>URL**. Enter or paste the URL for the template, and then<br>choose **Next**.<br>If you have a template in a versioning-enabled bucket, you can<br>specify a specific version of the template by appending<br>`?versionId=`version-id`` to<br>the URL. For more information, see [Working with<br>objects in a versioning-enabled bucket](../../../AmazonS3/latest/userguide/manage-objects-versioned-bucket.md "../../../AmazonS3/latest/userguide/manage-objects-versioned-bucket.md") in the<br>_Amazon Simple Storage Service User Guide_.<br>• For a template stored locally on your computer, choose<br>**Upload a template file**. Choose **Choose<br>File\*<br>• to navigate to the file and select it, and then<br>choose **Next\*\*. |
| To modify the template                         | If you haven't modified the template, choose **Edit template in<br>Infrastructure Composer**, and then choose **Edit in Infrastructure Composer**.<br>You're redirected to the AWS Infrastructure Composer. Once you've modified the template,<br>choose **Create change set\*<br>• and then **Confirm and<br>continue to CloudFormation*<br>• to return to the \*\*Create change<br>set for `stack-name`*<br>• page, and then<br>choose **Next**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

6. On the **Specify stack details** page, specify a name for the
   change set and optionally specify a description of the change set to identify its
   purpose in the **Overview** section. If your template contains
   parameters, on the **Specify stack details** page, enter or modify
   applicable input parameter values, and then choose **Next**.

If you're reusing the stack's template, CloudFormation populates each parameter with
the current value in the stack, with the exception of parameters declared with the
`NoEcho` attribute. To use existing values for those parameters, select
**Use existing value**.

For more information about using `NoEcho` to mask sensitive
information, as well as using dynamic parameters to manage secrets, see the [Do not embed credentials in your templates](security-best-practices.md#creds "security-best-practices.md#creds") best practice. 7. On the **Configure stack options** page, update the stack's
tags, IAM service role, stack policy, rollback configuration, Amazon SNS notification
topic (if applicable), or change sets. For more information, see [Configure stack options](cfn-console-create-stack.md#configure-stack-options "cfn-console-create-stack.md#configure-stack-options").

###### Note

Change sets for nested stacks are **Enabled** by default,
which will create change sets for all nested stacks specified in your template.
For more information about change sets for nested stacks, see [Change sets for nested stacks](change-sets-for-nested-stacks.md "change-sets-for-nested-stacks.md"). 8. If the template includes IAM resources, for **Capabilities**,
choose **I acknowledge that CloudFormation might create IAM
resources**. IAM resources can modify permissions in your AWS
account; review these resources to ensure that you're permitting only the actions
that you intend. For more information, see [Acknowledging IAM resources in CloudFormation
templates](control-access-with-iam.md#using-iam-capabilities "control-access-with-iam.md#using-iam-capabilities"). 9. Choose **Next** to continue. 10. On the **Review `stack-name`** page,
review the changes for this change set. 11. Choose **Submit**.

###### Note

CloudFormation property-level change sets does not resolve cross-stack references
when you create change sets for nested stacks. Change sets can mark resources in
a child stack for conditional replacement if they reference the output of a parent
stack, and the parent stack has been modified

You're redirected to the **Changes** tab of the change set's
details page. While CloudFormation generates the change set, the status of the change
set is `CREATE_PENDING`. After it has created the change set, CloudFormation
sets the status to `CREATE_COMPLETE`. In the **Changes**
section, CloudFormation lists all of the changes that it will make to your stack. For
more information, see [View a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-view.md "using-cfn-updating-stacks-changesets-view.md").

If CloudFormation fails to create the change set (reports `FAILED`
status), fix the error displayed in the **Status** field, and then
recreate the change set. 12. After confirming the changes look correct, choose **Execute change
set**

###### To create a change set (AWS CLI)

- Use the [create-change-set](../../../cli/latest/reference/cloudformation/create-change-set.md "../../../cli/latest/reference/cloudformation/create-change-set.md") command.

You submit your changes as command options. You can specify new parameter values, a
modified template, or both. For example, the following command creates a change set named
`SampleChangeSet` for the `MyStack` stack. The change set uses
the current stack's template, but with a different value for the `Purpose`
parameter:

```
aws cloudformation create-change-set --stack-name `MyStack` \
    --change-set-name `SampleChangeSet` --use-previous-template \
    --parameters \
      `ParameterKey="InstanceType",UsePreviousValue=true ParameterKey="KeyPairName",UsePreviousValue=true ParameterKey="Purpose",ParameterValue="production"`
```
