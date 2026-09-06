

# Deployment
<a name="data-collection-deployment"></a>

Deployment of the stack consists of 2 steps. First step is in Management Account and the 2nd in Data Collection Account. If you do not have access to Management Account please follow this [guide](data-collection-without-org.md).

![Data Collection architecture diagram](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/data-collection/deployment-steps.png)


## Prerequisites for deployment
<a name="prerequisites-for-deployment"></a>
+ Access to the **Management AWS Account** of the AWS Organization to deploy CloudFormation. You need permissions in the Management Account to create an IAM role and policy and deploy CloudFormation Stacks and StackSets. **Note:** If you do not have access to the Management Account, you can perform an [alternate deployment](data-collection-without-org.md) of certain modules with a manually created list of Linked Accounts.
+ Access to a Linked Account - referred as **Data Collection Account** 
+ Deployment can be only done in following **regions**: (eu-west-1, us-east-2, us-east-1, us-west-1, us-west-2, ap-southeast-1, eu-central-1, eu-central-2, eu-west-2, eu-north-1, eu-south-1, ap-southeast-2, ap-south-1, ap-northeast-3, ap-northeast-2, ap-northeast-1, ca-central-1, eu-west-3, sa-east-1). Please make sure you choose one of these regions to install the Data Collection stack.
+ Lambda [concurrent executions limit](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) of at least 500 (1000 is recommended) in your Data Collection Account. Most accounts will have the regular default of 1000. But depending upon how your account was provisioned, such as through Control Tower, it may have a default limit of only 10, which is insufficient for effective operation. You can check and increase your limit via the [Service Quotas console](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/lambda/quotas).
+ The Trusted Advisor and Support Cases Modules of Data Collection require a Business, Enterprise On-Ramp, or Enterprise Support plan. Please see more information about prerequisites of individual modules [on GitHub](https://github.com/awslabs/cid-framework/tree/main/data-collection#modules) 

## Step 1. [In Management Accounts] Deploy the Read Permissions stack
<a name="step-1-in-management-accounts-deploy-the-read-permissions-stack"></a>

Prerequisites: Make sure the [trusted access with AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html) is activated. The Management Account stack makes use of [stack sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) configured to use [service-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stacksets-concepts-stackset-permission-models) to deploy stack instances to linked accounts in the AWS Organization. Typically in Organizations it is already the case. For the new Organization you can activate it by going to [StakSet page of CloudFormation](https://console.aws.amazon.com/cloudformation/home?#/stacksets) if this access is not activated, you will see the banner with an action button to do so. **Note:** If you do not have access to the Management Account, you can perform an [alternate deployment](data-collection-without-org.md) of certain modules with a manually created list of Linked Accounts.

Login to Management Account and click Launch Stack for deploying [Permission Stack](https://github.com/awslabs/cid-framework/tree/main/data-collection/deploy/deploy-data-read-permissions.yaml):

 [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?&templateURL=https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-read-permissions.yaml&stackName=CidDataCollectionReadPermissionsStack&param_DataCollectionAccountID=REPLACE%20WITH%20DATA%20COLLECTION%20ACCOUNT%20ID&param_AllowModuleReadInMgmt=yes&param_OrganizationalUnitID=REPLACE%20WITH%20ORGANIZATIONAL%20UNIT%20ID&param_IncludeBackupModule=no&param_IncludeBudgetsModule=no&param_IncludeComputeOptimizerModule=yes&param_IncludeCostAnomalyModule=yes&param_IncludeECSChargebackModule=no&param_IncludeInventoryCollectorModule=yes&param_IncludeRDSUtilizationModule=no&param_IncludeRightsizingModule=no&param_IncludeTAModule=yes&param_IncludeTransitGatewayModule=no&param_IncludeHealthEventsModule=yes&param_IncludeCostOptimizationHubModule=no&param_IncludeLicenseManagerModule=yes) 

### More info
<a name="collapsible-section-id-data-collection-deployment-1"></a>

1. To ensure full visibility of data across your organization accounts, in the parameters section, we recommend to pass the Organization Root ID as the organizational unit parameter (OrganizationalUnitID). You can check it here: https://console.aws.amazon.com/organizations/v2/home/accounts

![Organization Root ID](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/data-collection/update-process/data-read-permissions/2a-find-organisation-root-id.png)


![Data Read Role CloudFormation stack - parameters](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/data-collection/update-process/data-read-permissions/2b-data-read-permissions-stack-create-parameters.png)


1. Make sure to select all modules that you want to allow access to your organization accounts data. You can check the list of the modules [on GitHub](https://github.com/awslabs/cid-framework/tree/main/data-collection#modules).

![Data Read Role CloudFormation - modules selection](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/data-collection/update-process/data-read-permissions/2c-data-read-permissions-stack-create-modules.png)


1. Please make sure you specify **Data Collection Account Id** correctly. It is not the Management Account Id; it’s an ID of the dedicated Data Collection Account.

1. Click **Next** at the bottom of the **Specify stack details** stage, and then, click **Next** again at the bottom of the **Configure stack options** stage to move to the **Review** stage. Click **Submit** at the end of the **Review** stage to initiate the update. This process will take a few minutes until completion.

## Step 2. [In Data Collection Account] Deploy the Data Collection Stack
<a name="step-2-in-data-collection-account-deploy-the-data-collection-stack"></a>

Login to Data Collection Account and click Launch Stack for deploying [Data Collection Stack](https://github.com/awslabs/cid-framework/tree/main/data-collection/deploy/deploy-data-collection.yaml).

 [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?&templateURL=https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-collection.yaml&stackName=CidDataCollectionStack&param_ManagementAccountID=REPLACE%20WITH%20MANAGEMENT%20ACCOUNT%20ID&param_IncludeTAModule=yes&param_IncludeRightsizingModule=no&param_IncludeCostAnomalyModule=yes&param_IncludeInventoryCollectorModule=yes&param_IncludeComputeOptimizerModule=yes&param_IncludeECSChargebackModule=no&param_IncludeRDSUtilizationModule=no&param_IncludeOrgDataModule=yes&param_IncludeBudgetsModule=yes&param_IncludeTransitGatewayModule=no&param_IncludeHealthEventsModule=yes) 

### More Info
<a name="collapsible-section-id-data-collection-deployment-2"></a>

1. Please make sure you specify the same Prefix and Role Name parameters and the account Id of the Management Account (can be comma separated list).

1. In the same parameters section, update the regions from which data about resources will be collected. Specify at least the same regions your existing Data Collection stack uses.

![Optimization Data Collection Stack update - regions parameter](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/data-collection/update-process/data-collectors/1f-data-collection-update-compopt-regions.png)


1. Click **Next** at the bottom of the **Specify stack details** stage, and then, click **Next** again at the bottom of the **Configure stack options** stage to move to the **Review** stage. Click **Submit** at the end of the **Review** stage to initiate the update. This process will take a few minutes until completion.

After deployment you can [check the execution state](data-collection-utilize-data.md#data-collection-utilize-data-check-execution) and then install [Advanced Dashboards](dashboard-advanced.md) for collected data.

## Step 3. (Optional) [In Data Collection Account] Apply granular control over accounts, regions, and modules
<a name="step-3-optional-in-data-collection-account-apply-granular-control-over-accounts-regions-and-modules"></a>

In most cases, the Data Collection framework can be run as deployed, collecting data from all accounts in your Organization for all enabled modules and the regions defined during installation. However, in some scenarios you may need to limit certain modules to a subset of accounts, OUs, and/or regions — for example, excluding sandbox accounts from specific modules or restricting regional data collection for compliance reasons.

For detailed instructions on configuring inclusion lists, exclusion lists, and per-module allow/deny rules, see [Granular Account and Region Control over Data Collection](granular-data-collection-control.md).