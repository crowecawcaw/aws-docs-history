# Update

## Update Process

You can check the version of your existing Data Collection in the
description of the CloudFormation stack. If it does not contain any
version reference, then it is less then v3 and you need to [update from legacy versions](#data-collection-update-from-legacy-versions "#data-collection-update-from-legacy-versions").

Please check the full
[Change
Log on GitHub](https://github.com/awslabs/cid-framework/blob/main/data-collection/CHANGELOG.md "https://github.com/awslabs/cid-framework/blob/main/data-collection/CHANGELOG.md").

### Step 1. [In Management/Payer Account] Deploy permissions stack

1. The URL to the latest Permissions Stack CloudFormation Template is https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-read-permissions.yaml. Copy this URL and keep it at hand, you will use it to update the current stack.
2. Login to the Management/Payer Account. Open respective CloudFormation Stack and update it by providing the URL that you copied above.

### Step 2. [In Data Collection Account] Update Data Collection stack

1. The URL to the latest Data Collection CloudFormation is https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-collection.yaml. Copy this URL and keep it at hand, you will use it to update the current Data Collection stack.
2. Login to the Data Collection Account. Open respective CloudFormation Stack and update it by providing the URL that you copied above.

## Update from legacy versions

The Data Collection gets updated to increase performance and add the new
data collection modules. If you already have this lab installed via Well
Architected Labs site, you have a version 1 or 2. This update procedure
will help you updated both to the latest v3. You can check the
description of Data Collection Stack. If the description of the stack
does not contain version (ex: 3.0.0).

Watch [demo of update process from legacy version to v3](https://www.youtube.com/watch?v=vpRNkwmuOEM "https://www.youtube.com/watch?v=vpRNkwmuOEM")

### Step 1. [In Management/Payer Account] Deploy permissions stack

1. Login to your Management/Payer Account and get the Organization Root ID from the
   [AWS Organizations console](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts").

![Organization Root ID](images/data-collection/update-process/data-read-permissions/2a-find-organisation-root-id.png)

1. Install the Permission Stack in your Management/Payer Account by clicking Launch Stack below

[![Launch Stack button](/images/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?&templateURL=https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-read-permissions.yaml&stackName=CidDataCollectionDataReadPermissionsStack&param_DataCollectionAccountID=REPLACE%20WITH%20DATA%20COLLECTION%20ACCOUNT%20ID&param_AllowModuleReadInMgmt=yes&param_OrganizationalUnitID=REPLACE%20WITH%20ORGANIZATIONAL%20UNIT%20ID&param_IncludeBudgetsModule=no&param_IncludeComputeOptimizerModule=no&param_IncludeCostAnomalyModule=no&param_IncludeECSChargebackModule=no&param_IncludeInventoryCollectorModule=no&param_IncludeRDSUtilizationModule=no&param_IncludeRightsizingModule=no&param_IncludeTAModule=no&param_IncludeTransitGatewayModule=no "https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?&templateURL=https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-read-permissions.yaml&stackName=CidDataCollectionDataReadPermissionsStack¶m_DataCollectionAccountID=REPLACE%20WITH%20DATA%20COLLECTION%20ACCOUNT%20ID¶m_AllowModuleReadInMgmt=yes¶m_OrganizationalUnitID=REPLACE%20WITH%20ORGANIZATIONAL%20UNIT%20ID¶m_IncludeBudgetsModule=no¶m_IncludeComputeOptimizerModule=no¶m_IncludeCostAnomalyModule=no¶m_IncludeECSChargebackModule=no¶m_IncludeInventoryCollectorModule=no¶m_IncludeRDSUtilizationModule=no¶m_IncludeRightsizingModule=no¶m_IncludeTAModule=no¶m_IncludeTransitGatewayModule=no")

###### Note

To ensure full visibility of data across your organization accounts, in the parameters section, we recommend to pass the Organization Root ID as the organizational unit parameter (OrganizationalUnitID), to ensure the data read role stack is deployed to all accounts in your organization, allowing data collectors to access data from all your organization.

![Data Read Role CloudFormation stack - parameters](images/data-collection/update-process/data-read-permissions/2b-data-read-permissions-stack-create-parameters.png)

1. Make sure to select all modules that you want to allow access to your organization accounts data.

![Data Read Role CloudFormation - modules selection](images/data-collection/update-process/data-read-permissions/2c-data-read-permissions-stack-create-modules.png)

### Step 2. [Data Collection Account] Update Data Collection stack

1. The URL to the latest Data Collection CloudFormation is https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-collection.yaml. Copy this URL and keep it at hand, you will use it to update the current Data Collection stack.
2. Make a note of the value set on your existing Data Collection stack
   regions parameter. Previous versions of the Data Collection stack would
   have the regions in the parameter "ComputeOptimizerRegions":

![Compute Optimizer Regions parameter](images/data-collection/update-process/data-collectors/0-data-collection-stack-current-region-parameter.png)

1. Find the existing data collection stack. The default name of the data
   collection stack is **OptimizationDataCollectionStack**.

![Optimization Data Collection Stack](images/data-collection/update-process/data-collectors/1a-data-collection-stack.png)

1. Start the Data Collection stack update process by clicking on the "Update" button:

![Optimization Data Collection Stack detailed view update button](images/data-collection/update-process/data-collectors/1b-data-collection-stack-detailed-view.png)

1. Choose the option to "Replace current template", using the "Amazon S3 URL" option, and paste the URL of the latest Data Collection CloudFormation template you copied before.

![Optimization Data Collection Stack replace template entering S3 URL to new template](images/data-collection/update-process/data-collectors/1d-data-collection-update-replace-template-S3-url.png)

1. In the **Specify stack details** stage parameters section, you will find
   the parameter "Role Prefix" with the value "CID-DC-". We recommend
   to use this new prefix to avoid conflicts with any existing resources
   when updating to the latest version of the Data Collection stack.

![Optimization Data Collection Stack update - role prefix](images/data-collection/update-process/data-collectors/1e-data-collection-update-role-prefix.png)

1. In the same parameters section, update the regions from which data
   about resources will be collected. Specify at least the same regions
   your existing Data Collection stack uses.

![Optimization Data Collection Stack update - regions parameter](images/data-collection/update-process/data-collectors/1f-data-collection-update-compopt-regions.png)

1. Click **Next** at the bottom of the **Specify stack details** stage, and
   then, click **Next** again at the bottom of the **Configure stack options**
   stage to move to the **Review** stage. Click **Submit** at the end of the
   **Review** stage to initiate the update. This process will take a few
   minutes until completion.

![Optimization Data Collection Stack update - submit action](images/data-collection/update-process/data-collectors/1g-data-collection-update-submit.png)
Once updated, the new version of the Data Collection stack will be visible in the stack description.

![Optimization Data Collection Stack update complete](images/data-collection/update-process/data-collectors/1h-data-collection-update-complete.png)

### Step 3. [In Data Collection Account] Run data migration script

The workshop was updated to work for multiple management accounts, and
also minor adjustments have been applied to align the folder structure
across the data collection modules. To migrate the historical data on
your S3 bucket you can run a migration [script](https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/source/s3_files_migration.py "https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/source/s3_files_migration.py"). The script accepts
the parameter `<your_bucket_name>` which is the bucket of data
collection stack. Default in legacy versions of this lab is
`costoptimizationdata<account_id>`.

You can run following commands from your AWS CloudShell

```
curl https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/data-collection/source/s3_files_migration.py -o s3_files_migration.py
python3 s3_files_migration.py
```

### Step 4. [In Management/Payer Account] Clean up

**Delete read role stacks from v2 (OptimizationDataRoleStack)**

Before version 3.0, 2 stacks were deployed in the Management account: -
Read role stack for Management account specific data. - (Optional) Read
role stack for collector-specific data.

1. Find the current data read permissions stacks by navigating to the
   [CloudFormation
   console](https://us-east-1.console.aws.amazon.com/cloudformation/home "https://us-east-1.console.aws.amazon.com/cloudformation/home")

![Find current data read role stacks](images/data-collection/update-process/data-read-permissions/1a-find-current-data-read-permissions-stacks.png)

1. Delete the Management data read role stack. The default name of the
   stack is **OptimizationManagementDataRoleStack**.

![Management account data read role stack](images/data-collection/update-process/data-read-permissions/1b-mgmt-acc-mgmt-read-role-stack-delete.png)

1. Confirm you want to delete the stack.

![Confirm deletion of Management account data read permissions stack](images/data-collection/update-process/data-read-permissions/1c-mgmt-acc-mgmt-read-role-stack-delete-confirm.png)

1. Delete data read role stack, if installed. The default name of the
   stack is **OptimizationDataRoleStack**.

![Collectors data read role stack](images/data-collection/update-process/data-read-permissions/1d-mgmt-acc-data-read-role-stack-delete.png)

1. Confirm you want to delete the stack.

![Confirm deletion of the collectors data read permissions stack](images/data-collection/update-process/data-read-permissions/1e-mgmt-acc-data-read-role-stack-delete-confirm.png)

**Delete data read role StackSet from v2 (OptimizationDataRoleStack)**

Before version 3.0, data read permissions were deployed as a StackSet in
the Management account with the default name
**OptimizationDataRoleStack**.

1. Find the Organizational Unit the stackset is targeting by looking at
   the stackset details:

![Optimization Data Role Stack Organizational Unit IDs](images/data-collection/update-process/data-read-permissions/1f-data-read-permissions-stackset-info-ouid.png)

1. Find the data read role permission stackset in the CloudFormation
   StackSet console.

![CloudFormation StackSets console - search data read role stackset](images/data-collection/update-process/data-read-permissions/1g-find-data-read-permissions-stackset.png)

1. Delete the stacks deployed by the stackset. You can select the stackset and select the "Delete stacks from StackSet" menu option.

![Delete stacks from stackset menu option](images/data-collection/update-process/data-read-permissions/1h-data-read-permissions-stackset-delete-stacks.png)

1. Enter the Organizational Unit ID you found in step #1 and select all
   the regions the stackset is targeting. Usually, the stackset will deploy
   to a single region, for example, us-east-1. Click **Next** to move to the
   **Review** stage, and then click **Submit** to start deleting the stacks
   from the stackset. **NOTE** The deletion process can take a few minutes to
   complete.

![Delete stacks from stackset - parameters](images/data-collection/update-process/data-read-permissions/1i-data-read-permissions-stackset-delete-stacks-parameters.png)

1. After the stackset’s stacks are deleted, return to the StackSets page,
   select the data read roles stackset, and use the menu option **Delete
   StackSet** to delete it.

![Delete StackSet menu option](images/data-collection/update-process/data-read-permissions/1j-data-read-permissions-stackset-delete.png)

1. Confirm you want to delete the stacks in the set.

![Confirmation to delete stackset](images/data-collection/update-process/data-read-permissions/1k-data-read-permissions-stackset-delete-confirm.png)

### Step 5. [In Data Collection Account] Update Dashboards

After update from previous versions you might need to update dashboards
of Advanced Group to take into account the change of s3 path:

```
cid-cmd -vvv update --force --recursive --dashboard-id compute-optimizer-dashboard
cid-cmd -vvv update --force --recursive --dashboard-id ta-organizational-view
```

Please carefully verify existence of default path on S3 when asked
(mainly S3 bucket names), and adjust accordingly.

## Post Update

After deployment you can [check the execution state](data-collection-utilize-data.md#data-collection-utilize-data-check-execution "data-collection-utilize-data.md#data-collection-utilize-data-check-execution") and refresh the data by triggering the execution of Step Functions.
