

# Encryption in Amazon Textract

Data encryption refers to protecting data while in transit and at rest. You can protect your data by using Amazon S3-Managed Keys or AWS KMS key at rest, alongside standard Transport Layer Security (TLS) while in transit. Amazon Textract Insights also encrypts the projects, blueprints, and job data that it stores, with AWS owned keys by default or with a customer managed key that you choose.

## Encryption at rest
<a name="encryption-at-rest"></a>

The primary method of encrypting data in Amazon Textract Core is server-side encryption. Input documents passed from Amazon S3 buckets are encrypted by Amazon S3 and decrypted when you access them. As long as you authenticate your request and you have access permissions, there is no difference in the way you access encrypted or unencrypted objects. For example, if you share your objects using a presigned URL, that URL works the same way for both encrypted and unencrypted objects. Additionally, when you list objects in your bucket, the `List` API returns a list of all objects, regardless of whether they are encrypted. 

Amazon Textract Core uses two mutually exclusive methods of server-side encryption.

**Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3)**

When you use server-side encryption with Amazon S3-Managed Keys (SSE-S3), each object is encrypted with a unique key. As an additional safeguard, this method encrypts the key itself with a master key that it regularly rotates. Amazon S3 server-side encryption uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data. For more information, see Protecting Data Using Server-Side Encryption with Amazon S3-Managed Encryption Keys (SSE-S3). 

**Server-Side Encryption with KMS keys Stored in AWS Key Management Service (SSE-KMS)**

Server-side encryption with KMS keys stored in AWS Key Management Service (SSE-KMS) is similar to SSE-S3, but with some additional benefits and charges for using this service. There are separate permissions for the use of a KMS key that provides added protection against unauthorized access of your objects in Amazon S3. SSE-KMS also provides you with an audit trail that shows when your KMS key was used and by whom. Additionally, you can create and manage KMS keys or use AWS managed keys that are unique to you, your service, and your AWS Region. For more information, see Protecting Data Using Server-Side Encryption with KMS keys Stored in AWS Key Management Service (SSE-KMS). 

## Encryption at rest for Amazon Textract Insights
<a name="encryption-at-rest-insights"></a>

Amazon Textract Insights encrypts the projects, blueprints, and job data that it stores. By default, it uses AWS owned keys at no additional charge. No configuration is required.

To control the key yourself, you can use a customer managed AWS KMS key instead. You specify the key in `EncryptionConfiguration` when you create or update a project or blueprint, or when you start a job. The identity that calls Amazon Textract Insights also needs permission to use the key. Your key stays in the AWS Region you call, and cross-Region inference doesn't change how it's scoped.

Amazon Textract Insights writes job output, including `job_metadata.json`, the result files, and any additional files and page images, to the output location that you specify. If you pass a customer managed key in `EncryptionConfiguration` when you call `StartDocumentInsights`, Amazon Textract Insights encrypts each output object with server-side encryption using that KMS key (SSE-KMS). If you don't pass a key, the output objects get your bucket's default encryption. A key that you set on a project encrypts the project's stored data, not its job output. To encrypt job output with your key, pass the key with each job. Anyone who reads the output needs `kms:Decrypt` on the key.

For the operations that accept a key, the required AWS KMS permissions, an example key policy, and the encryption context that Amazon Textract Insights attaches to each AWS KMS request, see [Data protection and encryption](insights-data-protection.md).

## Encryption in transit
<a name="encryption-in-transit"></a>

For data in transit, Amazon Textract uses TLS to encrypt data sent between the service and your client. Additionally, Amazon Textract uses VPC endpoints to send data between the various microservices used when Amazon Textract processes a document. When Amazon Textract Insights routes a request to another AWS Region in the same geography for inference, the data is encrypted in transit across the Amazon network.