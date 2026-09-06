

# Use your own ACM certificate for backend mutual TLS in API Gateway
<a name="rest-api-acm-client-certificates"></a>

You can configure API Gateway to present your own CA-signed certificate to backend services. Import your certificate into AWS Certificate Manager (ACM), or issue one through AWS Private Certificate Authority. Then, link the ACM certificate ARN to your API stage.

## Prerequisites
<a name="rest-api-acm-client-certificates-prereqs"></a>

Before you configure an ACM client certificate, you must have the following:
+ AWS Certificate Manager access in the same Region as your API.
+ IAM permissions: `acm:ImportCertificate` and `acm:DescribeCertificate` (for Option A import), or `acm:RequestCertificate` (for Option B), or `acm-pca:IssueCertificate`, `acm-pca:GetCertificate`, and `acm:ImportCertificate` (for Option C).
+ A REST API deployed to a stage.

## Step 1: Import a certificate, or issue one through AWS Private Certificate Authority
<a name="rest-api-acm-client-certificates-import"></a>

You can either import a certificate from your existing PKI or issue a new certificate through AWS Private Certificate Authority. Both paths produce an ACM certificate ARN that you use in the following step.

**Note**  
ACM public certificates are not supported for backend client authentication. Effective June 11, 2025, AWS Certificate Manager no longer issues public certificates with the `clientAuth` extended key usage (EKU). This feature requires that EKU, so use a certificate that you import into ACM, or one issued through AWS Private Certificate Authority.

**Note**  
Create the ACM certificate in the same AWS Region as the REST API that will use it. ACM certificates are Regional resources, so the certificate must exist in your API's Region.

### Option A: Import from your existing PKI
<a name="rest-api-acm-client-certificates-import-pki"></a>

