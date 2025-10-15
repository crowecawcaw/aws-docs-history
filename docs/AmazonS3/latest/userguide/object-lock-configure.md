# Configuring S3 Object Lock

With Amazon S3 Object Lock, you can store objects in Amazon S3 general purpose buckets by using a
 *write-once-read-many* (WORM) model. You can use S3 Object Lock to
 prevent an object from being deleted or overwritten for a fixed amount of time or indefinitely.
 For general information about Object Lock capabilities, see [Locking objects with Object Lock](object-lock.md "object-lock.md").

Before you lock any objects, you must enable S3 Versioning and Object Lock on a general purpose bucket.
 Afterward, you can set a retention period, a legal hold, or both. 

To work with Object Lock, you must have certain permissions. For a list of the permissions
 related to various Object Lock operations, see [Required permissions](object-lock.md#object-lock-permissions "object-lock.md#object-lock-permissions").

###### Important


* After you enable Object Lock on a bucket, you can't disable Object Lock or suspend
 versioning for that bucket.
* S3 buckets with Object Lock can't be used as destination buckets for server access
 logs. For more information, see [Logging requests with server access logging](ServerLogs.md "ServerLogs.md").
###### Topics

* [Enable Object Lock when creating a new S3 general purpose
 bucket](#object-lock-configure-new-bucket "#object-lock-configure-new-bucket")
* [Enable Object Lock on an existing S3
 bucket](#object-lock-configure-existing-bucket "#object-lock-configure-existing-bucket")
* [Set or modify a legal hold on an S3
 object](#object-lock-configure-set-legal-hold "#object-lock-configure-set-legal-hold")
* [Set or modify a retention
 period on an S3 object](#object-lock-configure-set-retention-period-object "#object-lock-configure-set-retention-period-object")
* [Set or modify a default
 retention period on an S3 bucket](#object-lock-configure-set-retention-period-bucket "#object-lock-configure-set-retention-period-bucket")

## Enable Object Lock when creating a new S3 general purpose
 bucket


You can enable Object Lock when creating a new S3 general purpose bucket by using the Amazon S3 console,
 AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3 REST API.


1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. Choose **Create bucket**.


The **Create bucket** page opens.
4. For **Bucket name**, enter a name for your bucket.


###### Note

After you create a bucket, you can't change its name. For more information about
 naming buckets, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md").
5. For **Region**, choose the AWS Region where you want the bucket
 to reside.
6. Under **Object Ownership**, choose to disable or enable access
 control lists (ACLs) and control ownership of objects uploaded in your bucket.
7. Under **Block Public Access settings for this bucket**, choose
 the Block Public Access settings that you want to apply to the bucket.
8. Under **Bucket Versioning**, choose
 **Enabled**.


Object Lock works only with versioned buckets.
9. (Optional) Under **Tags**, you can choose to add tags to your
 bucket. Tags are key-value pairs that are used to categorize storage and allocate
 costs.
10. Under **Advanced settings**, find
 **Object Lock** and choose **Enable**.


You must acknowledge that enabling Object Lock will permanently allow objects in
 this bucket to be locked.
11. Choose **Create bucket**.
The following `create-bucket` example creates a new S3 bucket named
 ``amzn-s3-demo-bucket1`` with Object Lock enabled:


```
aws s3api create-bucket --bucket ``amzn-s3-demo-bucket1`` --object-lock-enabled-for-bucket
```
For more information and examples, see [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html") in the
 *AWS CLI Command Reference*.

###### Note

You can run AWS CLI commands from the console by using AWS CloudShell.
 AWS CloudShell is a browser-based, pre-authenticated shell that you can launch
 directly from the AWS Management Console. For more information, see [What is CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html") in the
 *AWS CloudShell User Guide*.

You can use the REST API to create a new S3 bucket with Object Lock enabled. For more
 information, see [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md") in
 the *Amazon Simple Storage Service API Reference*.

For examples of how to enable Object Lock when creating a new S3 bucket with the AWS SDKs, see [Code examples](../API/s3_example_s3_LCreateBucket_section.md "../API/s3_example_s3_LCreateBucket_section.md") in the *Amazon S3 API Reference*.

For examples of how to get the current Object Lock configuration with the AWS SDKs, see [Code examples](../API/s3_example_s3_GetObjectLockConfiguration_section.md "../API/s3_example_s3_GetObjectLockConfiguration_section.md") in the *Amazon S3 API Reference*.

For an interactive scenario demonstrating different Object Lock features using the AWS SDKs, see [Code examples](../API/s3_example_s3_Scenario_ObjectLock_section.md "../API/s3_example_s3_Scenario_ObjectLock_section.md") in the *Amazon S3 API Reference*.

For general information about using different AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](../API/sdk-general-information-section.md "../API/sdk-general-information-section.md") in the *Amazon S3 API Reference*.


## Enable Object Lock on an existing S3
 bucket


You can enable Object Lock for an existing S3 bucket by using the Amazon S3 console, the AWS CLI, AWS SDKs, or Amazon S3 REST API.


###### Note

Object Lock works only with versioned buckets.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, choose the name of the bucket that you
 want to enable Object Lock on.
4. Choose the **Properties** tab.
5. Under **Properties**, scroll down to the **Object
 Lock** section, and choose **Edit**.
6. Under **Object Lock**, choose **Enable**.


You must acknowledge that enabling Object Lock will permanently allow objects in
 this bucket to be locked.
7. Choose **Save changes**.
The following `put-object-lock-configuration` example command sets a 50-day
 Object Lock retention period on a bucket named ``amzn-s3-demo-bucket1``:


```
aws s3api put-object-lock-configuration --bucket ``amzn-s3-demo-bucket1`` --object-lock-configuration=`'{ "ObjectLockEnabled": "Enabled", "Rule": { "DefaultRetention": { "Mode": "COMPLIANCE", "Days": 50 }}}'`
```
For more information and examples, see [put-object-lock-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-lock-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-lock-configuration.html") in the
 *AWS CLI Command Reference*.

###### Note

You can run AWS CLI commands from the console by using AWS CloudShell.
 AWS CloudShell is a browser-based, pre-authenticated shell that you can launch
 directly from the AWS Management Console. For more information, see [What is CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html") in the
 *AWS CloudShell User Guide*.

You can use the Amazon S3 REST API to enable Object Lock on an existing S3 bucket. For
 more information, see [PutObjectLockConfiguration](../API/API_PutObjectLockConfiguration.md "../API/API_PutObjectLockConfiguration.md") in the
 *Amazon Simple Storage Service API Reference*.

For examples of how to enable Object Lock for an existing S3 bucket with the AWS SDKs, see [Code examples](../API/s3_example_s3_PutObjectLockConfiguration_section.md "../API/s3_example_s3_PutObjectLockConfiguration_section.md") in the *Amazon S3 API Reference*.

For examples of how to get the current Object Lock configuration with the AWS SDKs, see [Code examples](../API/s3_example_s3_GetObjectLockConfiguration_section.md "../API/s3_example_s3_GetObjectLockConfiguration_section.md") in the *Amazon S3 API Reference*.

For an interactive scenario demonstrating different Object Lock features using the AWS SDKs, see [Code examples](../API/s3_example_s3_Scenario_ObjectLock_section.md "../API/s3_example_s3_Scenario_ObjectLock_section.md") in the *Amazon S3 API Reference*.

For general information about using different AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](../API/sdk-general-information-section.md "../API/sdk-general-information-section.md") in the *Amazon S3 API Reference*.


## Set or modify a legal hold on an S3
 object


You can set or remove a legal hold on an S3 object by using the Amazon S3 console, AWS CLI, AWS
 SDKs, or Amazon S3 REST API.


###### Important


* If you want to set a legal hold on an object, the object's bucket must already have
 Object Lock enabled.
* When you `PUT` an object version that has an explicit individual
 retention mode and period in a bucket, the object version's individual Object Lock
 settings override any bucket property retention settings.

For more information, see [Legal holds](object-lock.md#object-lock-legal-holds "object-lock.md#object-lock-legal-holds").


1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, choose the name of the bucket that
 contains the object that you want to set or modify a legal hold on.
4. In the **Objects** list, select the object that you want to set
 or modify a legal hold on.
5. On the **Object properties** page, find the **Object Lock
 legal hold** section, and choose **Edit**.
6. Choose **Enable** to set a legal hold or
 **Disable** to remove a legal hold.
7. Choose **Save changes**.
The following `put-object-legal-hold` example sets a legal hold on the
 object ``my-image.fs`` in the bucket
 named ``amzn-s3-demo-bucket1``:


```
aws s3api put-object-legal-hold --bucket ``amzn-s3-demo-bucket1`` --key `my-image.fs` --legal-hold="Status=ON"
```
The following `put-object-legal-hold` example removes a legal hold on the
 object ``my-image.fs`` in the bucket
 named ``amzn-s3-demo-bucket1``:


```
aws s3api put-object-legal-hold --bucket ``amzn-s3-demo-bucket1`` --key `my-image.fs` --legal-hold="Status=OFF"
```
For more information and examples, see [put-object-legal-hold](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-legal-hold.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-legal-hold.html") in the
 *AWS CLI Command Reference*.

###### Note

You can run AWS CLI commands from the console by using AWS CloudShell.
 AWS CloudShell is a browser-based, pre-authenticated shell that you can launch
 directly from the AWS Management Console. For more information, see [What is CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html") in the
 *AWS CloudShell User Guide*.

You can use the REST API to set or modify a legal hold on an object. For more
 information, see [PutObjectLegalHold](../API/API_PutObjectLegalHold.md "../API/API_PutObjectLegalHold.md") in the
 *Amazon Simple Storage Service API Reference*.

For examples of how to set a legal hold on an object with the AWS SDKs, see [Code examples](../API/s3_example_s3_PutObjectLegalHold_section.md "../API/s3_example_s3_PutObjectLegalHold_section.md") in the *Amazon S3 API Reference*.

For examples of how to get the current legal hold status with the AWS SDKs, see [Code examples](../API/s3_example_s3_GetObjectLegalHoldConfiguration_section.md "../API/s3_example_s3_GetObjectLegalHoldConfiguration_section.md") in the *Amazon S3 API Reference*.

For an interactive scenario demonstrating different Object Lock features using the AWS SDKs, see [Code examples](../API/s3_example_s3_Scenario_ObjectLock_section.md "../API/s3_example_s3_Scenario_ObjectLock_section.md") in the *Amazon S3 API Reference*.

For general information about using different AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](../API/sdk-general-information-section.md "../API/sdk-general-information-section.md") in the *Amazon S3 API Reference*.


## Set or modify a retention
 period on an S3 object


You can set or modify a retention period on an S3 object by using the Amazon S3 console, AWS CLI,
 AWS SDKs, or Amazon S3 REST API.


###### Important


* If you want to set a retention period on an object, the object's bucket must already
 have Object Lock enabled.
* When you `PUT` an object version that has an explicit individual
 retention mode and period in a bucket, the object version's individual Object Lock
 settings override any bucket property retention settings.
* The only way to delete an object under the compliance mode before its retention date expires is to delete the associated AWS account.

For more information, see [Retention periods](object-lock.md#object-lock-retention-periods "object-lock.md#object-lock-retention-periods").


1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, choose the name of the bucket that
 contains the object that you want to set or modify a retention period on.
4. In the **Objects** list, select the object that you want to set
 or modify a retention period on.
5. On the **Object properties** page, find the **Object Lock
 retention** section, and choose **Edit**.
6. Under **Retention**, choose **Enable** to set a
 retention period or **Disable** to remove a retention period.
7. If you chose **Enable**, under **Retention
 mode**, choose either **Governance mode** or
 **Compliance mode**. For more information, see [Retention modes](object-lock.md#object-lock-retention-modes "object-lock.md#object-lock-retention-modes").
8. Under **Retain until date**, choose the date that you want to
 have the retention period end on. During this period, your object is WORM-protected
 and can't be overwritten or deleted. For more information, see [Retention periods](object-lock.md#object-lock-retention-periods "object-lock.md#object-lock-retention-periods").
9. Choose **Save changes**.
The following `put-object-retention` example sets a retention period on the
 object ``my-image.fs`` in the bucket
 named ``amzn-s3-demo-bucket1`` until January 1, 2025:


```
aws s3api put-object-retention --bucket ``amzn-s3-demo-bucket1`` --key `my-image.fs` --retention='{ "Mode": "GOVERNANCE", "RetainUntilDate": "2025-01-01T00:00:00" }'
```
For more information and examples, see [put-object-retention](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-retention.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-retention.html") in the
 *AWS CLI Command Reference*.

###### Note

You can run AWS CLI commands from the console by using AWS CloudShell.
 AWS CloudShell is a browser-based, pre-authenticated shell that you can launch
 directly from the AWS Management Console. For more information, see [What is CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html") in the
 *AWS CloudShell User Guide*.

You can use the REST API to set a retention period on an object. For more information,
 see [PutObjectRetention](../API/API_PutObjectRetention.md "../API/API_PutObjectRetention.md") in the
 *Amazon Simple Storage Service API Reference*.

For examples of how to set a retention period on an object with the AWS SDKs, see [Code examples](../API/s3_example_s3_PutObjectRetention_section.md "../API/s3_example_s3_PutObjectRetention_section.md") in the *Amazon S3 API Reference*.

For examples of how to get the retention period on an object with the AWS SDKs, see [Code examples](../API/s3_example_s3_GetObjectLockConfiguration_section.md "../API/s3_example_s3_GetObjectLockConfiguration_section.md") in the *Amazon S3 API Reference*.

For an interactive scenario demonstrating different Object Lock features using the AWS SDKs, see [Code examples](../API/s3_example_s3_GetObjectLockConfiguration_section.md "../API/s3_example_s3_GetObjectLockConfiguration_section.md") in the *Amazon S3 API Reference*.

For general information about using different AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](../API/sdk-general-information-section.md "../API/sdk-general-information-section.md") in the *Amazon S3 API Reference*.


## Set or modify a default
 retention period on an S3 bucket


You can set or modify a default retention period on an S3 bucket by using the Amazon S3
 console, AWS CLI, AWS SDKs, or Amazon S3 REST API. You specify a duration, in either days or years,
 for how long to protect every object version placed in the bucket.


###### Important


* If you want to set a default retention period on a bucket, the bucket must already
 have Object Lock enabled.
* When you `PUT` an object version that has an explicit individual
 retention mode and period in a bucket, the object version's individual Object Lock
 settings override any bucket property retention settings.
* The only way to delete an object under the compliance mode before its retention date expires is to delete the associated AWS account.

For more information, see [Retention periods](object-lock.md#object-lock-retention-periods "object-lock.md#object-lock-retention-periods").


1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, choose the name of the bucket that you
 want to set or modify a default retention period on.
4. Choose the **Properties** tab.
5. Under **Properties**, scroll down to the **Object
 Lock** section, and choose **Edit**.
6. Under **Default retention**, choose **Enable**
 to set a default retention or **Disable** to remove a default
 retention.
7. If you chose **Enable**, under **Retention
 mode**, choose either **Governance mode** or
 **Compliance mode**. For more information, see [Retention modes](object-lock.md#object-lock-retention-modes "object-lock.md#object-lock-retention-modes").
8. Under **Default retention period**, choose the number of days or
 years that you want the retention period to last for. Objects placed in this bucket
 will be locked for this number of days or years. For more information, see [Retention periods](object-lock.md#object-lock-retention-periods "object-lock.md#object-lock-retention-periods").
9. Choose **Save changes**.
The following `put-object-lock-configuration` example command sets a 50-day
 Object Lock retention period on the bucket named ``amzn-s3-demo-bucket1`` by
 using compliance mode:


```
aws s3api put-object-lock-configuration --bucket ``amzn-s3-demo-bucket1`` --object-lock-configuration=`'{ "ObjectLockEnabled": "Enabled", "Rule": { "DefaultRetention": { "Mode": "COMPLIANCE", "Days": 50 }}}'`
```
The following `put-object-lock-configuration` example removes the default
 retention configuration on a bucket:


```
aws s3api put-object-lock-configuration --bucket ``amzn-s3-demo-bucket1`` --object-lock-configuration=`'{ "ObjectLockEnabled": "Enabled"}'`
```
For more information and examples, see [put-object-lock-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-lock-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-lock-configuration.html") in the
 *AWS CLI Command Reference*.

###### Note

You can run AWS CLI commands from the console by using AWS CloudShell.
 AWS CloudShell is a browser-based, pre-authenticated shell that you can launch
 directly from the AWS Management Console. For more information, see [What is CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html") in the
 *AWS CloudShell User Guide*.

You can use the REST API to set a default retention period on an existing S3 bucket.
 For more information, see [PutObjectLockConfiguration](../API/API_PutObjectLockConfiguration.md "../API/API_PutObjectLockConfiguration.md") in the
 *Amazon Simple Storage Service API Reference*.

For examples of how to set a default retention period on an existing S3 bucket with the AWS SDKs, see [Code examples](../API/s3_example_s3_PutObjectLockConfiguration_section.md "../API/s3_example_s3_PutObjectLockConfiguration_section.md") in the *Amazon S3 API Reference*.

For an interactive scenario demonstrating different Object Lock features using the AWS SDKs, see [Code examples](../API/s3_example_s3_Scenario_ObjectLock_section.md "../API/s3_example_s3_Scenario_ObjectLock_section.md") in the *Amazon S3 API Reference*.

For general information about using different AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](../API/sdk-general-information-section.md "../API/sdk-general-information-section.md") in the *Amazon S3 API Reference*.
