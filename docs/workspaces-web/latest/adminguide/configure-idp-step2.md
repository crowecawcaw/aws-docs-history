# Configuring your IdP on your own

IdP

To configure your IdP on your own IdP, follow these steps.

1. Open a new tab in your browser.
2. Add your portal metadata to your SAML IdP.

Either upload the SP metadata document that you downloaded in the previous step to your
IdP, or copy and paste the metadata values into the correct fields in your IdP. Some
providers do not allow file upload.

The details of this process can vary between providers. Find your provider's
documentation in [Guidance for using specific IdPs with Amazon WorkSpaces Secure Browser](idp-guidance.md "idp-guidance.md") for help on how to add the portal details to
your IdP configuration. 3. Confirm the **NameID** for your SAML assertion.

Make sure your SAML IdP populates **NameID** in the SAML assertion
with the user email field. **NameID** and user email are used for uniquely
identifying your SAML federated user with the portal. Use the persistent SAML Name ID
format. 4. Optional: Configure the **Relay State** for IdP-initiated
authentication.

If you chose **Accept SP-initiated and IdP-initiated SAML assertions**
in the previous step, follow steps in step 2 of [Configuring your identity provider on
Amazon WorkSpaces Secure Browser](configure-idp-step1.md "configure-idp-step1.md") to set
the default **Relay State** for your IdP application. 5. Optional: Configure **Request signing**. If you chose **Sign
SAML requests to this provider** in the previous step, follow steps in step 3 of
[Configuring your identity provider on
Amazon WorkSpaces Secure Browser](configure-idp-step1.md "configure-idp-step1.md") to upload the signing certificate onto your IdP and
enable request signing. Some IdPs such as Okta might require your
**NameID** to belong to the “persistent” type to use **Request
signing**. Make sure to confirm your **NameID** for your SAML
assertion by following the steps above. 6. Optional: Configure **Assertion encryption**. If you chose
**Require encrypted SAML assertions from this provider**, wait until
portal creation is complete, then follow step 4 in "Upload metadata" below to upload the
encryption certificate onto your IdP and enable assertion encryption. 7. Optional: Configure **Single Logout**. If you chose **Single
Logout**, follow the steps in step 5 of [Configuring your identity provider on
Amazon WorkSpaces Secure Browser](configure-idp-step1.md "configure-idp-step1.md") to
upload the signing certificate onto your IdP, fill in **Single Logout
URL**, and enable **Single Logout**. 8. Grant access to your users in your IdP to use WorkSpaces Secure Browser. 9. Download a metadata exchange file from your IdP. You will upload this metadata to WorkSpaces Secure Browser
in the next step.
