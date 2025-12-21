# AwsEks resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsEks` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsEksCluster

The `AwsEksCluster` object provides details about an Amazon EKS cluster.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEksCluster` object. To view descriptions of
`AwsEksCluster` attributes, see [AwsEksClusterDetails](../../1.0/APIReference/API_AwsEksClusterDetails.md "../../1.0/APIReference/API_AwsEksClusterDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
{
  "AwsEksCluster": {
    "Name": "example",
    "Arn": "arn:aws:eks:us-west-2:222222222222:cluster/example",
    "CreatedAt": 1565804921.901,
    "Version": "1.12",
    "RoleArn": "arn:aws:iam::222222222222:role/example-cluster-ServiceRole-1XWBQWYSFRE2Q",
    "ResourcesVpcConfig": {
      "EndpointPublicAccess": false,
      "SubnetIds": [
        "subnet-021345abcdef6789",
        "subnet-abcdef01234567890",
        "subnet-1234567890abcdef0"
      ],
      "SecurityGroupIds": [
        "sg-abcdef01234567890"
      ]
    },
    "Logging": {
      "ClusterLogging": [
        {
          "Types": [
            "api",
            "audit",
            "authenticator",
            "controllerManager",
            "scheduler"
          ],
          "Enabled": true
        }
      ]
    },
    "Status": "CREATING",
    "CertificateAuthorityData": {},
  }
}
```
