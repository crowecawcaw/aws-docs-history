# Setting encryption in S3 Vectors

This topic explains how to set the encryption configuration for your S3 vector
buckets and indexes.

Before you begin, make sure you have the following:

- Appropriate permissions to view bucket and index properties.

###### To configure encryption for a vector bucket

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Vector buckets**.
3. Choose **Create vector bucket**.
4. For **Bucket name**, enter a name for your bucket.

The bucket name must:

    * Be unique within your account for this AWS Region
    * Be between 3 and 63 characters long
    * Consist only of lowercase letters, numbers, and hyphens (-)

5.  For **Encryption**, choose
    - **Specify encryption type** – Choose a specific encryption method:
      - **Server-side encryption with Amazon S3 managed keys (SSE-S3)** – With SSE-S3, Amazon S3 handles the generation, rotation, and management of encryption keys automatically.
      - **Server-side encryption with AWS Key Management Service keys (SSE-KMS)** – Similar to SSE-S3, but uses customer managed keys (CMKs) in AWS KMS, giving you more control over your keys. For more information about customer managed keys, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

      If you select this option, under **AWS KMS key**, choose one of the following options:

          - **Choose from your AWS KMS keys** – Select an existing KMS key from the dropdown list
          - **Enter AWS KMS key ARN** – Enter the Amazon Resource Name (ARN) of a KMS key
          - **Create a KMS key** – Create a new customer managed key in the AWS KMS console. For more information, see [Creating symmetric customer managed keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the *AWS Key Management Service Developer Guide*.

###### Note

The following requirements apply to the KMS key:

    * AWS KMS key ID must not be empty
    * Your KMS key must be in the same Region where this bucket is being created
    * AWS KMS key ARN must start with "arn:aws:kms:"

###### Important

Encryption settings can't be changed after the vector bucket is created. 6. If you chose **Enter AWS KMS key ARN**, enter the ARN in the text field provided. 7. If you chose **Create a KMS key**, the console opens the AWS KMS console in a new tab. For instructions on creating a KMS key, see [Creating symmetric customer managed keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_. 8. Choose **Create vector bucket**.

###### Important

When using KMS encryption, ensure that the IAM principals that need to access objects in the bucket have the necessary KMS permission (kms:Decrypt) for the selected KMS key.

###### To configure encryption for a vector index

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Vector buckets**.
3. In the list of vector buckets, choose the name of the bucket where you want to create a vector index.
4. Choose **Create vector index**.
5. For **Vector index name**, enter a name for your vector index.

Vector index names must be unique within the vector bucket. Index name must be between 3 and 63 characters. Valid characters are lowercase letters (a-z), numbers (0-9), hyphens (-), and dots (.). For more information about the vector index naming requirements, see [Vector bucket naming rules](s3-vectors-buckets-naming.md "s3-vectors-buckets-naming.md"). 6. For **Dimension**, enter the number of values in each vector.

###### Note

    * The value for **Dimension** determines how many numerical values each vector will contain.
    * All vectors added to this index must have exactly this number of values.
    * Dimension must be between 1 and 4096.
    * A larger dimension requires more storage space.
    * Choose based on your embedding model's output dimensions.For more information about the dimension requirements, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md").

7. For **Distance metric**, choose one of the following options:
   - **Cosine** – Measures the cosine of the angle between vectors. Best for normalized vectors and when direction matters more than magnitude
   - **Euclidean** – Measures the straight-line distance between vectors. Best when both direction and magnitude are important.

8. (Optional) Under **Non-filterable metadata**, configure metadata keys that will be stored but not used for filtering:

To add non-filterable metadata keys:

    1. Choose **Add key**.
    2. Enter a key name (1-63 characters and unique within this vector index).
    3. Repeat to add additional keys (maximum 10 keys).###### Note

You can attach filterable metadata as key-value pairs to each vector when you insert vector data after you create a vector index. By default, all metadata keys that are attached to vectors are filterable and can be used as filters in a similarity query. Only metadata keys that are specified as non-filterable during vector index creation are excluded from filtering. For more information about metadata size limits per vector, including both total and filterable metadata constraints, see . 9. For **Encryption**, choose **Specify encryption type** and then choose one of the following options:

    * **Use bucket settings for encryption** – Amazon S3 applies the vector bucket encryption settings to encrypt vector data in the vector index.
    * **Override bucket settings for encryption** – Specify a specific encryption type for the vector index:




    	+ **Server-side encryption with Amazon S3 managed keys (SSE-S3)** – With SSE-S3, Amazon S3 handles the generation, rotation, and management of encryption keys automatically.
    	+ **Server-side encryption with AWS Key Management Service keys (SSE-KMS)** – Similar to SSE-S3, but uses customer managed keys (CMKs) in AWS KMS, giving you more control over your keys. For more information about customer managed keys, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the *AWS Key Management Service Developer Guide*.


    	If you select this option, under **AWS KMS key**, choose one of the following options:




    		- **Choose from your AWS KMS keys** – Select an existing KMS key from the dropdown list
    		- **Enter AWS KMS key ARN** – Enter the Amazon Resource Name (ARN) of a KMS key
    		- **Create a KMS key** – Create a new customer managed key in the AWS KMS console. For more information, see [Creating symmetric customer managed keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the *AWS Key Management Service Developer Guide*.
    	###### Note

    	The following requirements apply to the KMS key:



    		- AWS KMS key ID must not be empty.
    		- Your KMS key must be in the same Region where this bucket is being created.
    		- AWS KMS key ARN must start with "arn:aws:kms:"
    	###### Important



    		- Encryption settings can't be changed after the vector index is created.
    		- If you chose
    		 **Enter AWS KMS key ARN**, enter the ARN in
    		 the text field provided.
    		- If you chose **Create a KMS
    		 key**, the console opens the AWS KMS console in a new tab. For
    		 instructions on creating a KMS key, see *Creating symmetric customer
    		 managed keys* in the *AWS Key Management Service
    		 Developer Guide*.
    	###### Important

    	When using KMS encryption, ensure that the IAM principals that need to access objects in the bucket have the necessary KMS permission (kms:Decrypt) for the selected KMS key.

10. Under **Tags (Optional)**, you can add tags as key-value pairs to help track and organize vector index costs using AWS Billing and Cost Management. Enter a **Key** and a **Value**. To add another tag, choose **Add Tag**. You can enter up to 50 tags for a vector index. For more information, see [Using tags with S3 vector buckets](s3-vectors-tags.md "s3-vectors-tags.md").
11. Review your configuration carefully.

###### Note

These settings can't be changed after creation. 12. Choose **Create vector index**.
The following example shows how to create a vector bucket with the SSE-S3 encryption
configuration by using the AWS CLI. To use this example, replace the `user input
 placeholders` with your own information.

```
aws s3vectors create-vector-bucket \
        --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
        --encryption-configuration '{"sseType": "AES256"}'
```

The following examples shows how to create a vector bucket that uses the SSE-KMS
encryption configuration with a customer managed key. To use this example, replace the `user
 input placeholders` with your own information.

```
aws s3vectors create-vector-bucket \
        --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
        --encryption-configuration '{"sseType": "aws:kms", "kmsKeyArn": "arn:aws:kms:`us-east-1`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"}'
```

The following example shows how to create a vector index with the SSE-S3 encryption configuration by using the AWS CLI. To use this example, replace the `user input placeholders` with your own information.

```
aws s3vectors create-index \
        --vector-bucket-name `"amzn-s3-demo-vector-bucket"` \
        --index-name `"amzn-s3-demo-vector-index"` \
        --encryption-configuration '{"sseType": "AES256"}'
```

The following examples shows how to create a vector index that uses the SSE-KMS encryption configuration with a customer managed key. To use this example, replace the `user input placeholders` with your own information.

```
aws s3vectors create-index \
        --vector-bucket-name `"amzn-s3-demo-vector-bucket"` \
        --index-name `"amzn-s3-demo-vector-index"` \
        --encryption-configuration '{"sseType": "aws:kms", "kmsKeyArn": `"arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890abc"`}'
```

The following examples shows will create a vector index using the encryption settings of the vector bucket. To use this example, replace the `user input placeholders` with your own information.

```
aws s3vectors create-index \
        --vector-bucket-name `"amzn-s3-demo-vector-bucket"` \
        --index-name `"amzn-s3-demo-vector-index"` \
```
