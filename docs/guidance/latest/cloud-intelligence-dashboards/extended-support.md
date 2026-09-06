

# Extended Support - Cost Projection
<a name="extended-support"></a>

## Introduction
<a name="introduction"></a>

This dashboard provides insights on resources reaching extended support and projects the cost of extended support based on resource usage over a given period of time.

Services with extended support covered by this dashboard:

 **ElastiCache Extended Support** 

With ElastiCache Extended Support, you can continue running your cache on a major engine version past the end of standard support date for an additional cost. If you don’t upgrade after the end of standard support date, you will be charged.

Extended Support provides the following updates and technical support:
+ Security updates for critical and high CVEs for your cache and cache engine
+ Bug fixes and patches for critical issues
+ The ability to open support cases and receive troubleshooting help within the standard ElastiCache service level agreement

This dashboard provides a clear view on ElastiCache clusters reaching extended support in the next 3, 6, 12 months, and beyond.

It presents the estimated monthly cost of extended support, and allows you to drill down to cluster level, to review where your usage and estimated cost will be if, and when, your clusters enter the extended support period.

See also:
+  [Amazon ElastiCache Extended Support](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/extended-support.html) 

 **EKS Extended Support** 

With Amazon EKS Extended Support, you can continue running your EKS clusters on a version that has reached the end of its standard support, for an additional 12 months.

During extended support, Amazon EKS clusters will receive ongoing security patches for the Kubernetes control plane. Additionally, Amazon EKS will release patches for specific add-ons.

This dashboard provides a clear view on EKS clusters reaching extended support in the next 3, 6, 12 months, and beyond.

It presents the estimated monthly cost of extended support, and allows you to drill down to cluster level, to review where your usage and estimated cost will be if, and when, your clusters enter the extended support period.

See also:
+  [Amazon EKS Extended Support FAQs](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html#extended-support-faqs) 

 **RDS Extended Support** 

With Amazon RDS Extended Support, you can continue running your database on a major engine version past the RDS end of standard support date for an additional cost.

The dashboard provides a clear view on databases reaching extended support in the next 3, 6, 12 months, and beyond.

It presents the estimated monthly cost of extended support, and allows you to drill down to database instance level, to review where your usage and estimated cost will be if, and when, your databases enter the extended support period.

See also:
+  [Using Amazon RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) 

 **OpenSearch Extended Support** 

With Amazon OpenSearch Extended Support, you can continue running your legacy ElasticSearch and OpenSearch versions beyond end of Standard Support for an incremental flat fee over regular instance pricing.

The dashboard provides a clear view on ElasticSearch and OpenSearch domains reaching extended support in the next 3, 6, 12 months, and beyond.

It presents the estimated monthly cost of extended support, and allows you to drill down to domain level, to review where your usage and estimated cost will be if, and when, your domains enter the extended support period.

See also:
+  [Using Amazon OpenSearch Extended Support](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html#standard-support-extended-suppport) 

## Demo Dashboard
<a name="demo-dashboard"></a>

Get more familiar with the Dashboard using the live, interactive demo dashboard following this [link](https://cid.workshops.aws.dev/demo?dashboard=extended-support-cost-projection&sheet=default) 

![Extended Support Cost Projection Dashboard](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/rdsxtsuppcp.png)


## Prerequisites
<a name="prerequisites"></a>

1. Deploy the [Foundational dashboards (CUDOS, CID, KPI)](deployment-in-global-regions.md) to ensure cost and usage information is available to produce the cost projection for RDS Extended Support based on actual usage for a given period of time.

1. Deploy or update [Data Collection Lab](data-collection.md) and make sure Inventory Data collection module is enabled. Version 3.2.0 or higher required.

## Deployment
<a name="deployment"></a>

**Example**  
 **Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) 

1. Log in to your **Data Collection** Account.

1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Extended-Support-Cost-Projection&param_DashboardId=extended-support-cost-projection&param_RequiresDataCollection=yes) 

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
    cid-cmd deploy --dashboard-id extended-support-cost-projection
   ```

   Please follow the instructions from the deployment wizard. More info about command line options are in the [Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd) or `cid-cmd --help`.

## Update
<a name="update"></a>

Please note that dashboards are not updated with update of CloudFormation Stack. When a new version of the dashboard template is released, you can update your dashboard by running the following command in your command-line interface:

```
cid-cmd update --dashboard-id extended-support-cost-projection
```

## Authors
<a name="authors"></a>
+ Julio Chaves, Technical Account Manager
+ Iakov Gan, Ex-Amazonian
+ Yuriy Prykhodko, Principal Technical Account Manager

## Feedback & Support
<a name="extended-support-feedback-support"></a>

Follow [Feedback & Support](feedback-support.md) guide

**Note**  
These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.