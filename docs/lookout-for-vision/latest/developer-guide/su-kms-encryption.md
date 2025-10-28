End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Step 5: (Optional) Using your own AWS Key Management Service key

You can use AWS Key Management Service (KMS) to manage encryption for the input images that
you store in Amazon S3 buckets.

By default your images are encrypted with a key that AWS owns and manages. You can also
choose to use your own AWS Key Management Service (KMS) key. For more information, see [AWS Key Management Service concepts](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys").

If you want to use your own KMS key, use the
following policy to specify the KMS key. Change
`kms_key_arn` to the ARN of the KMS key (or KMS alias ARN) that you want to use.
Alternatively, specify `*` to use any KMS key. For information about
adding the policy to a user or role, see [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").
