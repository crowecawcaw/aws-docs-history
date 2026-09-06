

# Use `DescribeConfigurationRecorderStatus` with a CLI
<a name="example_config-service_DescribeConfigurationRecorderStatus_section"></a>

The following code examples show how to use `DescribeConfigurationRecorderStatus`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Getting started with configuration management](example_config_service_GettingStarted_053_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To get status information for the configuration recorder**  
The following command returns the status of the default configuration recorder:  

```
aws configservice describe-configuration-recorder-status
```
Output:  

```
{
    "ConfigurationRecordersStatus": [
        {
            "name": "default",
            "lastStatus": "SUCCESS",
            "recording": true,
            "lastStatusChangeTime": 1452193834.344,
            "lastStartTime": 1441039997.819,
            "lastStopTime": 1441039992.835
        }
    ]
}
```
+  For API details, see [DescribeConfigurationRecorderStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorder-status.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This sample returns status of the configuration recorders. **  

```
Get-CFGConfigurationRecorderStatus
```
**Output:**  

```
LastErrorCode        :
LastErrorMessage     :
LastStartTime        : 10/11/2019 10:13:51 AM
LastStatus           : Success
LastStatusChangeTime : 12/31/2019 6:14:12 AM
LastStopTime         : 10/11/2019 10:13:46 AM
Name                 : default
Recording            : True
```
+  For API details, see [DescribeConfigurationRecorderStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This sample returns status of the configuration recorders. **  

```
Get-CFGConfigurationRecorderStatus
```
**Output:**  

```
LastErrorCode        :
LastErrorMessage     :
LastStartTime        : 10/11/2019 10:13:51 AM
LastStatus           : Success
LastStatusChangeTime : 12/31/2019 6:14:12 AM
LastStopTime         : 10/11/2019 10:13:46 AM
Name                 : default
Recording            : True
```
+  For API details, see [DescribeConfigurationRecorderStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Config with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.