# Integrate IAM Access Analyzer with

AWS Security Hub CSPM

[AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") provides a comprehensive view of your security state across AWS. It helps
you assess your environment against security industry standards and best practices. Security Hub CSPM
collects security data from across AWS accounts, services, and supported third-party partner
products. It then analyzes your security trends and identify the highest priority security
issues.

When you integrate IAM Access Analyzer with Security Hub CSPM, you can send findings from IAM Access Analyzer to
Security Hub CSPM. Security Hub CSPM can then include those findings in its analysis of your overall security
posture.

###### Contents

- [How IAM Access Analyzer
  sends findings to Security Hub CSPM](access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-sending-findings "access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-sending-findings")
  - [Types of findings
    that IAM Access Analyzer sends](access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-finding-types "access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-finding-types")
  - [Latency for
    sending findings](access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-finding-latency "access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-finding-latency")
  - [Retrying when Security Hub CSPM is
    not available](access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-retry-send "access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-retry-send")
  - [Updating existing
    findings in Security Hub CSPM](access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-finding-updates "access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-finding-updates")

- [Viewing
  IAM Access Analyzer findings in Security Hub CSPM](access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-viewing-findings "access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-viewing-findings")
  - [Interpreting IAM Access Analyzer finding names in Security Hub CSPM](access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-intrepreting-finding-names "access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-intrepreting-finding-names")

- [Typical findings
  from IAM Access Analyzer](access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-finding-example "access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-finding-example")
- [Enabling and configuring the
  integration](access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-enable "access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-enable")
- [How to stop sending
  findings](access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-disable "access-analyzer-securityhub-integration.md#access-analyzer-securityhub-integration-disable")

## How IAM Access Analyzer

sends findings to Security Hub CSPM

In Security Hub CSPM, security issues are tracked as findings. Some findings come from issues that are
detected by other AWS services or by third-party partners. Security Hub CSPM also has a set of rules
that it uses to detect security issues and generate findings.

Security Hub CSPM provides tools to manage findings from across all of these sources. You can view and
filter lists of findings and view detailed information about each finding. For more
information, see [Viewing
findings](../../../securityhub/latest/userguide/securityhub-findings-viewing.md "../../../securityhub/latest/userguide/securityhub-findings-viewing.md") in the _AWS Security Hub User Guide_. You can also
track the status of investigations into findings. For more information, see [Taking action on
findings](../../../securityhub/latest/userguide/securityhub-findings-taking-action.md "../../../securityhub/latest/userguide/securityhub-findings-taking-action.md") in the _AWS Security Hub User Guide_.

All findings in Security Hub CSPM use a standard JSON format called the AWS Security Finding Format
(ASFF). The ASFF includes details about the source of the issue, the affected resources, and
the current status of the finding. For more information, see [AWS Security Finding
Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md") in the _AWS Security Hub User Guide_.

AWS Identity and Access Management Access Analyzer is one of the AWS services that sends findings to Security Hub CSPM. For unused
access, IAM Access Analyzer detects unused access granted to IAM users or roles and generates a
finding for each of them. IAM Access Analyzer then sends these findings to Security Hub CSPM.

For external access, IAM Access Analyzer detects policy statements that allow public access or
cross-account access to external principals on [supported resources](access-analyzer-resources.md "access-analyzer-resources.md") in your organization or account. IAM Access Analyzer generates a
finding for public access and sends it to Security Hub CSPM. For cross-account access, IAM Access Analyzer sends
a single finding for one external principal at a time to Security Hub CSPM. If there are multiple
cross-account findings in IAM Access Analyzer, you must resolve the Security Hub CSPM finding for the single
external principal before IAM Access Analyzer provides the next cross-account finding. For a full
list of external principals with cross-account access outside the zone of trust for the
analyzer, you must view the findings in IAM Access Analyzer. Details about the resource control
policy (RCP) are available in the resource detail section.

### Types of findings

that IAM Access Analyzer sends

IAM Access Analyzer sends the findings to Security Hub CSPM using the [AWS Security Finding
Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md"). In ASFF, the `Types` field provides the finding type.
Findings from IAM Access Analyzer can have the following values for `Types`.

- External access findings – Effects/Data Exposure/External Access
  Granted
- External access findings – Software and Configuration Checks/AWS Security
  Best Practices/External Access Granted
- Unused access findings – Software and Configuration Checks/AWS Security
  Best Practices/Unused Permission
- Unused access findings – Software and Configuration Checks/AWS Security
  Best Practices/Unused IAM Role
- Unused access findings – Software and Configuration Checks/AWS Security
  Best Practices/Unused IAM User Password
- Unused access findings – Software and Configuration Checks/AWS Security
  Best Practices/Unused IAM User Access Key

### Latency for

sending findings

When IAM Access Analyzer creates a new finding, it is usually sent to Security Hub CSPM within 30 minutes.
However, there are rare cases when IAM Access Analyzer may not be notified about a policy change.
For example:

- Changes to Amazon S3 account-level block public access settings can take up to 12 hours
  to be reflected in IAM Access Analyzer.
- Changes to a resource control policy (RCP) without a change to the resource-based
  policy do not trigger a rescan of the resource reported in the finding. IAM Access Analyzer
  analyzes the new or updated policy during the next periodic scan, which is within 24
  hours.
- If there is a delivery issue with AWS CloudTrail log delivery, a policy change may not
  trigger a rescan of the resource that was reported in the finding.

In these situations, IAM Access Analyzer analyzes the new or updated policy during the next
periodic scan.

### Retrying when Security Hub CSPM is

not available

If Security Hub CSPM is not available, IAM Access Analyzer retries sending the findings on a periodic
basis.

### Updating existing

findings in Security Hub CSPM

After sending a finding to Security Hub CSPM, IAM Access Analyzer continues to send updates to reflect any
additional observations of the finding activity to Security Hub CSPM. These updates are reflected within
the same finding.

For external access findings IAM Access Analyzer groups them per resource. In Security Hub CSPM, the
finding for a resource remains active if at least one of the findings for that resource is
active in IAM Access Analyzer. If all findings in IAM Access Analyzer for a resource are archived or
resolved, then the Security Hub CSPM finding is also archived. The Security Hub CSPM finding is updated when the
policy access changes between public and cross-account access. This update can include
changes to the type, title, description, and severity of the finding.

For unused access findings, IAM Access Analyzer does not group them by resource. Instead, if
an unused access finding is resolved in IAM Access Analyzer, then the corresponding Security Hub CSPM finding
is also resolved. The Security Hub CSPM finding is updated when you update the IAM user or role that
generated the unused access finding.

## Viewing

IAM Access Analyzer findings in Security Hub CSPM

To view your IAM Access Analyzer findings in Security Hub CSPM, choose **See findings** in
the **AWS: IAM Access Analyzer** section of the summary page.
Alternatively, you can choose **Findings** from the navigation panel. You can
then filter the findings to display only AWS Identity and Access Management Access Analyzer findings by choosing the
**Product name:** field with a value of
`IAM Access Analyzer`.

### Interpreting IAM Access Analyzer finding names in Security Hub CSPM

AWS Identity and Access Management Access Analyzer sends the findings to Security Hub CSPM using the AWS Security Finding Format
(ASFF). In ASFF, the **Types** field provides the finding type. ASFF types
use a different naming scheme than AWS Identity and Access Management Access Analyzer. The following table includes details
about all of the ASFF types associated with AWS Identity and Access Management Access Analyzer findings as they appear in
Security Hub CSPM.

| ASFF finding type                                                                           | Security Hub CSPM finding title                    | Description                                                                                                                                        |
| ------------------------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Effects/Data Exposure/External Access Granted                                               | <resource ARN> allows public access                | A resource-based policy attached to the resource allows public access on the<br>resource to all external principals.                               |
| Software and Configuration Checks/AWS Security Best Practices/External Access<br>Granted    | <resource ARN> allows cross-account access         | A resource-based policy attached to the resource allows cross-account access to<br>external principals outside the zone of trust for the analyzer. |
| Software and Configuration Checks/AWS Security Best Practices/Unused<br>Permission          | <resource ARN> contains unused permissions         | A user or role contains unused service and action permissions.                                                                                     |
| Software and Configuration Checks/AWS Security Best Practices/Unused IAM<br>Role            | <resource ARN> contains unused IAM role            | A user or role contains an unused IAM role.                                                                                                        |
| Software and Configuration Checks/AWS Security Best Practices/Unused IAM<br>User Password   | <resource ARN> contains unused IAM user password   | A user or role contains an unused IAM user password.                                                                                               |
| Software and Configuration Checks/AWS Security Best Practices/Unused IAM<br>User Access Key | <resource ARN> contains unused IAM user access key | A user or role contains an unused IAM user access key.                                                                                             |

## Typical findings

from IAM Access Analyzer

IAM Access Analyzer sends findings to Security Hub CSPM using the [AWS Security Finding
Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md").

Here is an example of a typical finding from IAM Access Analyzer for external access
findings.

```
{
    "SchemaVersion": "2018-10-08",
    "Id": "arn:aws:access-analyzer:us-west-2:111122223333:analyzer/my-analyzer/arn:aws:s3:::amzn-s3-demo-bucket",
    "ProductArn": "arn:aws:securityhub:us-west-2::product/aws/access-analyzer",
    "GeneratorId": "aws/access-analyzer",
    "AwsAccountId": "111122223333",
    "Types": ["Software and Configuration Checks/AWS Security Best Practices/External Access Granted"],
    "CreatedAt": "2020-11-10T16:17:47Z",
    "UpdatedAt": "2020-11-10T16:43:49Z",
    "Severity": {
        "Product": 1,
        "Label": "LOW",
        "Normalized": 1
    },
    "Title": "AwsS3Bucket/arn:aws:s3:::amzn-s3-demo-bucket/ allows cross-account access",
    "Description": "AWS::S3::Bucket/arn:aws:s3:::amzn-s3-demo-bucket/ allows cross-account access from AWS 444455556666",
    "Remediation": {
        "Recommendation": {"Text": "If the access isn't intended, it indicates a potential security risk. Use the console for the resource to modify or remove the policy that grants the unintended access. You can use the Rescan button on the Finding details page in the Access Analyzer console to confirm whether the change removed the access. If the access is removed, the status changes to Resolved."}
    },
    "SourceUrl": "https://console.aws.amazon.com/access-analyzer/home?region=us-west-2#/findings/details/dad90d5d-63b4-6575-b0fa-ef9c556ge798",
    "Resources": [
        {
            "Type": "AwsS3Bucket",
            "Id": "arn:aws:s3:::amzn-s3-demo-bucket",
            "Details": {
                "Other": {
                    "External Principal Type": "AWS",
                    "Condition": "none",
                    "Action Granted": "s3:GetObject,s3:GetObjectVersion",
                    "External Principal": "444455556666"
                }
            }
        }
    ],
    "WorkflowState": "NEW",
    "Workflow": {"Status": "NEW"},
    "RecordState": "ACTIVE"
}
```

Here is an example of a typical finding from IAM Access Analyzer for unused access
findings.

```
{
    "Findings": [
    {
      "SchemaVersion": "2018-10-08",
      "Id": "arn:aws:access-analyzer:us-west-2:111122223333:analyzer/integTestAnalyzer-DO-NOT-DELETE/arn:aws:iam::111122223333:role/TestRole/UnusedPermissions",
      "ProductArn": "arn:aws:securityhub:us-west-2::product/aws/access-analyzer",
      "ProductName": "IAM Access Analyzer",
      "CompanyName": "AWS",
      "Region": "us-west-2",
      "GeneratorId": "aws/access-analyzer",
      "AwsAccountId": "111122223333",
      "Types": [
        "Software and Configuration Checks/AWS Security Best Practices/Unused Permission"
      ],
      "CreatedAt": "2023-09-18T16:29:09.657Z",
      "UpdatedAt": "2023-09-21T20:39:16.651Z",
      "Severity": {
        "Product": 1,
        "Label": "LOW",
        "Normalized": 1
      },
      "Title": "AwsIamRole/arn:aws:iam::111122223333:role/IsengardRole-DO-NOT-DELETE/ contains unused permissions",
      "Description": "AWS::IAM::Role/arn:aws:iam::111122223333:role/IsengardRole-DO-NOT-DELETE/ contains unused service and action-level permissions",
      "Remediation": {
        "Recommendation": {
          "Text":"If the unused permissions aren’t required, delete the permissions to refine access to your account. Use the IAM console to modify or remove the policy that grants the unused permissions. If all the unused permissions are removed, the status of the finding changes to Resolved."
        }
      },
      "SourceUrl": "https://us-west-2.console.aws.amazon.com/access-analyzer/home?region=us-west-2#/unused-access-findings?resource=arn%3Aaws%3Aiam%3A%3A903798373645%3Arole%2FTestRole",
      "ProductFields": {
      "numberOfUnusedActions": "256",
      "numberOfUnusedServices": "15",
      "resourceOwnerAccount": "111122223333",
      "findingId": "DEMO24d8d-0d3f-4d3d-99f4-299fc8a62ee7",
      "findingType": "UnusedPermission",
      "aws/securityhub/FindingId": "arn:aws:securityhub:us-west-2::product/aws/access-analyzer/arn:aws:access-analyzer:us-west-2:111122223333:analyzer/integTestAnalyzer-DO-NOT-DELETE/arn:aws:iam::111122223333:role/TestRole/UnusedPermissions",
      "aws/securityhub/ProductName": "AM Access Analyzer",
      "aws/securityhub/CompanyName": "AWS"
    },
    "Resources": [
    {
      "Type": "AwsIamRole",
      "Id": "arn:aws:iam::111122223333:role/TestRole"
    }
  ],
  "WorkflowState": "NEW",
  "Workflow": {
    "Status": "NEW"
    },
  "RecordState": "ARCHIVED",
  "FindingProviderFields": {
    "Severity": {
      "Label": "LOW"
    },
    "Types": [
    "Software and Configuration Checks/AWS Security Best Practices/Unused Permission"
    ]
  }
  }
]
}
```

## Enabling and configuring the

integration

To use the integration with Security Hub CSPM, you must enable Security Hub CSPM. For information on how to enable
Security Hub CSPM, see [Setting up Security
Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md") in the _AWS Security Hub User Guide_.

When you enable both IAM Access Analyzer and Security Hub CSPM, the integration is enabled automatically.
IAM Access Analyzer immediately begins to send findings to Security Hub CSPM.

## How to stop sending

findings

To stop sending findings to Security Hub CSPM, you can use either the Security Hub CSPM console or the API.

See [Disabling and enabling the flow of findings from an integration
(console)](../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-console "../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-console") or [Disabling the flow of findings from an integration (Security Hub API,
AWS CLI)](../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-disable-api "../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-disable-api") in the _AWS Security Hub User Guide_.
