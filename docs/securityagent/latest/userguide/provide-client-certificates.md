

# Provide client certificates for mutual TLS
<a name="provide-client-certificates"></a>

Attach a client certificate to a penetration test so that AWS Security Agent can test endpoints that require mutual Transport Layer Security (mTLS). An mTLS endpoint accepts a connection only when the client presents a certificate during the TLS handshake. Without a client certificate, the endpoint rejects the connection and AWS Security Agent cannot test it.

You store each client certificate and its private key in an AWS Secrets Manager secret in your account, and reference the secret from the penetration test. AWS Security Agent stores only the secret ARN. It reads the certificate and private key from the secret when the penetration test runs. You can attach client certificates in the AWS Security Agent web application or with the AWS CLI or API.

**Note**  
Skip this task if your target endpoints do not require a client certificate.  
The endpoint’s own server certificate is a separate setting. If it is self-signed, or issued by a private or internal certificate authority (CA), you also provide a trust anchor. For more information about trusted CA certificates, see [Provide trusted CA certificates for a penetration test](provide-trusted-ca-certificates.md). An endpoint can need both.

## How client certificates apply
<a name="provide-client-certificates-how"></a>
+  **A certificate applies to a whole host** – You attach a certificate to one or more hosts, and it applies to every path and port on each host. A host can use only one client certificate.
+  **Hosts must be target endpoints** – Each host must belong to a target URL of the penetration test.
+  **Hosts must use HTTPS and a hostname** – An origin uses the form ` [:port](https://host) ` with no path. An IP address is not accepted. AWS Security Agent selects the certificate from the TLS server name, and a connection to an IP address does not carry one.
+  **Certificates are presented only to their hosts** – AWS Security Agent presents a certificate only when it connects to a host that you attached it to. It never presents the certificate to any other host.
+  **Certificate names** – A name can be 1–100 characters: letters, numbers, hyphens, and underscores, starting with a letter or number. Names must be unique within the penetration test.

**Important**  
The certificate must remain valid for the whole run. AWS Security Agent rejects a certificate that has expired or is not yet valid. It also requires the certificate to stay valid for at least 36 hours after the penetration test starts. If you set a maximum task-hours limit lower than 36, the certificate must stay valid for that number of hours instead.

AWS Security Agent reads the secret once, when the penetration test starts. Rotating the secret during a run does not affect that run.

## Store the certificate in Secrets Manager
<a name="provide-client-certificates-secret"></a>

The secret must hold a JSON `SecretString` with the following fields:

```
{
  "certificate": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----",
  "privateKey": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----",
  "privateKeyPassword": "optional"
}
```
+  `certificate` – The PEM-encoded client certificate, followed by any intermediate CA certificates.
+  `privateKey` – The PEM-encoded private key that matches the certificate.
+  `privateKeyPassword` – (Optional) Include it only if the private key is encrypted.

Each PEM value must contain real line breaks: the `BEGIN` and `END` markers each on their own line, and the base64 body on the lines between them. In JSON, write each line break as `\n`.

