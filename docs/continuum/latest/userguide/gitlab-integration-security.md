

# Security for GitLab integrations in AWS Continuum
<a name="gitlab-integration-security"></a>

A GitLab integration gives AWS Continuum an access token for a GitLab group or project on GitLab.com or on a self-managed GitLab instance. AWS Continuum uses the token to read the source code that it scans, and to open merge requests that contain generated patches. This topic describes the security controls that AWS Continuum applies to GitLab integrations and the actions that you are responsible for.

## Access token handling
<a name="gitlab-integration-security-token"></a>
+ AWS Continuum accepts personal, group, and project access tokens. When you create the integration, AWS Continuum validates the token with GitLab and checks that it can access the group or project that you specify. If the check fails, AWS Continuum doesn't create the integration.
+ The access token is write-only. AWS Continuum never returns it in an API response or in the console after you create the integration.
+ AWS Continuum encrypts the token at rest. If you specify a customer managed key when you create the integration, AWS Continuum encrypts the token with that key. For more information, see [Encryption at rest](https://docs.aws.amazon.com/continuum/latest/userguide/encryption-at-rest.html).
+ AWS Continuum connects to GitLab only over HTTPS.
+ If the token has the `self_rotate` scope, AWS Continuum rotates it automatically and issues a new token with a 90-day lifetime. Otherwise, AWS Continuum records the token's expiration date. In that case, replace the token before it expires.

When AWS Continuum rotates a token that has the `self_rotate` scope, the following happens:
+ AWS Continuum first rotates the token shortly before it expires. It then rotates each new token before it expires.
+ The token that you provided stops working right away. Tools that still use it also stop working.
+ AWS Continuum stores the new token securely. You can't view it.

**Use a dedicated access token**  
Create an access token only for this integration. Don't share it with other tools or scripts, and don't rotate or reuse it yourself.  
If you rotate or reuse the token, GitLab can revoke the token that AWS Continuum uses. The integration then fails with `401 Unauthorized` errors. To reconnect, create a new integration with a new access token.

## Private projects only
<a name="gitlab-integration-security-visibility"></a>

A patch for a vulnerability discloses the vulnerability to anyone who can read the repository. For this reason, AWS Continuum works only with GitLab groups and projects whose visibility is **Private**. AWS Continuum treats **Internal** visibility, which lets every signed-in user of the instance read the project, the same as **Public**.

AWS Continuum checks visibility at each of the following points:
+ When you create the integration, AWS Continuum rejects a group or project that isn't private.
+ When you add a project to an environment, AWS Continuum rejects a project that isn't private.
+ Before it opens a merge request, AWS Continuum reads the project again. It doesn't deliver a patch if the project is no longer private or if the project ID changed. It also doesn't deliver a patch if the project was renamed or moved since you added it to the environment, including a move out of the integration's group.

## Self-managed GitLab instances
<a name="gitlab-integration-security-instance"></a>

For a self-managed instance, AWS Continuum connects to the instance URL that you specify over the internet. The instance must be reachable from the internet over HTTPS on port 443. AWS Continuum rejects the instance URL in the following cases:
+ The URL uses a scheme other than `https`.
+ The URL uses an IP address or `localhost` instead of a host name.
+ The URL specifies a port other than 443.
+ The URL contains a user name, password, query string, or fragment.

## Merge request delivery and CI/CD pipelines
<a name="gitlab-integration-security-delivery"></a>

AWS Continuum delivers each patch as a single commit on a new branch, and opens a merge request to the branch that it scanned. AWS Continuum never pushes to the target branch and never merges the merge request. You or someone in your organization reviews and merges every change.

GitLab runs continuous integration and continuous delivery (CI/CD) pipelines with the permissions of the user who owns the access token. To keep patched code from running in your pipelines before you review it, AWS Continuum applies the following controls:
+ The commit message and the merge request title both contain `[skip ci]`. The commit message skips branch pipelines and merge request pipelines. The merge request title skips merged results pipelines and merge trains. These pipelines run on a merge commit that GitLab creates. To run your merge request pipelines after you review the patch, remove `[skip ci]` from the merge request title. You can also run a pipeline from the merge request's **Pipelines** tab.
+ A patch never changes CI/CD configuration. AWS Continuum doesn't deliver a patch that changes `.gitlab-ci.yml`, a file in `.gitlab/ci/` or `.gitlab/agents/` in any directory, or the project's custom CI/CD configuration file.
+ AWS Continuum doesn't push a branch that matches one of the project's protected branch rules. Pipelines on protected branches can use protected CI/CD variables and protected runners.
+ A patch changes only regular files. AWS Continuum doesn't deliver a patch that changes a symbolic link or a submodule.

**Note**  
A pipeline execution policy or a scan execution policy on your project can force pipelines to run even when the commit message or merge request title contains `[skip ci]`. AWS Continuum doesn't work around these policies. If you use them, make sure that they don't run untrusted code with access to secrets.

## Your responsibilities
<a name="gitlab-integration-security-customer"></a>

Under the shared responsibility model, you are responsible for the GitLab access that you grant to AWS Continuum. Follow these practices:
+ Use a project or group access token instead of a personal access token, so that the token isn't tied to one person's account and access.
+ Grant the least privilege that AWS Continuum needs. To scan code and open merge requests, use a token with the `api` scope and the **Developer** role. Don't use a token that belongs to an administrator or that has the `sudo` or `admin_mode` scope.
+ Add the `self_rotate` scope so that AWS Continuum can rotate the token, or set an expiration date and replace the token before it expires.
+ Create a separate access token for each integration. Don't use the token anywhere else, and don't rotate it yourself. If the integration stops working because GitLab returns `401 Unauthorized`, create a new integration with a new access token.
+ Protect your default and release branches, and require approval before a merge request can be merged.
+ Review each AWS Continuum merge request before you remove `[skip ci]` or run its pipelines.
+ Keep the groups and projects that you connect private. If you change a project's visibility to **Internal** or **Public**, AWS Continuum stops delivering patches to it.
+ Revoke the token in GitLab and delete the integration in AWS Continuum if you think the token was exposed.