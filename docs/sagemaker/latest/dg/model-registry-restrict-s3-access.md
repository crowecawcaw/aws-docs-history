

# Restrict artifact access to model package deployments
<a name="model-registry-restrict-s3-access"></a>

When you share a model package across accounts, the consuming account's execution role needs `s3:GetObject` on the model artifacts in the producing account. By default, that permission applies whenever the role is used. As a result, any principal that uses the role can read the artifacts from a notebook, from a training job, or through a direct API call—not only from an endpoint deployed from a model package.

You can narrow that access so that only endpoints deployed from a model package can read the artifacts. When you deploy an endpoint from a model package, SageMaker AI applies the session tag `sagemaker:ModelPackageArn` to the execution-role sessions it assumes for that endpoint. The tag value is the ARN of the model package version. The tag applies for the life of the endpoint, both to the sessions SageMaker AI uses to download the model artifacts and to the credentials that the inference container receives at runtime. A bucket policy that requires this tag therefore grants access only to sessions that belong to an endpoint deployed from a matching model package. Notebooks, training jobs, and endpoints deployed from a plain container image do not carry the tag.

If code in your inference container assumes another role, the resulting credentials do not carry the `sagemaker:ModelPackageArn` tag.

**Note**  
This applies to real-time endpoint deployments. Serverless endpoints and inference components do not carry the `sagemaker:ModelPackageArn` session tag, so a bucket policy that requires the tag denies them at read time. If you need to deploy the same artifacts that way, keep them in a bucket that does not require the tag.

This requires three pieces working together. All three are yours to configure; SageMaker AI supplies only the session tag:
+ An execution role tagged `ManagedBy=SageMaker` whose trust policy allows only the SageMaker AI service principal to assume it.
+ A service control policy that prevents anyone other than SageMaker AI from assuming that role or from setting the `sagemaker:ModelPackageArn` tag key. Without this, a principal with permission to call AWS STS might supply the tag themselves.
+ An Amazon S3 bucket policy that grants `s3:GetObject` only when the session carries the tag, the caller is in your organization, and the role is tagged `ManagedBy=SageMaker`.

**Important**  
The SCP is what makes the session tag trustworthy. If you apply the bucket policy without the SCP, a principal that can assume the execution role directly can attach the `sagemaker:ModelPackageArn` tag to its own session and satisfy the bucket policy.

## Step 1: Tag and scope the execution role
<a name="model-registry-restrict-s3-access-role"></a>

In the consuming account, tag the execution role `ManagedBy=SageMaker` and restrict its trust policy to the SageMaker AI service principal. The trust policy must allow both `sts:AssumeRole` and `sts:TagSession`. Without `sts:TagSession`, SageMaker AI cannot apply the `sagemaker:ModelPackageArn` session tag, and Amazon S3 denies every read that the bucket policy in Step 3 requires.

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
<a name="model-registry-restrict-s3-access-scp"></a>

Attach the following SCP in your organization. The first statement allows only the SageMaker AI service principal to assume a role tagged `ManagedBy=SageMaker`. The second allows only SageMaker AI to set the `sagemaker:ModelPackageArn` tag key, which is the only tag key that the bucket policy evaluates. For more information, see [Creating, updating, and deleting service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_create.html).

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

**Note**  
Both statements use `StringNotEquals` on `aws:PrincipalServiceName`, which evaluates to true when the key is absent. The SCP therefore denies these actions to every IAM user and role in your member accounts, including sessions that carry no service principal at all. SCPs do not apply to calls that AWS services make with their own service principals; the role's trust policy, which grants access only to the SageMaker AI service principal, is what excludes other AWS services.

## Step 3: Add the Amazon S3 bucket policy
<a name="model-registry-restrict-s3-access-bucket"></a>

