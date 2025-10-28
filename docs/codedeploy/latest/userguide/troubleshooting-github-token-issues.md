# Troubleshoot GitHub token issues

## Invalid GitHub OAuth token

CodeDeploy applications created after June 2017 use GitHub OAuth tokens for each AWS
Region. The use of tokens tied to specific AWS Regions gives you more control over which
CodeDeploy applications have access to a GitHub repository.

If you receive a GitHub token error, you might have an older token that is now invalid.

**To fix an invalid GitHub OAuth token**

1. Remove the old token using one of the following methods:
   - To remove the old token using the API, use [DeleteGitHubAccountToken](../APIReference/API_DeleteGitHubAccountToken.md "../APIReference/API_DeleteGitHubAccountToken.md").
   - To remove the old token using the AWS Command Line Interface:
     1. Go to the computer where the token resides.
     2. Make sure the AWS CLI is installed on this computer. For installation
        instructions, see [Installing, updating, and
        uninstalling the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the
        _AWS Command Line Interface User Guide_
     3. Enter the following command on the computer where the token resides:

     `aws delete-git-hub-account-token`

     For details on the command syntax, see [delete-git-hub-account-token](../../../cli/latest/reference/deploy/delete-git-hub-account-token.md "../../../cli/latest/reference/deploy/delete-git-hub-account-token.md").

2. Add a new OAuth token. For more information, see [Integrating CodeDeploy with GitHub](integrations-partners-github.md "integrations-partners-github.md").

## Maximum number of GitHub OAuth

tokens exceeded

When you create a CodeDeploy deployment, the maximum number of allowed GitHub tokens is 10.
If you receive an error about GitHub OAuth tokens, make sure you have 10 or fewer tokens. If
you have more than 10 tokens, the first tokens that were created are invalid. For example,
if you have 11 tokens, the first token you created is invalid. If you have 12 tokens, the
first two tokens you created are invalid. For information about using the CodeDeploy API to
remove old tokens, see [DeleteGitHubAccountToken](../APIReference/API_DeleteGitHubAccountToken.md "../APIReference/API_DeleteGitHubAccountToken.md").
