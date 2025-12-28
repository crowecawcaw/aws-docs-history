# Troubleshooting

This section describes common issues and resolutions when integrating AWS-managed
applications.

## Application launch

failures

**Symptoms**

Applications fail to launch, display error messages, or the iframe remains blank.

**Possible causes and solutions**

- CCP not initialized:
  - Ensure the CCP is fully initialized before launching applications.

- Missing AppManager plugin:
  - Verify that the AppManager plugin is properly configured during
    CCP initialization.
  - ```
    connect.core.initCCP(container, {
        ccpUrl: instanceUrl,
        plugins: [AppManagerPlugin], // Required
    });
    ```

  ```

  ```

- Security Profile permissions:
  - Confirm the user has necessary Security Profile permissions to
    access the applications.

- Cross-origin issues:
  - Verify that your domain is properly [allowlisted](../../../connect/latest/adminguide/app-integration.md "../../../connect/latest/adminguide/app-integration.md") in Amazon Connect.
  - Check the browser console for Cross-Origin Resource Sharing (CORS)
    errors.
  - Ensure third-party cookies are not blocked in the browser
    settings.

- Iframe configuration:
  - Verify that iframes have the necessary permissions in `allow`
    and `sandbox` attributes.
  - Allow AppManager to configure the iframe. Do not manually set the `src` attribute.

- Content Security Policy (CSP):
  - Ensure CSP allows communication with Amazon Connect domains either
    via response headers or meta tags in the HTML head.

## Application not

appearing in catalog

**Symptoms**

The `getAppCatalog()` method returns an empty array or does not include
expected applications.

**Possible causes and solutions**

- Applications not enabled: Verify that the required applications are
  enabled in the Amazon Connect instance.
- Security Profile permissions: Confirm that the user has necessary Security
  Profile permissions to access the applications.