In the producing account, apply the following policy to the bucket holding the model artifacts. The first statement governs reads by endpoints deployed from a model package. All three of its conditions must hold, and Amazon S3 denies any session that is missing one. The second statement allows model package registration, which happens before any deployment tag exists.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOnlyModelPackageDeployments",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::{{model-artifacts-bucket}}/{{model-package-prefix}}/*",
      "Condition": {
        "StringLike": {
          "aws:PrincipalTag/sagemaker:ModelPackageArn":
            "arn:aws:sagemaker:*:{{producer-account-id}}:model-package/{{model-package-group}}/*"
        },
        "StringEquals": {
          "aws:PrincipalOrgID": "{{o-organization-id}}",
          "aws:PrincipalTag/ManagedBy": "SageMaker"
        }
      }
    },
    {
      "Sid": "AllowModelPackageRegistrationReads",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{registering-account-id}}:role/{{model-registration-role}}"
      },
      "Action": [ "s3:GetObject", "s3:ListBucket" ],
      "Resource": [
        "arn:aws:s3:::{{model-artifacts-bucket}}",
        "arn:aws:s3:::{{model-artifacts-bucket}}/{{model-package-prefix}}/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "{{o-organization-id}}"
        }
      }
    }
  ]
}
```

`AllowModelPackageRegistrationReads` is required. `CreateModelPackage` reads the artifact to validate it, and at that point the model package does not exist yet, so no `sagemaker:ModelPackageArn` session tag can be present. Without this statement, the first statement denies registration, and you cannot create the model package at all. Set {{model-registration-role}} to the role that calls `CreateModelPackage`, and keep it scoped to that role rather than to the whole account.

Using `Principal` with a value of `*` together with these conditions means any role in your organization can read the artifacts, provided it is tagged `ManagedBy=SageMaker` and carries the session tag. You do not have to edit the policy for each consuming role. The wildcard on the model package ARN covers every version in the group.

To allow more than one model package group, add one statement per group. Pair that group's ARN pattern with that group's artifact prefix. The condition also accepts a list of ARN patterns in a single statement. Use that form only when the groups are meant to share the same artifacts, because a single statement grants every pattern it lists access to everything its `Resource` covers.

Artifacts from more than one producer account need the same treatment: one pattern per account, because the tag value carries the account that owns the model package.

**Important**  
Do not put a wildcard immediately after a version number. A pattern ending `model-package/{{model-package-group}}/1*` also matches versions 10, 11, and 19. To restrict access to a single version, end the pattern at the version and omit the wildcard. An over-broad pattern is not visible from the endpoint or the model package, because deployments succeed either way.

**Important**  
Scope `Resource` to the artifacts of a single model package group. A prefix spanning several groups would let a deployment of one model package read another group's artifacts. The session tag is checked against the group wildcard rather than the object path.

If the artifacts are encrypted with a customer managed AWS KMS key, the execution role also needs `kms:Decrypt` on that key. Because the key and the role are in different accounts, grant it in both places: the key policy in the producing account must allow the execution role, and the execution role's IAM policy must allow `kms:Decrypt` on the key. Either grant alone is not sufficient.

## Monitor artifact access
<a name="model-registry-restrict-s3-access-monitor"></a>

Your account records both the tagging of the session and the resulting access decision.
+ In CloudTrail, the `AssumeRole` event for the execution role lists the session tags under `requestParameters`. Confirm that at least one event carries `sagemaker:ModelPackageArn` and that its value matches the model package you deployed. A single deployment also produces *untagged* `AssumeRole` events, because SageMaker AI validates the artifact before the tagged session is created. Untagged events alongside a tagged one are expected and do not mean the tag was not applied.
+ In Amazon S3 data events or server access logs, `GetObject` requests against the artifact prefix show whether each read was allowed or denied, so you can confirm that access from outside a model package endpoint is being refused. A successful deployment also produces a denied `GetObject` from SageMaker AI, because SageMaker AI validates the artifact with an untagged session before the tagged session is created. This denial is expected and does not stop the deployment.

Before applying the policies to a production bucket, you can evaluate them with the IAM policy simulator to confirm that a deployment session is allowed and that a session without the tag is denied. The simulator evaluates your policy against context keys that you supply, so it confirms the policy logic but not that a deployment actually produces the tag. Confirm that separately in CloudTrail, as described earlier in this section. For more information, see [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html).