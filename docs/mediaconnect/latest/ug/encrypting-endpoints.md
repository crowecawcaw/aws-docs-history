

# Encrypting endpoints in MediaConnect
<a name="encrypting-endpoints"></a>

Encryption protects the content that flows across a connection between two endpoints. How you set up encryption depends on whether the endpoint is a standard endpoint or a managed endpoint.

## Encrypting standard endpoints
<a name="encrypting-standard-endpoints"></a>

A standard endpoint represents a device or software that you own, such as an encoder or decoder. By default, the connection to a standard endpoint isn't encrypted. For protocols that support encryption, such as SRT, you can encrypt the connection by providing a secret.

To turn on encryption, select **Enable encryption** under **Encryption** when you register or edit a source endpoint, or **Enable decryption** under **Decryption** when you register or edit a destination endpoint. You then provide a secret that you store in AWS Secrets Manager. The secret holds the passphrase or key, depending on the protocol.

An endpoint encryption secret must use a customer managed, enabled, symmetric AWS KMS key in the same account and Region, and you can't use the AWS managed key `aws/secretsmanager`. For more information about endpoint considerations and limitations, see [Endpoint considerations and limitations](working-with-endpoints.md#endpoints-considerations).

## Encrypting managed endpoints
<a name="encrypting-managed-endpoints"></a>

A managed endpoint represents a resource that MediaConnect manages, such as a router input or output. A managed endpoint has no encryption setting of its own. Instead, you set encryption on the resource that the endpoint represents.

You set encryption on the resource that a managed endpoint represents by choosing a key type. You can choose an automatic key type, where MediaConnect sets the key when the endpoint connects, or a Secrets Manager key type, where you provide a secret that you store in Secrets Manager.

## How encryption applies across a connection
<a name="endpoint-encryption-resolution"></a>

When two endpoints connect, MediaConnect resolves the encryption for the connection from the encryption settings of both endpoints.

The following table describes the result when a standard endpoint connects to a managed endpoint.


| Standard endpoint | Managed endpoint | Result | 
| --- | --- | --- | 
| No encryption | Automatic | The connection isn't encrypted. | 
| No encryption | A secret | Not a valid combination. Either set the managed endpoint to automatic, or create a secret for the standard endpoint. | 
| A secret | Automatic | The connection uses the standard endpoint's secret. | 
| A secret | A secret | Both secrets must hold the same passphrase or key, or the connection doesn't work. | 

The following table describes the result when two managed endpoints connect.


| Managed endpoint 1 | Managed endpoint 2 | Result | 
| --- | --- | --- | 
| Automatic | Automatic | MediaConnect creates and manages a key for the connection. | 
| Automatic | A secret | The connection uses that secret. | 
| A secret | A secret | Both secrets must hold the same passphrase or key, or the connection doesn't work. | 

## Encryption for shared endpoints
<a name="encrypting-shared-endpoints"></a>

When you share an endpoint that uses a customer secret, MediaConnect needs permission to read the secret and use its KMS key on behalf of the consuming account. Until MediaConnect has that permission, the consuming account can't connect to the endpoint. To grant it, the sharing account adds the consuming account to the `aws:SourceAccount` condition in the secret's resource policy, and adds a statement to the KMS key policy that lets the MediaConnect service principal use the key.

In the console share dialog box, you can select **Allow these principals to use the endpoint's encryption secret** to update the secret's resource policy for the principals that you share with.