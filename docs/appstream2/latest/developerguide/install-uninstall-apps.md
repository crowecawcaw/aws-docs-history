# Install or uninstall license included applications

###### Install or uninstall license included applications

To install or uninstall one or more license included application(s) on your image,
follow these steps.

1. Complete one of the following options:
   - Launch an image Builder and configure license included applications.
     For more information, see [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md "tutorial-image-builder-create.md").
   - Manage license included applications on your image builder. For
     more information, see [Attribute-Based Application Entitlements
     Using a Third-Party SAML 2.0 Identity Provider](application-entitlements-saml.md "application-entitlements-saml.md").

2. When you have an image created with one or more license included applications,
   you can use this image to create fleets. Users connecting to this fleet can
   access these applications.

###### Important

All the users streaming through a fleet powered by an image with one
or more licensed apps will incur billing for these apps monthly,
regardless of usage. The application entitlement feature does not
restrict access for specific users.
If you encounter failures during license included app installation or uninstallation,
you will see a failure status on your Image Builder's details page. To troubleshoot
these issues, we recommend connecting to your Image Builder and enabling verbose
logging. For more information see [How to enable Microsoft 365 Apps for enterprise logging](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/diagnostic-logs/how-to-enable-office-365-proplus-uls-logging "https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/diagnostic-logs/how-to-enable-office-365-proplus-uls-logging"). If the problem
persists after reviewing the logs and troubleshooting, contact AWS Support for
help.
