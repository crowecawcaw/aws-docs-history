# Connecting GitLab

GitLab integration enables AWS DevOps Agent to monitor deployments from GitLab Pipelines to inform causal investigations during incident response. This integration follows a two-step process: account-level registration of GitLab, followed by connecting specific projects to individual Agent Spaces.

## Registering GitLab (account-level)

GitLab is registered at the AWS account level and shared among all Agent Spaces in that account. Individual Agent Spaces can then choose which specific projects apply to their Agent Space.

### Step 1: Navigate to pipeline providers

1. Sign in to the AWS Management Console
2. Navigate to the AWS DevOps Agent console
3. Go to the **Capabilities** tab
4. In the **Pipeline** section, click **Add**
5. Select **GitLab** from the list of available providers

If GitLab hasn't been registered yet, you'll be prompted to register it first.

### Step 2: Choose connection type

On the "Register GitLab Account / Group" screen, select whether you're connecting as a person or a group:

- **Personal** – Your individual GitLab user account with a username and profile
- **Group** – In GitLab, you use groups to manage one or more related projects at the same time

### Step 3: Select GitLab instance type

Choose which type of GitLab instance you're connecting to:

- **[GitLab.com](http://gitlab.com/ "http://gitlab.com/")** (default) – The public GitLab service
- **Publicly accessible Managed GitLab instance** – A managed GitLab deployment accessible from the public internet
- **Publicly accessible self-hosted GitLab** – Your own GitLab deployment accessible from the public internet

If you're using a self-hosted or managed GitLab instance, check the box "Use GitLab self hosted endpoint" and provide the URL to your GitLab instance.

###### Note

Currently, only publicly accessible GitLab instances are supported.

### Step 4: Create and provide an access token

1. In a separate browser tab, log in to your GitLab account
2. Navigate to your user settings and select **Access Tokens**
3. Create a new personal access token with the following permissions:
   - `read_repository` – Required to access repository content
   - `read_virtual_registry` – Required to access virtual registry information
   - `read_registry` – Required to access registry information
   - `api` – Required for read and write API access
   - `self_rotate` - Required for rotating tokens. This feature is currently unsupported by AWS DevOps Agent but will be supported at a later date. Adding now prevents the need to create a new token in the future.

4. Set the token expiration to a maximum of 365 days from the current date
5. Copy the generated token
6. Return to the AWS DevOps Agent console
7. Paste the token into the "Access Token" field

### Step 5: Complete registration

Click **Submit** to complete the GitLab registration process. The system will validate your access token and establish the connection.

## Connecting projects to an Agent Space

After registering GitLab at the account level, you can connect specific projects to individual Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space
2. Go to the **Capabilities** tab
3. In the **Pipeline** section, click **Add**
4. Select **GitLab** from the list of available providers
5. Select the GitLab projects relevant to your Agent Space
6. Click **Save**

AWS DevOps Agent will monitor these projects for deployments from GitLab Pipelines to inform causal investigations.

### Associating AWS resources with project deployments

See See the CI/CD pipeline documentation for associating AWS resources with deployments to associate deployments with AWS resources. This helps incident investigations correlate recent deployments with possible root causes.

## Managing GitLab connections

- **Updating access token** – If your access token expires or needs to be updated, you can update it in the AWS DevOps Agent console by modifying the GitLab registration at the account level.
- **Viewing connected projects** – In the AWS DevOps Agent console, select your Agent Space and go to the Capabilities tab to view connected projects in the Pipeline section.
- **Removing GitLab connection** – To disconnect GitLab projects from an Agent Space, select the connection in the Pipeline section and click **Remove**. To remove the GitLab registration completely, remove it from all Agent Spaces first, then delete the registration at the account level.

## Associating AWS resources with project deployments

###### Associate AWS resources with your project

1. ###### Edit project settings
   1. In the **Pipeline** section of your Agent Space, locate your connected GitLab or GitHub project in the sources list
   2. Click the **Edit** button

2. ###### Associate AWS resources from primary account
   1. Under **Associate AWS resources**, provide the corresponding resource ARNs for resources that your project deploys to:
      - **CloudFormation stacks** – Enter the CloudFormation stack ARN
      - **Amazon ECR repositories** – Enter the ECR repository ARN
      - **AWS CDK deployments** – Enter the relevant CloudFormation stack ARNs created by CDK
      - **Terraform** – Enter the S3 object ARN where your Terraform state file is stored

   2. Click **Add new resource** to associate additional resources if needed

   ###### Important

   Do not include sensitive data in Terraform state files.

3. ###### Associate resources from secondary AWS accounts
   1. If your project deploys resources to secondary AWS accounts, provide those resource ARNs under **Associate resources from secondary AWS accounts**
   2. Click **Add new resource** to add additional resources if needed

4. ###### Save your changes
   1. Click **Update Association** to save your AWS resource associations
   2. Following successful configuration, AWS DevOps Agent will automatically monitor your projects and workflows, tracking deployments to your AWS environment and correlating code changes with deployed resources
