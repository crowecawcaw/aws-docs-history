# Configure Jamf Pro for Connector for SCEP

You can use AWS Private CA as an external certificate authority (CA) with the Jamf Pro mobile
device management (MDM) system. This guide provides instructions on how to configure Jamf
Pro after you create a general-purpose connector.

## Configure Jamf Pro for Connector for SCEP

This guide provides instructions on how to configure Jamf Pro for use with Connector for SCEP.
After you successfully configure Jamf Pro and Connector for SCEP, you'll be able to issue AWS Private CA
certificates to your managed devices.

### Jamf Pro

requirements

Your implementation of Jamf Pro must meet the following requirements.

- You must enable the **Enable certificate-based
  authentication** setting in Jamf Pro. You can find details on
  this setting on the Jamf Pro [Security Settings](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Security_Settings.html "https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Security_Settings.html") page in the Jamf Pro documentation.

### Step 1: (Optional -

recommended) Obtain your private CA's fingerprint

A fingerprint is a unique identifier for your private CA that can be used to
verify the identity of your CA when establishing trust with other systems or
applications. Incorporating a certificate authority (CA) fingerprint allows managed
devices to authenticate the CA they are connecting to and request certificates
solely from the anticipated CA. We recommend using a CA fingerprint with Jamf
Pro.

###### To generate a fingerprint for your private CA

1. Obtain the private CA certificate from either AWS Private CA console or by using
   the [GetCertificateAuthorityCertificate](../APIReference/API_GetCertificateAuthorityCertificate.md "../APIReference/API_GetCertificateAuthorityCertificate.md"). Save it as
   `ca.pem` file.
