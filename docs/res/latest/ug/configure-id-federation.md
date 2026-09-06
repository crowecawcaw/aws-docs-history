

# Configuring your identity provider for single sign-on (SSO)
<a name="configure-id-federation"></a>

Research and Engineering Studio integrates with any SAML 2.0 identity provider to authenticate user access to the RES portal. These steps provide directions to integrate with your chosen SAML 2.0 identity provider. If you intend to use IAM Identity Center, see [Setting up single sign-on (SSO) with IAM Identity Center](sso-idc.md).

**Note**  
The user's email must match in the IDP SAML assertion and Active Directory. You will need to connect your identity provider with your Active Directory and periodically sync users.

**Topics**
+ [Configure your identity provider](#configure-id-federation_config-idp)
+ [Configure RES to use your identity provider](#configure-id-federation_config-res)
+ [Configuring your identity provider in a non-production environment](#configure-id-federation-demo-env)
+ [Debugging SAML IdP issues](#configure-id-federation_debug)

## Configure your identity provider
<a name="configure-id-federation_config-idp"></a>

This section provides the steps to configure your identity provider with information from the RES Amazon Cognito user pool.

1. RES assumes that you have an AD (AWS Managed AD or a self-provisioned AD) with the user identities allowed to access the RES portal and projects. Connect your AD to your identity service provider and sync the user identities. Check your identity provider's documentation to learn how to connect your AD and sync user identities. For example, see [Using Active Directory as an identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/gs-ad.html) in the *AWS IAM Identity Center User Guide*.

1. Configure a SAML 2.0 application for RES in your identity provider (IdP). This configuration requires the following parameters:
   + **SAML Redirect URL** — The URL that your IdP uses to send the SAML 2.0 response to the service provider.
**Note**  
Depending on the IdP, the SAML Redirect URL might have a different name:  
Application URL
Assertion Consumer Service (ACS) URL
ACS POST Binding URL

**To get the URL**

     1. Sign in to RES as an **admin** or **clusteradmin**.

     1. Navigate to **Environment Management** ⇒ **General Settings** ⇒ **Identity Provider**.

     1. Choose **SAML Redirect URL**.
   + **SAML Audience URI** — The unique ID of the SAML audience entity on the service provider side.
**Note**  
Depending on the IdP, the SAML Audience URI might have a different name:  
ClientID
Application SAML Audience
SP entity ID

     Provide the input in the following format.

     ```
     urn:amazon:cognito:sp:{{user-pool-id}}
     ```

**To find your SAML Audience URI**

     1. Sign in to RES as an **admin** or **clusteradmin**.

     1. Navigate to **Environment Management** ⇒ **General Settings** ⇒ **Identity Provider**.

     1. Choose **User Pool Id**.

1. The SAML assertion posted to RES must have the following fields/claims set to the user's email address:
   + SAML Subject or NameID
   + SAML email

1. Your IdP adds fields/claims to the SAML assertion, based on the configuration. RES requires these fields. Most providers automatically fill these fields by default. Refer to the following field inputs and values if you have to configure them.

   
   + **AudienceRestriction** — Set to `urn:amazon:cognito:sp:{{user-pool-id}}`. Replace {{user-pool-id}} with the ID of your Amazon Cognito user pool.

     ```
     <saml:AudienceRestriction>
         <saml:Audience> urn:amazon:cognito:sp:{{user-pool-id}}
     </saml:AudienceRestriction>
     ```
   + **Response** — Set `InResponseTo` to `https://{{user-pool-domain}}/saml2/idpresponse`. Replace {{user-pool-domain}} with the domain name of your Amazon Cognito user pool.

     ```
     <saml2p:Response 
       Destination="https://{{user-pool-domain}}/saml2/idpresponse"
       ID="id123" 
       InResponseTo="_dd0a3436-bc64-4679-a0c2-cb4454f04184" 
       IssueInstant="Date-time stamp" 
       Version="2.0" 
       xmlns:saml2p="urn:oasis:names:tc:SAML:2.0:protocol" 
       xmlns:xs="http://www.w3.org/2001/XMLSchema">
     ```
   + **SubjectConfirmationData** — Set `Recipient` to your user pool `saml2/idpresponse` endpoint and `InResponseTo` to the original SAML request ID.

     ```
     <saml2:SubjectConfirmationData 
       InResponseTo="_dd0a3436-bc64-4679-a0c2-cb4454f04184" 
       NotOnOrAfter="Date-time stamp" 
       Recipient="https://{{user-pool-domain}}/saml2/idpresponse"/>
     ```
   + **AuthnStatement** — Configure as the following:

     ```
     <saml2:AuthnStatement AuthnInstant="2016-10-30T13:13:28.152TZ"
       SessionIndex="32413b2e54db89c764fb96ya2k" SessionNotOnOrAfter="2016-10-30T13:13:28">
         <saml2:SubjectLocality />
         <saml2:AuthnContext>
             <saml2:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</saml2:AuthnContextClassRef>
         </saml2:AuthnContext>
     </saml2:AuthnStatement>
     ```

1. If your SAML application has a logout URL field, set it to: `{{<domain-url>}}/saml2/logout`.

**To get the domain URL**

   1. Sign in to RES as an **admin** or **clusteradmin**.

   1. Navigate to **Environment Management** ⇒ **General Settings** ⇒ **Identity Provider**.

   1. Choose **Domain URL**.

1. If your IdP accepts a signing certificate to establish trust with Amazon Cognito, download the Amazon Cognito signing certificate and upload it in your IdP.

**To get the signing certificate**

   1. Open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/v2/idp/user-pools/). 

   1. Select your user pool. Your user pool should be `res-{{<environment name>}}-user-pool`.

   1. Select the **Sign-in experience** tab.

   1. In the **Federated identity provider sign-in** section, choose **View signing certificate**.  
![The Amazon Cognito console with the View signing certificate button in the Federated identity provider sign-in section for a selected user pool.](http://docs.aws.amazon.com/res/latest/ug/images/cognito-user-pool-signing-cert.png)

      You can use this certificate to set up Active Directory IDP, add a `relying party trust`, and enable SAML support on this relying party.
**Note**  
This doesn't apply to Keycloak and IDC.

   1. After the application setup is complete, download the SAML 2.0 application metadata XML or URL. You use it in the next section.

## Configure RES to use your identity provider
<a name="configure-id-federation_config-res"></a>

**To complete the single sign-on setup for RES**

1. Sign in to RES as an **admin** or **clusteradmin**.

1. Navigate to **Environment Management** ⇒ **General Settings** ⇒ **Identity Provider**.  
![The Environment Settings user interface in RES, including a section for Single Sign-On.](http://docs.aws.amazon.com/res/latest/ug/images/environment-settings.png)

1. Under **Single Sign-On**, choose the edit icon next to the status indicator to open the **Single Sign On Configuration** page.  
![The Single Sign On Configuration user interface in RES.](http://docs.aws.amazon.com/res/latest/ug/images/sso-config.png)

   1. For **Identity Provider**, choose **SAML**.

   1. For **Provider Name**, enter a unique name for your identity provider.
**Note**  
The following names are not allowed:  
Cognito
IdentityCenter

   1. Under **Metadata Document Source**, choose the appropriate option and upload the metadata XML document or provide the URL from the identity provider.

   1. For **Provider Email Attribute**, enter the text value `email`.

   1. Choose **Submit**.

1. Reload the **Environment Settings** page. Single sign-on is enabled if the configuration was correct.

## Configuring your identity provider in a non-production environment
<a name="configure-id-federation-demo-env"></a>

If you used the provided [external resources](prerequisites.md#external-resources) to create a non-production RES environment and configured IAM Identity Center as your identity provider, you may want to configure a different identity provider such as Okta. The RES SSO enablement form asks for three configuration parameters: 

1. Provider name — Cannot be modified

1. Metadata document or URL — Can be modified

1. Provider email attribute — Can be modified

**To modify the metadata document and provider email attribute, do the following:**

1.  Go to the Amazon Cognito console. 

1. From the navigation, choose **User pools**.

1. Select your user pool to view the **User pool overview**.

1. From the **Sign-in experience** tab, go to **Federated identity provider sign-in** and open your configured identity provider. 

1. Generally, you will only be required to change the metadata and leave the attribute mapping unchanged. To update **Attribute mapping**, choose **Edit**. To update the **Metadata document**, choose **Replace metadata**.  
![The Amazon CognitoUser pool overview.](http://docs.aws.amazon.com/res/latest/ug/images/res-attributemetadata.png)

1. If you edited the attribute mapping, you will need to update the `<environment name>.cluster-settings` table in DynamoDB. 

   1. Open the DynamoDB console and choose **Tables** from the navigation. 

   1. Find and select the `<environment name>.cluster-settings` table, and from the **Actions** menu select **Explore items**.

   1. Under **Scan or query items**, go to **Filters** and enter the following parameters:
      + **Attribute name** — `key`
      + **Value** — `identity-provider.cognito.sso_idp_provider_email_attribute`

   1. Choose **Run**. 

1. Under **Items returned**, find the `identity-provider.cognito.sso_idp_provider_email_attribute` string and choose **Edit** to modify the string to match your changes in Amazon Cognito.  
![The Amazon CognitoUpdate the Filters and Items returned in DynamoDB.](http://docs.aws.amazon.com/res/latest/ug/images/res-scanqueryitems.png)

## Debugging SAML IdP issues
<a name="configure-id-federation_debug"></a>

**SAML-tracer** — You can use this extension for the Chrome browser to track SAML requests and check the SAML assertion values. For more information, see [ SAML-tracer](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch?pli=1) at the Chrome web store.

**SAML developer tools** — OneLogin provides tools that you can use to decode the SAML encoded value and check the required fields in the SAML assertion. For more information, see [Base 64 Decode \+ Inflate](https://www.samltool.com/decode.php) at the OneLogin web site.

**Amazon CloudWatch Logs** — You can check your RES logs in CloudWatch Logs for errors or warnings. Your logs are in a log group with the name format `/{{res-environment-name}}/cluster-manager`.

**Amazon Cognito documentation** — For more information about SAML integration with Amazon Cognito, see [Adding SAML identity providers to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-saml-idp.html) in the *Amazon Cognito Developer Guide*.