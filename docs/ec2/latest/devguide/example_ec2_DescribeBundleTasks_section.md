

# Use `DescribeBundleTasks` with a CLI
<a name="example_ec2_DescribeBundleTasks_section"></a>

The following code examples show how to use `DescribeBundleTasks`.

------
#### [ CLI ]

**AWS CLI**  
**To describe your bundle tasks**  
This example describes all of your bundle tasks.  
Command:  

```
aws ec2 describe-bundle-tasks
```
Output:  

```
{
  "BundleTasks": [
    {
      "UpdateTime": "2015-09-15T13:26:54.000Z",
      "InstanceId": "i-1234567890abcdef0",
      "Storage": {
        "S3": {
            "Prefix": "winami",
            "Bucket": "bundletasks"
        }
      },
      "State": "bundling",
      "StartTime": "2015-09-15T13:24:35.000Z",
      "Progress": "3%",
      "BundleId": "bun-2a4e041c"
    }
  ]
}
```
+  For API details, see [DescribeBundleTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-bundle-tasks.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example describes the specified bundle task.**  

```
Get-EC2BundleTask -BundleId bun-12345678
```
**Example 2: This example describes the bundle tasks whose state is either 'complete' or 'failed'.**  

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "complete", "failed" )

Get-EC2BundleTask -Filter $filter
```
+  For API details, see [DescribeBundleTasks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example describes the specified bundle task.**  

```
Get-EC2BundleTask -BundleId bun-12345678
```
**Example 2: This example describes the bundle tasks whose state is either 'complete' or 'failed'.**  

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "complete", "failed" )

Get-EC2BundleTask -Filter $filter
```
+  For API details, see [DescribeBundleTasks](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.