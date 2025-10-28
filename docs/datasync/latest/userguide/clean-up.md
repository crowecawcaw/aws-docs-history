# Cleaning up your AWS DataSync resources

If you used AWS DataSync for a test or don't need the AWS resources that you created,
delete them so that you aren't charged for resources you don't plan to use.

###### Note

If you have DataSync resources in an [opt-in Region](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md")
that you disable, those resources aren't automatically deleted. The resources are
still there if you enable that Region again.

## Deleting a DataSync agent

When you delete an agent from AWS DataSync, the agent resource is no longer
associated with your AWS account and can't be undone.

Keep in mind that deleting an agent from DataSync doesn't remove its virtual machine
(VM) or Amazon EC2 instance from your storage environment. You can delete the VM or
instance or reuse it to activate a new agent.

### Prerequisites

Don't delete an agent until you update or remove the DataSync resources that
depend on it. If you're replacing an agent, [update your transfer
locations](replacing-agent.md#replacing-agent-update-location "replacing-agent.md#replacing-agent-update-location") with the new agent. If you aren't replacing an agent,
delete transfer [tasks](#delete-task "#delete-task") and [locations](#deleting-location "#deleting-location") using that agent first.

### Deleting the agent

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, choose
   **Agents**.
3. Choose the agent that you want to delete.
4. Choose **Delete**, enter
   `delete` in the text box that appears, and then
   choose **Delete**.
5. If you aren't planning to [reuse the
   agent's infrastructure](#reusing-agent "#reusing-agent") for other DataSync activities, delete the
   agent's VM or Amazon EC2 instance to remove it from your storage
   environment.

## Reusing a DataSync agent's infrastructure

You can delete an agent resource from DataSync and still use the agent's underlying
VM or Amazon EC2 instance to activate a new agent.

###### To reuse an agent's infrastructure

1. [Test the agent's connection to AWS](test-agent-connections.md#test-network "test-agent-connections.md#test-network").
   If the network tests pass, go to the next step.

The network tests must pass before you can move to the next step. 2. [Delete the agent](#deleting-agent-resource "#deleting-agent-resource") resource
from DataSync but don't delete the agent's VM or Amazon EC2 instance. 3. Repeat step 1 to test the agent's connection to AWS again. If the
network tests pass, go to the next step. 4. About three minutes after deleting the agent resource from DataSync, check if
port 80 is open on the agent VM or Amazon EC2 instance. If it is, go to the next
step. 5. [Activate a new agent](activate-agent.md "activate-agent.md") with the
existing VM or Amazon EC2 instance.

You can activate the new agent in a different AWS Region, AWS account,
and with another type of [service
endpoint](choose-service-endpoint.md "choose-service-endpoint.md"). If you use a different type of service endpoint, you
have to adjust your [network
configuration](datasync-network.md "datasync-network.md").

## Deleting a DataSync location

As a best practice, remove the AWS DataSync locations that you no longer need.

###### To remove a location by using the DataSync console

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**,
   then choose **Locations**.
3. Choose the location that you want to remove.
4. Choose **Delete**. Confirm the deletion by entering
   `delete`, and then choose
   **Delete**.

## Deleting a DataSync task

If you no longer need an AWS DataSync task, you can delete it and its related AWS
resources.

### Prerequisites

When you run a task, DataSync automatically creates and manages [network interfaces](required-network-interfaces.md "required-network-interfaces.md") for data
transfer traffic. When you delete a task, you also delete its related network
interfaces as long as you have the following permissions:

- `ec2:DeleteNetworkInterface`
- `ec2:DescribeNetworkInterfaces`
- `ec2:ModifyNetworkInterfaceAttribute`

These permissions are available in the AWS managed policy
`AWSDataSyncFullAccess`. For more information, see [AWS managed policies for AWS DataSync](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

### Deleting the task

Once you delete a task, you can't restore it.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data
   transfer**, then choose
   **Tasks**.
3. Select the task that you want to delete.
4. Choose **Actions**, then choose
   **Delete**.
5. In the dialog box, choose **Delete**.
6. Copy the following `delete-task` command:

```
aws datasync delete-task \
      --task-arn "`task-to-delete`"
```

2. For the `--task-arn` parameter, specify the Amazon
   Resource Name (ARN) of the task you're deleting (for example,
   `arn:aws:datasync:us-east-2:123456789012:task/task-012345678abcd0123`).
3. Run the `delete-task` command.
