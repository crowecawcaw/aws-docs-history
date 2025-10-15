# Configuring replication for buckets in the same
 account

Live replication is the automatic, asynchronous copying of objects across general purpose buckets in the
 same or different AWS Regions. Live replication copies newly created objects and object
 updates from a source bucket to a destination bucket or buckets. For more information, see
 [Replicating objects within and across Regions](replication.md "replication.md").

When you configure replication, you add replication rules to the source bucket. Replication rules
 define which source bucket objects to replicate and the destination bucket or buckets where the
 replicated objects are stored. You can create a rule to replicate all the objects in a bucket or
 a subset of objects with a specific key name prefix, one or more object tags, or both. A
 destination bucket can be in the same AWS account as the source bucket, or it can be in a
 different account.

If you specify an object version ID to delete, Amazon S3 deletes that object version in the
 source bucket. But it doesn't replicate the deletion in the destination bucket. In other words,
 it doesn't delete the same object version from the destination bucket. This protects data from
 malicious deletions.

When you add a replication rule to a bucket, the rule is enabled by default, so it starts
 working as soon as you save it. 

In this example, you set up live replication for source and destination buckets that are
 owned by the same AWS account. Examples are provided for using the Amazon S3 console, the
 AWS Command Line Interface (AWS CLI), and the AWS SDK for Java and AWS SDK for .NET.


## Prerequisites


Before you use the following procedures, make sure that you've set up the necessary
 permissions for replication, depending on whether the source and destination buckets are
 owned by the same or different accounts. For more information, see [Setting up permissions for live
 replication](setting-repl-config-perm-overview.md "setting-repl-config-perm-overview.md").


###### Note


* If you want to replicate encrypted objects, you also must grant the necessary
 AWS Key Management Service (AWS KMS) key permissions. For more information, see [Replicating encrypted objects (SSE-S3,
 SSE-KMS, DSSE-KMS, SSE-C)](replication-config-for-kms-objects.md "replication-config-for-kms-objects.md").
