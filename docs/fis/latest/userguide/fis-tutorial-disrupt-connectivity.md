

# Tutorial: Simulate a connectivity event
<a name="fis-tutorial-disrupt-connectivity"></a>

You can use AWS Fault Injection Service (AWS FIS) to simulate a variety of connectivity events. AWS FIS simulates connectivity events by blocking network connections in one of the following ways:
+ `all` – Denies all traffic entering and leaving the subnet. Note that this option allows intra-subnet traffic, including traffic to and from network interfaces in the subnet.
+ `availability-zone` – Denies intra-VPC traffic to and from subnets in other Availability Zones.
+ `dynamodb` – Denies traffic to and from the Regional endpoint for DynamoDB in the current Region.
+ `prefix-list` – Denies traffic to and from the specified prefix list.
+ `s3` – Denies traffic to and from the Regional endpoint for Amazon S3 in the current Region.
+ `s3express` – Denies traffic to and from the zonal endpoint for Amazon S3 Express One Zone in the target subnets’ AZ. Target subnets must reside in AZs where S3 Express One Zone is currently available. For more information, see [S3 Express One Zone Availability Zones and Regions.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Endpoints.html).
+ `vpc` – Denies traffic entering and leaving the VPC.

Use this tutorial to create an experiment template that uses the AWS FIS `aws:network:disrupt-connectivity` action to introduce connectivity loss with Amazon S3 in a target subnet.

