

# HealthOmics workflow integration with Git-based repositories
<a name="workflows-git-integration"></a>

When you create a workflow (or a workflow version), you provide a workflow definition to specify information about the workflow, runs, and tasks. HealthOmics can retrieve the workflow definition as a .zip archive (stored locally or in an Amazon S3 bucket), or from a supported Git-based repository.

The HealthOmics integration with Git-based repositories enables the following capabilities:
+ Direct workflow creation from public, private, and self-managed instances.
+ Integration of workflow README files and parameter templates from repositories.
+ Support for GitHub, GitLab, and Bitbucket repositories.

By using a Git-based repository, you avoid the manual steps of downloading workflow definition files and input parameter template files, creating a .zip archive, and then staging the archive to S3. This simplifies workflow creation for scenarios such as the following examples:

1. You want to get started quickly using a common open source workflow, such as nf-core. HealthOmics automatically retrieves all workflow definition and input parameter template files from the nf-core repository on GitHub and uses these files to create your new workflow.

1. You are using a public workflow from GitHub, and some new updates become available. You can easily create a new HealthOmics workflow version using the updated workflow definition on GitHub as the source. Users of your workflow can choose between the original workflow or the new workflow version that you created.

1. Your team is building a proprietary pipeline that is not public. You keep your code on a private git repository and use this workflow definition for your HealthOmics workflows. The team updates the workflow definition frequently as part of an iterative workflow development lifecycle. You can easily create new workflow versions as required from your private repository.

**Topics**
+ [Supported Git-based repositories](#workflows-git-supported)
+ [Configure connections to external code repositories](#workflows-git-connections)
+ [Accessing self managed repositories](#workflows-git-self-managed)
+ [Quotas related to external code repositories](#workflows-git-quotas)
+ [Required IAM permissions](#workflows-git-permissions)

## Supported Git-based repositories
<a name="workflows-git-supported"></a>

HealthOmics supports public and private repositories for the following Git-based providers:
+ GitHub 
+ GitLab 
+ Bitbucket 

HealthOmics supports self-managed repositories for the following Git-based providers:
+ GitHubEnterpriseServer 
+ GitLabSelfManaged 

HealthOmics supports use of cross-account connections for GitHub, GitLab, and Bitbucket. Set up shared permissions through the AWS Resource Access Manager. For an example, see [Shared connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-shared.html) in the *CodePipeline user guide*.

## Configure connections to external code repositories
<a name="workflows-git-connections"></a>

Connect your workflows to Git-based repositories using AWS CodeConnection. HealthOmics uses this connection to access your source code repositories.

**Note**  
The AWS CodeConnections service is not available in the il-central-1 region. For this region, configure service us-east-1 to create workflows or workflow versions from a repository. 

### Create a connection
<a name="workflows-git-connection-create"></a>

Before you can create connections, follow the instructions in [Setting up connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/setting-up-connections.html) in the *Developer Console Tools User Guide*. 

To create a connection, follow the instructions in [Create a connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create.html) in the *Developer Console Tools User Guide*. 

### Configure authorization for the connection
<a name="workflows-git-connection-create"></a>

You must authorize the connection using the provider's OAuth flow. Make sure that the connection status is `AVAILABLE` before you use it.

For examples, see the blog post [ How To Create an AWS HealthOmics Workflows from Content in Git](https://repost.aws/articles/ARCEN7AjhaRSmteczRoc_QsA/how-to-create-an-aws-healthomics-workflows-from-content-in-git). 

## Accessing self managed repositories
<a name="workflows-git-self-managed"></a>

To set up connections to a GitLab self-managed repository, use an admin Personal Access Token when creating a host. The subsequent connection creation accesses Oauth with the customer’s account.

The following example sets up a connection to a GitLab self-managed repository:

1. Set up access to the Personal Access Token of an admin user.

   To set up a PAT in a GitLab self managed repository, see [Personal access tokens](https://docs.gitlab.com/user/profile/personal_access_tokens/) in *GitLab Docs*.

1. Create a host

   1. Navigate to **CodePipeline>Settings>Connections**.

   1. Choose the **Hosts** tab and then choose **Create Host**.

   1. Configure the following fields:
      + Enter a name of the host
      + For provider type, choose **GitLab Self Managed**
      + Enter the **Host URL** 
      + Enter the VPC information if the host is defined in a VPC

   1. Choose **Create Host**, which creates the host in PENDING state.

   1. To complete the set up, choose **Set up Host**.

   1. Enter the Personal Access Token (PAT) of an Admin user, then choose **Continue**. 

1. Create the connection

   1. Choose **Create Connections** on the **Connections** tab.

   1. For provider type, select **GitLab self-managed**.

   1. Under **Connection Settings>Enter Connection Name**, enter the Host URL that you previously created.

   1. If your GitLab self-managed instance is only accessible via a VPC, configure the VPC details.

   1. Choose **Update Pending Connection**. The modal window re-directs you to the GitLab login page.

   1. Enter the username and password for the customer account and complete the authorization process.

   1.  For first time setup, choose **Authorize AWS Connector for Gitlab Self Managed**.

## Quotas related to external code repositories
<a name="workflows-git-quotas"></a>

For HealthOmics integration with external code repositories, there is a maximum size for a repository, each repository file, and each README file. For details, see [HealthOmics workflow fixed size quotas](fixed-quotas.md#fixed-quotas-workflows).

## Required IAM permissions
<a name="workflows-git-permissions"></a>

Add the following actions to your identity-based IAM policy:

```
   "codeconnections:CreateConnection",
   "codeconnections:GetConnection",
   "codeconnections:GetHost",
   "codeconnections:ListConnections",
   "codeconnections:UseConnection"
```