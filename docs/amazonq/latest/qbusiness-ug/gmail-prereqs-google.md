

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Setting up Google Workspace authentication
<a name="gmail-prereqs-google"></a>

Complete these steps in your Google Workspace environment to prepare for the Amazon Q Business connection:

**To set up Google Workspace authentication**

1. Verify you have Google Workspace (not personal Gmail accounts).

1. Create a Google Cloud Platform admin account and Google Cloud project if you don't already have them.

1. Enable the Gmail API and Admin SDK API in your Google Cloud project:

   1. Go to the Google Cloud Console API Library.

   1. Search for and enable the Gmail API.

   1. Search for and enable the Admin SDK API.

1. Create a service account and download the JSON private key. For detailed instructions, see [Create a service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating) and [Service account credentials](https://cloud.google.com/iam/docs/service-account-creds#key-types) in the Google Cloud documentation.

1. Configure OAuth scopes for your service account. Add these required scopes:
   + `https://www.googleapis.com/auth/admin.directory.user.readonly`
   + `https://www.googleapis.com/auth/admin.directory.group.readonly`
   + `https://www.googleapis.com/auth/gmail.readonly`

1. Save the following information for use in Amazon Q Business:
   + Admin account email address
   + Service account email address
   + Private key from the JSON file