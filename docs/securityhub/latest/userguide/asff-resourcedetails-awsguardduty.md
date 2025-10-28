# AwsGuardDuty resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsGuardDuty` resources.

AWS Security Hub normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsGuardDutyDetector

The `AwsGuardDutyDetector` object provides information about an Amazon GuardDuty
detector. A detector is an object that represents the GuardDuty service. A detector is
required for GuardDuty to become operational.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsGuardDutyDetector` object. To view descriptions of
`AwsGuardDutyDetector` attributes, see [AwsGuardDutyDetector](../../1.0/APIReference/API_AwsGuardDutyDetectorDetails.md "../../1.0/APIReference/API_AwsGuardDutyDetectorDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsGuardDutyDetector": {
    "FindingPublishingFrequency": "SIX_HOURS",
    "ServiceRole": "arn:aws:iam::123456789012:role/aws-service-role/guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDuty",
    "Status": "ENABLED",
    "DataSources": {
        "CloudTrail": {
            "Status": "ENABLED"
        },
        "DnsLogs": {
            "Status": "ENABLED"
        },
        "FlowLogs": {
            "Status": "ENABLED"
        },
        "S3Logs": {
             "Status": "ENABLED"
         },
         "Kubernetes": {
             "AuditLogs": {
                "Status": "ENABLED"
             }
         },
         "MalwareProtection": {
             "ScanEc2InstanceWithFindings": {
                "EbsVolumes": {
                    "Status": "ENABLED"
                 }
             },
            "ServiceRole": "arn:aws:iam::123456789012:role/aws-service-role/malware-protection.guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDutyMalwareProtection"
         }
    }
}
```
