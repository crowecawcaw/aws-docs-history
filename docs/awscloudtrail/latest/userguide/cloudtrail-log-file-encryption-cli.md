# Enabling and disabling encryption for CloudTrail log files, digest files and event data stores with the AWS CLI

This topic describes how to enable and disable SSE-KMS encryption for CloudTrail log files, digest files,
 and event data stores by using the AWS CLI. For background information, see 
 [Encrypting CloudTrail log files, digest files, and event data stores with AWS KMS keys (SSE-KMS)](encrypting-cloudtrail-log-files-with-aws-kms.md "encrypting-cloudtrail-log-files-with-aws-kms.md").

###### Topics

* [Enabling encryption for CloudTrail log files, digest files,
 and event data stores by using the AWS CLI](#cloudtrail-log-file-encryption-cli-enable "#cloudtrail-log-file-encryption-cli-enable")
* [Disabling encryption for log files and digest files by using the AWS CLI](#cloudtrail-log-file-encryption-cli-disable "#cloudtrail-log-file-encryption-cli-disable")

## Enabling encryption for CloudTrail log files, digest files,
 and event data stores by using the AWS CLI



* [Enable log file and digest file encryption for a
 trail](#log-encryption-trail "#log-encryption-trail")
* [Enable encryption for an event
 data store](#log-encryption-eds "#log-encryption-eds")


###### Enable encryption for log files and digest files for a trail

1. Create a key with the AWS CLI. The key that you create must be in the same
 Region as the S3 bucket that receives your CloudTrail log files. For this step, you
 use the AWS KMS [**create-key**](https://docs.aws.amazon.com/cli/latest/reference/kms/create-key.html "https://docs.aws.amazon.com/cli/latest/reference/kms/create-key.html") command.
2. Get the existing key policy so that you can modify it for use with CloudTrail. You
 can retrieve the key policy with the AWS KMS [**get-key-policy**](https://docs.aws.amazon.com/cli/latest/reference/kms/get-key-policy.html "https://docs.aws.amazon.com/cli/latest/reference/kms/get-key-policy.html")
 command.
3. Add required sections to the key policy so that CloudTrail can encrypt and users can
 decrypt your log files and digest files. Be sure that all users who read the log files are
 granted decrypt permissions. Do not change existing sections of the policy. For
 information about the policy sections to include, see [Configure AWS KMS key policies for CloudTrail](create-kms-key-policy-for-cloudtrail.md "create-kms-key-policy-for-cloudtrail.md").
4. Attach the modified JSON policy file to the key by using the AWS KMS [**put-key-policy**](https://docs.aws.amazon.com/cli/latest/reference/kms/put-key-policy.html "https://docs.aws.amazon.com/cli/latest/reference/kms/put-key-policy.html") command.
5. Run the CloudTrail `create-trail` or `update-trail` command
 with the `--kms-key-id` parameter. This command enables encryption of
 log files and digest files.



```
aws cloudtrail update-trail --name Default --kms-key-id alias/`MyKmsKey`
```

The `--kms-key-id` parameter specifies the key whose policy you
 modified for CloudTrail. It can be any one of the following formats: 




	* **Alias Name**. Example:
	 `alias/MyAliasName`
	* **Alias ARN**. Example:
	 `arn:aws:kms:us-east-2:123456789012:alias/MyAliasName`
	* **Key ARN**. Example:
	 `arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`
	* **Globally unique key ID.** Example:
	 `12345678-1234-1234-1234-123456789012`
The following is an example response:



```
{
    "IncludeGlobalServiceEvents": true, 
    "Name": "Default", 
    "TrailARN": "arn:aws:cloudtrail:us-east-2:`123456789012`:trail/Default", 
    "LogFileValidationEnabled": false,
    "KmsKeyId": "arn:aws:kms:us-east-2:`123456789012`:key/`12345678-1234-1234-1234-123456789012`", 
    "S3BucketName": "`amzn-s3-demo-bucket`"
}
```

The presence of the `KmsKeyId` element indicates that encryption for your log files has been enabled. If log file 
 validation has been enabled (indicated by the `LogFileValidationEnabled` element being set to true), 
 this also indicates that encryption has been enabled for your digest files. The encrypted log files and digest 
 files should appear in the S3 bucket configured for the trail within approximately 5 minutes.


###### Enable encryption for an event data store

1. Create a key with the AWS CLI. The key that you create must be in the same
 Region as the event data store. For this step, run the AWS KMS [**create-key**](https://docs.aws.amazon.com/cli/latest/reference/kms/create-key.html "https://docs.aws.amazon.com/cli/latest/reference/kms/create-key.html")
 command.
2. Get the existing key policy to edit for use with CloudTrail. You can get the key
 policy by running the AWS KMS [**get-key-policy**](https://docs.aws.amazon.com/cli/latest/reference/kms/get-key-policy.html "https://docs.aws.amazon.com/cli/latest/reference/kms/get-key-policy.html")
 command.
3. Add required sections to the key policy so that CloudTrail can encrypt and users can 
 decrypt your event data store. Be sure that all users who read the event 
 data store are granted decrypt permissions. Do not change existing sections of the policy. For
 information about the policy sections to include, see [Configure AWS KMS key policies for CloudTrail](create-kms-key-policy-for-cloudtrail.md "create-kms-key-policy-for-cloudtrail.md").
4. Attach the edited JSON policy file to the key by running the AWS KMS [put-key-policy](https://docs.aws.amazon.com/cli/latest/reference/kms/put-key-policy.html "https://docs.aws.amazon.com/cli/latest/reference/kms/put-key-policy.html")
 command.
5. Run the CloudTrail `create-event-data-store` or
 `update-event-data-store` command, and add the
 `--kms-key-id` parameter. This command enables encryption of the
 event data store.



```
aws cloudtrail update-event-data-store --name my-event-data-store --kms-key-id alias/`MyKmsKey`
```

The `--kms-key-id` parameter specifies the key whose policy you
 modified for CloudTrail. It can be any one of the following four formats: 




	* **Alias Name**. Example:
	 `alias/MyAliasName`
	* **Alias ARN**. Example:
	 `arn:aws:kms:us-east-2:123456789012:alias/MyAliasName`
	* **Key ARN**. Example:
	 `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`
	* **Globally unique key ID.** Example:
	 `12345678-1234-1234-1234-123456789012`
The following is an example response:



```
{
    "Name": "my-event-data-store",
    "ARN": "arn:aws:cloudtrail:us-east-1:12345678910:eventdatastore/EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE",
    "RetentionPeriod": "90",
    "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
    "MultiRegionEnabled": false,
    "OrganizationEnabled": false,
    "TerminationProtectionEnabled": true,
    "AdvancedEventSelectors": [{
        "Name": "Select all external events",
        "FieldSelectors": [{
            "Field": "eventCategory",
            "Equals": [
                "ActivityAuditLog"
            ]
        }]
    }]
}
```

The presence of the `KmsKeyId` element indicates 
 that encryption for event data store has been enabled.

## Disabling encryption for log files and digest files by using the AWS CLI


To stop encrypting log files and digest files for a trail, run `update-trail` and pass an empty
 string to the `kms-key-id` parameter: 



```
aws cloudtrail update-trail --name my-test-trail --kms-key-id ""
```

The following is an example response:



```
{
    "IncludeGlobalServiceEvents": true, 
    "Name": "Default", 
    "TrailARN": "arn:aws:cloudtrail:us-east-2:`123456789012`:trail/Default", 
    "LogFileValidationEnabled": false, 
    "S3BucketName": "`amzn-s3-demo-bucket`"
}
```

The absence of the `KmsKeyId` value indicates 
 that encryption for log files and digest files is no longer enabled.


###### Important

You cannot stop encryption for an event data store.
