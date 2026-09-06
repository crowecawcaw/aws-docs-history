

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Configuring rollbacks
<a name="deploy-consumption-enable-alarms"></a>

By default, if the **Deploy CloudFormation stack** action fails, it will cause CloudFormation to roll back the stack to the last known stable state. You can change the behavior so that rollbacks occur not only when the action fails, but also when a specified Amazon CloudWatch alarm occurs. For more information about CloudWatch alarms, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/) in the *Amazon CloudWatch User Guide*.

You can also change the default behavior so that CloudFormation does not roll back the stack when the action fails. 

Use the following instructions to configure rollbacks.

**Note**  
You cannot start a rollback manually.

------
#### [ Visual ]

**Before you begin**

1. Make sure you have a [workflow](workflow.md) that includes a functioning **Deploy CloudFormation stack** action. For more information, see [Deploying an CloudFormation stack](deploy-action-cfn.md).

1. In the role specified in the **Stack role - optional** field of the **Deploy CloudFormation stack** action, make sure to include the **CloudWatchFullAccess** permission. For information about creating this role with the appropriate permissions, see [Step 2: Create AWS roles](deploy-tut-lambda.md#deploy-tut-lambda-cfn-roles).

**To configure rollback alarms for the 'Deploy CloudFormation stack' action**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **Visual**.

1. Choose your **Deploy CloudFormation stack** action.

1. In the details pane, choose **Configuration**.

1. At the bottom, expand **Advanced**.

1. Under **Monitor alarm ARNs**, choose **Add alarm**.

1. Enter information into the following fields.
   + **Alarm ARN**

     Specify the Amazon Resource Name (ARN) of an Amazon CloudWatch alarm to use as a rollback trigger. For example, `arn:aws:cloudwatch::123456789012:alarm/MyAlarm`. You can have a maximum of five rollback triggers.
**Note**  
If you specify a CloudWatch alarm ARN, you'll also need to configure additional permissions to enable the action to access CloudWatch. For more information, see [Configuring rollbacks](#deploy-consumption-enable-alarms).
   + **Monitoring time**

     Specify an amount of time, from 0 to 180 minutes, during which CloudFormation monitors the specified alarms. Monitoring begins *after* all the stack resources have been deployed. If the alarm occurs within the specified monitoring time, then the deployment fails, and CloudFormation rolls back the entire stack operation.

     Default: 0. CloudFormation only monitors alarms while the stack resources are being deployed, not after.

------
#### [ YAML ]

**To configure rollback triggers for the 'Deploy CloudFormation stack' action**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of a workflow that includes the **Deploy CloudFormation stack** action. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. Add the `monitor-alarm-arns` and `monitor-timeout-in-minutes` properties in the YAML code to add rollback triggers. For an explanation of each property, see ['Deploy CloudFormation stack' action YAML](deploy-action-ref-cfn.md).

1. In the role specified in the `role-arn` property of the **Deploy CloudFormation stack** action, make sure to include the **CloudWatchFullAccess** permission. For information about creating this role with the appropriate permissions, see [Step 2: Create AWS roles](deploy-tut-lambda.md#deploy-tut-lambda-cfn-roles).

------

------
#### [ Visual ]

**To turn off rollbacks for the 'Deploy CloudFormation stack' action**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of a workflow that includes the **Deploy CloudFormation stack** action. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **Visual**.

1. Choose your **Deploy CloudFormation stack** action.

1. In the details pane, choose **Configuration**.

1. At the bottom, expand **Advanced**.

1. Turn on **Disable rollback**.

------
#### [ YAML ]

**To turn off rollbacks for the 'Deploy CloudFormation stack' action**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of a workflow that includes the **Deploy CloudFormation stack** action. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. Add the `disable-rollback: 1` property in the YAML code to stop rollbacks. For an explanation of this property, see ['Deploy CloudFormation stack' action YAML](deploy-action-ref-cfn.md).

------