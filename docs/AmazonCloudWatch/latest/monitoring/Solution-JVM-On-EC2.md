# CloudWatch solution: JVM workload on Amazon EC2

This solution helps you configure out-of-the-box metric collection using CloudWatch agents 
 for JVM application running on EC2 instances. Additionally, it helps you set up a pre-configured CloudWatch dashboard. 
 For general information about all CloudWatch observability solutions, see [CloudWatch observability solutions](Monitoring-Solutions.md "Monitoring-Solutions.md").

###### Topics

* [Requirements](#Solution-JVM-On-EC2-Requirements "#Solution-JVM-On-EC2-Requirements")
* [Benefits](#Solution-JVM-On-EC2-Benefits "#Solution-JVM-On-EC2-Benefits")
* [Costs](#Solution-JVM-On-EC2-Costs "#Solution-JVM-On-EC2-Costs")
* [CloudWatch agent configuration for this solution](#Solution-JVM-CloudWatch-Agent "#Solution-JVM-CloudWatch-Agent")
* [Deploy the agent for your solution](#Solution-JVM-Agent-Deploy "#Solution-JVM-Agent-Deploy")
* [Create the JVM solution dashboard](#Solution-JVM-Dashboard "#Solution-JVM-Dashboard")

## Requirements


This solution is relevant for the following conditions:



* Supported versions: Java LTS versions 8, 11, 17, and 21
* Compute: Amazon EC2
* Supports up to 500 EC2 instances across all JVM workloads in a given AWS Region
* Latest version of CloudWatch agent
* SSM agent installed on EC2 instance


###### Note

AWS Systems Manager (SSM agent) is pre-installed on 
 some [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/systems-manager/latest/userguide/ami-preinstalled-agent.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/ami-preinstalled-agent.html") 
 provided by AWS and trusted third-parties. If the agent isn't installed, you can install it manually using the procedure 
 for your operating system type.



	+ [Manually installing and uninstalling SSM Agent on EC2 instances for Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-linux.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-linux.html")
	+ [Manually installing and uninstalling SSM Agent on EC2 instances for macOS](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-macos.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-macos.html")
	+ [Manually installing and uninstalling SSM Agent on EC2 instances for Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-windows.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-windows.html")

## Benefits


The solution delivers JVM monitoring, providing valuable insights for the following use cases:



* Monitor JVM heap and non-heap memory usage.
* Analyze thread and class loading for concurrency issues.
* Track garbage collection to identify memory leaks.
* Switch between different JVM applications configured via the solution under the same account.

Below are the key advantages of the solution:



* Automates metric collection for JVM using CloudWatch agent configuration, eliminating manual instrumentation.
* Provides a pre-configured, consolidated CloudWatch dashboard for JVM metrics. The dashboard will automatically handle metrics 
 from new JVM EC2 instances configured using the solution, even if those metrics don't exist when you first create the dashboard. 
 It also allows you to group the metrics into logical applications for easier focus and management.

The following image is an example of the dashboard for this solution.



![Example of JVM dashboard](images/JvmDashboard.png)

## Costs


This solution creates and uses resources in your account. You are charged for standard usage, including the following:



* All metrics collected by the CloudWatch agent are charged as custom metrics. The number of metrics used by this solution depends on the number 
 of EC2 hosts.




	+ Each JVM host configured for the solution publishes a total of 18 metrics plus one metric (`disk_used_percent`) 
	 for which the metric count depends on the number of paths for the host.
* One custom dashboard.
* API operations requested by the CloudWatch agent to publish the metrics. With the default
 configuration for this solution, the CloudWatch agent calls the **PutMetricData** once every minute for each
 EC2 host.
 This means the **PutMetricData** API will be called `30*24*60=43,200`
 in a 30-day month for each EC2 host.

For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").


The pricing calculator can help you estimate approximate monthly costs for using this solution. 


###### To use the pricing calculator to estimate your monthly solution costs

1. Open the [Amazon CloudWatch pricing calculator](https://calculator.aws/#/createCalculator/CloudWatch "https://calculator.aws/#/createCalculator/CloudWatch").
2. For **Choose a Region**, select the Region where you would like to deploy the solution.
3. In the **Metrics** section, for **Number of
 metrics**, enter `(18 + average number of disk paths per EC2 host)
 * number of EC2 instances configured for this solution`.
4. In the **APIs** section, for **Number of API requests**,
 enter `43200 * number of EC2 instances configured for this solution`.


By default, the CloudWatch agent performs one **PutMetricData** operation each minute for each EC2 host.
5. In the **Dashboards and Alarms** section, for **Number of Dashboards**, enter `1`.
6. You can see your monthly estimated costs at the bottom of the
 pricing calculator.

## CloudWatch agent configuration for this solution


The CloudWatch agent is software that runs continuously and autonomously on your servers and in containerized environments. It collects metrics, logs, and traces from your 
 infrastructure and applications and sends them to CloudWatch and X-Ray.


For more information about the CloudWatch agent, see [Collect metrics, logs, and traces using the CloudWatch
 agent](Install-CloudWatch-Agent.md "Install-CloudWatch-Agent.md").


The agent configuration in this solution collects the foundational metrics for the solution. The CloudWatch agent can be configured to collect more 
 JVM metrics than the dashboard displays by default. For a list of all JVM metrics that you can collect, see 
 [Collect JVM metrics](CloudWatch-Agent-JMX-metrics.md#CloudWatch-Agent-JVM-metrics "CloudWatch-Agent-JMX-metrics.md#CloudWatch-Agent-JVM-metrics"). For general information about CloudWatch agent configuration, see 
 [Metrics collected by the CloudWatch
 agent](metrics-collected-by-CloudWatch-agent.md "metrics-collected-by-CloudWatch-agent.md").


**Expose JMX ports for the JVM application**


The CloudWatch agent relies on JMX to collect the metrics related to the JVM process. To make this possible, you must expose the JMX port from your JVM application. 
 Instructions for exposing the JMX port depend on the workload type you are using for your JVM application. See the documentation for your application to find these instructions.


In general, to enable a JMX port for monitoring and management, you would set the following system properties for your JVM application. 
 Be sure to specify an unused port number. The following example sets up unauthenticated JMX. If your security policies/requirements require you to enable JMX with password authentication 
 or SSL for remote access, refer to the [JMX documentation](https://docs.oracle.com/en/java/javase/17/management/monitoring-and-management-using-jmx-technology.html "https://docs.oracle.com/en/java/javase/17/management/monitoring-and-management-using-jmx-technology.html")  
 to set the required property.



```
-Dcom.sun.management.jmxremote
-Dcom.sun.management.jmxremote.port=`port-number`
-Dcom.sun.management.jmxremote.authenticate=false 
-Dcom.sun.management.jmxremote.ssl=false
```

Review the starting scripts and configuration files of your application to find the best place to add these arguments. When you run a `.jar`
 file from the command line, this command could look like the following, where `pet-search.jar` is the name of the application jar.



```
$ java -jar -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9999 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false `pet-search.jar`
```

**Agent configuration for this solution**


The metrics collected by the agent are defined in the agent configuration. The solution provides agent configurations to collect the recommended metrics with 
 suitable dimensions for the solution’s dashboard. 


The steps for deploying the solution are described later in [Deploy the agent for your solution](#Solution-JVM-Agent-Deploy "#Solution-JVM-Agent-Deploy"). 
 The following information is intended to help you understand how to customize the agent configuration for your environment.


You must customize some parts of the following agent configuration for your environment:



* The JMX port number is the port number that you configured in the previous section of this documentation. It is in 
 the `endpoint` line in the configuration.
* `ProcessGroupName`– Provide meaningful names for the `ProcessGroupName` dimension. 
 These names should represent the cluster, application, or services grouping for EC2 instances running the same application or process. 
 This helps you to group metrics from instances belonging to the same JVM process group, providing a unified view of cluster, application, 
 and service performance in the solution dashboard.

For example, if you have two Java applications running in the same account, one for the `order-processing` application and another for the `inventory-management` 
 application, you should set the `ProcessGroupName` dimensions accordingly in the agent configuration of each instance.



* For the `order-processing` application instances, set `ProcessGroupName=order-processing`.
* For the `inventory-management` application instances, set `ProcessGroupName=inventory-management`.

When you follow these guidelines, the solution dashboard will automatically group the metrics based on the `ProcessGroupName` 
 dimension. The dashboard will include dropdown options to select and view metrics for a specific process group, allowing you to monitor the 
 performance of individual process groups separately.


### Agent configuration for JVM hosts


Use the following CloudWatch agent configuration on EC2 instances where your Java applications is deployed.
 Configuration will be stored as a parameter in SSM's Parameter Store,
 as detailed later in [Step 2: Store the recommended CloudWatch agent configuration file in Systems Manager Parameter Store](#Solution-JVM-Agent-Step2 "#Solution-JVM-Agent-Step2").


Replace
 `ProcessGroupName` with the name of your process group. Replace `port-number`
 with the JMX port of your Java application. If JMX was enabled with password authentication or SSL for remote access, 
 see [Collect Java Management Extensions (JMX)
 metrics](CloudWatch-Agent-JMX-metrics.md "CloudWatch-Agent-JMX-metrics.md") for information about setting up TLS or authorization in agent configuration as required.


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
            "ProcessGroupName": "`ProcessGroupName`"
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
 manage a fleet of managed servers within a single AWS account. The instructions in this section use Systems Manager and are intended for 
 when you don’t have the CloudWatch agent running with existing configurations. You can check whether the CloudWatch agent is 
 running by following the steps in [Verify that the CloudWatch agent
 is running](troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running "troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running").


If you are already running the CloudWatch agent on the 
 EC2 hosts where the workload is deployed and managing the agent configurations, 
 you can skip the instructions in this section and follow your existing deployment 
 mechanism to update the configuration. Be sure to merge the agent configuration 
 of JVM with your existing agent configuration, and then deploy the merged configuration. 
 If you are using Systems Manager to store and manage the configuration for the CloudWatch agent, you can merge the configuration 
 to the existing parameter value. For more information, see 
 [Managing CloudWatch agent configuration files](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/create-store-cloudwatch-configurations.html "https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/create-store-cloudwatch-configurations.html").


###### Note

Using Systems Manager to deploy the following CloudWatch agent configurations will replace or overwrite any existing CloudWatch agent 
 configuration on your EC2 instances. You can modify this configuration to suit your unique environment or use case. 
 The metrics defined in this solution are the minimum required for the recommended dashboard. 


The deployment process includes the following steps:



* Step 1: Ensure that the target EC2 instances have the required IAM permissions.
* Step 2: Store the recommended agent configuration file in the Systems Manager Parameter Store.
* Step 3: Install the CloudWatch agent on one or more EC2 instances using an AWS CloudFormation stack.
* Step 4: Verify the agent setup is configured properly.

### Step 1: Ensure the target EC2 instances have the required IAM permissions


You must grant permission for Systems Manager to install and configure the CloudWatch agent. You must also grant permission for the CloudWatch agent to publish telemetry from your 
 EC2 instance to CloudWatch. Make sure that the IAM role attached to the instance has the **CloudWatchAgentServerPolicy** and 
 **AmazonSSMManagedInstanceCore** IAM policies attached.



* After the role is created, attach the role to your EC2 instances. Follow the steps in [Launch an instance with an IAM role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#launch-instance-with-role "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#launch-instance-with-role") 
 to attach a role while launching a new EC2 instance. To attach a role to an existing EC2 instance, 
 follow the steps in [Attach an IAM role to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#attach-iam-role "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#attach-iam-role").

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
	 For example, `AmazonCloudWatch-JVM-Configuration`.
	3. (Optional) In the **Description** box, type a description for 
	 the parameter.
	4. For **Parameter tier**, choose **Standard**.
	5. For **Type**, choose **String**.
	6. For **Data type**, choose **text**.
	7. In the **Value** box, paste the corresponding JSON block that 
	 was listed in [Agent configuration for JVM hosts](#Solution-JVM-Agent-Config "#Solution-JVM-Agent-Config"). Be sure to customize the 
	 grouping dimension value and port number as described.
	8. Choose **Create parameter**.

### Step 3: Install the CloudWatch agent and apply the configuration using an AWS CloudFormation template


You can use AWS CloudFormation to install the agent and configure it to use the CloudWatch agent
 configuration that you created in the previous steps.


###### To install and configure the CloudWatch agent for this solution

1. Open the AWS CloudFormation **Quick create stack** wizard using this link: [https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json](https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json "https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json") .
2. Verify that the selected Region on the console is the Region where the JVM workload is running.
3. For **Stack name**, enter a name to identity this stack, 
 such as `CWAgentInstallationStack`.
4. In the **Parameters** section, specify the following:


	1. For **CloudWatchAgentConfigSSM**, enter the name of the Systems Manager parameter for the agent configuration 
	 that you created earlier, such as `AmazonCloudWatch-JVM-Configuration`.
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
 see [Creating a stack on AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md"). 
 You can use the following link to download the template: [https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json](https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json "https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json") .
 


###### Note

After this step is completed, this Systems Manager parameter will 
 be associated with the CloudWatch agents running in the targeted instances. This means that:


1. If the Systems Manager parameter is deleted, the agent will stop.
2. If the Systems Manager parameter is edited, the configuration changes will automatically 
 apply to the agent at the scheduled frequency which is 30 days by default.
3. If you want to immediately apply changes to this Systems Manager parameter, you must run this step again.
 For more information about associations, see [Working with associations in Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-associations.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-associations.html").

### Step 4: Verify the agent setup is configured properly


You can verify whether the CloudWatch agent is installed by following the steps in [Verify that the CloudWatch agent
 is running](troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running "troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-verify-running"). If the CloudWatch agent is
 not installed and running, make sure you have set up everything correctly.



* Be sure you have attached a role with correct permissions for the 
 EC2 instance as described in [Step 1: Ensure the target EC2 instances have the required IAM permissions](#Solution-JVM-Agent-Step1 "#Solution-JVM-Agent-Step1").
* Be sure you have correctly configured the JSON for the Systems Manager parameter. Follow the steps in 
 [Troubleshooting
 installation of the CloudWatch agent with AWS CloudFormation](Install-CloudWatch-Agent-New-Instances-CloudFormation.md#CloudWatch-Agent-CloudFormation-troubleshooting "Install-CloudWatch-Agent-New-Instances-CloudFormation.md#CloudWatch-Agent-CloudFormation-troubleshooting").

If everything is set up correctly, then you should see the 
 JVM metrics being published to CloudWatch. You can check the CloudWatch console to verify they are being published.


###### To verify that JVM metrics are being published to CloudWatch

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Metrics**, **All metrics**.
3. Make sure you've selected the Region where you deployed the solution, and choose **Custom namespaces**, 
 **CWAgent**.
4. Search for the metrics mentioned in [Agent configuration for JVM hosts](#Solution-JVM-Agent-Config "#Solution-JVM-Agent-Config"), such 
 as `jvm.memory.heap.used`. If you see results
 for these metrics, then the metrics are being published to CloudWatch.

## Create the JVM solution dashboard


The dashboard provided by this solution presents
 metrics for the underlying Java Virtual Machine (JVM) for the server. It offers an overview of the 
 JVM by aggregating and presenting metrics across all instances, providing a high-level summary of the overall 
 health and operational state. Additionally, the dashboard shows a breakdown of the top contributors (top 10 per metric widget) for each metric. 
 This helps you to quickly identify outliers or instances that significantly contribute to the observed metrics.


The solution dashboard doesn't display EC2 metrics. 
 To view EC2 metrics, you'll need to use the EC2 automatic dashboard to see EC2 vended metrics and 
 use the EC2 console dashboard to see EC2 metrics that are collected by the CloudWatch agent. For more information about automatic dashboards
 for AWS services, see [Viewing a CloudWatch dashboard for a
 single AWS service](CloudWatch_Automatic_Dashboards_Focus_Service.md "CloudWatch_Automatic_Dashboards_Focus_Service.md").


To create the dashboard, you can use the following options:



* Use CloudWatch console to create the dashboard.
* Use AWS CloudFormation console to deploy the dashboard.
* Download the AWS CloudFormation infrastructure as code and integrate it as part of your continuous integration (CI) automation.

By using the CloudWatch console to create a dashboard, you can preview the dashboard before actually creating and being charged.


###### Note


 The dashboard created with AWS CloudFormation in this solution displays metrics from the Region where the solution is deployed. 
 Be sure to create the AWS CloudFormation stack in the Region where your JVM metrics are published.
 

If CloudWatch agent metrics are getting published to a different namespace than `CWAgent` (for example, if you've provided 
 a customized namespace), you'll have to change the CloudFormation configuration 
 to replace `CWAgent` with the customized namespace you are using.


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
 [https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=JvmOnEc2&referrer=os-catalog](https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=JvmOnEc2&referrer=os-catalog "https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=JvmOnEc2&referrer=os-catalog") .
2. Verify that the selected Region on the console is the Region where the JVM workload is running.
3. Enter the name of the dashboard, then choose **Create Dashboard**.


To easily differentiate this dashboard from similar dashboards in other Regions, we recommend including the Region name
 in the dashboard name, such as `JVMDashboard-us-east-1`.
4. Preview the dashboard and choose **Save** to create the dashboard.

###### To create the dashboard via AWS CloudFormation

1. Open the AWS CloudFormation **Quick create stack** wizard using this link: [https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/JVM\_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json](https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/JVM_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json "https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/JVM_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json") .
2. Verify that the selected Region on the console is the Region where the JVM workload is running.
3. For **Stack name**, enter a name to identity this stack, 
 such as `JVMDashboardStack`.
4. In the **Parameters** section, specify the name of the dashboard under 
 the **DashboardName** parameter.


To easily differentiate this dashboard from similar dashboards in other Regions, 
 we recommend including the Region name in the dashboard name, such as `JVMDashboard-us-east-1`.
5. Acknowledge access capabilities for transforms under **Capabilities and transforms**. 
 Note that CloudFormation doesn't add any IAM resources.
6. Review the settings, then choose **Create stack**.
7. After the stack status is **CREATE\_COMPLETE**, choose the **Resources** tab under 
 the created stack and then choose the link under **Physical ID** to go to the dashboard. You can also access the 
 dashboard in the CloudWatch console by choosing **Dashboards** in the left navigation pane of the console, 
 and finding the dashboard name under **Custom Dashboards**.

If you want to edit the template file to customize it for any purpose, you can use **Upload a template file** option 
 under **Create Stack Wizard** to upload the edited template. For more information, see 
 [Creating a stack on AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md"). 
 You can use this link to download the template: [https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/JVM\_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json](https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/JVM_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json "https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/JVM_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json").
 


###### Note

Solution dashboards currently display garbage collection-related metrics only for the G1 Garbage Collector, 
 which is the default collector for the latest Java versions. 
 If you are using a different garbage collection algorithm, the widgets pertaining to garbage collection are empty. 
 However, you can customize these widgets by changing the dashboard CloudFormation template and applying the appropriate 
 garbage collection type to the name dimension of the garbage collection-related metrics. 
 For example, if you are using parallel garbage collection, 
 change the `name=\"G1 Young Generation\"` to `name=\"Parallel GC\"` of the garbage collection 
 count metric `jvm.gc.collections.count`.
 


### Get started with the JVM dashboard


Here are a few tasks that you can try out with the new JVM dashboard. These tasks allow you to validate that the 
 dashboard is working correctly and provide you some hands-on experience using it to monitor a JVM process group. As you 
 try these out, you'll get familiar with navigating the dashboard and interpreting the visualized metrics.


**Select a process group**


Use the **JVM Process Group Name** dropdown list to select the process group that you want to monitor. 
 The dashboard automatically updates to display metrics for the selected process group. If you have multiple Java applications or environments, 
 each might be represented as a separate process group. Selecting the appropriate process group ensures that you're viewing metrics specific to 
 the application or environment that you want to analyze.


**Review memory usage**


From the dashboard overview section, find the **Heap Memory Usage Percentage** and 
 **Non-Heap Memory Usage Percentage** widgets. These show the percentage of 
 heap and non-heap memory being used across all JVMs in the selected process group. A high percentage indicates 
 potential memory pressure that could lead to performance issues or `OutOfMemoryError` exceptions. You can also 
 drill down to heap usage by host under **Memory usage by host** to check the hosts with high usage.


**Analyze threads and classes loaded**


In the **Threads and Classes Loaded by Host** section, find the **Top 10 Threads Count** 
 and **Top 10 Classes Loaded** widgets. Look for any JVMs with an abnormally high number of threads 
 or classes compared to others. Too many threads can indicate thread leaks or excessive concurrency, while a large number of 
 loaded classes could point to potential class loader leaks or inefficient dynamic class generation.


**Identify garbage collection issues**


In the **Garbage Collection** section, find the **Top 10 Garbage Collections Invocations Per Minute** 
 and **Top 10 Garbage Collection Duration** widgets for the different garbage collector types:
 **Young**, **Concurrent**, and **Mixed**. Look for any JVMs that have an 
 unusually high number of collections or long collection durations compared to others. This could indicate configuration issues or memory leaks.
