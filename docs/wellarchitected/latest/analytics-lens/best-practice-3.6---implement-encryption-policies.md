

# Best practice 3.6 – Implement encryption policies
<a name="best-practice-3.6---implement-encryption-policies"></a>

 Data encryption is a way of translating data from plaintext (unencrypted) to ciphertext (encrypted). Encryption is a critical component of a *defense in depth* strategy. Therefore, it is highly recommended that your organization implement a well-designed encryption and key management system by separating access to the decryption key from access to your data to provide data security. 

## Suggestion 3.6.1 – Implement encryption policies for data at rest and in transit
<a name="suggestion-3.6.1---implement-encryption-policies-for-data-at-rest-and-in-transit"></a>

 Each analytics service provides different types of encryption methods. Review the viable encryption methods of your solutions and implement as necessary. 

 For more details, refer to the following information: 
+  [AWS Key Management Service (AWS KMS) encryption best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/kms.html) 
+  AWS Big Data Blog: [Best Practices for Securing Amazon EMR](https://aws.amazon.com/blogs/big-data/best-practices-for-securing-amazon-emr/) 
+  AWS Big Data Blog: [Encrypt Your Amazon Redshift Loads with Amazon S3 and AWS KMS](https://aws.amazon.com/blogs/big-data/encrypt-your-amazon-redshift-loads-with-amazon-s3-and-aws-kms/) 
+  AWS Big Data Blog: [Encrypt and Decrypt Amazon Kinesis Records Using AWS KMS](https://aws.amazon.com/blogs/big-data/encrypt-and-decrypt-amazon-kinesis-records-using-aws-kms/) 
+  AWS Partner Network (APN) Blog: [Data Tokenization with Amazon Redshift and Protegrity](https://aws.amazon.com/blogs/apn/data-tokenization-with-amazon-redshift-and-protegrity/) 