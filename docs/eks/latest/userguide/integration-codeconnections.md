

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Connect to Git repositories with AWS CodeConnections
<a name="integration-codeconnections"></a>

 [AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html) provides a secure way to connect AWS services to third-party source code repositories. AWS CodeConnections supports GitHub, GitLab, Bitbucket, and [other providers](https://docs.aws.amazon.com/dtconsole/latest/userguide/supported-versions-connections.html). To learn more and get started, see [Working with connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html).

## Use AWS CodeConnections with Argo CD
<a name="integration-codeconnections-use"></a>

When using the EKS capability for Argo CD, you can choose to use AWS CodeConnections to enable secure authentication to Git repositories without managing long-lived credentials or personal access tokens. AWS CodeConnections handles the OAuth authentication flow and manages the connection to your Git provider, providing a secure and manageable approach to accessing your GitOps repositories and application manifests stored in third-party Git providers.

 **Prerequisites** 
+ An Amazon EKS cluster with the Argo CD capability created
+ A connection created in AWS CodeConnections to your Git provider
+ IAM permissions configured for Argo CD to use the connection

 **To configure CodeConnections for Argo CD repository access** 

1. Create a connection in the CodeConnections console:

   1. Open the [CodeConnections console](https://console.aws.amazon.com/codesuite/settings/connections).

   1. Choose **Create connection**.

   1. Select your provider (GitHub, GitLab, or Bitbucket) and follow the authentication flow.

   1. Note the connection ARN for use in your Argo CD configuration.

1. Ensure the Argo CD capability role has permissions to use the connection with a resource-based policy:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "codeconnections:UseConnection",
           "codeconnections:GetConnection"
         ],
         "Resource": "arn:aws:codeconnections:region:account-id:connection/connection-id"
       }
     ]
   }
   ```

1. Configure Argo CD to reference the CodeConnections resource when adding a repository, using the CodeConnections resource endpoint as the repository url. The Argo CD capability uses the connection to authenticate to your Git provider without requiring long-lived credentials.

## Considerations for using CodeConnections with Argo CD
<a name="integration-codeconnections-considerations"></a>

When using AWS CodeConnections with the EKS Capability for Argo CD, keep the following in mind:
+ The CodeConnections connection must be in the same AWS Region as your EKS cluster
+ The Argo CD capability role must have `codeconnections:UseConnection` and `codeconnections:GetConnection` permissions
+ CodeConnections manages the OAuth flow and credential lifecycle automatically

For more information about configuring repository access with Argo CD, see [Configure repository access](argocd-configure-repositories.md).