# Edit Amazon DataZone domains

In Amazon DataZone, a domain is an organizing entity for connecting together your assets,
users, and their projects. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

After you create an Amazon DataZone domain, you can later edit the domain to: change the
description, enable IAM Identity Center, and add, edit, or remove tag keys and their
values. To edit an Amazon DataZone domain, you must assume an IAM role in the account with
administrative permissions. [Configure the IAM permissions required to use the
Amazon DataZone management console](create-iam-roles.md "create-iam-roles.md") to obtain the minimum permissions necessary to
edit a domain.

To edit a domain, complete the following steps:

1. Sign in to the AWS Management Console and open the Amazon DataZone console at
   [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Choose **View domains** and choose the domain’s name from the
   list. The name is a hyperlink.
3. On the details page for the domain, choose **Edit**.
4. - Edit the **Description**.
   - Set the **IAM Identity Center settings**. Learn more
     about these settings in [Setting up AWS IAM Identity Center for Amazon DataZone](sso-setup.md "sso-setup.md").
   - Add, edit, or remove **Tag** keys and their
     values.
5. Once you’ve made your edits, choose **Update domain**.
