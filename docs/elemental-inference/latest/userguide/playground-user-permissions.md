

# User permissions
<a name="playground-user-permissions"></a>

In addition to permission to use the Elemental Inference console, the IAM identity that you use to sign in needs the following permissions to use the playground:
+ MediaConvert – `GetQueue`, `CreateQueue`, `CreateJob`, `ListJobs`, `GetJob`
+ `iam:PassRole` on the service role (MediaConvert requires this to run a job as the role)
+ IAM read permissions – `GetRole`, `ListAttachedRolePolicies`, `GetPolicy`, `GetPolicyVersion`
+ To let the console create the service role – `iam:CreateRole`, `iam:CreatePolicy`, `iam:AttachRolePolicy`
+ To let the console update the service role – `iam:CreatePolicyVersion`, `iam:DeletePolicyVersion`
+ Amazon S3 – `ListAllMyBuckets`, `ListBucket`, and `GetObject` on the input and output buckets (the console plays both videos from Amazon S3)