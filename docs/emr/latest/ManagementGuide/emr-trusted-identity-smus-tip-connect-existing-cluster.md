# Connect existing Amazon EMR on EC2 clusters to Amazon SageMaker Unified Studio

To integrate an existing TIP-enabled Amazon EMR on EC2 cluster with Amazon SageMaker Unified Studio, complete the following prerequisites. For additional details, see:

- [Adding existing Amazon EMR on EC2 clusters](../../../sagemaker-unified-studio/latest/userguide/adding-existing-emr-on-ec2-clusters.md "../../../sagemaker-unified-studio/latest/userguide/adding-existing-emr-on-ec2-clusters.md")
- [Configuring TIP for Amazon EMR on EC2](../../../sagemaker-unified-studio/latest/userguide/emr-ec2-configuring-tip.md "../../../sagemaker-unified-studio/latest/userguide/emr-ec2-configuring-tip.md")
- [Enable Amazon EMR on EC2 blueprint](../../../sagemaker-unified-studio/latest/adminguide/enable-emr-on-ec2-blueprint.md "../../../sagemaker-unified-studio/latest/adminguide/enable-emr-on-ec2-blueprint.md")

## Step 1: Create an access role for Amazon EMR

Create an IAM role (for example, `EMRAccessRole`) that Amazon SageMaker Unified Studio will use to connect to the Amazon EMR on EC2 cluster. This must be done by the Amazon EMR administrator.

**Inline policy:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EmrAccess",
            "Effect": "Allow",
            "Action": [
                "elasticmapreduce:ListInstances",
                "elasticmapreduce:DescribeCluster",
                "elasticmapreduce:GetClusterSessionCredentials"
            ],
            "Resource": "arn:aws:elasticmapreduce:`region`:`account-id`:cluster/`cluster-id`"
        },
        {
            "Sid": "EMRSelfSignedCertAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::`bucket-location`/my-certs.zip"
            ]
        },
        {
            "Sid": "EMRSecurityConfigurationAccess",
            "Effect": "Allow",
            "Action": [
                "elasticmapreduce:DescribeSecurityConfiguration"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

###### Note

The `EMRSelfSignedCertAccess` statement can be omitted if your certificate is signed by a trusted CA.

**Trust policy:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`account-id`:role/`ProjectRoleName`"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "`project-id`"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`account-id`:role/`ProjectRoleName`"
            },
            "Action": [
                "sts:SetSourceIdentity",
                "sts:TagSession",
                "sts:SetContext"
            ]
        }
    ]
}
```

Where `ProjectRoleName` follows the pattern `datazone_usr_role_<ProjectId>_<ToolingBPenvironmentId>`.

## Step 2: Update the Amazon EMR instance profile role

Add the following inline policy to the EC2 instance profile role on the Amazon EMR on EC2 cluster (as per [Configuring TIP for Amazon EMR on EC2](../../../sagemaker-unified-studio/latest/userguide/emr-ec2-configuring-tip.md "../../../sagemaker-unified-studio/latest/userguide/emr-ec2-configuring-tip.md")):

```
{
    "Statement": [
        {
            "Sid": "IdCPermissions",
            "Effect": "Allow",
            "Action": [
                "sso-oauth:CreateTokenWithIAM",
                "sso-oauth:IntrospectTokenWithIAM",
                "sso-oauth:RevokeTokenWithIAM"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowAssumeRole",
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": [
                "`instance-profile-role-ARN`"
            ]
        }
    ]
}
```

**Managed policies:** Attach the following AWS managed policies (or equivalent permissions) to the instance profile role:

- `AmazonElasticMapReduceforEC2Role`
- `AmazonSSMManagedInstanceCore`
- `AWSGlueServiceRole` (or equivalent AWS Glue permissions, `glue:*`)

## Step 3: Enable user-governed Amazon EMR clusters in the blueprint

The Amazon SageMaker Unified Studio admin must set `allowConnectionToUserGovernedEmrClusters` to `true` in the tooling configurations of the blueprint for the project profile.

###### Note

The default value of `allowConnectionToUserGovernedEmrClusters` corresponds to an Amazon EMR release below 7.8.0. Because Amazon SageMaker Unified Studio integration with trusted identity propagation requires Amazon EMR 7.8.0 or later, you must explicitly set this parameter to `true`.

## Step 4: Associate the Amazon EMR security configuration IAM Identity Center instance with Lake Formation

For each Amazon EMR security configuration, the AWS IAM Identity Center (IAM Identity Center) instance must be associated with the Lake Formation IAM Identity Center integration. In the Lake Formation console, under **Administration** > **Application integration**, confirm that the same IAM Identity Center instance referenced by the security configuration is associated with the Lake Formation IAM Identity Center integration.

## Step 5: Add the Amazon EMR managed policies tag at cluster launch

The `for-use-with-amazon-emr-managed-policies=true` tag must be present at Amazon EMR on EC2 cluster launch. Add this tag when you create the cluster so that the Amazon EMR managed policies apply to the cluster resources.

## Step 6: Grant the project role access to Amazon EMR logs and bootstrap actions

The project role (`datazone_usr_role_<ProjectId>_<EnvId>`) needs access to the Amazon Simple Storage Service locations used for Amazon EMR logs and any bootstrap actions. Add a policy that grants read access to the bootstrap action Amazon S3 location and read/write access to the Amazon EMR log Amazon S3 location:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EmrLogsAndBootstrapAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::`emr-logs-bucket`",
                "arn:aws:s3:::`emr-logs-bucket`/*",
                "arn:aws:s3:::`bootstrap-action-bucket`",
                "arn:aws:s3:::`bootstrap-action-bucket`/*"
            ]
        }
    ]
}
```

