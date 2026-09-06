

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Key management
<a name="key-management"></a>

Amazon Q Business encrypts the contents of your index using the following types of keys:
+ An AWS-owned AWS KMS. This is the default.
+ A customer-managed KMS key. You can create the key when you are creating an Amazon Q application environment, retriever, index, web experience, data source, or plugins, or you can create the key using the AWS KMS console. Select a symmetric encryption customer-managed KMS key. 
**Important**  
Amazon Q does not support asymmetric KMS keys. For more information, see [Using Symmetric and Asymmetric Keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.