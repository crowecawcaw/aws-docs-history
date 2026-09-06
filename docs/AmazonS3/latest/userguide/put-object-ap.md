

# Upload an object through an access point for a general purpose bucket
<a name="put-object-ap"></a>

This section explains how to upload an object through an access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.

## Using the S3 console
<a name="put-object-ap-console"></a>

**To upload an object through an access point in your AWS account**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region that you want to list access points for. 

1. In the navigation pane on the left side of the console, choose **Access Points**.

1. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.

1. Choose the name of the access point you want to manage or use.

1. Under the **Objects** tab, select **Upload**.

1. Drag and drop files and folders you want to upload here, or choose **Add files** or **Add folder**.
**Note**  
The maximum size of a file that you can upload by using the Amazon S3 console is 160 GB. To upload a file larger than 160 GB, use the AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3 REST API.

1. To change access control list permissions, choose **Permissions**.

1. Under **Access control list (ACL)**, edit the permissions.

   For information about object access permissions, see [Using the S3 console to set ACL permissions for an object](managing-acls.md#set-object-permissions). You can grant read access to your objects to the public (everyone in the world) for all of the files that you're uploading. However, we recommend not changing the default setting for public read access. Granting public read access is applicable to a small subset of use cases, such as when buckets are used for websites. You can always change the object permissions after you upload the object. 

1. To configure other additional properties, choose **Properties**.

1. Under **Storage class**, choose the storage class for the files that you're uploading.

   For more information about storage classes, see [Understanding and managing Amazon S3 storage classes](storage-class-intro.md).

1. To update the encryption settings for your objects, under **Server-side encryption settings**, do the following.

   1. Choose **Specify an encryption key**.

   1. Under **Encryption settings**, choose **Use bucket settings for default encryption** or **Override bucket settings for default encryption**.

   1. If you chose **Override bucket settings for default encryption**, you must configure the following encryption settings.
      + To encrypt the uploaded files by using keys that are managed by Amazon S3, choose **Amazon S3 managed key (SSE-S3)**.

        For more information, see [Using server-side encryption with Amazon S3 managed keys (SSE-S3)](UsingServerSideEncryption.md).
      + To encrypt the uploaded files by using keys stored in AWS Key Management Service (AWS KMS), choose **AWS Key Management Service key (SSE-KMS)**. Then choose one of the following options for **AWS KMS key**:
        + To choose from a list of available KMS keys, choose **Choose from your AWS KMS keys**, and then choose your **KMS key** from the list of available keys.

          Both the AWS managed key (`aws/s3`) and your customer managed keys appear in this list. For more information about customer managed keys, see [Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt) in the *AWS Key Management Service Developer Guide*.
        + To enter the KMS key ARN, choose **Enter AWS KMS key ARN**, and then enter your KMS key ARN in the field that appears. 
        + To create a new customer managed key in the AWS KMS console, choose **Create a KMS key**.

          For more information about creating an AWS KMS key, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.
**Important**  
You can use only KMS keys that are available in the same AWS Region as the bucket. The Amazon S3 console lists only the first 100 KMS keys in the same Region as the bucket. To use a KMS key that is not listed, you must enter your KMS key ARN. If you want to use a KMS key that is owned by a different account, you must first have permission to use the key and then you must enter the KMS key ARN.   
Amazon S3 supports only symmetric encryption KMS keys, and not asymmetric KMS keys. For more information, see [Identifying symmetric and asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html) in the *AWS Key Management Service Developer Guide*.

1. To use additional checksums, choose **On**. Then for **Checksum function**, choose the function that you would like to use. Amazon S3 calculates and stores the checksum value after it receives the entire object. You can use the **Precalculated value** box to supply a precalculated value. If you do, Amazon S3 compares the value that you provided to the value that it calculates. If the two values do not match, Amazon S3 generates an error.

   Additional checksums enable you to specify the checksum algorithm that you would like to use to verify your data. For more information about additional checksums, see [Checking object integrity in Amazon S3](checking-object-integrity.md).

1. To add tags to all of the objects that you are uploading, choose **Add tag**. Enter a tag name in the **Key** field. Enter a value for the tag.

   Object tagging gives you a way to categorize storage. Each tag is a key-value pair. Key and tag values are case sensitive. You can have up to 10 tags per object. A tag key can be up to 128 Unicode characters in length, and tag values can be up to 255 Unicode characters in length. For more information about object tags, see [Tagging your objects](object-tagging.md).

1. To add metadata, choose **Add metadata**.

   1. Under **Type**, choose **System defined** or **User defined**.

      For system-defined metadata, you can select common HTTP headers, such as **Content-Type** and **Content-Disposition**. For a list of system-defined metadata and information about whether you can add the value, see [System-defined object metadata](UsingMetadata.md#SysMetadata). Any metadata starting with the prefix `x-amz-meta-` is treated as user-defined metadata. User-defined metadata is stored with the object and is returned when you download the object. Both the keys and their values must conform to US-ASCII standards. User-defined metadata can be as large as 2 KB. For more information about system-defined and user-defined metadata, see [Working with object metadata](UsingMetadata.md).

   1. For **Key**, choose a key.

   1. Type a value for the key. 

1. To upload your objects, choose **Upload**.

   Amazon S3 uploads your object. When the upload completes, you can see a success message on the **Upload: status** page.

## Using the AWS CLI
<a name="put-object-ap-cli"></a>

The following `put-object` example command shows how you can use the AWS CLI to upload an object through an access point.

The following command uploads the object `puppy.jpg` for AWS account {{111122223333}} using access point {{my-access-point}}.

```
aws s3api put-object --bucket arn:aws:s3:{{AWS Region}}:111122223333:accesspoint/{{my-access-point}} --key {{puppy.jpg}} --body {{puppy.jpg}}      
```

**Note**  
S3 automatically generate access point aliases for all access points and access point aliases can be used anywhere a bucket name is used to perform object-level operations. For more information, see [Access point aliases](access-points-naming.md#access-points-alias).

For more information and examples, see [put-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html) in the *AWS CLI Command Reference*.

## Using the REST API
<a name="put-object-ap-rest"></a>

You can use the REST API to upload an object through an access point. For more information, see [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) in the *Amazon Simple Storage Service API Reference*.

## Using the AWS SDKs
<a name="put-object-ap-SDKs"></a>

You can use the AWS SDK for Python to upload an object through an access point. 

------
#### [ Python ]

In the following example, the file named `{{hello.txt}}` is uploaded for AWS account {{111122223333}} using the access point named {{my-access-point}}.

```
import boto3
s3 = boto3.client('s3')
s3.upload_file('{{/tmp/hello.txt}}', 'arn:aws:s3:{{us-east-1}}:{{111122223333}}:accesspoint/{{my-access-point}}', '{{hello.txt}}')
```

------