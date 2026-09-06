

# Deployment In China
<a name="deployment-in-china"></a>

**Note**  
For deployments in AWS China Regions, please note there are specific regional considerations and limitations. For all other AWS Regions, please follow the [standard deployment guide](deployment-in-global-regions.md) 

## Architecture
<a name="architecture"></a>

There are 2 options how you can analyze your Cost and Usage. You can consolidate all your Cost and Usage data to Global Regions (for example using [Data Transfer Hub](https://github.com/aws-solutions/data-transfer-hub)) or you can deploy Cloud Intelligence Dashboards in China Regions. Here we will provide a specific guidance for deployment in China Regions.

We recommend deployment of the Dashboards in a dedicated Data Collection Account, other than your Management (Payer) Account. This guidance provides a CloudFormation template to copy Cost and Usage Report(CUR) data from your Management Account to the dedicated one. You can use it to aggregate data from multiple Management Accounts or multiple Linked Accounts.

If you do not have access to the Management/Payer Account, you can still collect the data across multiple Linked accounts using the same approach.

![Foundational Architecture](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/china/china-foundamental-architecture.png)


1.  [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-data-exports/) delivers daily the Cost & Usage data to an [Amazon S3 Bucket](https://aws.amazon.com/s3/) in the Management Account.

1.  [Amazon S3](https://aws.amazon.com/s3/) replication rule copies CUR data to a dedicated Data Collection Account S3 bucket automatically.

1.  [Amazon Athena](https://aws.amazon.com/athena/) allows querying data directly from the S3 bucket using an [AWS Glue](https://aws.amazon.com/glue/) table schema definition.

1.  [Amazon Quick Sight](https://aws.amazon.com/quicksight/) creates datasets from [Amazon Athena](https://aws.amazon.com/athena/), refreshes daily and caches in [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html)(Super-fast, Parallel, In-memory Calculation Engine) for [Amazon Quick Sight](https://aws.amazon.com/quicksight/) 

1. User Teams (Executives, FinOps, Engineers) can access Cloud Intelligence Dashboards in [Amazon Quick Sight](https://aws.amazon.com/quicksight/). Access is secured through [AWS IAM](https://aws.amazon.com/iam/), IIC ([AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/), formerly SSO), and optional [Row Level Security](https://catalog.workshops.aws/awscid/en-US/customizations/row-level-security).

## Deployment
<a name="deployment"></a>

![Deployment Steps](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/china/china-deploy-simple.png)


Deployment process consists of 3 main steps:

1. Deploy Amazon S3 Bucket and Athena Tables in the **Data Collection Account** 

1. Amazon S3 Bucket and a replication policy in **Source** Accounts (one or many)

1. Deploy Cloud Intelligence Dashboards (CID) Stack in the **Data Collection Account** 

## Deployment
<a name="deployment-2"></a>

### Before you start
<a name="before-you-start"></a>

1. Choose **Beijing Region (cn-north-1)** for your deployment as Quick Sight is only available in this region for AWS China.

1. Define your Data Collection Account. Create or reuse an existing shared account. We do not recommend using the Management(Payer) Account for data collection.

1. Make sure you have permissions for deploying CloudFormation Stacks.

#### See Required Permissions
<a name="collapsible-section-id-deployment-in-china-1"></a>
+ In the Management/Payer Account you will need permission to access AWS CloudFormation, AWS Cost & Usage Reports, AWS IAM, AWS Lambda and Amazon S3.
+ In the Data Collection Account you will need permission to access Amazon Athena, AWS CloudFormation, AWS Directory Service, Amazon EventBridge, AWS Glue, AWS IAM, AWS Lambda, Amazon Quick Sight, and Amazon S3 via both the console and the Command Line Tool.
+ For a CLI deployment, you will not require CloudFormation permissions.
+ You can use this CloudFormation template to provision an IAM role with minimal permissions required for dashboard deployment. It takes an IAM role name as a parameter and adds the required policies to the role.

### Step 1. [Data Collection Account] Create Destination For CUR Aggregation
<a name="step-1-data-collection-account-create-destination-for-cur-aggregation"></a>

1. Sign in to your Data Collection Account.

1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation console. This Stack will create bucket open for replication and Athena Tables.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.amazonaws.cn/cloudformation/home?region=cn-north-1#/stacks/quickcreate?&templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cur-aggregation.yaml&stackName=CID-CUR-Destination&param_CreateCUR=False&param_DestinationAccountId=REPLACE%20WITH%20THE%20CURRENT%20ACCOUNT%20ID&param_SourceAccountIds=PUT%20HERE%20PAYER%20ACCOUNT%20ID) 

### Step 2. [Source/Management Account] Create CUR and Configure Replication
<a name="step-2-sourcemanagement-account-create-cur-and-configure-replication"></a>

1. Sign in to your Source Account (Management/Payer Account).

1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation console.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.amazonaws.cn/cloudformation/home?region=cn-north-1#/stacks/quickcreate?&templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cur-aggregation.yaml&stackName=CID-CUR-Replication&param_CreateCUR=True&param_DestinationAccountId=REPLACE%20WITH%20DATA%20COLLECTION%20ACCOUNT%20ID&param_SourceAccountIds=) 

### Step 3. [Data Collection Account] Deploy Dashboards
<a name="step-3-data-collection-account-deploy-dashboards"></a>

#### 3.1 - Prepare Amazon Quick Sight (Quick)
<a name="3-1-prepare-amazon-quick-sight-quick"></a>

##### Click here to expand Amazon Quick Sign Up Workflow for AWS China Beijing Region
<a name="collapsible-section-id-deployment-in-china-2"></a>

**Note**  
Quick is only available in cn-north-1 Beijing region for AWS China

1. Sign in to your Data Collection Account and navigate to the AWS Management Console and search for **Quick** in the services menu.

1. Select **Sign up for Quick** if this is your first time accessing the service.

1. On the Quick setup page, you’ll need to choose an authentication method:
   +  **IAM Identity Center** - Recommended for simplified user management and SSO capabilities
   +  **Active Directory** - Suitable for enterprises with existing AD infrastructure

     You cannot change authentication method after the initial setup. You will need to re-create the Amazon Quick account.

1. If selecting IAM Identity Center:
   + Configure user groups for Quick access levels (Admin/Reader)
   + Follow the [IAM Identity Center user management guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/addusers.html) to set up groups and permissions

Note: Choose your authentication method based on your organization’s requirements and existing identity management infrastructure.

1. At the bottom of the sign up page, there is an optional add-on for Pixel-Perfect Reports:

**Note**  
Make sure to uncheck Pixel-Perfect Reports option unless specifically needed, as it incurs additional charges. This feature can be enabled later if needed.

![Quick Sight configuration page - uncheck Pixel-Perfect Reports option](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/pixel-perfect-china.png)


1. Complete the account creation:
   + Select the appropriate Authentication method
   + Enter a unique name for your Quick account
   + Enter an email address for notifications
   + (Optional) Click Select S3 buckets and choose all cid buckets (cid-\*)
   + Click Finish and wait for the congratulations screen

#### 3.2 - Deploy Foundational Dashboards
<a name="3-2-deploy-foundational-dashboards"></a>

**Note**  
To avoid cross-region data transfer costs, use the Beijing Region (cn-north-1) - the only region where Quick is available in China.

1. Sign in to your Data Collection Account.

1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation console.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.amazonaws.cn/cloudformation/home?region=cn-north-1#/stacks/quickcreate?&templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-cfn.yml&stackName=Cloud-Intelligence-Dashboards&param_DeployCUDOSv5=yes&param_DeployKPIDashboard=yes&param_DeployCostIntelligenceDashboard=yes&param_CreateLocalAssetsBucket=yes&param_CURVersion=1.0&param_KeepLegacyCURTable=yes&param_CurrencySymbol=JPY) 

1. Configure stack parameters:

##### Click here to expand Amazon Quick Sign Up Workflow for AWS China Beijing Region
<a name="collapsible-section-id-deployment-in-china-3"></a>
+ Enter a Stack name for your template such as Cloud-Intelligence-Dashboards
+ Review Common Parameters and confirm prerequisites before specifying the other parameters. You must answer "yes" to both prerequisites questions.
+ Copy and paste your **Quick SightUserName** into the parameter text box. To find your Quick Sight username:
  + Open a new tab or window and navigate to the **Quick Sight** console
  + Find your username from the person icon in the top right corner  
![Quick Sight page with username drop down in the top right highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/cd_dash_qs_china.png)
+ Select the Dashboards you want to install. We recommend deploying all three: Cost Intelligence Dashboard, CUDOS, and the KPI Dashboard.
+ Make sure Parameters **CreateLocalAssetsBucket** set to **yes** and **CURVersion** set to **1.0** 
+ The **CurrencySymbol** parameter is defaulted to JPY (Japanese Yen - ¥). Please select the appropriate symbol from the dropdown option to match your CUR settings.
+ Review the configuration, select the checkbox **I acknowledge that Amazon CloudFormation might create IAM resources with custom names**, and click **Create stack**.
+ You will see the stack will start in **CREATE\_IN\_PROGRESS**. This step can take \~20 minutes. Once complete, the stack will show **CREATE\_COMPLETE** 

**Note**  
Dashboards will be empty initially. We recommend initiating a backfill via Support Cases

### Step 4 (optional). Request Data Backfill
<a name="step-4-optional-request-data-backfill"></a>

You can create a Support Case requesting a back-fill of your Cost And Usage Report with up to 14 months of historical data. Case must be created from each of your Source Accounts (typically Management/Payer Accounts).

## Post-Deployment Steps
<a name="post-deployment-steps"></a>

After successful deployment:

1. Check stack outputs for dashboard URLs

1. Verify Quick Sight access

1. Wait for data to populate (typically 24-48 hours for first data delivery)

1. Consider requesting a backfill through AWS Support if you need historical data

## FAQ
<a name="deployment-in-china-faq"></a>

### How can I see AWS Usage in China and other Partitions?
<a name="how-can-i-see-aws-usage-in-china-and-other-partitions"></a>
+ You can consolidate Cost and Usage report from China and Global regions in one account (can be in any partition of your choice). We recommend using [Data Transfer Hub](https://github.com/aws-solutions/data-transfer-hub). Please consult with your legal team before moving data across AWS Partitions. If you aggregate data in different currencies you might need additionally a [currency conversion](spend-in-local-currency.md).

#### See Sample Architecture
<a name="collapsible-section-id-deployment-in-china-4"></a>

![Data Transfer Architecture](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/china/china-cur-transfer.png)


1. Amazon S3 replicates AWS CUR data from a Management account in Global region to a Data Collection Account.

1. Cloud Intelligence Dashboards leverage Amazon Athena and Amazon Quick Sight for visualization.

1.  [Data Transfer Hub](https://github.com/aws-solutions/data-transfer-hub) moves data from China region to the Data collection account in Global Region.

1. Additional solution can be used for pulling up to date exchange rate information from a 3rd party source.

### What dashboards are available in China?
<a name="what-dashboards-are-available-in-china"></a>
+ At the moment only Foundational Dashboards (CUDOS, CID, KPI) are available. We are working on other dashboards as well.

Other questions? Visit our [FAQs](faq.md).