To import a client certificate and its private key into ACM, run the following command. For more information, see [Importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *AWS Certificate Manager User Guide*.

```
aws acm import-certificate \
  --certificate fileb://{{client-cert.pem}} \
  --private-key fileb://{{private-key.pem}} \
  --certificate-chain fileb://{{ca-chain.pem}} \
  --region {{region}}
```

The command returns the ACM certificate ARN. Record this value for the following step.

### Option B: Request a certificate through AWS Private Certificate Authority (ACM-managed)
<a name="rest-api-acm-client-certificates-import-pca"></a>

To request a private certificate that ACM manages and can auto-renew, run the following command. For more information, see [Requesting a private certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html) in the *AWS Certificate Manager User Guide*.

```
aws acm request-certificate \
  --domain-name {{www.example.com}} \
  --certificate-authority-arn arn:aws:acm-pca:{{us-east-1}}:{{123456789012}}:certificate-authority/{{12345678-1234-1234-1234-123456789012}} \
  --region {{region}}
```

The command returns the ACM certificate ARN. Record this value for the following step.

### Option C: Issue through AWS Private Certificate Authority and import into ACM
<a name="rest-api-acm-client-certificates-import-pca-manual"></a>

If you need direct control over certificate parameters (such as custom extensions or signing algorithms), you can issue a certificate through AWS Private Certificate Authority and then import it into ACM. Certificates imported this way are not auto-renewed by ACM. Ensure the certificate meets the [certificate requirements](#rest-api-acm-client-certificates-requirements). For more information about issuing private certificates, see [Issuing a private end-entity certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PcaIssueCert.html) in the *AWS Private Certificate Authority User Guide*.

```
aws acm-pca issue-certificate \
  --certificate-authority-arn arn:aws:acm-pca:{{us-east-1}}:{{123456789012}}:certificate-authority/{{12345678-1234-1234-1234-123456789012}} \
  --csr fileb://{{csr.pem}} \
  --signing-algorithm SHA256WITHRSA \
  --validity Value=365,Type=DAYS
```

**Retrieve and import the certificate**  
The `issue-certificate` command returns a AWS Private Certificate Authority certificate ARN, not an ACM ARN. To use this certificate with API Gateway, retrieve it using `aws acm-pca get-certificate` and then import it into ACM using `aws acm import-certificate`. The import produces the ACM certificate ARN that you use in the following step. When you run `aws acm import-certificate`, set `--region` to your API's Region so the ACM certificate is created there.

## Step 2: Configure an API stage to use the ACM certificate
<a name="rest-api-acm-client-certificates-configure"></a>

After you have an ACM certificate ARN, set up your API stage to present the certificate to your backend.

### To configure a stage (console)
<a name="rest-api-acm-client-certificates-configure-console"></a>

1. Open the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose your REST API.

1. Choose **Stages**.

1. In the **Stage details** section, choose **Edit**.

1. For **Client certificate**, select your ACM certificate from the dropdown list.

1. Choose **Save changes**.

### To configure a stage (AWS CLI)
<a name="rest-api-acm-client-certificates-configure-cli"></a>

Run the following command:

```
aws apigateway update-stage \
  --rest-api-id {{abc123}} \
  --stage-name {{prod}} \
  --patch-operations op='replace',path=/clientCertificateId,value={{arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012}}
```

**Note**  
API Gateway uses the same `clientCertificateId` field for both ACM and API Gateway-generated certificates. When you provide an ACM certificate ARN, API Gateway automatically detects the format and uses the ACM-managed workflow.

## Step 3: Verify the configuration
<a name="rest-api-acm-client-certificates-verify"></a>

To verify that API Gateway sends the certificate to your backend, complete the following steps:

**Backend must request a client certificate**  
Your backend must be configured to request a client certificate during the TLS handshake. If the backend does not request one, API Gateway does not present the certificate.

1. Invoke your API endpoint.

1. Check that your backend gets the client certificate during the TLS handshake.

1. Check that your backend accepts the certificate and returns a successful response.

If the backend rejects the certificate, verify that the certificate chain can be validated against the backend's trust store.

## Certificate requirements
<a name="rest-api-acm-client-certificates-requirements"></a>

The leaf certificate that you configure must meet the following requirements.


**ACM client certificate requirements**  

| Requirement | Description | 
| --- | --- | 
| Maximum chain length | 5 certificates | 
| Validity | The certificate must not be expired or yet to be valid when you configure it | 
| Region | ACM certificate must be in the same Region as the API | 
| Account | ACM certificate must be in the same account as the API | 
| Extended Key Usage (EKU) | If present, must include clientAuth. If absent, the certificate is accepted. | 
| Key Usage (KU) | If present, must include digitalSignature or keyAgreement. If absent, the certificate is accepted. | 
| Key algorithm | Must be one of: RSA 2048, RSA 3072, RSA 4096, ECDSA P-256 (EC\_prime256v1), ECDSA P-384 (EC\_secp384r1), or ECDSA P-521 (EC\_secp521r1) | 
| ACM certificate status | Must be ISSUED | 

**Note**  
API Gateway does not validate the chain of trust between the leaf and intermediate certificates. API Gateway also does not validate certificate intent or basic constraints (such as `CA:TRUE`) on intermediate certificates. Your backend performs these validations during the TLS handshake.

## Certificate renewal and propagation
<a name="rest-api-acm-client-certificates-renewal"></a>

When a certificate changes in ACM, API Gateway detects the update and propagates the new certificate automatically. You do not need to redeploy your stage, and your API experiences no downtime during rotation.

Certificate propagation is eventually consistent. During the update, your backend might receive either the old or the new certificate until propagation completes.

How the certificate gets renewed depends on how it was issued:
+ **Certificates issued through AWS Private Certificate Authority (ACM-managed) (Option B)** – ACM auto-renews these certificates. API Gateway detects the renewal and updates automatically.
+ **Certificates issued by AWS Private Certificate Authority and imported (Option C)** – ACM does not auto-renew imported certificates. You must reimport the renewed certificate. After you reimport the certificate, API Gateway detects the change and updates automatically.
+ **Imported certificates from your PKI (Option A)** – You must [reimport](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) the renewed certificate into ACM. After you reimport the certificate, API Gateway detects the change and updates automatically.

ACM sends certificate expiration notifications through [Amazon EventBridge](https://docs.aws.amazon.com/acm/latest/userguide/supported-events.html). You can use these notifications to set up alarms before a certificate expires.

## ACM certificate behavior and limitations
<a name="rest-api-acm-client-certificates-important-notes"></a>

Viewing the configured certificate  
ACM certificates do not appear in the `GetClientCertificate` or `GetClientCertificates` API responses. To view the ACM certificate ARN configured on a stage, use [GetStage](https://docs.aws.amazon.com/apigateway/latest/api/API_GetStage.html). To view certificate details, use the ACM APIs [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html) and [GetCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetCertificate.html).

Reuse across stages  
You can attach the same ACM certificate to multiple stages. Each stage independently references the certificate by its ARN.

Client certificate APIs do not apply to ACM certificates  
ACM certificates are not API Gateway-managed resources. The `GetClientCertificate`, `UpdateClientCertificate`, and `DeleteClientCertificate` APIs return a `NotFoundException` when called with an ACM certificate ARN. Use ACM APIs to manage the certificate lifecycle.

Automatic certificate association cleanup  
When you remove an ACM certificate from a stage, update a stage to use a different certificate, or delete a stage or REST API, API Gateway cleans up the certificate association automatically. No manual action is required.

Deleting the ACM certificate  
ACM does not allow you to delete a certificate while API Gateway has an active association with it. To delete the certificate from ACM, first remove it from all stages that reference it.