

# Use `DescribeIdFormat` with a CLI
<a name="example_ec2_DescribeIdFormat_section"></a>

The following code examples show how to use `DescribeIdFormat`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To describe the ID format of a resource**  
The following `describe-id-format` example describes the ID format for security groups.  

```
aws ec2 describe-id-format \
    --resource {{security-group}}
```
In the following example output, the `Deadline` value indicates that the deadline for this resource type to permanently switch from the short ID format to the long ID format expired at 00:00 UTC on August 15, 2018.  

```
{
    "Statuses": [
        {
            "Deadline": "2018-08-15T00:00:00.000Z",
            "Resource": "security-group",
            "UseLongIds": true
        }
    ]
}
```
**Example 2: To describe the ID format for all resources**  
The following `describe-id-format` example describes the ID format for all resource types. All resource types that supported the short ID format were switched to use the long ID format.  

```
aws ec2 describe-id-format
```
+  For API details, see [DescribeIdFormat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-id-format.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example describes the ID format for the specified resource type.**  

```
Get-EC2IdFormat -Resource instance
```
**Output:**  

```
Resource       UseLongIds
--------       ----------
instance       False
```
**Example 2: This example describes the ID formats for all resource types that support longer IDs.**  

```
Get-EC2IdFormat
```
**Output:**  

```
Resource       UseLongIds
--------       ----------
reservation    False
instance       False
```
+  For API details, see [DescribeIdFormat](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example describes the ID format for the specified resource type.**  

```
Get-EC2IdFormat -Resource instance
```
**Output:**  

```
Resource       UseLongIds
--------       ----------
instance       False
```
**Example 2: This example describes the ID formats for all resource types that support longer IDs.**  

```
Get-EC2IdFormat
```
**Output:**  

```
Resource       UseLongIds
--------       ----------
reservation    False
instance       False
```
+  For API details, see [DescribeIdFormat](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.