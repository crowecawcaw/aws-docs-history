# Authentication mode

You can use authentication mode to allow users to log in using either their Amazon WorkMail
directory credentials, their IAM Identity Center credentials, or restricting login to only IAM Identity Center
credentials.

There are two authentication modes available in Amazon WorkMail.

###### Note

The choice of authentication mode depends on your organization's security
requirements and user experience preferences. It is recommended to use
_IAM Identity Center only_ mode as it provides enhanced security by
enforcing IAM Identity Center credentials and MFA. However, before switching from the
_Amazon WorkMail Directory and IAM Identity Center_ mode, make sure to test the MFA
process with all your users to ensure a smooth transition and avoid any impact on
existing email client access.

- **Amazon WorkMail Directory and IAM Identity Center (recommended for
  testing)** – This is the default option for you to test the
  IAM Identity Center associations before switching to production mode. Test mode allows users
  to log into the Amazon WorkMail web client using both the Amazon WorkMail directory and IAM Identity Center
  credentials. When you share the Amazon WorkMail web application URL from the
  _Organization_ settings, your user can log in using their
  Amazon WorkMail directory credentials. When you share the MFA-enabled URL from the IAM Identity Center
  settings, you user can log in using their IAM credentials.
- **IAM Identity Center only (recommended for production)**
  – This authentication mode only allows you to login into the Amazon WorkMail client
  mailbox using the IAM Identity Center credentials. For any existing Amazon WorkMail users, the Amazon WorkMail
  directory credentials are no longer valid for both the Amazon WorkMail web application and
  any existing email clients. You can request a personal access token to access
  the mailbox using any email clients. To avoid losing access to mailboxes, make
  sure MFA is enabled for all Amazon WorkMail users.

###### To enable authentication mode, follow these steps.

1. Under the **Identity Center Settings** page, choose the
   **Authentication Mode** tab.
2. Choose **Edit**.

The **Edit authentication mode** page appears. 3. Select one of the following:

    * *IAM Identity Center only*
    * *Amazon WorkMail Directory and IAM Identity Center*

4. Choose **Save**.
