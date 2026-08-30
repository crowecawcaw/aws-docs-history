# Restrict artifact access to model package deployments

When you share a model package across accounts, the consuming account's execution role
needs `s3:GetObject` on the model artifacts in the producing account. By default,
that permission applies whenever the role is used. As a result, any principal that uses the
role can read the artifacts from a notebook, from a training job, or through a direct API
call—not only while a model package is being deployed.

You can narrow that access so that only a model package deployment can read the
artifacts. During deployment, SageMaker AI applies the session tag
`sagemaker:ModelPackageArn` to the execution-role session it assumes. The tag
value is the ARN of the model package being deployed. A bucket policy that requires this tag
therefore grants access only to deployment sessions.

This requires three pieces working together. All three are yours to configure; SageMaker AI
supplies only the session tag:

- An execution role tagged `ManagedBy=SageMaker` whose trust policy allows
  only the SageMaker AI service principal to assume it.
- A service control policy that prevents anyone other than SageMaker AI from assuming that
  role or from setting the `sagemaker:ModelPackageArn` tag key. Without
  this, a principal with permission to call AWS STS might supply the tag
  themselves.
- An Amazon S3 bucket policy that grants `s3:GetObject` only when the session
  carries the tag, the caller is in your organization, and the role is tagged
  `ManagedBy=SageMaker`.

###### Important

The SCP is what makes the session tag trustworthy. If you apply the bucket policy
without the SCP, a principal that can assume the execution role directly can attach the
`sagemaker:ModelPackageArn` tag to its own session and satisfy the bucket
policy.

## Step 1: Tag and scope the execution role

In the consuming account, tag the execution role `ManagedBy=SageMaker` and
restrict its trust policy to the SageMaker AI service principal. The trust policy must allow both
`sts:AssumeRole` and `sts:TagSession`. Without
`sts:TagSession`, SageMaker AI cannot apply the
`sagemaker:ModelPackageArn` session tag, and Amazon S3 denies every read that
the bucket policy in Step 3 requires.

```
{
  "RoleName": "GovernedModelExecutionRole",
  "Tags": [ { "Key": "ManagedBy", "Value": "SageMaker" } ],
  "AssumeRolePolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": { "Service": "sagemaker.amazonaws.com" },
      "Action": [ "sts:AssumeRole", "sts:TagSession" ]
    }]
  }
}
```

## Step 2: Add a service control policy

Attach the following SCP in your organization. The first statement allows only the
SageMaker AI service principal to assume a role tagged
`ManagedBy=SageMaker`. The second allows only SageMaker AI to set the
`sagemaker:ModelPackageArn` tag key, which is the only tag key that the
bucket policy evaluates. For more information, see [Creating,
updating, and deleting service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md").

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyNonSageMakerAssumeOnManagedRoles",
      "Effect": "Deny",
      "Action": "sts:AssumeRole",
      "Resource": "*",
      "Condition": {
        "StringEquals": { "aws:ResourceTag/ManagedBy": "SageMaker" },
        "StringNotEquals": { "aws:PrincipalServiceName": "sagemaker.amazonaws.com" }
      }
    },
    {
      "Sid": "DenyTaggingProtectedKeysUnlessSageMaker",
      "Effect": "Deny",
      "Action": [ "iam:TagRole", "iam:UntagRole", "sts:TagSession" ],
      "Resource": "*",
      "Condition": {
        "StringLike": { "aws:RequestTag/sagemaker:ModelPackageArn": "*" },
        "StringNotEquals": { "aws:PrincipalServiceName": "sagemaker.amazonaws.com" }
      }
    }
  ]
}
```

###### Note

Both statements use `StringNotEquals` on
`aws:PrincipalServiceName`, which evaluates to true when the key is
absent. The SCP therefore denies these actions to every IAM user and role in your
member accounts, including sessions that carry no service principal at all. SCPs do
not apply to calls that AWS services make with their own service principals; the
role's trust policy, which grants access only to the SageMaker AI service principal, is what
excludes other AWS services.

## Step 3: Add the Amazon S3 bucket policy

In the producing account, apply the following policy to the bucket holding the model
artifacts. All three conditions must hold. Amazon S3 denies any session that is missing
one.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOnlyModelPackageDeployments",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::`model-artifacts-bucket`/`model-package-prefix`/*",
      "Condition": {
        "StringLike": {
          "aws:PrincipalTag/sagemaker:ModelPackageArn":
            "arn:aws:sagemaker:*:`producer-account-id`:model-package/`model-package-group`/*"
        },
        "StringEquals": {
          "aws:PrincipalOrgID": "`o-organization-id`",
          "aws:PrincipalTag/ManagedBy": "SageMaker"
        }
      }
    }
  ]
}
```

Using `Principal` with a value of `*` together with these
conditions means any role in your organization that is tagged
`ManagedBy=SageMaker` and carries the deployment tag can read the
artifacts. You do not have to edit the policy for each consuming role. The wildcard on
the model package ARN covers every version in the group.

###### Important

Scope `Resource` to the artifacts of a single model package group. A
prefix spanning several groups would let a deployment of one model package read
another group's artifacts, because the session tag is checked against the group
wildcard rather than the object path.

If the artifacts are encrypted with a customer managed AWS KMS key, the execution role
also needs `kms:Decrypt` on that key. Grant it in the key policy; an IAM
policy alone is not sufficient.

## Monitor artifact access

Your account records both the tagging of the session and the resulting access
decision.

- In CloudTrail, the `AssumeRole` event for the execution role lists the
  session tags under `requestParameters`. Confirm that
  `sagemaker:ModelPackageArn` is present and matches the model
  package you deployed.
- In Amazon S3 data events or server access logs, `GetObject` requests
  against the artifact prefix show whether each read was allowed or denied, so you
  can confirm that non-deployment access is being refused.

Before applying the policies to a production bucket, you can evaluate them with the
IAM policy simulator to confirm that a deployment session is allowed and that a
session without the tag is denied. For more information, see [Testing IAM
policies with the IAM policy simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md").
