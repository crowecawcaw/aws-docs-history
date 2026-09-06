

# Enabling EC2 Capacity Manager with AWS Organizations
<a name="enable-capacity-manager-organizations"></a>

You can enable EC2 Capacity Manager with AWS Organizations for organization-level visibility and management of your capacity across all member accounts. This integration allows you to monitor, analyze, and manage capacity usage from a centralized location.

The management account is responsible for enabling organization-level access and managing capacity across the organization.

Enabling Capacity Manager with AWS Organizations provides the following benefits:
+ **Centralized capacity visibility** — View capacity usage across all member accounts in your organization from a single dashboard with cross-account and cross-region aggregation.
+ **Organization-wide optimization** — Identify unused Capacity Reservations and optimization opportunities across all accounts in your organization.
+ **Delegated administrator** — Allow specific member accounts to manage Capacity Manager for an organization while maintaining proper access controls.

If you don't enable integration with AWS Organizations, you can only monitor resources in the individual AWS account where you enabled Capacity Manager.

## Prerequisites
<a name="organizations-prerequisites"></a>
+ You must have an AWS Organizations setup with a management account and one or more member accounts. For more information about account types, see [Terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) in the *AWS Organizations User Guide*.
+ The management account must have permissions for the following IAM actions:
  + `organizations:EnableAwsServiceAccess`
  + `organizations:RegisterDelegatedAdministrator` (if using delegated administration)
  + `iam:CreateServiceLinkedRole`
+ You must create a service-linked role with the **AWSEC2CapacityManagerServiceRolePolicy** use case to allow AWS Organization access. For more information, see [Creating a service-linked role for Capacity Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-service-linked-roles-cm.html#create-slr).

## Enabling Capacity Manager with AWS Organizations
<a name="enable-organization-integration"></a>

Using the management account, enable organization access in Capacity Manager.

------
#### [ Console ]

**To enable organization access in Capacity Manager**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Manager**.

1. Choose the **Settings** tab.

1. In the **Trusted access** section, choose **Manage trusted access**.

1. In the prompt that appears, select **Enable trusted access**. Then, choose **Save**.

------
#### [ AWS CLI ]

**To enable organization access in Capacity Manager**

1. Create a service-linked role

   ```
   aws iam create-service-linked-role --aws-service-name ec2.capacitymanager.amazonaws.com
   ```

1. Enable AWS Organization access

   ```
   aws organizations enable-aws-service-access --service-principal ec2.capacitymanager.amazonaws.com
   ```

1. Enable Capacity Manager with AWS Organization 

   ```
   aws ec2 enable-capacity-manager --organizations-access
   ```

To update organization access for an existing Capacity Manager, run the following command:

```
aws ec2 update-capacity-manager-organizations-access --organizations-access
```

------
#### [ PowerShell ]

**To enable organization access in Capacity Manager**

1. Create a service-linked role using the [New-IAMServiceLinkedRole](https://docs.aws.amazon.com/powershell/latest/reference/items/New-IAMServiceLinkedRole.html) cmdlet.

   ```
   New-IAMServiceLinkedRole -AWSServiceName "ec2.capacitymanager.amazonaws.com"
   ```

1. Enable AWS Organization access using the [Enable-ORGAWSServiceAccess](https://docs.aws.amazon.com/powershell/latest/reference/items/Enable-ORGAWSServiceAccess.html) cmdlet.

   ```
   Enable-ORGAWSServiceAccess -ServicePrincipal "ec2.capacitymanager.amazonaws.com"
   ```

1. Enable Capacity Manager with AWS Organization using the [Enable-EC2CapacityManager](https://docs.aws.amazon.com/powershell/latest/reference/items/Enable-EC2CapacityManager.html) cmdlet.

   ```
   Enable-EC2CapacityManager -OrganizationsAccess $true
   ```

To update organization access for an existing Capacity Manager, run the following [Update-EC2CapacityManagerOrganizationsAccess](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-EC2CapacityManagerOrganizationsAccess.html) cmdlet:

```
Update-EC2CapacityManagerOrganizationsAccess -OrganizationsAccess $true
```

------

## Verifying Capacity Manager is enabled with your organization
<a name="verify-organization-integration"></a>

------
#### [ Console ]

**To verify Capacity Manager is enabled with your organization**

1. In the Capacity Manager console, choose **Settings**.

1. In the **Trusted access** section, verify that **Organization access** shows as **Enabled**.

1. Check that the **Organization ID** displays your organization's ID.

------
#### [ AWS CLI ]

**To verify Capacity Manager is enabled with your organization**  
Run the following command:

```
aws ec2 get-capacity-manager-attributes
```

The output should display:

```
{
    "CapacityManagerStatus": "enabled",
    "OrganizationsAccess": true,
    "IngestionStatus": "initial-ingestion-pending",
    "IngestionStatusMessage": "Capacity Manager is collecting historical data from 2025-10-01T00:00:00Z. Data collection is in progress and may take several hours to complete."
}
```

------
#### [ PowerShell ]

**To verify Capacity Manager is enabled with your organization**  
Use the [Get-EC2CapacityManagerAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2CapacityManagerAttribute.html) cmdlet.

```
Get-EC2CapacityManagerAttribute
```

The output should display:

```
CapacityManagerStatus      : enabled
DataExportCount            : 0
EarliestDatapointTimestamp :
IngestionStatus            : initial-ingestion-in-progress
IngestionStatusMessage     : Capacity Manager is collecting historical data from
                              2026-03-17T16:00:00Z. Data collection is in progress and may take
                              several hours to complete.
LatestDatapointTimestamp   :
OrganizationsAccess        : True
```

------

## Considerations
<a name="organizations-considerations"></a>
+ **Service-linked role creation:** When you enable organization access through the console, Capacity Manager automatically creates the AWSServiceRoleForEC2CapacityManager service-linked role in all m ember accounts. If you enable through the AWS CLI, you must call `createServiceLinkedRole` manually.
+ **Data aggregation:** After enabling organization access, Capacity Manager backfills 14 days of historical data from all member accounts. This process typically takes a few minutes to complete.
+ **Regional limitations:** You can only enable Capacity Manager in one Region per organization, but it will aggregate data from all commercial Regions.
+ **Permissions:** Member accounts don't need to take any action. Capacity Manager uses the service-linked role to automatically discover resources across all accounts.