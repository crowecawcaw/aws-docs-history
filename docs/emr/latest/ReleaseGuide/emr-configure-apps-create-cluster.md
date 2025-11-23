# Configure applications when you

create a cluster

When you create a cluster, you can override the default configurations for
applications using the Amazon EMR console, the AWS Command Line Interface (AWS CLI), or the AWS SDK.

To override the default configuration for an application, you specify custom values in
a configuration classification. A configuration classification corresponds to a
configuration XML file for an application, such as `hive-site.xml`.

Configuration classifications vary by Amazon EMR release version. For a list of
configuration classifications that are available in a specific release version, see the
release detail page. For example, [Amazon EMR release
6.4.0.](emr-640-release.md#emr-640-class "emr-640-release.md#emr-640-class")

## Supply a configuration

in the console when you create a cluster

To supply a configuration, navigate to the **Create cluster**
page and expand **Software settings**. You can then enter the
configuration directly by using either JSON or a shorthand syntax demonstrated in
shadow text in the console. Otherwise, you can provide an Amazon S3 URI for a file with a
JSON `Configurations` object.

To supply a configuration for an instance group, choose a cluster in your list of clusters, then choose the
**Configurations** tab. In the **Instance group configurations** table, choose
the instance group to edit, then choose **Reconfigure**.

## Supply a configuration using

the AWS CLI when you create a cluster

You can provide a configuration to **create-cluster** by supplying
a path to a JSON file stored locally or in Amazon S3. The following example assumes that
you are using default roles for Amazon EMR and that the roles have been created. If you
need to create the roles, run `aws emr create-default-roles`
first.

If your configuration is in your local directory, you can use the following
example command.

```
aws emr create-cluster --use-default-roles --release-label `emr-7.12.0` --applications Name=Hive \
--instance-type m5.xlarge --instance-count 3 --configurations file://./configurations.json
```

If your configuration is in an Amazon S3 path, you'll need to set up the following
workaround before passing the Amazon S3 path to the `create-cluster`
command.

```
#!/bin/sh
# Assume the ConfigurationS3Path is not public, and its present in the same AWS account as the EMR cluster
ConfigurationS3Path="s3://amzn-s3-demo-bucket/config.json"
# Get a presigned HTTP URL for the s3Path
ConfigurationURL=`aws s3 presign $ConfigurationS3Path --expires-in 300`
# Fetch the presigned URL, and minify the JSON so that it spans only a single line
Configurations=`curl $ConfigurationURL | jq -c .`
aws emr create-cluster --use-default-roles --release-label emr-5.34.0 --instance-type m5.xlarge --instance-count 2 --applications Name=Hadoop Name=Spark --configurations $Configurations
```

## Supply a configuration using

the Java SDK when you create a cluster

The following program excerpt shows how to supply a configuration using the
AWS SDK for Java.

```
Application hive = new Application().withName("Hive");

Map<String,String> hiveProperties = new HashMap<String,String>();
	hiveProperties.put("hive.join.emit.interval","1000");
	hiveProperties.put("hive.merge.mapfiles","true");

Configuration myHiveConfig = new Configuration()
	.withClassification("hive-site")
	.withProperties(hiveProperties);

RunJobFlowRequest request = new RunJobFlowRequest()
	.withName("Create cluster with ReleaseLabel")
	.withReleaseLabel("emr-5.20.0")
	.withApplications(hive)
	.withConfigurations(myHiveConfig)
	.withServiceRole("EMR_DefaultRole")
	.withJobFlowRole("EMR_EC2_DefaultRole")
	.withInstances(new JobFlowInstancesConfig()
		.withEc2KeyName("myEc2Key")
		.withInstanceCount(3)
		.withKeepJobFlowAliveWhenNoSteps(true)
		.withMasterInstanceType("m4.large")
		.withSlaveInstanceType("m4.large")
	);

```
