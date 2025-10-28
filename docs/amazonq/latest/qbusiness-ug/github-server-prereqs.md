# Prerequisites for connecting Amazon Q Business to GitHub (Server)

Before you begin, make sure that you have completed the following
prerequisites.

**In GitHub (Server), make sure you have:**

- Created a GitHub (Server) user with administrative permissions to the
  GitHub (Server) organization.
- Created a classic personal access token for authentication credentials. See
  [GitHub documentation on creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token").
- **Recommended:**Created an OAuth token for
  authentication credentials. Use OAuth token for better API throttle limits and
  connector performance. See [GitHub documentation on OAuth authorization](https://docs.github.com/en/rest/apps/oauth-applications?apiVersion=2022-11-28#about-oauth-apps-and-oauth-authorizations-of-github-apps "https://docs.github.com/en/rest/apps/oauth-applications?apiVersion=2022-11-28#about-oauth-apps-and-oauth-authorizations-of-github-apps").

Then, added the following OAuth scopes:

    + `repo:status` – Grants read/write access to commit
     statuses in public and private repositories. This scope is only
     necessary to grant other users or services access to private repository
     commit statuses without granting access to the code.
    + `repo_deployment` – Grants access to deployment
     statuses for public and private repositories. This scope is only
     necessary to grant other users or services access to deployment
     statuses, without granting access to the code.
    + `public_repo` – Limits access to public
     repositories. That includes read/write access to code, commit statuses,
     repository projects, collaborators, and deployment statuses for public
     repositories and organizations. Also required for starring public
     repositories.
    + `repo:invite` – Grants accept/decline abilities for
     invitations to collaborate on a repository. This scope is only necessary
     to grant other users or services access to invites without granting
     access to the code.
    + `security_events` – Grants: read and write access to
     security events in the code scanning API. This scope is only necessary
     to grant other users or services access to security events without
     granting access to the code.
    + `read:org` – Read-only access to organization
     membership, organization projects, and team membership.
    + `user:email` – Grants read access to a user's email
     addresses. Required by Amazon Q Business to crawl ACLs.
    + `user:follow` – Grants access to follow or unfollow
     other users. Required by Amazon Q Business to crawl ACLs.
    + `read:user` – Grants access to read a user's profile
     data. Required by Amazon Q Business to crawl ACLs.
    + `workflow` – Grants the ability to add and update
     GitHub (Server) Actions workflow files. Workflow files can be
     committed without this scope if the same file (with both the same path
     and contents) exists on another branch in the same repository.

For more information, see [Scopes for OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps "https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps") in GitHub (Server)
Docs.

- Noted the GitHub (Server) host URL for the type of GitHub (Server)
  service that you use. For example, the host URL for GitHub (Server) Server
  could be `https://on-prem-host-url/api/v3/`.
- Noted the name of your organization for GitHub (Server) the GitHub
  Enterprise account you want to connect to. You can find your organization name
  by logging into GitHub (Server) desktop and selecting **Your
  organizations** under your profile picture dropdown.
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your GitHub (Server) authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
