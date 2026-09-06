

# Deployment
<a name="scad-containers-dashboard-deployment"></a>

## Deployment
<a name="deployment"></a>

**Example**  
 **Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) 

1. Log in to your **Data Collection** Account.

1. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=SCAD-Containers-Dashboard&param_DashboardId=scad-containers-cost-allocation) 

1. You can change **Stack name** for your template if you wish.

1. Leave **Parameters** values as they are.

1. Review the configuration and click **Create stack**.

1. You will see the stack will start in **CREATE\_IN\_PROGRESS**. Once complete, the stack will show **CREATE\_COMPLETE** status

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
   cid-cmd deploy --dashboard-id scad-containers-cost-allocation
   ```

   Please follow the instructions from the deployment wizard. More info about command line options are in the [Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd) or `cid-cmd --help`.
You can deploy the SCAD Containers Cost Allocation Dashboard using the [CID Terraform module](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/terraform/cicd-deployment).  
 **Prerequisite**: Complete the foundational Terraform deployment as described in the [Foundational Dashboards deployment guide](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard) (select the **Terraform** tab) before deploying additional dashboards.

1. In your [user-config.tf](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/terraform/cicd-deployment/user-config.tf), find the `dashboards` block and set `containers` to `"yes"`:

   ```
     containers = "yes"  # SCAD Containers Cost Allocation Dashboard
   ```

1. Ensure the following module block is present in your `dashboards.tf`:

   ```
   module "containers_dashboard" {
     source = "./modules/cloudformation_stack"
     providers = {
       aws = aws.datacollection
     }
   
     config = local.additional_dashboards.containers
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

**Note**  
Please note that DataExport can take up to 24-48 hours to deliver the first reports. If you just installed Data Exports, the dashboard will be most likely empty. Please come back after 24 hours.

### Update
<a name="update"></a>

Please note that dashboards are not updated with update of CloudFormation Stack. When a new version of the dashboard template is released, you can update your dashboard by running the following command in your command-line interface:

```
cid-cmd update --dashboard-id scad-containers-cost-allocation
```

Note:

Starting from version (v2.0.0), the `scad_cca_hourly_resource_view` Quick Sight dataset and Athena view are no longer used by the dashboard, and can be deleted. Please check the [SCAD Containers Cost Allocation Dashboard v2.0.0 changelog](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/changes/CHANGELOG-scad-cca.md#scad-containers-cost-allocation-dashboard---v200) for more information.