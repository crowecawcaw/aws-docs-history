# Revoke an AWS Certificate Manager public certificate

You can revoke an AWS Certificate Manager exportable public certificates using the ACM console, AWS CLI, or API
action.

###### Warning

After a certificate is revoked, you cannot reuse the certificate.
Revoking a certificate is permanent.

You may need to revoke a certificate to comply with your organization’s policies or
mitigate key compromise. A reason is required when revoking a certificate. The following
reasons can be used:

- Unspecified
- Affiliation changed
- Superseded
- Cessation of operation
  To learn more see, [Amazon Trust Services
  Certificate Subscriber Agreement](https://www.amazontrust.com/repository/sa-1.3.pdf "https://www.amazontrust.com/repository/sa-1.3.pdf") and [Amazon Trust Service](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/").

AWS provides two services to check certificate revocations: Online Certificate
Status Protocol (OCSP) and certificate revocation list. With OCSP, the client queries an
authoritative revocation database that returns a status in real-time. OCSP depends on
validation information embedded in certificates.

## Considerations

The following are considerations before revoking a certificate:

- You can only revoke certificates that were previously exported.
- You cannot revoke [non-exportable public certificates](acm-exportable-certificates.md "acm-exportable-certificates.md"). If you no longer need these
  certificate, you should [delete them](gs-acm-delete.md "gs-acm-delete.md")
  instead.
- If you no longer need the certificate, you should [delete certificates](gs-acm-delete.md "gs-acm-delete.md") instead of revoking
  certificates.
- The certificate revocation process is global. All valid certificates you
  choose to revoke will be revoked along with their associated ARNs.
- Certificate revocation is permanent. You can't retrieve revoked
  certificates to reuse.
- It can take up to 24 hours for certificate revocation to take
  effect.

## Revoke a certificate (console)

The following procedure walks you through how you can revoke an ACM public or
private certificate.

1. Sign in to the AWS Management Console and open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/ "https://console.aws.amazon.com/acm/").
2. Choose **List certificates** and select the checkbox of
   the certificate you want to revoke.
   1. Alternatively, you can select the certificate. In the certificate
      detail page, select **Revoke**.

3. Choose **More actions** and then choose
   **Revoke**.
4. A dialog box appears where you must provide a revoke reason, enter
   `revoke`, and then choose
   **Revoke**.

## Revoke a certificate (AWS CLI)

Use the [`revoke-certificate`](../../../cli/latest/reference/acm-pca/revoke-certificate.md "../../../cli/latest/reference/acm-pca/revoke-certificate.md") AWS CLI command or [`RevokeCertificate`](../APIReference/API_RevokeCertificate.md "../APIReference/API_RevokeCertificate.md") API action to revoke an ACM public
or private certificate. You can retrieve the certificate's ARN by calling the [`list-certificates`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html") command.

```
$ aws acm revoke-certificate \
    --certificate-arn arn:aws:acm:`us-east-1`:`111122223333`:certificate/`12345678-1234-1234-1234` \
    --revocation-reason "UNSPECIFIED"
```

###### Warning

After a certificate is revoked, you cannot reuse the certificate.
Revoking a certificate is permanent.

The following would be the output for the `revoke-certificate`
command.

```
arn:aws:acm:`us-east-1`:`111122223333`:certificate/`12345678-1234-1234-1234`
```
