# CloudWatch solution: Kafka workload on Amazon EC2

This solution helps you configure out-of-the-box metric collection using CloudWatch agents for 
 Kafka workloads (brokers, producers, and consumers) running on EC2 instances. Additionally, it helps you 
 set up a pre-configured CloudWatch dashboard. For general information about all CloudWatch observability solutions, see [CloudWatch observability solutions](Monitoring-Solutions.md "Monitoring-Solutions.md").

###### Topics

* [Requirements](#Solution-Kafka-On-EC2-Requirements "#Solution-Kafka-On-EC2-Requirements")
* [Benefits](#Solution-Kafka-On-EC2-Benefits "#Solution-Kafka-On-EC2-Benefits")
* [Costs](#Solution-Kafka-On-EC2-Costs "#Solution-Kafka-On-EC2-Costs")
* [CloudWatch agent configuration for this solution](#Solution-Kafka-CloudWatch-Agent "#Solution-Kafka-CloudWatch-Agent")
* [Deploy the agent for your solution](#Solution-Kafka-Agent-Deploy "#Solution-Kafka-Agent-Deploy")
* [Create the Kafka solution dashboard](#Solution-Kafka-Dashboard "#Solution-Kafka-Dashboard")
* [Configure the agent for multiple Kafka roles on the same instance](#Kafka-Multiple-Roles "#Kafka-Multiple-Roles")

## Requirements


This solution is relevant for the following conditions:



* Workload: Kafka v0.8.2.x and later
* Compute: Amazon EC2
* Supports up to 500 EC2 instances across all Kafka workloads in a given AWS Region
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


The solution delivers Kafka server monitoring, providing valuable insights for the following use cases:



* Monitor Kafka cluster health via replication and sync metrics.
* Track broker performance through request failures and latencies along with network traffic.
* Monitor producer/consumer errors, latencies, and consumer lag.
* Analyze underlying JVM performance for Kafka clusters.
* Switch between multiple Kafka clusters, producers, and consumers configured via the solution under the same account.

Below are the key advantages of the solution:



* Automates metric collection for Kafka and the underlying JVM using CloudWatch agent configuration, eliminating manual instrumentation.
* Provides a pre-configured, consolidated CloudWatch dashboard for Kafka and JVM metrics. The dashboard will automatically handle metrics 
 from new Kafka EC2 instances configured using the solution, even if those metrics don't exist when you first create the dashboard. It also allows 
 you to group the metrics into logical applications for easier focus and management.

The following image is an example of the dashboard for this solution.



![Kafka cluster dashboard showing metrics for partitions, producer/consumer performance, and broker status.](images/KafkaDashboard.png)

## Costs


This solution creates and uses resources in your account. You are charged for standard usage, including the following:



* All metrics collected by the CloudWatch agent are charged as custom metrics. The number of metrics used by this solution depends on the number 
 of EC2 hosts.




	+ Each broker host configured for the solution publishes 33 metrics plus one metric
	 (`disk_used_percent`) for which the metric count for each EC2 host depends on the number of disk paths
	 for that host.
	+ Each producer host configured for the solution publishes three metrics with the `topic` dimension and three metrics without the
	 `topic` dimension. For the
	 metrics with the `topic` dimension, each topic counts as a separate metric.
	+ Each consumer host configured for the solution publishes two metrics with `topic` dimensions and three metrics without `topic` dimensions. For the
	 metrics with topic dimensions, each topic counts as a separate metric.
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
2. In the **Metrics** section, for **Number of metrics**,
 enter `broker_metrics_count + producer_metrics_count + consumer_metrics_count`. Calculate these
 as follows:




	* `broker_metrics_count` = (33 + average number of disk paths per EC2 host) \* number\_of\_ec2\_broker\_hosts
	* `producer_metrics_count` = (3 \* average\_number\_of\_topics\_per\_producer\_host + 3) \* number\_of\_ec2\_producer\_hosts
	* `consumer_metrics_count` = (2 \* average\_number\_of\_topics\_per\_consumer\_host + 3) \* number\_of\_ec2\_consumer\_hosts
3. In the **APIs** section, for **Number of API requests**,
 enter `43200 * number of EC2 instances configured for this solution`.


By default, the CloudWatch agent performs one **PutMetricData** operation each minute for each EC2 host.
4. In the **Dashboards and Alarms** section, for **Number of Dashboards**, enter `1`.
5. You can see your monthly estimated costs at the bottom of the
 pricing calculator.

## CloudWatch agent configuration for this solution


The CloudWatch agent is software that runs continuously and autonomously on your servers and in containerized environments. It collects metrics, logs, and traces from your 
 infrastructure and applications and sends them to CloudWatch and X-Ray.


For more information about the CloudWatch agent, see [Collect metrics, logs, and traces using the CloudWatch
 agent](Install-CloudWatch-Agent.md "Install-CloudWatch-Agent.md").


The agent configuration in this solution collects the foundational metrics for Kafka, JVM, and EC2. The CloudWatch agent can be configured to collect more 
 Kafka and JVM metrics than the dashboard displays by default. For a list of all Kafka metrics that you can collect, see 
 [Collect Kafka metrics](CloudWatch-Agent-JMX-metrics.md#CloudWatch-Agent-Kafka-metrics "CloudWatch-Agent-JMX-metrics.md#CloudWatch-Agent-Kafka-metrics"). For a list of all JVM metrics that you can collect, see 
 [Collect JVM metrics](CloudWatch-Agent-JMX-metrics.md#CloudWatch-Agent-JVM-metrics "CloudWatch-Agent-JMX-metrics.md#CloudWatch-Agent-JVM-metrics"). For a list of EC2 metrics, see 
 [Metrics collected by the CloudWatch
 agent on Linux and macOS instances](metrics-collected-by-CloudWatch-agent.md#linux-metrics-enabled-by-CloudWatch-agent "metrics-collected-by-CloudWatch-agent.md#linux-metrics-enabled-by-CloudWatch-agent").


**Expose JMX ports for the Kafka broker, producer, and consumer roles**


The CloudWatch agent relies on JMX to collect the metrics related to the Kafka brokers, producers, and consumers. To make this possible, you must expose the JMX port on your servers
 and applications.


For Kafka brokers, you must use the `JMX_PORT` environment variable to set the port. You'll have to restart the brokers after
 you set this environment variable. Review the starting scripts and configuration files of your application to find the best place to add these arguments.


For example, for Linux and macOS systems, you can use the following command to set the JMX port. Be sure to specify an unused port number.



```
export JMX_PORT=`port-number`
```

For Kafka producers and consumers, instructions for exposing the JMX port depend on the workload type you are using for your 
 producer or consumer JVM application. See the documentation for your application to find these instructions.


In general, to enable a JMX port for monitoring and management, you would set the following system properties for your JVM application.
 The following example sets up unauthenticated JMX. If your security policies/requirements require you to enable JMX with password authentication 
 or SSL for remote access, refer to the [JMX documentation](https://docs.oracle.com/en/java/javase/17/management/monitoring-and-management-using-jmx-technology.html "https://docs.oracle.com/en/java/javase/17/management/monitoring-and-management-using-jmx-technology.html")  
 to set the required property.



```
-Dcom.sun.management.jmxremote
-Dcom.sun.management.jmxremote.port=`port-number`
-Dcom.sun.management.jmxremote.authenticate=false 
-Dcom.sun.management.jmxremote.ssl=false
```

To verify the JMX port, run `ps aux | grep jmxremote.port`. The results should show that the JMX port was set on the JVM processes.


**Agent configuration for this solution**


The metrics collected by the agent are defined in the agent configuration. The solution provides agent configurations to collect the recommended metrics with 
 suitable dimensions for the solution’s dashboard. Each Kafka role, such as broker, producer, or consumer, has its own agent 
 configuration that enables the collection of Kafka metrics and underlying JVM and EC2 metrics.


The steps for deploying the solution are described later in [Deploy the agent for your solution](#Solution-Kafka-Agent-Deploy "#Solution-Kafka-Agent-Deploy"). 
 The following information is intended to help you understand how to customize the agent configuration for your environment.


You must customize some parts of the following agent configuration for your environment:



* The JMX port number is the port number that you configured in the previous section of this documentation. The port number is in
 the `endpoint` line in the configuration.
* `ClusterName`– This is used as a dimension for broker metrics collected. Provide a meaningful name that represents the cluster grouping for the 
 instances that run the Kafka broker.
* `ProcessGroupName`– This is used as a dimension for JVM metrics collected for brokers. Provide the same value as you
 provide for `ClusterName`. This enables viewing the JVM metrics of the same Kafka broker group as the broker metrics in the solution dashboard.
* `ProducerGroupName`– This is used as a dimension for producer metrics
 collected. Provide a meaningful name that represents the group of producer instances.
 For this value, you can specify your producer application or service that you want to
 use for a combined view of producer metrics in the solution dashboard.
* `ConsumerGroupName`– This is used as a dimension for consumer metrics
 collected. Provide a meaningful name that represents the group of consumer instances
 This is not the same as the consumer group concept in Kafka. This is just a grouping
 dimension where you can specify your consumer application or service that you want to
 use for a combined view of consumer metrics in the solution dashboard

For example, if you have two Kafka clusters running in the same account, 
 one for the `order-processing` application and another for the `inventory-management` application, 
 you should set the `ClusterName` and `ProcessGroupName` dimensions accordingly in the agent configuration of the broker instance.



* For the `order-processing` cluster broker instances, 
 set `ClusterName=order-processing` and `ProcessGroupName=order-processing`.
* For the `inventory-management` cluster broker instances, set `ClusterName=inventory-management` 
 and `ProcessGroupName=inventory-management`.
* Similarly, set the `ProducerGroupName` for producer instances and `ConsumerGroupName` 
 for consumer instances based on their respective applications.

When you correctly set the above dimensions, the solution dashboard will automatically group the metrics 
 based on the `ClusterName`, `ProducerGroupName`, and `ConsumerGroupName` dimensions. 
 The dashboard will include dropdown options to select and view metrics for specific clusters and groups, 
 allowing you to monitor the performance of individual clusters and groups separately.


Be sure to deploy the relevant agent configuration to the correct EC2 instances. Each configuration will be stored as a separate Parameter
 in SSM's Parameter Store, as detailed later in [Step 2: Store the recommended CloudWatch agent configuration file in Systems Manager Parameter Store](#Solution-Kafka-Agent-Step2 "#Solution-Kafka-Agent-Step2").


The following instructions describe the situation where the
 producer, consumer, and broker roles are deployed to separate EC2 instances, without any overlap. If you are running multiple Kafka roles on the same EC2 instances,
 see [Configure the agent for multiple Kafka roles on the same instance](#Kafka-Multiple-Roles "#Kafka-Multiple-Roles") for more information.


### Agent configuration for Kafka broker agents


Use the following CloudWatch agent configuration on EC2 instances where Kafka broker agents are deployed.
 Replace
 `ClusterName` with the name of the cluster to use to group these metrics for a unified view. The value you specify 
 for `ClusterName` is used as
 both the `ClusterName` dimension and the `ProcessGroupName` dimension.
 Replace `port-number`
 with the JMX port of your Kafka server. If JMX was enabled with password authentication or SSL for remote access, 
 see [Collect Java Management Extensions (JMX)
 metrics](CloudWatch-Agent-JMX-metrics.md "CloudWatch-Agent-JMX-metrics.md") for information about setting up TLS or authorization as required.


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
          "kafka": {
            "measurement": [
              "kafka.request.time.avg",
              "kafka.request.failed",
              "kafka.request.count",
              "kafka.purgatory.size",
              "kafka.partition.under_replicated",
              "kafka.partition.offline",
              "kafka.network.io",
              "kafka.leader.election.rate",
              "kafka.isr.operation.count"
            ]
          },
          "append_dimensions": {
            "ClusterName": "`ClusterName`"
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
            "ProcessGroupName": "`ClusterName`"
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

### Agent configuration for Kafka producers


Use the following CloudWatch agent configuration on Amazon EC2 instances where Kafka producers are deployed. Replace
 `ProducerGroupName` with the name of the application or group that you want to use to group your metrics
 for a unified view. Replace `port-number`
 with the JMX port of your Kafka producer application.



 The solution doesn’t enable JVM metrics for Kafka producers because the solution dashboard doesn’t display 
 JVM metrics related to JVM for producers. You can customize the agent configuration to emit JVM metrics as well, 
 however, JVM metrics related to producers are not visible on the solution dashboard.



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
          "kafka-producer": {
            "measurement": [
              "kafka.producer.request-rate",
              "kafka.producer.byte-rate",
              "kafka.producer.request-latency-avg",
              "kafka.producer.response-rate",
              "kafka.producer.record-error-rate",
              "kafka.producer.record-send-rate"
            ]
          },
          "append_dimensions": {
            "ProducerGroupName": "`ProducerGroupName`"
          }
        }
      ]
    }
  }
}
```

### Agent configuration for Kafka consumers


Use the following CloudWatch agent configuration on EC2 instances where Kafka consumers are running.
 Replace
 `ConsumerGroupName` with the name of the application or group to use to group these metrics for a unified view.
 Replace `port-number`
 with the JMX port of your Kafka consumer application.


The solution doesn’t enable JVM metrics for Kafka consumers because the solution dashboard doesn’t display 
 JVM metrics related to JVM for consumers. You can customize the agent configuration to emit JVM metrics as well, 
 however JVM metrics related to consumer are not visible on the solution dashboard.



```
{
  "metrics": {
    "append_dimensions": {
      "InstanceId": "${aws:InstanceId}"
    },
    "metrics_collected": {
      "jmx": [
        {
          "endpoint": "localhost:`port-number`",
          "kafka-consumer": {
            "measurement": [
              "kafka.consumer.fetch-rate",
              "kafka.consumer.total.bytes-consumed-rate",
              "kafka.consumer.records-consumed-rate",
              "kafka.consumer.bytes-consumed-rate",
              "kafka.consumer.records-lag-max"
            ]
          },
          "append_dimensions": {
            "ConsumerGroupName": "`ConsumerGroupName`"
          }
        }
      ]
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
 according to the role (broker, producer, or consumer) with your existing agent 
 configuration, and then deploy the merged configuration. If you are using Systems Manager to 
 store and manage the configuration for the CloudWatch agent, you can merge the configuration 
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

You must repeat these steps based on whether your broker, producer, and consumer are deployed on the same EC2 instance or different instances.
 For example, if the Kafka broker, producer, and consumers are getting deployed on separate instances without overlap, you must repeat 
 these steps three times with the appropriate agent configurations for broker, producer, and consumer EC2 instances.


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
	2. Provide a name for the parameter that will store 
	 your CloudWatch agent configuration, such as `AmazonCloudWatch-Kafka-Producer-Configuration` for producers, 
	 `AmazonCloudWatch-Kafka-Consumer-Configuration` for consumers, or `AmazonCloudWatch-Kafka-Broker-Configuration` for brokers. 
	 If you have multiple Kafka roles on a single EC2, name the roles accordingly for easier identification. 
	 This value will later be used to distribute this configuration to the agent running on your EC2 instance.
	3. For **Parameter tier**, choose **Standard**.
	4. For **Type**, choose **String**.
	5. For **Data type**, choose **text**.
	6. In the **Value** box, paste the full text of the CloudWatch agent configuration. 
	 Be sure to select the JSON block for the Kafka role that this instance is hosting. 
	 Refer to the configuration provided in [Agent configuration for Kafka broker agents](#Solution-Kafka-Agent-Broker "#Solution-Kafka-Agent-Broker"), 
	 [Agent configuration for Kafka producers](#Solution-Kafka-Agent-Producer "#Solution-Kafka-Agent-Producer"), 
	 and [Agent configuration for Kafka consumers](#Solution-Kafka-Agent-Consumer "#Solution-Kafka-Agent-Consumer")
	 when storing the configuration for broker, producer, and consumer respectively. 
	 If you are running multiple Kafka roles on the same EC2 instance, be sure to 
	 merge the configuration if required as described in 
	 [Configure the agent for multiple Kafka roles on the same instance](#Kafka-Multiple-Roles "#Kafka-Multiple-Roles") on the same instance
	7. Choose **Create parameter**.

### Step 3: Install the CloudWatch agent and apply the configuration using an AWS CloudFormation template


You can use AWS CloudFormation to install the agent and configure it to use the CloudWatch agent
 configuration that you created in the previous steps.


###### To install and configure the CloudWatch agent for this solution

1. Open the AWS CloudFormation **Quick create stack** wizard using this link: [https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json](https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json "https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json").
2. Verify that the selected Region on the console is the Region where the Kafka workload is running.
3. For **Stack name**, enter a name to identity this stack, 
 such as `CWAgentInstallationStack`.
4. In the **Parameters** section, specify the following:


	1. For **CloudWatchAgentConfigSSM**, enter the name of the Systems Manager parameter for the agent configuration 
	 that you created earlier, such as `AmazonCloudWatch-Kafka-Broker-Configuration` for brokers, 
	 `AmazonCloudWatch-Kafka-Producer-Configuration` for producers, and 
	 `AmazonCloudWatch-Kafka-Consumer-Configuration` for consumers.
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
 You can use the following link to download the template: 
 [https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json](https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json "https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/CloudWatchAgent/CFN/v1.0.0/cw-agent-installation-template-1.0.0.json").
 


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
 EC2 instance as described in [Step 1: Ensure the target EC2 instances have the required IAM permissions](Solution-Tomcat-On-EC2.md#Solution-Tomcat-Agent-Step1 "Solution-Tomcat-On-EC2.md#Solution-Tomcat-Agent-Step1").
* Be sure you have correctly configured the JSON for the Systems Manager parameter. Follow the steps in 
 [Troubleshooting
 installation of the CloudWatch agent with AWS CloudFormation](Install-CloudWatch-Agent-New-Instances-CloudFormation.md#CloudWatch-Agent-CloudFormation-troubleshooting "Install-CloudWatch-Agent-New-Instances-CloudFormation.md#CloudWatch-Agent-CloudFormation-troubleshooting").

If everything is set up correctly, then you should see the 
 Kafka metrics being published to CloudWatch. You can check the CloudWatch console to verify they are being published.


###### To verify that Kafka metrics are being published to CloudWatch

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Metrics**, **All metrics**.
3. Make sure you've selected the Region where you deployed the solution, and choose **Custom namespaces**, 
 **CWAgent**.
4. Search for the metrics mentioned in the agent configuration section of this document, such 
 as `kafka.partition.offline` for brokers, `kafka.consumer.fetch.rate` for consumers, 
 or `kafka.producer.request-rate` for producers. If you see results
 for these metrics, then the metrics are being published to CloudWatch.

## Create the Kafka solution dashboard


This dashboard displays the newly emitted metrics for both Kafka and the underlying JVM. This dashboard provides a top contributor 
 view for the health of your Kafka workload, across producers, brokers, and consumers. 
 The top contributor view displays the top 10 per metric widget. This allows you to identify outliers at a glance.
 


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
 Be sure to create the AWS CloudFormation stack in the Region where your JVM and Kafka metrics are published.

If you've specified a custom namespace other than `CWAgent` in the CloudWatch agent
 configuration, you'll have to change the AWS CloudFormation template for the dashboard to replace 
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
 [https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=ApacheKafkaOnEc2&referrer=os-catalog](https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=ApacheKafkaOnEc2&referrer=os-catalog "https://console.aws.amazon.com/cloudwatch/home?#dashboards?dashboardTemplate=ApacheKafkaOnEc2&referrer=os-catalog") .
2. Verify that the selected Region on the console is the Region where the Kafka workload is running.
3. Enter the name of the dashboard, then choose **Create Dashboard**.


To easily differentiate this dashboard from similar dashboards in other Regions, we recommend including the Region name
 in the dashboard name, such as `KafkaDashboard-us-east-1`.
4. Preview the dashboard and choose **Save** to create the dashboard.

###### To create the dashboard via AWS CloudFormation

1. Open the AWS CloudFormation **Quick create stack** wizard using this link: [https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Kafka\_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json](https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Kafka_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json "https://console.aws.amazon.com/cloudformation/home?#/stacks/quickcreate?templateURL=https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Kafka_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json").
2. Verify that the selected Region on the console is the Region where the Kafka
 workload is running.
3. For **Stack name**, enter a name to identity this stack, 
 such as `KafkaDashboardStack`.
4. In the **Parameters** section, specify the name of the dashboard under 
 the **DashboardName** parameter.


To easily differentiate this dashboard from similar dashboards in other Regions, 
 we recommend including the Region name in the dashboard name, such as `KafkaDashboard-us-east-1`.
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
 You can use this link to download the template: [https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Kafka\_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json](https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Kafka_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json "https://aws-observability-solutions-prod-us-east-1.s3.us-east-1.amazonaws.com/Kafka_EC2/CloudWatch/CFN/v1.0.0/dashboard-template-1.0.0.json").
 


###### Note

Solution dashboards currently display garbage collection-related metrics only for the G1 Garbage Collector, 
 which is the default collector for the latest Java versions. 
 If you are using a different garbage collection algorithm, the widgets pertaining to garbage collection are empty. 
 However, you can customize these widgets by changing the dashboard CloudFormation template and applying the appropriate 
 garbage collection type to the name dimension of the garbage collection-related metrics. 
 For example, if you are using parallel garbage collection, 
 change the `name=\"G1 Young Generation\"` to `name=\"Parallel GC\"` of the garbage collection 
 count metric `jvm.gc.collections.count`.
 


### Get started with the Kafka dashboard


Here are a few tasks that you can try out with the new Kafka dashboard. These tasks allow you to validate that the 
 dashboard is working correctly and provide you some hands-on experience using it to monitor a Kafka cluster. As you 
 try these out, you'll get familiar with navigating the dashboard and interpreting the visualized metrics.


**Using the dropdown lists**


The dashboard provides dropdown lists at the top that you can use to filter and select the 
 specific Kafka cluster, producer, and consumer groups that you want to monitor.



* To display metrics for a specific Kafka cluster, select that cluster name in the **Kafka Cluster** dropdown list.
* To display metrics for a specific Kafka producer group, select that producer group name in the **Kafka Producer** dropdown list.
* To display metrics for a specific Kafka consumer group, select that consumer group name in the **Kafka Consumer Group** dropdown list.

**Verify cluster health**


From the **Cluster Overview** section, find the **Partitions Under Replicated** and 
 **In-Sync Replicas** widgets. These should ideally be zero or a small number. A large value 
 for any of these metrics could indicate issues with the Kafka cluster that need investigation. 


**Investigate broker performance**


In the **Brokers** section, find the **Failed Fetch Requests** 
 and **Failed Producer Requests** widgets. These show the number 
 of failed requests for fetch and produce operations, respectively. High failure rates 
 could indicate issues with the brokers or network connectivity that require further investigation.


**Monitor producer performance**


In the **Producer Group Overview** section, find the **Average Request Rate**, 
 **Average Request Latency**, and **Average Record Send/Error Rate** widgets. 
 These will give you an overview of how the producers in the selected group are performing. You can also drill down to 
 view metrics for specific producers and topics in the **Producers** section.


**Monitor consumer lag**


In the **Consumer Group Overview** section, find the **Consumer Lag** 
 widget. This shows how far behind the consumers are in processing messages from the latest offsets in the partitions they are 
 subscribed to. Ideally, the consumer lag should be low or zero. A high consumer lag could indicate that the consumers are unable 
 to keep up with the rate of data production, leading to potential data loss or delays in processing. You can also drill down to 
 view metrics for specific consumers and topics in the **Consumers** section.


## Configure the agent for multiple Kafka roles on the same instance


The individual configurations for Kafka roles listed in [CloudWatch agent configuration for this solution](#Solution-Kafka-CloudWatch-Agent "#Solution-Kafka-CloudWatch-Agent") apply only when the producer, consumer, and broker roles are deployed on 
 separate EC2 instances, without any overlap. If you are running multiple Kafka roles on the same Amazon EC2 instances, you have two options:



* Create a single agent configuration file which lists and configures all metrics for all the Kafka roles deployed on that instance. If you are going
 to use Systems Manager to manage agent configuration, this is the preferred option.


If you choose this option and the multiple Kafka roles are part of the same JVM process, you must specify the same endpoint for each Kafka role
 in the agent configuration. If the multiple Kafka roles are part of different JVM processes, the endpoint for each 
 role can be different depending on the JMX port set for that process.
* Create separate agent configuration files for each Kafka role, and configure the agent to apply both configuration files.
 For instructions for applying multiple configuration files, see [Creating multiple CloudWatch agent
 configuration files](create-cloudwatch-agent-configuration-file.md#CloudWatch-Agent-multiple-config-files "create-cloudwatch-agent-configuration-file.md#CloudWatch-Agent-multiple-config-files").

The following example shows a CloudWatch agent configuration where the producer and consumer roles are 
 running on one instance as part of the same JVM process. In this case, the port number must be the same in both the 
 producer and consumer parts of the configuration below. If instead the two roles were running as part of different JVM processes,
 you could specify different port numbers for each, according to the JMX port of each individual JVM process.



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
          "kafka-producer": {
            "measurement": [
              "kafka.producer.request-rate",
              "kafka.producer.byte-rate",
              "kafka.producer.request-latency-avg",
              "kafka.producer.response-rate",
              "kafka.producer.record-error-rate",
              "kafka.producer.record-send-rate"
            ]
          },
          "append_dimensions": {
            "ProducerGroupName": "`ProducerGroupName`"
          }
        },
        {
          "endpoint": "localhost:`port-number`",
          "kafka-consumer": {
            "measurement": [
              "kafka.consumer.fetch-rate",
              "kafka.consumer.total.bytes-consumed-rate",
              "kafka.consumer.records-consumed-rate",
              "kafka.consumer.bytes-consumed-rate",
              "kafka.consumer.records-lag-max"
            ]
          },
          "append_dimensions": {
            "ConsumerGroupName": "`ConsumerGroupName`"
          }
        }
      ]
    }
  }
}
```
