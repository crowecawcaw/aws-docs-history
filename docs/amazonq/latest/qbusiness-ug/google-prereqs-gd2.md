# Prerequisites for connecting Amazon Q Business to Google Drive

Before you begin, make sure that you have completed the following
prerequisites.

**In Google Drive, make sure you have:**

- **Either** been granted access by a super admin
  role **or** are a user with administrative
  privileges. You do not need a super admin role for yourself if you have been
  granted access by a super admin role.
- Configured Google Drive Service Account connection credentials
  containing your admin account email, client email (service account email), and
  private key. See [Google Cloud
  documentation on creating and deleting service account keys](https://cloud.google.com/iam/docs/keys-create-delete "https://cloud.google.com/iam/docs/keys-create-delete").
- Created a Google Cloud Service Account (an account with delegated authority to
  assume a user identity) with **Enable G Suite Domain-wide
  Delegation** activated for server-to-server authentication, and
  then generated a JSON private key using the account.

###### Note

The private key should be generated after the creation of the service
account.

- Added Admin SDK API and Google Drive API in your user account.
- Added (or asked a user with a super admin role to add) the following OAuth
  scopes to your service account using a super admin role. These API scopes are
  needed to crawl all documents, and access control (ACL) information for all
  users in a Google Workspace domain:

      + https://www.googleapis.com/auth/drive.readonly—View and
       download all your Google Drive files
      + https://www.googleapis.com/auth/drive.metadata.readonly—View
       metadata for files in your Google Drive
      + https://www.googleapis.com/auth/admin.directory.group.readonly—Scope
       for only retrieving group, group alias, and member information. This is
       needed for the Amazon Q Identity Crawler.
      + https://www.googleapis.com/auth/admin.directory.user.readonly—Scope
       for only retrieving users or user aliases. This is needed for listing
       users in the Amazon Q Identity Crawler and for setting
       ACLs.
      + https://www.googleapis.com/auth/cloud-platform—Scope for
       generating access token for fetching content of large Google Drive
       files.
      + https://www.googleapis.com/auth/forms.body.readonly—Scope for
       fetching data from Google Forms.

  **To support the Forms API, add the following additional
  scope:**

      + https://www.googleapis.com/auth/forms.body.readonly

  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Google Drive authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
