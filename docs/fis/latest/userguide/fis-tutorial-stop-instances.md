# Tutorial: Test instance stop and start using AWS FIS

You can use AWS Fault Injection Service (AWS FIS) to test how your applications handle instance stop and
start. Use this tutorial to create an experiment template that uses the AWS FIS
`aws:ec2:stop-instances` action to stop one instance and then a second
instance.

## Prerequisites

To complete this tutorial, ensure that you do the following:

- Launch two test EC2 instances in your account. After you launch your
  instances, note the IDs of both instances.
- Create an IAM role that enables the AWS FIS service to perform the
  `aws:ec2:stop-instances` action on your behalf. For more
  information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").
- Ensure that you have access to AWS FIS. For more information, see
  [AWS FIS policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Step 1: Create an experiment template

Create the experiment template using the AWS FIS console. In the template,
you specify two actions that will run sequentially for three minutes each. The first
action stops one of the test instances, which AWS FIS chooses randomly. The
second action stops both test instances.

###### To create an experiment template

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiment templates**.
3. Choose **Create experiment template**.
4. For **Step 1, Specify template details**, do the following:
   1. For **Description and name**, enter a description for the template, such as `Amazon S3 Network Disrupt
Connectivity`.
   2. Choose **Next**, and move to **Step 2, Specify actions and targets**.

5. For **Actions**, do the following:
   1. Choose **Add action**.
   2. Enter a name for the action. For example, enter
      `stopOneInstance`.
   3. For **Action type**, choose
      **aws:ec2:stop-instances**.
   4. For **Target** keep the target that AWS FIS
      creates for you.
   5. For **Action parameters**, **Start
      instances after duration**, specify 3 minutes
      (PT3M).
   6. Choose **Save**.

6. For **Targets**, do the following:
   1. Choose **Edit** for the target that AWS FIS
      automatically created for you in the previous step.
   2. Replace the default name with a more descriptive name. For
      example, enter `oneRandomInstance`.
   3. Verify that **Resource type** is
      **aws:ec2:instance**.
   4. For **Target method**, choose **Resource
      IDs**, and then choose the IDs of the two test instances.
   5. For **Selection mode**, choose
      **Count**. For **Number of
      resources**, enter `1`.
   6. Choose **Save**.

7. Choose **Add target** and do the following:
   1. Enter a name for the target. For example, enter
      `bothInstances`.
   2. For **Resource type**, choose
      **aws:ec2:instance**.
   3. For **Target method**, choose **Resource
      IDs**, and then choose the IDs of the two test instances.
   4. For **Selection mode**, choose
      **All**.
   5. Choose **Save**.

8. From the **Actions** section, choose **Add
   action**. Do the following:
   1. For **Name**, enter a name for the action. For
      example, enter `stopBothInstances`.
   2. For **Action type**, choose
      **aws:ec2:stop-instances**.
   3. For **Start after**, choose the first action
      that you added (`stopOneInstance`).
   4. For **Target**, choose the second target
      that you added (`bothInstances`).
   5. For **Action parameters**, **Start
      instances after duration**, specify 3 minutes
      (PT3M).
   6. Choose **Save**.

9. Choose **Next** to move to **Step 3, Configure service access**.
10. For **Service Access**, choose **Use an existing
    IAM role**, and then choose the IAM role that you created as
    described in the prerequisites for this tutorial. If your role is not displayed,
    verify that it has the required trust relationship. For more information, see
    [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").
11. Choose **Next** to move to **Step 4, Configure optional settings**.
12. (Optional) For **Tags**, choose **Add new
    tag** and specify a tag key and tag value. The tags that you
    add are applied to your experiment template, not the experiments that are
    run using the template.
13. Choose **Next** to move to **Step 5, Review and create**.
14. Review the template and choose **Create experiment template**.
    When prompted for confirmation, enter `create`, Then choose **Create experiment template**.

###### (Optional) To view the experiment template JSON

Choose the **Export** tab. The following is an example of
the JSON created by the preceding console procedure.

```
{
    "description": "Test instance stop and start",
    "targets": {
        "bothInstances": {
            "resourceType": "aws:ec2:instance",
            "resourceArns": [
                "arn:aws:ec2:`region`:`123456789012`:instance/`instance_id_1`",
                "arn:aws:ec2:`region`:`123456789012`:instance/`instance_id_2`"
            ],
            "selectionMode": "ALL"
        },
        "oneRandomInstance": {
            "resourceType": "aws:ec2:instance",
            "resourceArns": [
                "arn:aws:ec2:`region`:`123456789012`:instance/`instance_id_1`",
                "arn:aws:ec2:`region`:`123456789012`:instance/`instance_id_2`"
            ],
            "selectionMode": "COUNT(1)"
        }
    },
    "actions": {
        "stopBothInstances": {
            "actionId": "aws:ec2:stop-instances",
            "parameters": {
                "startInstancesAfterDuration": "PT3M"
            },
            "targets": {
                "Instances": "bothInstances"
            },
            "startAfter": [
                "stopOneInstance"
            ]
        },
        "stopOneInstance": {
            "actionId": "aws:ec2:stop-instances",
            "parameters": {
                "startInstancesAfterDuration": "PT3M"
            },
            "targets": {
                "Instances": "oneRandomInstance"
            }
        }
    },
    "stopConditions": [
        {
            "source": "none"
        }
    ],
    "roleArn": "arn:aws:iam::`123456789012`:role/`AllowFISEC2Actions`",
    "tags": {}
}
```

## Step 2: Start the experiment

When you have finished creating your experiment template, you can use it to start
an experiment.

###### To start an experiment

1. You should be on the details page for the experiment template that you
   just created. Otherwise, choose **Experiment templates** and
   then select the ID of the experiment template to open the details page.
2. Choose **Start experiment**.
3. (Optional) To add a tag to your experiment, choose **Add new
   tag** and enter a tag key and a tag value.
4. Choose **Start experiment**. When prompted for
   confirmation, enter `start` and choose **Start
   experiment**.

## Step 3: Track the experiment progress

You can track the progress of a running experiment until the experiment is
completed, stopped, or failed.

###### To track the progress of an experiment

1. You should be on the details page for the experiment that you just
   started. Otherwise, choose **Experiments** and then select the
   ID of the experiment to open the details page.
2. To view the state of the experiment, check **State** in the
   **Details** pane. For more information, see [experiment states](view-experiment-progress.md#experiment-states "view-experiment-progress.md#experiment-states").
3. When the state of the experiment is **Running**, go to
   the next step.

## Step 4: Verify the experiment result

You can verify that the instances were stopped and started by the experiment as
expected.

###### To verify the result of the experiment

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/") in a new browser tab or window. This
   allows you to continue to track the progress of the experiment in the AWS FIS
   console while viewing the result of the experiment in the Amazon EC2 console.
2. In the navigation pane, choose **Instances**.
3. When the state of the first action changes from **Pending** to
   **Running** (AWS FIS console), the state of one of the target instances
   changes from **Running** to **Stopped** (Amazon EC2 console).
4. After three minutes, the state of the first action changes to **Completed**,
   the state of the second action changes to **Running**, and the state of the
   other target instance changes to **Stopped**.
5. After three minutes, the state of the second action changes to **Completed**,
   the state of the target instances changes to **Running**, and the
   state of the experiment changes to **Completed**.

## Step 5: Clean up

If you no longer need the test EC2 instances that you created for this experiment,
you can terminate them.

###### To terminate the instances

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select both test instances and choose **Instance state**,
   **Terminate instance**.
4. When prompted for confirmation, choose **Terminate**.

If you no longer need the experiment template, you can delete it.

###### To delete an experiment template using the AWS FIS console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiment
   templates**.
3. Select the experiment template, and choose **Actions**,
   **Delete experiment template**.
4. When prompted for confirmation, enter `delete` and
   then choose **Delete experiment template**.
