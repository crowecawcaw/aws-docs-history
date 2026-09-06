

# Use `DescribeConfigurationRecorders` with a CLI
<a name="example_config-service_DescribeConfigurationRecorders_section"></a>

The following code examples show how to use `DescribeConfigurationRecorders`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Getting started with configuration management](example_config_service_GettingStarted_053_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To get details about the configuration recorder**  
The following command returns details about the default configuration recorder:  

```
aws configservice describe-configuration-recorders
```
Output:  

```
{
    "ConfigurationRecorders": [
        {
            "recordingGroup": {
                "allSupported": true,
                "resourceTypes": [],
                "includeGlobalResourceTypes": true
            },
            "roleARN": "arn:aws:iam::123456789012:role/config-ConfigRole-A1B2C3D4E5F6",
            "name": "default"
        }
    ]
}
```
+  For API details, see [DescribeConfigurationRecorders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorders.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example returns the details of configuration recorders.**  

```
Get-CFGConfigurationRecorder | Format-List
```
**Output:**  

```
Name           : default
RecordingGroup : Amazon.ConfigService.Model.RecordingGroup
RoleARN        : arn:aws:iam::123456789012:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig
```
+  For API details, see [DescribeConfigurationRecorders](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example returns the details of configuration recorders.**  

```
Get-CFGConfigurationRecorder | Format-List
```
**Output:**  

```
Name           : default
RecordingGroup : Amazon.ConfigService.Model.RecordingGroup
RoleARN        : arn:aws:iam::123456789012:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig
```
+  For API details, see [DescribeConfigurationRecorders](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Config with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.