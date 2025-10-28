Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Troubleshooting

connections from Amazon Redshift query editor v2

This list details errors that commonly occur and can help you to connect to your
Redshift database with query editor v2, using an AWS IAM Identity Center identity.

- Error: **Connection Issue: No Identity center session
  information available.** – When this error occurs, check your
  browser’s security and privacy settings. These browser settings, particularly those for
  secure cookies, such as Firefox’s Total Cookie Protection feature, can result in blocked
  connection attempts from Amazon Redshift query editor v2 to a Redshift database. Follow the remediation
  steps detailed for your browser:

      + **Firefox** – Currently, third-party cookies
       are blocked by default. Click the shield in the browser's address bar and switch the
       toggle to turn off enhanced tracking protection for query editor v2.
      + **Chrome incognito mode** – By default,
       Chrome Incognito mode blocks third party cookies. Click the eye icon in the address
       bar to allow third-party cookies for query editor v2. After you change the setting to allow
       cookies, you may not see the eye icon on the address bar.
      + **Safari** – On a Mac, open the Safari app.
       Choose **Settings**, then choose **Advanced**.
       Toggle to turn off: **Block all cookies**.
      + **Edge** – Choose
       **Settings**, then choose **Cookies and site
       permissions**. Then select **Manage and delete cookies and site
       data** and turn off **Block third-party
       cookies**.

  If you try to connect after changing the settings and continue to receive the error
  message **Connection Issue: No Identity center session information
  available**, we recommend that you refresh your connection with AWS IAM Identity Center.
  To do this, right click your Redshift database instance and choose
  **Refresh**. A new window appears, which you can use to
  authenticate.

- Error: **Connection issue: Identity center session expired or
  invalid.** – Following integration of a Redshift provisioned cluster
  or Serverless workgroup with AWS IAM Identity Center, a user might receive this error when they
  attempt to connect to a Redshift database from query editor v2. This can follow successful
  connection attempts. In this case, we recommend that you re-authenticate. To do this,
  right click your Redshift database instance and choose **Refresh**.
  A new window appears, which you can use to authenticate.
- Error: **Invalid scope. User credentials are not authorized to
  connect to Redshift.** – Following integration of a Redshift
  provisioned cluster or Serverless workgroup with AWS IAM Identity Center for identity management, a
  user might receive this error when they attempt to connect to a Redshift database from
  query editor v2. In this case, in order for query editor v2 to successfully connect and authenticate a
  user via AWS IAM Identity Center to access the correct resources, an administrator must assign the
  user to the Redshift AWS IAM Identity Center application through the Redshift console. This is
  completed under **IAM Identity Center connections**. Following this, the user
  can establish a successful connection after one hour, which is the limit of AWS IAM Identity Center
  session caching.
- Error: **Databases couldn't be listed. FATAL: Failed query when
  cluster is auto paused.** – When an Amazon Redshift Serverless database is in
  an idle state, not processing any workloads, it can remain paused when you connect with
  an AWS IAM Identity Center identity. To remedy this, log in with another authentication method to
  resume the Serverless workgroup. Then connect to the database with your AWS IAM Identity Center
  identity.
- Error: **An error occurred during the attempt to federate with
  AWS IAM Identity Center. An Amazon Redshift administrator must delete and recreate the AWS IAM Identity Center QEV2
  application, using the Redshift console.** – This error typically
  occurs when the AWS IAM Identity Center applicaiton instance associated with query editor v2 is deleted. To
  remedy this, an Amazon Redshift administrator must delete and recreate the Redshift and query editor v2
  applications for AWS IAM Identity Center. This can be performed on the Redshift console or using
  the [https://docs.aws.amazon.com/cli/latest/reference/redshift/delete-redshift-idc-application.html](../../../cli/latest/reference/redshift/delete-redshift-idc-application.md "../../../cli/latest/reference/redshift/delete-redshift-idc-application.md") CLI command.
