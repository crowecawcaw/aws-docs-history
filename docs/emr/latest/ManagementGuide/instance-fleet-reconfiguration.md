# Reconfiguring instance fleets for your Amazon EMR cluster

With Amazon EMR version 5.21.0 and later, you can reconfigure cluster applications and specify additional configuration classifications for
each instance fleet in a running cluster. To do so, you can use the AWS Command Line Interface (AWS CLI), or the AWS SDK.

You can track the state of an instance fleet, by viewing the CloudWatch events. For more information,
see [Instance fleet reconfiguration events](emr-manage-cloudwatch-events.md#emr-cloudwatch-instance-fleet-events-reconfig "emr-manage-cloudwatch-events.md#emr-cloudwatch-instance-fleet-events-reconfig").

###### Note

You can only override the cluster Configurations object specified during cluster creation. For more information about Configurations objects,
see [RunJobFlow request syntax](../APIReference/API_RunJobFlow.md#API_RunJobFlow_RequestSyntax "../APIReference/API_RunJobFlow.md#API_RunJobFlow_RequestSyntax"). If there are differences between the existing
configuration and the file that you supply, Amazon EMR resets manually modified configurations, such as configurations that you have modified while connected to
your cluster using SSH, to the cluster defaults for the specified instance fleet.

When you submit a reconfiguration request using the Amazon EMR console, the AWS Command Line interface (AWS CLI), or the AWS SDK, Amazon EMR checks the existing on-cluster
configuration file. If there are differences between the existing configuration and the file that you supply, Amazon EMR initiates reconfiguration actions, restarts
some applications, and resets any manually modified configurations, such as configurations that you have modified while connected to your cluster using SSH,
to the cluster defaults for the specified instance fleet.

## Reconfiguration behaviors

Reconfiguration overwrites on-cluster configuration with the newly submitted configuration set, and can overwrite configuration
changes made outside of the reconfiguration API.

Amazon EMR follows a rolling process to reconfigure instances in the Task and Core instance fleet. Only a percentage of the instances for a
single instance type are modified and restarted at a time. If your instance fleet has multiple different instance
type configurations, they would reconfigure in parallel.

Reconfigurations are declared at the [InstanceTypeConfig](../APIReference/API_InstanceTypeConfig.md "../APIReference/API_InstanceTypeConfig.md") level. For
a visual example, refer to [Reconfigure an instance fleet](#instance-fleet-reconfiguration-cli-sdk "#instance-fleet-reconfiguration-cli-sdk"). You can submit reconfiguration requests that contain updated
configuration settings for one or more instance types within a single request. You must include all instance types that are part of your
instance fleet in the modify request; however, instance types with populated configuration fields will undergo reconfiguration, while other `InstanceTypeConfig` instances
in the fleet remain unchanged. A reconfiguration is considered successful only when all instances of the specified instance types complete reconfiguration. If any instance
fails to reconfigure, the entire Instance Fleet automatically reverts to its last known stable configuration.

## Limitations

When you reconfigure an instance fleet in a running cluster, consider the following limitations:

- Non-YARN applications can fail during restart or cause cluster issues, especially if the applications aren't configured
  properly. Clusters approaching maximum memory and CPU usage may run into issues after the restart process. This is especially true
  for the primary instance fleet. Consult the [Troubleshoot instance fleet reconfiguration](#instance-fleet-reconfiguration-troubleshooting "#instance-fleet-reconfiguration-troubleshooting") section.
- Resizes and Reconfiguration operation do not happen in parallel. Reconfiguration requests will wait for an ongoing resize
  and vice versa.
- Resizes and Reconfiguration operation do not happen in parallel. Reconfiguration requests will wait for an ongoing
  resize and vice versa.
- After reconfiguring an instance fleet, Amazon EMR restarts the applications to allow the new configurations to take
  effect. Job failure or other unexpected application behavior might occur if the applications are in use during
  reconfiguration.
- If a reconfiguration for any instance type config under an instance fleet fails, Amazon EMR reverses the
  configuration parameters to the previous working version for the entire instance fleet, along with emitting events and updating state details.
  If the reversion process fails too, you must submit a new `ModifyInstanceFleet` request to recover the instance fleet from the `ARRESTED` state.
  Reversion failures result in [Instance fleet
  reconfiguration events](emr-manage-cloudwatch-events.md#emr-cloudwatch-instance-fleet-events-reconfig "emr-manage-cloudwatch-events.md#emr-cloudwatch-instance-fleet-events-reconfig") and state change.
- Reconfiguration requests for Phoenix configuration classifications are only supported in Amazon EMR version 5.23.0 and later, and are
  not supported in Amazon EMR version 5.21.0 or 5.22.0.
- Reconfiguration requests for HBase configuration classifications are only supported in Amazon EMR version 5.30.0 and later, and are not
  supported in Amazon EMR versions 5.23.0 through 5.29.0.
- Reconfiguring hdfs-encryption-zones classification or any of the Hadoop KMS configuration classifications is not supported on an Amazon EMR
  cluster with multiple primary nodes.
- Amazon EMR currently doesn't support certain reconfiguration requests for the YARN capacity scheduler that
  require restarting the YARN ResourceManager. For example, you cannot completely remove a queue.
- When YARN needs to restart, all running YARN jobs are typically terminated and lost. This might cause data processing delays. To run
  YARN jobs during a YARN restart, you can either create an Amazon EMR cluster with multiple primary nodes or
  set yarn.resourcemanager.recovery.enabled to `true` in your yarn-site configuration classification. For more
  information about using multiple master nodes, see [High
  availability YARN ResourceManager](emr-plan-ha-applications.md#emr-plan-ha-applications-YARN "emr-plan-ha-applications.md#emr-plan-ha-applications-YARN").

## Reconfigure an instance fleet

Using the AWS CLI
Use the `modify-instance-fleet` command to specify a new configuration for an instance fleet in a
running cluster.

###### Note

In the following examples, replace **j-2AL4XXXXXX5T9** with your cluster ID, and replace **if-1xxxxxxx9** with
your instance fleet ID.

**Example – Replace a configuration for an instance fleet**

###### Warning

Specify all `InstanceTypeConfig` fields that you used at launch. Not including fields can
result in overwriting specifications you declared at launch. Refer to [InstanceTypeConfig](../APIReference/API_InstanceTypeConfig.md "../APIReference/API_InstanceTypeConfig.md") for a list.

The following example references a configuration JSON file called instanceFleet.json to edit the property of the YARN NodeManager disk health checker for an instance fleet.

**Instance Fleet Modification JSON**

1. Prepare your configuration classification, and save it as instanceFleet.json in the same directory where you will run the command.

```
{
    "InstanceFleetId":"`if-1xxxxxxx9`",
    "InstanceTypeConfigs": [
            {
                "InstanceType": "m5.xlarge",
               `other InstanceTypeConfig fields`
                "Configurations": [
                    {
                        "Classification": "yarn-site",
                        "Properties": {
                            "yarn.nodemanager.disk-health-checker.enable":"true",
                            "yarn.nodemanager.disk-health-checker.max-disk-utilization-per-disk-percentage":"100.0"
                        }
                    }
                ]
            },
            {
                "InstanceType": "r5.xlarge",
               `other InstanceTypeConfig fields`
                "Configurations": [
                    {
                        "Classification": "yarn-site",
                        "Properties": {
                            "yarn.nodemanager.disk-health-checker.enable":"false",
                            "yarn.nodemanager.disk-health-checker.max-disk-utilization-per-disk-percentage":"70.0"
                        }
                    }
                ]
            }
        ]
```

2. Run the following command.

```
aws emr modify-instance-fleet \
--cluster-id `j-2AL4XXXXXX5T9` \
--region us-west-2 \
--instance-fleet instanceFleet.json
```

**Example – Add a configuration to an instance fleet**

If you want to add a configuration to an instance type, you must include all previously specified configurations for
that instance type in your new `ModifyInstanceFleet` request. Otherwise, the previously specified configurations are removed.

The following example adds a property for the YARN NodeManager virtual memory checker. The configuration also includes
previously specified values for the YARN NodeManager disk health checker so that the values won't be overwritten.

1. Prepare the following contents in instanceFleet.json and save it in the same directory
   where you will run the command.

```
{
    "InstanceFleetId":"`if-1xxxxxxx9`",
    "InstanceTypeConfigs": [
            {
                "InstanceType": "m5.xlarge",
                `other InstanceTypeConfig fields`
                "Configurations": [
                    {
                        "Classification": "yarn-site",
                        "Properties": {
                            "yarn.nodemanager.disk-health-checker.enable":"true",
                            "yarn.nodemanager.disk-health-checker.max-disk-utilization-per-disk-percentage":"100.0",
                            "yarn.nodemanager.vmem-check-enabled":"true",
                            "yarn.nodemanager.vmem-pmem-ratio":"3.0"
                        }
                    }
                ]
            },
            {
                "InstanceType": "r5.xlarge",
                `other InstanceTypeConfig fields`
                "Configurations": [
                    {
                        "Classification": "yarn-site",
                        "Properties": {
                            "yarn.nodemanager.disk-health-checker.enable":"false",
                            "yarn.nodemanager.disk-health-checker.max-disk-utilization-per-disk-percentage":"70.0"
                        }
                    }
                ]
            }
        ]
}
```

2. Run the following command.

```
aws emr modify-instance-fleet \
--cluster-id `j-2AL4XXXXXX5T9` \
--region us-west-2 \
--instance-fleet instanceFleet.json
```

using the Java SDK

###### Note

In the following examples, replace **j-2AL4XXXXXX5T9** with your cluster ID, and replace **if-1xxxxxxx9** with
your instance fleet ID.

The following code snippet provides a new configuration for an instance fleet using the AWS SDK for Java.

```
AWSCredentials credentials = new BasicAWSCredentials("access-key", "secret-key");
AmazonElasticMapReduce emr = new AmazonElasticMapReduceClient(credentials);

Map<String,String> hiveProperties = new HashMap<String,String>();
hiveProperties.put("hive.join.emit.interval","1000");
hiveProperties.put("hive.merge.mapfiles","true");

Configuration newConfiguration = new Configuration()
    .withClassification("hive-site")
    .withProperties(hiveProperties);

List<InstanceTypeConfig> instanceTypeConfigList = new ArrayList<>();

for (InstanceTypeConfig instanceTypeConfig : currentInstanceTypeConfigList) {
    instanceTypeConfigList.add(new InstanceTypeConfig()
        .withInstanceType(instanceTypeConfig.getInstanceType())
        .withBidPrice(instanceTypeConfig.getBidPrice())
        .withWeightedCapacity(instanceTypeConfig.getWeightedCapacity())
        .withConfigurations(newConfiguration)
    );
}

InstanceFleetModifyConfig instanceFleetModifyConfig = new InstanceFleetModifyConfig()
    .withInstanceFleetId("`if-1xxxxxxx9`")
    .withInstanceTypeConfigs(instanceTypeConfigList);

ModifyInstanceFleetRequest modifyInstanceFleetRequest = new ModifyInstanceFleetRequest()
    .withInstanceFleet(instanceFleetModifyConfig)
    .withClusterId("`j-2AL4XXXXXX5T9`");

emrClient.modifyInstanceFleet(modifyInstanceFleetRequest);
```

## Troubleshoot instance fleet reconfiguration

If the reconfiguration process for any instance type within an instance fleet fails, Amazon EMR reverts the in progress reconfiguration
and logs a failure message using an AAmazon CloudWatch Events events. The event provides a brief summary of the reconfiguration failure. It lists the instances for
which reconfiguration has failed and corresponding failure messages. The following is an example
failure message.

`Amazon EMR couldn't revert the instance fleet if-1xxxxxxx9 in the Amazon EMR cluster 
 j-2AL4XXXXXX5T9 (ExampleClusterName) to the previously successful configuration at 
 2021-01-01 00:00 UTC. The reconfiguration reversion failed because of 
 Instance i-xxxxxxx1, i-xxxxxxx2, i-xxxxxxx3 failed with message 
 "This is an example failure message"...`

### To access node provisioning logs

Use SSH to connect to the node on which reconfiguration has failed. For instructions, see [Connect to your Linux instance](../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md "../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md") in the _Amazon Elastic
Compute Cloud_.

Accessing logs by connecting to a node

1. Navigate to the following directory, which contains the node provisioning log files.

```
/mnt/var/log/provision-node/
```

2. Open the reports subdirectory and search for the node provisioning report for your reconfiguration. The
   reports directory organizes logs by reconfiguration version number, universally unique identifier (UUID), Amazon EC2 instance IP address, and
   timestamp. Each report is a compressed YAML file that contains detailed information about the reconfiguration process. The following is an
   example report file name and path.

```
/reports/2/ca598xxx-cxxx-4xxx-bxxx-6dbxxxxxxxxx/ip-10-73-xxx-xxx.ec2.internal/202104061715.yaml.gz
```

3. You can examine a report using a file viewer like zless, as in the following example.

```
zless 202104061715.yaml.gz
```

Accessing logs using Amazon S3
Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
Open the Amazon S3 bucket that you specified when you configured the cluster to archive log files.

1. Navigate to the following folder, which contains the node provisioning log files:

```
amzn-s3-demo-bucket/elasticmapreduce/`cluster id`/node/`instance id`/provision-node/
```

2. Open the reports folder and search for the node provisioning report for your reconfiguration. The
   reports folder organizes logs by reconfiguration version number, universally unique identifier (UUID), Amazon EC2 instance IP address, and timestamp. Each
   report is a compressed YAML file that contains detailed information about the reconfiguration process. The following is an example report file name and path.

```
/reports/2/ca598xxx-cxxx-4xxx-bxxx-6dbxxxxxxxxx/ip-10-73-xxx-xxx.ec2.internal/202104061715.yaml.gz
```

To view a log file, you can download it from Amazon S3 to your local machine as a text file. For instructions,
see [Downloading an object](../../../AmazonS3/latest/userguide/download-objects.md "../../../AmazonS3/latest/userguide/download-objects.md").

Each log file contains a detailed provisioning report for the associated reconfiguration. To find error message information, you can search for the `err` log
level of a report. Report format depends on the version of Amazon EMR on your cluster.
The following example shows error information for Amazon EMR release versions 5.32.0 and 6.2.0 and later use the following format:

```
- level: err
  message: 'Example detailed error message.'
  source: Puppet
  tags:
  - err
  time: '2021-01-01 00:00:00.000000 +00:00'
  file:
  line:
```
