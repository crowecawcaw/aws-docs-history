

# Use `DescribeDeliveryChannels` with a CLI
<a name="example_config-service_DescribeDeliveryChannels_section"></a>

The following code examples show how to use `DescribeDeliveryChannels`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Getting started with configuration management](example_config_service_GettingStarted_053_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To get details about the delivery channel**  
The following command returns details about the delivery channel:  

```
aws configservice describe-delivery-channels
```
Output:  

```
{
    "DeliveryChannels": [
        {
            "snsTopicARN": "arn:aws:sns:us-east-1:123456789012:config-topic",
            "name": "default",
            "s3BucketName": "config-bucket-123456789012"
        }
    ]
}
```
+  For API details, see [DescribeDeliveryChannels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-delivery-channels.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example retrieves the delivery channel for the region and displays details.**  

```
Get-CFGDeliveryChannel -Region eu-west-1 | Select-Object Name, S3BucketName, S3KeyPrefix, @{N="DeliveryFrequency";E={$_.ConfigSnapshotDeliveryProperties.DeliveryFrequency}}
```
**Output:**  

```
Name    S3BucketName               S3KeyPrefix DeliveryFrequency
----    ------------               ----------- -----------------
default config-bucket-NA my          TwentyFour_Hours
```
+  For API details, see [DescribeDeliveryChannels](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example retrieves the delivery channel for the region and displays details.**  

```
Get-CFGDeliveryChannel -Region eu-west-1 | Select-Object Name, S3BucketName, S3KeyPrefix, @{N="DeliveryFrequency";E={$_.ConfigSnapshotDeliveryProperties.DeliveryFrequency}}
```
**Output:**  

```
Name    S3BucketName               S3KeyPrefix DeliveryFrequency
----    ------------               ----------- -----------------
default config-bucket-NA my          TwentyFour_Hours
```
+  For API details, see [DescribeDeliveryChannels](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Config with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.