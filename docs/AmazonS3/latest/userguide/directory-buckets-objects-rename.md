# Renaming objects in directory buckets

Using the `RenameObject` operation, you can atomically rename an existing
 object in a directory bucket that uses the S3 Express One Zone storage class, without any data
 movement. You can rename an object by specifying the existing object’s name as the source
 and the new name of the object as the destination within the same directory bucket. The
 `RenameObject` API operation will not succeed on objects that end with the
 slash (`/`) delimiter character. For more information, see [Naming Amazon S3
 objects](object-keys.md "object-keys.md").

The `RenameObject` operation is typically completed in milliseconds
 regardless of the size of the object. This capability accelerates applications like log file
 management, media processing, and data analytics. Additionally, `RenameObject` preserves all
 object metadata properties, including the storage class, encryption type, creation date,
 last modified date, and checksum properties.

###### Note

`RenameObject` is only supported for objects stored in the S3 Express One Zone storage class.

 To grant access to the `RenameObject` operation, we recommend that you use the
 `CreateSession` operation for session-based authorization. Specifically, you
 grant the `s3express:CreateSession` permission to the directory bucket in a
 bucket policy or an identity-based policy. Then, you make the `CreateSession` API
 call on the directory bucket to obtain a session token. With the session token in your
 request header, you can make API requests to this operation. After the session token
 expires, you make another `CreateSession` API call to generate a new session
 token for use. The AWS CLI and AWS SDKs will create and manage your session including
 refreshing the session token automatically to avoid service interruptions when a session
 expires. For more information about authorization, see [`CreateSession`](../API/API_CreateSession.md "../API/API_CreateSession.md") in
 the *Amazon S3 API Reference*. To learn more about Zonal endpoint API
 operations, see [Authorizing Zonal
 endpoint API operations with `CreateSession`](s3-express-create-session.md "s3-express-create-session.md"). 

 If you don't want to overwrite an existing object, you can add the
 `If-None-Match` conditional header with the value `‘*’` in the
 `RenameObject` request. Amazon S3 returns a `412 Precondition Failed`
 error if the object name already exists. For more information, see [`RenameObject`](../API/API_RenameObject.md "../API/API_RenameObject.md") in the *Amazon S3 API Reference*.
 

 `RenameObject` is a Zonal endpoint API operation (object-level or data plane operation) that is logged to
 AWS CloudTrail. You can use CloudTrail to gather information on the `RenameObject` operation
 performed on your objects in directory buckets. For more information, see [Logging with AWS CloudTrail for directory buckets](s3-express-one-zone-logging.md "s3-express-one-zone-logging.md") and [CloudTrail log file examples for
 directory buckets](s3-express-log-files.md "s3-express-log-files.md"). 

