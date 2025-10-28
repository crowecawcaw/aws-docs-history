# Create a cluster with JupyterHub

You can create an Amazon EMR cluster with JupyterHub using the AWS Management Console, AWS Command Line Interface, or
the Amazon EMR API. Ensure that the cluster is not created with the option to terminate
automatically after completing steps (`--auto-terminate` option in the
AWS CLI). Also, make sure that administrators and notebook users can access the key
pair that you use when you create the cluster. For more information, see [Use a key pair for SSH
credentials](../ManagementGuide/emr-plan-access-ssh.md "../ManagementGuide/emr-plan-access-ssh.md") in the _Amazon EMR Management Guide_.

## Create a cluster with JupyterHub using the console

Use the following procedure to create a cluster with JupyterHub installed using
**Advanced Options** in the Amazon EMR console.

###### To create an Amazon EMR cluster with JupyterHub installed using the Amazon EMR

console

1. Navigate to the new Amazon EMR console and select **Switch to the old console** from the side navigation. For more information on what to expect when you switch to the old console, see [Using the old console](../ManagementGuide/whats-new-in-console.md#console-opt-in "../ManagementGuide/whats-new-in-console.md#console-opt-in").
2. Choose **Create cluster**, **Go to advanced options**.
3. Under **Software Configuration**:
   - For **Release**, select emr-5.36.2, and choose JupyterHub.
   - If you use Spark, to use the AWS Glue Data Catalog as the metastore for Spark SQL, select **Use
     for Spark table metadata**. For more information, see
     [Use AWS Glue Data Catalog catalog with Spark on Amazon EMR](emr-spark-glue.md "emr-spark-glue.md").
   - For **Edit software settings** choose **Enter configuration** and specify values, or choose **Load JSON from S3** and specify a JSON configuration file. For more information, see [Configuring JupyterHub](emr-jupyterhub-configure.md "emr-jupyterhub-configure.md").

4. Under **Add steps (optional)** configure steps to run when the cluster is created, make sure that **Auto-terminate cluster after the last step is completed** is not selected, and choose **Next**.
5. Choose **Hardware Configuration** options, **Next**. For more information, see [Configure cluster hardware and networking](../ManagementGuide/emr-plan-instances.md "../ManagementGuide/emr-plan-instances.md") in the _Amazon EMR Management Guide_.
6. Choose options for **General Cluster Settings**, **Next**.
7. Choose **Security Options**, specifying a key pair, and choose **Create Cluster**.

## Create a cluster with JupyterHub using the AWS CLI

To launch a cluster with JupyterHub, use the `aws emr create-cluster`
command and, for the `--applications` option, specify
`Name=JupyterHub`. The following example launches a JupyterHub
cluster on Amazon EMR with two EC2 instances (one master and one core instance). Also,
debugging is enabled, with logs stored in the Amazon S3 location as specified by
`--log-uri`. The specified key pair provides access to Amazon EC2
instances in the cluster.

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --name="`MyJupyterHubCluster`" --release-label emr-5.36.2 \
--applications Name=JupyterHub --log-uri `s3://amzn-s3-demo-bucket/MyJupyterClusterLogs` \
--use-default-roles --instance-type m5.xlarge --instance-count `2` --ec2-attributes KeyName=`MyKeyPair`
```
