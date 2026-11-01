

# Scan an Amazon EC2 AMI for software vulnerabilities with Amazon Inspector
<a name="ami-scanning"></a>

Amazon Inspector is a vulnerability management service that scans your AWS workloads, including your Amazon EC2 AMIs, for software vulnerabilities. Two scan types are available: an on-demand scan of an AMI, and continuous AMI scanning on an AWS account. For more information, see [Scanning machine images with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-machine-images.html) in the *Amazon Inspector User Guide*.

When Amazon Inspector scans an AMI, Amazon EC2 makes the scan results available for the AMI. The scan results include a summary and the detailed findings. You can view the summary in the `ScanResults` field of the `describe-images` response, and you can view the detailed findings with the `get-image-findings` command. In the Amazon EC2 console, you can view both on the **Security** tab for the AMI.

When you share an AMI with other AWS accounts, organizations, or organizational units (OUs), or make it public, its scan results and findings are available to those accounts along with the AMI. When you copy an AMI, Amazon EC2 copies the scan results summary and the source AMI's top 50 findings to the new AMI, so the copy can have fewer findings than the source AMI. This number might change in the future.

You can use Allowed AMIs to permit only AMIs that meet your scan-result criteria. To do so, add a `ScanResultCondition` to your Allowed AMIs settings. For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](ec2-allowed-amis.md).

