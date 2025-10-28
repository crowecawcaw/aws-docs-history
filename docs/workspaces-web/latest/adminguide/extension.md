# Single sign-on extension for Amazon WorkSpaces Secure Browser

Amazon WorkSpaces Secure Browser offers an extension for single sign-on with Chrome and Firefox browsers on
desktop computers. If your administrator has enabled the extension, the web portal will ask
you to install the extension when you sign in.

Amazon WorkSpaces Secure Browser built the extension to enable single sign-on to websites during your session.
For example, if you sign into your web portal using a SAML 2.0 identity provider (such as Okta
or Ping), and you visit a website during your session that uses the same identity provider,
the extension can make it easier to access the website by removing additional sign-in
prompts.

You aren’t required to install the extension to access your web portal, but it can improve
your experience by reducing the number of times you are asked to enter your username and
password.

When you sign in, the extension locates the cookies your administrator listed for your
session. All of the data that the extension locates is encrypted at rest and during transit.
None of this data is stored in your local browser. When you end your session, all of your
session data (such as open tabs, files downloaded, and cookies delivered to or created during
the session) is deleted.

###### Topics

- [Single sign-on extension compatibility for Amazon WorkSpaces Secure Browser](extension-compatibility.md "extension-compatibility.md")
- [Installing the single sign-on extension for Amazon WorkSpaces Secure Browser](extension-install.md "extension-install.md")
- [Troubleshooting the single sign-on extension for Amazon WorkSpaces Secure Browser](extension-troubleshooting.md "extension-troubleshooting.md")
