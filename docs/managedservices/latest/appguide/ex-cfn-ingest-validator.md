# CloudFormation ingest stack: CFN validator examples

These examples can help you prepare your template for a successful ingest.

## Format validation

Validate that the template contains a "Resources" section, and all resources defined under it have a
"Type" value.

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description" : "Create a SNS topic",
  "Resources": {
    "SnsTopic": {
      "**Type**": "AWS::SNS::Topic"
    }
  }
}
```

Validate that the root keys of the template are allowed. Allowed root keys are:

```
[
  "AWSTemplateFormatVersion",
  "Description",
  "Mappings",
  "Parameters",
  "Conditions",
  "Resources",
  "Rules",
  "Outputs",
  "Metadata"
]
```

## Manual Managed Automation validation

If the template contains the following resources, automatic validation fails and you'll need a manual review.

The shown policies are high risk areas from a security standpoint. For example, an S3 bucket policy
allowing anyone except for specific users or groups to create objects or write permissions, is
extremely dangerous. So we validate the policies and approve or deny based on the contents, and those
polices cannot be auto-created. We are investigating possible approaches to address this issue.

We currently don’t have automated validation around the following resources.

```
[
    "S3::BucketPolicy",
    "SNS::TopicPolicy",
    "SQS::QueuePolicy"
]
```

## Parameter validation

Validate that if a template parameter doesn't have a value provided; it must
have a default value.

## Resource attribute validation

Required attribute check: Certain attributes must exist for certain resource types.

- "VPCOptions" must exist in `AWS::OpenSearch::Domain`
- "CludsterSubnetGroupName" must exist in `AWS::Redshift::Cluster`

```
{
    "AWS::OpenSearch::Domain": [
      "VPCOptions"
    ],
    "AWS::Redshift::Cluster": [
      "ClusterSubnetGroupName"
    ]
}
```

Disallowed attributes check: Certain attributes must \*not\* exist for certain resource types.

- "SecretString" must not exist in "AWS::SecretsManager::Secret"
- "MongoDbSettings" must not exist in "AWS::DMS::Endpoint"

```
{
  "AWS::SecretsManager::Secret": [
    "SecretString"
  ],
  "AWS::DMS::Endpoint": [
    "MongoDbSettings"
  ]
}
```

SSM parameter check: For attributes in the following list, values must be specified via Secrets
Manager or Systems Manager Parameter Store (Secure String Parameter):

```
{
  "RDS::DBInstance": [
    "MasterUserPassword",
    "TdeCredentialPassword"
  ],
  "RDS::DBCluster": [
    "MasterUserPassword"
  ],
  "ElastiCache::ReplicationGroup": [
    "AuthToken"
  ],
  "DMS::Certificate": [
    "CertificatePem",
    "CertificateWallet"
  ],
  "DMS::Endpoint": [
    "Password"
  ],
  "CodePipeline::Webhook": {
    "AuthenticationConfiguration": [
        "SecretToken"
    ]
  },
  "DocDB::DBCluster": [
    "MasterUserPassword"
  ]
},
```

Some attributes must comply with certain patterns; for example, IAM instance profile names must not start with
[AMS reserved prefixes](../userguide/ams-reserved-prefixes.md "../userguide/ams-reserved-prefixes.md"),
and the attribute value must match the specific regex as shown:

```
{
    "AWS::EC2::Instance": {
      "IamInstanceProfile": [
        "^(?!arn:aws:iam|ams|Ams|AMS|AWSManagedServices|Managed_Services|mc|Mc|MC|sentinel|Sentinel).+",
        "arn:aws:iam::(\\$\\{AWS::AccountId\\}|[0-9]+):instance-profile/(?!ams|Ams|AMS|AWSManagedServices|Managed_Services|mc|Mc|MC|sentinel|Sentinel).+"
      ]
    },
    "AWS::AutoScaling::LaunchConfiguration": {
      "IamInstanceProfile": [
        "^(?!arn:aws:iam|ams|Ams|AMS|AWSManagedServices|Managed_Services|mc|Mc|MC|sentinel|Sentinel).+",
        "arn:aws:iam::(\\$\\{AWS::AccountId\\}|[0-9]+):instance-profile/(?!ams|Ams|AMS|AWSManagedServices|Managed_Services|mc|Mc|MC|sentinel|Sentinel).+"
      ]
    },
    "AWS::EC2::LaunchTemplate": {
      "LaunchTemplateData.IamInstanceProfile.Name": [
        "^(?!ams|Ams|AMS|AWSManagedServices|Managed_Services|mc|Mc|MC|sentinel|Sentinel).+"
      ],
      "LaunchTemplateData.IamInstanceProfile.Arn": [
        "arn:aws:iam::(\\$\\{AWS::AccountId\\}|[0-9]+):instance-profile\/(?!ams|Ams|AMS|AWSManagedServices|Managed_Services|mc|Mc|MC|sentinel|Sentinel).+"
      ]
    }
}
```

## Resource validation

Only allowlisted resources can be specified in the template; those resources are described in
[Supported Resources](cfn-ingest-supp-services.md "cfn-ingest-supp-services.md").

EC2 stacks and Auto Scaling groups (ASGs) are not allowed in the same stack due to patching limitations.

## Security group ingress rule validation

- For requests that come from the CFN Ingest Create or Stack Update CT change types:
  - If (`IpProtocol` is tcp or 6) AND (Port is 80 or 443) , there are no
    restrictions around the `CidrIP` value
  - Otherwise, the `CidrIP` cannot be 0.0.0.0/0

- For requests that come from Service Catalog (Service Catalog products):
  - In addition to the CFN Ingest Create or Stack Update CT change type validation, the port in
    `management_ports` with the protocol in `ip_protocols` can only be
    accessed via `allowed_cidrs`:

  ```
  {
        "ip_protocols": ["tcp", "6", "udp", "17"],
        "management_ports": [22, 23, 389, 636, 1494, 1604, 2222, 3389, 5900, 5901, 5985, 5986],
        "allowed_cidrs": ["10.0.0.0/8", "100.64.0.0/10", "172.16.0.0/12", "192.168.0.0/16"]
    }
  ```
