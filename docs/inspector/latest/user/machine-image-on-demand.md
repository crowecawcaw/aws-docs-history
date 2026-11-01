

# Running on-demand machine image scans with Amazon Inspector
<a name="machine-image-on-demand"></a>

 An on-demand machine image scan is a one-time scan of a single machine image that you request. You don't need to activate Amazon Inspector to run one. Use an on-demand scan to scan a single image at a point in time, such as an image a build pipeline just produced. The image doesn't enter a continuous scanning scope. 

 You start an on-demand scan with the [StartOnDemandScan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StartOnDemandScan.html) API operation. Amazon Inspector returns a `scanId` that identifies the scan, collects a software inventory from the Amazon EBS snapshots that back the machine image, evaluates that inventory against Amazon Inspector vulnerability data, and then publishes the results to Amazon EventBridge. You can also start an on-demand scan from the Amazon EC2 console, which calls StartOnDemandScan on your behalf. 

**Important**  
 Amazon Inspector delivers the findings from an on-demand scan only through EventBridge. On-demand scan findings don't appear in the Amazon Inspector console, aren't returned by the [ListFindings](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListFindings.html) API operation, and aren't sent to AWS Security Hub CSPM. To view the findings for a machine image in a console, use the Amazon EC2 console. If you also activated continuous machine image scanning and the image is in scope, its continuous-scan findings still appear in these places. For more information, see [Receiving on-demand scan results with Amazon EventBridge](#machine-image-on-demand-events). 

 The following table compares on-demand scanning with continuous machine image scanning. 


**On-demand compared with continuous machine image scanning**  

