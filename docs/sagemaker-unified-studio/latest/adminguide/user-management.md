# Managing users in Amazon SageMaker Unified Studio

By default, Amazon SageMaker unified domains support IAM user credentials. You can also
enable access to the Amazon SageMaker unified domains in the Amazon SageMaker Unified Studio for users with SSO and
SAML credentials. To do this, complete the following procedures.

To enable access to the Amazon SageMaker unified domains in the Amazon SageMaker Unified Studio for users with SSO
credentials, complete the following procedure:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Either create a new or choose an existing Amazon SageMaker unified domain where you want
   to configure SSO user access.
3. On the domain's details page, either choose **Configure** next to the
   **Configure SSO user access** in the **Next steps for your domain
   section** or navigate to the **User management** tab and choose
   **Configure SSO user access**.
4. On the **Choose user authentication method**, choose the **IAM
   Identity Center**. With IAM Identity Center, users configured in IAM Identity
   Center get to access the domain's Amazon SageMaker Unified Studio.

You are either connecting to an organization instance of the IAM Identity Center or to
an account instance of the IAM Identity Center.

    * If the account is the management account of an AWS Organization and IAM Identity
     Center organization instance is enabled, the IAM Identity Center organization instance
     is selected.
    * If the account is a member account of an AWS Organization and IAM Identity Center
     organization instance is enabled, an IAM Identity Center account instance is
     selected.
    * If the account is not a member account of an AWS Organization, an IAM Identity
     Center account instance is selected.

5. On the **Configure IAM Identity Center** details page, verify that your
   domain is connected to the IAM Identity Center and then choose user and group assignment
   method. You can choose either **Require assignments** - which allows only
   assigned IAM Identity Center users and groups access to this domain or **Do not
   require assignments** - which allows all authorized IAM Identity Center users and
   groups access to this domain.
6. On the **Review and save** page, review your choices and then choose
   **Save**. These settings cannot be changed once you save them.
7. If you've chosen to require assignments, use the **Add users and
   groups** to add IAM Identity Center users and groups to your Amazon SageMaker Unified Studio
   domain.
   Complete the following procedure to configure SAML user access to Amazon SageMaker Unified Studio for your Amazon
   SageMaker unified domain.

8. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
9. Either create a new or choose an existing Amazon SageMaker unified domain where you want
   to configure SAML user access.
10. On the domain's details page, either choose **Configure** next to the
    **Configure SSO user access** in the **Next steps for your
    domain** section or navigate to the **User management** tab and
    choose **Configure SSO user access**.
11. On the **Choose user authentication method** page, choose
    **SAML**. With SAML, users configured through external Identity Providers
    (IdPs) get to access the domain's Amazon SageMaker Unified Studio. Choose **Next**.
12. On the **Configure SAML** page, specify the Identity Provider (IdP) SSO
    URL. You must first configure a new IdP in the IAM console. You must then also choose the
    user and group assignment method. You can choose either **Require
    assignments** - which allows only assigned IAM Identity Center users and groups
    access to this domain or **Do not require assignments** - which allows all
    authorized IAM Identity Center users and groups access to this domain.
13. On the **Review and save** page, review your choices and then choose
    **Save**. These settings cannot be changed once you save them.
14. If you've chosen to require assignments, use the **Add users and
    groups** to add SAML users and groups to your domain.
    Complete the following procedure to manage root domain owners for your Amazon SageMaker
    unified domain.

15. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
    navigation bar to choose the appropriate AWS Region.
16. Either create a new or choose an existing Amazon SageMaker unified domain and the
    nativate to the **User management** tab.
17. You can select existing owners and then expand the **Actions** menu and
    choose to **Remove** these owners.

You can add new owners, by expanding **Add** and choosing the add SSO
users and groups or IAM users and groups.

## Update Root Domain Unit Owner

The root domain unit owner for your Amazon SageMaker domain can be changed using AWS CLI
or API. This procedure is helpful when the original IAM role/user no longer exists and
ownership needs to be replaced.

To use the AWS CLI to update the root domain unit owner, use the
update-root-domain-unit-owner command. The IAM user or role initiating the call needs to have
the datazone:UpdateRootDomainUnitOwner permission.

Considerations:

1. Domain ID, Current Owner, and New Owner are required.
2. The new owner needs to exist as a user in the domain.
3. SSO users/groups are referenced using their display name. IAM users/groups are
   referenced using their ARN.

Example command:

```

  aws datazone update-root-domain-unit-owner \
  --domain-identifier DOMAIN_ID \
  --current-owner CURRENT_OWNER \
  --new-owner NEW_OWNER

```
