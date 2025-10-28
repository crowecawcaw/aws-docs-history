# View a SAML response in your

browser

The following procedures describe how to view the SAML response from your service provider
from in your browser when troubleshooting a SAML 2.0–related issue.

For all browsers, go to the page where you can reproduce the issue. Then follow the steps
for the appropriate browser:

###### Topics

- [Google Chrome](#chrome "#chrome")
- [Mozilla Firefox](#firefox "#firefox")
- [Apple Safari](#safari "#safari")
- [What to do with the Base64-encoded SAML response](#whatnext "#whatnext")

## Google Chrome

###### To view a SAML response in Chrome

These steps were tested using version 106.0.5249.103 (Official Build) (arm64) of Google
Chrome. If you use another version, you might need to adapt the steps accordingly.

1. Press **F12** to start the **Developer Tools**
   console.
2. Select the **Network** tab, and then select **Preserve
   log** in the upper left of the **Developer Tools**
   window.
3. Reproduce the issue.
4. (Optional) If the **Method** column is not visible in the
   **Developer Tools**
   **Network** log pane, right-click on any column label and choose
   **Method** to add the column.
5. Look for a **SAML Post** in the **Developer Tools**
   **Network** log pane. Select that row, and then view the
   **Payload** tab at the top. Look for the
   **SAMLResponse** element that contains the encoded request. The
   associated value is the Base64-encoded response.

## Mozilla Firefox

###### To view a SAML response in Firefox

This procedure was tested on version 105.0.3 (64-bit) of Mozilla Firefox. If you use
another version, you might need to adapt the steps accordingly.

1. Press **F12** to start the **Web Developer Tools**
   console.
2. Select the **Network** tab.
3. In the upper right of the **Web Developer Tools** window, choose
   options (the small gear icon). Select **Persist logs**.
4. Reproduce the issue.
5. (Optional) If the **Method** column is not visible in the
   **Web Developer Tools**
   **Network** log pane, right-click on any column label and choose
   **Method** to add the column.
6. Look for a **POST**
   **SAML** in the table. Select that row, and then view the
   **Request** tab and find the **SAMLResponse** element.
   The associated value is the Base64-encoded response.

## Apple Safari

###### To view a SAML response in Safari

These steps were tested using version 16.0 (17614.1.25.9.10, 17614) of Apple Safari. If
you use another version, you might need to adapt the steps accordingly.

1. Enable Web Inspector in Safari. Open the **Preferences** window,
   select the **Advanced** tab, and then select **Show Develop menu
   in the menu bar**.
2. Now you can open Web Inspector. Choose **Develop** in the menu bar,
   then select **Show Web Inspector**.
3. Select the **Network** tab.
4. In the upper left of the **Web Inspector** window, choose options
   (the small circle icon containing three horizontal lines). Select **Preserve
   Log**.
5. (Optional) If the **Method** column is not visible in the
   **Web Inspector**
   **Network** log pane, right-click on any column label and choose
   **Method** to add the column.
6. Reproduce the issue.
7. Look for a **POST**
   **SAML** in the table. Select that row, and then view the Headers
   tab.
8. Look for the **SAMLResponse** element that contains the encoded
   request. Scroll down to find `Request Data` with the name
   `SAMLResponse`. The associated value is the Base64-encoded response.

## What to do with the Base64-encoded SAML response

Once you find the Base64-encoded SAML response element in your browser, copy it and use
your favorite Base-64 decoding tool to extract the XML tagged response.

###### Security tip

Because the SAML response data that you are viewing might contain sensitive security
data, we recommend that you do not use an _online_ base64 decoder.
Instead use a tool installed on your local computer that does not send your SAML data over
the network.

**Built-in option for Windows systems (PowerShell):**

```
`PS C:\>` [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("`base64encodedtext`"))
```

**Built-in option for MacOS and Linux systems:**

```
`$` echo "`base64encodedtext`" | base64 --decode
```

###### Review the values in the decoded file

Review the values in the decoded SAML response file.

- Verify that the value for the saml:NameID attribute matches the username for the
  authenticated user.
- Review the value for https://aws.amazon.com/SAML/Attributes/Role. The ARN and SAML
  provider are case sensitive, and the [ARN](reference-arns.md "reference-arns.md") must match the resource in
  your account.
- Review the value for https://aws.amazon.com/SAML/Attributes/RoleSessionName. The value
  must match the value in the [claim
  rule](id_roles_providers_create_saml_relying-party.md "id_roles_providers_create_saml_relying-party.md").
- If you configure the attribute value for an email address or an account name, then
  make sure that the values are correct. The values must correspond to the email address or
  account name of the authenticated user.

###### Check for errors and confirm the configuration

Check whether the values contain errors, and confirm that the following configurations
are correct.

- The claim rules meet the required elements and all ARNs are correct. For more
  information, see [Configure your SAML 2.0 IdP with
  relying party trust and adding claims](id_roles_providers_create_saml_relying-party.md "id_roles_providers_create_saml_relying-party.md").
- You uploaded the latest metadata file from your IdP into AWS in your SAML provider.
  For more information, see [Enabling SAML 2.0 federated principals
  to access the AWS Management Console](id_roles_providers_enable-console-saml.md "id_roles_providers_enable-console-saml.md").
- You correctly configured the IAM role's trust policy. For more information, see
  [Methods to assume a role](id_roles_manage-assume.md "id_roles_manage-assume.md").
