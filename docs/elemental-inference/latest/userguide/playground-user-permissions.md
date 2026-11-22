

# User permissions

In addition to permission to use the Elemental Inference console, the IAM identity that you sign in with needs the following permissions to use the playground:
+ MediaConvert – `GetQueue`, `CreateQueue`, `CreateJob`, `ListJobs`, `GetJob`
+ `iam:PassRole` on the service role (MediaConvert requires this to run a job as the role)
+ IAM read permissions – `GetRole`, `ListAttachedRolePolicies`, `GetPolicy`, `GetPolicyVersion`
+ To let the console create the service role – `iam:CreateRole`, `iam:CreatePolicy`, `iam:AttachRolePolicy`
+ To let the console update the service role – `iam:CreatePolicyVersion`, `iam:DeletePolicyVersion`
+ Amazon S3 – `ListAllMyBuckets`, `ListBucket`, and `GetObject` on the input and output buckets (the console plays both videos from Amazon S3)

An All features preview runs in your browser, so your identity also needs the following:
+ Elemental Inference – `CreateFeed`, `AssociateFeed`, `GetFeed`, `ListFeeds`, `DeleteFeed`, `PutMedia`, and `GetMetadata`
+ MediaConvert – `CancelJob`, to cancel the job when you stop a preview
+ Amazon S3 – `PutObject` on the output bucket, to save the results

If the output bucket uses SSE-KMS with a customer managed key, your IAM identity also needs `kms:Decrypt` on that key to play the output and to read a preview's segments. To save a preview's results, it needs `kms:GenerateDataKey` on that key.