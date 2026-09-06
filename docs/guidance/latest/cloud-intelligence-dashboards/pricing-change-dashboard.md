

# Pricing Change Analysis Dashboard
<a name="pricing-change-dashboard"></a>

## Introduction
<a name="introduction"></a>

The Pricing Change Analysis Dashboard provides insight into the impact of AWS pricing changes on your spend, based on actual usage. It includes visualizations and tables to isolate the impacts of pricing changes based on service, payer account, linked account, and region.

![Image of a Pricing Change Analysis dashboard in Quick Sight](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/pricing_change_dashboard.png)


## Prerequisites
<a name="prerequisites"></a>

1. Deploy one or more of the foundational dashboards: [CUDOS, Cost Intelligence, or KPI Dashboard.](cudos-cid-kpi.md) 

## Deployment
<a name="deployment"></a>

**Example**  
 **Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) 

1. Log in to your **Data Collection** Account.

1. Choose the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Pricing-Change-Analysis-Dashboard&param_DashboardId=pricing-change-analysis) 

1. You can change **Stack name** for your template if you wish.

1. Leave **Parameters** values as they are.

1. Review the configuration and choose **Create stack**.

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
   cid-cmd deploy --dashboard-id pricing-change-analysis
   ```

   Please follow the instructions from the deployment wizard. More info about command line options are in the [Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd) or `cid-cmd --help`.

## Update
<a name="update"></a>

Please note that dashboards are not updated with update of CloudFormation Stack. When a new version of the dashboard template is released, you can update your dashboard by running the following command in your command-line interface:

```
cid-cmd update --dashboard-id pricing-change-analysis
```

## Authors
<a name="authors"></a>
+ Jason Walp, Senior Technical Account Manager
+ Mohamed Sherif, Senior Technical Account Manager
+ Hicham Lahlali, Senior Cloud FinOps Architect
+ Prem Chandran, Technical Account Manager

## Feedback & Support
<a name="datatransfer-dashboard-feedback-support"></a>

Follow [Feedback & Support](feedback-support.md) guide

**Note**  
These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.