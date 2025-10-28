# Configuring your identity provider on

Amazon WorkSpaces Secure Browser

Complete the following steps to configure your identity provider:

1. On the **Configure identity provider page** of the creation wizard,
   choose **Standard**.
2. Choose **Continue with Standard IdP**.
3. Download the SP metadata file, and keep the tab open for individual metadata
   values.
   - If the SP metadata file is available, choose **Download metadata
     file** to download the service provider (SP) metadata document, and
     upload the service provider metadata file to your IdP in the next step. Without
     this, users won't be able to sign in.
   - If your provider doesn't upload SP metadata files, manually enter the
     metadata values.

4. Under **Choose SAML sign-in type**, choose between
   **SP-initiated and IdP-initiated SAML assertions**, or
   **SP-initiated SAML assertions only**.
   - **SP-initiated and IdP-initiated SAML assertions** allow
     your portal to support both types of sign-in flows. Portals that support
     IdP-initiated flows allow you to present SAML assertions to the service identity
     federation endpoint without requiring users to launch a session by visiting the
     portal URL.
     - Choose this to allow the portal to accept unsolicited IdP-initiated SAML
       assertions.
     - This option requires a **default Relay State** to be
       configured in your SAML 2.0 Identity Provider. The Relay state parameter for
       your portal is in the console under **IdP initiated SAML sign
       in**, or you can copy it from the SP metadata file under
       `<md:IdPInitRelayState>`.
     - Note
       - The following is the format of the relay state:
         `redirect_uri=https%3A%2F%2Fportal-id.workspaces-web.com%2Fsso&response_type=code&client_id=1example23456789&identity_provider=Example-Identity-Provider`.
       - If you copy and paste the value from the SP metadata file, make sure
         that you change `&amp;` to `&`.
         `&amp;` is an XML escape character.

   - Choose **SP-initiated SAML assertions only** for the portal
     to only support SP-initiated sign in flows. This option will reject unsolicited
     SAML assertions from IdP-initiated sign-in flows.

###### Note

Some third-party IdPs allow you to create a custom SAML application that can deliver
IdP-initiated authentication experiences leveraging SP-initiated flows. For example, see
[Add an Okta bookmark application](https://help.okta.com/oag/en-us/content/topics/access-gateway/add-app-saml-pass-thru-add-bookmark.htm "https://help.okta.com/oag/en-us/content/topics/access-gateway/add-app-saml-pass-thru-add-bookmark.htm"). 5. Choose whether you want to enable **Sign SAML requests to this
provider**. SP-initiated authentication allows your IdP to validate that the
authentication request is coming from the portal, which prevents accepting other third-party
requests.

    1. Download the signing certificate and upload it to your IdP. The same signing
     certificate can be used for single logout.
    2. Enable signed request in your IdP. The name might be different, depending on the
     IdP.


    ###### Note

    RSA-SHA256 is the only request and default request signing algorithm
     supported.

6. Choose whether you want to enable **Require encrypted SAML
   assertions**. This allows you to encrypt the SAML assertion that comes from your
   IdP. It can prevent data from being intercepted in SAML assertions between the IdP and
   WorkSpaces Secure Browser.

###### Note

The encryption certificate is not available at this step. It will be created
after your portal launches. After you launch the portal, download the encryption
certificate and upload it to your IdP. Then, enable assertion encryption in your
IdP (the name might be different, depending on the IdP. 7. Choose whether you want to enable **Single Logout**. Single logout
allows your end users to sign out of both their IdP and WorkSpaces Secure Browser session with a single
action.

    1. Download the signing certificate from WorkSpaces Secure Browser and upload it onto your IdP. This is the
     same signing certificate used for **Request Signing** in the previous
     step.
    2. Using **Single Logout** requires you to configure a **Single
     Logout URL** in your SAML 2.0 identity provider. You can find the
     **Single Logout URL** for your portal in the console under
     **Service provider (SP) details - Show individual metadata values**, or
     from the SP metadata file under `<md:SingleLogoutService>` .
    3. Enable **Single Logout** in your IdP. The name might be different,
     depending on the IdP.
