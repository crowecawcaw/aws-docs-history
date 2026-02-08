# `AWSPremiumSupport-OnboardWorkloadToIDR`

**Description**

The **AWSPremiumSupport-OnboardWorkloadToIDR** runbook helps AWS Enterprise Support customers onboard a workload for monitoring and critical incident management using AWS Incident Detection and Response. A workload can be defined as a collection of AWS resources associated with an AWS Resource Group or AWS Service Catalog AppRegistry application. If an AWS Resource Group or an AWS Service Catalog AppRegistry application are not specified, the runbook creates a Resource Group on your behalf using tag filters or the AWS CloudFormation stack ID whose resources you want included in the group. If you set the parameter `CreateApplicationInsights` to `Yes`, then the automation provisions an Amazon CloudWatch Application Insights application using AWS CloudFormation. CloudWatch Application Insights sets up recommended metrics and logs for selected application resources using Amazon CloudWatch metrics, Logs, and Events for notifications on detected problems.

###### Important

This runbook performs the following actions in your account depending on the input parameters provided:

- Creates a new AWS Resource Group using AWS CloudFormation if `ResourceGroupName` or `AppRegistryApplication` are not specified. After the stack is created, the runbook tries to set termination protection.
- Tags the workload associated AWS Resource Group, including the `aws_idr` tag.
- Creates an Amazon CloudWatch Application Insights Resource group-based application if the `CreateApplicationInsights` input parameter is set to `Yes`. After the stack is created, the runbook tries to set termination protection for the stack.
- Installs the `AWSServiceRoleForHealth_EventProcessor` service-linked role (SLR) to provision access for alert ingestion to Incident Detection and Response if the `InstallServiceLinkedRole` input parameter is set to `Yes`.
- Creates an AWS support case with AWS Incident Detection and Response.

###### Important

To use this runbook and onboard to AWS Incident Detection and Response, you require an AWS Enterprise Support (with additional fee) or Unified Operations Subscription. For more
information, see [Compare
Support Plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/").

**How does it work?**

The runbook performs the following high-level steps:

- Checks if the current AWS Account Support Plan is Enterprise; otherwise the automation ends.
- Determines whether to use an existing AWS Resource Group or create a new one based on the provided parameters.
- If creating a new Resource Group, generates an AWS CloudFormation template and creates the stack with appropriate tags.
- Tags the Resource Group with the required AWS Incident Detection and Response tags.
- Optionally installs the service-linked role for AWS Incident Detection and Response.
- Optionally creates an Amazon CloudWatch Application Insights application for enhanced monitoring.
- Creates an AWS support case to complete the onboarding process.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-OnboardWorkloadToIDR "https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-OnboardWorkloadToIDR")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudformation:CreateStack`
- `cloudformation:DescribeStackResource`
- `cloudformation:DescribeStacks`
- `cloudformation:UpdateTerminationProtection`
- `iam:CreateServiceLinkedRole`
- `resource-groups:CreateGroup`
- `resource-groups:GetGroup`
- `resource-groups:TagResource`
- `servicecatalog-appregistry:GetApplication`
- `support:CreateCase`
- `support:DescribeSeverityLevels`
- `support:DescribeServices`
- `support:DescribeSupportLevel`
  Example Policy:

```
{
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack",
                "cloudformation:DescribeStackResource",
                "cloudformation:DescribeStacks",
                "cloudformation:UpdateTerminationProtection",
                "iam:CreateServiceLinkedRole",
                "resource-groups:CreateGroup",
                "resource-groups:GetGroup",
                "resource-groups:TagResource",
                "servicecatalog-appregistry:GetApplication",
                "support:CreateCase",
                "support:DescribeSeverityLevels",
                "support:DescribeServices",
                "support:DescribeSupportLevel"
            ],
            "Resource": "*"
            }
        ]
        }
