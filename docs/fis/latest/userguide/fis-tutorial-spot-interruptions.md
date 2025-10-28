# Tutorial: Test Spot Instance interruptions using AWS FIS

Spot Instances use spare EC2 capacity that is available, for up to a 90% discount compared
to On-Demand pricing. However, Amazon EC2 can interrupt your Spot Instances when it needs the
capacity back. When using Spot Instances, you must be prepared for potential interruptions.
For more information, see [Spot Instance
interruptions](../../../AWSEC2/latest/UserGuide/spot-interruptions.md "../../../AWSEC2/latest/UserGuide/spot-interruptions.md") in the _Amazon EC2 User Guide_.

You can use AWS Fault Injection Service (AWS FIS) to test how your applications handle a Spot Instance
interruption. Use this tutorial to create an experiment template that uses the AWS FIS
`aws:ec2:send-spot-instance-interruptions` action to interrupt one of your
Spot Instances.

Alternatively, to initiate the experiment using the Amazon EC2 console, see [Initiate a
Spot Instance interruption](../../../AWSEC2/latest/UserGuide/initiate-a-spot-instance-interruption.md "../../../AWSEC2/latest/UserGuide/initiate-a-spot-instance-interruption.md") in the _Amazon EC2 User Guide_.

## Prerequisites

Before you can use AWS FIS to interrupt a Spot Instance, complete the following
prerequisites.

###### 1. Create an IAM role

Create a role and attach a policy that enables AWS FIS to perform the
`aws:ec2:send-spot-instance-interruptions` action on your behalf. For
more information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").

###### 2. Verify access to AWS FIS

