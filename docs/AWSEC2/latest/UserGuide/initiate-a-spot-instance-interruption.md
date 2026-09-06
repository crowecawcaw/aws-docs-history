

# Initiate a Spot Instance interruption
<a name="initiate-a-spot-instance-interruption"></a>

You can select a Spot Instance request or a Spot Fleet request in the Amazon EC2 console and initiate a Spot Instance interruption so that you can test how the applications on your Spot Instances handle being interrupted. When you initiate a Spot Instance interruption, Amazon EC2 notifies you that your Spot Instance will be interrupted in two minutes, and then, after two minutes, the instance is interrupted.

The underlying service that performs the Spot Instance interruption is AWS Fault Injection Service (AWS FIS). For information about AWS FIS, see [AWS Fault Injection Service](https://aws.amazon.com/fis/).

**Note**  
Interruption behaviors are `terminate`, `stop`, and `hibernate`. If you set the interruption behavior to `hibernate`, when you initiate a Spot Instance interruption, the hibernation process will begin immediately.

Initiating a Spot Instance interruption is supported in all AWS Regions except Asia Pacific (Jakarta), Asia Pacific (Osaka), China (Beijing), China (Ningxia), and Middle East (UAE).

**Topics**
+ [Initiate a Spot Instance interruption](#initiate-interruption)
+ [Verify the Spot Instance interruption](#spot-interruptions-verify-result)
+ [Quotas](#fis-quota-for-spot-instance-interruption)

## Initiate a Spot Instance interruption
<a name="initiate-interruption"></a>

You can use the EC2 console to quickly initiate a Spot Instance interruption. When you select a Spot Instance request, you can initiate the interruption of one Spot Instance. When you select a Spot Fleet request, you can initiate the interruption of multiple Spot Instances at once.

For more advanced experiments to test Spot Instance interruptions, you can create your own experiments using the AWS FIS console.

**To initiate the interruption of one Spot Instance in a Spot Instance request using the EC2 console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation pane, choose **Spot Requests**.

1. Select a Spot Instance request, and then choose **Actions**, **Initiate interruption**. You can’t select multiple Spot Instance requests to initiate an interruption.

1. In the **Initiate Spot Instance interruption** dialog box, under **Service access**, either use the default role, or choose an existing role. To choose an existing role, choose **Use an existing service role**, and then, for **IAM role**, select the role to use.

1. When you're ready to initiate the Spot Instance interruption, choose **Initiate interruption.**

**To initiate the interruption of one or more Spot Instances in a Spot Fleet request using the EC2 console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation pane, choose **Spot Requests**.

1. Select a Spot Fleet request, and then choose **Actions**, **Initiate interruption**. You can’t select multiple Spot Fleet requests to initiate an interruption.

1. In the **Specify number of Spot Instances** dialog box, for **Number of instances to interrupt**, enter the number of Spot Instances to interrupt, and then choose **Confirm**.
**Note**  
The number can't exceed the number of Spot Instances in the fleet or your [quota](#fis-quota-for-spot-instance-interruption) for the number of Spot Instances that AWS FIS can interrupt per experiment.

1. In the **Initiate Spot Instance interruption** dialog box, under **Service access**, either use the default role, or choose an existing role. To choose an existing role, choose **Use an existing service role**, and then, for **IAM role**, select the role to use.

1. When you're ready to initiate the Spot Instance interruption, choose **Initiate interruption.**

**To create more advanced experiments to test Spot Instance interruptions using the AWS FIS console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation pane, choose **Spot Requests**.

1. Choose **Actions**, **Create advanced experiments**.

   The AWS FIS console opens. For more information, see [Tutorial: Test Spot Instance interruptions using AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-spot-interruptions.html) in the *AWS Fault Injection Service User Guide*.

## Verify the Spot Instance interruption
<a name="spot-interruptions-verify-result"></a>

After you initiate the interruption, the following occurs:
+ The Spot Instance receives an [instance rebalance recommendation](rebalance-recommendations.md).
+ A [Spot Instance interruption notice](spot-instance-termination-notices.md) is issued two minutes before AWS FIS interrupts your instance.
+ After two minutes, the Spot Instance is interrupted.
+ A Spot Instance that was stopped by AWS FIS remains stopped until you restart it.

**To verify that the instance was interrupted after you initiated the interruption**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation pane, open **Spot Requests** and **Instances** in separate browser tabs or windows.

1. For **Spot Requests**, select the Spot Instance request or Spot Fleet request. The initial status is `fulfilled`. After the instance is interrupted, the status changes as follows, depending on the interruption behavior:
   + `terminate` – The status changes to `instance-terminated-by-experiment`.
   + `stop` – The status changes to `marked-for-stop-by-experiment` and then `instance-stopped-by-experiment`.

1. For **Instances**, select the Spot Instance. The initial status is `Running`. Two minutes after you receive the Spot Instance interruption notice, the status changes as follows, depending on the interruption behavior:
   + `stop` – The status changes to `Stopping` and then `Stopped`.
   + `terminate` – The status changes to `Shutting-down` and then `Terminated`.

## Quotas
<a name="fis-quota-for-spot-instance-interruption"></a>

Your AWS account has the following default quota for the number of Spot Instances that AWS FIS can interrupt per experiment.


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Target SpotInstances for aws:ec2:send-spot-instance-interruptions | Each supported Region: 5 | Yes | The maximum number of Spot Instances that aws:ec2:send-spot-instance-interruptions can target when you identify targets using tags, per experiment. | 

You can request a quota increase. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

To view all the quotas for AWS FIS, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **AWS Fault Injection Service**. You can also view all the [quotas for AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/fis-quotas.html) in the *AWS Fault Injection Service User Guide*.