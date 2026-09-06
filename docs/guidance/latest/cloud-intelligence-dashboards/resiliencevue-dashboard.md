

# ResilienceVue Dashboard
<a name="resiliencevue-dashboard"></a>

## Introduction
<a name="introduction"></a>

The ResilienceVue Dashboard provides you with valuable insights into your current AWS workloads assessed by AWS Resilience Hub by consolidating the assessments across accounts and workloads in your AWS Organizations across all AWS Regions and Payer accounts. Out-of-the-box benefits of the ResilienceVue include (but are not limited to):
+ Monitor Application Resilience across Organization
+ Assess Application RTO/RPO targets
+ Quick visibility into Policy breaches across all accounts and regions
+ Analyze Infrastructure recommendation trends
+ Track Unimplemented operational recommendations

To learn more about AWS Resilience Hub, See:
+  [How to Manage Application Resilience using AWS Resilience hub](https://catalog.workshops.aws/aws-resilience-hub-lab/en-US) 
+  [AWS Resilience Hub - Getting Started](https://docs.aws.amazon.com/resilience-hub/latest/userguide/getting-started.html) 

## Architecture
<a name="architecture"></a>

![Architecture](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/architecture/rh_architecture.png)


1. The "[Data Collection Lab](data-collection.md)" provides an Amazon Lambda function that assumes a role in one or multiple Linked accounts to retrieve daily the AWS Resilience Hub assessment Data and store it on Amazon S3. The Lambda only pulls data that are updated since the last retrieval. The stack also provides AWS Glue Tables to query collected data.

1. Cloud Intelligence Dashboards provide Amazon Athena views for querying data directly from the S3 bucket using an AWS Glue tables and Amazon Quick Sight Datasets and Dashboards, allowing Enterprise Teams access to AWS Resilience Hub data. Access can be secured through AWS IAM, IIC (SSO), and optional Row Level Security.

## Demo Dashboard
<a name="demo-dashboard"></a>

Get more familiar with the Dashboard using the live, interactive demo dashboard following this [link](https://cid.workshops.aws.dev/demo?dashboard=resiliencevue) 

![Image of ResilienceVue dashboard in Quick Sight](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/rv_demo.png)


## Prerequisites
<a name="prerequisites"></a>

1. To assess resilience for an application, you need to [Add an application to AWS ResilienceHub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/describe-applicationlication.html). You can try AWS Resilience Hub free for 6 months, for your first 3 applications. For more information on pricing, follow [AWS Resilience Hub pricing](https://aws.amazon.com/resilience-hub/pricing/) 

1. Deploy or update [Data Collection Lab](data-collection.md) and make sure ResilienceVue Data Collection Module is enabled. Version 3.12.0 or higher required.

## Deployment
<a name="deployment"></a>

**Example**  
 **Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) 

1. Log in to your **Data Collection** Account.

1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Resiliencevue-Dashboard&param_DashboardId=resiliencevue&param_RequiresDataCollection=yes) 

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
   cid-cmd deploy --dashboard-id resiliencevue
   ```

   Please follow the instructions from the deployment wizard. More info about command line options are in the [Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd) or `cid-cmd --help`.

## Update
<a name="update"></a>

Please note that dashboards are not updated with an update of the CloudFormation Stack. When a new version of the dashboard template is released, you can update your dashboard by running the following command in your command-line interface:

```
cid-cmd update --dashboard-id resiliencevue
```

## Authors
<a name="authors"></a>
+ Subha Kalia, Senior Technical Account Manager
+ Ravindra Kori, Senior Solutions Architect
+ Praney Mahajan, Senior Technical Account Manager
+ Beau Henry, Technical Account Manager

## Contributors
<a name="contributors"></a>
+ Iakov Gan, Ex-Amazonian
+ Yuriy Prykhodko, Principal Technical Account Manager

## Feedback & Support
<a name="resiliencevue-dashboard-feedback-support"></a>

Follow [Feedback & Support](feedback-support.md) guide

**Note**  
These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.