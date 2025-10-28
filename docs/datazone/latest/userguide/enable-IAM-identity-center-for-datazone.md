# Enable IAM Identity Center for

Amazon DataZone

###### Note

To complete this procedure, you must have AWS IAM Identity Center enabled in the
same AWS Region as your Amazon DataZone domain.

You can provide SSO users and groups with access to your Amazon DataZone data portal using
AWS IAM Identity Center. After completing [Setting up AWS IAM Identity Center for Amazon DataZone](sso-setup.md "sso-setup.md"), you can enable your SSO users and groups to access your
Amazon DataZone domain data portal.

To enable AWS IAM Identity Center for use with your Amazon DataZone domain, you must
assume an IAM role in the account with administrative permissions. [Configure the IAM permissions required to use the
Amazon DataZone management console](create-iam-roles.md "create-iam-roles.md") and [Create a custom policy for IAM
permissions to enable the Amazon DataZone service console simplified role creation](create-iam-roles.md#create-custom-to-manage-EZCRZ "create-iam-roles.md#create-custom-to-manage-EZCRZ") to obtain the minimum permissions
necessary to enable IAM Identity Center for use with Amazon DataZone.

Complete the following procedure to enable the AWS IAM Identity Center for
Amazon DataZone.

1. Sign in to the AWS Management Console and open the DataZone console at
   [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Select **View domains** and choose the domain’s name from the
   list. The name is a hyperlink.
3. On the detail page for the domain, choose **Edit**.
   - Select the checkbox for **Enable users in IAM Identity
     Center**.
   - Choose whether to connect to an organization instance of the IAM
     Identity center or to connect to an account instance of the IAM identity
     center.
   - Choose between the two user assignment modes. Once your domain is
     updated with your selection, it cannot be changed later.
     - With **Implicit user assignment**, any user
       added to your IAM Identity Center directory can access your
       Amazon DataZone domain.
     - With **Explicit user assignment**, you will
       add specific users or groups from you IAM Identity Center
       directory to provide them access to your Amazon DataZone domain. You
       will add and remove these users and groups later in the
       Amazon DataZone Console.

4. Once you are satisfied with your selection, choose **Update
   domain**.