**Topics**
+ [Prerequisites](#disrupt-connectivity-prerequisites)
+ [Step 1: Create an AWS FIS experiment template](#disrupt-connectivity-step1)
+ [Step 2: Ping an Amazon S3 endpoint](#disrupt-connectivity-step2)
+ [Step 3: Start your AWS FIS experiment](#disrupt-connectivity-step3)
+ [Step 4: Track your AWS FIS experiment progress](#disrupt-connectivity-step4)
+ [Step 5: Verify Amazon S3 network disruption](#disrupt-connectivity-step5)
+ [Step 5: Clean up](#disrupt-connectivity-step6)

## Prerequisites
<a name="disrupt-connectivity-prerequisites"></a>

Before beginning this tutorial, you need a role with the appropriate permissions in your AWS account, and a test Amazon EC2 instance:

**A role with permissions in your AWS account**  
Create a role and attach a policy that enables AWS FIS to perform the `aws:network:disrupt-connectivity` action on your behalf. 

Your IAM role requires the following policy:
+  [AWSFaultInjectionSimulatorNetworkAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorNetworkAccess) – Grants AWS FIS service permission in Amazon EC2 networking and other required services to perform AWS FIS actions related to network infrastructure.

**Note**  
For simplicity, this tutorial uses an AWS managed policy. For production use, we recommend that you instead grant only the minimum permissions necessary for your use case.  
For more information about how to create an IAM role, see [IAM roles for AWS FIS experiments (AWS CLI)](https://docs.aws.amazon.com/fis/latest/userguide/getting-started-iam-service-role) or [Creating an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user) in the *IAM User Guide*.

**A test Amazon EC2 instance**  
Launch and connect to a test Amazon EC2 instance. You can use the following tutorial to launch and connect to an Amazon EC2 instance: [Tutorial: Get started with Amazon EC2 Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted) in the *Amazon EC2 User Guide*.

## Step 1: Create an AWS FIS experiment template
<a name="disrupt-connectivity-step1"></a>

Create the experiment template by using the AWS FIS AWS Management Console. An AWS FIS template is made up of actions, targets, stop conditions, and an experiment role. For more information about how the templates work, see [Experiment templates for AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates).

Before you begin, make sure you have the following ready:
+ An IAM role with the correct permissions.
+ An Amazon EC2 instance.
+ The subnet ID of your Amazon EC2 instance.

**To create an experiment template**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the left navigation pane, choose **Experiment templates**.

1. Choose **Create experiment template**.

1. For **Step 1, Specify template details**, do the following:

   1. For **Description and name**, enter a description for the template, such as `Amazon S3 Network Disrupt Connectivity`.

   1. Choose **Next**, and move to **Step 2, Specify actions and targets**. 

1. Under **Actions**, choose **Add action**.

   1. For the **Name**, enter `disruptConnectivity`.

   1. For **Action type**, select **aws:network:disrupt-connectivity**.

   1. Under **Action parameters**, set the **Duration** to `2 minutes`.

   1. Under **Scope**, select **s3**.

   1. At the top, choose **Save**.

1. Under **Targets**, you should see the target that has been created automatically. Choose **Edit**.

   1. Verify that **Resource type** is `aws:ec2:subnet`.

   1. Under **Target method**, select **Resource IDs**, and then choose the subnet that you used when creating your Amazon EC2 instance in the [Prerequisites](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-disrupt-connectivity.html#disrupt-connectivity-prerequisites) steps.

   1. Verify that **Selection mode** is **All**.

   1. Choose **Save**.

1. Choose **Next** to move to **Step 3, Configure service access**. 

1. Under **Service Access**, select the IAM role that you created as described in the [Prerequisites](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-disrupt-connectivity.html#disrupt-connectivity-prerequisites) for this tutorial. If your role is not displayed, verify that it has the required trust relationship. For more information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md).

1. Choose **Next** to move to **Step 4, Configure optional settings**. 

1. (Optional) Under **Stop conditions**, you can select a CloudWatch alarm to stop the experiment if the condition occurs. For more information, see [Stop conditions for AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions).

1. (Optional) Under **Logs**, you can select an Amazon S3 bucket, or send logs to CloudWatch for your experiment.

1. Choose **Next** to move to **Step 5, Review and create**. 

1. Review the template and choose **Create experiment template**. When prompted for confirmation, enter `create`, Then choose **Create experiment template**. 

## Step 2: Ping an Amazon S3 endpoint
<a name="disrupt-connectivity-step2"></a>

Verify that your Amazon EC2 instance is able to reach an Amazon S3 endpoint.

1. Connect to the Amazon EC2 instance that you created in the [Prerequisites](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-disrupt-connectivity.html#disrupt-connectivity-prerequisites) steps.

   For troubleshooting, see [Troubleshoot connecting to your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting) in the *Amazon EC2 User Guide*.

1. Check to see the AWS Region where your instance is located. You can do this in the Amazon EC2 console or by running the following command.

   ```
   hostname
   ```

   For example, if you launched an Amazon EC2 instance in `us-west-2`, you'll see the following output.

   ```
   [ec2-user@ip-172.16.0.0 ~]$ hostname
   ip-172.16.0.0.us-west-2.compute.internal
   ```

1. Ping an Amazon S3 endpoint in your AWS Region. Replace {{AWS Region}} with your Region.

   ```
   ping -c 1 s3.{{AWS Region}}.amazonaws.com
   ```

   For the output, you should see a successful ping with 0% packet loss, as shown in the following example.

   ```
   PING s3.us-west-2.amazonaws.com (x.x.x.x) 56(84) bytes of data.
   64 bytes from s3-us-west-2.amazonaws.com (x.x.x.x: icmp_seq=1 ttl=249 time=1.30 ms
   
   --- s3.us-west-2.amazonaws.com ping statistics ---
   1 packets transmitted, 1 received, 0% packet loss, time 0ms
   rtt min/avg/max/mdev = 1.306/1.306/1.306/0.000 ms
   ```

## Step 3: Start your AWS FIS experiment
<a name="disrupt-connectivity-step3"></a>

Start an experiment with the experiment template that you just created.

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the left navigation pane, choose **Experiment templates**.

1. Select the ID of the experiment template that you created to open its details page.

1. Choose **Start experiment**.

1. (Optional) In the confirmation page, add tags for your experiment.

1. In the confirmation page, choose **Start experiment**.

## Step 4: Track your AWS FIS experiment progress
<a name="disrupt-connectivity-step4"></a>

You can track the progress of a running experiment until the experiment is completed, stopped, or has failed.

1. You should be on the details page for the experiment that you just started. If you're not, choose **Experiments**, and then select the ID of the experiment to open its details page.

1. To view the state of the experiment, check the **State** in the details pane. For more information, see [Experiment states](https://docs.aws.amazon.com/fis/latest/userguide/experiments.html#experiment-states).

1. When the state of the experiment is **Running**, move to the next step.

## Step 5: Verify Amazon S3 network disruption
<a name="disrupt-connectivity-step5"></a>

You can validate the experiment progress by by pinging the Amazon S3 endpoint.
+ From your Amazon EC2 instance, ping the Amazon S3 endpoint in your AWS Region. Replace {{AWS Region}} with your Region.

  ```
  ping -c 1 s3.{{AWS Region}}.amazonaws.com
  ```

  For the output, you should see an unsuccessful ping with 100% packet loss, as shown in the following example.

  ```
  ping -c 1 s3.us-west-2.amazonaws.com
  PING s3.us-west-2.amazonaws.com (x.x.x.x) 56(84) bytes of data.
  
  --- s3.us-west-2.amazonaws.com ping statistics ---
  1 packets transmitted, 0 received, 100% packet loss, time 0ms
  ```

## Step 5: Clean up
<a name="disrupt-connectivity-step6"></a>

If you no longer need the Amazon EC2 instance that you created for this experiment or the AWS FIS template, you can remove them.

**To remove the Amazon EC2 instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the test instance, choose **Instance state**, and then choose **Terminate instance**.

1. When prompted for confirmation, choose **Terminate**.



**To delete the experiment template using the AWS FIS console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiment templates**.

1. Select the experiment template, and then choose **Actions**, **Delete experiment template**.

1. When prompted for confirmation, enter `delete`, and then choose **Delete experiment template**.