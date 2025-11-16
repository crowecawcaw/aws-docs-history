# Configure managed scaling for

Amazon EMR

The following sections explain how to launch an EMR cluster that uses managed
scaling with the AWS Management Console, the AWS SDK for Java, or the AWS Command Line Interface.

###### Topics

- [Use the AWS Management Console to configure managed
  scaling](#managed-scaling-console "#managed-scaling-console")
- [Use the AWS CLI to configure managed
  scaling](#managed-scaling-cli "#managed-scaling-cli")
- [Use AWS SDK for Java to configure managed
  scaling](#managed-scaling-sdk "#managed-scaling-sdk")

## Use the AWS Management Console to configure managed

scaling

You can use the Amazon EMR console to configure managed scaling when you create a
cluster or to change a managed scaling policy for a running cluster.

Console

###### To configure managed scaling when you create a cluster with

the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left
   navigation pane, choose **Clusters**, and
   then choose **Create cluster**.
3. Choose an Amazon EMR release **emr-5.30.0** or
   later, except version **emr-6.0.0**.
4. Under **Cluster scaling and provisioning
   option**, choose
   **Use EMR-managed scaling**.
   Specify the **Minimum** and
   **Maximum** number of instances, the
   **Maximum core node** instances, and
   the **Maximum On-Demand** instances.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

###### To configure managed scaling on an existing cluster with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left
   navigation pane, choose **Clusters**, and
   select the cluster that you want to update.
3. On the **Instances** tab of the cluster
   details page, find the **Instance group
   settings** section. Select **Edit
   cluster scaling** to specify new values for the
   **Minimum** and
   **Maximum** number of instances and the
   **On-Demand** limit.

## Use the AWS CLI to configure managed

scaling

You can use AWS CLI commands for Amazon EMR to configure managed scaling when you
create a cluster. You can use a shorthand syntax, specifying the JSON
configuration inline within the relevant commands, or you can reference a file
containing the configuration JSON. You can also apply a managed scaling policy
to an existing cluster and remove a managed scaling policy that was previously
applied. In addition, you can retrieve details of a scaling policy configuration
from a running cluster.

**Enabling Managed Scaling During Cluster
Launch**

You can enable managed scaling during cluster launch as the following example
demonstrates.

```
aws emr create-cluster \
 --service-role EMR_DefaultRole \
 --release-label emr-7.11.0 \
 --name EMR_Managed_Scaling_Enabled_Cluster \
 --applications Name=Spark Name=Hbase \
 --ec2-attributes KeyName=keyName,InstanceProfile=EMR_EC2_DefaultRole \
 --instance-groups InstanceType=m4.xlarge,InstanceGroupType=MASTER,InstanceCount=1 InstanceType=m4.xlarge,InstanceGroupType=CORE,InstanceCount=2 \
 --region us-east-1 \
 --managed-scaling-policy ComputeLimits='{MinimumCapacityUnits=2,MaximumCapacityUnits=4,UnitType=Instances}'
```

You can also specify a managed policy configuration using the
--managed-scaling-policy option when you use `create-cluster`.

**Applying a Managed Scaling Policy to an Existing
Cluster**

You can apply a managed scaling policy to an existing cluster as the following
example demonstrates.

```
aws emr put-managed-scaling-policy
--cluster-id `j-123456`
--managed-scaling-policy ComputeLimits='{MinimumCapacityUnits=`1`,
MaximumCapacityUnits=`10`,  MaximumOnDemandCapacityUnits=`10`, UnitType=`Instances`}'
```

You can also apply a managed scaling policy to an existing cluster by using
the `aws emr put-managed-scaling-policy` command. The following
example uses a reference to a JSON file, `managedscaleconfig.json`,
that specifies the managed scaling policy configuration.

```
aws emr put-managed-scaling-policy --cluster-id `j-123456` --managed-scaling-policy file://./managedscaleconfig.json
```

The following example shows the contents of the
`managedscaleconfig.json` file, which defines the managed scaling
policy.

```
{
    "ComputeLimits": {
        "UnitType": "`Instances`",
        "MinimumCapacityUnits": `1`,
        "MaximumCapacityUnits": `10`,
        "MaximumOnDemandCapacityUnits": `10`
    }
}
```

**Retrieving a Managed Scaling Policy
Configuration**

The `GetManagedScalingPolicy` command retrieves the policy
configuration. For example, the following command retrieves the configuration
for the cluster with a cluster ID of `j-123456`.

```
aws emr get-managed-scaling-policy --cluster-id `j-123456`
```

The command produces the following example output.

```
{
   "ManagedScalingPolicy": {
      "ComputeLimits": {
         "MinimumCapacityUnits": `1`,
         "MaximumOnDemandCapacityUnits": `10`,
         "MaximumCapacityUnits": `10`,
         "UnitType": "Instances"
      }
   }
}
```

For more information about using Amazon EMR commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

**Removing Managed Scaling Policy**

The `RemoveManagedScalingPolicy` command removes the policy
configuration. For example, the following command removes the configuration for
the cluster with a cluster ID of `j-123456`.

```
aws emr remove-managed-scaling-policy --cluster-id `j-123456`
```

## Use AWS SDK for Java to configure managed

scaling

The following program excerpt shows how to configure managed scaling using the
AWS SDK for Java:

```
package com.amazonaws.emr.sample;

import java.util.ArrayList;
import java.util.List;

import com.amazonaws.AmazonClientException;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.elasticmapreduce.AmazonElasticMapReduce;
import com.amazonaws.services.elasticmapreduce.AmazonElasticMapReduceClientBuilder;
import com.amazonaws.services.elasticmapreduce.model.Application;
import com.amazonaws.services.elasticmapreduce.model.ComputeLimits;
import com.amazonaws.services.elasticmapreduce.model.ComputeLimitsUnitType;
import com.amazonaws.services.elasticmapreduce.model.InstanceGroupConfig;
import com.amazonaws.services.elasticmapreduce.model.JobFlowInstancesConfig;
import com.amazonaws.services.elasticmapreduce.model.ManagedScalingPolicy;
import com.amazonaws.services.elasticmapreduce.model.RunJobFlowRequest;
import com.amazonaws.services.elasticmapreduce.model.RunJobFlowResult;

public class CreateClusterWithManagedScalingWithIG {

	public static void main(String[] args) {
		AWSCredentials credentialsFromProfile = getCreadentials("AWS-Profile-Name-Here");

		/**
		 * Create an Amazon EMR client with the credentials and region specified in order to create the cluster
		 */
		AmazonElasticMapReduce emr = AmazonElasticMapReduceClientBuilder.standard()
			.withCredentials(new AWSStaticCredentialsProvider(credentialsFromProfile))
			.withRegion(Regions.US_EAST_1)
			.build();

		/**
		 * Create Instance Groups - Primary, Core, Task
		 */
		InstanceGroupConfig instanceGroupConfigMaster = new InstanceGroupConfig()
				.withInstanceCount(1)
				.withInstanceRole("MASTER")
				.withInstanceType("m4.large")
				.withMarket("ON_DEMAND");

		InstanceGroupConfig instanceGroupConfigCore = new InstanceGroupConfig()
			.withInstanceCount(4)
			.withInstanceRole("CORE")
			.withInstanceType("m4.large")
			.withMarket("ON_DEMAND");

		InstanceGroupConfig instanceGroupConfigTask = new InstanceGroupConfig()
			.withInstanceCount(5)
			.withInstanceRole("TASK")
			.withInstanceType("m4.large")
			.withMarket("ON_DEMAND");

		List<InstanceGroupConfig> igConfigs = new ArrayList<>();
		igConfigs.add(instanceGroupConfigMaster);
		igConfigs.add(instanceGroupConfigCore);
		igConfigs.add(instanceGroupConfigTask);

        /**
         *  specify applications to be installed and configured when Amazon EMR creates the cluster
         */
		Application hive = new Application().withName("Hive");
		Application spark = new Application().withName("Spark");
		Application ganglia = new Application().withName("Ganglia");
		Application zeppelin = new Application().withName("Zeppelin");

		/**
		 * Managed Scaling Configuration -
         * Using UnitType=Instances for clusters composed of instance groups
		 *
         * Other options are:
         * UnitType = VCPU ( for clusters composed of instance groups)
         * UnitType = InstanceFleetUnits ( for clusters composed of instance fleets)
         **/
		ComputeLimits computeLimits = new ComputeLimits()
				.withMinimumCapacityUnits(1)
				.withMaximumCapacityUnits(20)
				.withUnitType(ComputeLimitsUnitType.Instances);

		ManagedScalingPolicy managedScalingPolicy = new ManagedScalingPolicy();
		managedScalingPolicy.setComputeLimits(computeLimits);

		// create the cluster with a managed scaling policy
		RunJobFlowRequest request = new RunJobFlowRequest()
	       		.withName("EMR_Managed_Scaling_TestCluster")
	       		.withReleaseLabel("emr-7.11.0")          // Specifies the version label for the Amazon EMR release; we recommend the latest release
	       		.withApplications(hive,spark,ganglia,zeppelin)
	       		.withLogUri("s3://path/to/my/emr/logs")  // A URI in S3 for log files is required when debugging is enabled.
	       		.withServiceRole("EMR_DefaultRole")      // If you use a custom IAM service role, replace the default role with the custom role.
	       		.withJobFlowRole("EMR_EC2_DefaultRole")  // If you use a custom Amazon EMR role for EC2 instance profile, replace the default role with the custom Amazon EMR role.
	       		.withInstances(new JobFlowInstancesConfig().withInstanceGroups(igConfigs)
	       	   		.withEc2SubnetId("subnet-123456789012345")
	           		.withEc2KeyName("my-ec2-key-name")
	           		.withKeepJobFlowAliveWhenNoSteps(true))
	       		.withManagedScalingPolicy(managedScalingPolicy);
	   RunJobFlowResult result = emr.runJobFlow(request);

	   System.out.println("The cluster ID is " + result.toString());
	}

	public static AWSCredentials getCredentials(String profileName) {
		// specifies any named profile in .aws/credentials as the credentials provider
		try {
			return new ProfileCredentialsProvider("AWS-Profile-Name-Here")
					.getCredentials();
        } catch (Exception e) {
            throw new AmazonClientException(
                    "Cannot load credentials from .aws/credentials file. " +
                    "Make sure that the credentials file exists and that the profile name is defined within it.",
                    e);
        }
	}

	public CreateClusterWithManagedScalingWithIG() { }
}
```
