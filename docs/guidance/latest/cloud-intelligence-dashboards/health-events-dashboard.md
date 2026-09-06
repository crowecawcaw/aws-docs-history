

# Health Events Dashboard
<a name="health-events-dashboard"></a>

## Introduction
<a name="introduction"></a>

 [AWS Health](https://aws.amazon.com/premiumsupport/technology/aws-health/) is the authoritative data source for events and changes affecting your AWS cloud resources. Through a centralized view across your organization, AWS Health integrates with 200\+ AWS services to aggregate important information in a timely manner. AWS Health notifies you about service events, planned changes, and other account matters to help you manage your resources and take actions where necessary.

The CID Health Events Dashboard uses data collected from [AWS Health Organizational View API](https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html) and creates a variety of visualizations for your past, current, and upcoming AWS Health events. The dashboard’s charts allow you to analyze individual or multiple events to raise awareness and facilitate your operational planning.

Some of the features of this dashboard include:
+ Drill down from summary views to granular details - See the most impactful events and drill down to lists of affected resources
+ Deprecating versions tracking - Analyze and plan for deprecating versions of different AWS services, such as RDS and Lambda
+ Upcoming event timeline - See the scope and dates of future events to facilitate operational planning
+ Consolidation - Centralized view of all accounts in an organization or across multiple payer accounts

The Data Collection Stack uses AWS Organizations API to collect daily the AWS Health data. See more in [prerequisites](#health-event-dashboard-prerequisites).

**Note**  
Please note that the data on this dashboard may have a lag of 48 hours or more. Please do not use this dashboard for monitoring or real time operational events. This dashboard is exclusively for review and longer term operational planning. Please use [AWS Health Notifications](https://docs.aws.amazon.com/health/latest/ug/manage-user-notifications.html) to get the real time information when needed.

**Note**  
AWS Health might not include records of events that occurred in your organization before you enabled the organizational view feature. This limitation also applies to scheduled change announcements.

**Note**  
You must have a Business, Enterprise On-Ramp, or Enterprise Support plan from AWS Support to use the AWS Health API.

## Architecture
<a name="architecture"></a>

We recommend installing the Health Events Dashboards in a separate Data Collection Account (Can be the same with your other CID dashboards).

![Architecture](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/aws-health-archi.png)


1. The [Data Collection Stack](data-collection.md) provides an Amazon Lambda function that assumes a role in one or multiple Management accounts to retrieve daily the AWS Health Data and store it on Amazon S3. The Lambda only pulls data that has been updated since the last retrieval. The stack also provides AWS Glue Tables to query collected data.

1. Cloud Intelligence Dashboards provide Amazon Athena views for querying data directly from the S3 bucket using an AWS Glue tables and Amazon Quick Sight Datasets and Dashboards, allowing Operations Teams to access AWS Health data. Access can be secured through AWS IAM, IIC (SSO), and optional Row Level Security.

## Demo Dashboard
<a name="demo-dashboard"></a>

Get more familiar with the Dashboard using the live, interactive demo dashboard following this [link](https://cid.workshops.aws.dev/demo/?dashboard=health-events-dashboard) 

![Health Dashboard Screenshot](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/he_dashboard.png)


## Prerequisites
<a name="health-event-dashboard-prerequisites"></a>

1. Enable AWS Health events across accounts with organizational view.

   For this dashboard you need to [enable the organizational view of Health events](https://docs.aws.amazon.com/health/latest/ug/enable-organizational-view-in-health-console.html#enable-organizational-view-console). By default, you can use AWS Health to view the AWS Health events of a single AWS account. If you use AWS Organizations, you can also view AWS Health events centrally across your organization. This feature provides access to the same information as single account operations and it is the mechanism used to render this dashboard. You must have a Business, Enterprise On-Ramp, or Enterprise Support plan from AWS Support to use the AWS Health API.

1. Deploy or update [Data Collection Lab](data-collection.md) and make sure Health Events Data Collection Module is enabled. Version 3.0.8 or higher required.

1. Prepare Athena

   If this is the first time you will be using Athena you will need to complete a few setup steps before you are able to create the views needed. If you are already a regular Athena user you can skip these steps and move on to the Enable Amazon Quick Sight section below.

### Click here to get Athena warmed up
<a name="collapsible-section-id-health-events-dashboard-1"></a>

1. From the services list, choose **S3** 

1. Create a new S3 bucket for Athena queries to be logged to. Keep to the same region as the S3 bucket created for your Compute Optimizer data created via Data Collection Lab.

1. From the services list, choose **Athena** 

1. Select **Get Started** to enable Athena and start the basic configuration  
![Athena getting started page from the AWS console](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/co_athena.png)

1. At the top of this screen select **Before you run your first query, you need to set up a query result location in Amazon S3**.  
![Athena Query editor in the AWS console](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/co_athena_v2.png)

1. Validate your Athena primary workgroup has an output location by
   + Open a new tab or window and navigate to the **Athena** console
   + Select **Workgroup: primary**   
![Athena Query editor with primary workgroup highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/co_athena_v3.png)
   + Confirm your **Query result location** is configured with an S3 bucket path.
     + If not configured, continue to setting up by clicking **Edit workgroup**   
![Athena workgroup settings with the edit workgroup button highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/co_athena_v4.png)
   + Add the **S3 bucket path** you have selected for your Query result location and click save  
![Athena edit workgroup with the query results location input highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/co_athena_v5.png)

1. Enable Amazon Quick Sight

   Amazon Quick Sight is the AWS Business Intelligence tool that will allow you to not only view the Standard AWS provided insights into all of your accounts, but will also allow to produce new versions of the Dashboards we provide or create something entirely customized to you. If you are already a regular Amazon Quick Sight user you can skip these steps.

### Click here to get started with Amazon Quick Sight
<a name="collapsible-section-id-health-events-dashboard-2"></a>

1. Log into your AWS Account and search for **Quick Sight** in the list of Services

1. You will be asked to **sign up** before you will be able to use it  
![Page with a button to sign up for Amazon Quick Sight](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/qs.png)

1. After pressing the **Sign up** button you will be presented with 2 options, please ensure you select the **Enterprise Edition** during this step

1. Select **continue** and you will need to fill in a series of options in order to finish creating your account.
   + Ensure you select the region that is most appropriate based on where your S3 Bucket is located containing your CO report files.  
![Quick Sight configuration page with the Amazon S3 checkbox highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/co_qs_v2.png)
   + Enable the Amazon S3 option and select the bucket where your Compute Optimizer data created via Data Collection Lab are located  
![Quick Sight Amazon S3 bucket selection dialog](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/co_qs_v3.png)

1. Click **Finish** & wait for the congratulations screen to display

1. Click **Go to Amazon Quick Sight**   
![Amazon Quick Sight finished configuration page with button to go to Quick Sight](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/co_qs_v4.png)

1. Check you have **Amazon Quick Sight Enterprise Edition**   
![Quick Sight page with callouts to select Manage Quick Sight from the menu to confirm the Quick Sight edition](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/co_qs_v5.png)

## Deployment
<a name="deployment"></a>

**Example**  
 **Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) 

1. Log in to your **Data Collection** Account. 1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Health-Events-Dashboard&param_DashboardId=health-events-dashboard&param_RequiresDataCollection=yes) 

1. You can change **Stack name** for your template if you wish.

1. Leave **Parameters** values as they are.

1. Review the configuration and click **Create stack**.

1. You will see the stack will start in **CREATE\_IN\_PROGRESS**. Once complete, the stack will show **CREATE\_COMPLETE** 

1. You can check the stack output for dashboard URLs.
**Note**  
 **Troubleshooting:** If you see error "No export named cid-CidExecArn found" during stack deployment, make sure you have completed prerequisite steps.
An alternative method to install dashboards is the [cid-cmd](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd) tool.  

1. Log in to your **Data Collection** Account.

1. Open up a command-line interface with permissions to run API requests in your AWS account. We recommend using [CloudShell](https://console.aws.amazon.com/cloudshell).

1. In your command-line interface run the following command to download and install the CID CLI tool:

   ```
    pip3 install --upgrade cid-cmd
   ```

1. In your command-line interface run the following command to deploy the dashboard:

   ```
    cid-cmd deploy --dashboard-id health-events-dashboard
   ```

   Please follow the instructions from the deployment wizard. More info about command line options are in the [Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd) or `cid-cmd --help`.

## Update
<a name="update"></a>

Please note that dashboards are not updated with update of CloudFormation Stack. When a new version of the dashboard template is released, you can update your dashboard by running the following command in your command-line interface:

```
 cid-cmd update --dashboard-id health-events-dashboard
```

## Authors
<a name="authors"></a>
+ Eric Christensen, Senior Technical Account Manager
+ Iakov Gan, Ex-Amazonian

## Contributors
<a name="contributors"></a>
+ Yuriy Prykhodko, Principal Technical Account Manager

## Feedback & Support
<a name="health-events-dashboard-feedback-support"></a>

Follow [Feedback & Support](feedback-support.md) guide

**Note**  
These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.