|  | On-demand scanning | Continuous scanning | 
| --- | --- | --- | 
| How a scan starts | You call StartOnDemandScan for a specific machine image. | Amazon Inspector scans machine images automatically when you create, copy, register, or enable an image, and when a relevant new CVE is published, as long as the image is within your scan eligibility windows. For more information, see [Setting scan eligibility windows](machine-image-scan-configuration.md#machine-image-eligibility-windows). | 
| Activation required | No. You don't need to activate Amazon Inspector. | Yes. You activate machine image scanning for the account. | 
| Scan configuration | Not applied. On-demand scans ignore scan eligibility windows, scan mode, and exclusion options. | Applied. For more information, see [Configuring machine image scanning](machine-image-scan-configuration.md). | 
| Rescans | None. Each scan is a one-time evaluation. Call StartOnDemandScan again to rescan. | Amazon Inspector rescans in-scope images automatically. For more information about which images are in scope, see [Eligible machine images](scanning-machine-images.md#machine-image-eligible). | 
| Where results go | EventBridge only. | The same places as your other Amazon Inspector findings. For more information, see [Viewing Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-locating-analyzing.html). | 
| Free trial | Not eligible. | Eligible. For more information, see [About the Amazon Inspector free trial](usage.md#free-trial). | 

**Note**  
 On-demand scanning is independent of continuous machine image scanning. If you activated machine image scanning for your account, you can still run on-demand scans, including for machine images that your scan configuration excludes. Amazon Inspector meters an on-demand scan separately from any continuous scan of the same image. 

**Topics**
+ [Requirements for on-demand machine image scans](#machine-image-on-demand-requirements)
+ [Starting an on-demand machine image scan](#machine-image-on-demand-start)
+ [Scan status values for on-demand machine image scans](#machine-image-on-demand-status)
+ [Receiving on-demand scan results with Amazon EventBridge](#machine-image-on-demand-events)
+ [Pricing for on-demand machine image scans](#machine-image-on-demand-pricing)

## Requirements for on-demand machine image scans
<a name="machine-image-on-demand-requirements"></a>

 Amazon Inspector runs an on-demand scan only if the following conditions are met: 
+  The IAM identity that starts the scan has permission for both the `inspector2:StartOnDemandScan` action and the `iam:CreateServiceLinkedRole` action. Amazon Inspector needs `iam:CreateServiceLinkedRole` to create the service-linked roles that it uses to read your snapshot data. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*. 
+  Your account owns the machine image and the Amazon EBS snapshots that back it. If the image belongs to another account, Amazon Inspector returns an `AccessDeniedException`. To scan an image that another account shared with you, or a public image, first copy it into your own account. Then scan the copy. 
+  No other on-demand scan is already in progress for the same machine image. Amazon Inspector runs one on-demand scan per image at a time, but you can scan different images at the same time. If a scan is already in progress, Amazon Inspector returns a `ConflictException`. Use [GetOnDemandScanStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetOnDemandScanStatus.html) to check whether the in-progress scan finished before you retry. 
+  The machine image meets the same eligibility requirements that apply to continuous scanning, including a supported operating system and a supported file system format on every snapshot that backs the image. For more information, see [Eligible machine images](scanning-machine-images.md#machine-image-eligible) and [Supported operating systems: machine image scanning](supported.md#supported-os-ami). 

 When you start your first on-demand scan, Amazon Inspector creates the service-linked roles that it needs to read your snapshot data. While an on-demand scan is in progress for your account, Amazon Inspector prevents you from deleting those service-linked roles so that the scan can finish. After all of your on-demand scans finish, you can delete the roles. The roles remain in your account until you delete them. For more information, see [Using service-linked roles for Amazon Inspector](using-service-linked-roles.md). 

## Starting an on-demand machine image scan
<a name="machine-image-on-demand-start"></a>

 The following procedure describes how to start an on-demand scan of a machine image. 

------
#### [ API ]

 Run the [StartOnDemandScan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StartOnDemandScan.html) API operation. In the request, provide the ID of the machine image as `resourceId`, and set `resourceType` to `AMI`. 

```
{
    "resourceId": "ami-0abcdef1234567890",
    "resourceType": "AMI"
}
```

 Amazon Inspector returns a `scanId` that uniquely identifies the scan. Store the `scanId`. You use it to check the status of the scan, and Amazon Inspector includes it in every EventBridge notification for the scan. If you don't have the `scanId`, you can find it by using the [ListOnDemandScans](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListOnDemandScans.html) API operation. 

```
{
    "scanId": "9f1c4b8d2e6a4f0b7c3d5e1a8b2f6c4d"
}
```

------
#### [ Amazon EC2 console ]

**To start an on-demand machine image scan**

1.  Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/home). 

1.  Select the AWS Region that contains the machine image that you want to scan. 

1.  From the navigation pane, choose **AMIs**, and then select the machine image that you want to scan. 

1.  Choose **Actions**, and then choose **Scan for vulnerabilities**. 

------

 To check the status of a scan, use the [GetOnDemandScanStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetOnDemandScanStatus.html) API operation with the `scanId` and the machine image ID. To list the on-demand scans that Amazon Inspector still retains for a machine image, use the [ListOnDemandScans](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListOnDemandScans.html) API operation. Amazon Inspector returns the scans for the machine image with the most recent scan first, and paginates the results with `maxResults` and `nextToken`. 

**Note**  
 Amazon Inspector retains the record of an on-demand scan, including its status and the manifest that Amazon Inspector collected, for 30 days after the scan completes. After 30 days, GetOnDemandScanStatus returns a `ResourceNotFoundException` for that `scanId`, and the scan no longer appears in ListOnDemandScans results. 

## Scan status values for on-demand machine image scans
<a name="machine-image-on-demand-status"></a>

 GetOnDemandScanStatus returns a `scanStatus` for the scan, and a `scanStatusReason` when the scan failed. These values are specific to on-demand scans and differ from the scan status values that Amazon Inspector reports for continuously scanned machine images. For the continuous scanning values, see [Scan status values for machine images](scanning-machine-images.md#machine-image-scan-status). 


**On-demand machine image scan status values**  

| Scan status | Scan status reason | Description | 
| --- | --- | --- | 
| IN\_PROGRESS | – | Amazon Inspector started the scan and is collecting the software inventory or evaluating it for vulnerabilities. | 
| SUCCESSFUL | – | Amazon Inspector finished the scan and published the findings to EventBridge. | 
| FAILED | ACCESS\_DENIED | Amazon Inspector couldn't access the machine image or the snapshots that back it. This can occur if a resource policy or a AWS KMS key policy prevents Amazon Inspector from reading the snapshot data. | 
| FAILED | UNSUPPORTED\_OS | The operating system of the machine image isn't supported for scanning, or one or more of the snapshots that back the image uses a configuration that Amazon Inspector can't read, such as Logical Volume Manager (LVM). For more information, see [Supported operating systems: machine image scanning](supported.md#supported-os-ami). | 
| FAILED | STORAGE\_LIMIT\_EXCEEDED | The combined size of the snapshots that back the machine image exceeds the limit that Amazon Inspector supports for scanning. Amazon Inspector can't scan this machine image. | 
| FAILED | EXTRACTION\_COLLECTION\_TIME\_LIMIT\_EXCEEDED | Amazon Inspector timed out while collecting the software inventory from the snapshots that back the machine image. | 
| FAILED | RESOURCE\_TERMINATED | You deregistered the machine image, or deleted a snapshot that backs it, while the scan was in progress. | 
| FAILED | INTERNAL\_ERROR | Amazon Inspector encountered an internal error while scanning the machine image. Call StartOnDemandScan again to retry the scan. | 

## Receiving on-demand scan results with Amazon EventBridge
<a name="machine-image-on-demand-events"></a>

 Amazon Inspector publishes two kinds of EventBridge events for an on-demand machine image scan: 

**Findings events**  
 Amazon Inspector publishes one event for each vulnerability that it detects in the machine image. The `detail-type` field is set to `Inspector2 OnDemand Finding`. These events identify the machine image by its ID and don't include other machine image metadata. 

**Scan complete events**  
 Amazon Inspector publishes one event when the scan reaches a terminal state. The `detail-type` field is set to `Inspector2 OnDemand Scan Complete`. A successful event includes a `findingSeverityCounts` object. A failed event includes a `scanStatusReason` field instead. 

 Every event includes the `scanId` of the scan, so you can correlate findings events with the scan complete event for the same scan. To receive these events, create an EventBridge rule in the same AWS Region and account as the scan. For more information, see [Amazon EventBridge event schema for Amazon Inspector events](eventbridge-integration.md) and [Creating rules that react to events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the *Amazon EventBridge User Guide*. 

 The following example shows the scan complete event for a successful on-demand scan. 

```
{
    "version": "0",
    "id": "7bf7f4b1-9f6c-4d3e-8a2b-5c1d0e9f3a44",
    "detail-type": "Inspector2 OnDemand Scan Complete",
    "source": "aws.inspector2",
    "account": "111122223333",
    "time": "2026-06-12T01:30:00Z",
    "region": "us-east-1",
    "resources": [
        "ami-0abcdef1234567890"
    ],
    "detail": {
        "scanId": "9f1c4b8d2e6a4f0b7c3d5e1a8b2f6c4d",
        "awsAccountId": "111122223333",
        "resourceId": "ami-0abcdef1234567890",
        "resourceType": "MACHINE_IMAGE",
        "scanStatus": "SUCCESSFUL",
        "startedAt": "2026-06-12T00:00:00.000Z",
        "completedAt": "2026-06-12T01:30:00.000Z",
        "findingSeverityCounts": {
            "CRITICAL": 0,
            "HIGH": 2,
            "MEDIUM": 5,
            "LOW": 1,
            "INFORMATIONAL": 0,
            "UNTRIAGED": 0,
            "TOTAL": 8
        },
        "version": "1.0"
    }
}
```

 The following example shows the scan complete event for a failed on-demand scan. 

```
{
    "version": "0",
    "id": "3c2e9a17-8b4d-4f61-9a0c-2d7e6f1b8c33",
    "detail-type": "Inspector2 OnDemand Scan Complete",
    "source": "aws.inspector2",
    "account": "111122223333",
    "time": "2026-06-12T01:30:00Z",
    "region": "us-east-1",
    "resources": [
        "ami-0abcdef1234567890"
    ],
    "detail": {
        "scanId": "9f1c4b8d2e6a4f0b7c3d5e1a8b2f6c4d",
        "awsAccountId": "111122223333",
        "resourceId": "ami-0abcdef1234567890",
        "resourceType": "MACHINE_IMAGE",
        "scanStatus": "FAILED",
        "scanStatusReason": "UNSUPPORTED_OS",
        "startedAt": "2026-06-12T00:00:00.000Z",
        "completedAt": "2026-06-12T01:30:00.000Z",
        "version": "1.0"
    }
}
```

 The following example shows a findings event for a package vulnerability that Amazon Inspector detected in a machine image. 

```
{
    "source": "aws.inspector2",
    "detail-type": "Inspector2 OnDemand Finding",
    "detail": {
        "findingArn": "arn:aws:inspector2:us-east-1:111122223333:finding/ondemand/9f1c4b8d2e6a4f0b7c3d5e1a8b2f6c4d/cea7c73a3d57d9c142992e845644d317",
        "scanId": "9f1c4b8d2e6a4f0b7c3d5e1a8b2f6c4d",
        "awsAccountId": "111122223333",
        "type": "PACKAGE_VULNERABILITY",
        "title": "CVE-2022-3171 - com.google.protobuf:protobuf-java",
        "description": "A parsing issue with binary data in protobuf-java...",
        "severity": "HIGH",
        "status": "ACTIVE",
        "firstObservedAt": "2026-06-12T01:30:00.000Z",
        "lastObservedAt": "2026-06-12T01:30:00.000Z",
        "updatedAt": "2026-06-12T01:30:00.000Z",
        "resources": [
            {
                "type": "MACHINE_IMAGE",
                "id": "ami-0abcdef1234567890",
                "partition": "aws",
                "region": "us-east-1"
            }
        ],
        "inspectorScore": 7.5,
        "inspectorScoreDetails": {
            "adjustedCvss": {
                "scoreSource": "NVD",
                "cvssSource": "NVD",
                "version": "3.1",
                "score": 7.5,
                "scoringVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
                "adjustments": []
            }
        },
        "packageVulnerabilityDetails": {
            "vulnerabilityId": "CVE-2022-3171",
            "vulnerablePackages": [
                {
                    "name": "com.google.protobuf:protobuf-java",
                    "version": "2.5.0",
                    "epoch": 0,
                    "packageManager": "JAVA",
                    "filePath": "/usr/lib/jars/protobuf-java-2.5.0.jar",
                    "fixedInVersion": "3.16.3"
                }
            ],
            "source": "NVD",
            "sourceUrl": "https://nvd.nist.gov/vuln/detail/CVE-2022-3171",
            "vendorSeverity": "high"
        },
        "remediation": {
            "recommendation": {
                "text": "Update com.google.protobuf:protobuf-java to 3.16.3 or later"
            }
        },
        "fixAvailable": "YES",
        "exploitAvailable": "NO"
    }
}
```

**Note**  
 EventBridge delivers events at least once, so your rule can receive the same event more than once. Use the `findingArn` field to deduplicate findings events. If a rule is misconfigured, a target is throttled, or a target lacks the permissions that EventBridge needs, an event can also be dropped. Confirm that you received a scan complete event for every `scanId` that you started, and use GetOnDemandScanStatus to reconcile any scan that you don't have an event for. 

## Pricing for on-demand machine image scans
<a name="machine-image-on-demand-pricing"></a>

 Amazon Inspector meters each on-demand machine image scan individually. Amazon Inspector meters a scan only after it reaches a `SUCCESSFUL` status, so you're not charged for a scan that fails. Each call to StartOnDemandScan that completes successfully is a separate metered scan, even if you scan the same machine image more than once. 

**Important**  
 On-demand machine image scans aren't included in the Amazon Inspector free trial. Amazon Inspector meters on-demand scans from your first scan, whether or not you activated Amazon Inspector for the account. For more information, see [Monitoring Usage and Cost in Amazon Inspector](usage.md) and [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/). 