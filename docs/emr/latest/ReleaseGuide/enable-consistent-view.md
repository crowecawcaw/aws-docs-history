# Enable consistent view

You can enable Amazon S3 server-side encryption or consistent view for EMRFS using the
AWS Management Console, AWS CLI, or
the `emrfs-site` configuration classification.

###### To configure consistent view using the

console

1. Navigate to the new Amazon EMR console and select **Switch to the old console** from the side navigation. For more information on what to expect when you switch to the old console, see [Using the old console](../ManagementGuide/whats-new-in-console.md#console-opt-in "../ManagementGuide/whats-new-in-console.md#console-opt-in").
2. Choose **Create cluster**, **Go to advanced options**.
3. Choose settings for **Step 1: Software and Steps** and **Step 2: Hardware**.
4. For **Step 3: General Cluster Settings**, under **Additional Options**, choose **EMRFS consistent view**.
5. For **EMRFS Metadata store**, type the name of your
   metadata store. The default value is
   `EmrFSMetadata`. If the EmrFSMetadata table
   does not exist, it is created for you in DynamoDB.

###### Note

Amazon EMR does not automatically remove the EMRFS metadata from DynamoDB
when the cluster is terminated. 6. For **Number of retries**, type an integer value. If an inconsistency
is detected, EMRFS tries to call Amazon S3 this number of times. The default
value is `5`. 7. For **Retry period (in seconds)**, type an integer
value. This is the amount of time that EMRFS waits between retry attempts. The default value is
`10`.

###### Note

Subsequent retries use an exponential backoff.

###### To launch a cluster with consistent view enabled using the AWS CLI

We recommend that you install the current version of AWS CLI. To download the latest
release, see [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").

- ###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --instance-type `m5.xlarge` --instance-count `3` --emrfs Consistent=`true` \
--release-label `emr-7.10.0` --ec2-attributes KeyName=`myKey`
```

###### To check if consistent view is enabled using the AWS Management Console

- To check whether consistent view is enabled in the console, navigate to the
  **Cluster List** and select your cluster name to view
  **Cluster Details**. The "EMRFS consistent view" field has
  a value of `Enabled` or `Disabled`.

###### To check if consistent view is enabled by examining the

`emrfs-site.xml` file

- You can check if consistency is enabled by inspecting the
  `emrfs-site.xml` configuration file on the master
  node of the cluster. If the Boolean value for
  `fs.s3.consistent` is set to `true`
  then consistent view is enabled for file system operations involving
  Amazon S3.
