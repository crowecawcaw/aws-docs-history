# Viewing and editing a hybrid directory

Use the following procedures to view or edit your hybrid directory.

## Viewing a hybrid directory

You can view a hybrid directory in the AWS Directory Service console.

###### To view detailed directory information

1. In the [AWS Directory Service
   console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose
   **Directories**.
2. Choose the directory ID link for your directory. Information about the
   directory appears on the **Directory details**
   page.

### Self-managed Active Directory information

This section provides information about your self-managed Active Directory that's joined
with AWS infrastructure.

- Directory type
- Directory ID
- Directory status
- Networking details for your self-managed AD, such as:
  - VPC
  - Subnets
  - DNS addresses

- Systems Manager managed nodes

### Hybrid directory tabs

You can find the following information about your AWS Managed Microsoft AD:

- On the **Share & share** tab, you can share your
  AWS Managed Microsoft AD with other AWS accounts and view the networking details for
  your domain controllers.
- On the **Application management** tab, you can enable
  an application access URL for your AWS Managed Microsoft AD and enable AWS
  applications and services for your AWS Managed Microsoft AD.
- On the **Maintenance** tab, you can enable SNS to
  receive notifications of your AWS Managed Microsoft AD status and review snapshots of
  your AWS Managed Microsoft AD.
- For more information about the **Status** field, see
  [Understanding your AWS Managed Microsoft AD directory status](ms_ad_directory_status.md "ms_ad_directory_status.md").

## Updating a hybrid directory

You can update a hybrid directory in the AWS Directory Service console to modify DNS settings or recover
administrator account access.

###### To update hybrid directory information

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2 "https://console.aws.amazon.com/directoryservicev2")
   navigation pane, choose **Directories**.
2. Choose the directory ID link for your directory to open the
   **Directory details** page.
3. Choose **Actions**, and then choose
   **Update hybrid directory information**.
4. On the **Update hybrid directory information** page,
   you can update your DNS settings or recover your administrator account.

**Update DNS settings (optional)**

Under **Self-managed Active Directory information**,
you can change the following:

    1. **Directory DNS Name**
    2. **DNS IP Addresses**You can update both settings together or individually. At least one change is

required for the update process. 5. **Recover hybrid directory administrator
account**

To recover your hybrid directory administrator account, we need temporary access
to a user. This access is provided through a secret from Secrets Manager. We use these
credentials only once during recovery and don't store them. If your hybrid directory
administrator account exists, you don't need to update this secret, even if you
updated your self-managed Active Directory administrator user.

    1. **Admin credentials secret** – We create a
     hybrid directory administrator account when we create a hybrid directory. If you
     deleted this secret, enter your Secrets Manager secret for your self-managed AD
     administrator user.
