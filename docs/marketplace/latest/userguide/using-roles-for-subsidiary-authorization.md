

# Subsidiary authorization service role
<a name="using-roles-for-subsidiary-authorization"></a>

If you register your local entities as separate AWS Marketplace seller accounts, you can maintain a product in one account and authorize your other accounts to sell it. The account that owns the product is the *primary account*. An account that is authorized to sell it is a *subsidiary account*. For more information about subsidiary authorization, see [Creating private offers as a subsidiary account](subsidiary-offers.md).

To share an authorization from the primary account to the subsidiary account, AWS needs permission to create and manage that share for you. To grant that permission, create the `AWSMarketplaceSubsidiaryAuthorizationServiceRole` service role in AWS Partner Central.

**Important**  
If this role doesn't exist, AWS can't share the authorization with the subsidiary account. The primary account can still create the authorization. However, the authorization never becomes active, and the subsidiary account can't see it or use it to create offers.

## Creating the service role
<a name="create-subsidiary-authorization-service-role"></a>

Create this role before you create your first subsidiary authorization. Both the primary account and the subsidiary account need it.

Before you begin, make sure that you have the following:
+ Permissions to create IAM roles. If you don't have them, ask your administrator to grant them or to complete these steps for you. For more information about IAM roles, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.
+ Access to each connected account that shares or receives subsidiary authorizations

**To create the subsidiary authorization service role**

1. Sign in to AWS Partner Central and open the [Service roles](https://console.aws.amazon.com/partnercentral/settings?tab=service-roles) tab of the **Settings** page.

1. On the **Service roles** tab, choose **Create Partner Central service role**.

1. For **Service role name**, enter **AWSMarketplaceSubsidiaryAuthorizationServiceRole**.

1. Choose **Save role**.

The `AWSMarketplaceSubsidiaryAuthorizationServiceRole` role appears on the **Service roles** tab. If it doesn't appear, refresh the page. If saving fails, confirm that you have permissions to create IAM roles and that a role with this name doesn't already exist in the account.

Repeat these steps in each account that doesn't have the role yet. Then create the authorization. For instructions, see [Authorizing a subsidiary account to sell your product](subsidiary-offers.md#authorize-a-subsidiary).

## What the role allows
<a name="subsidiary-authorization-service-role-permissions"></a>

With `AWSMarketplaceSubsidiaryAuthorizationServiceRole`, AWS Marketplace can create, accept, and delete the subsidiary authorization. AWS Marketplace uses the role when you create an authorization and when you revoke one.

The role doesn't give the primary account access to the subsidiary account's offers, agreements, transactions, or financial data. It also doesn't let the subsidiary account change the primary account's product listing.

## Authorization or resource share creation fails
<a name="subsidiary-authorization-service-role-troubleshooting"></a>

Use this section if creating a new authorization fails, or if the Catalog API returns an error that indicates the resource share couldn't be created.

AWS Marketplace uses the `AWSMarketplaceSubsidiaryAuthorizationServiceRole` service role to create the resource share between the two accounts. If the role is missing from the primary account, the subsidiary account, or both, AWS Marketplace can't create the share. The role might be missing because no one created it, or because someone deleted it.

To resolve this issue, do the following:

1. In each account, check whether the role appears on the **Service roles** tab.

1. Create the role in any account that doesn't have it. For instructions, see [Creating the service role](#create-subsidiary-authorization-service-role).

1. Create the authorization again.