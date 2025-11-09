# Setting up service provider–initiated

federation with Quick Suite Enterprise edition

|                                            |
| ------------------------------------------ |
| \*_Applies<br>to:_<br>• Enterprise Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

###### Note

IAM identity federation doesn't support syncing identity provider groups
with Amazon Quick Suite.

After you have finished configuring your identity provider with AWS Identity and Access Management (IAM), you
can set up service provider–initiated sign in through Amazon Quick Suite Enterprise
Edition. For Quick Suite-initiated IAM federation to work, you need to authorize
Quick Suite to send the authentication request to your IdP. A Quick Suite
administrator can configure this by adding the following information provided by the
IdP:

- The IdP URL – Quick Suite redirects users to this URL for
  authentication.
- The relay state parameter – This parameter relays the state that the
  browser session was in when it was redirected for authentication. The IdP
  redirects the user back to the original state after authentication. The state is
  provided as a URL.
  The following table shows the standard authentication URL
  and relay state parameter for redirecting the user to the Quick Suite URL that you
  provide.

| Identity provider | Parameter        | Authentication URL                                                                         |
| ----------------- | ---------------- | ------------------------------------------------------------------------------------------ |
| Auth0             | `RelayState`     | `https://<sub_domain>.auth0.com/samlp/<app_id>`                                            |
| Google accounts   | `RelayState`     | `https://accounts.google.com/o/saml2/initsso?idpid=<idp_id>&spid=<sp_id>&forceauthn=false` |
| Microsoft Azure   | `RelayState`     | `https://myapps.microsoft.com/signin/<app_name>/<app_id>?tenantId=<tenant_id>`             |
| Okta              | `RelayState`     | `https://<sub_domain>.okta.com/app/<app_name>/<app_id>/sso/saml`                           |
| PingFederate      | `TargetResource` | `https://<host>/idp/<idp_id>/startSSO.ping?PartnerSpId=<sp_id>`                            |
| PingOne           | `TargetResource` | `https://sso.connect.pingidentity.com/sso/sp/initsso?saasid=<app_id>&idpid=<idp_id>`       |

Amazon Quick Suite supports connecting to one IdP per AWS account. The configuration page
in Amazon Quick Suite provides you with test URLs based on your entries, so you can test the
settings before you turn on the feature. To make the process even more seamless,
Amazon Quick Suite provides a parameter (`enable-sso=0`) to temporarily turn off
Amazon Quick Suite initiated IAM federation, in case you need to disable it
temporarily.

## To set up Amazon Quick Suite as a service provider that can

initiate IAM federation for an existing IdP

1. Make sure that you already have IAM federation set up in your IdP, in
   IAM, and Amazon Quick Suite. To test this setup, check if you can share a
   dashboard with another person in your company's domain.
2. Open Amazon Quick Suite, and choose **Manage Amazon Quick Suite**
   from your profile menu at upper right.

To perform this procedure, you need to be a Amazon Quick Suite administrator. If
you aren't, you can't see **Manage Amazon Quick Suite** under
your profile menu. 3. Choose **Single sign-on (IAM federation)** from the
navigation pane. 4. For **Configuration**, **IdP
URL**, enter the URL that your IdP provides to authenticate
users. 5. For **IdP URL**, enter the parameter that your IdP
provides to relay state, for example `RelayState`. The actual
name of the parameter is provided by your IdP. 6. Test signing in:

    * To test signing in with your identity provider, use the custom URL
     provided in **Test starting with your IdP**. You
     should arrive at the start page for Amazon Quick Suite, for example
     https://quicksight.aws.amazon.com/sn/start.
    * To test signing in with Amazon Quick Suite first, use the custom URL
     provided in **Test the end-to-end
     experience**. The `enable-sso` parameter is
     appended to the URL. If `enable-sso=1`, IAM federation
     attempts to authenticate.

7. Choose **Save** to keep your settings.

## To enable service provider–initiated IAM

federation IdP

1. Make sure your IAM federation settings are configured and tested. If
   you're not sure about the configuration, test the connection by using the
   URLs from the previous procedure.
2. Open Amazon Quick Suite, and choose **Manage Amazon Quick Suite**
   from your profile menu.
3. Choose **Single sign-on (IAM federation)** from the
   navigation pane.
4. For **Status**, choose **ON**.
5. Verify that it's working by disconnecting from your IdP and opening
   Amazon Quick Suite.

## To disable service provider initiated IAM

federation

1. Open Amazon Quick Suite, and choose **Manage Amazon Quick Suite**
   from your profile menu.
2. Choose **Single sign-on (IAM federation)** from the
   navigation pane.
3. For **Status**, choose **OFF**.
