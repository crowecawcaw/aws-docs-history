

# User-identity trust providers for Verified Access
<a name="user-trust"></a>

You can choose to use either AWS IAM Identity Center or an OpenID Connect-compatible user-identity trust provider.

**Topics**
+ [Using IAM Identity Center as a trust provider](#identity-center)
+ [Use an OpenID Connect trust provider](#oidc-provider)

## Using IAM Identity Center as a trust provider
<a name="identity-center"></a>

You can use AWS IAM Identity Center as your *user-identity* trust provider with AWS Verified Access.

### Prerequisites and considerations
<a name="create-idc-prereq"></a>
+ Your IAM Identity Center instance must be an AWS Organizations instance. A standalone AWS account IAM Identity Center instance will not work.
+ Your IAM Identity Center instance must be enabled in the same AWS Region that you want to create the Verified Access trust provider in.
+ Verified Access can provide access to users in IAM Identity Center who are assigned to up to 1,000 groups.

See [Manage organization and account instances of IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html) in the *AWS IAM Identity Center User Guide* for details on the different instance types.

### Create an IAM Identity Center trust provider
<a name="create-identity-center"></a>

After IAM Identity Center is enabled on your AWS account, you can use the following procedure to set up IAM Identity Center as your trust provider for Verified Access.

**To create an IAM Identity Center trust provider (AWS console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access trust providers**, and then **Create Verified Access trust provider**.

1. (Optional) For **Name tag** and **Description**, enter a name and description for the trust provider.

1. For **Policy reference name**, enter an identifier to use later when working with policy rules.

1. Under **Trust provider type**, select **User trust provider**.

1. Under **User trust provider type**, select **IAM Identity Center**.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and the tag value.

1. Choose **Create Verified Access trust provider**.

**To create an IAM Identity Center trust provider (AWS CLI)**
+ [create-verified-access-trust-provider](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-verified-access-trust-provider.html) (AWS CLI)

### Delete an IAM Identity Center trust provider
<a name="delete-identity-center"></a>

Before you can delete a trust provider, you must remove all endpoint and group configuration from the instance to which the trust provider is attached.

**To delete an IAM Identity Center trust provider (AWS console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access trust providers**, and then select the trust provider you want to delete under **Verified Access trust providers**.

1. Choose **Actions**, then **Delete Verified Access trust provider**.

1. Confirm the deletion by entering `delete` into the text box.

1. Choose **Delete**.

**To delete an IAM Identity Center trust provider (AWS CLI)**
+ [delete-verified-access-trust-provider](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-verified-access-trust-provider.html) (AWS CLI)

## Use an OpenID Connect trust provider
<a name="oidc-provider"></a>

AWS Verified Access supports identity providers that use standard OpenID Connect (OIDC) methods. You can use OIDC compatible providers as *user-identity* trust providers with Verified Access. However, due to the wide array of potential OIDC providers, AWS is not able to test each OIDC integration with Verified Access.

Verified Access obtains the trust data that it evaluates from the OIDC provider's `UserInfo Endpoint`. The `Scope` parameter is used to determine which sets of trust data will be retrieved. After the trust data is received, the Verified Access policy is evaluated against it.

With trust providers created as of February 24, 2025, the ID token claims from the OIDC trust provider are included in the `addition_user_context` key.

With trust providers created before February 24, 2025, Verified Access does not use trust data from the `ID token` sent by the OIDC provider. Only trust data from the `UserInfo Endpoint` is evaluated against the policy.

With trust providers created as of February 24, 2025, the default session duration is one day. With trust providers created before February 24, 2025, the default session duration is seven days.

If a refresh token is specified, Verified Access uses the expiration of the refresh token as the session duration. If there is no refresh token, the default session duration is used.

**Topics**
+ [Prerequisites for creating an OIDC trust provider](#create-oidc-prereq)
+ [Create an OIDC trust provider](#create-oidc-provider)
+ [Modify an OIDC trust provider](#modify-oidc-provider)
+ [Delete an OIDC trust provider](#delete-oidc-provider)

### Prerequisites for creating an OIDC trust provider
<a name="create-oidc-prereq"></a>

You will need to gather the following information from your trust provider service directly:
+ Issuer
+ Authorization endpoint
+ Token endpoint
+ UserInfo endpoint
+ Client ID
+ Client secret
+ Scope

### Create an OIDC trust provider
<a name="create-oidc-provider"></a>

Use the following procedure to create an OIDC as your trust provider.

**To create an OIDC trust provider (AWS console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access trust providers**, and then **Create Verified Access trust provider**.

1. (Optional) For **Name tag** and **Description**, enter a name and description for the trust provider.

1. For **Policy reference name**, enter an identifier to use later when working with policy rules.

1. Under **Trust provider type**, select **User trust provider**.

1. Under **User trust provider type**, select **OIDC (OpenID Connect)**.

1. For **OIDC (OpenID Connect)**, choose the trust provider.

1. For **Issuer**, enter the identifier of the OIDC issuer.

1. For **Authorization endpoint**, enter the full URL of the authorization endpoint.

1. For **Token endpoint**, enter the full URL of the token endpoint.

1. For **User endpoint**, enter the full URL of the user endpoint.

1. (Native Application OIDC) For **Public signing key URL**, enter the full URL of the public signing key endpoint.

1. Enter the OAuth 2.0 client identifier for **Client ID**.

1. Enter the OAuth 2.0 client secret for **Client secret**.

1. Enter a space-delimited list of scopes defined with your identity provider. At minimum, the openid scope is required for **Scope**.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and the tag value.

1. Choose **Create Verified Access trust provider**.

1. You must add a redirect URI to the allow list for your OIDC provider.
   + HTTP applications – Use the following URI: **https://application\_domain/oauth2/idpresponse**. In the console, you can find the application domain on the **Details** tab for the Verified Access endpoint. Using the AWS CLI or an AWS SDK, the application domain is included in the output when you describe the Verified Access endpoint.
   + TCP applications – Use the following URI: **http://localhost:8000**.

**To create an OIDC trust provider (AWS CLI)**
+ [create-verified-access-trust-provider](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-verified-access-trust-provider.html) (AWS CLI)

### Modify an OIDC trust provider
<a name="modify-oidc-provider"></a>

After you create a trust provider, you can update its configuration.

**To modify an OIDC trust provider (AWS console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access trust providers**, and then select the trust provider you want to modify under **Verified Access trust providers**.

1. Choose **Actions**, then **Modify Verified Access trust provider**.

1. Modify the options you want to change.

1. Choose **Modify Verified Access trust provider**.

**To modify an OIDC trust provider (AWS CLI)**
+ [modify-verified-access-trust-provider](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-verified-access-trust-provider.html) (AWS CLI)

### Delete an OIDC trust provider
<a name="delete-oidc-provider"></a>

Before you can delete a user trust provider, you first need to remove all endpoint and group configuration from the instance the trust provider is attached to.

**To delete an OIDC trust provider (AWS console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access trust providers**, and then select the trust provider you want to delete under **Verified Access trust providers**.

1. Choose **Actions**, then **Delete Verified Access trust provider**.

1. Confirm the deletion by entering `delete` into the text box.

1. Choose **Delete**.

**To delete an OIDC trust provider (AWS CLI)**
+ [delete-verified-access-trust-provider](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-verified-access-trust-provider.html) (AWS CLI)