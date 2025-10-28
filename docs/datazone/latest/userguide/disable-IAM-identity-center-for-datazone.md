# Disable IAM Identity Center

for Amazon DataZone

Disabling AWS IAM Identity Center for an Amazon DataZone domain will remove access for
all SSO users.

###### Note

Disabling IAM Identity Center will not stop billing for SSO users. To stop billing
for SSO users, you must deactivate them in your domain. Billing continues until the
end of the month in which a user is deactivated. To deactivate users, see [Manage users in the Amazon DataZone console](user-management-console.md "user-management-console.md").

You can provide SSO users and groups with access to your Amazon DataZone data portal using
AWS IAM Identity Center. If you have enabled AWS IAM Identity Center for Amazon DataZone,
you can later disable access for all users.

To disable AWS IAM Identity Center for use with your Amazon DataZone domain, you must
assume an IAM role in the account with administrative permissions. [Configure the IAM permissions required to use the
Amazon DataZone management console](create-iam-roles.md "create-iam-roles.md") and [Create a custom policy for IAM
permissions to enable the Amazon DataZone service console simplified role creation](create-iam-roles.md#create-custom-to-manage-EZCRZ "create-iam-roles.md#create-custom-to-manage-EZCRZ") to obtain the minimum permissions
necessary to disable IAM Identity Center from use with Amazon DataZone.

Complete the following procedure to disable the AWS IAM Identity Center for
Amazon DataZone.

1. Sign in to the AWS Management Console and open the DataZone console at
   [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Select **View domains** and choose the domain’s name from the
   list. The name is a hyperlink.
3. Copy the **Amazon Resource Name (ARN)** for your domain,
   which starts with
   arn:aws:datazone:<regionName>:<accountId>:domain/<domainName>.
4. Open the IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
5. Choose **Applications**.
6. Choose the domain for which you want to disable AWS IAM Identity Center,
   which as a result will remove access to the domain’s data portal for all SSO
   users. You can use the **Filter** menu and the search box to
   filter the list of applications.
7. From the **Actions** menu, choose
   **Disable**.
8. SSO users will lose access to the Amazon DataZone domain.
9. To re-enable AWS IAM Identity Center for the Amazon DataZone domain, choose the
   domain for which you want to re-enable AWS IAM Identity Center, and from the
   **Actions** menu, choose
   **Enable**.