```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSPremiumSupport-OnboardWorkloadToIDR`](https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-OnboardWorkloadToIDR/description "https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-OnboardWorkloadToIDR/description") in Systems Manager under Documents.
2. Select **Execute automation.**
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **WorkloadName (Required):**
     - Description: (Required) The name of the workload. If `ResourceGroupName` is not provided, the workload name is used to setup a new AWS Resource Group with the name `IDR-AWS-<WorkloadName>`.
     - Type: `String`
     - Allow Pattern: `^[a-zA-Z0-9_-]{1,128}$`

   - **WorkloadDescription (Required):**
     - Description: (Required) The workload description. Enter a brief description to detail the use cases of this workload. Please include the primary end user and the function of this workload.
     - Type: `String`
     - Allow Pattern: `^[a-zA-Z0-9.:;,-_&() ]{1,1024}$`

   - **AppRegistryApplication (Optional):**
     - Description: (Optional) The name or ID of the AWS Service Catalog AppRegistry application. If not provided, you must provide an input for `ResourceGroupName`.
     - Type: `String`
     - Allow Pattern: `^$|^[a-zA-Z0-9.-_]{1,128}$`
     - Default: `""`

   - **ResourceGroupName (Optional):**
     - Description: (Optional) The name of an existing AWS Resource Group if `AppRegistryApplication` is not provided. If you want to create a Resource Group, you must provide an input for `TagFilters` and optionally `ResourceTypeFilters` to create a new AWS Resource Group.
     - Type: `String`
     - Allow Pattern: `^$|^[a-zA-Z0-9_.-]{1,128}$`
     - Default: `""`

   - **TagFilters (Conditional):**
     - Description: (Conditional) The list of key/values (string/list of strings) pairs that are compared to the tags attached to your AWS resources. This parameter is used to create a new AWS Resource Group if you do not specify an existing `ResourceGroupName` or `AppRegistryApplication`.
     - Type: `StringMap`

   - **ResourceTypeFilters (Conditional):**
     - Description: (Conditional) The list of resource types supported by Resource Groups.
     - Type: `StringList`
     - Max Items: `10`
     - Default: `AWS::AllSupported`

   - **InstallServiceLinkedRole (Optional):**
     - Description: (Optional) Select `Yes` to install the `AWSServiceRoleForHealth_EventProcessor` service-linked role (SLR).
     - Type: `String`
     - Allowed Values: `[Yes,No]`
     - Default: `No`

   - **CreateApplicationInsights (Optional):**
     - Description: (Optional) Select `Yes` to create an Amazon CloudWatch Application Insights Resource group-based application.
     - Type: `String`
     - Allowed Values: `[Yes,No]`
     - Default: `No`

   - **ComplianceAndRegulatoryRequirements (Required):**
     - Description: (Required) Applicable compliance and/or regulatory requirements for this workload and any actions required from AWS after an incident.
     - Type: `String`
     - Allow Pattern: `^[a-zA-Z0-9.:;,\\-_&() ]{1,1024}$`

   - **NonAWSComponents (Optional):**
     - Description: (Optional) Detail any on-premise or non-AWS components for this workload? If so, what are they and what functions do they perform.
     - Type: `String`
     - Allow Pattern: `^$|^[a-zA-Z0-9.:;,\\-_&() ]{1,1024}$`
     - Default: `""`

   - **UpstreamDownstreamDependencies (Optional):**
     - Description: (Optional) Details of any upstream/downstream components not being onboarded, that could affect this workload if experiencing an outage.
     - Type: `String`
     - Allow Pattern: `^$|^[a-zA-Z0-9.:;,\\-_&() ]{1,1024}$`
     - Default: `""`

   - **FailoverDisasterRecoveryPlan (Optional):**
     - Description: (Optional) Provide details of any manual or automated failover/disaster recovery plans at the AZ and regional level.
     - Type: `String`
     - Allow Pattern: `^$|^[a-zA-Z0-9.:;,\\-_&() ]{1,1024}$`
     - Default: `""`

   - **BridgeDetails (Optional):**
     - Description: (Optional) The static incident/crisis management bridge established by your company. If you utilize a non-static bridge, specify your preferred application and AWS will request these details during an incident.
     - Type: `String`
     - Allowed Values: `[Amazon Chime bridge, Non-Static bridge, Static bridge]`
     - Default: `Amazon Chime bridge`

   - **SubscriptionStartDate (Required):**
     - Description: (Required) The date in `YYYY-MM-DD` format that you want to start your AWS Incident Detection and Response subscription.
     - Type: `String`
     - Allow Pattern: `^(202[4-9]|20[3-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$`

4. Select **Execute**.
5. The automation initiates.
6. The document performs the following steps:
   - **CheckAWSSupportPlan**:

   Checks if the current AWS Account Support Plan is Enterprise; otherwise the automation ends.
   - **BranchOnResourceGroup**:

   Branches the automation on whether an existing AWS Resource Group was provided. If not provided, the automation creates a new AWS Resource Group.
   - **GetAppRegistryApplication**:

   Gets metadata information about the AWS Service Catalog AppRegistry application if provided.
   - **GenerateResourceGroupTemplate**:

   Generates an AWS CloudFormation template for the AWS Resource Group with the specified tag filters.
   - **CreateResourceGroup**:

   Creates a new AWS Resource Group by using AWS CloudFormation.
   - **TagResourceGroup**:

   Tags the resource group with the AWS Incident Detection and Response (IDR) required tags.
   - **InstallServiceLinkedRole**:

   Installs the AWS Incident Detection and Response (IDR) service-linked role if requested.
   - **CreateApplicationInsightsApplication**:

   Creates an Amazon CloudWatch Application Insights application if requested.
   - **CreateAwsSupportCase**:

   Creates an AWS support case with AWS Incident Detection and Response.

7. After completion, review the **Outputs** section for the detailed results of the execution.
   **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-OnboardWorkloadToIDR/description "https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-OnboardWorkloadToIDR/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
- [Get started with AWS Incident Detection and Response](../../../IDR/latest/userguide/getting-started-idr.md "../../../IDR/latest/userguide/getting-started-idr.md")
- [Workload discovery in Incident Detection and Response](../../../IDR/latest/userguide/idr-gs-discovery.md "../../../IDR/latest/userguide/idr-gs-discovery.md")
