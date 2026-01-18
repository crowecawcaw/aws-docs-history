# View your AMI usage

If you share your Amazon Machine Images (AMIs) with other AWS accounts—whether with
specific AWS accounts, organizations, organizational units (OUs), or publicly—you
can see how these AMIs are used by creating AMI usage reports. The reports provide
visibility into:

- Which AWS accounts are using your AMIs in EC2 instances or launch templates
- How many EC2 instances or launch templates are referencing each AMI
  AMI usage reports help you manage your AMIs more effectively by helping you:

- Identify the AWS accounts and resource types referencing your AMIs so that you can safely
  deregister or disable AMIs.
- Identify unused AMIs for deregistration to reduce storage costs.
- Identify your most used AMIs.

###### Contents

- [How AMI usage reports work](#how-ami-usage-reports-work "#how-ami-usage-reports-work")
- [Create an AMI usage report](#create-ami-usage-reports "#create-ami-usage-reports")
- [View AMI usage reports](#view-ami-usage-reports "#view-ami-usage-reports")
- [Delete an AMI usage report](#delete-ami-usage-reports "#delete-ami-usage-reports")
- [Report quotas](#ami-usage-report-quotas "#ami-usage-report-quotas")

## How AMI usage reports work

When you create an AMI usage report, you specify:

- The AMI to report on.
- The AWS accounts to check (specific accounts or all accounts).
- The resource types to check (EC2 instances, launch templates, or both).
- For launch templates, the number of versions to check (defaults to the 20 most
  recent versions).

Amazon EC2 creates a separate report for each AMI. Each report provides:

- A list of the AWS accounts using the AMI.
- A count of the resources referencing the AMI by resource type per account.
  Note that for launch templates, if an AMI is referenced in multiple versions of
  a launch template, the count is only 1.

###### Important

When you generate an AMI usage report, it might not contain the most recent activity.
Instance activity from the past 24 hours and launch template activity from the past
few days might not appear in the report.

Amazon EC2 automatically deletes a report 30 days after creation. You can download reports
from the EC2 console to retain locally.

## Create an AMI usage report

To view how your AMI is being used, you must first create an AMI usage report,
specifying the accounts and resource types to report on. Once the report is created, you
can view the contents of the report. You can also download the report from the EC2
console.

Console

###### To create an AMI usage report

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. Select an AMI and choose **Actions**,
   **AMI usage**, **View my AMI
   usage**.
4. On the **Create my AMI usage report** page, do
   the following:
   1. For **Resource types**, select one or
      more resource types to report on.
   2. For **Account IDs**, do one of the
      following:
      - Choose **Specify accounts IDs**
        and then choose **Add account ID**
        for each account to report on.
      - Choose **Include all accounts**
        to report on all accounts.

   3. Choose **Create my AMI usage
      report**.

5. On the AMI page, choose the **My AMI
   usage** tab.
6. Choose a report ID to view its details.

AWS CLI

###### To create an AMI usage report for a list of accounts

Use the [create-image-usage-report](../../../cli/latest/reference/ec2/create-image-usage-report.md "../../../cli/latest/reference/ec2/create-image-usage-report.md") command with the following
required parameters:

- `--image-id` – The ID of the AMI to report on.
- `--resource-types` – The types of resources to check. In the following
  example, the resource types to check are EC2 instances and launch
  templates. In addition, the number of launch template versions to
  check is also specified
  (`version-depth=`100``).

To report on specific accounts, use the `--account-ids` parameter to specify
the ID of each account to report on.

```
aws ec2 create-image-usage-report \
    --image-id `ami-0abcdef1234567890` \
    --account-ids `111122223333 444455556666 123456789012` \
    --resource-types ResourceType=ec2:Instance \
      'ResourceType=ec2:LaunchTemplate,ResourceTypeOptions=[{OptionName=version-depth,OptionValues=`100`}]'
```

###### To create an AMI usage report of all accounts

To report on all accounts using the specified AMI, use the same command but omit the
`--account-ids` parameter.

```
aws ec2 create-image-usage-report \
    --image-id `ami-0abcdef1234567890` \
    --resource-types ResourceType=ec2:Instance \
      'ResourceType=ec2:LaunchTemplate,ResourceTypeOptions=[{OptionName=version-depth,OptionValues=`100`}]'
```

The following is example output.

```
{
    "ReportId": "amiur-00b877d192f6b02d0"
}
```

###### To monitor the report creation status

Use the [describe-image-usage-reports](../../../cli/latest/reference/ec2/describe-image-usage-reports.md "../../../cli/latest/reference/ec2/describe-image-usage-reports.md") command and specify the report
ID.

```
aws ec2 describe-image-usage-reports --report-ids `amiur-00b877d192f6b02d0`
```

The following is example output. The initial value of the `State` field is
`pending`. To be able to view the report entries, the state
must be `available`.

```
{
    "ImageUsageReports": [
        {
            "ImageId": "ami-0e9ae3dc21c2b3a64",
            "ReportId": "amiur-abcae3dc21c2b3999",
            "ResourceTypes": [
                {"ResourceType": "ec2:Instance"}
            ],
            "State": "pending",
            "CreationTime": "2025-09-29T13:27:12.322000+00:00",
            "ExpirationTime": "2025-10-28T13:27:12.322000+00:00"
        }
    ]
}
```

PowerShell

###### To create an AMI usage report for a list of accounts

Use the [New-EC2ImageUsageReport](../../../powershell/latest/reference/items/New-EC2ImageUsageReport.md "../../../powershell/latest/reference/items/New-EC2ImageUsageReport.md") cmdlet with the following required
parameters:

- `-ImageId` – The ID of the AMI to report
  on.
- `-ResourceType` – The types of resources to check. In the following
  example, the resource types to check are EC2 instances and launch
  templates. In addition, the number of launch template versions to
  check is also specified (`'version-depth' =
`100``).

To report on specific accounts, use the `-AccountId` parameter to specify the
ID of each account to report on.

```
New-EC2ImageUsageReport `
    -ImageId `ami-0abcdef1234567890` `
    -AccountId `111122223333 444455556666 123456789012` `
    -ResourceType @(
        @{ResourceType = 'ec2:Instance'},
        @{ResourceType = 'ec2:LaunchTemplate'ResourceTypeOptions = @{'version-depth' = 100}
        })
```

###### To create an AMI usage report of all accounts

To report on all accounts using the specified AMI, use the same command but omit the
`-AccountId` parameter.

```
New-EC2ImageUsageReport `
    -ImageId `ami-0abcdef1234567890` `
    -ResourceType @(
        @{ResourceType = 'ec2:Instance'},
        @{ResourceType = 'ec2:LaunchTemplate'ResourceTypeOptions = @{'version-depth' = 100}
        })
```

The following is example output.

```
ReportId
--------
amiur-00b877d192f6b02d0
```

###### To monitor the report creation status

Use the [Get-EC2ImageUsageReport](../../../powershell/latest/reference/items/Get-EC2ImageUsageReport.md "../../../powershell/latest/reference/items/Get-EC2ImageUsageReport.md") command and specify the report
ID.

```
Get-EC2ImageUsageReport -ReportId `amiur-00b877d192f6b02d0`
```

The following is example output. The initial value of the `State` field is
`pending`. To be able to view the report entries, the state
must be `available`.

```
ImageUsageReports
-----------------
{@{ImageId=ami-0e9ae3dc21c2b3a64; ReportId=amiur-abcae3dc21c2b3999; ResourceTypes=System.Object[]; State=pending; CreationTime=2025-09-29; ExpirationTime=2025-10-28}}
```

## View AMI usage reports

You can view all the usage reports you've created for an AMI in the past 30 days. Amazon EC2
automatically deletes a report 30 days after creation.

For each report, you can see the AWS accounts that are using the AMI, and for each
account, a count of the resources referencing the AMI by resource type. You can also see
when the report creation was initiated. This information is only available when the
report is in the **Complete** (console) or `available` (AWS CLI)
state.

###### Important

When you generate an AMI usage report, it might not contain the most recent activity.
Instance activity from the past 24 hours and launch template activity from the past
few days might not appear in the report.

Console

###### To view an AMI usage report

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. Select an AMI.
4. Choose the **My usage reports** tab.

The report list shows:

    * All reports generated in the past 30 days for the selected
     AMI.
    * For each report, the **Report initiated
     time** column shows the date the report was
     created.

5. Choose the ID of a report to view its contents.
6. To go back to the **My usage reports** tab on the AMI details page,
   choose **View all reports for this AMI**.

AWS CLI

###### To list all the AMI usage reports for the specified AMI

Use the [describe-image-usage-reports](../../../cli/latest/reference/ec2/describe-image-usage-reports.md "../../../cli/latest/reference/ec2/describe-image-usage-reports.md") command and specify the ID of
the AMI to get a list of its reports.

```
aws ec2 describe-image-usage-reports --image-ids `ami-0abcdef1234567890`
```

The following is example output. Each report ID is listed along with the resource types
that were scanned and the report creation and expiration dates. You can use
this information to identify the reports whose entries you want to
view.

```
{
  "ImageUsageReports": [
    {
      "ImageId": "ami-0abcdef1234567890",
      "ReportId": "amiur-1111111111111111",
      "ResourceTypes": [
        {
          "ResourceType": "ec2:Instance"
        }
      ],
      "State": "available",
      "CreationTime": "2025-09-29T13:27:12.322000+00:00",
      "ExpirationTime": "2025-10-28T13:27:12.322000+00:00",
      "Tags": []
    },
    {
      "ImageId": "ami-0abcdef1234567890",
      "ReportId": "amiur-22222222222222222",
      "ResourceTypes": [
        {
          "ResourceType": "ec2:Instance"
        },
        {
          "ResourceType": "ec2:LaunchTemplate"
        }
      ],
      "State": "available",
      "CreationTime": "2025-10-01T13:27:12.322000+00:00",
      "ExpirationTime": "2025-10-30T13:27:12.322000+00:00",
      "Tags": []
    }
  ],
  "NextToken": "opaque"
}
```

###### To view the contents of an AMI usage report for the specified AMI

Use the [describe-image-usage-report-entries](../../../cli/latest/reference/ec2/describe-image-usage-report-entries.md "../../../cli/latest/reference/ec2/describe-image-usage-report-entries.md") command and specify the
ID of the AMI. The response returns all the reports for the specified
AMI, showing the accounts that have used the AMI and their resource
counts.

```
aws ec2 describe-image-usage-report-entries --image-ids `ami-0abcdef1234567890`
```

The following is example output.

```
{
  "ImageUsageReportEntries": [
    {
      "ImageId": "ami-0abcdef1234567890",
      "ResourceType": "ec2:Instance",
      "AccountId": "123412341234",
      "UsageCount": 15,
      "ReportCreationTime": "2025-09-29T13:27:12.322000+00:00",
      "ReportId": "amiur-1111111111111111"
    },
    {
      "ImageId": "ami-0abcdef1234567890",
      "ResourceType": "ec2:Instance",
      "AccountId": "123412341234",
      "UsageCount": 2,
      "ReportCreationTime": "2025-10-01T13:27:12.322000+00:00",
      "ReportId": "amiur-22222222222222222"
    },
    {
      "ImageId": "ami-0abcdef1234567890",
      "ResourceType": "ec2:Instance",
      "AccountId": "001100110011",
      "UsageCount": 39,
      "ReportCreationTime": "2025-10-01T13:27:12.322000+00:00",
      "ReportId": "amiur-22222222222222222"
    }
  ],
  "NextToken": "opaque"
}
```

###### To view the contents of an AMI usage report for the specified report

Use the [describe-image-usage-report-entries](../../../cli/latest/reference/ec2/describe-image-usage-report-entries.md "../../../cli/latest/reference/ec2/describe-image-usage-report-entries.md") command and specify the
ID of the report. The response returns all the entries for the specified
report, showing the accounts that have used the AMI and their resource
counts.

```
aws ec2 describe-image-usage-report-entries --report-ids `amiur-11111111111111111`
```

The following is example output.

```
{
  "ImageUsageReportEntries": [
    {
      "ImageId": "ami-0abcdef1234567890",
      "ResourceType": "ec2:Instance",
      "AccountId": "123412341234",
      "UsageCount": 15,
      "ReportCreationTime": "2025-09-29T13:27:12.322000+00:00",
      "ReportId": "amiur-11111111111111111"
    },
    {
      "ImageId": "ami-0abcdef1234567890",
      "ResourceType": "ec2:LaunchTemplate",
      "AccountId": "123412341234",
      "UsageCount": 4,
      "ReportCreationTime": "2025-09-29T13:27:12.322000+00:00",
      "ReportId": "amiur-11111111111111111"
    },
    {
      "ImageId": "ami-0abcdef1234567890",
      "ResourceType": "ec2:LaunchTemplate",
      "AccountId": "001100110011",
      "UsageCount": 2,
      "ReportCreationTime": "2025-09-29T13:27:12.322000+00:00",
      "ReportId": "amiur-11111111111111111"
    }
  ],
  "NextToken": "opaque"
}
```

PowerShell

###### To list all the AMI usage reports for the specified AMI

Use the [Get-EC2ImageUsageReport](../../../powershell/latest/reference/items/Get-EC2ImageUsageReport.md "../../../powershell/latest/reference/items/Get-EC2ImageUsageReport.md") cmdlet and specify the ID of the
AMI to get a list of its reports.

```
Get-EC2ImageUsageReport -ImageId `ami-0abcdef1234567890`
```

The following is example output. Each report ID is listed along with the resource types
that were scanned and the report creation and expiration dates. You can use
this information to identify the reports whose entries you want to
view.

```
@{
    ImageUsageReports = @(
        @{
            ImageId = "ami-0abcdef1234567890"
            ReportId = "amiur-1111111111111111"
            ResourceTypes = @(
                @{
                    ResourceType = "ec2:Instance"
                }
            )
            State = "available"
            CreationTime = "2025-09-29T13:27:12.322000+00:00"
            ExpirationTime = "2025-10-28T13:27:12.322000+00:00"
        },
        @{
            ImageId = "ami-0abcdef1234567890"
            ReportId = "amiur-22222222222222222"
            ResourceTypes = @(
                @{
                    ResourceType = "ec2:Instance"
                }
            )
            State = "available"
            CreationTime = "2025-09-30T13:27:12.322000+00:00"
            ExpirationTime = "2025-10-29T13:27:12.322000+00:00"
        },
        @{
            ImageId = "ami-0abcdef1234567890"
            ReportId = "amiur-33333333333333333"
            ResourceTypes = @(
                @{
                    ResourceType = "ec2:Instance"
                }
            )
            State = "available"
            CreationTime = "2025-10-01T13:27:12.322000+00:00"
            ExpirationTime = "2025-10-30T13:27:12.322000+00:00"
        }
    )
    NextToken = "opaque"
}
```

###### To view the contents of an AMI usage report for the specified AMI

Use the [Get-EC2ImageUsageReportEntry](../../../powershell/latest/reference/items/Get-EC2ImageUsageReportEntry.md "../../../powershell/latest/reference/items/Get-EC2ImageUsageReportEntry.md") cmdlet and specify the ID of
the AMI. The response returns all the reports for the specified AMI,
showing the accounts that have used the AMI and their resource
counts.

```
Get-EC2ImageUsageReportEntry -ImageId `ami-0abcdef1234567890`
```

The following is example output.

```
ImageUsageReportEntries : {@{
    ImageId = "ami-0abcdef1234567890"
    ResourceType = "ec2:Instance"
    AccountId = "123412341234"
    UsageCount = 15
    ReportCreationTime = "2025-09-29T13:27:12.322000+00:00"
    ReportId = "amiur-1111111111111111"
    }, @{
    ImageId = "ami-0abcdef1234567890"
    ResourceType = "ec2:Instance"
    AccountId = "123412341234"
    UsageCount = 7
    ReportCreationTime = "2025-09-30T13:27:12.322000+00:00"
    ReportId = "amiur-22222222222222222"
    }...}
NextToken : opaque
```

###### To view the contents of an AMI usage report for the specified report

Use the [Get-EC2ImageUsageReportEntry](../../../powershell/latest/reference/items/Get-EC2ImageUsageReportEntry.md "../../../powershell/latest/reference/items/Get-EC2ImageUsageReportEntry.md") cmdlet and specify the ID of
the report. The response returns all the entries for the specified
report, showing the accounts that have used the AMI and their resource
counts.

```
Get-EC2ImageUsageReportEntry -ReportId `amiur-11111111111111111`
```

The following is example output.

```
ImageUsageReportEntries : {@{
    ImageId = "ami-0abcdef1234567890"
    ResourceType = "ec2:Instance"
    AccountId = "123412341234"
    UsageCount = 15
    ReportCreationTime = "2025-09-29T13:27:12.322000+00:00"
    ReportId = "amiur-11111111111111111"
    }, @{
    ImageId = "ami-0abcdef1234567890"
    ResourceType = "ec2:LaunchTemplate"
    AccountId = "123412341234"
    UsageCount = 4
    ReportCreationTime = "2025-09-29T13:27:12.322000+00:00"
    ReportId = "amiur-11111111111111111"
    }, @{
    ImageId = "ami-0abcdef1234567890"
    ResourceType = "ec2:LaunchTemplate"
    AccountId = "************"
    UsageCount = 2
    ReportCreationTime = "2025-09-29T13:27:12.322000+00:00"
    ReportId = "amiur-11111111111111111"
    }}
NextToken : opaque
```

## Delete an AMI usage report

Amazon EC2 automatically deletes a report 30 days after it was created. You can delete
it manually before that time.

Console

###### To delete an AMI usage report

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. Select an AMI.
4. Choose the **My AMI usage** tab.
5. Choose the option button next to the report to delete, and then
   choose **Delete**.

AWS CLI

###### To delete an AMI usage report

Use the [delete-image-usage-report](../../../cli/latest/reference/ec2/delete-image-usage-report.md "../../../cli/latest/reference/ec2/delete-image-usage-report.md") command and specify the ID of the
report.

```
aws ec2 delete-image-usage-report --report-id `amiur-0123456789abcdefg`
```

PowerShell

###### To delete an AMI usage report

Use the [Remove-EC2ImageUsageReport](../../../powershell/latest/reference/items/Remove-EC2ImageUsageReport.md "../../../powershell/latest/reference/items/Remove-EC2ImageUsageReport.md") cmdlet and specify the ID of the
report.

```
Remove-EC2ImageUsageReport -ReportId `amiur-0123456789abcdefg`
```

## Report quotas

The following quotas apply to creating AMI usage reports. The quotas apply per
AWS Region.

| Description                                               | Quota |
| --------------------------------------------------------- | ----- |
| In-progress (`pending`) AMI usage reports per AWS account | 2,000 |
| In-progress (`pending`) AMI usage reports per AMI         | 1     |
