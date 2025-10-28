# Data perimeters

A [data perimeter](https://aws.amazon.com/identity/data-perimeters-on-aws/ "https://aws.amazon.com/identity/data-perimeters-on-aws/") is a set of permissions guardrails in your AWS environment
you use to help ensure that only your trusted identities are accessing trusted resources from
expected networks.

Amazon Athena uses service-owned Amazon S3 buckets to store example queries and sample datasets. If
you are using data perimeters to control access in your environment, you must explicitly allow
access to these service-owned resources to use the corresponding Athena features.

The following table lists the ARN of the Amazon S3 bucket that Athena needs to access, required
permissions, identity used by Athena, and the features that rely on the S3 bucket. To allow
access, replace `<region>` in the bucket ARN with your actual AWS Region and
allowlist this bucket based on your Amazon S3 access controls.

| Data perimeters that Athena uses        | Resource ARN              | Required permissions                | Identity used for access                                                                                 | Access scenarios |
| --------------------------------------- | ------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------- |
| `arn:aws:s3:::athena-examples-<region>` | s3:GetObjects3:ListBucket | The IAM principal accessing Athena. | <br>• Running example queries in the Athena console <br>• Exploring sample datasets that Athena provides |
