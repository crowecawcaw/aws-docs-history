# CloudWatch solution: NVIDIA GPU workload on Amazon EC2

This solution helps you configure out-of-the-box metric collection using CloudWatch agents for
NVIDIA GPU workloads running on EC2 instances. Additionally, it helps you set up a
pre-configured CloudWatch dashboard. For general information about all CloudWatch observability solutions,
see [CloudWatch observability solutions](Monitoring-Solutions.md "Monitoring-Solutions.md").

###### Topics

- [Requirements](#Solution-NVIDIA-GPU-On-EC2-Requirements "#Solution-NVIDIA-GPU-On-EC2-Requirements")
- [Benefits](#Solution-NVIDIA-GPU-On-EC2-Benefits "#Solution-NVIDIA-GPU-On-EC2-Benefits")
- [CloudWatch agent configuration for this
  solution](#Solution-NVIDIA-GPU-CloudWatch-Agent "#Solution-NVIDIA-GPU-CloudWatch-Agent")
- [Deploy the agent for your solution](#Solution-NVIDIA-GPU-Agent-Deploy "#Solution-NVIDIA-GPU-Agent-Deploy")
- [Create the NVIDIA GPU solution dashboard](#Solution-NVIDIA-GPU-Dashboard "#Solution-NVIDIA-GPU-Dashboard")

## Requirements

This solution is relevant for the following conditions:

- Compute: Amazon EC2
- Supports up to 500 GPUs across all EC2 instances in a given AWS Region
- Latest version of CloudWatch agent
- SSM agent installed on EC2 instance
- The EC2 instance must have an NVIDIA driver installed. NVIDIA drivers are pre-installed on some Amazon Machine Images (AMIs).
  Otherwise, you can manually install the driver. For more information, see [Install NVIDIA drivers on Linux instances](../../../AWSEC2/latest/UserGuide/install-nvidia-driver.md "../../../AWSEC2/latest/UserGuide/install-nvidia-driver.md").

###### Note

AWS Systems Manager (SSM agent) is pre-installed on some [Amazon Machine Images (AMIs)](../../../systems-manager/latest/userguide/ami-preinstalled-agent.md "../../../systems-manager/latest/userguide/ami-preinstalled-agent.md")
provided by AWS and trusted third-parties. If the agent isn't installed, you can install it manually using the procedure
for your operating system type.

- [Manually installing and uninstalling SSM Agent on EC2 instances for Linux](../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md")
- [Manually installing and uninstalling SSM Agent on EC2 instances for macOS](../../../systems-manager/latest/userguide/manually-install-ssm-agent-macos.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-macos.md")
- [Manually installing and uninstalling SSM Agent on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/manually-install-ssm-agent-windows.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-windows.md")

## Benefits

The solution delivers NVIDIA monitoring, providing valuable insights for the following use cases:

- Analyze GPU and memory usage for performance bottlenecks or the need for additional resources.
- Monitor temperature and power draw to ensure GPUs operate within safe limits.
- Evaluate encoder performance for GPU video workloads.
- Verify PCIe connectivity for expected generation and width.
- Monitor GPU clock speeds to detect scaling and throttling issues.

Below are the key advantages of the solution:

- Automates metric collection for NVIDIA using CloudWatch agent configuration, eliminating manual instrumentation.
- Provides a pre-configured, consolidated CloudWatch dashboard for NVIDIA metrics. The dashboard will automatically handle metrics
  from new NVIDIA EC2 instances configured using the solution, even if those metrics don't exist when you first create the dashboard.

The following image is an example of the dashboard for this solution.

![Example dashboard for NVIDIA GPU solution.](images/NVIDIADashboard.png)

### Costs

This solution creates and uses resources in your account. You are charged for standard usage, including the following:

- All metrics collected by the CloudWatch agent are charged as custom metrics. The number of metrics used by this solution depends on the number
  of EC2 hosts.
  - Each EC2 host configured for the solution publishes a total of 17 metrics per GPU.

- One custom dashboard.
- API operations requested by the CloudWatch agent to publish the metrics. With the default configuration for this solution,
  the CloudWatch agent calls the **PutMetricData** once every minute for each EC2 host. This means the
  **PutMetricData** API will be called `30*24*60=43,200` in a 30-day month for each EC2 host.

For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

The pricing calculator can help you estimate approximate monthly costs for using this solution.

###### To use the pricing calculator to estimate your monthly solution costs

1. Open the [Amazon CloudWatch pricing calculator](https://calculator.aws/#/createCalculator/CloudWatch "https://calculator.aws/#/createCalculator/CloudWatch").
2. For **Choose a Region**, select the Region where you would like to deploy the solution.
3. In the **Metrics** section, for **Number of metrics**,
   enter `17 * average number of GPUs per EC2 host * number of EC2 instances configured for this solution`.
4. In the **APIs** section, for **Number of API requests**,
   enter `43200 * number of EC2 instances configured for this solution`.
5. By default, the CloudWatch agent performs one **PutMetricData** operation each minute for each EC2 host.
6. In the **Dashboards and Alarms** section, for **Number of
   Dashboards**, enter `1`.
7. You can see your monthly estimated costs at the bottom of the pricing calculator.

## CloudWatch agent configuration for this

solution

The CloudWatch agent is software that runs continuously and autonomously on your servers and
in containerized environments.
It collects metrics, logs, and traces from your infrastructure and applications and sends
them to CloudWatch and X-Ray.

For more information about the CloudWatch agent, see [Collect metrics, logs, and traces using the CloudWatch
agent](Install-CloudWatch-Agent.md "Install-CloudWatch-Agent.md").

The agent configuration in this solution collects a set of metrics to help you get
started monitoring and observing your NVIDIA GPU. The CloudWatch agent can be configured to
collect more NVIDIA GPU metrics than the dashboard displays by default. For a list of all
NVIDIA GPU metrics that you can collect, see [Collect NVIDIA GPU metrics](CloudWatch-Agent-NVIDIA-GPU.md "CloudWatch-Agent-NVIDIA-GPU.md").

### Agent configuration for this solution

The metrics collected by the agent are defined in the agent configuration. The
solution provides agent configurations to collect
the recommended metrics with suitable dimensions for the solution's dashboard.

Use the following CloudWatch agent configuration on EC2 instances with NVIDIA GPUs.
Configuration will be stored as a parameter in SSM's Parameter Store, as detailed later in
[Step 2: Store the recommended CloudWatch agent configuration file in Systems Manager Parameter Store](#Solution-NVIDIA-GPU-Agent-Step2 "#Solution-NVIDIA-GPU-Agent-Step2").

```
{
    "metrics": {
        "namespace": "CWAgent",
        "append_dimensions": {
            "InstanceId": "${aws:InstanceId}"
        },
        "metrics_collected": {
            "nvidia_gpu": {
                "measurement": [
                    "utilization_gpu",
                    "temperature_gpu",
                    "power_draw",
                    "utilization_memory",
                    "fan_speed",
                    "memory_total",
                    "memory_used",
                    "memory_free",
                    "pcie_link_gen_current",
                    "pcie_link_width_current",
                    "encoder_stats_session_count",
                    "encoder_stats_average_fps",
                    "encoder_stats_average_latency",
                    "clocks_current_graphics",
                    "clocks_current_sm",
                    "clocks_current_memory",
                    "clocks_current_video"
                ],
                "metrics_collection_interval": 60
            }
        }
    },
    "force_flush_interval": 60
}
```

## Deploy the agent for your solution

There are several approaches for installing the CloudWatch agent, depending on the use case. We recommend using Systems Manager for this solution.
It provides a console experience and makes it simpler to manage a fleet of managed servers within a single AWS account.
The instructions in this section use Systems Manager and are intended for when you don't have the CloudWatch agent running with existing configurations.
You can check whether the CloudWatch agent is running by following the steps in [Verify that the CloudWatch agent
is running](troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running "troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running").

If you are already running the CloudWatch agent on the EC2 hosts where the workload is deployed and managing agent configurations,
you can skip the instructions in this section and follow your existing deployment mechanism to update the configuration.
Be sure to merge the agent configuration of NVIDIA GPU with your existing agent configuration, and then deploy the merged configuration.
If you are using Systems Manager to store and manage the configuration for the CloudWatch agent, you can merge the configuration to the existing parameter value.
For more information, see [Managing CloudWatch agent configuration files](../../../prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/create-store-cloudwatch-configurations.md "../../../prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/create-store-cloudwatch-configurations.md").

###### Note

Using Systems Manager to deploy the following CloudWatch agent configurations will replace or overwrite any existing CloudWatch agent
configuration on your EC2 instances. You can modify this configuration to suit your unique environment or use case.
The metrics defined in configuration are the minimum required for the dashboard provided the solution.

The deployment process includes the following steps:

- Step 1: Ensure that the target EC2 instances have the required IAM permissions.
- Step 2: Store the recommended agent configuration file in the Systems Manager Parameter Store.
- Step 3: Install the CloudWatch agent on one or more EC2 instances using an CloudFormation stack.
- Step 4: Verify the agent setup is configured properly.

### Step 1: Ensure the target EC2 instances have the required IAM permissions

You must grant permission for Systems Manager to install and configure the CloudWatch agent. You must also grant permission for the CloudWatch agent
to publish telemetry from your EC2 instance to CloudWatch. Make sure that the IAM role attached to the instance has the
**CloudWatchAgentServerPolicy** and **AmazonSSMManagedInstanceCore** IAM policies attached.

- After the role is created, attach the role to your EC2 instances. To attach a role to an EC2 instance, follow the steps in
  [Attach an IAM role to an instance](../../../AWSEC2/latest/UserGuide/attach-iam-role.md "../../../AWSEC2/latest/UserGuide/attach-iam-role.md").

### Step 2: Store the recommended CloudWatch agent configuration file in Systems Manager Parameter Store

Parameter Store simplifies the installation of the CloudWatch agent on an EC2 instance by securely storing and managing configuration parameters,
eliminating the need for hard-coded values. This ensures a more secure and flexible deployment process, enabling centralized
management and easier updates to configurations across multiple instances.

Use the following steps to store the recommended CloudWatch agent configuration file as a parameter in Parameter Store.

###### To create the CloudWatch agent configuration file as a parameter

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Verify that the selected Region on the console is the Region where the NVIDIA GPU workload is running.
3. From the navigation pane, choose **Application Management**, **Parameter Store**.
4. Follow these steps to create a new parameter for the configuration.
   1. Choose **Create parameter**.
   2. In the **Name** box, enter a name that you'll use to reference the CloudWatch agent configuration file in later steps.
      For example, `AmazonCloudWatch-NVIDIA-GPU-Configuration`.
   3. (Optional) In the **Description** box, type a description for the parameter.
   4. For **Parameter tier**, choose **Standard**.
   5. For **Type**, choose **String**.
   6. For **Data type**, choose **text**.
   7. In the **Value** box, paste the corresponding JSON block that was listed in
      [Agent configuration for this solution](#Solution-NVIDIA-GPU-Agent-Config "#Solution-NVIDIA-GPU-Agent-Config").
   8. Choose **Create parameter**.

### Step 3: Install the CloudWatch agent and apply the configuration using an CloudFormation template

You can use AWS CloudFormation to install the agent and configure it to use the CloudWatch agent configuration that you created in the previous steps.

###### To install and configure the CloudWatch agent for this solution

1. Open the CloudFormation **Quick create stack** wizard using this link: [https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json](cloudformation/home.md#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json "cloudformation/home.md#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json").
2. Verify that the selected Region on the console is the Region where the NVIDIA GPU workload is running.
3. For **Stack name**, enter a name to identity this stack, such as `CWAgentInstallationStack`.
4. In the **Parameters** section, specify the following:
   1. For **CloudWatchAgentConfigSSM**, enter the name of the Systems Manager parameter for the agent configuration
      that you created earlier, such as `AmazonCloudWatch-NVIDIA-GPU-Configuration`.
   2. To select the target instances, you have two options.
      1. For **InstanceIds**, specify a comma-delimited list of instance IDs list of instance IDs where you want to install
         the CloudWatch agent with this configuration. You can list a single instance or several instances.
      2. If you are deploying at scale, you can specify the **TagKey** and the corresponding **TagValue**
         to target all EC2 instances with this tag and value. If you specify a **TagKey**, you must specify a corresponding
         **TagValue**. (For an Amazon EC2 Auto Scaling group, specify `aws:autoscaling:groupName` for the **TagKey**
         and specify the Amazon EC2 Auto Scaling group name for the **TagValue** to deploy to all instances within the Amazon EC2 Auto Scaling group.)

5. Review the settings, then choose **Create stack**.

If you want to edit the template file first to customize it, choose the **Upload a template file** option under
**Create Stack Wizard** to upload the edited template. For more information, see [Creating a stack on CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md").

###### Note

After this step is completed, this Systems Manager parameter will be associated with the CloudWatch agents running in the targeted instances.
This means that:

1. If the Systems Manager parameter is deleted, the agent will stop.
2. If the Systems Manager parameter is edited, the configuration changes will automatically apply to the agent at the scheduled frequency
   which is 30 days by default.
3. If you want to immediately apply changes to this Systems Manager parameter, you must run this step again. For more information about associations,
   see [Working with associations in Systems Manager](../../../systems-manager/latest/userguide/state-manager-associations.md "../../../systems-manager/latest/userguide/state-manager-associations.md").

### Step 4: Verify the agent setup is configured properly

You can verify whether the CloudWatch agent is installed by following the steps in [Verify that the CloudWatch agent
is running](troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running "troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running"). If the CloudWatch agent is not installed and running,
make sure you have set up everything correctly.

- Be sure you have attached a role with correct permissions for the EC2 instance as described in
  [Step 1: Ensure the target EC2 instances have the required IAM permissions](#Solution-NVIDIA-GPU-Agent-Step1 "#Solution-NVIDIA-GPU-Agent-Step1").
- Be sure you have correctly configured the JSON for the Systems Manager parameter. Follow the steps in
  [Troubleshooting
  installation of the CloudWatch agent with CloudFormation](Install-CloudWatch-Agent-New-Instances-CloudFormation.md#CloudWatch-Agent-CloudFormation-troubleshooting "Install-CloudWatch-Agent-New-Instances-CloudFormation.md#CloudWatch-Agent-CloudFormation-troubleshooting").

If everything is set up correctly, then you should see the NVIDIA GPU metrics being published to CloudWatch.
You can check the CloudWatch console to verify they are being published.

###### To verify that NVIDIA GPU metrics are being published to CloudWatch

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Metrics**, **All metrics**.
3. Make sure you've selected the Region where you deployed the solution, and choose **Custom namespaces**,
   **CWAgent**.
4. Search for the metrics mentioned in [Agent configuration for this solution](#Solution-NVIDIA-GPU-Agent-Config "#Solution-NVIDIA-GPU-Agent-Config"), such as `nvidia_smi_utilization_gpu`.
   If you see results for these metrics, then the metrics are being published to CloudWatch.

## Create the NVIDIA GPU solution dashboard

The dashboard provided by this solution presents NVIDIA GPUs metrics by aggregating and presenting metrics
across all instances. The dashboard shows a breakdown of the top contributors (top 10 per metric widget) for each metric. This helps
you to quickly identify outliers or instances that significantly contribute to the observed metrics.

To create the dashboard, you can use the following options:

- Use CloudWatch console to create the dashboard.
- Use AWS CloudFormation console to deploy the dashboard.
- Download the AWS CloudFormation infrastructure as code and integrate it as part of your continuous integration (CI) automation.

By using the CloudWatch console to create a dashboard, you can preview the dashboard before actually creating and being charged.

###### Note

The dashboard created with CloudFormation in this solution displays metrics from the Region where the solution is deployed. Be sure to
create the CloudFormation stack in the Region where your NVIDIA GPU metrics are published.

If you've specified a custom namespace other than CWAgent in the CloudWatch agent configuration, you'll have to change the CloudFormation
template for the dashboard to replace CWAgent with the customized namespace you are using.

###### To create the dashboard via CloudWatch Console

1. Open the CloudWatch Console **Create Dashboard** using this link:
   [https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=NvidiaGpuOnEc2&referrer=os-catalog](https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=NvidiaGpuOnEc2&referrer=os-catalog "https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=NvidiaGpuOnEc2&referrer=os-catalog") .
2. Verify that the selected Region on the console is the Region where the NVIDIA GPU workload is running.
3. Enter the name of the dashboard, then choose **Create Dashboard**.

To easily differentiate this dashboard from similar dashboards in other Regions, we recommend including the Region name
in the dashboard name, such as `NVIDIA-GPU-Dashboard-us-east-1`. 4. Preview the dashboard and choose **Save** to create the dashboard.

###### To create the dashboard via CloudFormation

1. Open the CloudFormation **Quick create stack** wizard using this link: [https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/NVIDIA_GPU_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json](cloudformation/home.md#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/NVIDIA_GPU_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json "cloudformation/home.md#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/NVIDIA_GPU_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json").
2. Verify that the selected Region on the console is the Region where the NVIDIA GPU workload is running.
3. For **Stack name**, enter a name to identity this stack, such as `NVIDIA-GPU-DashboardStack`.
4. In the **Parameters** section, specify the name of the dashboard under the **DashboardName** parameter.
5. To easily differentiate this dashboard from similar dashboards in other Regions, we recommend including the Region name in the
   dashboard name, such as `NVIDIA-GPU-Dashboard-us-east-1`.
6. Acknowledge access capabilities for transforms under **Capabilities and transforms**. Note that CloudFormation doesn't
   add any IAM resources.
7. Review the settings, then choose **Create stack**.
8. After the stack status is **CREATE_COMPLETE**, choose the **Resources** tab under the created stack and then choose the link under **Physical
   ID** to go to the dashboard. You can also access the dashboard in the CloudWatch
   console by choosing **Dashboards** in the left navigation pane of the
   console, and finding the dashboard name under **Custom Dashboards**.

If you want to edit the template file to customize it for any purpose, you can use **Upload
a template file** option under **Create Stack Wizard** to upload
the edited template. For more information, see [Creating a stack on
CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md"). You can use this link to download the template: [https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/NVIDIA_GPU_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json](https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/NVIDIA_GPU_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json "https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/NVIDIA_GPU_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json")
.

### Get started with the NVIDIA GPU dashboard

Here are a few tasks that you can try out with the new NVIDIA GPU dashboard. These tasks allow you to validate that the dashboard
is working correctly and provide you some hands-on experience using it to monitor your NVIDIA GPUs. As you try these out, you'll get
familiar with navigating the dashboard and interpreting the visualized metrics.

**Review GPU utilization**

From the **Utilization** section, find the **GPU Utilization** and **Memory Utilization** widgets. These show the percentage of time the GPU
is being actively used for computations and the percentage of global memory being read or written, respectively. High utilization could
indicate potential performance bottlenecks or the need for additional GPU resources.

**Analyze GPU memory usage**

In the **Memory** section, find the **Total Memory**, **Used Memory**, and **Free Memory** widgets. These provide insights into the overall memory
capacity of the GPUs and how much memory is currently being consumed or available. Memory pressure could lead to performance issues or
out-of-memory errors, so it's important to monitor these metrics and ensure sufficient memory is available for your workloads.

**Monitor temperature and power draw**

In the **Temperature / Power** section, find the **GPU Temperature** and **Power Draw** widgets. These metrics are essential for ensuring that
your GPUs are operating within safe thermal and power limits.

**Identify encoder performance**

In the **Encoder** section, find the **Encoder Session Count**, **Average FPS**, and **Average Latency** widgets. These metrics are relevant if
you're running video encoding workloads on your GPUs. Monitor these metrics to ensure that your encoders are performing optimally and
identify any potential bottlenecks or performance issues.

**Check PCIe link status**

In the **PCIe** section, find the **PCIe Link Generation** and **PCIe Link Width** widgets. These metrics provide information about the PCIe
link connecting the GPU to the host system. Ensure that the link is operating at the expected generation and width to avoid potential
performance limitations due to PCIe bottlenecks.

**Review GPU clocks**

In the **Clock** section, find the **Graphics Clock**, **SM Clock**, **Memory Clock**, and **Video Clock** widgets. These metrics show the current
operating frequencies of various GPU components. Monitoring these clocks can help identify potential issues with GPU clock scaling or
frequency throttling, which could impact performance.