2. Install the [OpenSSL
   Command Line Utilities](https://wiki.openssl.org/index.php/Command_Line_Utilities "https://wiki.openssl.org/index.php/Command_Line_Utilities").
3. In OpenSSL, run the following command to generate the fingerprint:

```
openssl x509 -in ca.pem -sha256 -fingerprint
```

### Step 2: Configure AWS Private CA

as an external CA in Jamf Pro

After you create a connector for SCEP, you must set AWS Private CA as an external
certificate authority (CA) in Jamf Pro. You can set AWS Private CA as a global, external CA.
Alternatively, you can use a Jamf Pro configuration profile to issue different
certificates from AWS Private CA for different use cases, such as issuing certificates to a
subset of devices in your organization. Guidance on implementing Jamf Pro
configuration profiles is beyond the scope of this document.

###### To configure AWS Private CA as an external certificate authority (CA) in Jamf

Pro

1. In the Jamf Pro console, go to the **PKI certificates
   settings** page by going to **Settings** >
   **Global** > **PKI
   certificates**.
2. Select the **Management Certificate Template**
   tab.
3. Select **External CA**.
4. Select **Edit**.
5. (Optional) Select **Enable Jamf Pro as SCEP Proxy for
   configuration profiles**. You can use Jamf Pro configuration
   profiles to issue different certificates tailored to specific use-cases. For
   guidance on how to use configuration profiles in Jamf Pro, see [Enabling Jamf Pro as SCEP Proxy for Configuration Profiles](https://learn.jamf.com/en-US/bundle/technical-paper-scep-proxy-current/page/Enabling_as_SCEP_Proxy_for_Configuration_Profiles.html#ariaid-title2 "https://learn.jamf.com/en-US/bundle/technical-paper-scep-proxy-current/page/Enabling_as_SCEP_Proxy_for_Configuration_Profiles.html#ariaid-title2") in
   the Jamf Pro documentation.
6. Select **Use a SCEP-enabled external CA for computer and mobile
   device enrollment**.
7. (Optional) Select **Use Jamf Pro as SCEP Proxy for computer and
   mobile device enrollment**. If you experience profile
   installation failures, see [Troubleshoot profile installation failures](#connector-for-scep-jamf-pro-user-initiated-enrollment-troubleshoot "#connector-for-scep-jamf-pro-user-initiated-enrollment-troubleshoot").
8. Copy and paste the Connector for SCEP **public SCEP URL** from the
   connector's details to the **URL** field in Jamf Pro. To
   view a connector's details, choose the connector from the [Connectors for
   SCEP](https://console.aws.amazon.com/pca-connector-scep/home#/connectors "https://console.aws.amazon.com/pca-connector-scep/home#/connectors") list. Alternatively, you can get the URL by calling [GetConnector](../../../pca-connector-scep/latest/APIReference/API_GetConnector.md "../../../pca-connector-scep/latest/APIReference/API_GetConnector.md") and copy the `Endpoint` value from the
   response.
9. (Optional) Enter the name of the instance in the **Name**
   field. For example, you can name it **AWS Private CA**.
10. Select **Static** for the challenge type.
11. Copy a challenge password from your connector, and paste it into the
    **Challenge** field. A connector can have multiple
    challenge passwords. To view your connector's challenge passwords, navigate
    to your connector's details page in the AWS console and select the
    **View password** button. Alternatively, you can get a
    connector's challenge password(s) by calling [GetChallengePassword](../../../pca-connector-scep/latest/APIReference/API_GetChallengePassword.md "../../../pca-connector-scep/latest/APIReference/API_GetChallengePassword.md") and copy a `Password` value
    from the response. For information about using challenge passwords, see
    [Understand Connector for SCEP considerations and limitations](c4scep-considerations-limitations.md "c4scep-considerations-limitations.md").
12. Paste the challenge password into the **Verify
    Challenge** field.
13. Choose a **Key Size**. We recommend a key size of 2048 or
    higher.
14. (Optional) Select **Use as digital signature**. Select
    this for authentication purposes to grant devices secure access to resources
    like Wi-Fi and VPN.
15. (Optional) Select **Use for key encipherment**.
16. (Optional - recommended) Enter a hex string in the
    **Fingerprint** field. We recommend that you add a CA
    fingerprint to allow managed devices to verify the CA, and only request
    certificates from the CA. For instructions on how to generate a fingerprint
    for your private CA, see [Step 1: (Optional -
    recommended) Obtain your private CA's fingerprint](#connector-for-scep-jamf-pro-ca-fingerprint "#connector-for-scep-jamf-pro-ca-fingerprint").
17. Select **Save**.

### Step 3: Set up a

configuration profile signing certificate

To use Jamf Pro with Connector for SCEP, you must provide the signing and CA certificates
for the private CA that's associated with your connector. You can do this by
uploading a profile signing certificate keystore to Jamf Pro that contains both
certificates.

Here are the steps to create a certificate keystore and upload it into Jamf
Pro:

- Generate a certificate signing request (CSR) using your internal
  processes.
- Get the CSR signed by the private CA associated with your
  connector.
- Create a profile signing certificate keystore that contains both the
  profile signing and CA certificates.
- Upload the certificate keystore to Jamf Pro.

By following these steps, you can make sure that your devices can validate and
authenticate the configuration profile signed by your private CA, enabling the use
of Connector for SCEP with Jamf Pro.

1. The following example uses OpenSSL and AWS Certificate Manager, but you can generate a
   certificate signing request using your preferred method.

AWS Certificate Manager console

###### To create a profile signing certificate using the ACM

console

    1. Use ACM to request a private PKI
     certificate. Include the following:




    	* **Type** - Use the same
    	 private CA type that's serving as the SCEP
    	 certificate authority for your MDM system.
    	* In the **Certificate authority
    	 details** section, select the
    	 **Certificate authority** menu
    	 and choose the private CA that serves as the CA
    	 for Jamf Pro.
    	* **Domain name** - Provide a
    	 domain name to be embedded into the certificate.
    	 You can use a fully qualified domain name (FQDN),
    	 such as `www.example.com`, or a bare or
    	 apex domain name such as `example.com`
    	 (which excludes `www.`).
    2. Use ACM to [export the private certificate](../../../acm/latest/userguide/export-private.md "../../../acm/latest/userguide/export-private.md") you created
     in the preceding step. Choose **Export a
     file** for the certificate, certificate
     chain, and encrypted key. Keep the
     **Passphrase** handy because you'll
     need it in the next step.
    3. In a terminal, run the following command in a folder
     containing the exported files to write the PKCS#12
     bundle into the `output.p12` file
     encoded by the passphrase you created in the previous
     step.



    ```
    openssl pkcs12 -export \
      -in "Exported Certificate.txt" \
      -certfile "Certificate Chain.txt" \
      -inkey "Exported Certificate Private Key.txt" \
      -name example \
      -out output.p12 \
      -passin pass:`your-passphrase` \
      -passout pass:`your-passphrase`

    ```

AWS Certificate Manager CLI

###### To create a profile signing certificate using the ACM

CLI

    * The following command shows how to create a
     certificate in ACM, and then export the files as a
     PKCS#12 bundle.



    ```
    PCA=<Enter your Private CA ARN>

    CERTIFICATE=$(aws acm request-certificate \
        --certificate-authority-arn $PCA \
        --domain-name <`any valid domain name, such as test.name`> \

| jq -r '.CertificateArn') while [[$(aws acm describe-certificate \ --certificate-arn $CERTIFICATE \
| jq -r '.Certificate.Status') != "ISSUED"]] do sleep 1; done aws acm export-certificate \ --certificate-arn $CERTIFICATE \ --passphrase password | jq -r '.Certificate' > Certificate.pem aws acm export-certificate \ --certificate-arn $CERTIFICATE \ --passphrase password | jq -r '.CertificateChain' > CertificateChain.pem aws acm export-certificate \ --certificate-arn $CERTIFICATE \ --passphrase password | jq -r '.PrivateKey' > PrivateKey.pem openssl pkcs12 -export \ -in "Certificate.pem" \ -certfile "CertificateChain.pem" \ -inkey "PrivateKey.pem" \ -name `example` \ -out output.p12 \ -passin pass:`passphrase` \ -passout pass:`passphrase` `OpenSSL CLI ###### To create a profile signing certificate using OpenSSL CLI 1. Using OpenSSL, generate a private key by running the following command.` openssl genrsa -out local.key 2048 `2. Generate a certificate signing request (CSR):` openssl req -new -key local.key -sha512 -out local.csr -subj "/CN=MySigningCertificate/O=MyOrganization" -addext keyUsage=critical,digitalSignature,nonRepudiation `3. Using the AWS CLI, issue the signing certificate using the CSR you generated in the previous step. Run the following command, and note the certificate ARN in the response.` aws acm-pca issue-certificate --certificate-authority-arn <SAME CA AS USED ABOVE, SO IT’S TRUSTED> --csr fileb://local.csr --signing-algorithm SHA512WITHRSA --validity Value=365,Type=DAYS `4. Get the signing certificate by running the following command. Specify the certificate ARN from the previous step.` aws acm-pca get-certificate --certificate-authority-arn <SAME CA AS USED ABOVE, SO IT’S TRUSTED> --certificate-arn <ARN OF NEW CERTIFICATE> | jq -r '.Certificate' >local.crt `5. Get the CA certificate by running the following command.` aws acm-pca get-certificate-authority-certificate --certificate-authority-arn <SAME CA AS USED ABOVE, SO IT’S TRUSTED> | jq -r '.Certificate' > ca.crt `6. Using OpenSSL, output the signing certificate keystore in p12 format. Use the CRT files that you generated in steps four and five.` openssl pkcs12 -export -in local.crt -inkey local.key -certfile ca.crt -name "CA Chain" -out local.p12 ```7. When prompted, enter an export password. This password is your keystore password to provide to Jamf Pro. 2. In Jamf Pro, navigate to the **Management Certificate Template** and go to the **External CA** pane. 3. At the bottom of the **External CA** pane, select **Change Signing and CA Certificates**. 4. Follow the onscreen instructions to upload the signing and CA certificates for the external CA. ### Step 4: (Optional) Install certificate during user-initiated enrollment To establish trust between your client devices and your private CA, you must ensure your devices trust the certificates issued by Jamf Pro. You can use Jamf Pro's [User-Initiated Enrollment Settings](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/User-Initiated_Enrollment_Settings.html#:~:text=In%20Jamf%20Pro%2C%20click%20Settings,to%20be%20used%20during%20enrollment. "https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/User-Initiated_Enrollment_Settings.html#:~:text=In%20Jamf%20Pro%2C%20click%20Settings,to%20be%20used%20during%20enrollment.") to automatically install your AWS Private CA's CA certificate on the client devices when they request a certificate during the enrolllment process. ### Troubleshoot profile installation failures If you're experiencing profile installation failures after enabling **Use Jamf Pro as SCEP Proxy for computer and mobile device enrollment**, consult your device logs and try the following.
| Device log error message | Mitigation |
| --- | --- |
|`Profile installation failed. Unable to obtain certificate from SCEP server at "<your-jamf-endpoint>.jamfcloud.com". <MDM-SCEP:15001>`| If you receive this error message while trying to enroll, retry the enrollment. It can take several tries before enrollment succeeds. |
|`Profile installation failed. Unable to obtain certificate from SCEP server at "<your-jamf-endpoint>.jamfcloud.com". <MDM-SCEP:14006>` | Your challenge password might be misconfigured. Verify that the challenge password in Jamf Pro matches your connector’s challenge password. |
