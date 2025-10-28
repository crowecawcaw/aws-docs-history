# Tutorial: Simulate a connectivity

event

You can use AWS Fault Injection Service (AWS FIS) to simulate a variety of connectivity events. AWS FIS
simulates connectivity events by blocking network connections in one of the following ways:

- `all` – Denies all traffic entering and leaving the subnet. Note that this
  option allows intra-subnet traffic, including traffic to and from network interfaces in the subnet.
- `availability-zone` – Denies intra-VPC traffic to and from subnets in other Availability Zones.
- `dynamodb` – Denies traffic to and from the Regional endpoint for DynamoDB in the current Region.
- `prefix-list` – Denies traffic to and from the specified prefix list.
- `s3` – Denies traffic to and from the Regional endpoint for Amazon S3 in the current Region.
- `s3express` – Denies traffic to and from the zonal endpoint for Amazon S3 Express One Zone in the target subnets’ AZ. Target subnets must reside in AZs where S3 Express One Zone is currently available. For more information, see [S3 Express One Zone Availability Zones and Regions.](../../../AmazonS3/latest/userguide/s3-express-Endpoints.md "../../../AmazonS3/latest/userguide/s3-express-Endpoints.md").
- `vpc` – Denies traffic entering and leaving the VPC.
  Use this tutorial to create an experiment template that uses the AWS FIS
  `aws:network:disrupt-connectivity` action to introduce connectivity loss with
  Amazon S3 in a target subnet.

###### Topics

