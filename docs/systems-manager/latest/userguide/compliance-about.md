AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Learn details about Compliance

Compliance, a tool in AWS Systems Manager, collects and reports data about the status of
patching in Patch Manager patching and associations in State Manager. (Patch Manager and State Manager are
also both tools in AWS Systems Manager.) Compliance also reports on custom compliance types you
have specified for your managed nodes. This section includes details about each of these
compliance types and how to view Systems Manager compliance data. This section also includes
information about how to view compliance history and change tracking.

###### Note

Systems Manager integrates with [Chef
InSpec](https://www.chef.io/inspec/ "https://www.chef.io/inspec/"). InSpec is an open-source, runtime framework that
allows you to create human-readable profiles on GitHub or Amazon Simple Storage Service
(Amazon S3). Then you can use Systems Manager to run compliance scans and view compliant and
noncompliant instances. For more information, see [Using Chef InSpec profiles
with Systems Manager Compliance](integration-chef-inspec.md "integration-chef-inspec.md").

## About patch compliance

After you use Patch Manager to install patches on your instances, compliance status
information is immediately available to you in the console or in response to
AWS Command Line Interface (AWS CLI) commands or corresponding Systems Manager API operations.

For information about patch compliance status values, see [Patch compliance state
values](patch-manager-compliance-states.md "patch-manager-compliance-states.md").

## About State Manager association

compliance

After you create one or more State Manager associations, compliance status information
is immediately available to you in the console or in response to AWS CLI commands or
corresponding Systems Manager API operations. For associations, Compliance shows statuses of
`Compliant` or `Non-compliant` and the severity level
assigned to the association, such as `Critical` or
`Medium`.

When State Manager executes an association on a managed node, it triggers a compliance
aggregation process that updates compliance status for all associations on that
node. The `ExecutionTime` value in compliance reports represents when the
compliance status was captured by Systems Manager, not when the association was executed on
the managed node. This means multiple associations might display identical
`ExecutionTime` values even if they were executed at different times.
To determine actual association execution times, refer to the association execution
history using the AWS CLI command
[describe-association-execution-targets](../../../cli/latest/reference/ssm/describe-association-execution-targets.md "../../../cli/latest/reference/ssm/describe-association-execution-targets.md") or by viewing the execution
details in the console.

## About custom compliance

You can assign compliance metadata to a managed node. This metadata can then be
aggregated with other compliance data for compliance reporting purposes. For
example, say that your business runs versions 2.0, 3.0, and 4.0 of software X on
your managed nodes. The company wants to standardize on version 4.0, meaning that
instances running versions 2.0 and 3.0 are non-compliant. You can use the [PutComplianceItems](../APIReference/API_PutComplianceItems.md "../APIReference/API_PutComplianceItems.md") API
operation to explicitly note which managed nodes are running older versions of
software X. You can only assign compliance metadata by using the AWS CLI, AWS Tools for Windows PowerShell,
or the SDKs. The following CLI sample command assigns compliance metadata to a
managed instance and specifies the compliance type in the required format
`Custom:`. Replace each `example resource
 placeholder` with your own information.

Linux & macOS

```
aws ssm put-compliance-items \
    --resource-id `i-1234567890abcdef0` \
    --resource-type ManagedInstance \
    --compliance-type Custom:`SoftwareXCheck` \
    --execution-summary ExecutionTime=`AnyStringToDenoteTimeOrDate` \
    --items Id=`Version2.0`,Title=`SoftwareXVersion`,Severity=`CRITICAL`,Status=`NON_COMPLIANT`
```

Windows

```
aws ssm put-compliance-items ^
    --resource-id `i-1234567890abcdef0` ^
    --resource-type ManagedInstance ^
    --compliance-type Custom:`SoftwareXCheck` ^
    --execution-summary ExecutionTime=`AnyStringToDenoteTimeOrDate` ^
    --items Id=`Version2.0`,Title=`SoftwareXVersion`,Severity=`CRITICAL`,Status=`NON_COMPLIANT`
```

###### Note

The `ResourceType` parameter only supports
`ManagedInstance`. If you add custom compliance to a managed
AWS IoT Greengrass core device, you must specify a `ResourceType` of
`ManagedInstance`.

Compliance managers can then view summaries or create reports about which managed
nodes are or aren't compliant. You can assign a maximum of 10 different custom
compliance types to a managed node.

For an example of how to create a custom compliance type and view compliance data,
see [Assign custom compliance metadata using
the AWS CLI](compliance-custom-metadata-cli.md "compliance-custom-metadata-cli.md").

## Viewing current compliance data

This section describes how to view compliance data in the Systems Manager console and by
using the AWS CLI. For information about how to view patch and association compliance
history and change tracking, see [Viewing compliance configuration history and
change tracking](#compliance-history "#compliance-history").

###### Topics

- [Viewing current compliance
  data (console)](#compliance-view-results-console "#compliance-view-results-console")
- [Viewing current compliance data
  (AWS CLI)](#compliance-view-data-cli "#compliance-view-data-cli")

### Viewing current compliance

data (console)

Use the following procedure to view compliance data in the Systems Manager
console.

###### To view current compliance reports in the Systems Manager console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Compliance**.
3. In the **Compliance dashboard filtering** section,
   choose an option to filter compliance data. The **Compliance
   resources summary** section displays counts of compliance
   data based on the filter you chose.
4. To drill down into a resource for more information, scroll down to the
   **Details overview for resources** area and choose
   the ID of a managed node.
5. On the **Instance ID** or **Name**
   details page, choose the **Configuration compliance**
   tab to view a detailed configuration compliance report for the managed
   node.

###### Note

For information about fixing compliance issues, see [Remediating compliance issues using EventBridge](compliance-fixing.md "compliance-fixing.md").

### Viewing current compliance data

(AWS CLI)

You can view summaries of compliance data for patching, associations, and
custom compliance types in the in the AWS CLI by using the following AWS CLI
commands.

[list-compliance-summaries](../../../cli/latest/reference/ssm/list-compliance-summaries.md "../../../cli/latest/reference/ssm/list-compliance-summaries.md")

Returns a summary count of compliant and non-compliant association
statuses according to the filter you specify. (API: [ListComplianceSummaries](../APIReference/API_ListComplianceSummaries.md "../APIReference/API_ListComplianceSummaries.md"))

[list-resource-compliance-summaries](../../../cli/latest/reference/ssm/list-resource-compliance-summaries.md "../../../cli/latest/reference/ssm/list-resource-compliance-summaries.md")

Returns a resource-level summary count. The summary includes
information about compliant and non-compliant statuses and detailed
compliance-item severity counts, according to the filter criteria
you specify. (API: [ListResourceComplianceSummaries](../APIReference/API_ListResourceComplianceSummaries.md "../APIReference/API_ListResourceComplianceSummaries.md"))

You can view additional compliance data for patching by using the following
AWS CLI commands.

[describe-patch-group-state](../../../cli/latest/reference/ssm/describe-patch-group-state.md "../../../cli/latest/reference/ssm/describe-patch-group-state.md")

Returns high-level aggregated patch compliance state for a patch
group. (API: [DescribePatchGroupState](../APIReference/API_DescribePatchGroupState.md "../APIReference/API_DescribePatchGroupState.md"))

[describe-instance-patch-states-for-patch-group](../../../cli/latest/reference/ssm/describe-instance-patch-states-for-patch-group.md "../../../cli/latest/reference/ssm/describe-instance-patch-states-for-patch-group.md")

Returns the high-level patch state for the instances in the
specified patch group. (API: [DescribeInstancePatchStatesForPatchGroup](../APIReference/API_DescribeInstancePatchStatesForPatchGroup.md "../APIReference/API_DescribeInstancePatchStatesForPatchGroup.md"))

###### Note

For an illustration of how to configure patching and view patch compliance
details by using the AWS CLI, see [Tutorial: Patch a
server environment using the AWS CLI](patch-manager-patch-servers-using-the-aws-cli.md "patch-manager-patch-servers-using-the-aws-cli.md").

## Viewing compliance configuration history and

change tracking

Systems Manager Compliance displays _current_ patching and association
compliance data for your managed nodes. You can view patching and association
compliance history and change tracking by using [AWS Config](../../../config/latest/developerguide.md "../../../config/latest/developerguide.md"). AWS Config provides a detailed view of the configuration of AWS
resources in your AWS account. This includes how the resources are related to one
another and how they were configured in the past so that you can see how the
configurations and relationships change over time. To view patching and association
compliance history and change tracking, you must turn on the following resources in
AWS Config:

- `SSM:PatchCompliance`
- `SSM:AssociationCompliance`

For information about how to choose and configure these specific resources in
AWS Config, see [Selecting Which Resources
AWS Config Records](../../../config/latest/developerguide/select-resources.md "../../../config/latest/developerguide/select-resources.md") in the _AWS Config Developer Guide_.

###### Note

For information about AWS Config pricing, see [Pricing](https://aws.amazon.com/config/pricing/ "https://aws.amazon.com/config/pricing/").
