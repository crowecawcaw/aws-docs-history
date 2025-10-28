# Customer managed keys for AWS Fargate

ephemeral storage for Amazon ECS

AWS Fargate supports customer managed keys to encrypt data for Amazon ECS tasks stored in ephemeral storage
to help regulation-sensitive customers meet their internal security policies. Customers still get the
serverless benefit of Fargate, while giving enhanced visibility on self-managed storage encryption to
compliance auditors. While Fargate has Fargate-managed ephemeral storage encryption by default,
customers can also use their own self-managed keys when encrypting sensitive data like financial or health
related information.

You can import your own keys into AWS KMS or create the keys in AWS KMS. These self-managed keys are stored
in AWS KMS and perform standard AWS KMS lifecycle actions such as rotate, disable, and delete. You can audit
key access and usage in CloudTrail logs.

By default, KMS key supports 50,000 grants per key. Fargate uses a single AWS KMS grant per customer managed
key task, so it supports up to 50,000 concurrent tasks for a key. If you want to increase this number,
you can ask for a limit increase, which is approved on a case-by-case basis.

Fargate doesn't charge anything extra for using customer managed keys. You're only charged the standard
price for using AWS KMS keys for storage and API requests.

###### Topics

- [Create an encryption key for Fargate
  ephemeral storage for Amazon ECS](fargate-create-storage-key.md "fargate-create-storage-key.md")
- [Managing AWS KMS keys for Fargate ephemeral storage for Amazon ECS](fargate-managing-kms-key.md "fargate-managing-kms-key.md")
