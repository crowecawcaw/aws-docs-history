# Prerequisites for connecting Amazon Q Business to Google Calendar (Preview)

Before you begin, make sure that you have completed the following
prerequisites.

**In Google Calendar, make sure you
have:**

- Created a Google Cloud Platform admin account and have created a Google Cloud
  project.
- Activated the Google Calendar API and Admin SDK API in your
  admin account.
- Created a service account and downloaded a JSON private key for your
  Google Calendar. For information about how to create and
  access your private key, see [Create a
  service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating "https://cloud.google.com/iam/docs/keys-create-delete#creating") and [Service account credentials](https://cloud.google.com/iam/docs/service-account-creds#key-types "https://cloud.google.com/iam/docs/service-account-creds#key-types") on the Google Cloud website.

On the Google Cloud website:

- Copied your admin account email, your service account email, and your private
  key to use for authentication.
- Added the following Oauth scopes, using an admin role, for your user and the
  shared directories you want to index:
  - https://www.googleapis.com/auth/admin.directory.user.readonly
  - https://www.googleapis.com/auth/gmail.readonly

In your AWS account, make sure you have:

    + Created an Amazon Q Business application.
    + Created an Amazon Q Business retriever and added an
     index.
    + Created an IAM role for your data source and, if using the Amazon Q
     API, noted the ARN of the IAM role.
    + Stored your Google Calendar authentication credentials in an AWS
     Secrets Manager secret and, if using the Amazon Q API, noted
     the ARN of the secret.

**In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Google Calendar authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