**Topics**
+ [Run an on-demand scan of an AMI](#ami-scanning-on-demand)
+ [Enable continuous AMI scanning](#ami-scanning-continuous)
+ [View a summary of the scan results for an AMI](#view-ami-scan-results)
+ [View the detailed findings for an AMI](#view-ami-findings)
+ [Pricing](#ami-scanning-costs)

## Run an on-demand scan of an AMI
<a name="ami-scanning-on-demand"></a>

You can run an on-demand scan of an AMI that you own. You don't need to activate Amazon Inspector to run an on-demand scan. An AMI can have only one scan in progress at a time, and you can have up to 20 on-demand scans in progress at the same time. When the scan completes, Amazon Inspector sends the results to Amazon EC2. The results of an on-demand scan don't appear in the Amazon Inspector console. For more information, see [Running on-demand machine image scans with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/machine-image-on-demand.html) in the *Amazon Inspector User Guide*.

------
#### [ Console ]

**To run an on-demand scan of an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. From the filter bar, choose **Owned by me**.

1. Select the AMI, and then choose **Actions**, **Security**, **Initiate on-demand scan**.

1. To view the scan progress and the results, choose the **Security** tab.

------
#### [ AWS CLI ]

**To run an on-demand scan of an AMI**  
Use the following Amazon Inspector **start-on-demand-scan** command. For more information, see [start-on-demand-scan](https://docs.aws.amazon.com/cli/latest/reference/inspector2/start-on-demand-scan.html) in the *AWS CLI Command Reference*.

```
aws inspector2 start-on-demand-scan \
    --resource-id {{ami-1234567890EXAMPLE}} \
    --resource-type AMI
```

When the scan completes, use the `describe-images` and `get-image-findings` commands to view the results. For more information, see [View a summary of the scan results for an AMI](#view-ami-scan-results) and [View the detailed findings for an AMI](#view-ami-findings).

------

## Enable continuous AMI scanning
<a name="ami-scanning-continuous"></a>

With continuous AMI scanning, Amazon Inspector monitors the AMIs in your account that match the scanning criteria that you define, and scans them for software vulnerabilities. You can view the results in the Amazon Inspector console or in the Amazon EC2 console. When you share a scanned AMI, the accounts that you share it with can also view its scan results.

To scan the AMIs in your account continuously, activate AMI scanning in Amazon Inspector. To open the Amazon Inspector console from the Amazon EC2 console, choose **Actions**, **Security**, **Manage AMI scanning**. For more information, see [Configuring machine image scanning](https://docs.aws.amazon.com/inspector/latest/user/machine-image-scan-configuration.html) in the *Amazon Inspector User Guide*.

## View a summary of the scan results for an AMI
<a name="view-ami-scan-results"></a>

The scan results summary for an AMI includes the following:
+ `HighestFindingSeverityLabel` – The highest severity among the AMI's findings, whether or not a fix is available. The value is `informational`, `low`, `medium`, `high`, or `critical`.
+ `FindingScanDate` – The date and time of the most recent Amazon Inspector scan of the AMI.
+ `InformationalFixAvailableSince`, `LowFixAvailableSince`, `MediumFixAvailableSince`, `HighFixAvailableSince`, and `CriticalFixAvailableSince` – For each severity, the earliest date and time that Amazon Inspector reported a fix as available for a finding of that severity on the AMI. Amazon EC2 returns each field only when such a finding exists. These dates are specific to the AMI. Each date reflects when a fix became available for a finding on that AMI, not when the vendor released the fix. As a result, a date can be later than the vendor's release date, and AMIs with the same vulnerability can have different dates.

You can view the scan results for an AMI that you scanned, and for a shared or public AMI that Amazon Inspector has scanned.

------
#### [ Console ]

**To view a summary of the scan results for an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI, and then choose the **Security** tab.

1. Under **Scan summary**, view the number of findings for each severity, the number of findings with a fix available, and when Amazon Inspector last updated the results.

In the AMIs list, you can also display the **Highest vulnerability severity** and **Vulnerability results updated** columns. These columns are available for any AMI that you can view.

------
#### [ AWS CLI ]

**To view a summary of the scan results for an AMI**  
Use the following **describe-images** command. The `--query` option limits the output to the `ScanResults` field. For more information, see [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) in the *AWS CLI Command Reference*.

```
aws ec2 describe-images \
    --image-ids {{ami-1234567890EXAMPLE}} \
    --query "Images[].ScanResults"
```

The following is example output.

```
[
    {
        "HighestFindingSeverityLabel": "high",
        "FindingScanDate": "2026-10-05T12:00:00.000Z",
        "MediumFixAvailableSince": "2026-09-20T08:30:00.000Z",
        "HighFixAvailableSince": "2026-10-01T14:15:00.000Z"
    }
]
```

**To find AMIs by their scan results**  
Use the `scan-result.*` filters. For example, the following command finds AMIs whose highest finding severity is `critical`. For the full list of filters, see [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) in the *AWS CLI Command Reference*.

```
aws ec2 describe-images \
    --filters "Name=scan-result.highest-finding-severity-label,Values=critical" \
    --query "Images[].ImageId"
```

------

## View the detailed findings for an AMI
<a name="view-ami-findings"></a>

Each finding includes the title, the severity label, and the Amazon Inspector score. Each finding shows whether a fix is available, and when Amazon Inspector first observed and last updated the finding. Each finding also includes the ID of the Amazon EBS snapshot where Amazon Inspector detected the vulnerability, and the affected file paths. Amazon EC2 returns up to 10 affected file paths for each finding.

To view the history of on-demand scans for an AMI, select the AMI in the Amazon EC2 console and choose the **Security** tab. The `describe-images` and `get-image-findings` responses don't include the scan history. For more information, see [Running on-demand machine image scans with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/machine-image-on-demand.html) in the *Amazon Inspector User Guide*.

------
#### [ Console ]

**To view the findings for an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI, and then choose the **Security** tab.

1. Under **Vulnerability findings**, view the findings. For each finding, the table shows the title, the severity, the score, whether a fix is available, the affected file paths, and when Amazon Inspector last updated the finding.

------
#### [ AWS CLI ]

**To view the findings for an AMI**  
Use the [get-image-findings](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-image-findings.html) command.

```
aws ec2 get-image-findings \
    --image-id {{ami-1234567890EXAMPLE}}
```

The following is example output.

```
{
    "ImageFindings": [
        {
            "Title": "CVE-2026-12345 - openssl",
            "SeverityLabel": "high",
            "Score": 7.5,
            "FixAvailable": true,
            "FirstObservedAt": "2026-10-05T12:00:00.000Z",
            "UpdatedAt": "2026-10-06T08:30:00.000Z",
            "SnapshotId": "snap-1234567890EXAMPLE",
            "Paths": [
                "/usr/lib/libssl.so.3",
                "/usr/bin/openssl"
            ]
        }
    ],
    "NextToken": "EXAMPLETOKEN1234567890"
}
```

To control the number of findings that Amazon EC2 returns, use the `--max-results` parameter with a value from `1` to `1000`. To get the next page of results, pass the returned `NextToken` value in the `--next-token` parameter.

------

## Pricing
<a name="ami-scanning-costs"></a>

Amazon Inspector charges for both on-demand scans and continuous AMI scanning. For more information, see [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/) on the AWS website.