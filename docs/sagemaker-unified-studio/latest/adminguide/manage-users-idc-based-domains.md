

# Managing users for Identity Center-based domains
<a name="manage-users-idc-based-domains"></a>

Configure single sign-on (SSO) access to your Amazon SageMaker unified domain through IAM Identity Center or SAML federation. You can also manage root domain unit owners from this page.

## Enable IAM Identity Center
<a name="enable-iam-identity-center"></a>

To enable access to the Amazon SageMaker unified domains in the Amazon SageMaker Unified Studio for users with SSO credentials, complete the following procedure: 

**Note**  
The Amazon SageMaker Unified Studio domain can reside in a different AWS Region than where the IAM Identity Center organization instance is located using IAM Identity Center multi-Region support. Once IAM Identity Center multi-Region is set up, follow the same steps in the following procedure to enable single sign-on through IAM Identity Center for your domain. To use this feature, your IAM Identity Center instance must be connected to an external identity provider (IdP). For information on setting up IAM Identity Center multi-Region, see [Using IAM Identity Center across multiple AWS Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html).

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and use the region selector in the top navigation bar to choose the appropriate AWS Region.

1. Either create a new or choose an existing Amazon SageMaker unified domain where you want to configure SSO user access. 

1. On the domain's details page, either choose **Configure** next to the **Configure SSO user access** in the **Next steps for your domain section** or navigate to the **User management** tab and choose **Configure SSO user access**.

1. On the **Choose user authentication method**, choose the **IAM Identity Center**. With IAM Identity Center, users configured in IAM Identity Center can access the domain's Amazon SageMaker Unified Studio. 

   You are either connecting to an organization instance of the IAM Identity Center or to an account instance of the IAM Identity Center.
   + If the account is the management account of an AWS Organization and IAM Identity Center organization instance is enabled, the IAM Identity Center organization instance is selected.
   + If the account is a member account of an AWS Organization and IAM Identity Center organization instance is enabled, an IAM Identity Center account instance is selected.
   + If the account is not a member account of an AWS Organization, an IAM Identity Center account instance is selected.

1. On the **Configure IAM Identity Center** details page, verify that your domain is connected to the IAM Identity Center and then choose user and group assignment method. You can choose either **Require assignments** - which allows only assigned IAM Identity Center users and groups access to this domain or **Do not require assignments** - which allows all authorized IAM Identity Center users and groups access to this domain.

1. On the **Review and save** page, review your choices and then choose **Save**. These settings cannot be changed once you save them. 

1. If you've chosen to require assignments, use the **Add users and groups** to add IAM Identity Center users and groups to your Amazon SageMaker Unified Studio domain.

## Enable SAML
<a name="enable-saml"></a>

Complete the following procedure to configure SAML user access to Amazon SageMaker Unified Studio for your Amazon SageMaker unified domain.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and use the region selector in the top navigation bar to choose the appropriate AWS Region.

1. Either create a new or choose an existing Amazon SageMaker unified domain where you want to configure SAML user access. 

1. On the domain's details page, either choose **Configure** next to the **Configure SSO user access** in the **Next steps for your domain** section or navigate to the **User management** tab and choose **Configure SSO user access**.

1. On the **Choose user authentication method** page, choose **SAML**. With SAML, users configured through external Identity Providers (IdPs) can access the domain's Amazon SageMaker Unified Studio. Choose **Next**.

1. On the **Configure SAML** page, specify the Identity Provider (IdP) SSO URL. You must first configure a new IdP in the IAM console. You must then also choose the user and group assignment method. You can choose either **Require assignments** - which allows only assigned IAM Identity Center users and groups access to this domain or **Do not require assignments** - which allows all authorized IAM Identity Center users and groups access to this domain.

1. On the **Review and save** page, review your choices and then choose **Save**. These settings cannot be changed once you save them. 

1. If you've chosen to require assignments, use the **Add users and groups** to add SAML users and groups to your domain.

## Update Root Domain Unit Owner
<a name="update-root-domain-unit-owner"></a>

Complete the following procedure to manage root domain owners for your Amazon SageMaker unified domain. 

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and use the region selector in the top navigation bar to choose the appropriate AWS Region.

1. Either create a new or choose an existing Amazon SageMaker unified domain and then navigate to the **User management** tab.

1. You can select existing owners and then expand the **Actions** menu and choose to **Remove** these owners.

   You can add new owners, by expanding **Add** and choosing the add SSO users and groups or IAM users and groups.

The root domain unit owner for your Amazon SageMaker domain can be changed using AWS CLI or API. This procedure is helpful when the original IAM role/user no longer exists and ownership needs to be replaced.

To use the AWS CLI to update the root domain unit owner, use the update-root-domain-unit-owner command. The IAM user or role initiating the call needs to have the datazone:UpdateRootDomainUnitOwner permission.

Considerations:

1. Domain ID, Current Owner, and New Owner are required.

1. The new owner needs to exist as a user in the domain.

1. SSO users/groups are referenced using their display name. IAM users/groups are referenced using their ARN.

Example command:

```
  aws datazone update-root-domain-unit-owner \
  --domain-identifier DOMAIN_ID \
  --current-owner CURRENT_OWNER \
  --new-owner NEW_OWNER
```