

# Support Cases Radar Dashboard
<a name="support-cases-radar"></a>

## Introduction
<a name="introduction"></a>

AWS Support Cases Radar Dashboard provides a centralized platform to consolidate, monitor and analyze [AWS Support Cases](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html) across all linked accounts and multiple AWS organizations. With unified view of all support cases, this dashboard empowers cloud governance teams to enhance operational efficiency and maximize the value delivered by AWS Support.

## Demo Dashboard
<a name="demo-dashboard"></a>

Get more familiar with the Dashboard using the live, interactive demo dashboard following this [link](https://cid.workshops.aws.dev/demo?dashboard=support-cases-radar) 

![image of a support cases radar dashboard in Quick Sight](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/support_cases_radar_dashboard.png)


## Architecture Overview
<a name="architecture-overview"></a>

![Data Collection Overview](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/support_cases_radar_arch.png)


The Data Collection Stack collects the information about cases on a daily basis. Only the cases which have changes are collected. An Amazon Step Function saves case information on Amazon S3 and sends an event with case reference to the Default Bus of EventBridge. The Quick Sight dashboard is refreshed every night to provide case summary and insights.

## Prerequisites
<a name="prerequisites"></a>

1. Make sure all concerned accounts have a **Business**, **On-Ramp** or **Enterprise** [Support Plan](https://console.aws.amazon.com/support/plans/home).

1. Deploy or update [Data Collection Lab](data-collection.md) and make sure Support Cases Data Collection Module is enabled.

## Deployment
<a name="deployment"></a>

**Example**  
 **Prerequisite:** To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) 

1. Log in to your **Data Collection** Account.

1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Support-Cases-Radar-Dashboard&param_DashboardId=support-cases-radar&param_RequiresDataCollection=yes) 

1. You can change **Stack name** for your template if you wish.

1. Leave **Parameters** values as they are.

1. Review the configuration and click **Create stack**.

1. You will see the stack will start in **CREATE\_IN\_PROGRESS**. Once complete, the stack will show **CREATE\_COMPLETE** 

1. You can check the stack output for dashboard URLs.

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
   cid-cmd deploy ---dashboard-id support-cases-radar
   ```

   Please follow the instructions from the deployment wizard. More info about command line options are in the [Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd) or `cid-cmd --help`.

## Optional Plugins
<a name="optional-plugins"></a>

Support Cases Radar has optional plugins that can be deployed to enable additional capabilities such as a generative AI case summarization.

 [Optional Plugins](optional-plugin.md) 

## Update
<a name="update"></a>

Please note that dashboards are not updated with update of CloudFormation Stack. When a new version of the dashboard template is released, you can update your dashboard by running the following command in your command-line interface:

```
cid-cmd update --dashboard-id support-cases-radar
```

## Authors
<a name="authors"></a>
+ Raffy Armistead, Senior Technical Account Manager
+ Samuel Chniber, Senior Solution Architect
+ Iakov Gan, Ex-Amazonian
+ Yuriy Prykhodko, Principal Technical Account Manager

## Feedback & Support
<a name="support-case-radar-feedback-support"></a>

Follow [Feedback & Support](feedback-support.md) guide

**Note**  
These dashboards and their content (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.