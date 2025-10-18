# Encrypting CloudTrail log files, digest files, and event data stores with AWS KMS keys (SSE-KMS)

By default, the log files and digest files delivered by CloudTrail to your bucket are encrypted by using 
 [server-side encryption with
 a KMS key (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html"). If you don't enable SSE-KMS encryption, your log files and digest files are encrypted 
 using [SSE-S3 encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html").

###### Note

If you're using an existing S3 bucket with an [S3 bucket Key](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html"),
 CloudTrail must be allowed permission in the key policy to use the AWS KMS actions
 `GenerateDataKey` and `DescribeKey`. If
 `cloudtrail.amazonaws.com` is not granted those permissions in the key policy,
 you cannot create or update a trail.

To use SSE-KMS with CloudTrail, you create and manage a [AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html"). You attach a policy to the
 key that determines which users can use the key for encrypting and decrypting CloudTrail log files and digest files.
 The decryption is seamless through S3. When authorized users of the key read CloudTrail log files or digest files, 
 S3 manages the decryption, and the authorized users are able to read the files in unencrypted form.

This approach has the following advantages:


* You can create and manage the KMS key yourself.
* You can use a single KMS key to encrypt and decrypt log files and digest files for multiple accounts across
 all Regions.
* You have control over who can use your key for encrypting and decrypting CloudTrail log files and digest files.
 You can assign permissions for the key to the users in your organization according to your
 requirements.
* You have enhanced security. With this feature, to read log files or digest files, the following
 permissions are required:



	+ A user must have S3 read permissions for the bucket that contains the log files and digest files.
	+ A user must also have a policy or role applied that allows decrypt permissions by the KMS key
	 policy.
* Because S3 automatically decrypts the log files and digest files for requests from users authorized to
 use the KMS key, SSE-KMS encryption for the files is backward-compatible with applications
 that read CloudTrail log data.
###### Note

The KMS key that you choose must be created in the same AWS Region as the Amazon S3 bucket that
 receives your log files and digest files. For example, if the log files and digest files will be stored in a bucket in the
 US East (Ohio) Region, you must create or choose a KMS key that was created in that Region. To
 verify the Region for an Amazon S3 bucket, inspect its properties in the Amazon S3 console.

By default, event data stores are encrypted by CloudTrail. You have the option to use your own KMS key 
 for encryption when you create or update an event data store.


## Enabling log file encryption


###### Note

If you create a KMS key in the CloudTrail console, CloudTrail adds the required KMS key policy sections for
 you. Follow these procedures if you created a key in the IAM console or AWS CLI and you need
 to manually add the required policy sections.


To enable SSE-KMS encryption for CloudTrail log files, perform the following high-level
 steps:


1. Create a KMS key.




	* For information about creating a KMS key with the AWS Management Console, see [Creating Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html "https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html") in the
	 *AWS Key Management Service Developer Guide*.
	* For information about creating a KMS key with the AWS CLI, see [create-key](https://docs.aws.amazon.com/cli/latest/reference/kms/create-key.html "https://docs.aws.amazon.com/cli/latest/reference/kms/create-key.html").
###### Note

The KMS key that you choose must be in the same Region as the S3 bucket that receives
 your log files and digest files. To verify the Region for an S3 bucket, inspect the bucket's properties
 in the S3 console.
2. Add policy sections to the key that enable CloudTrail to encrypt and users to decrypt log
 files and digest files. 




	* For information about what to include in the policy, see [Configure AWS KMS key policies for CloudTrail](create-kms-key-policy-for-cloudtrail.md "create-kms-key-policy-for-cloudtrail.md").
	
	
	###### Warning
	
	Be sure to include decrypt permissions in the policy for all users who need to
	 read log files or digest files. If you do not perform this step before adding the key to your trail
	 configuration, users without decrypt permissions cannot read encrypted files until
	 you grant them those permissions.
	* For information about editing a policy with the IAM console, see [Editing a Key Policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-editing "https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-editing")
	 in the *AWS Key Management Service Developer Guide*.
	* For information about attaching a policy to a KMS key with the AWS CLI, see [put-key-policy](https://docs.aws.amazon.com/cli/latest/reference/kms/put-key-policy.html "https://docs.aws.amazon.com/cli/latest/reference/kms/put-key-policy.html").
3. Update your trail or event data store to use the KMS key whose policy you modified for CloudTrail.




	* To update a trail or event data store using the CloudTrail console, see [Updating a resource to
	 use your KMS key with the console](create-kms-key-policy-for-cloudtrail-update-trail.md "create-kms-key-policy-for-cloudtrail-update-trail.md").
	* To update a trail or event data store using the AWS CLI, see [Enabling and disabling encryption for CloudTrail log files, digest files and event data stores with the AWS CLI](cloudtrail-log-file-encryption-cli.md "cloudtrail-log-file-encryption-cli.md").

CloudTrail also supports AWS KMS multi-Region keys. For more information about multi-Region keys,
 see [Using multi-Region
 keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html "https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html") in the *AWS Key Management Service Developer Guide*.


The next section describes the policy sections that your KMS key policy requires for use with
 CloudTrail.
