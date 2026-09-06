

# Bitbucket OAuth app
<a name="oauth-app-bitbucket"></a>

**Required action for Bitbucket OAuth token rotation**  
Atlassian now enforces single-use rotating refresh tokens for Bitbucket OAuth. We recommend migrating to [Bitbucket App connections](connections-bitbucket-app.md), which eliminates token management entirely. For instructions on migrating, see [Migrate to AWS CodeConnections (recommended)](connections-bitbucket-app.md#connections-bitbucket-migrate-to-codeconnections).  
If you prefer to continue using OAuth with Secrets Manager, add the `secretsmanager:PutSecretValue` permission to your CodeBuild service role. For more information, see [Required action for Secrets Manager-stored credentials](connections-bitbucket-app.md#connections-bitbucket-oauth-sm-action).  
If you use the CodeBuild-managed option, no changes are needed. CodeBuild handles token rotation automatically.

## Connect Bitbucket using OAuth (console)
<a name="oauth-app-bitbucket-console"></a>

To use the console to connect your project to Bitbucket using an OAuth app, do the following when you create a project. For information, see [Create a build project (console)](create-project.md#create-project-console). 

1. For **Source provider**, choose **Bitbucket**. 

1. For **Credential**, do one of the following:
   + Choose to use account credentials to apply your account's default source credential to all projects.

     1. If you aren't connected to Bitbucket, choose **Manage account credential**.

     1. For **Credential type**, choose **OAuth app**.
   + If you chose to use account level credentials for **Service**, choose which service you'd like to use to store your token and do the following:

     1. If you choose to use **Secrets Manager**, you can choose to use an existing secret connection or create a new secret, and then choose **Save**. For more information about creating a new secret, see [Create and store a token in a Secrets Manager secret](asm-create-secret.md).

     1. If you choose to use **CodeBuild** and then choose **Save**.
   + Select **Use override credentials for this project only** to use a custom source credential to override your account's credential settings.

     1. From the populated credential list, choose one of the options under **OAuth app**.

     1. You can also create a new OAuth app token by selecting **create a new Oauth app token connection** in the description.

To review your authorized OAuth apps, navigate to [Application authorizations](https://bitbucket.org/account/settings/app-authorizations/) on Bitbucket, and verify that an application named `AWS CodeBuild ({{region}})` is listed. 