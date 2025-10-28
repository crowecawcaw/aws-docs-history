# Finishing IdP configuration on Amazon WorkSpaces Secure Browser

To finish IdP configuration on WorkSpaces Secure Browser follow these steps.

1. Return to the WorkSpaces Secure Browserconsole. On the **Configure identity provider page**
   of the creation wizard, under **IdP metadata**, either upload a metadata
   file, or enter a metadata URL from your IdP. The portal uses this metadata from your IdP to
   establish trust.
2. To upload a metadata file, under **IdP metadata document**, choose
   **Choose file**. Upload the XML-formatted metadata file from your IdP that
   you downloaded in the previous step.
3. To use a metadata URL, go to your IdP that you set up in the previous step and obtain
   its **Metadata URL**. Go back to the WorkSpaces Secure Browser console, and under **IdP
   metadata URL**, enter the metadata url that you obtained from your IdP.
4. When you are done, choose **Next**.
5. For portals where you have enabled the **Require encrypted SAML assertions from
   this provider** option, you need to download the encryption certificate from the
   portal IdP details section and upload it onto your IdP. Then, you can enable the option
   there.

###### Note

WorkSpaces Secure Browser requires the subject or NameID to be mapped and set in the SAML assertion within
your IdP's settings. Your IdP can create these mappings automatically. If these mappings
aren't configured correctly, your users can't sign in to the web portal and start a
session.

WorkSpaces Secure Browser requires the following claims to be present in the SAML response. You can find
`<Your SP Entity ID>` and `<Your SP ACS
 URL>` from your portal’s service provider details or metadata document,
either through the console or the CLI.

    * An `AudienceRestriction` claim with an `Audience` value that
     sets your SP Entity ID as the target of the response. Example:



    ```
    <saml:AudienceRestriction>
        <saml:Audience><Your SP Entity ID></saml:Audience>
    </saml:AudienceRestriction>
    ```
    * A `Response` claim with an `InResponseTo` value of the
     original SAML request ID. Example:



    ```
    <samlp:Response ... InResponseTo="<originalSAMLrequestId>">
    ```
    * A `SubjectConfirmationData` claim with a `Recipient` value of
     your SP ACS URL, and an `InResponseTo` value that matches the original SAML
     request ID. Example:



    ```
    <saml:SubjectConfirmation>
        <saml:SubjectConfirmationData ...
            Recipient="<Your SP ACS URL>"
            InResponseTo="<originalSAMLrequestId>"
            />
    </saml:SubjectConfirmation>
    ```WorkSpaces Secure Browser validates your request parameters and SAML assertions. For IdP-initiated SAML

assertions, the details of your request must be formatted as a `RelayState`
parameter in the body of an HTTP POST request. The request body must also contain your SAML
assertion as a `SAMLResponse` parameter. Both of these should be present if you
have followed the previous step.

The following is an example `POST` body for an IdP-initiated SAML
provider.

```
SAMLResponse=<Base64-encoded SAML assertion>&RelayState=<RelayState>
```
