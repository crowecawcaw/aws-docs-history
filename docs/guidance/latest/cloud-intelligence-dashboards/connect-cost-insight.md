

# Amazon Connect Cost Insight Dashboard
<a name="connect-cost-insight"></a>

## Introduction
<a name="introduction"></a>

The Amazon Connect Cost Insight Dashboard leverages AWS Cost and Usage Report data to provide visualizations that help optimize cloud spending and enhance operational efficiency within the [Amazon Connect contact center](https://aws.amazon.com/pm/connect) infrastructure.

![Image of Amazon Connect Cost Insight Dashboard architecture](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/CID_Connect_archi.png)


The Amazon Connect Cost Insight Dashboard is organized into 7 intuitive tabs:

1.  **Overview** A high-level summary of Amazon Connect and Contact Center Telecom charges.

1.  **Contact Center Analysis** Focus on cost and usage metrics exclusively for accounts running Amazon Connect and associated contact center services, enabling targeted monitoring of contact center operations.

1.  **Connect** Detailed view of Amazon Connect Voice service usage and costs.

1.  **Telecom Spend** Breakdown of contact center Telecommunications costs by number types and countries.

1.  **Daily Usage** 30-day trending data for costs and usage patterns with drill downs to inbound/outbound minutes and phone numbers usage.

1.  **Call Details** Key metrics about call patterns, durations, and regional distribution.

1.  **Contact Search** Detailed analysis of individual contacts and their characteristics. You can focus on a particular contact and see detailed information.

Each tab progressively moves from broad insights to specific details, helping you effectively monitor your contact center operations.

## Demo Dashboard
<a name="demo-dashboard"></a>

Get more familiar with the Dashboard using the live, interactive demo dashboard following this [link](https://cid.workshops.aws.dev/demo?dashboard=amazon-connect-cost-insight-dashboard) 

![Image of Amazon Connect Cost Insight Dashboard in Quick Sight](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/Amazon_Connect_dash.png)


## Prerequisites
<a name="prerequisites"></a>

1. Deploy one or more of the foundational dashboards: [CUDOS, Cost Intelligence, or KPI Dashboard.](cudos-cid-kpi.md) 

## Deployment
<a name="deployment"></a>

**Example**  
 **Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) 

1. Log in to your **Data Collection** Account.

1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Amazon-Connect-Cost-Insight-Dashboard&param_DashboardId=amazon-connect-cost-insight-dashboard) 

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
   cid-cmd deploy --dashboard-id amazon-connect-cost-insight-dashboard
   ```

   Please follow the instructions from the deployment wizard. More info about command line options are in the [Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd) or `cid-cmd --help`.
You can deploy the Amazon Connect Cost Insight Dashboard using the [CID Terraform module](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/terraform/cicd-deployment).  
 **Prerequisite**: Complete the foundational Terraform deployment as described in the [Foundational Dashboards deployment guide](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) (select the **Terraform** tab) before deploying additional dashboards.

1. In your [user-config.tf](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/terraform/cicd-deployment/user-config.tf), find the `dashboards` block and set `connect` to `"yes"`:

   ```
     connect = "yes"  # Amazon Connect Cost Insight Dashboard
   ```

1. Ensure the following module block is present in your `dashboards.tf`:

   ```
   module "connect_dashboard" {
     source = "./modules/cloudformation_stack"
     providers = {
       aws = aws.datacollection
     }
   
     config = local.additional_dashboards.connect
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
cid-cmd update --dashboard-id amazon-connect-cost-insight-dashboard
```

## Dashboard Customization
<a name="dashboard-customization"></a>

1. Unleash your data creativity\! Dive into custom analysis by creating your own visuals from this dashboard. Follow our quick [guide](create-analysis.md) to get started.

1. To integrate CID with AWS Organizations for enhanced cost visibility across multiple accounts and organizational units follow this [documentation](add-org-taxonomy.md) 

1. To replace Amazon Connect instance IDs with more readable custom labels in your dashboard check the following section [link](#replace-connect-instance-id-with-custom-names) 

1. To set up granular billing for a detailed view of your Amazon Connect usage follow this [documentation](https://docs.aws.amazon.com/connect/latest/adminguide/granular-billing.html) 

### Replacing Connect Instance IDs with Custom Names in Amazon Connect Dashboard
<a name="replace-connect-instance-id-with-custom-names"></a>

This process allows you to replace Amazon Connect instance IDs with more readable custom labels in your dashboard. This is a one-time setup that needs to be done after dashboard deployment.

#### Expand for the steps to follow
<a name="collapsible-section-id-connect"></a>

 **Steps** 

1. Create an Analysis. Refer to [How do I edit or customize the dashboards](faq.md#faq-how-do-i-edit-or-customize-the-dashboards) 

1. Edit the Calculated Field: Under Data >> Dataset 'resource\_connect\_view' edit **\_\_connect\_instance\_name** field  
![Connect Instance Name](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/connect/instance_name.png)

You’ll find an example that you can uncomment to provide your instance ID and preferred label

```
ifelse (
  {#connect_instance_id}="bb83be25-8c15-4696-a583-5dejlk12","EuropeProd",
//   {#connect_instance_id}="<instance_id>","<instance_name2>",
//   {#connect_instance_id}="<instance_id>","<instance_name3>",
   contains({usage_type},'-numbers'), 'phone numbers'
   ,
   {#connect_instance_id}
    )
```

Save the calculated field and verify the changes in the Overview tab’s verification table (bottom right)

![Connect Instance Label](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/connect/instance_label.png)


1. Publish your Analysis as Dashboard.

 **Notes** 
+ Each instance ID mapping should follow the format: {\#connect\_instance\_id}="instance-id","custom-name"
+ Maintain the default 'phone numbers' handling and fallback options
+ Multiple instances can be added by repeating the mapping line
+ Remember to include the comma between each condition

## Authors
<a name="authors"></a>
+ Alex Yankovskyy, Solutions Architect
+ Baraa Elkosh, Sr Technical Account Manager
+ Mariia Poliakh, Technical Account Manager

## Feedback & Support
<a name="connect-cost-insights-feedback-support"></a>

Follow [Feedback & Support](feedback-support.md) guide

Have a success story to share with the Team, suggest an improvement or report an error?
+ Please email: [cloud-intelligence-dashboards-amazon-connect@amazon.com](mailto:cloud-intelligence-dashboards-amazon-connect@amazon.com) 

**Note**  
These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.