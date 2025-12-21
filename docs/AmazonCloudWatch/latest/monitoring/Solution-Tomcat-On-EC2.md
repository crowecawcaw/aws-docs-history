# CloudWatch solution: Tomcat workload on Amazon EC2

This solution helps you configure out-of-the-box metric collection
using CloudWatch agents for Tomcat server running on EC2 instances.
Additionally, it helps you set up a pre-configured CloudWatch dashboard.
For general information about all CloudWatch observability solutions, see [CloudWatch observability solutions](Monitoring-Solutions.md "Monitoring-Solutions.md").

###### Topics

- [Requirements](#Solution-Tomcat-On-EC2-Requirements "#Solution-Tomcat-On-EC2-Requirements")
- [Benefits](#Solution-Tomcat-On-EC2-Benefits "#Solution-Tomcat-On-EC2-Benefits")
- [Costs](#Solution-Tomcat-On-EC2-Costs "#Solution-Tomcat-On-EC2-Costs")
- [CloudWatch agent configuration for this solution](#Solution-Tomcat-CloudWatch-Agent "#Solution-Tomcat-CloudWatch-Agent")
- [Deploy the agent for your solution](#Solution-Tomcat-Agent-Deploy "#Solution-Tomcat-Agent-Deploy")
- [Create the Tomcat solution dashboard](#Solution-Tomcat-Dashboard "#Solution-Tomcat-Dashboard")

## Requirements

This solution is relevant for the following conditions:

- Supported versions: Tomcat versions 9, 10.1, and 11 (beta)
- Compute: Amazon EC2
- Supports up to 500 EC2 instances across all Tomcat workloads in a given AWS Region
- Latest version of CloudWatch agent
- SSM agent installed on EC2 instance

###### Note

AWS Systems Manager (SSM agent) is pre-installed on
some [Amazon Machine Images (AMIs)](../../../systems-manager/latest/userguide/ami-preinstalled-agent.md "../../../systems-manager/latest/userguide/ami-preinstalled-agent.md")
provided by AWS and trusted third-parties. If the agent isn't installed, you can install it manually using the procedure
for your operating system type.

    + [Manually installing and uninstalling SSM Agent on EC2 instances for Linux](../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md")
    + [Manually installing and uninstalling SSM Agent on EC2 instances for macOS](../../../systems-manager/latest/userguide/manually-install-ssm-agent-macos.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-macos.md")
    + [Manually installing and uninstalling SSM Agent on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/manually-install-ssm-agent-windows.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-windows.md")

## Benefits

The solution delivers Tomcat server monitoring, providing valuable insights for the
following use cases:

- Detect Tomcat server errors and performance issues.
- Monitor network traffic for data transfer problems.
- Track thread usage and active user sessions.
- Analyze underlying JVM performance for Tomcat server.

Below are the key advantages of the solution:

- Automates metric collection for Apache Tomcat and the underlying JVM using
  CloudWatch agent configuration, eliminating manual instrumentation.
- Provides a pre-configured, consolidated CloudWatch dashboard for Apache Tomcat and
  JVM metrics. The dashboard will automatically handle metrics
  from new Tomcat EC2 instances configured using the solution, even if those metrics don't
  exist when you first create the dashboard. It also allows
  you to group the metrics into logical applications for easier focus and management.

The following image is an example of the dashboard for this solution.

![Example dashboard for Apache Tomcat solution.](images/TomcatDashboard.png)

## Costs

This solution creates and uses resources in your account. You are charged for standard usage, including the following:

- All metrics collected by the CloudWatch agent
  are charged as custom metrics. The number of metrics used by this solution depends on the number
  of EC2 hosts.
  - Each Tomcat host configured for the solution publishes a total of
    27 metrics plus one metric (`disk_used_percent`) for which the metric count
    depends on number of disk paths for that host.

- One custom dashboard.
- API operations requested by the CloudWatch agent to publish the metrics. With the default
  configuration for this solution, the CloudWatch agent calls the **PutMetricData** once every minute.
  This means the **PutMetricData** API will be called `30*24*60=43,200`
  in a 30-day month for each EC2 host.

For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

The pricing calculator can help you estimate approximate monthly costs for using this solution.

###### To use the pricing calculator to estimate your monthly solution costs

1. Open the [Amazon CloudWatch pricing calculator](https://calculator.aws/#/createCalculator/CloudWatch "https://calculator.aws/#/createCalculator/CloudWatch").
2. In the **Metrics** section, for **Number of metrics**,
   enter `(27 + average number of disk paths per EC2 host) * number of EC2 instances configured for this solution`.
3. In the **APIs** section, for **Number of API
   requests**, enter `43200 * number of EC2 instances
configured for this solution`.

By default, the solution performs one **PutMetricData** operation each minute for each EC2 host. 4. In the **Dashboards and Alarms** section, for **Number of Dashboards**, enter `1`. 5. You can see your monthly estimated costs at the bottom of the
pricing calculator.

## CloudWatch agent configuration for this solution

The CloudWatch agent is software that runs continuously and autonomously on your servers and in containerized environments. It collects metrics, logs, and traces from your
infrastructure and applications and sends them to CloudWatch and X-Ray.

For more information about the CloudWatch agent, see [Collect metrics, logs, and traces using the CloudWatch
agent](Install-CloudWatch-Agent.md "Install-CloudWatch-Agent.md").

The agent configuration in this solution collects the foundational metrics for Tomcat, JVM, and EC2.
The CloudWatch agent can be configured to collect more JVM metrics than the dashboard displays by default.
For a list of all Tomcat metrics that you can collect, see
[Collect Tomcat metrics](CloudWatch-Agent-JMX-metrics.md#CloudWatch-Agent-Tomcat-metrics "CloudWatch-Agent-JMX-metrics.md#CloudWatch-Agent-Tomcat-metrics"). For a list of all JVM metrics that you can collect, see
[Collect JVM metrics](CloudWatch-Agent-JMX-metrics.md#CloudWatch-Agent-JVM-metrics "CloudWatch-Agent-JMX-metrics.md#CloudWatch-Agent-JVM-metrics"). For a list of Amazon EC2 metrics, see
[Metrics collected by the CloudWatch
agent on Linux and macOS instances](metrics-collected-by-CloudWatch-agent.md#linux-metrics-enabled-by-CloudWatch-agent "metrics-collected-by-CloudWatch-agent.md#linux-metrics-enabled-by-CloudWatch-agent").

**Expose JMX ports for the Tomcat server**

The CloudWatch agent relies on JMX to collect the metrics related to the Tomcat server and JVM process.
To make this possible, you must expose the JMX port from your servers. To enable a JMX port for monitoring and management,
you would set system properties for your Tomcat servers. You can use the environment variable `CATALINA_OPTS`  
 to set the required system properties for Tomcat. Review the startup scripts and configuration files of your Tomcat server
on the best place to set the environment variable. Be sure that you specify an unused port number.
You will need to restart the server after the change.

```
export CATALINA_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=<<port-number>> -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false"
```

This example sets up unauthenticated JMX. If your security policies/requirements require you to enable JMX with password authentication
or SSL for remote access, refer to the [JMX documentation](https://docs.oracle.com/en/java/javase/17/management/monitoring-and-management-using-jmx-technology.html "https://docs.oracle.com/en/java/javase/17/management/monitoring-and-management-using-jmx-technology.html")  
 to set the required property.

To verify the JMX port, run `ps aux | grep jmxremote.port`. The results should show that the JMX port was set on the JVM processes.

### Agent configuration for Tomcat solution

The metrics collected by the agent are defined in the agent configuration. The solution provides agent configurations to
collect the recommended metrics with suitable dimensions for the solution’s dashboard.

The steps for deploying the solution are described later in [Deploy the agent for your solution](#Solution-Tomcat-Agent-Deploy "#Solution-Tomcat-Agent-Deploy").
The following information is intended to help you understand how to customize the agent configuration for your environment.

You must customize some parts of the following agent configuration for your environment:

- The JMX port number is the port number that you configured in the previous section of this documentation.
  The port number is in the `endpoint` line in the configuration.
- `AppName` – This is used as a dimension for the Tomcat application metrics collected.
  Provide a meaningful name that represents the grouping for the instances that run the Tomcat application.
- `ProcessGroupName` – This is used as a dimension for JVM metrics collected for Tomcat hosts. Provide the value
  which is the same as `AppName` above. This is to enable viewing the JVM metrics
  of the same Tomcat app group as server metrics under the solution dashboard.

For example, if you have two Tomcat apps running in the same AWS account, one for the `billing-system` application and
another for the `order-system` application, you can set the `AppName`
and `ProcessGroupName` dimensions accordingly in the agent configuration of each instance.

- For the `billing-system` application instances, set `AppName=billing-system`
  and `ProcessGroupName=billing-system`.
- For the `order-system` application instances, set `AppName=order-system` and
  `ProcessGroupName=order-system`.

When you follow these guidelines, the solution will automatically group the metrics based on the
`AppName` and `ProcessGroupName` dimensions. The dashboard will include
dropdown options to select and view metrics for a specific Tomcat application, allowing you
to monitor the performance of individual applications separately.

### Agent configuration for Tomcat hosts

Use the following CloudWatch agent configuration on EC2 instances where your Tomcat applications are deployed.
Configuration will be stored as a parameter in SSM's Parameter Store,
as detailed later in [Step 2: Store the recommended CloudWatch agent configuration file in Systems Manager Parameter Store](#Solution-Tomcat-Agent-Step2 "#Solution-Tomcat-Agent-Step2").

Replace `AppName` with a meaningful name that represents the Tomcat application the instances are part of.
Replace `port-number` with the JMX port of your Tomcat server. If JMX was enabled with password authentication
or SSL for remote access, see [Collect Java Management Extensions (JMX)
metrics](CloudWatch-Agent-JMX-metrics.md "CloudWatch-Agent-JMX-metrics.md") for information
about setting up TLS or authorization in agent configuration as required.

The EC2 metrics shown in this configuration (configuration shown outside the JMX block)
only work for Linux and macOS instances. If you are using Windows instances, you can choose to omit these metrics in the configuration.
For information about metrics collected on Windows instances, see [Metrics collected by the CloudWatch
agent on Windows Server instances](metrics-collected-by-CloudWatch-agent.md#windows-metrics-enabled-by-CloudWatch-agent "metrics-collected-by-CloudWatch-agent.md#windows-metrics-enabled-by-CloudWatch-agent").

```
{
  "metrics": {
    "namespace": "CWAgent",
    "append_dimensions": {
      "InstanceId": "${aws:InstanceId}"
    },
    "metrics_collected": {
      "jmx": [
        {
          "endpoint": "localhost:`port-number`",
          "tomcat": {
            "measurement": [
              "tomcat.sessions",
              "tomcat.errors",
              "tomcat.processing_time",
              "tomcat.traffic",
              "tomcat.max_time",
              "tomcat.request_count",
              "tomcat.threads"
            ]
          },
          "append_dimensions": {
            "AppName": "`AppName`"
          }
        },
        {
          "endpoint": "localhost:`port-number`",
          "jvm": {
            "measurement": [
              "jvm.classes.loaded",
              "jvm.gc.collections.count",
              "jvm.gc.collections.elapsed",
              "jvm.memory.heap.committed",
              "jvm.memory.heap.max",
              "jvm.memory.heap.used",
              "jvm.memory.nonheap.committed",
              "jvm.memory.nonheap.max",
              "jvm.memory.nonheap.used",
              "jvm.threads.count"
            ]
          },
          "append_dimensions": {
            "ProcessGroupName": "`AppName`"
          }
        }
      ],
      "disk": {
        "measurement": [
          "used_percent"
        ]
      },
      "mem": {
        "measurement": [
          "used_percent"
        ]
      },
      "swap": {
        "measurement": [
          "used_percent"
        ]
      },
      "netstat": {
        "measurement": [
          "tcp_established",
          "tcp_time_wait"
        ]
      }
    }
  }
}
```

## Deploy the agent for your solution

There are several approaches for installing the CloudWatch agent, depending on the use case.
We recommend using Systems Manager for this solution. It provides a console experience and makes it simpler to
manage a fleet of managed servers within a single AWS account. The instructions in this section
use Systems Manager and are intended for when you don’t have the CloudWatch agent running with existing configurations. You can check whether the CloudWatch agent is
running by following the steps in [Verify that the CloudWatch agent
is running](troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running "troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running").

If you are already running the CloudWatch agent on the
EC2 hosts where the JVM application is deployed and managing the agent configurations,
you can skip the instructions in this section and follow your existing deployment
mechanism to update the configuration. Be sure to merge the agent configuration
of JVM with your existing agent configuration, and then deploy the merged configuration.
If you are using Systems Manager to store and manage the configuration for the CloudWatch agent, you can merge the configuration
to the existing parameter value. For more information, see
[Managing CloudWatch agent configuration files](../../../prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/create-store-cloudwatch-configurations.md "../../../prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/create-store-cloudwatch-configurations.md").

###### Note

Using Systems Manager to deploy the following CloudWatch agent configurations will replace or overwrite any existing CloudWatch agent
configuration on your EC2 instances. You can modify this configuration to suit your unique environment or use case.
The metrics defined in this solution are the minimum required for the recommended dashboard.

The deployment process includes the following steps:

- Step 1: Ensure that the target EC2 instances have the required IAM permissions.
- Step 2: Store the recommended agent configuration file in the Systems Manager Parameter Store.
- Step 3: Install the CloudWatch agent on one or more EC2 instances using an CloudFormation stack.
- Step 4: Verify the agent setup is configured properly.

### Step 1: Ensure the target EC2 instances have the required IAM permissions

You must grant permission for Systems Manager to install and configure the CloudWatch agent. You must also grant permission for the CloudWatch agent to publish telemetry from your
EC2 instance to CloudWatch. Make sure that the IAM role attached to the instance has the **CloudWatchAgentServerPolicy** and
**AmazonSSMManagedInstanceCore** IAM policies attached.

- After the role is created, attach the role to your EC2 instances. Follow the steps in [Launch an instance with an IAM role](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#launch-instance-with-role "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#launch-instance-with-role")
  to attach a role while launching a new EC2 instance. To attach a role to an existing EC2 instance,
  follow the steps in [Attach an IAM role to an instance](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role").

### Step 2: Store the recommended CloudWatch agent configuration file in Systems Manager Parameter Store

Parameter Store simplifies the installation of the CloudWatch agent on an EC2 instance by securely storing and managing configuration parameters,
eliminating the need for hard-coded values. This ensures a more secure and flexible deployment process, enabling centralized
management and easier updates to configurations across multiple instances.

Use the following steps to store the recommended CloudWatch agent configuration file as a
parameter in Parameter Store.

###### To create the CloudWatch agent configuration file as a parameter

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. From the navigation pane, choose **Application Management**, **Parameter Store**.
3. Follow these steps to create a new parameter for the configuration.
   1. Choose **Create parameter**.
   2. In the **Name** box, enter a name that you'll use
      to reference the CloudWatch agent configuration file in later steps.
      For example, `AmazonCloudWatch-Tomcat-Configuration`.
   3. (Optional) In the **Description** box, type a description for
      the parameter.
   4. For **Parameter tier**, choose **Standard**.
   5. For **Type**, choose **String**.
   6. For **Data type**, choose **text**.
   7. In the **Value** box, paste the corresponding JSON block
      that was listed in [Agent configuration for Tomcat hosts](#Solution-Agent-Configuration-Tomcat-Host "#Solution-Agent-Configuration-Tomcat-Host"). Be sure to customize
      the grouping dimension value and port number as described.
   8. Choose **Create parameter**.

### Step 3: Install the CloudWatch agent and apply the configuration using an CloudFormation template

You can use AWS CloudFormation to install the agent and configure it to use the CloudWatch agent
configuration that you created in the previous steps.

###### To install and configure the CloudWatch agent for this solution

1. Open the CloudFormation **Quick create stack** wizard using this link:
   [https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json](https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json "https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json").
2. Verify that the selected Region on the console is the Region where the Tomcat workload is running.
3. For **Stack name**, enter a name to identity this stack,
   such as `CWAgentInstallationStack`.
4. In the **Parameters** section, specify the following:
   1. For **CloudWatchAgentConfigSSM**, enter the name of the Systems Manager parameter for the agent configuration
      that you created earlier, such as `AmazonCloudWatch-Tomcat-Configuration`.
   2. To select the target instances, you have two options.
      1. For **InstanceIds**, specify a comma-delimited list of instance IDs
         list of instance IDs where you want to install the CloudWatch agent with this configuration.
         You can list a single instance or several instances.
      2. If you are deploying at scale, you can specify the **TagKey** and the corresponding **TagValue**
         to target all EC2 instances with this tag and value. If you specify a **TagKey**, you must specify a corresponding **TagValue**.
         (For an Auto Scaling group, specify `aws:autoscaling:groupName` for the **TagKey** and specify the Auto Scaling group name for
         the **TagValue** to deploy to all instances within the Auto Scaling group.)

      If you specify both the **InstanceIds** and the **TagKeys** parameters,
      the **InstanceIds** will take precedence and the tags will be ignored.

5. Review the settings, then choose **Create stack**.

If you want to edit the template file first to customize it, choose the **Upload a template file** option
under **Create Stack Wizard** to upload the edited template. For more information,
see [Creating a stack on CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md").
You can use the following link to download the template: [https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json](https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json "https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json").

###### Note

After this step is completed, this Systems Manager parameter will
be associated with the CloudWatch agents running in the targeted instances. This means that:

1. If the Systems Manager parameter is deleted, the agent will stop.
2. If the Systems Manager parameter is edited, the configuration changes will automatically
   apply to the agent at the scheduled frequency which is 30 days by default.
3. If you want to immediately apply changes to this Systems Manager parameter, you must run this step again.
   For more information about associations, see [Working with associations in Systems Manager](../../../systems-manager/latest/userguide/state-manager-associations.md "../../../systems-manager/latest/userguide/state-manager-associations.md").

### Step 4: Verify the agent setup is configured properly

You can verify whether the CloudWatch agent is installed by following the steps in [Verify that the CloudWatch agent
is running](troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running "troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running"). If the CloudWatch agent is
not installed and running, make sure you have set up everything correctly.

- Be sure you have attached a role with correct permissions for the
  EC2 instance as described in [Step 1: Ensure the target EC2 instances have the required IAM permissions](#Solution-Tomcat-Agent-Step1 "#Solution-Tomcat-Agent-Step1").
- Be sure you have correctly configured the JSON for the Systems Manager parameter. Follow the steps in
  [Troubleshooting
  installation of the CloudWatch agent with CloudFormation](Install-CloudWatch-Agent-New-Instances-CloudFormation.md#CloudWatch-Agent-CloudFormation-troubleshooting "Install-CloudWatch-Agent-New-Instances-CloudFormation.md#CloudWatch-Agent-CloudFormation-troubleshooting").

If everything is set up correctly, then you should see the
Tomcat metrics being published to CloudWatch. You can check the CloudWatch console to verify they are being published.

###### To verify that Tomcat metrics are being published to CloudWatch

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Metrics**, **All metrics**.
3. Make sure you've selected the Region where you deployed the solution, and choose **Custom namespaces**,
   **CWAgent**.
4. Search for the metrics mentioned in the agent configuration section of this document, such
   as `tomcat.errors`. If you see results
   for these metrics, then the metrics are being published to CloudWatch.

## Create the Tomcat solution dashboard

This dashboard displays the newly emitted metrics, showing both the Tomcat
application server and the underlying JVM. This dashboard provides a top contributor view
for the health of your Tomcat workload. The top contributor view displays the top 10 per
metric widget. This allows you to identify outliers at a glance. The dashboard also includes
an overview of the cluster by aggregating and presenting metrics across all instances,
providing a high-level summary of the overall health and operational state of the
cluster.

The solution dashboard doesn't display EC2 metrics.
To view EC2 metrics, you'll need to use the EC2 automatic dashboard to see EC2 vended metrics and
use the EC2 console dashboard to see EC2 metrics that are collected by the CloudWatch agent. For more information about automatic dashboards
for AWS services, see [Viewing a CloudWatch dashboard for a
single AWS service](CloudWatch_Automatic_Dashboards_Focus_Service.md "CloudWatch_Automatic_Dashboards_Focus_Service.md").

To create the dashboard, you can use the following options:

- Use CloudWatch console to create the dashboard.
- Use AWS CloudFormation console to deploy the dashboard.
- Download the AWS CloudFormation infrastructure as code and integrate it as part of your continuous integration (CI) automation.

By using the CloudWatch console to create a dashboard, you can preview the dashboard before actually creating and being charged.

###### Note

The dashboard created with CloudFormation in this solution displays metrics from the Region where the solution is deployed.
Be sure to create the CloudFormation stack in the Region where your Tomcat metrics are published.

If you've specified a custom namespace other than `CWAgent` in the CloudWatch agent
configuration, you'll have to change the CloudFormation template for the dashboard to replace
`CWAgent` with the customized namespace you are using.

###### To create the dashboard via CloudWatch Console

###### Note

Solution dashboards currently display garbage collection-related metrics only for the G1 Garbage Collector,
which is the default collector for the latest Java versions.
If you are using a different garbage collection algorithm, the widgets pertaining to garbage collection are empty.
However, you can customize these widgets by changing the dashboard CloudFormation template and applying the appropriate
garbage collection type to the name dimension of the garbage collection-related metrics.
For example, if you are using parallel garbage collection,
change the `name=\"G1 Young Generation\"` to `name=\"Parallel GC\"` of the garbage collection
count metric `jvm.gc.collections.count`.

1. Open the CloudWatch Console **Create Dashboard** using this link:
   [https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=ApacheTomcatOnEc2&referrer=os-catalog](https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=ApacheTomcatOnEc2&referrer=os-catalog "https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=ApacheTomcatOnEc2&referrer=os-catalog") .
2. Verify that the selected Region on the console is the Region where the Tomcat workload is running.
3. Enter the name of the dashboard, then choose **Create Dashboard**.

To easily differentiate this dashboard from similar dashboards in other Regions, we recommend including the Region name
in the dashboard name, such as `TomcatDashboard-us-east-1`. 4. Preview the dashboard and choose **Save** to create the dashboard.

###### To create the dashboard via CloudFormation

1. Open the CloudFormation **Quick create stack** wizard using this link:
   [https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Tomcat_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json](https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Tomcat_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json "https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Tomcat_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json").
2. Verify that the selected Region on the console is the Region where the Tomcat workload is running.
3. For **Stack name**, enter a name to identity this stack,
   such as `TomcatDashboard-us-east-1`.
4. In the **Parameters** section, specify the name of the dashboard under
   the **DashboardName** parameter.
5. To easily differentiate this dashboard from similar dashboards in other Regions,
   we recommend including the Region name in the dashboard name, such as `TomcatDashboard-us-east-1`.
6. Acknowledge access capabilities for transforms under **Capabilities and transforms**.
   Note that CloudFormation doesn't add any IAM resources.
7. Review the settings, then choose **Create stack**.
8. After the stack status is **CREATE_COMPLETE**, choose the **Resources** tab under
   the created stack and then choose the link under **Physical ID** to go to the dashboard. You can also access the
   dashboard in the CloudWatch console by choosing **Dashboards** in the left navigation pane of the console,
   and finding the dashboard name under **Custom Dashboards**.

If you want to edit the template file to customize it for any purpose, you can use **Upload a template file** option
under **Create Stack Wizard** to upload the edited template. For more information, see
[Creating a stack on CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md").
You can use this link to download the template: [https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Tomcat_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json](https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Tomcat_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json "https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Tomcat_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json").

###### Note

Solution dashboards currently display garbage collection-related metrics only for the G1 Garbage Collector,
which is the default collector for the latest Java versions.
If you are using a different garbage collection algorithm, the widgets pertaining to garbage collection are empty.
However, you can customize these widgets by changing the dashboard CloudFormation template and applying the appropriate
garbage collection type to the name dimension of the garbage collection-related metrics.
For example, if you are using parallel garbage collection,
change the `name=\"G1 Young Generation\"` to `name=\"Parallel GC\"` of the garbage collection
count metric `jvm.gc.collections.count`.

### Get started with the Tomcat monitoring dashboard

Here are a few tasks that you can try out with the new Tomcat dashboard.
These tasks allow you to validate that the dashboard is working correctly and
provide you some hands-on experience using it to monitor a Tomcat application.
As you try these out, you'll get familiar with navigating the dashboard and interpreting the visualized metrics.

**Using the dropdown list**

The dashboard provides a dropdown list at the top that you can use
to filter and select the specific Tomcat application that you want to monitor.
To display metrics for a specific Tomcat application, select that application
name in the **Tomcat App** dropdown list.

**Verify application health**

From the **App Overview** section,
find the **Requests**, **Errors**, and **Error Rate** widgets.
These provide a high-level summary of the application's request handling performance.
Look for any abnormally high error counts or rates, which could indicate issues that need investigation.

**Monitor request processing**

In the **Request Processing Time** section, find the
**Max Time** and **Total Time to Process All Requests** widgets.
These metrics help you identify potential performance bottlenecks in request processing.
Look for any servers with significantly higher max processing times compared to others.

**Analyze network traffic**

In the **Network Traffic** section, find the **Sent Traffic** and **Received Traffic** widgets.
These show the amount of data being sent and received by the application over the
network. Unexpectedly high traffic levels could indicate potential issues
with network saturation or inefficient data transfer.

**Investigate thread usage**

In the **Sessions and Threads** section, find the **Busy Threads Count**,
**Threads Count**, and **Sessions** widgets. These metrics provide insights into
the application's thread management and active user sessions. Look for any servers
with an abnormally high number of busy threads or sessions, which could indicate potential resource constraints.