Ensure that you have access to AWS FIS. For more information, see
[AWS FIS policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

###### 3. (Optional) Create a Spot Instance request

If you'd like a new Spot Instance to use for this experiment, use the
[run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command
to request a Spot Instance. The default is to terminate Spot Instances that
are interrupted. If you set the interruption behavior to `stop`, you must
also set the type to `persistent`. For this tutorial, do not set the
interruption behavior to `hibernate`, as the hibernation process begins
immediately.

```
aws ec2 run-instances \
    --image-id `ami-0ab193018fEXAMPLE` \
    --instance-type "`t2.micro`" \
    --count 1 \
    --subnet-id `subnet-1234567890abcdef0` \
    --security-group-ids `sg-111222333444aaab` \
    --instance-market-options file://`spot-options.json` \
    --query Instances[*].InstanceId
```

The following is an example of the `spot-options.json` file.

```
{
    "MarketType": "spot",
    "SpotOptions": {
        "SpotInstanceType": "persistent",
        "InstanceInterruptionBehavior": "stop"
    }
}
```

The `--query` option in the example command makes it so that the command
returns only the instance ID of the Spot Instance. The following is example
output.

```
[
    "i-0abcdef1234567890"
]
```

###### 4. Add a tag so that AWS FIS can identify the target Spot Instance

Use the [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") command
to add the tag Name=interruptMe to your target Spot Instance.

```
aws ec2 create-tags \
    --resources `i-0abcdef1234567890` \
    --tags Key=Name,Value=interruptMe
```

## Step 1: Create an experiment template

Create the experiment template using the AWS FIS console. In the template,
you specify the action that will run. The action interrupts the Spot Instance
with the specified tag. If there is more than one Spot Instance with the tag,
AWS FIS chooses one of them at random.

###### To create an experiment template

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiment
   templates**.
3. Choose **Create experiment template**.
4. For **Step 1, Specify template details**, do the following:
   1. For **Description and name**, enter a description and a name for the template.
   2. Choose **Next**, and move to **Step 2, Specify actions and targets**.

5. For **Actions**, do the following:
   1. Choose **Add action**.
   2. Enter a name for the action. For example, enter
      `interruptSpotInstance`.
   3. For **Action type**, choose
      **aws:ec2:send-spot-instance-interruptions**.
   4. For **Target** keep the target that AWS FIS
      creates for you.
   5. For **Action parameters**, **Duration
      before interruption**, specify 2 Minutes (PT2M).
   6. Choose **Save**.

6. For **Targets**, do the following:
   1. Choose **Edit** for the target that
      AWS FIS automatically created for you in the previous step.
   2. Replace the default name with a more descriptive name. For
      example, enter `oneSpotInstance`.
   3. Verify that **Resource type** is
      **aws:ec2:spot-instance**.
   4. For **Target method**, choose **Resource
      tags, filters, and parameters**.
   5. For **Resource tags**, choose **Add new
      tag**, and enter the tag key and tag value. Use the tag
      that you added to the Spot Instance to interrupt, as described in the
      Prerequisites for this tutorial.
   6. For **Resource filters** choose **Add new
      filter** and enter `State.Name` as the
      path and `running` as the value.
   7. For **Selection mode**, choose
      **Count**. For **Number of
      resources**, enter `1`.
   8. Choose **Save**.

7. Choose **Next** to move to **Step 3, Configure service access**.
8. For **Service Access**, choose **Use an existing
   IAM role**, and then choose the IAM role that you created as
   described in the prerequisites for this tutorial. If your role is not displayed,
   verify that it has the required trust relationship. For more information, see
   [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").
9. Choose **Next** to move to **Step 4, Configure optional settings**.
10. (Optional) For **Tags**, choose **Add new
    tag** and specify a tag key and tag value. The tags that you
    add are applied to your experiment template, not the experiments that are
    run using the template.
11. Choose **Next** to move to **Step 5, Review and create**.
12. Review the template and choose **Create experiment template**.
    When prompted for confirmation, enter `create`, Then choose **Create experiment template**.

###### (Optional) To view the experiment template JSON

Choose the **Export** tab. The following is an example of the
JSON created by the preceding console procedure.

```
{
    "description": "Test Spot Instance interruptions",
    "targets": {
        "oneSpotInstance": {
            "resourceType": "aws:ec2:spot-instance",
            "resourceTags": {
                "Name": "interruptMe"
            },
            "filters": [
                {
                    "path": "State.Name",
                    "values": [
                        "running"
                    ]
                }
            ],
            "selectionMode": "COUNT(1)"
        }
    },
    "actions": {
        "interruptSpotInstance": {
            "actionId": "aws:ec2:send-spot-instance-interruptions",
            "parameters": {
                "durationBeforeInterruption": "PT2M"
            },
            "targets": {
                "SpotInstances": "oneSpotInstance"
            }
        }
    },
    "stopConditions": [
        {
            "source": "none"
        }
    ],
    "roleArn": "arn:aws:iam::`123456789012`:role/`AllowFISSpotInterruptionActions`",
    "tags": {
        "Name": "my-template"
    }
}
```

## Step 2: Start the experiment

When you have finished creating your experiment template, you can use it to start
an experiment.

###### To start an experiment

1. You should be on the details page for the experiment template that you just
   created. Otherwise, choose **Experiment templates** and then
   select the ID of the experiment template to open the details page.
2. Choose **Start experiment**.
3. (Optional) To add a tag to your experiment, choose **Add new
   tag** and enter a tag key and a tag value.
4. Choose **Start experiment**. When prompted for confirmation,
   enter `start` and choose **Start experiment**.

## Step 3: Track the experiment progress

You can track the progress of a running experiment until the experiment is
completed, stopped, or failed.

###### To track the progress of an experiment

1. You should be on the details page for the experiment that you just started.
   Otherwise, choose **Experiments** and then select the ID of the
   experiment to open the details page.
2. To view the state of the experiment, check **State** in the
   **Details** pane. For more information, see [experiment states](view-experiment-progress.md#experiment-states "view-experiment-progress.md#experiment-states").
3. When the state of the experiment is **Running**, go to the
   next step.

## Step 4: Verify the experiment result

When the action for this experiment is completed, the following occurs:

- The target Spot Instance receives an [instance rebalance recommendation](../../../AWSEC2/latest/UserGuide/rebalance-recommendations.md "../../../AWSEC2/latest/UserGuide/rebalance-recommendations.md").
- A [Spot Instance interruption notice](../../../AWSEC2/latest/UserGuide/spot-interruptions.md#spot-instance-termination-notices "../../../AWSEC2/latest/UserGuide/spot-interruptions.md#spot-instance-termination-notices") is issued two minutes before Amazon EC2
  terminates or stops your instance.
- After two minutes, the Spot Instance is terminated or stopped.
- A Spot Instance that was stopped by AWS FIS remains stopped until you restart
  it.

###### To verify that the instance was interrupted by the experiment

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation pane, open **Spot Requests** and
   **Instances** in separate browser tabs or windows.
3. For **Spot Requests**, select the Spot Instance request.
   The initial status is `fulfilled`. After the experiment completes,
   the status changes as follows:
   - `terminate` - The status changes to
     `instance-terminated-by-experiment`.
   - `stop` - The status changes to
     `marked-for-stop-by-experiment` and then
     `instance-stopped-by-experiment`.

4. For **Instances**, select the Spot Instance. The initial
   status is `Running`. Two minutes after you receive the Spot Instance
   interruption notice, the status changes as follows:
   - `stop` - The status changes to `Stopping` and then
     `Stopped`.
   - `terminate` - The status changes to `Shutting-down`
     and then `Terminated`.

## Step 5: Clean up

If you created the test Spot Instance for this experiment with an interruption
behavior of `stop` and you no longer need it, you can cancel the Spot
Instance request and terminate the Spot Instance.

###### To cancel the request and terminate the instance using the AWS CLI

1. Use the [cancel-spot-instance-requests](../../../cli/latest/reference/ec2/cancel-spot-instance-requests.md "../../../cli/latest/reference/ec2/cancel-spot-instance-requests.md") command to cancel the Spot Instance
   request.

```
`aws ec2 cancel-spot-instance-requests --spot-instance-request-ids `sir-ksie869j``
```

2. Use the [terminate-instances](../../../cli/latest/reference/ec2/terminate-instances.md "../../../cli/latest/reference/ec2/terminate-instances.md") command to terminate the instance.

```
`aws ec2 terminate-instances --instance-ids `i-0abcdef1234567890``
```

If you no longer need the experiment template, you can delete it.

###### To delete an experiment template using the AWS FIS console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiment
   templates**.
3. Select the experiment template, and choose **Actions**,
   **Delete experiment template**.
4. When prompted for confirmation, enter `delete` and
   then choose **Delete experiment template**.
