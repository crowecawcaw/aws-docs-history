# Create two-way replication rules
 for your Multi-Region Access Point

Replication rules enable automatic and asynchronous copying of objects across buckets.
 A two-way replication rule (also known as a bidirectional replication rule) ensures that
 data is fully synchronized between two or more buckets in different AWS Regions. When
 two-way replication is set up, a replication rule from the source bucket
 (DOC-EXAMPLE-BUCKET-1) to the bucket containing the replicas (DOC-EXAMPLE-BUCKET-2) is
 created. Then, a second replication rule from the bucket containing the replicas
 (DOC-EXAMPLE-BUCKET-2) to the source bucket (DOC-EXAMPLE-BUCKET-1) is created.

Like all replication rules, you can apply the two-way replication rule to the entire
 Amazon S3 bucket or to a subset of objects filtered by a prefix or object tags. You can also
 keep metadata changes to your objects in sync by [enabling replica modification sync](replication-for-metadata-changes.md#enabling-replication-for-metadata-changes "replication-for-metadata-changes.md#enabling-replication-for-metadata-changes") for each replication rule. You can
 enable replica modification sync through the
 Amazon S3
 console, the AWS CLI, the AWS SDKs, the Amazon S3 REST API, or
 AWS CloudFormation.

To monitor the replication progress of objects and object metadata in Amazon CloudWatch, enable
 S3 Replication metrics and notifications. For more information, see [Monitoring progress with replication metrics and Amazon S3 event
 notifications](replication-metrics.md "replication-metrics.md").

###### To create a two-way replication rule for your Multi-Region Access Point

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Multi-Region Access Points**.
3. Choose the name of the Multi-Region Access Point that you want to update.
4. Choose the **Replication and failover** tab.
5. Scroll down to the **Replication rules** section, and then
 choose **Create replication rules**.
6. On the **Create replication rules** page, choose the
 **Replicate objects among all specified buckets** template.
 The **Replicate objects among all specified buckets** template
 sets up two-way replication (with failover capabilities) for your
 buckets.


###### Important

When you create replication rules by using this template, they replace any
 existing
 replication
 rules that are already assigned to the bucket. 

To add to or modify any existing replication rules instead of replacing
 them, go to each bucket's **Management** tab in the
 console, and then edit the rules in the **Replication
 rules** section. You can also add to or modify existing
 replication rules by using the AWS CLI, AWS SDKs, or Amazon S3 REST API. For more
 information, see [Replication configuration file elements](replication-add-config.md "replication-add-config.md").
7. In the **Buckets** section, select at least two buckets that
 you want to replicate objects from. All buckets chosen for replication must have
 S3 Versioning enabled, and each bucket must reside in a different AWS Region.
 For more information about S3 Versioning, see [Using
 versioning in Amazon S3 buckets](Versioning.md "Versioning.md").


###### Note

Make sure that you have the
 required
 read and replicate permissions to establish replication,
 or
 you
 will encounter errors. For more information, see [Creating an IAM role](setting-repl-config-perm-overview.md "setting-repl-config-perm-overview.md").
8. In the **Replication rule configuration** section, choose
 whether the replication rule will be **Enabled** or
 **Disabled** when it's created.


###### Note

You can't enter a name in the **Replication rule name**
 box. Replication rule names are generated based on your configuration when
 you create the replication rule.
9. In the **Scope** section, choose the appropriate scope for
 your replication.




	* To replicate the whole bucket, choose **Apply to all objects
	 in the bucket**.
	* To replicate a subset of the objects in the bucket, choose
	 **Limit the scope of this rule using one or more
	 filters**. 
	
	
	You can filter your objects by using a prefix, object tags, or a
	 combination of both. 
	
	
	
	
		+ To limit replication to all objects that have names that begin
		 with the same string (for example `pictures`), enter
		 a prefix in the **Prefix** box. 
		
		
		If you enter a prefix that is the name of a folder, you must
		 use a `/` (forward slash) as the last
		 character
		 (for example, `pictures/`).
	
	
		+ To replicate all objects that have one or more object tags,
		 choose **Add tag** and enter the key-value pair
		 in the boxes. To add another tag, repeat the procedure. For more
		 information about object tags, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md").
10. Scroll down to the **Additional replication options**
 section, and select the replication options that you want to apply.


###### Note

We recommend that you apply the following options, especially if you
 intend to configure your Multi-Region Access Point to support
 failover:



	* **Replication time control (RTC)** – To
	 replicate your data across different Regions within a predictable
	 time frame, you can use S3 Replication Time Control (S3 RTC). S3 RTC replicates 99.99
	 percent of new objects stored in Amazon S3 within 15 minutes (backed by a
	 service-level agreement). For more information, see [Meeting compliance requirements with
	 S3 Replication Time Control](replication-time-control.md "replication-time-control.md").
	* **Replication metrics and notifications**
	 – Enable Amazon CloudWatch metrics to monitor replication
	 events.
	* **Delete marker replication** – Delete
	 markers created by S3 delete operations will be replicated. Delete
	 markers created by lifecycle rules are not replicated. For more
	 information, see [Replicating delete markers between buckets](delete-marker-replication.md "delete-marker-replication.md").
	* **Replica modification sync** – Enable
	 replica modification sync for each replication rule to also keep
	 metadata changes to your objects in sync. For more information, see
	 [Enabling replica modification sync](replication-for-metadata-changes.md#enabling-replication-for-metadata-changes "replication-for-metadata-changes.md#enabling-replication-for-metadata-changes").There are additional charges for S3 RTC and CloudWatch replication metrics and
 notifications. For more information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/") and [Amazon CloudWatch
 pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
11. If you're writing a new replication rule that replaces an existing one, select
 **I acknowledge that by choosing Create replication rules, these
 existing replication rules will be overwritten**.
12. Choose **Create replication rules** to create and save your
 new two-way replication rules.
