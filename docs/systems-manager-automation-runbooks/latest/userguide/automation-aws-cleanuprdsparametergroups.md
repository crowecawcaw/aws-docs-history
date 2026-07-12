# `AWSSupport-CleanupRDSParameterGroups`

**Description**

The `AWSSupport-CleanupRDSParameterGroups` automation runbook removes unattached, non-default Amazon Relational Database Service (Amazon RDS) Option Groups, Parameter Groups, and Cluster Parameter Groups. Before deleting any resources, the automation includes a manual approval step to receive user confirmation. The resource deletion is controlled by the following parameters:

- `DeleteInstanceParameterGroups` (Optional): Set this flag to `true` to delete unattached Parameter Groups. The default value is `false`.
- `DeleteClusterParameterGroups` (Optional): Set this flag to `true` to delete unattached Cluster Parameter Groups. The default value is `false`.
- `DeleteOptionGroups` (Optional): Set this flag to `true` to delete unattached Option Groups. The default value is `false`.
  If you want to review the resources that would be deleted before proceeding, run the execution with these parameters set to `false`. This will provide a list of resources that are applicable for deletion if the parameters were set to `true`.

###### Important

This runbook permanently deletes Amazon RDS resources. Ensure you review the approval message carefully before confirming the deletion.

**How does it work?**

The runbook performs the following operations:

- Lists all Amazon RDS instances, clusters, and snapshots to identify which Parameter Groups, Cluster Parameter Groups, and Option Groups are currently in use.
- Identifies unattached Instance Parameter Groups that are not default groups.
- Identifies unattached Cluster Parameter Groups that are not default groups.
- Identifies unattached Option Groups that are not default groups.
- Based on the input parameters, generates an approval message listing the resources to be deleted.
- Pauses execution and waits for manual approval from the specified approvers.
- Upon approval, deletes the specified resources according to the input flags.
- Generates a final report of the deleted resources.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CleanupRDSParameterGroups "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CleanupRDSParameterGroups")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `rds:DeleteDBClusterParameterGroup`
- `rds:DeleteDBParameterGroup`
- `rds:DeleteOptionGroup`
- `rds:DescribeDBClusterParameterGroups`
- `rds:DescribeDBClusterSnapshots`
- `rds:DescribeDBClusters`
- `rds:DescribeDBInstances`
- `rds:DescribeDBParameterGroups`
- `rds:DescribeDBSnapshots`
- `rds:DescribeOptionGroups`
  Example IAM policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rds:DeleteDBClusterParameterGroup",
                "rds:DeleteDBParameterGroup",
                "rds:DeleteOptionGroup",
                "rds:DescribeDBClusterParameterGroups",
                "rds:DescribeDBClusterSnapshots",
                "rds:DescribeDBClusters",
                "rds:DescribeDBInstances",
                "rds:DescribeDBParameterGroups",
                "rds:DescribeDBSnapshots",
                "rds:DescribeOptionGroups"
            ],
            "Resource": "*"
        }
    ]
}

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-CleanupRDSParameterGroups`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CleanupRDSParameterGroups/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CleanupRDSParameterGroups/description") in Systems Manager under Documents.
2. Select Execute automation.
3. For the input parameters, enter the following:

   - **AutomationAssumeRole (Optional):**

   The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your permissions.
   - **DeleteInstanceParameterGroups (Optional):**

   Flag used to determine if all unattached Amazon RDS Instance Parameter Groups should be deleted or not. Default value is `false`.
   - **DeleteClusterParameterGroups (Optional):**

   Flag used to determine if all unattached Amazon RDS Cluster Parameter Groups should be deleted or not. Default value is `false`.
   - **DeleteOptionGroups (Optional):**

   Flag used to determine if all unattached Amazon RDS Option Groups should be deleted or not. Default value is `false`.
   - **Approvers (Required):**

   The list of AWS authenticated principals who are able to either approve or reject the action. The maximum number of approvers is 10. You can specify principals by using any of the following formats: user name, user ARN, IAM role ARN, or IAM assume role ARN.

4. Select Execute.
5. The automation initiates.
6. The document performs the following steps:

   - **`ListRDSResources`**:

   Lists Amazon RDS instances, clusters, and snapshots in order to determine the instance parameter groups, cluster parameter groups, and option groups that are currently being used.
   - **`ListInstanceParameterGroups`**:

   Lists all Amazon RDS Instance Parameter Groups and identifies which ones are unattached and non-default.
   - **`ListClusterParameterGroups`**:

   Lists all Amazon RDS Cluster Parameter Groups and identifies which ones are unattached and non-default.
   - **`ListOptionGroups`**:

   Lists all Amazon RDS Option Groups and identifies which ones are unattached and non-default.
   - **`BranchOnAutomationParameters`**:

   Evaluates the input parameters to determine if any resources should be deleted.
   - **`GenerateApprovalMessage`**:

   Generates a message listing all resources that will be deleted, based on the input parameters.
   - **`ApproveDeletion`**:

   Pauses the automation and waits for manual approval from the specified approvers.
   - **`DeleteInstanceParameterGroups`**:

   Deletes the unattached Instance Parameter Groups if the `DeleteInstanceParameterGroups` flag is set to `true`.
   - **`DeleteClusterParameterGroups`**:

   Deletes the unattached Cluster Parameter Groups if the `DeleteClusterParameterGroups` flag is set to `true`.
   - **`DeleteOptionGroups`**:

   Deletes the unattached Option Groups if the `DeleteOptionGroups` flag is set to `true`.
   - **`GenerateReport`**:

   Generates a final report of all resources that were deleted during the automation execution.

7. After completion, review the Outputs section for the detailed results of the execution.
   **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CleanupRDSParameterGroups/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CleanupRDSParameterGroups/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
