

# Amazon Inspector deep inspection for Linux-based Amazon EC2 instances
<a name="deep-inspection"></a>

**Note**  
This page applies to customers that have not opted in to Enhanced EC2 Scanning. Customers opted into Enhanced EC2 Scanning do not need any additional policy configuration.

 Amazon Inspector expands Amazon EC2 scanning coverage to include deep inspection. With deep inspection, Amazon Inspector detects package vulnerabilities for application programming language packages in your Linux-based Amazon EC2 instances. Amazon Inspector scans default paths for programming language package libraries. However, you can [configure custom paths](https://docs.aws.amazon.com/inspector/latest/user/deep-inspection.html#deep-inspection-paths) in addition to the paths that Amazon Inspector scans by default. 

**Note**  
 Deep inspection requires `ssm:PutInventory` and `ssm:GetParameter` permissions. If an IAM instance profile is configured on the instance, Amazon Inspector uses that profile and ignores the DHMC role. The instance profile must include these permissions. If no instance profile is set, Amazon Inspector uses the configured [Default Host Management Configuration](https://docs.aws.amazon.com/systems-manager/latest/userguide/managed-instances-default-host-management.html) role, which must include these permissions. 

 To perform deep inspection scans for your Linux-based Amazon EC2 instances, Amazon Inspector uses data collected with the Amazon Inspector SSM plugin. To manage the Amazon Inspector SSM plugin and perform deep inspection for Linux, Amazon Inspector automatically creates the SSM association `InvokeInspectorLinuxSsmPlugin-do-not-delete` in your account. Amazon Inspector collects updated application inventory from your Linux-based Amazon EC2 instances every 6 hours. 

**Deep inspection on Windows and macOS**  
 Deep inspection is not supported for Windows or Mac instances unless you use Enhanced EC2 Scanning. With Enhanced EC2 Scanning, deep inspection is performed by the [Amazon Inspector VM Scanner](https://docs.aws.amazon.com/inspector/latest/user/inspector-vm-scanner.html), which supports Linux, Windows, and macOS instances. 

 This section describes how to manage Amazon Inspector deep inspection for Amazon EC2 instances, including how to set custom paths for Amazon Inspector to scan. 

**Topics**
+ [Accessing or deactivating deep inspection](#deep-inspection-activate)
+ [Custom paths for Amazon Inspector deep inspection](#deep-inspection-paths)
+ [Custom schedules for Amazon Inspector deep inspection](#deep-inspection-schedules)
+ [Supported programming languages](#supported-deep-inspection)

## Accessing or deactivating deep inspection
<a name="deep-inspection-activate"></a>

**Note**  
 For accounts that activate Amazon Inspector after April 17, 2023, deep inspection is automatically activated as part of Amazon EC2 scanning. 

**To manage deep inspection**

1.  Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home) 

1.  From the navigation pane, choose **General settings**, and then choose Amazon EC2 scanning settings. 

1.  Under **Deep inspection of Amazon EC2 instance**, you can [set custom paths for your organization or for your own account](https://docs.aws.amazon.com/inspector/latest/user/deep-inspection.html#deep-inspection-paths). 

 You can check the activation status programmatically for a single account with the [GetEc2DeepInspectionConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetEc2DeepInspectionConfiguration.html) API. You can check the activation status programmatically for multiple accounts with the [BatchGetMemberEc2DeepInspectionStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html) API. 

 If you activated Amazon Inspector before April 17, 2023, you can activate deep inspection through the console banner or the [UpdateEc2DeepInspectionConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.html) API. If you're the delegated administrator for an organization in Amazon Inspector, you can use the [BatchUpdateMemberEc2DeepInspectionStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html) API to activate deep inspection for yourself and your member accounts. 

 You can deactivate deep inspection through the [UpdateEc2DeepInspectionConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.html) API. Member accounts in an organization can't deactivate deep inspection. Instead, the member account must be deactivated by their delegated administrator using the [BatchUpdateMemberEc2DeepInspectionStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html) API. 

## Custom paths for Amazon Inspector deep inspection
<a name="deep-inspection-paths"></a>

 You can set custom paths for Amazon Inspector to scan during deep inspection of your Amazon EC2 instances. When you set a custom path, Amazon Inspector scans packages in that directory and all of the sub-directories in it, in addition to the locations Amazon Inspector scans by default. 

**Important**  
 Custom paths are supported for Linux, Windows, and macOS instances when you use [Enhanced EC2 Scanning](https://docs.aws.amazon.com/inspector/latest/user/inspector-vm-scanner.html) (the Amazon Inspector VM Scanner). If you use the legacy Amazon Inspector SSM plugin instead of Enhanced EC2 Scanning, deep inspection and custom paths are available only for Linux instances. 

 All accounts can define up to 5 custom paths. The delegated administrator for an organization can define 10 custom paths. 

 Amazon Inspector scans all custom paths in addition to the locations that Amazon Inspector scans by default for all accounts. On Linux instances, the default locations include the following: 
+ `/usr/lib`
+ `/usr/lib64`
+ `/usr/local/lib`
+ `/usr/local/lib64`

 On Windows instances, Amazon Inspector scans standard operating system and programming language package locations on the system drive by default. Software installed in a custom or non-standard location – for example, a database or application server on a non-system drive such as `D:\` – is scanned only if you add it as a custom path. 

**Note**  
 Custom paths must be local paths. Amazon Inspector doesn't scan mapped network paths, such as Network File System mounts or Amazon S3 file system mounts. 

### Formatting custom paths
<a name="deep-inspection-paths-format"></a>

 A custom path cannot be longer than 256 characters. The following is an example of how a custom path might look: 

**Example path**  
 `/home/usr1/project01` 

**Note**  
 The package limit per instance is 5,000. The maximum package inventory collection time is 15 minutes. Amazon Inspector recommends that you choose custom paths to avoid these limits. 

### Setting a custom path in the Amazon Inspector console and with the Amazon Inspector API
<a name="deep-inspection-add-paths"></a>

 The following procedures describe how to set a custom path for Amazon Inspector deep inspection in the Amazon Inspector console and with the Amazon Inspector API. After you set a custom path, Amazon Inspector includes the path in the next deep inspection. 

------
#### [ Console ]

1.  Sign in to the AWS Management Console as the delegated administrator, and open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home) 

1.  Use the AWS Region selector to choose the Region where you want to activate Lambda standard scanning. 

1.  From the navigation pane, choose **General settings**, and then choose **EC2 scanning settings**. 

1.  Under **Custom paths for your own account**, choose **Edit**. 

1.  In the path text boxes, enter your custom paths. 

1.  Choose **Save**. 

------
#### [ API ]

 Run the [UpdateEc2DeepInspectionConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.html) command. For `packagePaths` specify an array of paths to scan. 

------

## Custom schedules for Amazon Inspector deep inspection
<a name="deep-inspection-schedules"></a>

 By default, Amazon Inspector collects an application inventory from Amazon EC2 instances every 6 hours. However, you can run the following commands to control how often Amazon Inspector does this. 

 **Example command 1: List associations to view association ID and current interval ** 

 The following command shows the association ID for the association `InvokeInspectorLinuxSsmPlugin-do-not-delete`. 

```
aws ssm list-associations \
--association-filter-list "key=AssociationName,value=InvokeInspectorLinuxSsmPlugin-do-not-delete" \
--region {{your-Region}}
```

 **Example command 2: Update association to include new interval** 

 The following command uses the association ID for the association `InvokeInspectorLinuxSsmPlugin-do-not-delete`. You can set the rate for `schedule-expression` from 6 hours to a new interval, such as 12 hours. 

```
aws ssm update-association \
--association-id "{{your-association-ID}}" \
--association-name "InvokeInspectorLinuxSsmPlugin-do-not-delete" \
--schedule-expression "rate({{6}} hours)" \
--region {{your-Region}}
```

**Note**  
 Depending on your use case, if you set the rate for `schedule-expression` from 6 hours to an interval like 30 minutes, you can [exceed the daily ssm inventory limit](https://docs.aws.amazon.com/inspector/latest/user/assessing-coverage.html#viewing-coverage-instances). This causes results to be delayed, and you might encounter Amazon EC2 instances with partial error statuses. 

## Supported programming languages
<a name="supported-deep-inspection"></a>

 For Linux instances, Amazon Inspector deep inspection can produce findings for application programming language packages and operating system packages. 

 For Mac and Windows instances, Amazon Inspector deep inspection can produce findings only for operating system packages. 

 For more information about supported programming languages, see [Supported programming languages: Amazon EC2 deep inspection](https://docs.aws.amazon.com/inspector/latest/user/supported.html#supported-programming-languages-deep-inspection). 