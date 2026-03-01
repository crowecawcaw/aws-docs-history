# Setting the storage class of an object

You
can specify a storage class for an object when you upload it. If you don't, Amazon S3 uses
the default Amazon S3 Standard storage class for objects in general purpose buckets. You can also change the storage class of an object
that's already stored in an Amazon S3 general purpose bucket to any other storage class using the Amazon S3 console, AWS
SDKs, or the AWS Command Line Interface (AWS CLI). All of these approaches use Amazon S3 API operations to send
requests to Amazon S3.

###### Note

You can't change the storage class of objects stored in directory buckets.

You can direct Amazon S3 to change the storage class of objects automatically by adding an S3 Lifecycle configuration to a bucket. For more information, see [Managing the lifecycle of objects](object-lifecycle-mgmt.md "object-lifecycle-mgmt.md").

When setting up a S3 Replication configuration, you can set the storage class for replicated objects to any other storage class. However, you can't replicate objects that are stored in the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes. For more information, see [Replication configuration file elements](replication-add-config.md "replication-add-config.md").

When setting the storage class programmatically you provide the value of the storage class. The following is a list of console names for storage classes with their corresponding API values:

- **Reduced Redundancy Storage** – `REDUCED_REDUNDANCY`
- **S3 Express One Zone** – `EXPRESS_ONEZONE`
- **S3 Glacier Deep Archive** – `DEEP_ARCHIVE`
- **S3 Glacier Flexible Retrieval** – `GLACIER`
- **S3 Glacier Instant Retrieval** – `GLACIER_IR`
- **S3 Intelligent-Tiering** – `INTELLIGENT_TIERING`
- **S3 One Zone-IA** – `ONEZONE_IA`
- **S3 Standard** – `STANDARD`
- **S3 Standard-IA** – `STANDARD_IA`

## Setting the storage class on a new object

To set the storage class when you upload an object, you can use the following methods.

To set the storage class when uploading a new object in the console:

1. Sign in to the AWS Management Console and open the Amazon S3 console at: [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com//s3 "https://console.aws.amazon.com//s3").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket that you want to upload your folders or files to.
4. Choose **Upload**.
5. In the **Upload** window, choose **Properties**.
6. Under Storage class, choose a storage classes for the files you're uploading.
7. (Optional) Configure any additional properties for the files you're uploading, For more information, see [Uploading objects](upload-objects.md "upload-objects.md")
8. In the Upload window, do one of the following:
   - Drag files and folders to the Upload window.
   - Choose **Add file** or **Add folder**, choose the files or folders to upload, and choose **Open**.

9. At the bottom of the page, Choose **Upload**.

You can specify the storage class on an object when you create it using the `PutObject`, `POST Object` Object, and `CreateMultipartUpload` API operations, add the `x-amz-storage-class` request header. If you don't add this header, Amazon S3 uses the default S3 Standard (`STANDARD`) storage class.

This example request uses the `PutObject` command to set the storage class on a new object to S3 Intelligent-Tiering:

```

PUT /my-image.jpg HTTP/1.1
Host: ``amzn-s3-demo-bucket1``.s3.`Region`.amazonaws.com
Date: Wed, 12 Oct 2009 17:50:00 GMT
Authorization: authorization string
Content-Type: image/jpeg
Content-Length: 11434
Expect: 100-continue
x-amz-storage-class: INTELLIGENT_TIERING

```

This example uses the `put-object` command to upload the `my_images.tar.bz2` to `amzn-s3-demo-bucket1` in the `GLACIER` storage class:

```

aws s3api put-object --bucket ``amzn-s3-demo-bucket1`` --key `dir-1/my_images.tar.bz2` --storage-class `GLACIER` --body `my_images.tar.bz2`

```

If the object size is more than 5 GB, use the following command to set the storage class:

```

aws s3 cp `large_test_file` `s3://`amzn-s3-demo-bucket1`` --storage-class `GLACIER`

```

## Changing the storage class for an existing object

To set the storage class when you upload an object, you can use the following methods.

You can change an object's storage class using the Amazon S3 console if the object size is less than 5 GB. If larger, we recommend adding an S3 Lifecycle configuration to change the object's storage class.

To change the storage class of an object in the console:

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket containing the objects you want to change.
4. Select the check box to the left of the names of the objects you want to
   change.
5. On the **Actions** menu, choose **Edit storage class** from
   the list of options that appears.
6. Select from the storage classes available for your object.
7. Under **Additional copy settings**, choose whether you want to **Copy source settings**, **Don’t specify settings**, or **Specify settings**. **Copy source settings** is the default option. If you only want to copy the object without the source settings attributes, choose **Don’t specify settings**. Choose **Specify settings** to specify settings for storage class, ACLs, object tags, metadata, server-side encryption, and additional checksums.
8. Choose **Save changes** in the bottom-right corner. Amazon S3 saves your
   changes.

To change the storage class of an existing object, use the following methods.

This example request uses the `PutObject` command to set the storage class for an existing object to S3 Intelligent-Tiering:

```

PUT /my-image.jpg HTTP/1.1
Host: ``amzn-s3-demo-bucket1``.s3.`Region`.amazonaws.com
Date: Wed, 12 Oct 2009 17:50:00 GMT
Authorization: authorization string
Content-Type: image/jpeg
Content-Length: 11434
Expect: 100-continue
x-amz-storage-class: INTELLIGENT_TIERING

```

This example uses the `cp` command to change the storage class of the of an existing object from its current storage class to `DEEP_ARCHIVE` storage class:

```

aws s3 cp `object_S3_URI` `object_S3_URI` --storage-class `DEEP_ARCHIVE`

```

## Restricting access policy permissions to a specific storage class

When you grant access policy permissions for Amazon S3 operations, you can use the
`s3:x-amz-storage-class` condition key to restrict which storage class to use
when storing uploaded objects. For example, when you grant the `s3:PutObject`
permission, you can restrict object uploads to a specific storage class. For an example
policy, see [Example: Restricting object uploads to objects with a specific storage class](security_iam_service-with-iam.md#example-storage-class-condition-key "security_iam_service-with-iam.md#example-storage-class-condition-key").

For more information about using conditions in policies and a complete list of Amazon S3
condition keys, see the following topics:

- [Actions, resources, and condition keys for Amazon S3](../../../service-authorization/latest/reference/list_amazons3.md "../../../service-authorization/latest/reference/list_amazons3.md") in the _Service Authorization
  Reference_

For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").

- [Bucket policy examples using condition keys](amazon-s3-policy-keys.md "amazon-s3-policy-keys.md")
