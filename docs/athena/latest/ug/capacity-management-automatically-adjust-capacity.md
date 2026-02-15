# Automatically adjust capacity

You can automatically adjust the capacity of your reservation in response to workload utilization using Athena's auto-scaling solution. It automatically adds capacity when utilization exceeds your configured threshold and removes capacity during periods of low utilization to reduce costs. You can customize its behavior by setting different utilization thresholds, minimum and maximum DPU quantities, scaling increments, and utilization evaluation frequency. This eliminates manual capacity adjustments while helping you balance performance requirements with cost optimization.

You deploy this serverless solution using a CloudFormation template. It creates a Step Functions state machine which monitors utilization metrics and makes scaling decisions. You can further customize the template or state machine to meet your specific needs.

To get started, use the Athena console and choose **Set up auto-scaling** on your capacity reservation detail page, which redirects you to CloudFormation with the template pre-loaded. Alternatively, follow the procedure below.

## Prerequisites

- An active capacity reservation is required
- Required IAM permissions for deploying CloudFormation stacks and creating Step Functions resources

## Launch the CloudFormation stack

This automated CloudFormation template deploys the Athena Capacity Reservation auto-scaling solution. You must complete the applicable steps in [Prerequisites](#capacity-management-auto-scaling-prerequisites "#capacity-management-auto-scaling-prerequisites") before launching the stack.

[![CloudFormation launch button for creating the stack.](images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https:%2F%2Fathena-downloads.s3.us-east-1.amazonaws.com%2F%2Ftemplates%2F%2Fcapacity-reservation-scaling%2F%2Fstate-machine%2F%2Fathena-capacity-reservation-scaling-template-v1.1.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https:%2F%2Fathena-downloads.s3.us-east-1.amazonaws.com%2F%2Ftemplates%2F%2Fcapacity-reservation-scaling%2F%2Fstate-machine%2F%2Fathena-capacity-reservation-scaling-template-v1.1.yaml")

###### To launch the auto-scaling solution

1. Sign into [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and select the button to launch the `AWSAccelerator-InstallerStack` CloudFormation template.
2. The template launches in the US East (N. Virginia) by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
3. On the **Create stack** page, verify that the template URL is in the **Amazon S3 URL** text box and choose **Next**.
4. On the **Specify stack details** page, assign a name to your solution stack.
5. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

| Parameter                     | Default            | Description                                                       |
| ----------------------------- | ------------------ | ----------------------------------------------------------------- |
| AthenaCapacityReservationName | _<requires input>_ | Name of your existing capacity reservation to monitor and adjust. |
| MaxTargetDpus                 | _<requires input>_ | Maximum number of DPUs the solution can scale up to.              |
| MinTargetDpus                 | 4                  | Minimum number of DPUs the solution can scale down to.            |
| ScaleOutDpuAmount             | 16                 | Number of DPUs to add when scaling up.                            |
| ScaleInDpuAmount              | 8                  | Number of DPUs to remove when scaling down.                       |
| HighUtilizationThreshold      | 75                 | Utilization percentage that triggers scaling up.                  |
| LowUtilizationThreshold       | 25                 | Utilization percentage that triggers scaling down.                |
| EvaluationLookbackWindow      | 300                | Time window in seconds for measuring utilization.                 |
| EvaluationFrequency           | rate (5 minutes)   | How often to check utilization and adjust capacity.               |

###### Note

All DPU values must be multiples of 4 to comply with Athena's capacity reservation requirements. 6. Choose **Next**. 7. On the **Configure stack options** page, choose **Next**. 8. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template might create IAM resources. 9. Choose **Submit** to deploy the stack.

You can view the status of the stack in the CloudFormation console in the **Status** column. You should receive a `CREATE_COMPLETE` status in a few minutes.