**Note**  
If you create the secret in the Secrets Manager console, use the **Plaintext** tab and paste the JSON. The **Key/value** tab stores `\n` as two literal characters rather than a line break, and AWS Security Agent then cannot read the certificate. Alternatively, the AWS Security Agent web application can create the secret for you, as described in [Provide a client certificate in the console](#provide-client-certificates-console).

The following AWS CLI command builds the secret from local `client.crt` and `client.key` files, so that the line breaks are encoded correctly. Replace `client.crt` and `client.key` with the paths to your certificate and private key files, and replace `my-agent-space-partner-api-cert` with your secret name. Start the name with your Agent Space name so that the service role can read the secret without an extra grant:

```
aws secretsmanager create-secret \
  --name "my-agent-space-partner-api-cert" \
  --secret-string "$(jq -n --rawfile c client.crt --rawfile k client.key \
      '{certificate: $c, privateKey: $k}')"
```

## Grant access to the secret
<a name="provide-client-certificates-permissions"></a>

The penetration test service role reads the secret when the penetration test runs. It must have the following permissions:
+  `secretsmanager:GetSecretValue` on the secret.
+  `kms:Decrypt` on the secret’s AWS Key Management Service (AWS KMS) key, if the secret is encrypted with a customer managed key. For more information about customer managed keys, see [Customer managed keys for AWS Security Agent](customer-managed-keys.md).

If the secret name starts with your Agent Space name, the service role policy described in [Create the IAM roles for AWS Security Agent](create-iam-role.md) already grants `secretsmanager:GetSecretValue` on it. Otherwise, add a statement for the secret, as in the following example:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:us-east-1:111122223333:secret:partner-api-cert-AbCdEf"
    },
    {
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    }
  ]
}
```

If you let the AWS Security Agent web application create the secret, your own IAM identity must also have `secretsmanager:CreateSecret`. If you encrypt your Agent Space with a customer managed key, the web application encrypts the secret with that key, so your IAM identity also needs `kms:GenerateDataKey` and `kms:Decrypt` on it.

## Provide a client certificate in the console
<a name="provide-client-certificates-console"></a>

Client certificates are part of **Advanced network access** in the penetration test create and edit forms. Add the target URLs first, because you choose the certificate’s hosts from them.

To attach a client certificate, follow these steps:

1. On the **Penetration test details** step, in the **Penetration testing scope** section, expand **Advanced network access**, and then expand **Client certificates for mTLS - optional**. In some configurations, the client certificates appear directly under **Advanced network access**, without a separate section to expand.

1. Choose **Add certificate**.

1. For **Name**, enter a name for the certificate, such as `partner-api-cert`.

1. For **Certificate source**, choose one of the following:
   +  **Use an existing secret** – Enter the **Secrets Manager ARN** of a secret that you created as described in [Store the certificate in Secrets Manager](#provide-client-certificates-secret). If the secret name does not start with your Agent Space name, grant the service role the permission that the form shows.
   +  **Create a new secret** – Paste the **Certificate** and the **Private key** in PEM format, and enter the **Private key password** if the key is encrypted. AWS Security Agent creates the secret in your account when you save the penetration test, and names it so that the service role can already read it. For the permissions this requires, see [Grant access to the secret](#provide-client-certificates-permissions).

1. For **Hosts**, choose one or more target hosts that require this certificate.

1. Choose **Save**.

To attach another certificate, choose **Add certificate** again. To change or remove a certificate later, choose the actions menu on its row, and then choose **Edit** or **Remove**. While a certificate applies to a host, you cannot change that host’s target URL. Update or remove the certificate first.

## Provide a client certificate with the AWS CLI or API
<a name="provide-client-certificates-cli"></a>

Set `clientCertificates` in the `assets` parameter of your `create-pentest` or `update-pentest` request. Each entry has a `name`, the `secretArn` of the secret that holds the certificate and private key, and the `origins`, which are the hosts that the certificate covers.

The following example attaches one client certificate to a target host:

```
aws securityagent create-pentest \
  --title "My penetration test" \
  --agent-space-id "your-agent-space-id" \
  --assets '{
    "endpoints": [{"uri": "https://api.example.com/"}],
    "clientCertificates": [{
      "name": "partner-api-cert",
      "secretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:my-agent-space-partner-api-cert-AbCdEf",
      "origins": ["https://api.example.com"]
    }]
  }'
```

To update the client certificates on an existing penetration test, use `update-pentest`. The `assets` parameter replaces all saved assets, not only the client certificates. Send the complete `assets` object, including the endpoints, any other assets, and the full `clientCertificates` list. An empty `clientCertificates` list removes all client certificates.

## Troubleshoot client certificate errors
<a name="provide-client-certificates-troubleshoot"></a>

AWS Security Agent checks each client certificate before testing begins. If a check fails, the penetration test stops with a message that names the certificate. Find the message in the following table, and take the action for that certificate.


| Message contains | What to do | 
| --- | --- | 
| Cannot assume the pentest service role | Confirm that the service role’s trust policy allows AWS Security Agent to assume it for this penetration test. For instructions on configuring the service role, see [Create the IAM roles for AWS Security Agent](create-iam-role.md). | 
| Cannot access the secret | Grant the service role `secretsmanager:GetSecretValue` on the secret. For instructions on granting access to the secret, see [Grant access to the secret](#provide-client-certificates-permissions). | 
| Cannot decrypt the secret | Grant the service role `kms:Decrypt` on the secret’s customer managed key, and confirm the key is enabled. | 
| Secret not found, or could not be read due to an invalid parameter | Confirm that the Secrets Manager ARN is correct. | 
| is in an invalid state | The secret is pending deletion. Restore the secret, or replace it with a new one. | 
| does not contain a text value | The secret is stored as binary. Store the certificate and key as a JSON `SecretString` in the format shown in [Store the certificate in Secrets Manager](#provide-client-certificates-secret). | 
| is not valid JSON, or must be a JSON object | Store the value as a JSON object in the format shown in [Store the certificate in Secrets Manager](#provide-client-certificates-secret). | 
| is missing the 'certificate' or 'privateKey' field | Add both fields to the secret. | 
| is not valid PEM-encoded X.509 material, or could not be loaded by the TLS stack | Check the PEM line breaks. A secret created in the Secrets Manager console **Key/value** tab stores `\n` as literal characters. | 
| The private key in client certificate | Confirm that the key is PEM-encoded and that `privateKeyPassword` is correct, or remove it if the key is not encrypted. | 
| The private key does not match the certificate | Use the private key from the same key pair as the certificate. | 
| has expired, or is not yet valid | Replace the certificate with one that is currently valid. | 
| run window | Use a certificate that stays valid for at least 36 hours after the penetration test starts, or for your maximum task-hours limit if it is lower than 36. | 