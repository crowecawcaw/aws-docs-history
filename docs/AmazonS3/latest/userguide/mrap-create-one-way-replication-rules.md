# Create one-way replication rules for your Multi-Region Access Point

Replication rules enable automatic and asynchronous copying of objects across buckets.
A one-way replication rule helps ensure that data is fully replicated from a source
bucket in one AWS Region to a destination bucket in another Region. When one-way
replication is set up, a replication rule from the source bucket (`amzn-s3-demo-bucket`)
to the destination bucket (`amzn-s3-demo-bucket`) is created. Like all replication rules,
you can apply the one-way replication rule to the entire Amazon S3 bucket or to a subset of
objects that are filtered by a prefix or object tags.

###### Important

We
recommend using one-way replication if your users will only be consuming the objects
in your destination buckets. If your users will be uploading or modifying the
objects in your destination buckets, use two-way replication to keep all of your
buckets in sync. We also recommend two-way replication if you plan to use your
Multi-Region Access Point for failover. To set up two-way replication, see [Create two-way replication rules for your Multi-Region Access Point](mrap-create-two-way-replication-rules.md "mrap-create-two-way-replication-rules.md").

###### To create a one-way replication rule for your Multi-Region Access Point

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Multi-Region Access Points**.
3. Choose the name of your Multi-Region Access Point.
4. Choose the **Replication and failover** tab.
5. Scroll down to the **Replication rules** section, and then
   choose **Create replication rules**. Make sure that you have
   sufficient permissions to create the replication rule, or
   versioning
   will be disabled.

###### Note

You can create replication rules only for buckets in your own account. To
create replication rules for external buckets, the bucket owners must create
the replication rules for those buckets. 6. On the **Create replication rules** page, choose the
**Replicate objects from one or more source buckets to one or more
destination buckets**
template.

###### Important

When you create replication rules by using this template, they replace any
existing
replication
rules that are already assigned to the bucket.

To add to or modify any existing replication rules instead of replacing
them, go to each bucket's **Management** tab in the
console, and then edit the rules in the **Replication
rules** section. You can also add to or modify existing
replication rules by using the AWS CLI, SDKs, or REST API. For more
information, see [Replication configuration file elements](replication-add-config.md "replication-add-config.md"). 7. In the **Source and destination** section, under
**Source buckets**, select one or more buckets that you
want to replicate objects from. All buckets (source and destination) that are
chosen for replication must have S3 Versioning enabled, and each bucket must
reside in a different AWS Region. For more information about S3 Versioning, see
[Using versioning in Amazon S3 buckets](Versioning.md "Versioning.md").

Under **Destination buckets**, select one or more buckets
that you want to replicate objects to. 8. In the **Replication rule configuration** section, choose
whether the replication rule will be **Enabled** or
**Disabled** when it's created.

###### Note

You can't enter a name in the **Replication rule name**
box. Replication rule names are generated based on your configuration when
you create the replication rule. 9. In the **Scope** section, choose the appropriate scope for
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
    	 use a delimiter such as a `/` (forward slash) to
    	 indicate its level of hierarchy (for example,
    	 `pictures/`). For more information about
    	 prefixes, see [Organizing objects using prefixes](using-prefixes.md "using-prefixes.md").


    	+ To replicate all objects that have one or more object tags,
    	 choose **Add tag** and enter the key-value pair
    	 in the boxes. To add another tag, repeat the procedure. For more
    	 information about object tags, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md").

10. Scroll down to the **Additional replication options**
    section, and select the replication options that you want to apply.

###### Note

We recommend that you apply the following
options:

    * **Replication time control (RTC)** – To
     replicate your data across different Regions within a predictable
     time frame, you can use S3 Replication Time Control (S3 RTC). S3 RTC replicates 99.99
     percent of new objects stored in Amazon S3 within 15 minutes (backed by a
     service-level agreement). For more information, see
     [Meeting compliance requirements with S3 Replication Time Control](replication-time-control.md "replication-time-control.md").
    * **Replication metrics and notifications**
     – Enable Amazon CloudWatch metrics to monitor replication
     events.
    * **Delete marker replication** – Delete
     markers created by S3 delete operations will be replicated. Delete
     markers created by lifecycle rules are not replicated. For more
     information, see [Replicating delete markers between buckets](delete-marker-replication.md "delete-marker-replication.md").There are additional charges for S3 RTC and CloudWatch replication metrics and

notifications. For more information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/") and
[Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). 11. If you're writing a new replication rule that replaces an existing one, select
**I acknowledge that by choosing Create replication rules, these
existing replication rules will be overwritten**. 12. Choose **Create replication rules** to create and save your
new one-way replication rule.
