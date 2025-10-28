# Teardown

## Remove the AWS Config Resource Compliance Dashboard dashboard resources

Follow these steps to remove the dashboard.

### Step 1: all deployment architectures

1. Log into the AWS Console of the account where you deployed the
   dashboard. This is the AWS account ID that you specified in the `Dashboard account ID` parameter of the CloudFormation template.
2. Open AWS CloudShell in the region where the dashboard is deployed.
3. Execute the following command to delete the dashboard:

```
cid-cmd delete --resources cid-crcd.yaml --tag1 '`tag1`' --tag2 '`tag2`' --tag3 '`tag3`' --tag4 '`tag4`'
```

- `cid-crcd.yaml` is the template file provided in the
  `dashboard_template` directory. Upload it to AWS CloudShell if needed.
- The command provides default values for the tag parameters so that
  they are not asked later. There is no need to specify your actual tag
  names here.

1. When prompted:
   - Select the `[cid-crcd] AWS Config Resource Compliance Dashboard (CRCD)` dashboard.
   - For each QuickSight dataset, choose `yes` to delete the dataset.
   - If prompted, accept the default values for the S3 Path for the Athena table.
   - If prompted, accept the default values for the tags.

### Step 2: only for deployment on Log Archive or standalone account

###### Note

Follow these steps if you deployed the dashboard on the Log Archive account or a standalone AWS account.

1. Log into the AWS Console of the account where you deployed the dashboard resources with CloudFormation. This is the AWS account ID that you specified both in the `Log Archive account ID` and the `Dashboard account ID` parameters of the CloudFormation template.
2. Revert any manual configuration made during setup.
3. Open the S3 console and empty the Amazon S3 bucket for the Athena Query results. The bucket name is in the CloudFormation stack output.
4. In the same account, open CloudFormation and delete the stack that installed the data pipeline resources for the dashboard.

### Step 2: only for deployment on dedicated Dashboard account

###### Note

Follow these steps if you deployed the dashboard on a dedicated
Dashboard account.

#### Remove resources on Log Archive account

1. Log into the AWS Console of the Log Archive account. This is the AWS account ID that you specified in the `Log Archive account ID` parameter of the CloudFormation template.
2. Revert any manual configuration made during setup.
3. Open CloudFormation and delete the stack that installed the resources for the dashboard.

#### Remove resources on Dashboard account

1. Log into the AWS Console of the account where you deployed the dashboard resources with CloudFormation. This is the AWS account ID that you specified in the `Dashboard account ID` parameter of the CloudFormation template.
2. Revert any manual configuration made during setup.
3. Open the S3 console and empty the Amazon S3 bucket for the Athena Query results. The bucket name is in the CloudFormation stack output.
4. Empty the Dashboard bucket, as well. This bucket contains a copy of the AWS Config files from the Log Archive account. The bucket name is in the CloudFormation stack output.
5. In the same account, open CloudFormation and delete the stack that installed the data pipeline resources for the dashboard.
