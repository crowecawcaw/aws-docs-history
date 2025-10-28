# Use `CreateInternetGateway` with a CLI

The following code examples show how to use `CreateInternetGateway`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Create a VPC with private subnets and NAT gateways](example_vpc_GettingStartedPrivate_section.md "example_vpc_GettingStartedPrivate_section.md")
- [Get started with Amazon VPC](example_vpc_GettingStartedCLI_section.md "example_vpc_GettingStartedCLI_section.md")

CLI

**AWS CLI**

**To create an internet gateway**

The following `create-internet-gateway` example creates an internet gateway with the tag `Name=my-igw`.

```
`aws ec2 create-internet-gateway \
 --tag-specifications `ResourceType=internet-gateway,Tags=[{Key=Name,Value=my-igw}]``

```

Output:

```
{
    "InternetGateway": {
        "Attachments": [],
        "InternetGatewayId": "igw-0d0fb496b3994d755",
        "OwnerId": "123456789012",
        "Tags": [
            {
                "Key": "Name",
                "Value": "my-igw"
            }
        ]
    }
}
```

For more information, see [Internet gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the _Amazon VPC User Guide_.

- For API details, see
  [CreateInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-internet-gateway.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-internet-gateway.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates an Internet gateway.**

```
New-EC2InternetGateway

```

**Output:**

```
Attachments    InternetGatewayId    Tags
-----------    -----------------    ----
{}             igw-1a2b3c4d         {}
```

- For API details, see
  [CreateInternetGateway](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates an Internet gateway.**

```
New-EC2InternetGateway

```

**Output:**

```
Attachments    InternetGatewayId    Tags
-----------    -----------------    ----
{}             igw-1a2b3c4d         {}
```

- For API details, see
  [CreateInternetGateway](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
