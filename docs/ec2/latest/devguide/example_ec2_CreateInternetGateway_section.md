

# Use `CreateInternetGateway` with a CLI
<a name="example_ec2_CreateInternetGateway_section"></a>

The following code examples show how to use `CreateInternetGateway`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Create a basic virtual private network](example_vpc_GettingStartedCLI_section.md) 
+  [Getting started with graph databases](example_ec2_GettingStarted_064_section.md) 
+  [Virtual private network with private servers](example_vpc_GettingStartedPrivate_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To create an internet gateway**  
The following `create-internet-gateway` example creates an internet gateway with the tag `Name=my-igw`.  

```
aws ec2 create-internet-gateway \
    --tag-specifications {{ResourceType=internet-gateway,Tags=[{Key=Name,Value=my-igw}]}}
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
For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.  
+  For API details, see [CreateInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-internet-gateway.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

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
+  For API details, see [CreateInternetGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

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
+  For API details, see [CreateInternetGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.