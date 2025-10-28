# Consistent view

###### Warning

On June 1, 2023, EMRFS consistent view will reach end of standard
support for future Amazon EMR releases. EMRFS consistent view will continue to
work for existing releases.

With the release of Amazon S3 strong read-after-write consistency on December 1, 2020, you no
longer need to use EMRFS consistent view (EMRFS CV) with your Amazon EMR
clusters. EMRFS CV is an optional feature that allows Amazon EMR clusters to check
for list and read-after-write consistency for Amazon S3 objects. When you create a
cluster and EMRFS CV is turned on, Amazon EMR creates an Amazon DynamoDB database to
store object metadata that it uses to track list and read-after-write consistency for S3
objects. You can now turn off EMRFS CV and delete the DynamoDB database that it
uses so that you don't accrue additional costs. The following procedures explain how to
check for the CV feature, turn it off, and delete the DynamoDB database that the feature
uses.

###### To check if you're using the EMRFS

CV feature

1. Navigate to the **Configuration** tab. If your cluster
   has the following configuration, it uses EMRFS CV.

```
Classification=emrfs-site,Property=fs.s3.consistent,Value=true
```

2. Alternatively, use the AWS CLI to describe your cluster with the [`describe-cluster` API](../../../cli/latest/reference/emr/describe-cluster.md "../../../cli/latest/reference/emr/describe-cluster.md"). If the output contains
   `fs.s3.consistent: true`, your cluster uses EMRFS
   CV.

###### To turn off EMRFS CV on your Amazon EMR clusters

To turn off the EMRFS CV feature, use one of the following three
options. You should test these options in your testing environment before
applying them to your production environments.

1. ###### To stop your existing cluster and start a new cluster without

   EMRFS CV options.
   1. Before you stop your cluster, ensure that you back up your data
      and notify your users.
   2. To stop your cluster, follow the instructions in [Terminate a cluster](../ManagementGuide/UsingEMR_TerminateJobFlow.md "../ManagementGuide/UsingEMR_TerminateJobFlow.md").
   3. If you use the Amazon EMR console to create new cluster, navigate to
      **Advanced Options**. In the **Edit
      software settings** section, deselect the option to
      turn on EMRFS CV. If the check box for
      **EMRFS consistent view** is
      available, keep it unchecked.
   4. If you use AWS CLI to create a new cluster with the [`create-cluster` API](../../../cli/latest/reference/emr/create-cluster.md "../../../cli/latest/reference/emr/create-cluster.md"), don't use the
      `--emrfs` option, which turns on EMRFS
      CV.
   5. If you use an SDK or AWS CloudFormation to create a new cluster, don't use any
      of the configurations listed in [Configure consistent view](emrfs-configure-consistent-view.md "emrfs-configure-consistent-view.md").

2. ###### To clone a cluster and remove EMRFS CV
   1. In the Amazon EMR console, choose the cluster that uses EMRFS
      CV.
   2. At the top of the **Cluster Details** page,
      choose **Clone**.
   3. Choose **Previous** and navigate to
      **Step 1: Software and Steps**.
   4. In **Edit software settings**, remove
      EMRFS CV. In **Edit configuration**,
      delete the following configurations in the `emrfs-site`
      classification. If you're loading JSON from a S3 bucket, you must
      modify your S3 object.

   ```
   [
   	{"classification":
   		"emrfs-site",
   		"properties": {
   			"fs.s3.consistent.retryPeriodSeconds":"10",
   			"fs.s3.consistent":"true",
   			"fs.s3.consistent.retryCount":"5",
   			"fs.s3.consistent.metadata.tableName":"EmrFSMetadata"
   		}
   	}
   ]
   ```

3. ###### To remove EMRFS CV from a cluster that uses instance

   groups
   1. Use the following command to check if a single EMR cluster uses
      the DynamoDB table that is associated with EMRFS CV, or if
      multiple clusters share the table. The table name is specified in
      `fs.s3.consistent.metadata.tableName`, as described
      in [Configure consistent view](emrfs-configure-consistent-view.md "emrfs-configure-consistent-view.md"). The default table name used
      by EMRFS CV is `EmrFSMetadata`.

   ```
   aws emr describe-cluster --cluster-id j-XXXXX | grep fs.s3.consistent.metadata.tableName
   ```

   2. If your cluster doesn't share your DynamoDB database with another
      cluster, use the following command to reconfigure the cluster and
      deactivate EMRFS CV. For more information, see [Reconfigure an instance group in a running
      cluster](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").

   ```
   aws emr modify-instance-groups --cli-input-json file://disable-emrfs-1.json
   ```

   This command opens the file you want to modify. Modify the file
   with the following configurations.

   ```
   {
   	"ClusterId": "j-xxxx",
   	"InstanceGroups": [
   		{
   			"InstanceGroupId": "ig-xxxx",
   			"Configurations": [
   				{
   					"Classification": "emrfs-site",
   					"Properties": {
   						"fs.s3.consistent": "false"
   					},
   					"Configurations": []
   				}
   			]
   		}
   	]
   }
   ```

   3. If your cluster shares the DynamoDB table with another cluster, turn
      off EMRFS CV on all clusters at a time when no clusters
      modify any objects in the shared S3 location.

###### To delete Amazon DynamoDB resources associated with EMRFS CV

After you remove EMRFS CV from your Amazon EMR clusters, delete the DynamoDB
resources associated with EMRFS CV. Until you do so, you continue to
incur DynamoDB charges associated with EMRFS CV.

1. Check the CloudWatch metrics for your DynamoDB table and confirm that the table
   isn't used by any clusters.
2. Delete the DynamoDB table.

```
aws dynamodb delete-table --table-name `<your-table-name>`
```

###### To delete Amazon SQS resources associated with EMRFS CV

1. If you configured your cluster to push inconsistency notifications to
   Amazon SQS, you can delete all SQS queues.
2. Find the Amazon SQS queue name specified in
   `fs.s3.consistent.notification.SQS.queueName`, as described
   in [Configure consistent view](emrfs-configure-consistent-view.md "emrfs-configure-consistent-view.md"). The default queue name format is
   `EMRFS-Inconsistency-`<j-cluster
   ID>``.

```
aws sqs list-queues | grep ‘EMRFS-Inconsistency’
aws sqs delete-queue –queue-url `<your-queue-url>`
```

###### To stop using the EMRFS CLI

- The [EMRFS
  CLI](emrfs-cli-reference.md "emrfs-cli-reference.md") manages the metadata that EMRFS CV generates. As
  standard support for EMRFS CV reaches its end in future releases
  of Amazon EMR, support for the EMRFS CLI will also reach its end.

###### Topics

- [Enable consistent view](enable-consistent-view.md "enable-consistent-view.md")
- [Understanding how EMRFS consistent view tracks
  objects in Amazon S3](emrfs-files-tracked.md "emrfs-files-tracked.md")
- [Retry logic](emrfs-retry-logic.md "emrfs-retry-logic.md")
- [EMRFS consistent view metadata](emrfs-metadata.md "emrfs-metadata.md")
- [Configure consistency notifications for CloudWatch and
  Amazon SQS](emrfs-configure-sqs-cw.md "emrfs-configure-sqs-cw.md")
- [Configure consistent view](emrfs-configure-consistent-view.md "emrfs-configure-consistent-view.md")
- [EMRFS CLI Command Reference](emrfs-cli-reference.md "emrfs-cli-reference.md")
