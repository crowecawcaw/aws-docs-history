

# Teardown
<a name="config-resource-teardown"></a>

## Remove the AWS Config Resource Compliance Dashboard dashboard resources
<a name="remove-the-aws-config-resource-compliance-dashboard-dashboard-resources"></a>

Follow these steps to remove the dashboard.

### Step 1: all deployment architectures
<a name="step-1-all-deployment-architectures"></a>

1. Log into the AWS Console of the account where you deployed the dashboard. This is the AWS account ID that you specified in the `Dashboard account ID` parameter of the CloudFormation template.

1. Open AWS CloudShell in the AWS Region where the dashboard is deployed.

1. Execute the following command to delete the dashboard:

```
cid-cmd delete --resources 'https://raw.githubusercontent.com/aws-samples/config-resource-compliance-dashboard/refs/heads/main/dashboard_template/cid-crcd.yaml'
```

1. When prompted:
   + Select the `[cid-crcd] AWS Config Resource Compliance Dashboard (CRCD)` dashboard.
   + For each Quick Sight dataset, choose `yes` to delete the dataset.
   + If prompted, accept the default values for the S3 Path for the Athena table.
   + If prompted, accept the default values for the tags.

### Step 2: only for deployment on AWS Config or standalone account
<a name="step-2-only-for-deployment-on-aws-config-or-standalone-account"></a>

**Note**  
Follow these steps if you deployed the dashboard on the AWS Config account or a standalone AWS account.

1. Log into the AWS Console of the account where you deployed the dashboard resources with CloudFormation. This is the AWS account ID that you specified both in the `AWS Config account ID` and the `Dashboard account ID` parameters of the CloudFormation template.

1. Revert any manual configuration made during setup.

1. Open the S3 console and empty the Amazon S3 bucket for the Athena Query results. The bucket name is in the CloudFormation stack output.

1. In the same account, open CloudFormation and delete the stack that installed the data pipeline resources for the dashboard.

### Step 2: only for deployment on dedicated Dashboard account
<a name="step-2-only-for-deployment-on-dedicated-dashboard-account"></a>

**Note**  
Follow these steps if you deployed the dashboard on a dedicated Dashboard account.

#### Remove resources on AWS Config account
<a name="remove-resources-on-aws-config-account"></a>

1. Log into the AWS Console of the AWS Config account. This is the AWS account ID that you specified in the `AWS Config account ID` parameter of the CloudFormation template.

1. Revert any manual configuration made during setup.

1. Open CloudFormation and delete the stack that installed the resources for the dashboard.

#### Remove resources on Dashboard account
<a name="remove-resources-on-dashboard-account"></a>

1. Log into the AWS Console of the account where you deployed the dashboard resources with CloudFormation. This is the AWS account ID that you specified in the `Dashboard account ID` parameter of the CloudFormation template.

1. Revert any manual configuration made during setup.

1. Open the S3 console and empty the Amazon S3 bucket for the Athena Query results. The bucket name is in the CloudFormation stack output.

1. Empty the Dashboard bucket, as well. This bucket contains a copy of the AWS Config files from the AWS Config Logs bucket. The bucket name is in the CloudFormation stack output.

1. In the same account, open CloudFormation and delete the stack that installed the data pipeline resources for the dashboard.