S3 Express One Zone is the only storage class that supports `RenameObject`, which is priced the same as `PUT`, 
 `COPY`, `POST`, and `LIST` requests (per 1,000 requests) in S3 Express One Zone.
 For more information, see [Amazon S3
 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"). 


## Renaming an object


To rename an object in your directory bucket, you can use the Amazon S3 console, AWS CLI,
 AWS SDKs, the REST API or Mountpoint for Amazon S3 (version 1.19.0 or higher).


###### To rename an object in a directory bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Buckets**, and
 then choose the **Directory buckets** tab. Navigate to
 the Amazon S3 directory bucket that contains the object that you want to
 rename.
3. Select the check box for the object that you want to rename.
4. On the **Actions** menu, choose **Rename
 object**.
5. In the **New object name** box, enter the new name for the
 object.


###### Note

If you specify the same object name as an existing object, the operation will fail and Amazon S3
 returns a `412 Precondition Failed` error. The object key
 name length can't exceed 1,024 bytes. Prefixes included in the
 object name count toward the total length.
6. Choose **Rename object**. Amazon S3 renames your
 object.
The `rename-object` examples show how you can use the
 AWS CLI to rename an object. To run these commands, replace the
 `user input placeholders` with your own
 information

The following example shows how to rename an object with a conditional check
 on the source object's ETag. 


```
aws s3api rename-object \                                    
    --bucket `amzn-s3-demo-bucket--usw2-az1--x-s3` \
    --key `new-file.txt` \
    --rename-source `original-file.txt` \
    --source-if-match "\"`a1b7c3d2e5f6`\""
```
This command does the following:


* Renames an object from `original-file.txt` to
 `new-file.txt` in the
 `amzn-s3-demo-bucket--usw2-az1--x-s3` directory bucket.
* Only performs the rename if the source object's ETag matches
 "`a1b7c3d4e5f6`".
If the ETag doesn't match, the operation will fail with a `412
 Precondition Failed` error. 

The following example shows how to rename an object with a conditional check
 on the new specified object name.


```
aws s3api rename-object \
    --bucket `amzn-s3-demo-bucket--usw2-az1--x-s3` \
    --key `new-file.txt` \
    --rename-source `amzn-s3-demo-bucket--usw2-az1--x-s3`/`original-file.txt` \
    --destination-if-none-match "\"`e5f3g7h8i9j0`\""
```
This command does the following:


* Renames an object from `original-file.txt` to
 `new-file.txt` in the
 `amzn-s3-demo-bucket--usw2-az1--x-s3` directory bucket.
* Only performs the rename operation if the object exists and the object's ETag doesn't match
 "`e5f3g7h8i9j0`".
If an object already exists with the new specified name and the matching ETag,
 the operation will fail with a `412 Precondition Failed` error. 


SDK for Java
You can use the AWS SDK for Java to rename your objects. To use these examples, replace the
 `user input placeholders` with your own
 information


The following example demonstrates how to create a
 `RenameObjectRequest` using the AWS SDK for
 Java



```
String key = "`key`";
String newKey = "`new-key`";
String expectedETag = "`e5f3g7h8i9j0`";
RenameObjectRequest renameRequest = RenameObjectRequest.builder()
    .bucket(`amzn-s3-demo-bucket--usw2-az1--x-s3`)
    .key(`newKey`)
    .renameSource(`key`)
    .destinationIfMatch(`e5f3g7h8i9j0`)
    .build();
```

This code does the following:



* Create a request to rename an object from "`key`" to
 "`new-key`" in the
 `amzn-s3-demo-bucket--usw2-az1--x-s3` directory bucket.
* Includes a condition that the rename will only occur if the object's ETag matches
 "`e5f3g7h8i9j0`".
* If the ETag doesn't match or the object doesn't exist, the operation will fail.

The following example shows how to create a
 `RenameObjectRequest` with a none-match condition
 using the AWS SDK for Java.



```
String key = "`key`";
String newKey = "`new-key`";
String noneMatchETag = "`e5f3g7h8i9j0`";
RenameObjectRequest renameRequest = RenameObjectRequest.builder()
    .bucket(`amzn-s3-demo-bucket--usw2-az1--x-s3`)
    .key(`newKey`)
    .renameSource(`key`)
    .destinationIfNoneMatch(noneMatchETag)
    .build();
```

This code does the following:



* Creates a request to rename an object from "`key`" to
 "`new-key`" in the
 `amzn-s3-demo-bucket--usw2-az1--x-s3` directory bucket.
* Includes a condition using `.destinationIfNoneMatch(noneMatchETag)` that ensures
 the rename will only occur if the destination object's ETag
 doesn't match
 "`e5f3g7h8i9j0`".

The operation will fail with a `412 Precondition
 Failed` error if an object exists with the new specified
 name and has the specified ETag. 



SDK for Python
You can use the SDK for Python to rename your objects. To use these
 examples, replace the `user input
 placeholders` with your own information.


The following example demonstrates how to rename an object using
 the AWS SDK for Python (Boto3).



```
def basic_rename(bucket, source_key, destination_key):
    try:
        s3.rename_object(
            Bucket=`amzn-s3-demo-bucket--usw2-az1--x-s3`,
            Key=`destination_key`,
            RenameSource=f"{`source_key`}"
        )
        print(f"Successfully renamed {`source_key`} to {`destination_key`}")
    except ClientError as e:
        print(f"Error renaming object: {e}")
```

This code does the following:



* Renames an object from `source_key` to
 `destination_key` in the
 `amzn-s3-demo-bucket--usw2-az1--x-s3` directory bucket.
* Prints a success message if the renaming of your object is successful or prints an error
 message if it fails.

The following example demonstrate how to rename an object with the `SourceIfMatch` and 
 `DestinationIfNoneMatch` conditions using the AWS SDK for Python (Boto3).



```
def rename_with_conditions(bucket, source_key, destination_key, source_etag, dest_etag):
    try:
        s3.rename_object(
            Bucket=`amzn-s3-demo-bucket--usw2-az1--x-s3`,
            Key=`destination_key`,
            RenameSource=f"{`amzn-s3-demo-bucket--usw2-az1--x-s3`}/{`source_key`}",
            SourceIfMatch=`source_ETag`,
            DestinationIfNoneMatch=`dest_ETag`
        )
        print(f"Successfully renamed {`source_key`} to {`destination_key`} with conditions")
    except ClientError as e:
        print(f"Error renaming object: {e}")
```

This code does the following:



* Performs a conditional rename operation and applies two
 conditions, `SourceIfMatch` and
 `DestinationIfNoneMatch`. The combination of
 these conditions ensures that the object hasn't been
 modified and that an object doesn't already exist with the
 new specified name.
* Renames an object from `source_key` to
 `destination_key` in the
 `amzn-s3-demo-bucket--usw2-az1--x-s3` directory bucket.
* Prints a success message if the renaming of your object is
 successful, or prints an error message if it fails or if
 conditions aren't met.


SDK for Rust
You can use the SDK for Rust to rename your objects. To use these
 examples, replace the `user input
 placeholders` with your own information.


The following example demonstrates how to rename an object in the
 `amzn-s3-demo-bucket--usw2-az1--x-s3` directory bucket using the
 SDK for Rust.



```
async fn basic_rename_example(client: &Client) -> Result<(), Box<dyn Error>> {
    let response = client
        .rename_object()
        .bucket(" `amzn-s3-demo-bucket--usw2-az1--x-s3`")
        .key("`new-name.txt`")  // New name/path for the object
        .rename_source("`old-name.txt`")  // Original object name/path
        .send()
        .await?;
    Ok(())
}
```

This code does the following:



* Creates a request to rename an object from "`old-name.tx`" to "`new-name.txt`" in the `amzn-s3-demo-bucket--usw2-az1--x-s3` directory bucket.
* Returns a `Result` type to handle potential errors.


 You can send REST requests to rename an object. For more information, see [`RenameObject`](../API/API_RenameObject.md "../API/API_RenameObject.md") in the *Amazon S3 API Reference*.
 

 Starting with the 1.19.0 version or higher, Mountpoint for Amazon S3 supports
 renaming objects in S3 Express One Zone. For more information on Mountpoint, see
 [Working with Mountpoint](mountpoint.md "mountpoint.md").
