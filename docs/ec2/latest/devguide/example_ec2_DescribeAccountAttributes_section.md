# Use `DescribeAccountAttributes` with a CLI

The following code examples show how to use `DescribeAccountAttributes`.

CLI

**AWS CLI**

**To describe all the attributes for your AWS account**

This example describes the attributes for your AWS account.

Command:

```
`aws ec2 describe-account-attributes`

```

Output:

```
{
    "AccountAttributes": [
        {
            "AttributeName": "vpc-max-security-groups-per-interface",
            "AttributeValues": [
                {
                    "AttributeValue": "5"
                }
            ]
        },
        {
            "AttributeName": "max-instances",
            "AttributeValues": [
                {
                    "AttributeValue": "20"
                }
            ]
        },
        {
            "AttributeName": "supported-platforms",
            "AttributeValues": [
                {
                    "AttributeValue": "EC2"
                },
                {
                    "AttributeValue": "VPC"
                }
            ]
        },
        {
            "AttributeName": "default-vpc",
            "AttributeValues": [
                {
                    "AttributeValue": "none"
                }
            ]
        },
        {
            "AttributeName": "max-elastic-ips",
            "AttributeValues": [
                {
                    "AttributeValue": "5"
                }
            ]
        },
        {
            "AttributeName": "vpc-max-elastic-ips",
            "AttributeValues": [
                {
                    "AttributeValue": "5"
                }
            ]
        }
    ]
}
```

**To describe a single attribute for your AWS account**

This example describes the `supported-platforms` attribute for your AWS account.

Command:

```
`aws ec2 describe-account-attributes --attribute-names `supported-platforms``

```

Output:

```
{
    "AccountAttributes": [
        {
            "AttributeName": "supported-platforms",
            "AttributeValues": [
                {
                    "AttributeValue": "EC2"
                },
                {
                    "AttributeValue": "VPC"
                }
            ]
        }
    ]
}
```

- For API details, see
  [DescribeAccountAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-account-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-account-attributes.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes whether you can launch instances into EC2-Classic and EC2-VPC in the region, or only into EC2-VPC.**

```
(Get-EC2AccountAttribute -AttributeName supported-platforms).AttributeValues

```

**Output:**

```
AttributeValue
--------------
EC2
VPC
```

**Example 2: This example describes your default VPC, or is 'none' if you do not have a default VPC in the region.**

```
(Get-EC2AccountAttribute -AttributeName default-vpc).AttributeValues

```

**Output:**

```
AttributeValue
--------------
vpc-12345678
```

**Example 3: This example describes the maximum number of On-Demand instances that you can run.**

```
(Get-EC2AccountAttribute -AttributeName max-instances).AttributeValues

```

**Output:**

```
AttributeValue
--------------
20
```

- For API details, see
  [DescribeAccountAttributes](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes whether you can launch instances into EC2-Classic and EC2-VPC in the region, or only into EC2-VPC.**

```
(Get-EC2AccountAttribute -AttributeName supported-platforms).AttributeValues

```

**Output:**

```
AttributeValue
--------------
EC2
VPC
```

**Example 2: This example describes your default VPC, or is 'none' if you do not have a default VPC in the region.**

```
(Get-EC2AccountAttribute -AttributeName default-vpc).AttributeValues

```

**Output:**

```
AttributeValue
--------------
vpc-12345678
```

**Example 3: This example describes the maximum number of On-Demand instances that you can run.**

```
(Get-EC2AccountAttribute -AttributeName max-instances).AttributeValues

```

**Output:**

```
AttributeValue
--------------
20
```

- For API details, see
  [DescribeAccountAttributes](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