## Step 7: Configure the certificate location

Copy the certificate used in the Amazon EMR security configuration to the Amazon SageMaker Unified Studio domain bucket:

```
s3://`DomainBucketName`/`AmazonDataZoneDomainID`/certificate_location/`certs.zip`
```

Under the Blueprint parameters section, edit the `certificateLocation` parameter. Enter the Amazon S3 location of the ZIP file containing PEM certificate file(s) using the format: `s3://<DomainBucketName>/<AmazonDataZoneDomainID>/certificate_location/`.

## Step 8: Configure Amazon EMR cluster software settings

When launching the Amazon EMR on EC2 cluster, provide the following configuration in the software settings:

```
[
  {
    "Classification": "livy-conf",
    "Properties": {
      "livy.support.s3-lib-mgmt": "true"
    }
  },
  {
    "Classification": "iceberg-defaults",
    "Properties": {
      "iceberg.enabled": "true"
    }
  },
  {
    "Classification": "emrfs-site",
    "Properties": {
      "fs.s3.s3AccessGrants.enabled": "true",
      "fs.s3.s3AccessGrants.fallbackToIAM": "true"
    }
  }
]
```

## Step 9: Configure networking

Configure network access between the Amazon SageMaker Unified Studio project and the Amazon EMR on EC2 cluster. The Amazon SageMaker Unified Studio project has a security group associated with its project environment. You open the Livy port on the Amazon EMR primary node to that security group and add an interface VPC endpoint for Amazon EMR to the Amazon SageMaker Unified Studio VPC.

1. **Find the Amazon SageMaker Unified Studio project security group.** Each Amazon SageMaker Unified Studio project environment has a `securityGroup` resource. Retrieve it from the project's Tooling environment. First, list the environments for your project to get the environment ID, then read the `securityGroup` provisioned resource:

```
aws datazone list-environments \
    --domain-identifier `domain-id` \
    --project-identifier `project-id` \
    --query "items[?name=='Tooling'].id" --output text

aws datazone get-environment \
    --domain-identifier `domain-id` \
    --identifier `environment-id` \
    --query "provisionedResources[?name=='securityGroup'].value" --output text
```

The returned value (for example, `sg-`0abc123smus``) is the Amazon SageMaker Unified Studio domain security group used in the following steps. 2. **Open the Livy port (8998) on the Amazon EMR primary node.** Add an ingress rule to the Amazon EMR primary node security group that allows TCP port `8998` from the Amazon SageMaker Unified Studio project security group:

```
aws ec2 authorize-security-group-ingress \
    --group-id `emr-primary-node-sg-id` \
    --protocol tcp \
    --port 8998 \
    --source-group `smus-project-sg-id`
```

Replace `emr-primary-node-sg-id` with the Amazon EMR managed primary (main) node security group and `smus-project-sg-id` with the Amazon SageMaker Unified Studio project security group from the previous step. 3. **Add the Amazon EMR interface VPC endpoint to the Amazon SageMaker Unified Studio VPC.** Create an interface endpoint for `com.amazonaws.`region`.elasticmapreduce` in the Amazon SageMaker Unified Studio VPC private subnet, associated with the Amazon SageMaker Unified Studio project security group:

```
aws ec2 create-vpc-endpoint \
    --vpc-id `smus-vpc-id` \
    --vpc-endpoint-type Interface \
    --service-name com.amazonaws.`region`.elasticmapreduce \
    --subnet-ids `smus-private-subnet-id` \
    --security-group-ids `smus-project-sg-id` \
    --private-dns-enabled
```

With `--private-dns-enabled`, requests to `elasticmapreduce.`region`.amazonaws.com` from the Amazon SageMaker Unified Studio VPC resolve to the interface endpoint.
