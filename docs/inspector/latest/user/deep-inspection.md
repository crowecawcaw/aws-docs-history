# Amazon Inspector deep inspection for Linux-based Amazon EC2 instances

Amazon Inspector expands Amazon EC2 scanning coverage to include deep inspection.
With deep inspection, Amazon Inspector detects package vulnerabilities for application programming language packages in your Linux-based Amazon EC2 instances.
Amazon Inspector scans default paths for programming language package libraries.
However, you can [configure custom paths](deep-inspection.md#deep-inspection-paths "deep-inspection.md#deep-inspection-paths") in addition to the paths that Amazon Inspector scans by default.

###### Note

You can use deep inspection with the Default Host Management Configuration setting.
However, you must create or use a role that's configured with the `ssm:PutInventory` and `ssm:GetParameter` permissions.

To perform deep inspection scans for your Linux-based Amazon EC2 instances, Amazon Inspector uses data collected with the Amazon Inspector SSM plugin.
To manage the Amazon Inspector SSM plugin and perform deep inspection for Linux, Amazon Inspector automatically creates the SSM association `InvokeInspectorLinuxSsmPlugin-do-not-delete` in your account.
Amazon Inspector collects updated application inventory from your Linux-based Amazon EC2 instances every 6 hours.

###### Note

Deep inspection is not supported for Windows or Mac instances.

This section describes how to manage Amazon Inspector deep inspection for Amazon EC2 instances, including how to set custom paths for Amazon Inspector to scan.

###### Topics

- [Accessing or deactivating deep inspection](#deep-inspection-activate "#deep-inspection-activate")
- [Custom paths for Amazon Inspector deep inspection](#deep-inspection-paths "#deep-inspection-paths")
- [Custom schedules for Amazon Inspector deep inspection](#deep-inspection-schedules "#deep-inspection-schedules")
- [Supported programming languages](#supported-deep-inspection "#supported-deep-inspection")

## Accessing or deactivating deep inspection

###### Note

For accounts that activate Amazon Inspector after April 17, 2023, deep inspection is automatically activated as part of Amazon EC2 scanning.

###### To manage deep inspection

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home")
2. From the navigation pane, choose **General settings**, and then choose Amazon EC2 scanning settings.
3. Under **Deep inspection of Amazon EC2 instance**, you can [set custom paths for your organization or for your own account](deep-inspection.md#deep-inspection-paths "deep-inspection.md#deep-inspection-paths").

You can check the activation status programmatically for a single account with the [GetEc2DeepInspectionConfiguration](../../v2/APIReference/API_GetEc2DeepInspectionConfiguration.md "../../v2/APIReference/API_GetEc2DeepInspectionConfiguration.md") API.
You can check the activation status programmatically for multiple accounts with the [BatchGetMemberEc2DeepInspectionStatus](../../v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.md "../../v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.md") API.

If you activated Amazon Inspector before April 17, 2023, you can activate deep inspection through the console banner or the [UpdateEc2DeepInspectionConfiguration](../../v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.md "../../v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.md") API.
If you're the delegated administrator for an organization in Amazon Inspector, you can use the [BatchUpdateMemberEc2DeepInspectionStatus](../../v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.md "../../v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.md") API to activate deep inspection for yourself and your member accounts.

You can deactivate deep inspection through the [UpdateEc2DeepInspectionConfiguration](../../v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.md "../../v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.md") API.
Member accounts in an organization can't deactivate deep inspection.
Instead, the member account must be deactivated by their delegated administrator using the [BatchUpdateMemberEc2DeepInspectionStatus](../../v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.md "../../v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.md") API.

## Custom paths for Amazon Inspector deep inspection

You can set custom paths for Amazon Inspector to scan during deep inspection of your Linux Amazon EC2 instances.
When you set a custom path, Amazon Inspector scans packages in that directory and all of the sub-directories in it.

All accounts can define up to 5 custom paths.
The delegated administrator for an organization can define 10 custom paths.

Amazon Inspector scans all custom paths in addition to the following default paths, which Amazon Inspector scans for all accounts:

- `/usr/lib`
- `/usr/lib64`
- `/usr/local/lib`
- `/usr/local/lib64`

###### Note

Custom paths must be local paths.
Amazon Inspector doesn't scan mapped network paths, such as Network File System mounts or Amazon S3 file system mounts.

### Formatting custom paths

A custom path cannot be longer than 256 characters.
The following is an example of how a custom path might look:

###### Example path

`/home/usr1/project01`

###### Note

The package limit per instance is 5,000.
The maximum package inventory collection time is 15 minutes.
Amazon Inspector recommends that you choose custom paths to avoid these limits.

### Setting a custom path in the Amazon Inspector console and with the Amazon Inspector API

The following procedures describe how to set a custom path for Amazon Inspector deep inspection in the Amazon Inspector console and with the Amazon Inspector API.
After you set a custom path, Amazon Inspector includes the path in the next deep inspection.

Console

1. Sign in to the AWS Management Console as the delegated administrator, and open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home")
2. Use the AWS Region selector to choose the Region where you want to activate Lambda standard scanning.
3. From the navigation pane, choose **General settings**, and then choose **EC2 scanning settings**.
4. Under **Custom paths for your own account**, choose **Edit**.
5. In the path text boxes, enter your custom paths.
6. Choose **Save**.

API

Run the [UpdateEc2DeepInspectionConfiguration](../../v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.md "../../v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.md") command.
For `packagePaths` specify an array of paths to scan.

## Custom schedules for Amazon Inspector deep inspection

By default, Amazon Inspector collects an application inventory from Amazon EC2 instances every 6 hours.
However, you can run the following commands to control how often Amazon Inspector does this.

**Example command 1: List associations to view association ID and current interval**

The following command shows the association ID for the association `InvokeInspectorLinuxSsmPlugin-do-not-delete`.

```
aws ssm list-associations \
--association-filter-list "key=AssociationName,value=InvokeInspectorLinuxSsmPlugin-do-not-delete" \
--region `your-Region`
```

**Example command 2: Update association to include new interval**

The following command uses the association ID for the association `InvokeInspectorLinuxSsmPlugin-do-not-delete`.
You can set the rate for `schedule-expression` from 6 hours to a new interval, such as 12 hours.

```
aws ssm update-association \
--association-id "`your-association-ID`" \
--association-name "InvokeInspectorLinuxSsmPlugin-do-not-delete" \
--schedule-expression "rate(`6` hours)" \
--region `your-Region`
```

###### Note

Depending on your use case, if you set the rate for `schedule-expression` from 6 hours to an interval like 30 minutes, you can [exceed the daily ssm inventory limit](assessing-coverage.md#viewing-coverage-instances "assessing-coverage.md#viewing-coverage-instances").
This causes results to be delayed, and you might encounter Amazon EC2 instances with partial error statuses.

## Supported programming languages

For Linux instances, Amazon Inspector deep inspection can produce findings for application programming language packages and operating system packages.

For Mac and Windows instances, Amazon Inspector deep inspection can produce findings only for operating system packages.

For more information about supported programming languages, see [Supported programming languages: Amazon EC2 deep inspection](supported.md#supported-programming-languages-deep-inspection "supported.md#supported-programming-languages-deep-inspection").
