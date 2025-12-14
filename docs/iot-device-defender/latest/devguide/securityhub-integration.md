# Integration with AWS Security Hub CSPM

[AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") provides you with a comprehensive view of your security state in AWS and
helps you check your environment against security industry standards and best practices. Security Hub CSPM
collects security data from across AWS accounts, services, and supported third-party
products. You can use Security Hub CSPM to analyze your security trends and identify the highest priority
security issues.

With the AWS IoT Device Defender integration with Security Hub CSPM, you can send findings from AWS IoT Device Defender to Security Hub CSPM. Security Hub CSPM
includes those findings in its analysis of your security posture.

###### Contents

- [Enabling and configuring the
  integration](securityhub-integration.md#securityhub-integration-enable "securityhub-integration.md#securityhub-integration-enable")
- [How AWS IoT Device Defender sends findings to
  Security Hub CSPM](securityhub-integration.md#securityhub-integration-sending-findings "securityhub-integration.md#securityhub-integration-sending-findings")
  - [Types of findings that AWS IoT Device Defender
    sends](securityhub-integration.md#securityhub-integration-finding-types "securityhub-integration.md#securityhub-integration-finding-types")
  - [Latency for sending
    findings](securityhub-integration.md#securityhub-integration-finding-latency "securityhub-integration.md#securityhub-integration-finding-latency")
  - [Retrying when Security Hub CSPM isn't
    available](securityhub-integration.md#securityhub-integration-retry-send "securityhub-integration.md#securityhub-integration-retry-send")
  - [Updating existing findings in
    Security Hub CSPM](securityhub-integration.md#securityhub-integration-finding-updates "securityhub-integration.md#securityhub-integration-finding-updates")

- [Typical finding from AWS IoT Device Defender](securityhub-integration.md#securityhub-integration-finding-example "securityhub-integration.md#securityhub-integration-finding-example")
- [Stopping AWS IoT Device Defender from sending findings to
  Security Hub CSPM](securityhub-integration.md#securityhub-integration-disable "securityhub-integration.md#securityhub-integration-disable")

## Enabling and configuring the

integration

Before you integrate AWS IoT Device Defender with Security Hub CSPM, you must first enable Security Hub CSPM. For information
about how to enable Security Hub CSPM, see [Setting up Security
Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md") in the _AWS Security Hub CSPM User Guide_.

After you enable both AWS IoT Device Defender and Security Hub CSPM, open the [Integrations page in the Security Hub CSPM console](https://console.aws.amazon.com//securityhub/home#/integrations "https://console.aws.amazon.com//securityhub/home#/integrations"), and
then choose **Accept findings** for Audit, Detect, or both. AWS IoT Device Defender begins
sending findings to Security Hub CSPM.

## How AWS IoT Device Defender sends findings to

Security Hub CSPM

In Security Hub CSPM, security issues are tracked as _findings_. Some
findings come from issues that are detected by other AWS services or by third-party
products.

Security Hub CSPM provides tools to manage findings from across all of these sources. You can view and
filter lists of findings and view details for a finding. For more information, see [Viewing findings](../../../securityhub/latest/userguide/securityhub-findings-viewing.md "../../../securityhub/latest/userguide/securityhub-findings-viewing.md") in the _AWS Security Hub CSPM User Guide_. You
can also track the status of an investigation into a finding. For more information, see [Taking action on
findings](../../../securityhub/latest/userguide/securityhub-findings-taking-action.md "../../../securityhub/latest/userguide/securityhub-findings-taking-action.md") in the _AWS Security Hub CSPM User Guide_.

All findings in Security Hub CSPM use a standard JSON format called the _AWS
Security Finding Format (ASFF)_. The ASFF includes details about the source of the
issue, the affected resources, and the current status of the finding. For more information
about ASFF, see [AWS Security Finding
Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md") in the _AWS Security Hub CSPM User Guide_.

AWS IoT Device Defender is one of the AWS services that sends findings to Security Hub CSPM.

### Types of findings that AWS IoT Device Defender

sends

After you enable the Security Hub CSPM integration, AWS IoT Device Defender Audit sends the findings it generates
(called _check summaries_) to Security Hub CSPM. Check summaries are
general information for a specific audit check type and a specific audit task. For more
information, see [Audit
checks](../../../iot/latest/developerguide/device-defender-audit-checks.md "../../../iot/latest/developerguide/device-defender-audit-checks.md").

AWS IoT Device Defender Audit sends finding updates to Security Hub CSPM for both Audit Check Summaries and Audit Findings in each Audit task. If all resources found in Audit Checks are compliant, or an Audit Task is canceled, Audit updates the Check Summaries in Security Hub CSPM to an ARCHIVED record state. If a resource was reported as non-compliant for an Audit Check, but was reported as compliant in the last Audit task, Audit changes it to compliant and also updates the finding in Security Hub CSPM to an ARCHIVED record state.

AWS IoT Device Defender Detect sends violation findings to Security Hub CSPM. These violation findings include
machine learning (ML), statistical, and static behaviors.

To send the findings to Security Hub CSPM, AWS IoT Device Defender uses the [AWS Security Finding
Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md"). In ASFF, the `Types` field provides the finding type.
Findings from AWS IoT Device Defender can have the following values for `Types`.

**Unusual behaviors**

The finding type for conflicting MQTT client IDs and device certificate shared
checks, and the finding type for Detect.

**Software and Configuration Check/Vulnerabilities**

The finding type for all other Audit checks.

### Latency for sending

findings

When AWS IoT Device Defender Audit creates a new finding, it's immediately sent to Security Hub CSPM after the audit
task completes. The latency depends on the volume of the findings generated in the audit
task. Security Hub CSPM typically receives the findings within one hour.

AWS IoT Device Defender Detect sends findings for violations in near real time. After a violation goes
into or out of alarm (meaning the alarm is created or deleted), the corresponding Security Hub CSPM
finding is immediately created or archived.

### Retrying when Security Hub CSPM isn't

available

If Security Hub CSPM isn't available, AWS IoT Device Defender Audit and AWS IoT Device Defender Detect retry sending the findings
until they're received.

### Updating existing findings in

Security Hub CSPM

After an AWS IoT Device Defender Audit finding is sent to Security Hub CSPM, you can identify it by checked resource
identifier and audit check type. If a new audit finding is generated with a subsequent audit
task for the same resource and audit check, AWS IoT Device Defender Audit sends updates to reflect additional
observations of the finding activity to Security Hub CSPM. If no additional audit finding is generated
with a subsequent audit task for the same resource and audit check, the resource changes to
compliant with the audit check. AWS IoT Device Defender Audit then archives the findings in Security Hub CSPM.

AWS IoT Device Defender Audit also updates check summaries in Security Hub CSPM. If there are non-compliant resources found in an audit check or the check fails, the status of the Security Hub CSPM finding becomes active. Otherwise, AWS IoT Device Defender Audit archives the finding in Security Hub CSPM.

AWS IoT Device Defender Detect creates a Security Hub CSPM finding when there's a violation (for example, in-alarm). That finding is updated only if one of the following criteria is met:

- The finding is expiring soon in Security Hub CSPM so AWS IoT Device Defender sends an update to keep the finding current. Findings are deleted 90 days after the most recent update or 90 days after the creation date if no update occurs. For more information, see [Security Hub CSPM quotas](../../../securityhub/latest/userguide/securityhub_limits.md "../../../securityhub/latest/userguide/securityhub_limits.md") in the _AWS Security Hub CSPM User Guide_.
- The corresponding violation goes out of alarm, so AWS IoT Device Defender updates its finding status
  to ARCHIVED.

## Typical finding from AWS IoT Device Defender

AWS IoT Device Defender uses the [AWS Security Finding
Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md") to send findings to Security Hub CSPM.

The following example shows a typical finding from Security Hub CSPM for an audit finding. The
`ReportType` in `ProductFields` is `AuditFinding`.

```

  {
  "SchemaVersion": "2018-10-08",
  "Id": "336757784525/IOT_POLICY/policyexample/1/IOT_POLICY_OVERLY_PERMISSIVE_CHECK/ALLOWS_BROAD_ACCESS_TO_IOT_DATA_PLANE_ACTIONS",
  "ProductArn": "arn:aws:securityhub:us-west-2::product/aws/iot-device-defender-audit",
  "ProductName": "IoT Device Defender - Audit",
  "CompanyName": "AWS",
  "Region": "us-west-2",
  "GeneratorId": "1928b87ab338ee2f541f6fab8c41c4f5",
  "AwsAccountId": "123456789012",
  "Types": [
    "Software and Configuration Check/Vulnerabilities"
  ],
  "CreatedAt": "2022-11-06T22:11:40.941Z",
  "UpdatedAt": "2022-11-06T22:11:40.941Z",
  "Severity": {
    "Label": "CRITICAL",
    "Normalized": 90
  },
  "Title": "IOT_POLICY_OVERLY_PERMISSIVE_CHECK: ALLOWS_BROAD_ACCESS_TO_IOT_DATA_PLANE_ACTIONS",
  "Description": "IOT_POLICY policyexample:1 is reported as non-compliant for IOT_POLICY_OVERLY_PERMISSIVE_CHECK by Audit task 9f71b6e90cfb57d4ac671be3a4898e6a. The non-compliant reason is Policy allows broad access to IoT data plane actions: [iot:Connect].",
  "SourceUrl": "https://us-west-2.console.aws.amazon.com/iot/home?region=us-west-2#/policy/policyexample",
  "ProductFields": {
    "CheckName": "IOT_POLICY_OVERLY_PERMISSIVE_CHECK",
    "TaskId": "9f71b6e90cfb57d4ac671be3a4898e6a",
    "TaskType": "ON_DEMAND_AUDIT_TASK",
    "PolicyName": "policyexample",
    "IsSuppressed": "false",
    "ReasonForNonComplianceCode": "ALLOWS_BROAD_ACCESS_TO_IOT_DATA_PLANE_ACTIONS",
    "ResourceType": "IOT_POLICY",
    "FindingId": "1928b87ab338ee2f541f6fab8c41c4f5",
    "PolicyVersionId": "1",
    "ReportType": "AuditFinding",
    "TaskStartTime": "1667772700554",
    "aws/securityhub/FindingId": "arn:aws:securityhub:us-west-2::product/aws/iot-device-defender-audit/336757784525/IOT_POLICY/policyexample/1/IOT_POLICY_OVERLY_PERMISSIVE_CHECK/ALLOWS_BROAD_ACCESS_TO_IOT_DATA_PLANE_ACTIONS",
    "aws/securityhub/ProductName": "IoT Device Defender - Audit",
    "aws/securityhub/CompanyName": "AWS"
  },
  "Resources": [
    {
      "Type": "AwsIotPolicy",
      "Id": "policyexample",
      "Partition": "aws",
      "Region": "us-west-2",
      "Details": {
        "Other": {
          "PolicyVersionId": "1"
        }
      }
    }
  ],
  "WorkflowState": "NEW",
  "Workflow": {
    "Status": "NEW"
  },
  "RecordState": "ACTIVE",
  "FindingProviderFields": {
    "Severity": {
      "Label": "CRITICAL"
    },
    "Types": [
      "Software and Configuration Check/Vulnerabilities"
    ]
  }
}

```

The following example shows a finding from Security Hub CSPM for an audit check summary. The
`ReportType` in `ProductFields` is `CheckSummary`.

```

  {
  "SchemaVersion": "2018-10-08",
  "Id": "615243839755/SCHEDULED_AUDIT_TASK/daily_audit_schedule_checks/DEVICE_CERTIFICATE_KEY_QUALITY_CHECK",
  "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/iot-device-defender-audit",
  "ProductName": "IoT Device Defender - Audit",
  "CompanyName": "AWS",
  "Region": "us-east-1",
  "GeneratorId": "f3021945485adf92487c273558fcaa51",
  "AwsAccountId": "123456789012",
  "Types": [
    "Software and Configuration Check/Vulnerabilities/CVE"
  ],
  "CreatedAt": "2022-10-18T14:20:13.933Z",
  "UpdatedAt": "2022-10-18T14:20:13.933Z",
  "Severity": {
    "Label": "CRITICAL",
    "Normalized": 90
  },
  "Title": "DEVICE_CERTIFICATE_KEY_QUALITY_CHECK Summary: Completed with 2 non-compliant resources",
  "Description": "Task f3021945485adf92487c273558fcaa51 of weekly scheduled Audit daily_audit_schedule_checks completes. 2 non-cimpliant resources are found for DEVICE_CERTIFICATE_KEY_QUALITY_CHECK out of 1000 resources in the account. The percentage of non-compliant resources is 0.2%.",
  "SourceUrl": "https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/dd/audit/results/f3021945485adf92487c273558fcaa51/DEVICE_CERTIFICATE_KEY_QUALITY_CHECK",
  "ProductFields": {
    "TaskId": "f3021945485adf92487c273558fcaa51",
    "TaskType": "SCHEDULED_AUDIT_TASK",
    "ScheduledAuditName": "daily_audit_schedule_checks",
    "CheckName": "DEVICE_CERTIFICATE_KEY_QUALITY_CHECK",
    "ReportType": "CheckSummary",
    "CheckRunStatus": "COMPLETED_NON_COMPLIANT",
    "NonComopliantResourcesCount": "2",
    "SuppressedNonCompliantResourcesCount": "1",
    "TotalResourcesCount": "1000",
    "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-1::product/aws/iot-device-defender-audit/615243839755/SCHEDULED/daily_audit_schedule_checks/DEVICE_CERTIFICATE_KEY_QUALITY_CHECK",
    "aws/securityhub/ProductName": "IoT Device Defender - Audit",
    "aws/securityhub/CompanyName": "AWS"
  },
  "Resources": [
    {
      "Type": "AwsIotAuditTask",
      "Id": "f3021945485adf92487c273558fcaa51",
      "Region": "us-east-1"
    }
  ],
  "WorkflowState": "NEW",
  "Workflow": {
    "Status": "NEW"
  },
  "RecordState": "ACTIVE",
  "FindingProviderFields": {
    "Severity": {
      "Label": "CRITICAL"
    },
    "Types": [
      "Software and Configuration Check/Vulnerabilities/CVE"
    ]
  }
}

```

The following example shows a typical finding from Security Hub CSPM for an AWS IoT Device Defender Detect violation.

```

  {
  "SchemaVersion": "2018-10-08",
  "Id": "e92a782593c6f5b1fc7cb6a443dc1a12",
  "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/iot-device-defender-detect",
  "ProductName": "IoT Device Defender - Detect",
  "CompanyName": "AWS",
  "Region": "us-east-1",
  "GeneratorId": "arn:aws:iot:us-east-1:123456789012:securityprofile/MySecurityProfile",
  "AwsAccountId": "123456789012",
  "Types": [
    "Unusual Behaviors"
  ],
  "CreatedAt": "2022-11-09T22:45:00Z",
  "UpdatedAt": "2022-11-09T22:45:00Z",
  "Severity": {
    "Label": "MEDIUM",
    "Normalized": 40
  },
  "Title": "Registered thing MyThing is in alarm for STATIC behavior MyBehavior.",
  "Description": "Registered thing MyThing violates STATIC behavior MyBehavior of security profile MySecurityProfile. Violation was triggered because the device did not conform to aws:num-disconnects less-than 1.",
  "SourceUrl": "https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/dd/securityProfile/MySecurityProfile?tab=violations",
  "ProductFields": {
    "ComparisonOperator": "less-than",
    "BehaviorName": "MyBehavior",
    "ViolationId": "e92a782593c6f5b1fc7cb6a443dc1a12",
    "ViolationStartTime": "1668033900000",
    "SuppressAlerts": "false",
    "ConsecutiveDatapointsToAlarm": "1",
    "ConsecutiveDatapointsToClear": "1",
    "DurationSeconds": "300",
    "Count": "1",
    "MetricName": "aws:num-disconnects",
    "BehaviorCriteriaType": "STATIC",
    "ThingName": "MyThing",
    "SecurityProfileName": "MySecurityProfile",
    "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-1::product/aws/iot-device-defender-detect/e92a782593c6f5b1fc7cb6a443dc1a12",
    "aws/securityhub/ProductName": "IoT Device Defender - Detect",
    "aws/securityhub/CompanyName": "AWS"
  },
  "Resources": [
    {
      "Type": "AwsIotRegisteredThing",
      "Id": "MyThing",
      "Region": "us-east-1",
      "Details": {
        "Other": {
          "SourceUrl": "https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/thing/MyThing?tab=violations",
          "IsRegisteredThing": "true",
          "ThingArn": "arn:aws:iot:us-east-1:123456789012:thing/MyThing"
        }
      }
    }
  ],
  "WorkflowState": "NEW",
  "Workflow": {
    "Status": "NEW"
  },
  "RecordState": "ACTIVE",
  "FindingProviderFields": {
    "Severity": {
      "Label": "MEDIUM"
    },
    "Types": [
      "Unusual Behaviors"
    ]
  }
}

```

## Stopping AWS IoT Device Defender from sending findings to

Security Hub CSPM

To stop sending findings to Security Hub CSPM, you can use either the Security Hub CSPM console or the API.

For more information, see [Disabling and enabling the flow of findings from an integration
(console)](../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-console "../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-console") or [Disabling the flow of findings from an integration (Security Hub CSPM API,
AWS CLI)](../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-disable-api "../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-disable-api") in the _AWS Security Hub CSPM User Guide_.
