# Create an experiment template

Before you begin, complete the following tasks:

- [Plan your experiment](getting-started-planning.md "getting-started-planning.md").
- Create an IAM role that grants the AWS FIS service permission to
  perform actions on your behalf. For more information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").
- Ensure that you have access to AWS FIS. For more information, see
  [AWS FIS
  policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

###### To create an experiment template using the console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiment
   templates**.
3. Choose **Create experiment template**.
4. For **Step 1, Specify template details**, do the following:
   1. For **Description and name**, enter a description for the template, such as `Amazon S3 Network Disrupt
Connectivity`.
   2. (Optional) For **Account targeting**, choose **Multiple accounts**
      to configure a multi-account experiment template.
   3. Choose **Next**, and move to **Step 2, Specify actions and targets**.

5. For **Actions**, specify the set of actions for the
   template. For each action, choose **Add action** and complete
   the following:
   - For **Name**, enter a name for the action.

   Allowed characters are alphanumeric characters, hyphens (-), and
   underscores(\_). The name must start with a letter. No spaces are
   allowed. Each action name must be unique in this template.
   - (Optional) For **Description**, enter a
     description for the action. The maximum length is 512
     characters.
   - (Optional) For **Start after**, select another
     action defined in this template that must be completed before the
     current action starts. Otherwise, the action runs at the start of
     the experiment.
   - For **Action type**, choose the AWS FIS
     action.
   - For **Target**, choose a target that you defined
     in the **Targets** section. If you haven't defined
     a target for this action yet, AWS FIS creates a new target for
     you.
   - For **Action parameters**, specify the parameters
     for the action. This section appears only if the AWS FIS action has
     parameters.
   - Choose **Save**.

6. For **Targets**, define the target resources on which to
   carry out the actions. You must specify at least one resource ID or one
   resource tag as a target. Choose **Edit** to edit the
   target that AWS FIS created for you in the previous step, or choose
   **Add target**. For each target, do the
   following:
   - For **Name**, enter a name for the
     target.

   Allowed characters are alphanumeric characters, hyphens (-), and
   underscores(\_). The name must start with a letter. No spaces are
   allowed. Each target name must be unique in this template.
   - For **Resource type**, choose a resource type
     that is supported for the action.
   - For **Target method**, do one of the
     following:
     - Choose **Resource IDs** and then choose or add
       the resource IDs.
     - Choose **Resource tags, filters, and
       parameters** and then add the tags and filters
       that you need. For more information, see [Identify target resources](targets.md#target-identification "targets.md#target-identification").

   - For **Selection mode**, choose
     **Count** to run the action on the specified
     number of identified targets or choose **Percent**
     to run the action on the specified percentage of identified targets.
     By default, the action runs on all identified targets.
   - Choose **Save**.

7. To update an action with the target that you created, find the action under
   **Actions**, choose **Edit**, and then update
   **Target**. You can use the same target for multiple actions.
8. (Optional) For **experiment options**, select the behavior of the empty target resolution mode.
9. Choose **Next** to move to **Step 3, Configure service access**.
10. For **Service Access**, choose **Use an existing
    IAM role**, and then choose the IAM role that you created as
    described in the prerequisites for this tutorial. If your role is not
    displayed, verify that it has the required trust relationship. For more
    information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").
11. (Multi-account experiments only) For **Target account configurations**,
    add a Role ARN and optional description for each target account. To upload the target account role ARNs
    with a CSV file, choose **Upload role ARNs for all target accounts** and then choose
    **Choose .CSV file**
12. Choose **Next** to move to **Step 4, Configure optional settings**.
13. (Optional) For **Stop conditions**, select the Amazon CloudWatch
    alarms for the stop conditions. For more information, see [Stop conditions for AWS FIS](stop-conditions.md "stop-conditions.md").
14. (Optional) For **Logs**, configure the destination option.
    To send logs to an S3 bucket, choose **Send to an Amazon S3
    bucket** and enter the bucket name and prefix. To send logs to
    CloudWatch Logs, choose **Send to CloudWatch Logs** and enter the log
    group.
15. (Optional) For **Tags**, choose **Add new
    tag** and specify a tag key and tag value. The tags that you
    add are applied to your experiment template, not the experiments that are
    run using the template.
16. Choose **Next** to move to **Step 5, Review and create**.
17. Review the template and choose **Create experiment template**.
    When prompted for confirmation, enter `create`, Then choose **Create experiment template**.

###### To create an experiment template using the CLI

Use the [create-experiment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html")
command.

You can load an experiment template from a JSON file.

Use the `--cli-input-json` parameter.

```
aws fis create-experiment-template --cli-input-json fileb://`<path-to-json-file>`
```

For more information, see [Generating a CLI skeleton template](../../../cli/latest/userguide/cli-usage-skeleton.md "../../../cli/latest/userguide/cli-usage-skeleton.md") in the
_AWS Command Line Interface User Guide_. For example templates, see [Example AWS FIS experiment templates](experiment-template-example.md "experiment-template-example.md").
