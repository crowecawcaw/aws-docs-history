# `AWSSupport-TroubleshootS3AccessSameAccount`

**Description**

The `AWSSupport-TroubleshootS3AccessSameAccount` runbook helps diagnose Amazon Simple Storage Service (Amazon S3) access denied issues on bucket or object operations by evaluating the access level granted to the requester AWS Identity and Access Management (IAM) identity (user or role) on your Amazon S3 resource. The runbook evaluates all the relevant access policies, user policies, and resource-based policies (bucket policy, bucket ACL, and object ACL) associated with the Amazon S3 resource and the IAM user or role specified in the input parameters.

###### Important

You can only use this runbook to evaluate access denied issues if the requestor is in the same AWS account as the Amazon S3 bucket or object.

Make sure that your user or the `AutomationAssumeRole` used to run this runbook has the necessary permissions to get/list the relevant resource policies and bucket/key metadata configuration.

If there is a `NotPrincipal` element in the Resource Policy, the runbook will throw an error in the step `PolicyModifier`.

**How does it work?**

The runbook performs the following evaluations:

- Verifies the existence of the IAM user or role and deconstructs the ARN to identify its key components.
- Checks if the Amazon S3 resource (bucket or object) exists and returns the bucket and key name.
- Validates that the user/role and bucket/object are in the same AWS account.
- Retrieves bucket and object ACL configurations if applicable.
- Fetches IAM policies attached to the user or role.
- Retrieves bucket policies if they exist.
- If applicable, fetches AWS KMS key policies for encrypted objects.
- If applicable, fetches VPC endpoint policies.
- Retrieves AWS Organizations Service Control Policies (SCPs) if provided.
- Evaluates all policies together to determine the effective permissions for the specified action.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootS3AccessSameAccount "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootS3AccessSameAccount")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeVpcEndpoints` (if VPC endpoint is specified)
- `iam:GetGroupPolicy`
- `iam:GetPolicy`
- `iam:GetPolicyVersion`
- `iam:GetRole`
- `iam:GetRolePolicy`
- `iam:GetUser`
- `iam:GetUserPolicy`
- `iam:ListAttachedRolePolicies`
- `iam:ListAttachedUserPolicies`
- `iam:ListGroupsForUser`
- `iam:ListRolePolicies`
- `iam:ListUserPolicies`
- `iam:SimulatePrincipalPolicy`
- `kms:GetKeyPolicy` (if KMS encryption is used)
- `s3:GetBucketAcl`
- `s3:GetBucketLocation`
- `s3:GetBucketPolicy`
- `s3:GetObjectAcl`
- `s3:GetObjectVersion`
- `s3:ListBucket`
  Example IAM policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeVpcEndpoints",
                "iam:GetGroupPolicy",
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:GetUser",
                "iam:GetUserPolicy",
                "iam:ListAttachedRolePolicies",
                "iam:ListAttachedUserPolicies",
                "iam:ListGroupsForUser",
                "iam:ListRolePolicies",
                "iam:ListUserPolicies",
                "iam:SimulatePrincipalPolicy",
                "kms:GetKeyPolicy",
                "s3:GetBucketAcl",
                "s3:GetBucketLocation",
                "s3:GetBucketPolicy",
                "s3:GetObjectAcl",
                "s3:GetObjectVersion",
                "s3:ListBucket"
            ],
            "Resource": "*"
        }
    ]
}

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-TroubleshootS3AccessSameAccount`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootS3AccessSameAccount/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootS3AccessSameAccount/description") in Systems Manager under Documents.
2. Select Execute automation.
3. For the input parameters, enter the following:

   - **AutomationAssumeRole (Optional):**

   The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your permissions.
   - **S3ResourceArn (Required):**

   The ARN of your Amazon S3 resource (bucket or key). For object operations such as `PutObject` or `GetObject`, provide the ARN of the object. Example: `arn:aws:s3:::bucket_name`, or `arn:aws:s3:::bucket_name/key_name`.
   - **S3Action (Required):**

   The Amazon S3 Action for which you want the runbook to evaluate the access context. Make sure you provide the corresponding Amazon S3 resource type (bucket or object) for the specific action. Examples include: `GetObject`, `PutObject`, `DeleteObject`, `GetBucketAcl`, etc.
   - **RequesterArn (Required):**

   The IAM Principal (user or role) ARN for which you want to find the access level on the specific Amazon S3 resource. For example: `arn:aws:iam::123456789012:user/user_name` or `arn:aws:iam::123456789012:role/example-role`.
   - **RequesterRoleSessionName (Optional):**

   The session name of the assumed role, in case the IAM ARN is a role and you want to provide a specific session name.
   - **S3ObjectVersionId (Optional):**

   If the object has multiple versions, this parameter allows you to specify the specific version of the object you want to evaluate the access context.
   - **KmsKeyArn (Optional):**

   The AWS KMS Key ARN if it is relevant to the action (example: `CompleteMultipartUpload`, `CopyObject`, `CreateMultipartUpload`, `PutObject`, etc.). Note: The runbook does not support specifying an AWS KMS key in a different AWS account.
   - **VpcEndpointId (Optional):**

   The virtual private cloud (VPC) endpoint ID related to the access evaluation. Amazon S3 bucket policies can control access to buckets from specific VPC endpoints.
   - **ContextKeyList (Optional):**

   Condition keys list and corresponding values with respect to the policy evaluation. For example: `[{"ContextKeyName":"aws:PrincipalArn","ContextKeyValues":["arn:aws:iam::123456789012:root"],"ContextKeyType":"string"}]`.
   - **SCPPolicy (Optional):**

   The AWS Organizations Service Control Policy (SCP) in case you want the runbook to evaluate the input against a particular SCP policy. This is not needed and ignored when you run this runbook from the organization's management account.

4. Select Execute.
5. The automation initiates.
6. The document performs the following steps:

   - **`IAMCheckTypeset`**:

   Checks the existence of the IAM user or role and deconstructs the ARN to identify its key components.
   - **`ResourceTypeCheck`**:

   Checks if the Amazon S3 resource (bucket or object) exists and returns the bucket and key name.
   - **`UaBoOoAccountCheck`**:

   Validates that the user/role and bucket/object are in the same AWS account.
   - **`KeyDetailsChecker`**:

   Retrieves details about the Amazon S3 object if the resource is an object.
   - **`ACLBucketCheck`**:

   Retrieves the bucket ACL configuration.
   - **`ConditionSetter`**:

   Sets up condition keys for policy evaluation.
   - **`FetchIAMPolicy`**:

   Fetches IAM policies attached to the user or role.
   - **`branchOnACLCheck`**:

   Determines if object ACL needs to be checked.
   - **`FetchBucketPolicy`**:

   Retrieves the bucket policy if it exists.
   - **`branchOnKMSCheck`**:

   Determines if AWS KMS key policy needs to be evaluated.
   - **`FetchKMSPolicy`**:

   Retrieves the AWS KMS key policy if applicable.
   - **`branchOnVPCeCheck`**:

   Determines if VPC endpoint policy needs to be evaluated.
   - **`FetchVPCePolicy`**:

   Retrieves the VPC endpoint policy if applicable.
   - **`FetchSCPPolicy`**:

   Retrieves the AWS Organizations SCP if provided.
   - **`PolicyModifier`**:

   Modifies and prepares all policies for evaluation.
   - **`EvaluatePolicy`**:

   Evaluates all policies together to determine the effective permissions for the specified action.

7. After completion, review the Outputs section for the detailed results of the execution.
   **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootS3AccessSameAccount/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootS3AccessSameAccount/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
