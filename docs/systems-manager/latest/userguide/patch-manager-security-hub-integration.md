# Integrating Patch Manager with

AWS Security Hub

[AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")
provides you with a comprehensive view of your security state in AWS. Security Hub
collects security data from across AWS accounts, AWS services, and supported
third-party partner products. With Security Hub, you can check your environment against
security industry standards and best practices. Security Hub helps you to analyze your
security trends and identify the highest priority security issues.

By using the integration between Patch Manager, a tool in AWS Systems Manager, and Security Hub, you can
send findings about noncompliant nodes from Patch Manager to Security Hub. A finding is the
observable record of a security check or security-related detection. Security Hub can then
include those patch-related findings in its analysis of your security
posture.

The information in the following topics applies no matter which method or type of
configuration you are using for your patching operations:

- A patch policy configured in Quick Setup
- A Host Management option configured in Quick Setup
- A maintenance window to run a patch `Scan` or
  `Install` task
- An on-demand **Patch now** operation

###### Contents

- [How Patch Manager sends
  findings to Security Hub](patch-manager-security-hub-integration.md#securityhub-integration-sending-findings "patch-manager-security-hub-integration.md#securityhub-integration-sending-findings")
  - [Types of findings
    that Patch Manager sends](patch-manager-security-hub-integration.md#securityhub-integration-finding-types "patch-manager-security-hub-integration.md#securityhub-integration-finding-types")
  - [Latency for
    sending findings](patch-manager-security-hub-integration.md#securityhub-integration-finding-latency "patch-manager-security-hub-integration.md#securityhub-integration-finding-latency")
  - [Retrying when Security Hub
    isn't available](patch-manager-security-hub-integration.md#securityhub-integration-retry-send "patch-manager-security-hub-integration.md#securityhub-integration-retry-send")
  - [Viewing findings in
    Security Hub](patch-manager-security-hub-integration.md#securityhub-integration-view-findings "patch-manager-security-hub-integration.md#securityhub-integration-view-findings")

- [Typical finding from
  Patch Manager](patch-manager-security-hub-integration.md#securityhub-integration-finding-example "patch-manager-security-hub-integration.md#securityhub-integration-finding-example")
- [Turning on and configuring the
  integration](patch-manager-security-hub-integration.md#securityhub-integration-enable "patch-manager-security-hub-integration.md#securityhub-integration-enable")
- [How to stop sending
  findings](patch-manager-security-hub-integration.md#securityhub-integration-disable "patch-manager-security-hub-integration.md#securityhub-integration-disable")

## How Patch Manager sends

findings to Security Hub

In Security Hub, security issues are tracked as findings. Some findings come from
issues that are detected by other AWS services or by third-party partners.
Security Hub also has a set of rules that it uses to detect security issues and
generate findings.

Patch Manager is one of the Systems Manager tools that sends findings to Security Hub. After you
perform a patching operation by running a SSM document
(`AWS-RunPatchBaseline`,
`AWS-RunPatchBaselineAssociation`, or
`AWS-RunPatchBaselineWithHooks`), the patching information is
sent to Inventory or Compliance, tools in AWS Systems Manager, or both. After Inventory,
Compliance, or both receive the data, Patch Manager receives a notification. Then,
Patch Manager evaluates the data for accuracy, formatting, and compliance. If all
conditions are met, Patch Manager forwards the data to Security Hub.

Security Hub provides tools to manage findings from across all of these sources. You
can view and filter lists of findings and view details for a finding. For more
information, see [Viewing
findings](../../../securityhub/latest/userguide/securityhub-findings-viewing.md "../../../securityhub/latest/userguide/securityhub-findings-viewing.md") in the _AWS Security Hub User Guide_.
You can also track the status of an investigation into a finding. For more
information, see [Taking action on findings](../../../securityhub/latest/userguide/securityhub-findings-taking-action.md "../../../securityhub/latest/userguide/securityhub-findings-taking-action.md") in the _AWS Security Hub User Guide_.

All findings in Security Hub use a standard JSON format called the AWS Security
Finding Format (ASFF). The ASFF includes details about the source of the issue,
the affected resources, and the current status of the finding. For more
information, see [AWS
Security Finding Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md") in the _AWS Security Hub User Guide_.

### Types of findings

that Patch Manager sends

Patch Manager sends the findings to Security Hub using the [AWS Security Finding Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md"). In ASFF, the
`Types` field provides the finding type. Findings from
Patch Manager have the following value for `Types`:

- Software and Configuration Checks/Patch Management

Patch Manager sends one finding per noncompliant managed node. The finding is
reported with the resource type [`AwsEc2Instance`](../../../securityhub/latest/userguide/securityhub-findings-format-attributes.md#asff-resourcedetails-awsec2instance "../../../securityhub/latest/userguide/securityhub-findings-format-attributes.md#asff-resourcedetails-awsec2instance") so that findings can be
correlated with other Security Hub integrations that report
`AwsEc2Instance` resource types. Patch Manager only forwards a
finding to Security Hub if the operation discovered the managed node to be
noncompliant. The finding includes the Patch Summary results.

###### Note

After reporting a noncompliant node to Security Hub. Patch Manager doesn't send an
update to Security Hub after the node is made compliant. You can manually
resolve findings in Security Hub after the required patches have been applied
to the managed node.

For more information about compliance definitions, see [Patch compliance state
values](patch-manager-compliance-states.md "patch-manager-compliance-states.md"). For more information about
`PatchSummary`, see [PatchSummary](../../../securityhub/1.0/APIReference/API_PatchSummary.md "../../../securityhub/1.0/APIReference/API_PatchSummary.md") in the
_AWS Security Hub API Reference_.

### Latency for

sending findings

When Patch Manager creates a new finding, it's usually sent to Security Hub within a
few seconds to 2 hours. The speed depends on the traffic in the AWS Region
being processed at that time.

### Retrying when Security Hub

isn't available

If there is a service outage, an AWS Lambda function is run to put the
messages back into the main queue after the service is running again. After
the messages are in the main queue, the retry is automatic.

If Security Hub isn't available, Patch Manager retries sending the findings until
they're received.

### Viewing findings in

Security Hub

This procedure describes how to view findings in Security Hub about managed nodes
in your fleet that are out of patch compliance.

###### To review Security Hub findings for patch compliance

1. Sign in to the AWS Management Console and open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose
   **Findings**.
3. Choose the **Add filters** (
   ![The Search icon](images/search-icon.png)
   ) box.
4. In the menu, under **Filters**, choose
   **Product name**.
5. In the dialog box that opens, choose **is** in
   the first field and then enter `Systems Manager
Patch Manager` in the second field.
6. Choose **Apply**.
7. Add any additional filters you want to help narrow down your
   results.
8. In the list of results, choose the title of a finding you want
   more information about.

A pane opens on the right side of the screen with more details
about the resource, the issue discovered, and a recommended
remediation.

###### Important

At this time, Security Hub reports the resource type of all managed
nodes as `EC2 Instance`. This includes on-premises
servers and virtual machines (VMs) that you have registered for
use with Systems Manager.

###### Severity classifications

The list of findings for `Systems Manager Patch
 Manager` includes a report of the severity of the
finding. **Severity** levels include the following,
from lowest to highest:

- **INFORMATIONAL** – No issue was
  found.
- **LOW** – The issue does not require
  remediation.
- **MEDIUM** – The issue must be addressed
  but is not urgent.
- **HIGH** – The issue must be addressed as
  a priority.
- **CRITICAL** – The issue must be
  remediated immediately to avoid escalation.

Severity is determined by the most severe noncompliant package on an
instance. Because you can have multiple patch baselines with multiple
severity levels, the highest severity is reported out of all the
noncompliant packages. For example, suppose you have two noncompliant
packages where the severity of package A is "Critical" and the severity of
package B is "Low". "Critical" will be reported as the severity.

Note that the severity field correlates directly with the Patch Manager
`Compliance` field. This is a field that you set assign to
individual patches that match the rule. Because this `Compliance`
field is assigned to individual patches, it is not reflected at the Patch
Summary level.

**Related content**

- [Findings](../../../securityhub/latest/userguide/securityhub-findings.md "../../../securityhub/latest/userguide/securityhub-findings.md") in the
  _AWS Security Hub User Guide_
- [Multi-Account patch compliance with Patch Manager and Security
  Hub](https://aws.amazon.com/blogs/mt/multi-account-patch-compliance-with-patch-manager-and-security-hub/ "https://aws.amazon.com/blogs/mt/multi-account-patch-compliance-with-patch-manager-and-security-hub/") in the _AWS Management & Governance
  Blog_

## Typical finding from

Patch Manager

Patch Manager sends findings to Security Hub using the [AWS
Security Finding Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md").

Here is an example of a typical finding from Patch Manager.

```
{
  "SchemaVersion": "2018-10-08",
  "Id": "arn:aws:patchmanager:us-east-2:111122223333:instance/i-02573cafcfEXAMPLE/document/AWS-RunPatchBaseline/run-command/d710f5bd-04e3-47b4-82f6-df4e0EXAMPLE",
  "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/ssm-patch-manager",
  "GeneratorId": "d710f5bd-04e3-47b4-82f6-df4e0EXAMPLE",
  "AwsAccountId": "111122223333",
  "Types": [
    "Software & Configuration Checks/Patch Management/Compliance"
  ],
  "CreatedAt": "2021-11-11T22:05:25Z",
  "UpdatedAt": "2021-11-11T22:05:25Z",
  "Severity": {
    "Label": "INFORMATIONAL",
    "Normalized": 0
  },
  "Title": "Systems Manager Patch Summary - Managed Instance Non-Compliant",
  "Description": "This AWS control checks whether each instance that is managed by AWS Systems Manager is in compliance with the rules of the patch baseline that applies to that instance when a compliance Scan runs.",
  "Remediation": {
    "Recommendation": {
      "Text": "For information about bringing instances into patch compliance, see 'Remediating out-of-compliance instances (Patch Manager)'.",
      "Url": "https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-compliance-remediation.html"
    }
  },
  "SourceUrl": "https://us-east-2.console.aws.amazon.com/systems-manager/fleet-manager/i-02573cafcfEXAMPLE/patch?region=us-east-2",
  "ProductFields": {
    "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-2::product/aws/ssm-patch-manager/arn:aws:patchmanager:us-east-2:111122223333:instance/i-02573cafcfEXAMPLE/document/AWS-RunPatchBaseline/run-command/d710f5bd-04e3-47b4-82f6-df4e0EXAMPLE",
    "aws/securityhub/ProductName": "Systems Manager Patch Manager",
    "aws/securityhub/CompanyName": "AWS"
  },
  "Resources": [
    {
      "Type": "AwsEc2Instance",
      "Id": "i-02573cafcfEXAMPLE",
      "Partition": "aws",
      "Region": "us-east-2"
    }
  ],
  "WorkflowState": "NEW",
  "Workflow": {
    "Status": "NEW"
  },
  "RecordState": "ACTIVE",
  "PatchSummary": {
    "Id": "pb-0c10e65780EXAMPLE",
    "InstalledCount": 45,
    "MissingCount": 2,
    "FailedCount": 0,
    "InstalledOtherCount": 396,
    "InstalledRejectedCount": 0,
    "InstalledPendingReboot": 0,
    "OperationStartTime": "2021-11-11T22:05:06Z",
    "OperationEndTime": "2021-11-11T22:05:25Z",
    "RebootOption": "NoReboot",
    "Operation": "SCAN"
  }
}
```

## Turning on and configuring the

integration

To use the Patch Manager integration with Security Hub, you must turn on Security Hub. For
information about how to turn on Security Hub, see [Setting up
Security Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md") in the _AWS Security Hub User Guide_.

The following procedure describes how to integrate Patch Manager and Security Hub when
Security Hub is already active but Patch Manager integration is turned off. You only need to
complete this procedure if integration was manually turned off.

###### To add Patch Manager to Security Hub integration

1. In the navigation pane, choose **Patch Manager**.
2. Choose the **Settings** tab.

-or-

If you are accessing Patch Manager for the first time in the current
AWS Region, choose **Start with an overview**, and
then choose the **Settings** tab. 3. Under the **Export to Security Hub** section, to the right
of **Patch compliance findings aren't being exported to Security
Hub**, choose **Enable**.

## How to stop sending

findings

To stop sending findings to Security Hub, you can use either the Security Hub console or the
API.

For more information, see the following topics in the _AWS Security Hub User Guide_:

- [Disabling and enabling the flow of findings
  from an integration (console)](../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-console "../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-console")
- [Disabling the flow of findings from an
  integration (Security Hub API, AWS CLI)](../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-disable-api "../../../securityhub/latest/userguide/securityhub-integrations-managing.md#securityhub-integration-findings-flow-disable-api")
