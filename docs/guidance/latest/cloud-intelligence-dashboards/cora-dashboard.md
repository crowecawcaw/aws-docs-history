

# CORA Dashboard
<a name="cora-dashboard"></a>

## Introduction
<a name="introduction"></a>

The CORA (Cost Optimization Recommended Actions) Dashboard provides FinOps professionals, executives, and engineering leads with a comprehensive visualization of data from the [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/).

AWS Cost Optimization Hub offers customers a range of `Usage Optimization` and `Rate Optimization` aggregated from AWS Compute Optimizer and AWS Billing Console services

Usage Optimizations include:
+ Rightsizing suggestions
+ Idle resource detection
+ Migration and Upgrade recommendations

Rate Optimization consists of:
+ Savings Plans Recommendations
+ Reserved Instances recommendations

This dashboard leverages the [AWS Data Export of Cost Optimization Recommendations](data-exports.md) and enables additional capabilities:
+ Visualization of saving opportunities across multiple AWS Organizations (Payer Accounts) in one place.
+ Tracking of savings opportunities over time including daily updates and historical view.
+ Enablement of integration with customer business unit information to connect savings with workload owners (business units, teams, etc.)

Using the RLS (Row-Level Security) mechanism, this dashboard can be shared within your organization, allowing owners to track and take actions locally to maximize cost savings.

## Demo Dashboard
<a name="demo-dashboard"></a>

Get more familiar with the Dashboard using the live, interactive demo dashboard following this [link](https://cid.workshops.aws.dev/demo?dashboard=cora) 

![CORA Dashboard Screenshot](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/cora.png)


## Prerequisites
<a name="prerequisites"></a>

Before installing CORA Dashboard you need to enable COH Data Export and consolidate it from your Management (Payer) Accounts in Data Collection Account.

![Data Exports](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/cora-archi.png)


1. Create COH Data Export following the steps in [Data Export](data-exports.md) page and return to this page once completed.

1. Enable [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/faqs/#:~:text=How%20do%20I%20enable%20Cost%20Optimization%20Hub).

## Deployment
<a name="cora-dashboard-deploy"></a>

**Example**  
 **Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) 

1. Log in to your **Data Collection** Account.

1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=CORA-Dashboard&param_DashboardId=cora&param_RequiresDataExports=yes) 

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
   cid-cmd deploy --dashboard-id cora
   ```

   Please follow the instructions from the deployment wizard. More info about command line options are in the [Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd) or `cid-cmd --help`.
You can deploy the CORA Dashboard using the [CID Terraform module](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/terraform/cicd-deployment).  
 **Prerequisite**: Complete the foundational Terraform deployment as described in the [Foundational Dashboards deployment guide](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) (select the **Terraform** tab) before deploying additional dashboards.

1. In your [user-config.tf](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/terraform/cicd-deployment/user-config.tf), find the `dashboards` block and set `cora` to `"yes"`:

   ```
     cora = "yes"  # CORA Dashboard
   ```

1. Ensure the following module block is present in your `dashboards.tf`:

   ```
   module "cora_dashboard" {
     source = "./modules/cloudformation_stack"
     providers = {
       aws = aws.datacollection
     }
   
     config = local.additional_dashboards.cora
   }
   ```
**Note**  
This block is already included if you are using the full module files from the repository. If your existing deployment only has foundational dashboards, add this block to `dashboards.tf` manually. For individual dashboard deployments, include `depends_on = [module.cloud_intelligence_dashboards]` to ensure correct ordering.

1. Run the Terraform workflow:

   ```
   terraform init
   terraform plan
   terraform apply
   ```
**Note**  
If you are adding this dashboard to an existing Terraform deployment, `terraform plan` will show the additional stack to be created. The `dashboards.tf` file handles the resource definitions automatically — no manual edits to it are needed. If you have a custom module structure with a separate path, ensure the `source` parameter in your module block points to the correct location.

   For detailed instructions, refer to the [Terraform Deployment README](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/terraform/cicd-deployment/README.md).

## Update
<a name="update"></a>

Please note that dashboards are not updated with update of CloudFormation Stack. When a new version of the dashboard template is released, you can update your dashboard by running the following command in your command-line interface:

```
cid-cmd update --dashboard-id cora
```

## Usage Guide
<a name="usage-guide"></a>

The dashboard has several tabs and we recommend starting with the Summary. Here you can see the biggest recommendation categories, the potential savings they represent along with effort required for each resource and the number of resources.

We recommend you first estimate your Rightsizing, Upgrade, Migration and Stop-Idle opportunities. Typically it takes time to implement these recommendations especially at scale. We recommend you proceed with commitment (reserved instances and savings plan) for the volume that takes into account your rightsizing plan.

## Using Cost Allocation Tags
<a name="using-cost-allocation-tags"></a>

The dashboard also utilizes [Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).
+ Use the `FinopsException` tag to exclude workloads from the view if they are not eligible for cost optimization recommendations.
+ Configure `Name` as Cost Allocation tag to have this visibility on the dashboard by default.
+ Use `TagName` to specify a tag that you are interested in for GroupBy.

## Difference with UI
<a name="difference-with-ui"></a>

The AWS Cost Optimization Hub Console UI displays opportunities in a Donut chart with a special [deduplication](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/faqs/#:~:text=How%20does%20Cost%20Optimization%20Hub%20ensure%20savings%20from%20multiple%20recommendations%20are%20not%20double%20counted%3F). Commitment savings are shown accounting for the potential impact of implementing rightsizing recommendations. However, the Data Export of Cost Optimization does not have data for this level of adjustment.

The dashboard deduplicates recommendations by resource ID. Please note that dashboard shows recommendations for Rate Optimization and Usage Optimization deduplicated separately. But Rate Optimization is NOT taking into account the results of Usage Optimization (Rightsizing, Stop, Upgrade and such).

You can see discrepancies between the Donut Chart in the AWS Cost Optimization Hub Console and the data this service exported for analysis. The Console shows Rate Optimization savings adjusted to the results of Usage Optimization and thus can be more realistic. Please note that when using Dashboard you need to estimate the results of Usage Optimization and readjust the forecast of Rate Optimization accordingly.

## Authors
<a name="authors"></a>
+ Iakov Gan, Ex-Amazonian
+ Yuriy Prykhodko, Principal Technical Account Manager, AWS

## Feedback & Support
<a name="cora-dashboard-feedback-support"></a>

Follow [Feedback & Support](feedback-support.md) guide

**Note**  
These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.