- [Prerequisites](#disrupt-connectivity-prerequisites "#disrupt-connectivity-prerequisites")
- [Step 1: Create an AWS FIS experiment
  template](#disrupt-connectivity-step1 "#disrupt-connectivity-step1")
- [Step 2: Ping an Amazon S3 endpoint](#disrupt-connectivity-step2 "#disrupt-connectivity-step2")
- [Step 3: Start your AWS FIS experiment](#disrupt-connectivity-step3 "#disrupt-connectivity-step3")
- [Step 4: Track your AWS FIS experiment
  progress](#disrupt-connectivity-step4 "#disrupt-connectivity-step4")
- [Step 5: Verify Amazon S3 network
  disruption](#disrupt-connectivity-step5 "#disrupt-connectivity-step5")
- [Step 5: Clean up](#disrupt-connectivity-step6 "#disrupt-connectivity-step6")

## Prerequisites

Before beginning this tutorial, you need a role with the appropriate permissions in
your AWS account, and a test Amazon EC2 instance:

###### A role with permissions in your AWS account

Create a role and attach a policy that enables AWS FIS to perform the
`aws:network:disrupt-connectivity` action on your behalf.

Your IAM role requires the following policy:

- [AWSFaultInjectionSimulatorNetworkAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorNetworkAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorNetworkAccess") – Grants AWS FIS
  service permission in Amazon EC2 networking and other required services to perform
  AWS FIS actions related to network infrastructure.

###### Note

For simplicity, this tutorial uses an AWS managed policy. For production use, we
recommend that you instead grant only the minimum permissions necessary for your use
case.

For more information about how to create an IAM role, see [IAM roles for AWS FIS experiments (AWS CLI)](getting-started-iam-service-role.md "getting-started-iam-service-role.md") or [Creating an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.

###### A test Amazon EC2 instance

Launch and connect to a test Amazon EC2 instance. You can use the following tutorial to
launch and connect to an Amazon EC2 instance: [Tutorial: Get started with Amazon EC2
Linux instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the _Amazon EC2 User Guide_.

## Step 1: Create an AWS FIS experiment

template

Create the experiment template by using the AWS FIS AWS Management Console. An AWS FIS template is made
up of actions, targets, stop conditions, and an experiment role. For more information
about how the templates work, see [Experiment templates for
AWS FIS](experiment-templates.md "experiment-templates.md").

Before you begin, make sure you have the following ready:

- An IAM role with the correct permissions.
- An Amazon EC2 instance.
- The subnet ID of your Amazon EC2 instance.

###### To create an experiment template

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the left navigation pane, choose **Experiment
   templates**.
3. Choose **Create experiment template**.
4. For **Step 1, Specify template details**, do the following:
   1. For **Description and name**, enter a description for the template, such as `Amazon S3 Network Disrupt
Connectivity`.
   2. Choose **Next**, and move to **Step 2, Specify actions and targets**.

5. Under **Actions**, choose **Add
   action**.
   1. For the **Name**, enter
      `disruptConnectivity`.
   2. For **Action type**, select
      **aws:network:disrupt-connectivity**.
   3. Under **Action parameters**, set the
      **Duration** to `2 minutes`.
   4. Under **Scope**, select **s3**.
   5. At the top, choose **Save**.

6. Under **Targets**, you should see the target that has been
   created automatically. Choose **Edit**.
   1. Verify that **Resource type** is
      `aws:ec2:subnet`.
   2. Under **Target method**, select **Resource
      IDs**, and then choose the subnet that you used when creating your
      Amazon EC2 instance in the [Prerequisites](fis-tutorial-disrupt-connectivity.md#disrupt-connectivity-prerequisites "fis-tutorial-disrupt-connectivity.md#disrupt-connectivity-prerequisites")
      steps.
   3. Verify that **Selection mode** is
      **All**.
   4. Choose **Save**.

7. Choose **Next** to move to **Step 3, Configure service access**.
8. Under **Service Access**, select the IAM role that you
   created as described in the [Prerequisites](fis-tutorial-disrupt-connectivity.md#disrupt-connectivity-prerequisites "fis-tutorial-disrupt-connectivity.md#disrupt-connectivity-prerequisites") for this
   tutorial. If your role is not displayed, verify that it has the required trust
   relationship. For more information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").
9. Choose **Next** to move to **Step 4, Configure optional settings**.
10. (Optional) Under **Stop conditions**, you can select a CloudWatch
    alarm to stop the experiment if the condition occurs. For more information, see
    [Stop conditions for
    AWS FIS](stop-conditions.md "stop-conditions.md").
11. (Optional) Under **Logs**, you can select an Amazon S3 bucket, or
    send logs to CloudWatch for your experiment.
12. Choose **Next** to move to **Step 5, Review and create**.
13. Review the template and choose **Create experiment template**.
    When prompted for confirmation, enter `create`, Then choose **Create experiment template**.

## Step 2: Ping an Amazon S3 endpoint

Verify that your Amazon EC2 instance is able to reach an Amazon S3 endpoint.

1. Connect to the Amazon EC2 instance that you created in the [Prerequisites](fis-tutorial-disrupt-connectivity.md#disrupt-connectivity-prerequisites "fis-tutorial-disrupt-connectivity.md#disrupt-connectivity-prerequisites") steps.

For troubleshooting, see [Troubleshoot connecting to your instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md") in the
_Amazon EC2 User Guide_. 2. Check to see the AWS Region where your instance is located. You can do this
in the Amazon EC2 console or by running the following command.

```
`hostname`
```

For example, if you launched an Amazon EC2 instance in `us-west-2`,
you'll see the following output.

```
[ec2-user@ip-172.16.0.0 ~]$ hostname
ip-172.16.0.0.us-west-2.compute.internal
```

3. Ping an Amazon S3 endpoint in your AWS Region. Replace
   `AWS Region` with your Region.

```
ping -c 1 s3.`AWS Region`.amazonaws.com
```

For the output, you should see a successful ping with 0% packet loss, as shown
in the following example.

```
PING s3.us-west-2.amazonaws.com (x.x.x.x) 56(84) bytes of data.
64 bytes from s3-us-west-2.amazonaws.com (x.x.x.x: icmp_seq=1 ttl=249 time=1.30 ms

--- s3.us-west-2.amazonaws.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.306/1.306/1.306/0.000 ms
```

## Step 3: Start your AWS FIS experiment

Start an experiment with the experiment template that you just created.

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the left navigation pane, choose **Experiment
   templates**.
3. Select the ID of the experiment template that you created to open its details
   page.
4. Choose **Start experiment**.
5. (Optional) In the confirmation page, add tags for your experiment.
6. In the confirmation page, choose **Start experiment**.

## Step 4: Track your AWS FIS experiment

progress

You can track the progress of a running experiment until the experiment is completed,
stopped, or has failed.

1. You should be on the details page for the experiment that you just started. If
   you're not, choose **Experiments**, and then select the ID of
   the experiment to open its details page.
2. To view the state of the experiment, check the **State** in
   the details pane. For more information, see [Experiment
   states](experiments.md#experiment-states "experiments.md#experiment-states").
3. When the state of the experiment is **Running**, move to the
   next step.

## Step 5: Verify Amazon S3 network

disruption

You can validate the experiment progress by by pinging the Amazon S3 endpoint.

- From your Amazon EC2 instance, ping the Amazon S3 endpoint in your AWS Region. Replace
  `AWS Region` with your Region.

```
ping -c 1 s3.`AWS Region`.amazonaws.com
```

For the output, you should see an unsuccessful ping with 100% packet loss, as
shown in the following example.

```
ping -c 1 s3.us-west-2.amazonaws.com
PING s3.us-west-2.amazonaws.com (x.x.x.x) 56(84) bytes of data.

--- s3.us-west-2.amazonaws.com ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms
```

## Step 5: Clean up

If you no longer need the Amazon EC2 instance that you created for this experiment or the
AWS FIS template, you can remove them.

###### To remove the Amazon EC2 instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the test instance, choose **Instance state**, and then
   choose **Terminate instance**.
4. When prompted for confirmation, choose **Terminate**.

###### To delete the experiment template using the AWS FIS console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiment
   templates**.
3. Select the experiment template, and then choose **Actions**,
   **Delete experiment template**.
4. When prompted for confirmation, enter `delete`, and then choose
   **Delete experiment template**.
