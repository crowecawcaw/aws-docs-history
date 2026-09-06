

# Use `DescribeIdentityIdFormat` with a CLI
<a name="example_ec2_DescribeIdentityIdFormat_section"></a>

The following code examples show how to use `DescribeIdentityIdFormat`.

------
#### [ CLI ]

**AWS CLI**  
**To describe the ID format for an IAM role**  
The following `describe-identity-id-format` example describes the ID format received by instances created by the IAM role `EC2Role` in your AWS account.  

```
aws ec2 describe-identity-id-format \
    --principal-arn {{arn:aws:iam::123456789012:role/my-iam-role}} \
    --resource {{instance}}
```
The following output indicates that instances created by this role receive IDs in long ID format.  

```
{
    "Statuses": [
        {
            "Deadline": "2016-12-15T00:00:00Z",
            "Resource": "instance",
            "UseLongIds": true
        }
    ]
}
```
**To describe the ID format for an IAM user**  
The following `describe-identity-id-format` example describes the ID format received by snapshots created by the IAM user `AdminUser` in your AWS account.  

```
aws ec2 describe-identity-id-format \
    --principal-arn {{arn:aws:iam::123456789012:user/AdminUser}} \
    --resource {{snapshot}}
```
The output indicates that snapshots created by this user receive IDs in long ID format.  

```
{
    "Statuses": [
        {
            "Deadline": "2016-12-15T00:00:00Z",
            "Resource": "snapshot",
            "UseLongIds": true
        }
    ]
}
```
+  For API details, see [DescribeIdentityIdFormat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-identity-id-format.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example returns the ID format for the resouce 'image' for the role given**  

```
Get-EC2IdentityIdFormat -PrincipalArn arn:aws:iam::123456789511:role/JDBC -Resource image
```
**Output:**  

```
Deadline             Resource UseLongIds
--------             -------- ----------
8/2/2018 11:30:00 PM image    True
```
+  For API details, see [DescribeIdentityIdFormat](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example returns the ID format for the resouce 'image' for the role given**  

```
Get-EC2IdentityIdFormat -PrincipalArn arn:aws:iam::123456789511:role/JDBC -Resource image
```
**Output:**  

```
Deadline             Resource UseLongIds
--------             -------- ----------
8/2/2018 11:30:00 PM image    True
```
+  For API details, see [DescribeIdentityIdFormat](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.