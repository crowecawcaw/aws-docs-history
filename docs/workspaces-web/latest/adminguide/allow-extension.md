# Managing the single sign-on extension in Amazon WorkSpaces Secure Browser

You can enable an extension for your end users to have a better portal sign-on experience.
For example, if you use Okta as your portal’s SAML 2.0 identity provider (IdP), and you also use
it as the IdP for the websites you want users to visit during a session, you can pass the Okta
sign-in cookie to the session with the extension. Afterwards, when users visit a website that
requires the Okta domain cookie, they can access the website without having to sign in during the
session.

The extension is supported in Chrome and Firefox browsers. The extension enables cookie
synchronization for the allowed domains from the users sign-in to the session. The extension does
not require the user to sign in, and it works behind the scenes to enable cookie synchronization
without requiring the user to take any actions after installation. No data is stored by the
extension.

By default, extensions are not enabled in Chrome in Incognito windows or Firefox Private
Browsing windows. Users can enable them manually. For more information about Chrome, see [Extensions in Incognito
mode](https://support.google.com/chrome/a/answer/13130396?hl=en "https://support.google.com/chrome/a/answer/13130396?hl=en"). For more information about Firefox, see [Extensions in Private
Browsing](https://support.mozilla.org/en-US/kb/extensions-private-browsing "https://support.mozilla.org/en-US/kb/extensions-private-browsing").

Users are prompted to install the extension when they sign into a portal. For details about the user experience with the extension, see [Single sign-on extension for Amazon WorkSpaces Secure Browser](extension.md "extension.md").

###### Topics

- [Identifying domains for the single sign-on extension in Amazon WorkSpaces Secure Browser](identify-domains.md "identify-domains.md")
- [Adding the single sign-on extension to a new web portal in Amazon WorkSpaces Secure Browser](extension-new.md "extension-new.md")
- [Adding the single sign-on extension to an existing web portal in Amazon WorkSpaces Secure Browser](extension-existing.md "extension-existing.md")
- [Editing or removing the single sign-on extension in Amazon WorkSpaces Secure Browser](remove-extension.md "remove-extension.md")
