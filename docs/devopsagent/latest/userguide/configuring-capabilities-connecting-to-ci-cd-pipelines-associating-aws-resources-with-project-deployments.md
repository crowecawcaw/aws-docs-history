# Associating AWS resources with project deployments

After connecting projects to your Agent Space, you must configure the association between projects and AWS resources to enable AWS DevOps Agent to track deployments of CloudFormation templates, CDK, Elastic Container Repository images, and Terraform.

## Step 1: Edit project settings

- In the **Pipeline** section of your Agent Space, locate your connected GitLab or GitHub project in the sources list
- Click the **Edit** button

## Step 2: Associate AWS resources from primary account

Under **Associate AWS resources**, provide the corresponding resource ARNs for resources that your project deploys to:

- **CloudFormation stacks** – Enter the CloudFormation stack ARN
- **Amazon ECR repositories** – Enter the ECR repository ARN
- **AWS CDK deployments** – Enter the relevant CloudFormation stack ARNs created by CDK
- **Terraform** – Enter the S3 object ARN where your Terraform state file is stored. Currently only one Terraform state file is supported.

###### Important

Do not include sensitive data in Terraform state files.

Click **Add new resource** to associate additional resources if needed.

## Step 3: Associate resources from secondary AWS accounts

If your project deploys resources to secondary AWS accounts, provide those resource ARNs under **Associate resources from secondary AWS accounts**. Click **Add new resource** to add additional resources if needed.

## Step 4: Save your changes

Click **Update Association** to save your AWS resource associations. Following successful configuration, AWS DevOps Agent will automatically tracking deployment artifacts in GitLab Pipelines and GitHub Actions. Note that deployment artifacts that are deployed by external systems such as Jenkins or ArgoCD will not be tracked.
