On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Encryption at rest

Amazon Lookout for Equipment encrypts your data at rest with your choice of an encryption key.
You can choose one of the following:

- An AWS owned key. If you don't specify an encryption
  key, your data is encrypted with this key by default.
- A customer managed key. You can provide the Amazon Resource Name (ARN) of an
  encryption key that you created in your account. When you use a customer managed key, you must give the key a key policy that enables Amazon Lookout for Equipment to use
  the key. You must choose a symmetric customer managed key. Amazon Lookout for Equipment
  doesn't support asymmetric customer managed keys. For more information, see [Key management](key-management.md "key-management.md").
- Amazon Lookout for Equipment follows the Amazon S3 bucket encryption policy. You have
  to set Amazon S3 default encryption on your bucket to encrypt objects stored in your bucket
  by Amazon Lookout for Equipment. For more information ,see [S3 bucket encryption](../../../AmazonS3/latest/dev/bucket-encryption.md "../../../AmazonS3/latest/dev/bucket-encryption.md").
