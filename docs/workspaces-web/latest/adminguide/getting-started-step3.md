# Distributing your web portal in Amazon WorkSpaces Secure Browser

When you are ready for your users to begin using WorkSpaces Secure Browser, you choose from the following
options to distribute the portal:

- Add your portal to your SAML application gateway to enable users to launch a session from
  their IdP directly. You can do this through the IdP-initiated sign-in flow with your SAML
  2.0 compliant IdP. For more information, see **SP-initiated and IdP-initiated SAML
  assertions** in [Configuring the standard authentication type for Amazon WorkSpaces Secure Browser](configure-standard.md "configure-standard.md"). Alternatively, you can
  create a custom SAML application that can deliver IdP-initiated authentication experiences
  by using SP-initiated flows. For more information, see [Create a
  Bookmark App integration](https://help.okta.com/en-us/Content/Topics/Apps/apps-create-bookmark.htm "https://help.okta.com/en-us/Content/Topics/Apps/apps-create-bookmark.htm").
- Add the portal URL to a website that you own, and use a browser redirect to direct users
  to the web portal.
- Email the portal URL to your users, or push down to a device you manage as a browser home
  page or bookmark.
