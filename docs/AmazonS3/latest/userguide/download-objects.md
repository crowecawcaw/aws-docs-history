# Downloading objects

This section explains how to download objects from an Amazon S3 bucket. With Amazon S3, you can store
 objects in one or more buckets, and each single object can be up to 5 TB in size. Any Amazon S3
 object that is not archived is accessible in real time. Archived objects, however, must be
 restored before they can be downloaded. For information about downloading archived objects, see
 [Downloading archived objects](#download-archived-objects "#download-archived-objects").

You can download a single object by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), AWS SDKs,
 or Amazon S3 REST API. To download an object from S3 without writing any code or running any
 commands, use the S3 console. For more information, see [Downloading an object](#download-an-object "#download-an-object").

To download multiple objects, use AWS CloudShell, the AWS CLI, or the AWS SDKs. For more
 information, see [Downloading multiple objects](#download-multiple-objects "#download-multiple-objects").

If you need to download part of an object, you use extra parameters with the AWS CLI or REST
 API to specify only the bytes that you want to download. For more information, see [Downloading part of an object](#download-objects-parts "#download-objects-parts").

If you need to download an object that you don't own, ask the object owner to generate a
 presigned URL that allows you to download the object. For more information, see [Downloading an object from another
 AWS account](#download-objects-from-another-account "#download-objects-from-another-account").

When you download objects outside of the AWS network, data-transfer fees apply. Data
 transfer within the AWS network is free within the same AWS Region, but you will be charged
 for any `GET` requests. For more information about data-transfer costs and
 data-retrieval charges, see [Amazon S3
 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### Topics

* [Downloading an object](#download-an-object "#download-an-object")
* [Downloading multiple objects](#download-multiple-objects "#download-multiple-objects")
* [Downloading part of an object](#download-objects-parts "#download-objects-parts")
* [Downloading an object from another
 AWS account](#download-objects-from-another-account "#download-objects-from-another-account")
* [Downloading archived objects](#download-archived-objects "#download-archived-objects")
* [Downloading objects based on metadata](#download-objects-based-on-metadata "#download-objects-based-on-metadata")
* [Troubleshooting downloading objects](#download-objects-troubleshooting "#download-objects-troubleshooting")

## Downloading an object


You can download an object by using the Amazon S3 console, AWS CLI, AWS SDKs, or REST
 API.


This section explains how to use the Amazon S3 console to download an object from an S3
 bucket.

###### Note


* You can download only one object at a time.
* If you use the Amazon S3 console to download an object whose key name ends with a
 period (`.`), the period is removed from the key name of the
 downloaded object. To retain the period at the end of the name of the downloaded
 object, you must use the AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3 REST API.
###### To download an object from an S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets** or **Directory buckets**.
3. In the buckets list, choose the name of the bucket that you
 want to download an object from.
4. You can download an object from an S3 bucket in any of the following ways:




	* Select the check box next to the object, and choose
	 **Download**. If you want to download the object to a
	 specific folder, on the **Actions** menu, choose
	 **Download as**.
	* If you want to download a specific version of the object, turn on
	 **Show versions** (located next to the search box).
	 Select the check box next to the version of the object that you want, and
	 choose **Download**. If you want to download the object to
	 a specific folder, on the **Actions** menu, choose
	 **Download as**.
The following `get-object` example command shows how you can use the AWS CLI
 to download an object from Amazon S3. This command gets the object
 ``folder/my_image`` from the bucket
 ``amzn-s3-demo-bucket1``. You must include an `outfile`, which is a file name for the downloaded object, such as 
 ``my_downloaded_image.jpg``.


```
aws s3api get-object --bucket ``amzn-s3-demo-bucket1`` --key `folder/my_image` `my_downloaded_image.jpg`
```
For more information and examples, see [get-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html") in the *AWS CLI Command Reference*.

For examples of how to download an object with the AWS SDKs, see [Code examples](../API/s3_example_s3_GetObjectLockConfiguration_section.md "../API/s3_example_s3_GetObjectLockConfiguration_section.md") in the *Amazon S3 API Reference*.

For general information about using different AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](../API/sdk-general-information-section.md "../API/sdk-general-information-section.md") in the *Amazon S3 API Reference*.

You can use the REST API to retrieve objects from Amazon S3. For more information, see [GetObject](../API/API_GetObject.md "../API/API_GetObject.md") in the *Amazon Simple Storage Service API Reference*.


## Downloading multiple objects


You can download multiple objects by using AWS CloudShell, the AWS CLI, or the AWS SDKs. 


AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from
 the AWS Management Console.

For more information about AWS CloudShell, see [What is CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html") in the
 *AWS CloudShell User Guide*.

###### Important

With AWS CloudShell, your home directory has storage up to 1GB per AWS Region.
 Therefore you cannot sync buckets with objects totaling over this amount. For more limitations, see [Service quotas and restrictions](https://docs.aws.amazon.com/cloudshell/latest/userguide/limits.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/limits.html") in the
 *AWS CloudShell User Guide*.

###### To download objects by using AWS CloudShell

1. Sign in to the AWS Management Console and open the CloudShell console at [https://console.aws.amazon.com/cloudshell/](https://console.aws.amazon.com/cloudshell/ "https://console.aws.amazon.com/cloudshell/").
2. Run the following command to sync objects in your bucket to CloudShell. The
 following command syncs objects from the bucket named ``amzn-s3-demo-bucket1``
 and creates a folder named ``temp`` in
 CloudShell. CloudShell syncs your objects to this folder. To use this command,
 replace the ``user input placeholders`` with your
 own information.



```
aws s3 sync s3://`amzn-s3-demo-bucket1` ./`temp`
```

###### Note

The `sync` command is not compatible with directory buckets.

To perform pattern matching to either exclude or include particular objects, you
 can use the `--exclude "`value`"` and
 `--include "`value`"` parameters with the
 `sync` command.
3. Run the following command to zip your objects in the folder named
 ``temp`` to a file named
 ``temp.zip``.



```
zip `temp.zip` -r `temp`/
```
4. Choose **Actions**, and then choose **Download
 file**.
5. Enter the file name ``temp.zip`` and then
 choose **Download**.
6. (Optional) Delete the ``temp.zip``
 file and the objects that are synced to the
 ``temp`` folder in CloudShell. With
 AWS CloudShell, you have persistent storage of up to 1 GB for each AWS Region. 


You can use the following example command to delete your `.zip`
 file and your folder. To use this example command, replace the ``user
 input placeholders`` with your own information. 



```
rm `temp.zip` && rm -rf `temp`/
```
The following example shows how you can use the AWS CLI to download all of the files or
 objects under the specified directory or prefix. This command copies all objects from the
 bucket ``amzn-s3-demo-bucket1`` to your current directory. To use this example
 command, use your bucket name in place of ``amzn-s3-demo-bucket1``. 


```
aws s3 cp s3://`amzn-s3-demo-bucket1` . --recursive
```
The following command downloads all of the objects under the prefix
 ``logs`` in the bucket
 ``amzn-s3-demo-bucket1`` to your current directory. It also uses the
 `--exclude` and `--include` parameters to copy only objects with
 the suffix ``.log``. To use this example
 command, replace the ``user input placeholders`` with
 your own information.


```
aws s3 cp s3://`amzn-s3-demo-bucket1`/`logs`/ . --recursive --exclude "`*`" --include "`*.log`"
```
For more information and examples, see [cp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html") in the *AWS CLI Command Reference*.

For examples of how to download all objects in an Amazon S3 bucket with the AWS SDKs, see
 [Code examples](../API/s3_example_s3_DownloadBucketToDirectory_section.md "../API/s3_example_s3_DownloadBucketToDirectory_section.md") in the *Amazon S3 API Reference*.

For general information about using different AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](../API/sdk-general-information-section.md "../API/sdk-general-information-section.md") in the *Amazon S3 API Reference*.


## Downloading part of an object


You can download part of an object by using the AWS CLI or REST API. To do so, you use
 additional parameters to specify which part of an object that you want to download.


The following example command performs a `GET` request for a range of bytes
 in the object named ``folder/my_data`` in the
 bucket named ``amzn-s3-demo-bucket1``. In the request, the byte range must be
 prefixed with `bytes=`. The partial object is downloaded to the output file
 named ``my_data_range``. To use this example
 command, replace the ``user input placeholders`` with
 your own information.


```
aws s3api get-object --bucket `amzn-s3-demo-bucket1` --key `folder/my_data` --range bytes=`0-500` `my_data_range`
```
For more information and examples, see [get-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html") in the *AWS CLI Command Reference*.

For more information about the HTTP `Range` header, see [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-range "https://www.rfc-editor.org/rfc/rfc9110.html#name-range") on the RFC
 Editor website.

###### Note

Amazon S3 doesn't support retrieving multiple ranges of data in a single `GET`
 request.

You can use the `partNumber` and `Range` parameters in the REST
 API to retrieve object parts from Amazon S3. For more information, see [GetObject](../API/API_GetObject.md "../API/API_GetObject.md") in the *Amazon Simple Storage Service API Reference*.


## Downloading an object from another
 AWS account


You can use a presigned URL to grant others time-limited access to your objects without
 updating your bucket policy.


The presigned URL can be entered in a browser or used by a program to download an object. The
 credentials used by the URL are those of the AWS user who generated the URL. After the URL
 is created, anyone with the presigned URL can download the corresponding object until the URL
 expires.


You can use the Amazon S3 console to generate a presigned URL for sharing an object in a general purpose bucket by
 following these steps. When using the console, the maximum expiration time for a presigned URL
 is 12 hours from the time of creation.

###### To generate a presigned URL by using the Amazon S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket that
 contains the object that you want a presigned URL for.
4. In the **Objects** list, select the object that you want to
 create a presigned URL for.
5. On the **Object actions** menu, choose **Share with a
 presigned URL**.
6. Specify how long you want the presigned URL to be valid.
7. Choose **Create presigned URL**.
8. When a confirmation message appears, the URL is automatically copied to your
 clipboard. You will see a button to copy the presigned URL if you need to copy it
 again.
9. To download the object, paste the URL into any browser, and the object will
 attempt to download.
For more information about presigned URLs and other methods for creating them, see [Download and upload objects with presigned
 URLs](using-presigned-url.md "using-presigned-url.md").


## Downloading archived objects


To reduce your storage costs for infrequently accessed objects, you can *archive* those objects. When you archive an object, it is moved into
 low-cost storage, which means that you can't access it in real time. To download an archived
 object, you must first restore it. 


You can restore archived objects in minutes or hours, depending on the storage class. You
 can restore an archived object by using the Amazon S3 console, S3 Batch Operations, the Amazon S3 REST API,
 the AWS SDKs, and the AWS Command Line Interface (AWS CLI).


For instructions, see [Restoring an archived object](restoring-objects.md "restoring-objects.md"). After you restore the archived object, you can download it. 


## Downloading objects based on metadata


You can add preconditions to download an object based
 on it's metadata using a conditional read request. You can return an object based on it's Entity tag (ETag) or last modified date. This can limit an S3 operation to objects
 updated since a specified date or only return a specific object version.


You can use conditional writes for [GetObject](../API/API_GetObject.md "../API/API_GetObject.md") or 
 [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md") requests.


For more information about conditional requests see, [Add preconditions to S3 operations with conditional requests](conditional-requests.md "conditional-requests.md").


## Troubleshooting downloading objects


Insufficient permissions or incorrect bucket or AWS Identity and Access Management (IAM) user policies can cause
 errors when you're trying to download objects from Amazon S3. These problems can often cause Access
 Denied (403 Forbidden) errors, where Amazon S3 is unable to allow access to a resource.


For common causes of Access Denied (403 Forbidden) errors, see [Troubleshoot access denied (403
 Forbidden) errors in Amazon S3](troubleshoot-403-errors.md "troubleshoot-403-errors.md").


If you're getting a 404 NoSuchKey error when trying to access an object, see [How can I troubleshoot the 404 NoSuchKey error from Amazon S3?](https://repost.aws/knowledge-center/404-error-nosuchkey-s3 "https://repost.aws/knowledge-center/404-error-nosuchkey-s3") in the AWS re:Post Knowledge Center.