* To use Object Lock with replication, you must grant two additional
 permissions on the source S3 bucket in the AWS Identity and Access Management (IAM) role that you use
 to set up replication. The two additional permissions are
 `s3:GetObjectRetention` and `s3:GetObjectLegalHold`.
 If the role has an `s3:Get*` permission statement, that statement
 satisfies the requirement. For more information, see [Using Object Lock with
 S3 Replication](object-lock-managing.md#object-lock-managing-replication "object-lock-managing.md#object-lock-managing-replication").

To configure a replication rule when the destination bucket is in the same AWS account as
 the source bucket, follow these steps.

If the destination bucket is in a different account from the source bucket, you must add a
 bucket policy to the destination bucket to grant the owner of the source bucket account
 permission to replicate objects in the destination bucket. For more information, see [(Optional) Step 3: Granting permissions when the
 source and destination buckets are owned by different AWS accounts](setting-repl-config-perm-overview.md#setting-repl-config-crossacct "setting-repl-config-perm-overview.md#setting-repl-config-crossacct").

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket that you
 want.
4. Choose the **Management** tab, scroll down to **Replication
 rules**, and then choose **Create replication rule**.
5. In the **Replication rule configuration** section, under
 **Replication rule name**, enter a name for your rule to help identify
 the rule later. The name is required and must be unique within the bucket.
6. Under **Status**, **Enabled** is selected by default.
 An enabled rule starts to work as soon as you save it. If you want to enable the rule later,
 choose **Disabled**.
7. If the bucket has existing replication rules, you are instructed to set a priority for
 the rule. You must set a priority for the rule to avoid conflicts caused by objects that are
 included in the scope of more than one rule. In the case of overlapping rules, Amazon S3 uses the
 rule priority to determine which rule to apply. The higher the number, the higher the
 priority. For more information about rule priority, see [Replication configuration file elements](replication-add-config.md "replication-add-config.md").
8. Under **Source bucket**, you have the following options for setting the
 replication source:




	* To replicate the whole bucket, choose **Apply to all objects
	 in the bucket**.
	* To replicate all objects that have the same prefix, choose **Limit the scope
	 of this rule using one or more filters**. This limits replication to all
	 objects that have names that begin with the prefix that you specify (for example
	 `pictures`). Enter a prefix in the **Prefix** box. 
	
	
	###### Note
	
	If you enter a prefix that is the name of a folder, you must use
	 **/** (forward slash) as the last character (for example,
	 `pictures/`).
	* To replicate all objects with one or more object tags, choose **Add
	 tag** and enter the key-value pair in the boxes. Repeat the procedure to add
	 another tag. You can combine a prefix and tags. For more information about object tags,
	 see [Categorizing your objects using tags](object-tagging.md "object-tagging.md").
The new replication configuration XML schema supports prefix and tag filtering and the
 prioritization of rules. For more information about the new schema, see [Backward compatibility
 considerations](replication-add-config.md#replication-backward-compat-considerations "replication-add-config.md#replication-backward-compat-considerations"). For more information about
 the XML used with the Amazon S3 API that works behind the user interface, see [Replication configuration file elements](replication-add-config.md "replication-add-config.md"). The new schema
 is described as *replication configuration XML V2*.
9. Under **Destination**, choose the bucket where you want Amazon S3 to
 replicate objects.


###### Note

The number of destination buckets is limited to the number of AWS Regions in a given
 partition. A partition is a grouping of Regions. AWS currently has three partitions:
 `aws` (Standard Regions), `aws-cn` (China Regions), and
 `aws-us-gov` (AWS GovCloud (US) Regions). To request an increase in your
 destination bucket quota, you can use [service
 quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html "https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html").




	* To replicate to a bucket or buckets in your account, choose **Choose a
	 bucket in this account**, and enter or browse for the destination bucket
	 names.
	* To replicate to a bucket or buckets in a different AWS account, choose
	 **Specify a bucket in another account**, and enter the destination
	 bucket account ID and bucket name. 
	
	
	If the destination is in a different account from the source bucket, you must add a
	 bucket policy to the destination buckets to grant the owner of the source bucket account
	 permission to replicate objects. For more information, see [(Optional) Step 3: Granting permissions when the
	 source and destination buckets are owned by different AWS accounts](setting-repl-config-perm-overview.md#setting-repl-config-crossacct "setting-repl-config-perm-overview.md#setting-repl-config-crossacct").
	
	
	Optionally, if you want to help
	 standardize ownership of new objects in the destination bucket, choose **Change
	 object ownership to the destination bucket owner**. For more information about
	 this option, see [Controlling ownership of objects and disabling ACLs
	 for your bucket](about-object-ownership.md "about-object-ownership.md").
###### Note

If versioning is not enabled on the destination bucket, you get a warning that
 contains an **Enable versioning** button. Choose this button to enable
 versioning on the bucket.
10. Set up an AWS Identity and Access Management (IAM) role that Amazon S3 can assume to replicate objects on your
 behalf.


To set up an IAM role, in the **IAM role** section, select one of
 the following from the **IAM role** dropdown list:




	* We highly recommend that you choose **Create new role** to have
	 Amazon S3 create a new IAM role for you. When you save the rule, a new policy is generated
	 for the IAM role that matches the source and destination buckets that you
	 choose.
	* You can choose to use an existing IAM role. If you do, you must choose a role that
	 grants Amazon S3 the necessary permissions for replication. Replication fails if this role
	 does not grant Amazon S3 sufficient permissions to follow your replication rule.
###### Important

When you add a replication rule to a bucket, you must have the
 `iam:PassRole` permission to be able to pass the IAM role that grants Amazon S3
 replication permissions. For more information, see [Granting a user permissions to pass a
 role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html") in the *IAM User Guide*.
11. To replicate objects in the source bucket that are encrypted with server-side encryption
 with AWS Key Management Service (AWS KMS) keys (SSE-KMS), under **Encryption**, select
 **Replicate objects encrypted with AWS KMS**. Under **AWS KMS keys
 for encrypting destination objects** are the source keys that you allow
 replication to use. All source KMS keys are included by default. To narrow the KMS key
 selection, you can choose an alias or key ID. 


Objects encrypted by AWS KMS keys that you do not select are not replicated. A
 KMS key or a group of KMS keys is chosen for you, but you can choose the KMS keys if
 you want. For information about using AWS KMS with replication, see [Replicating encrypted objects (SSE-S3,
 SSE-KMS, DSSE-KMS, SSE-C)](replication-config-for-kms-objects.md "replication-config-for-kms-objects.md").


###### Important

When you replicate objects that are encrypted with AWS KMS, the AWS KMS request rate
 doubles in the source Region and increases in the destination Region by the same amount.
 These increased call rates to AWS KMS are due to the way that data is re-encrypted by using
 the KMS key that you define for the replication destination Region. AWS KMS has a request
 rate quota that is per calling account per Region. For information about the quota
 defaults, see [AWS KMS Quotas -
 Requests per Second: Varies](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second "https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second") in the *AWS Key Management Service Developer Guide*. 

If your current Amazon S3 `PUT` object request rate during replication is more
 than half the default AWS KMS rate limit for your account, we recommend that you request an
 increase to your AWS KMS request rate quota. To request an increase, create a case in the
 Support Center at [Contact Us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/"). For example,
 suppose that your current `PUT` object request rate is 1,000 requests per
 second and you use AWS KMS to encrypt your objects. In this case, we recommend that you ask
 Support to increase your AWS KMS rate limit to 2,500 requests per second, in both your source
 and destination Regions (if different), to ensure that there is no throttling by AWS KMS. 

To see your `PUT` object request rate in the source bucket, view
 `PutRequests` in the Amazon CloudWatch request metrics for Amazon S3. For information about
 viewing CloudWatch metrics, see [Using the S3 console](configure-request-metrics-bucket.md#configure-metrics "configure-request-metrics-bucket.md#configure-metrics").


If you chose to replicate objects encrypted with AWS KMS, do the following: 


	1. Under **AWS KMS key for encrypting destination objects** ,
	 specify your KMS key in one of the following ways:
	
	
	
	
		* To choose from a list of available KMS keys, choose **Choose from your
		 AWS KMS keys**, and choose your **KMS key** from
		 the list of available keys.
		
		
		Both the AWS managed key (`aws/s3`) and your customer managed keys appear in
		 this list. For more information about customer managed keys, see [Customer keys and AWS
		 keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt") in the *AWS Key Management Service Developer Guide*.
		* To enter the KMS key Amazon Resource Name (ARN), choose **Enter
		 AWS KMS key ARN**, and enter your KMS key ARN in the field that
		 appears. This encrypts the replicas in the destination bucket. You can find the ARN
		 for your KMS key in the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), under **Encryption keys**.
		* To create a new customer managed key in the AWS KMS console, choose **Create a
		 KMS key**.
		
		
		For more information about creating an AWS KMS key, see [Creating
		 keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html "https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html") in the *AWS Key Management Service Developer Guide*.
	###### Important
	
	You can only use KMS keys that are enabled in the same AWS Region as the
	 bucket. When you choose **Choose from your KMS keys**, the S3
	 console lists only 100 KMS keys per Region. If you have more than 100 KMS keys in
	 the same Region, you can see only the first 100 KMS keys in the S3 console. To use a
	 KMS key that is not listed in the console, choose **Enter AWS KMS key
	 ARN**, and enter your KMS key ARN.
	
	When you use an AWS KMS key for server-side encryption in Amazon S3, you must choose
	 a symmetric encryption KMS key. Amazon S3 supports only symmetric encryption KMS keys
	 and not asymmetric KMS keys. For more information, see [Identifying symmetric and
	 asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html "https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html") in the *AWS Key Management Service Developer
	 Guide*.
	
	
	For more information about creating an AWS KMS key, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html "https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html") in the
	 *AWS Key Management Service Developer Guide*. For more information about using AWS KMS with
	 Amazon S3, see [Using server-side encryption with AWS KMS keys
	 (SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md").
12. Under **Destination storage
 class**, if you want to replicate your data into a specific storage class in the destination,
 choose **Change the storage class for the replicated objects**. Then
 choose the storage class that you want to use for the replicated objects in the
 destination. If you don't choose this option, the storage class for replicated objects
 is the same class as the original objects.
13. You have the following additional options while setting the **Additional
 replication options**:




	* If you want to enable S3 Replication Time Control (S3 RTC) in your replication configuration, select
	 **Replication Time Control (RTC)**. For more information about this
	 option, see [Meeting compliance requirements with
	 S3 Replication Time Control](replication-time-control.md "replication-time-control.md").
	* If you want to enable S3 Replication metrics in your replication configuration, select
	 **Replication metrics and events**. For more information, see [Monitoring replication with metrics, event notifications,
	 and statuses](replication-metrics.md "replication-metrics.md").
	* If you want to enable delete marker replication in your replication configuration, select
	 **Delete marker replication**. For more information, see [Replicating delete markers between
	 buckets](delete-marker-replication.md "delete-marker-replication.md").
	* If you want to enable Amazon S3 replica modification sync in your replication configuration,
	 select **Replica modification sync**. For more information, see [Replicating metadata changes with
	 replica modification sync](replication-for-metadata-changes.md "replication-for-metadata-changes.md").
###### Note

When you use S3 RTC or S3 Replication metrics, additional fees apply.
14. To finish, choose **Save**.
15. After you save your rule, you can edit, enable, disable, or delete your rule by
 selecting your rule and choosing **Edit rule**.
To use the AWS CLI to set up replication when the source and destination buckets are
 owned by the same AWS account, you do the following:


* Create source and destination buckets.
* Enable versioning on the buckets.
* Create an AWS Identity and Access Management (IAM) role that gives Amazon S3 permission to replicate
 objects.
* Add the replication configuration to the source bucket.
To verify your setup, you test it.

###### To set up replication when the source and destination buckets are owned by
 the same AWS account

1. Set a credentials profile for the AWS CLI. This example uses the profile
 name `acctA`. For information about setting credential profiles
 and using named profiles, see [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html") in the *AWS Command Line Interface User Guide*. 


###### Important

The profile that you use for this example must have the necessary
 permissions. For example, in the replication configuration, you specify
 the IAM role that Amazon S3 can assume. You can do this only if the profile
 that you use has the `iam:PassRole` permission. For more
 information, see [Grant a user
 permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html") in the
 *IAM User Guide*. If you use administrator
 credentials to create a named profile, you can perform all the tasks.
2. Create a source bucket and enable versioning on it by using the following
 AWS CLI commands. To use these commands, replace the ``user
 input placeholders`` with your own information. 


The following `create-bucket` command creates a source bucket
 named ``amzn-s3-demo-source-bucket`` in the US East (N. Virginia)
 (`us-east-1`) Region:




```
aws s3api create-bucket \
--bucket `amzn-s3-demo-source-bucket` \
--region `us-east-1` \
--profile `acctA`
```

The following `put-bucket-versioning` command enables S3 Versioning on the
 ``amzn-s3-demo-source-bucket`` bucket: 



```
aws s3api put-bucket-versioning \
--bucket `amzn-s3-demo-source-bucket` \
--versioning-configuration Status=Enabled \
--profile `acctA`
```
3. Create a destination bucket and enable versioning on it by using the
 following AWS CLI commands. To use these commands, replace the
 ``user input placeholders`` with
 your own information. 


###### Note

To set up a replication configuration when both source and destination
 buckets are in the same AWS account, you use the same profile for the
 source and destination buckets. This example uses `acctA`. 

To test a replication configuration when the buckets are owned by
 different AWS accounts, specify different profiles for each account.
 For example, use an `acctB` profile for the destination
 bucket.



The following `create-bucket` command creates a destination
 bucket named ``amzn-s3-demo-destination-bucket`` in the
 US West (Oregon) (`us-west-2`) Region:



```
aws s3api create-bucket \
--bucket `amzn-s3-demo-destination-bucket` \
--region `us-west-2` \
--create-bucket-configuration LocationConstraint=`us-west-2` \
--profile `acctA`
```

The following `put-bucket-versioning` command enables
 S3 Versioning on the ``amzn-s3-demo-destination-bucket`` bucket: 



```
aws s3api put-bucket-versioning \
--bucket `amzn-s3-demo-destination-bucket` \
--versioning-configuration Status=Enabled \
--profile `acctA`
```
4. Create an IAM role. You specify this role in the replication
 configuration that you add to the source bucket later. Amazon S3 assumes this
 role to replicate objects on your behalf. You create an IAM role in two
 steps:




	* Create a role.
	* Attach a permissions policy to the role.
	1. Create the IAM role.
	
	
		1. Copy the following trust policy and save it to a file
		 named `s3-role-trust-policy.json` in the
		 current directory on your local computer. This policy grants
		 the Amazon S3 service principal permissions to assume the
		 role.
		
		
		
		JSON
		
		
		
		
		
		```
		`{
		 "Version":"2012-10-17", 
		 "Statement":[
		 {
		 "Effect":"Allow",
		 "Principal":{
		 "Service":"s3.amazonaws.com"
		 },
		 "Action":"sts:AssumeRole"
		 }
		 ]
		}`
		
		```
		2. Run the following command to create a role.
		
		
		
		```
		`$` aws iam create-role \
		--role-name `replicationRole` \
		--assume-role-policy-document file://`s3-role-trust-policy.json`  \
		--profile `acctA`
		```
	2. Attach a permissions policy to the role.
	
	
		1. Copy the following permissions policy and save it to a
		 file named `s3-role-permissions-policy.json` in
		 the current directory on your local computer. This policy
		 grants permissions for various Amazon S3 bucket and object
		 actions. 
		
		
		
		JSON
		
		
		
		
		
		```
		`{
		 "Version":"2012-10-17", 
		 "Statement":[
		 {
		 "Effect":"Allow",
		 "Action":[
		 "s3:GetObjectVersionForReplication",
		 "s3:GetObjectVersionAcl",
		 "s3:GetObjectVersionTagging"
		 ],
		 "Resource":[
		 "arn:aws:s3:::amzn-s3-demo-source-bucket/*"
		 ]
		 },
		 {
		 "Effect":"Allow",
		 "Action":[
		 "s3:ListBucket",
		 "s3:GetReplicationConfiguration"
		 ],
		 "Resource":[
		 "arn:aws:s3:::amzn-s3-demo-source-bucket"
		 ]
		 },
		 {
		 "Effect":"Allow",
		 "Action":[
		 "s3:ReplicateObject",
		 "s3:ReplicateDelete",
		 "s3:ReplicateTags"
		 ],
		 "Resource":"arn:aws:s3:::amzn-s3-demo-destination-bucket/*"
		 }
		 ]
		}`
		
		```
		
		
		
		
		
		###### Note
		
		
		
			* If you want to replicate encrypted objects, you also must grant the necessary
			 AWS Key Management Service (AWS KMS) key permissions. For more information, see [Replicating encrypted objects (SSE-S3,
			 SSE-KMS, DSSE-KMS, SSE-C)](replication-config-for-kms-objects.md "replication-config-for-kms-objects.md").
			* To use Object Lock with replication, you must grant two additional
			 permissions on the source S3 bucket in the AWS Identity and Access Management (IAM) role that you use
			 to set up replication. The two additional permissions are
			 `s3:GetObjectRetention` and `s3:GetObjectLegalHold`.
			 If the role has an `s3:Get*` permission statement, that statement
			 satisfies the requirement. For more information, see [Using Object Lock with
			 S3 Replication](object-lock-managing.md#object-lock-managing-replication "object-lock-managing.md#object-lock-managing-replication").
		2. Run the following command to create a policy and attach it
		 to the role. Replace the ``user input
		 placeholders`` with your own
		 information.
		
		
		
		```
		`$` aws iam put-role-policy \
		--role-name `replicationRole` \
		--policy-document file://`s3-role-permissions-policy.json` \
		--policy-name `replicationRolePolicy` \
		--profile `acctA`
		```
5. Add a replication configuration to the source bucket. 


	1. Although the Amazon S3 API requires that you specify the replication
	 configuration as XML, the AWS CLI requires that you specify the
	 replication configuration as JSON. Save the following JSON in a file
	 called `replication.json` to the local directory on your
	 computer.
	
	
	
	```
	{
	  "Role": "`IAM-role-ARN`",
	  "Rules": [
	    {
	      "Status": "Enabled",
	      "Priority": 1,
	      "DeleteMarkerReplication": { "Status": "Disabled" },
	      "Filter" : { "Prefix": "`Tax`"},
	      "Destination": {
	        "Bucket": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`"
	      }
	    }
	  ]
	}
	```
	2. Update the JSON by replacing the values for the
	 ``amzn-s3-demo-destination-bucket`` and
	 ``IAM-role-ARN`` with
	 your own information. Save the changes.
	3. Run the following `put-bucket-replication` command to
	 add the replication configuration to your source bucket. Be sure to
	 provide the source bucket name:
	
	
	
	```
	`$` aws s3api put-bucket-replication \
	--replication-configuration file://`replication.json` \
	--bucket `amzn-s3-demo-source-bucket` \
	--profile `acctA`
	```To retrieve the replication configuration, use the
 `get-bucket-replication` command:



```
`$` aws s3api get-bucket-replication \
--bucket `amzn-s3-demo-source-bucket` \
--profile `acctA`
```
6. Test the setup in the Amazon S3 console, by doing the following steps:


	1. Sign in to the AWS Management Console and open the Amazon S3 console at
	 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
	2. In the left navigation pane, choose **Buckets**.
	 In the **General purpose buckets** list, choose the
	 source bucket.
	3. In the source bucket, create a folder named
	 ``Tax``.
	4. Add sample objects to the
	 ``Tax`` folder in
	 the source bucket. 
	
	
	###### Note
	
	The amount of time that it takes for Amazon S3 to replicate an
	 object depends on the size of the object. For information about
	 how to see the status of replication, see [Getting replication status information](replication-status.md "replication-status.md").
	
	
	In the destination bucket, verify the following:
	
	
	
	
		* That Amazon S3 replicated the objects.
		* That the objects are replicas. On the
		 **Properties** tab for your objects,
		 scroll down to the **Object management
		 overview** section. Under **Management
		 configurations**, see the value under
		 **Replication status**. Make sure that
		 this value is set to `REPLICA`.
		* That the replicas are owned by the source bucket account.
		 You can verify the object ownership on the
		 **Permissions** tab for your objects. 
		
		
		If the source and destination buckets are owned by
		 different accounts, you can add an optional configuration to
		 tell Amazon S3 to change the replica ownership to the destination
		 account. For an example, see [How to change the replica owner](replication-change-owner.md#replication-walkthrough-3 "replication-change-owner.md#replication-walkthrough-3").
Use the following code examples to add a replication configuration to a bucket
 with the AWS SDK for Java and AWS SDK for .NET, respectively.

###### Note


* If you want to replicate encrypted objects, you also must grant the necessary
 AWS Key Management Service (AWS KMS) key permissions. For more information, see [Replicating encrypted objects (SSE-S3,
 SSE-KMS, DSSE-KMS, SSE-C)](replication-config-for-kms-objects.md "replication-config-for-kms-objects.md").
* To use Object Lock with replication, you must grant two additional
 permissions on the source S3 bucket in the AWS Identity and Access Management (IAM) role that you use
 to set up replication. The two additional permissions are
 `s3:GetObjectRetention` and `s3:GetObjectLegalHold`.
 If the role has an `s3:Get*` permission statement, that statement
 satisfies the requirement. For more information, see [Using Object Lock with
 S3 Replication](object-lock-managing.md#object-lock-managing-replication "object-lock-managing.md#object-lock-managing-replication").

Java
To add a replication configuration to a bucket and then retrieve and verify the configuration using the AWS SDK for Java, you can use the S3Client to manage replication settings programmatically.


For examples of how to configure replication with the AWS SDK for Java, see [Set replication configuration on a bucket](../API/s3_example_s3_PutBucketReplication_section.md "../API/s3_example_s3_PutBucketReplication_section.md") in the *Amazon S3 API Reference*.



C#
The following AWS SDK for .NET code example adds a replication configuration
 to a bucket and then retrieves it. To use this code, provide the names
 for your buckets and the Amazon Resource Name (ARN) for your IAM role.
 For information about setting up and running the code examples, see
 [Getting Started with the AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-config.html "https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-config.html") in the
 *AWS SDK for .NET Developer Guide*. 



```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using System;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class CrossRegionReplicationTest
    {
        private const string sourceBucket = "*** source bucket ***";
        // Bucket ARN example - arn:aws:s3:::destinationbucket
        private const string destinationBucketArn = "*** destination bucket ARN ***";
        private const string roleArn = "*** IAM Role ARN ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint sourceBucketRegion = RegionEndpoint.USWest2;
        private static IAmazonS3 s3Client;
        public static void Main()
        {
            s3Client = new AmazonS3Client(sourceBucketRegion);
            EnableReplicationAsync().Wait();
        }
        static async Task EnableReplicationAsync()
        {
            try
            {
                ReplicationConfiguration replConfig = new ReplicationConfiguration
                {
                    Role = roleArn,
                    Rules =
                        {
                            new ReplicationRule
                            {
                                Prefix = "Tax",
                                Status = ReplicationRuleStatus.Enabled,
                                Destination = new ReplicationDestination
                                {
                                    BucketArn = destinationBucketArn
                                }
                            }
                        }
                };

                PutBucketReplicationRequest putRequest = new PutBucketReplicationRequest
                {
                    BucketName = sourceBucket,
                    Configuration = replConfig
                };

                PutBucketReplicationResponse putResponse = await s3Client.PutBucketReplicationAsync(putRequest);

                // Verify configuration by retrieving it.
                await RetrieveReplicationConfigurationAsync(s3Client);
            }
            catch (AmazonS3Exception e)
            {
                Console.WriteLine("Error encountered on server. Message:'{0}' when writing an object", e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unknown encountered on server. Message:'{0}' when writing an object", e.Message);
            }
        }
        private static async Task RetrieveReplicationConfigurationAsync(IAmazonS3 client)
        {
            // Retrieve the configuration.
            GetBucketReplicationRequest getRequest = new GetBucketReplicationRequest
            {
                BucketName = sourceBucket
            };
            GetBucketReplicationResponse getResponse = await client.GetBucketReplicationAsync(getRequest);
            // Print.
            Console.WriteLine("Printing replication configuration information...");
            Console.WriteLine("Role ARN: {0}", getResponse.Configuration.Role);
            foreach (var rule in getResponse.Configuration.Rules)
            {
                Console.WriteLine("ID: {0}", rule.Id);
                Console.WriteLine("Prefix: {0}", rule.Prefix);
                Console.WriteLine("Status: {0}", rule.Status);
            }
        }
    }
}

```
