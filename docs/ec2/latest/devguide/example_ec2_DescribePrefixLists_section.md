

# Use `DescribePrefixLists` with a CLI
<a name="example_ec2_DescribePrefixLists_section"></a>

The following code examples show how to use `DescribePrefixLists`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Virtual private network with private servers](example_vpc_GettingStartedPrivate_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To describe prefix lists**  
This example lists all available prefix lists for the region.  
Command:  

```
aws ec2 describe-prefix-lists
```
Output:  

```
{
  "PrefixLists": [
    {
      "PrefixListName": "com.amazonaws.us-east-1.s3",
      "Cidrs": [
        "54.231.0.0/17"
      ],
      "PrefixListId": "pl-63a5400a"
    }
  ]
}
```
+  For API details, see [DescribePrefixLists](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-prefix-lists.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example fetches the available AWS services in a prefix list format for the region**  

```
Get-EC2PrefixList
```
**Output:**  

```
Cidrs                                          PrefixListId PrefixListName
-----                                          ------------ --------------
{52.94.5.0/24, 52.119.240.0/21, 52.94.24.0/23} pl-6fa54006  com.amazonaws.eu-west-1.dynamodb
{52.218.0.0/17, 54.231.128.0/19}               pl-6da54004  com.amazonaws.eu-west-1.s3
```
+  For API details, see [DescribePrefixLists](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example fetches the available AWS services in a prefix list format for the region**  

```
Get-EC2PrefixList
```
**Output:**  

```
Cidrs                                          PrefixListId PrefixListName
-----                                          ------------ --------------
{52.94.5.0/24, 52.119.240.0/21, 52.94.24.0/23} pl-6fa54006  com.amazonaws.eu-west-1.dynamodb
{52.218.0.0/17, 54.231.128.0/19}               pl-6da54004  com.amazonaws.eu-west-1.s3
```
+  For API details, see [DescribePrefixLists](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.