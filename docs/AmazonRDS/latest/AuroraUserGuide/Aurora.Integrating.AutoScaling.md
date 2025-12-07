# Editing an auto scaling policy for an Amazon Aurora DB cluster

You can edit a scaling policy using the AWS Management Console, the AWS CLI, or the Application Auto Scaling API.

You can edit a scaling policy by using the AWS Management Console.

###### To edit an auto scaling policy for an Aurora DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the Aurora DB cluster whose auto scaling policy you want to edit.
4. Choose the **Logs & events** tab.
5. In the **Auto scaling policies** section, choose the auto scaling policy, and then choose
   **Edit**.
6. Make changes to the policy.
7. Choose **Save**.
   The following is a sample **Edit Auto Scaling policy** dialog box.

![Editing an auto scaling policy based on average CPU utilization](images/aurora-autoscaling-edit-cpu.png)
You can use the AWS CLI or the Application Auto Scaling API to edit a scaling policy in the same way that you apply a scaling
policy:

- When using the AWS CLI, specify the name of the policy you want to edit in the `--policy-name`
  parameter. Specify new values for the parameters you want to change.
- When using the Application Auto Scaling API, specify the name of the policy you want to edit in the `PolicyName`
  parameter. Specify new values for the parameters you want to change.
  For more information, see [Applying a scaling policy to an Aurora DB
  cluster](Aurora.Integrating.AutoScaling.md#Aurora.Integrating.AutoScaling.AddCode.ApplyScalingPolicy "Aurora.Integrating.AutoScaling.md#Aurora.Integrating.AutoScaling.AddCode.ApplyScalingPolicy").
