

# Cost Anomaly Dashboard
<a name="cost-anomaly-dashboard"></a>

## Introduction
<a name="introduction"></a>

AWS Cost Anomaly Detection uses advanced Machine Learning to identify anomalous spend and root causes, empowering the customers to take action quickly. To make it easier for them to identify any sudden spike in the spends, they can visualize the insights into those anomalous spends across multiple accounts using Amazon Quick Sight that retrieves and refreshes the data periodically. Out-of-the-box benefits of the CAD include (but are not limited to):
+ Early Detection - A centralized cloud cost anomaly dashboard will allow our customers to quickly identify and investigate cost anomalies.
+ Trend Analysis - identify trends and patterns associated with cost anomalies MOM, Account, Service etc.
+ Governance - Centralized Dashboard view across organization (Payer) for FinOps Team to track and monitor AWS Cost Anomalies at the Organization level.
+ Early Resolution - With CAD, FinOps team proactively work with different teams in the organization to prevent overruns.

See also:
+  [AWS Cost Anomaly FAQ](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/faqs/) 

## Demo Dashboard
<a name="demo-dashboard"></a>

Get more familiar with the Dashboard using the live, interactive demo dashboard following this [link](https://cid.workshops.aws.dev/demo?dashboard=cost-anomaly-dashboard) 

![Image of a cost anomaly dashboard in Quick Sight](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/ca_demo.png)


## Prerequisites
<a name="prerequisites"></a>

1. To get cost anomalies on abnormal or sudden spend increases in your AWS account you need to [Enable Cost Anomaly Detection in your account](https://docs.aws.amazon.com/cost-management/latest/userguide/settingup-ad.html). AWS Cost Anomaly Detection is a feature within Cost Explorer. To access AWS Cost Anomaly Detection, enable Cost Explorer. For instructions on how to enable Cost Explorer using the console, [see Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html).

1. Deploy or update [Data Collection Lab](data-collection.md) and make sure Cost Anomalies Data Collection Module is enabled.

## Deployment
<a name="deployment"></a>

**Example**  
 **Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) 

1. Log in to your **Data Collection** Account.

1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Cost-Anomaly-Dashboard&param_DashboardId=aws-cost-anomalies&param_RequiresDataCollection=yes) 

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
    cid-cmd deploy --dashboard-id aws-cost-anomalies --athena-database optimization_data
   ```

   Please follow the instructions from the deployment wizard. More info about command line options are in the [Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd) or `cid-cmd --help`.

## Update
<a name="update"></a>

Please note that dashboards are not updated with update of CloudFormation Stack. When a new version of the dashboard template is released, you can update your dashboard by running the following command in your command-line interface:

```
cid-cmd update --dashboard-id aws-cost-anomalies
```

## Authors
<a name="authors"></a>
+ Yash Bindlish, Enterprise Support Manager
+ Iakov Gan, Ex-Amazonian
+ Yuriy Prykhodko, Principal Technical Account Manager

## Feedback & Support
<a name="cost-anomaly-dashboard-feedback-support"></a>

Follow [Feedback & Support](feedback-support.md) guide

**Note**  
These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.