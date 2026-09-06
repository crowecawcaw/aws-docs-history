

# EC2 instance metrics
<a name="ec2-metrics-analyzed"></a>

**Topics**
+ [Metrics analyzed for EC2 instances](#ec2-metrics-list)
+ [Enabling memory utilization with the CloudWatch agent](#cw-agent)
+ [Enabling NVIDIA GPU utilization with the CloudWatch agent](#nvidia-cw-agent)
+ [Configure external metrics ingestion](#external-metrics)

## Metrics analyzed for EC2 instances
<a name="ec2-metrics-list"></a>

Compute Optimizer analyzes the following CloudWatch metrics of your EC2 instances, including instances that are part of EC2 Auto Scaling groups.


| Metric | Description | 
| --- | --- | 
|  CPUUtilization  | The percentage of allocated EC2 compute units that are in use on the instance. This metric identifies the processing power that's required to run an application on an instance. | 
|  MemoryUtilization  | The percentage of memory that's used during the sample period. This metric identifies the memory that's required to run an application on an instance.<br />Memory utilization metrics are analyzed for the following resources:+  EC2 instances with the CloudWatch agent that's installed on them. For more information, see [Enabling memory utilization with the CloudWatch agent](#cw-agent). <br />+  External EC2 instances from one of the four observability products: Datadog, Dynatrace, Instana, and New Relic. For more information, see [ External metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion).  | 
|  GPUUtilization  | The percentage of allocated GPUs that are currently in use on the instance. To allow Compute Optimizer analyze the GPU utilization metric of your instances, install the CloudWatch agent on your instances. For more information, see [Enabling NVIDIA GPU utilization with the CloudWatch agent](#nvidia-cw-agent).  | 
|  GPUMemoryUtilization  | The percentage of total GPU memory that's currently in use on the instance. | 
|  GPUEncoderStatsSessionCount  | The number of active encoding sessions on an NVIDIA GPU. | 
|  NetworkIn  | The number of bytes that's received on all network interfaces by the instance. This metric identifies the volume of incoming network traffic to an instance. | 
|  NetworkOut  | The number of bytes that are sent out on all network interfaces by the instance. This metric identifies the volume of outgoing network traffic from an instance. | 
|  NetworkPacketsIn  | The number of packets that are received by the instance. | 
|  NetworkPacketsOut  | The number of packets that are sent out by the instance. | 
|  DiskReadOps  | The read operations per second of the instance store volume of the instance. | 
|  DiskWriteOps  | The write operations per second of the instance store volume of the instance. | 
|  DiskReadBytes  | The read bytes per second of the instance store volume of the instance. | 
|  DiskWriteBytes  | The write bytes per second of the instance store volume of the instance. | 
|  VolumeReadBytes  | The read bytes per second of EBS volumes attached to the instance. Displayed as KiBs in the console. | 
|  VolumeWriteBytes  | The write bytes per second of EBS volumes attached to the instance. Displayed as KiBs in the console. | 
|  VolumeReadOps  | The read operations per second of EBS volumes attached to the instance. | 
|  VolumeWriteOps  | The write operations per second of EBS volumes attached to the instance. | 

For more information about instance metrics, see [List the available CloudWatch metrics for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html) in the *Amazon Elastic Compute Cloud User Guide*. For more information about EBS volume metrics, see [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Enabling memory utilization with the CloudWatch agent
<a name="cw-agent"></a>

To have Compute Optimizer analyze the memory utilization metric of your instances, install the CloudWatch agent on your instances. Enabling Compute Optimizer to analyze memory utilization data for your instances provides an additional measurement of data that further improves Compute Optimizer's recommendations. For more information about installing the CloudWatch agent, see [Collecting Metrics and Logs from Amazon EC2 Instances and On-Premises Servers with the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) in the *Amazon CloudWatch User Guide*.

On Linux instances, Compute Optimizer analyses the `mem_used_percent` metric in the `CWAgent` namespace, or the legacy `MemoryUtilization` metric in the `System/Linux` namespace. On Windows instances, Compute Optimizer analyses the `Available MBytes` metric in the `CWAgent` namespace. If both the `Available MBytes` and `Memory % Committed Bytes In Use` metrics are configured in the `CWAgent` namespace, Compute Optimizer chooses `Available MBytes` as the primary memory metric to generate recommendations.

**Note**  
We recommend that you configure the `CWAgent` namespace to use `Available MBytes` as your memory metric for Windows instances.
Compute Optimizer also supports the `Available KBytes` and `Available Bytes` metrics, and prioritizes both over the `Memory % Committed Bytes In Use` metric when generating recommendations for Windows instances.

Additionally, the namespace must contain the `InstanceId` dimension. If the `InstanceId` dimension is missing or you overwrite it with a custom dimension name, Compute Optimizer can't collect memory utilization data for your instance. Namespaces and dimensions are defined in the CloudWatch agent configuration file. For more information, see [Create the CloudWatch agent Configuration File](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.html) in the *Amazon CloudWatch User Guide*.

**Important**  
All of the CloudWatch namespaces and metric names are case sensitive.

**Example: CloudWatch agent configuration for memory collection**

```
{
    "agent": {
        "metrics_collection_interval": 60,
        "run_as_user": "root"
    },
    "metrics": {
        "namespace": "CWAgent",
        "append_dimensions": {
            "InstanceId": "${aws:InstanceId}"
        },
        "metrics_collected": {
            "mem": {
                "measurement": [
                    "mem_used_percent"
                ],
                "metrics_collection_interval": 60
            }
        }
    }
}
```

## Enabling NVIDIA GPU utilization with the CloudWatch agent
<a name="nvidia-cw-agent"></a>

To allow Compute Optimizer to analyze the NVIDIA GPU utilization metric of your instances, do the following:

1. Install the CloudWatch agent on your instances. For more information, see [Installing the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) in the *Amazon CloudWatch User Guide*.

1. Allow the CloudWatch agent to collect NVIDIA GPU metrics. For more information, see [Collect NVIDIA GPU metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html) in the *Amazon CloudWatch User Guide*.

Compute Optimizer analyzes the following NVIDIA GPU metrics:
+ `nvidia_smi_utilization_gpu`
+ `nvidia_smi_memory_used`
+ `nvidia_smi_encoder_stats_session_count`
+ `nvidia_smi_encoder_stats_average_fps`
+ `nvidia_smi_encoder_stats_average_latency`
+ `nvidia_smi_temperature_gpu`

The namespace must contain the `InstanceId` dimension and `index` dimensions. If the dimensions are missing or you overwrite them with a custom dimension name, Compute Optimizer can't collect GPU utilization data for your instance. Namespaces and dimensions are defined in the CloudWatch agent configuration file. For more information, see [Create the CloudWatch agent Configuration File](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.html) in the *Amazon CloudWatch User Guide*.

## Configure external metrics ingestion
<a name="external-metrics"></a>

You can use the external metrics ingestion feature to configure AWS Compute Optimizer to ingest EC2 memory utilization metrics from one of the four observability products: Datadog, Dynatrace, Instana, and New Relic. When you enable external metrics ingestion, Compute Optimizer analyzes your external EC2 memory utilization metrics in addition to your CPU, disk, network, IO, and throughput data to generate EC2 rightsizing recommendations. These recommendations can provide you with additional savings and enhanced performance. For more information, see [External metrics ingestion](external-metrics-ingestion.md).