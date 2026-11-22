

# Install the CloudWatch agent on new instances using CloudFormation

 This section describes how to install the CloudWatch agent on new Amazon EC2 instances using AWS CloudFormation. 

**Note**  
 Amazon uploaded several CloudFormation templates to GitHub that can help you install and update the CloudWatch agent on new Amazon EC2 instances. For more information about using CloudFormation, see [ What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html). 

The template location is [ Deploy the Amazon CloudWatch agent to EC2 instances using CloudFormation](https://github.com/aws-cloudformation/aws-cloudformation-templates/tree/main/Solutions/AmazonCloudWatchAgent). This location includes both `inline` and `ssm` directories. Each of these directories contains templates for both Linux and Windows instances. 


+ The templates in the `inline` directory have the CloudWatch agent configuration embedded into the CloudFormation template. By default, the Linux templates collect the metrics `mem_used_percent` and `swap_used_percent`, and the Windows templates collect `Memory % Committed Bytes In Use` and `Paging File % Usage`.

  To modify these templates to collect different metrics, modify the following section of the template. The following example is from the template for Linux servers. Follow the format and syntax of the agent configuration file to make these changes. For more information, see [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md).

  ```
  {
     "metrics":{
        "append_dimensions":{
           "AutoScalingGroupName":"${!aws:AutoScalingGroupName}",
           "ImageId":"${!aws:ImageId}",
           "InstanceId":"${!aws:InstanceId}",
           "InstanceType":"${!aws:InstanceType}"
        },
        "metrics_collected":{
           "mem":{
              "measurement":[
                 "mem_used_percent"
              ]
           },
           "swap":{
              "measurement":[
                 "swap_used_percent"
              ]
           }
        }
     }
  }
  ```
**Note**  
In the inline templates, all placeholder variables must have an exclamation mark (\!) before them as an escape character. You can see this in the example template. If you add other placeholder variables, be sure to add an exclamation mark before the name.

  To have the agent receive OpenTelemetry Protocol (OTLP) data from your applications, add an `opentelemetry` section to the agent configuration. For more information, see [Amazon CloudWatch agent](CloudWatch-OTLPCloudWatchAgent.md).
+ The templates in the `ssm` directory load an agent configuration file from Parameter Store. To use these templates, you must first create a configuration file and upload it to Parameter Store. You then provide the Parameter Store name of the file in the template. You can create the configuration file manually or by using the wizard. For more information, see [Create the Classic CloudWatch agent configuration file](create-cloudwatch-agent-configuration-file.md).

You can use both types of templates for installing the CloudWatch agent and for updating the agent configuration.

For information about setting up the agent on a system that has security-enhanced Linux (SELinux) enabled, see [Set up the CloudWatch agent with security-enhanced Linux (SELinux)](CloudWatch-Agent-SELinux.md).

## Tutorial: Install and configure the CloudWatch agent using an CloudFormation inline template
<a name="installing-CloudWatch-Agent-using-CloudFormation-Templates-inline"></a>

This tutorial walks you through using CloudFormation to install the CloudWatch agent on a new Amazon EC2 instance. This tutorial installs on a new instance running AL2023 using the inline templates, which don't require the use of the JSON configuration file or Parameter Store. The inline template includes the agent configuration in the template. In this tutorial, you use the default agent configuration contained in the template.

After the procedure for installing the agent, the tutorial continues with how to update the agent.

**To use CloudFormation to install the CloudWatch agent on a new instance**

1. Download the template from GitHub. In this tutorial, download the inline template for Amazon Linux as follows:

   ```
   curl -O https://raw.githubusercontent.com/aws-cloudformation/aws-cloudformation-templates/main/Solutions/AmazonCloudWatchAgent/inline/amazon_linux.yaml
   ```

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. Choose **Create stack**, **With new resources (standard)**.

1. For **Prepare template**, choose **Choose an existing template**. For **Specify template**, choose **Upload a template file**, choose the downloaded template, and choose **Next**.

1. On the **Specify stack details** page, fill out the following parameters and choose **Next**:
   + **Stack name**: Choose a stack name for your CloudFormation stack. 
   + **IAMRole**: Enter the name of the instance profile for an IAM role that has the **CloudWatchAgentServerPolicy** policy attached. When you create a role for Amazon EC2 in the IAM console, the console creates an instance profile with the same name as the role. For more information, see [Prerequisites](prerequisites.md).
   + **InstanceAMI**: Keep the default, which is a public Parameter Store parameter that resolves to the latest AL2023 AMI in the Region where you launch your stack.
   + **InstanceType**: Choose a valid instance type.
   + **KeyName**: To enable SSH access to the new instance, choose an existing Amazon EC2 key pair. If you don't already have an Amazon EC2 key pair, you can create one in the AWS Management Console. For more information, see [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon EC2 User Guide*.
   + **SSHLocation**: Specifies the IP address range that can be used to connect to the instance using SSH. The default, `0.0.0.0/0`, allows access from any IP address. We recommend that you restrict this range to the IP addresses that you connect from.
   + **SubnetId**: Choose the subnet to launch the instance in. The instance must be able to reach the CloudWatch endpoints. For more information, see [Network requirements](prerequisites.md#CloudWatch-Agent-network-requirements).

1. On the **Configure stack options** page, you can choose to tag your stack resources. Choose **Next**.

1. On the **Review and create** page, review your information, and then choose **Submit**.

   If you refresh the console, you see that the new stack has the `CREATE_IN_PROGRESS` status.

1. When the instance is created, you can see it in the Amazon EC2 console. Optionally, you can connect to the host and check the progress.

   Use the following command to confirm that the agent is installed and running:

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a status
   ```

   The output shows the agent status, such as `"status": "running"`, and the agent version.

The next procedure demonstrates using CloudFormation to update the CloudWatch agent using an inline template. The default inline template collects the `mem_used_percent` metric. In this tutorial, you change the agent configuration to stop collecting that metric.

**To use CloudFormation to update the CloudWatch agent**

1. In the template that you downloaded in the previous procedure, remove the following lines and then save the template:

   ```
   "mem": {
                           
        "measurement": [
            "mem_used_percent"
          ]
    },
   ```

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the **Stacks** page, select the stack that you created and choose **Update**.

1. Choose **Replace existing template**. For **Specify template**, choose **Upload a template file**, choose the template that you modified, and choose **Next**.

1. On the **Specify stack details** and **Configure stack options** pages, choose **Next**.

1. On the review page, review your information and choose **Update stack**.

   After some time, you see `UPDATE_COMPLETE`.

## Tutorial: Install the CloudWatch agent using CloudFormation and Parameter Store
<a name="installing-CloudWatch-Agent-using-CloudFormation-Templates"></a>

This tutorial walks you through using CloudFormation to install the CloudWatch agent on a new Amazon EC2 instance. This tutorial installs on a new instance running AL2023 using an agent configuration file that you create and save in Parameter Store.

After the procedure for installing the agent, the tutorial continues with how to update the agent.

**To use CloudFormation to install the CloudWatch agent on a new instance using a configuration from Parameter Store**

1. If you haven't done so already, download the CloudWatch agent package to one of your computers so that you can create the agent configuration file. For more information and downloading the agent using Parameter Store, see [Download the CloudWatch agent package](download-CloudWatch-Agent-on-EC2-Instance-commandline-first.md).

1. Create the agent configuration file and save it in Parameter Store. For more information, see [Create the Classic CloudWatch agent configuration file](create-cloudwatch-agent-configuration-file.md).

1. Download the template from GitHub as follows:

   ```
   curl -O https://raw.githubusercontent.com/aws-cloudformation/aws-cloudformation-templates/main/Solutions/AmazonCloudWatchAgent/ssm/amazon_linux.yaml
   ```

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. Choose **Create stack**, **With new resources (standard)**.

1. For **Prepare template**, choose **Choose an existing template**. For **Specify template**, choose **Upload a template file**, choose the template that you downloaded, and choose **Next**.

1. On the **Specify stack details** page, fill out the following parameters accordingly and choose **Next**:
   + **Stack name**: Choose a stack name for your CloudFormation stack. 
   + **IAMRole**: Enter the name of the instance profile for an IAM role that has the **CloudWatchAgentServerPolicy** policy attached. When you create a role for Amazon EC2 in the IAM console, the console creates an instance profile with the same name as the role. For more information, see [Prerequisites](prerequisites.md).
   + **InstanceAMI**: Keep the default, which is a public Parameter Store parameter that resolves to the latest AL2023 AMI in the Region where you launch your stack.
   + **InstanceType**: Choose a valid instance type.
   + **KeyName**: To enable SSH access to the new instance, choose an existing Amazon EC2 key pair. If you don't already have an Amazon EC2 key pair, you can create one in the AWS Management Console. For more information, see [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon EC2 User Guide*.
   + **SSHLocation**: Specifies the IP address range that can be used to connect to the instance using SSH. The default, `0.0.0.0/0`, allows access from any IP address. We recommend that you restrict this range to the IP addresses that you connect from.
   + **SubnetId**: Choose the subnet to launch the instance in. The instance must be able to reach the CloudWatch endpoints. For more information, see [Network requirements](prerequisites.md#CloudWatch-Agent-network-requirements).
   + **SSMKey**: Specifies the agent configuration file that you created and saved in Parameter Store.

1. On the **Configure stack options** page, you can choose to tag your stack resources. Choose **Next**.

1. On the **Review and create** page, review your information, and then choose **Submit**.

   If you refresh the console, you see that the new stack has the `CREATE_IN_PROGRESS` status.

1. When the instance is created, you can see it in the Amazon EC2 console. Optionally, you can connect to the host and check the progress.

   Use the following command to confirm that the agent is installed and running:

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a status
   ```

   The output shows the agent status, such as `"status": "running"`, and the agent version.

The next procedure demonstrates using CloudFormation to update the CloudWatch agent, using an agent configuration that you saved in Parameter Store.

**To use CloudFormation to update the CloudWatch agent using a configuration in Parameter Store**

1. Change the agent configuration file stored in Parameter Store to the new configuration that you want.

1. In the CloudFormation template that you downloaded in the [Tutorial: Install the CloudWatch agent using CloudFormation and Parameter Store](#installing-CloudWatch-Agent-using-CloudFormation-Templates) topic, change the version number. For example, you might change `VERSION=1.0` to `VERSION=2.0`.

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the **Stacks** page, select the stack that you created and choose **Update**.

1. Choose **Replace existing template**. For **Specify template**, choose **Upload a template file**, choose the template that you modified, and choose **Next**.

1. On the **Specify stack details** and **Configure stack options** pages, choose **Next**.

1. On the review page, review your information and choose **Update stack**.

   After some time, you see `UPDATE_COMPLETE`.

## Troubleshooting installation of the CloudWatch agent with CloudFormation
<a name="CloudWatch-Agent-CloudFormation-troubleshooting"></a>

This section helps you troubleshoot issues with installing and updating the CloudWatch agent using CloudFormation.

### Detecting when an update fails
<a name="CloudWatch-Agent-troubleshooting-Detecting-CloudFormation-update-issues"></a>

If you use CloudFormation to update your CloudWatch agent configuration, and use an invalid configuration, the agent stops sending any metrics to CloudWatch. A quick way to check whether an agent configuration update succeeded is to look at the `cfn-init-cmd.log` file. On a Linux server, the file is located at `/var/log/cfn-init-cmd.log`. On a Windows instance, the file is located at `C:\cfn\log\cfn-init-cmd.log`.

### Metrics are missing
<a name="CloudWatch-Agent-troubleshooting-Cloudformation-missing-metrics"></a>

If you don't see metrics that you expect to see after installing or updating the agent, confirm that the agent is configured to collect that metric. To do this, check the `amazon-cloudwatch-agent.json` file to make sure that the metric is listed. For metrics that the agent publishes as CloudWatch metrics, check that you are looking in the correct metric namespace. OpenTelemetry metrics don't use a namespace; query them by metric name with PromQL. For more information, see [CloudWatch agent files and locations](troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-files-and-locations).