# Creating shortcut links to AWS Management Console destinations

Shortcut links created in the AWS access portal take IAM Identity Center users to a specific destination in
the AWS Management Console, with a specific permission set, and in a specific AWS account.

Shortcut links save time for you and your collaborators. Instead of navigating to a
desired destination URL in the AWS Management Console (for example, an Amazon S3 bucket instance page) through
multiple pages, including AWS access portal, you can use a shortcut link to get to the same
destination automatically.

## Shortcut link destination

options

Shortcut links have three destination options, listed here by priority:

- (Optional) Any destination URL in the AWS Management Console specified in the shortcut link. For
  example, the Amazon S3 bucket instance page.
- (Optional) Administrator-configured relay state URL for the permission set in
  question. For more information about setting the relay state, see [Set relay state for quick access to the
  AWS Management Console](howtopermrelaystate.md "howtopermrelaystate.md").
- AWS Management Console home. The default destination if you do not specify one.

###### Note

Automatic navigation to a destination is successful only when you’re authenticated
with IAM Identity Center and have the necessary permission set assigned for the AWS account and
destination URL.

The AWS access portal includes a **Create shortcut** button that helps you
create a shareable shortcut link. If you plan to specify a destination URL (the first option
in the previous list), you can copy the URL to a clipboard to share it.

## Create a shortcut link in the AWS access portal

1. While signed into the AWS access portal, choose the **Accounts** tab and
   then choose the **Create shortcut** button.
2. In the dialog box:
   1. Choose an AWS account using the account ID or account name. As you type, a
      drop-down menu displays matching account IDs and names that you can access. You can
      choose only an account to which you have access.
   2. Optionally choose an IAM role from the drop-down list. These are the
      permission sets assigned to you for the selected account. If you omit choosing the
      role, users are prompted to select one assigned to them for the chosen account when
      using the shortcut link.

   ###### Note

   You cannot grant new access with shortcut links. Shortcut links work only with
   the permission sets already assigned to the user. If the user doesn't have the
   necessary permission sets assigned for the account and destination URL, they are
   denied access. 3. Optionally enter the AWS access portal destination URL. If you omit entering a URL,
   the destination is automatically determined when using the shortcut link, based on
   the previously-mentioned shortcut link destination options. 4. Your shortcut link generates at the bottom of the dialog box, based on your
   input. Choose the **Copy URL** button. You can now create a
   bookmark with the copied shortcut link or share it with your collaborators who have
   access to the same account with the same permission set or another sufficient
   permission set.

## Constructing secure AWS Management Console shortcut links

with URL encoding

All parameter values of the URL, including the account ID, permission set name, and
destination URL, must be URL-encoded.

Shortcut links extend the AWS access portal URL with the following path:

`/#/console?account_id=`[account_ID]`&role_name=`[permission_set_name]`&destination=`[destination_URL]``

The full URL in the classic AWS partition follows this pattern:

**IPv4 endpoint:**

`https://`[your_subdomain]`.awsapps.com/start/#/console?account_id=`[account_ID]`&role_name=`[permission_set_name]`&destination=`[destination_URL]``

**Dual-stack endpoint**

`https://`[identity_center_instance_id]`.portal.`[region]`.app.aws/#/console?account_id=`[account_ID]`&role_name=`[permission_set_name]`&destination=`[destination_URL]``

Here's an example shortcut link that signs a user into account `123456789012`
with the `S3FullAccess` permission set, and takes them to the S3 console home
page:

- **IPv4 endpoint:**
  `https://example.awsapps.com/start/#/console?account_id=123456789012&role_name=S3FullAccess&destination=https%3A%2F%2Fconsole.aws.amazon.com%2Fs3%2Fhome`
- **Dual-stack endpoint:**
  `https://ssoins-1234567890abcdef.portal.us-east-1.app.aws/#/console?account_id=123456789012&role_name=S3FullAccess&destination=https%3A%2F%2Fconsole.aws.amazon.com%2Fs3%2Fhome`
- **(AWS GovCloud (US) Region) IPv4 endpoint:**
  `https://start.us-gov-west-1.us-gov-home.awsapps.com/directory/example/#/console?account_id=123456789012&role_name=S3FullAccess&destination=https%3A%2F%2Fconsole.amazonaws-us-gov.com%2Fs3%2Fhome`
- **(AWS GovCloud (US) Region) Dual-stack endpoint:**
  `https://ssoins-1234567890abcdef.portal.us-gov-west-1.app.aws/#/console?account_id=123456789012&role_name=S3FullAccess&destination=https%3A%2F%2Fconsole.amazonaws-us-gov.com%2Fs3%2Fhome`
