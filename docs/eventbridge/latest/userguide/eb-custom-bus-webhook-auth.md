

# Securing a webhook event source

Webhook Events verifies every incoming request before publishing an event. You choose one authentication type when you create a webhook event source: an HMAC signature, a static token, or basic authentication. EventBridge stores the associated credential as a secret in AWS Secrets Manager in your account and verifies each request against it. This section describes the authentication types, how EventBridge stores and rotates the credential, and what you can change after the event source is created.

**Note**  
The authentication type is set when you create the event source and cannot be changed afterward. If you need a different authentication type, create a new webhook event source. See [Create a webhook event source](eb-custom-bus-webhook-sources.md#eb-custom-bus-webhook-sources-create).

This section contains the following topics:
+ [Choosing an authentication type](#eb-custom-bus-webhook-auth-types)
+ [HMAC signature verification](#eb-custom-bus-webhook-auth-hmac)
+ [Static token authentication](#eb-custom-bus-webhook-auth-static)
+ [Basic authentication](#eb-custom-bus-webhook-auth-basic)
+ [How the credential is stored](#eb-custom-bus-webhook-auth-secrets)
+ [Rotating the credential](#eb-custom-bus-webhook-auth-rotate)
+ [Updating your webhook event source](#eb-custom-bus-webhook-auth-immutable)

## Choosing an authentication type
<a name="eb-custom-bus-webhook-auth-types"></a>

You specify exactly one authentication type in the `AuthConfiguration` of the webhook configuration when you create the event source:

HMAC signature (`HmacAuthConfiguration`)  
The sending system signs each request with a shared secret and includes the signature in a header. EventBridge recomputes the signature and compares it. Use this when your provider supports signed webhooks. See [HMAC signature verification](#eb-custom-bus-webhook-auth-hmac).

Static token (`StaticTokenAuthConfiguration`)  
The sending system includes a fixed secret token in a header that you name. EventBridge compares the header value to the stored token. See [Static token authentication](#eb-custom-bus-webhook-auth-static).

Basic authentication (`BasicHttpAuthConfiguration`)  
The sending system authenticates with a user name and password using HTTP basic authentication. See [Basic authentication](#eb-custom-bus-webhook-auth-basic).

For each type, you can either supply your own secret value or omit it and let EventBridge generate one. For how the credential is stored, see [How the credential is stored](#eb-custom-bus-webhook-auth-secrets).

## HMAC signature verification
<a name="eb-custom-bus-webhook-auth-hmac"></a>

With HMAC authentication, the sending system computes a hash-based message authentication code over the request and sends it in a header. EventBridge recomputes the code with the shared secret and rejects the request if it does not match. Configure `HmacAuthConfiguration` with the following fields.


| Field | Required | Values | Description | 
| --- | --- | --- | --- | 
| Algorithm | Yes | SHA256, SHA1 | The hash algorithm used to compute the signature. | 
| Encoding | Yes | HEX, BASE64 | How the computed signature is encoded in the header. | 
| SignatureHttpHeader | Yes | Header name | The header that carries the signature. | 
| SignedMessageComposition | Yes | BODY, TIMESTAMP\_DOT\_BODY, MESSAGE\_ID\_DOT\_TIMESTAMP\_DOT\_BODY | Which parts of the request are concatenated to form the signed message. | 
| TimestampHttpHeader | Conditional | Header name | The header that carries the request timestamp. Required for the composition values that include a timestamp. | 
| TimestampToleranceInSeconds | No | 1 to 900 seconds (default 300) | How far the request timestamp may differ from the current time before the request is rejected as expired. | 
| MessageIdHttpHeader | Conditional | Header name | The header that carries a unique message ID. Required for the message-ID composition value. | 
| SignaturePrefix | Conditional | 1 to 64 characters | A prefix that precedes the signature value in the header. | 
| TimestampPrefix | Conditional | 1 to 64 characters | A prefix that precedes the timestamp value. | 
| Delimiter | Conditional | 1 to 64 characters | The separator between parts of the signature header value, such as a comma in a value like t=1727816400,v1=signature, or a space when the header carries several signatures. When the signature and timestamp share one header, it also separates those two values. | 
| SecretValue | No | 6 to 512 characters encoding to 16 to 512 bytes | The signing secret. With BASE64 SecretEncoding, the value is a base64 string that EventBridge decodes to the signing key. If you omit it, EventBridge generates one. See [How the credential is stored](#eb-custom-bus-webhook-auth-secrets). | 
| SecretEncoding | No | RAW, BASE64 (default RAW) | How EventBridge decodes the secret before using it to sign. | 

Several fields are required only in combination with others. EventBridge rejects a configuration that violates one of these rules with an `InvalidInputException` (HTTP 400):
+ `TIMESTAMP_DOT_BODY` and `MESSAGE_ID_DOT_TIMESTAMP_DOT_BODY` require `TimestampHttpHeader`.
+ `MESSAGE_ID_DOT_TIMESTAMP_DOT_BODY` also requires `MessageIdHttpHeader`.
+ Setting `TimestampToleranceInSeconds` requires `TimestampHttpHeader`.
+ The `BODY` composition signs only the body, so it rejects `TimestampHttpHeader` and `TimestampToleranceInSeconds`.
+ When the timestamp and the signature use the same header (that is, `TimestampHttpHeader` equals `SignatureHttpHeader`), `Delimiter`, `SignaturePrefix`, and `TimestampPrefix` are all required so that EventBridge can separate the two values.

The following AWS CLI example configures HMAC authentication that signs the concatenation of the timestamp and the body, with EventBridge generating the secret.

```bash
aws eventsv2 create-event-source \
    --name orders-provider-hmac \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --configuration '{
        "WebhookEventsConfiguration": {
            "AuthConfiguration": {
                "HmacAuthConfiguration": {
                    "Algorithm": "SHA256",
                    "Encoding": "HEX",
                    "SignatureHttpHeader": "X-Signature",
                    "SignedMessageComposition": "TIMESTAMP_DOT_BODY",
                    "TimestampHttpHeader": "X-Timestamp",
                    "TimestampToleranceInSeconds": 300
                }
            },
            "RoleArn": "arn:aws:iam::111122223333:role/orders-provider-webhook-role",
            "KmsKeyIdentifier": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    }'
```

### Support for the Standard Webhooks specification
<a name="eb-custom-bus-webhook-auth-standard"></a>

The HMAC fields let you match the signing scheme of many webhook providers. Because providers differ in how they name headers, order the signed fields, and format the signature value, not every provider's scheme can be expressed with these options.

Where a provider gives you a choice, we recommend the Standard Webhooks specification, a common signing scheme supported by many webhook providers. Webhook Events verifies requests signed according to the Standard Webhooks specification; configure `HmacAuthConfiguration` as follows.

```bash
aws eventsv2 create-event-source \
    --name orders-provider-standard-webhooks \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --configuration '{
        "WebhookEventsConfiguration": {
            "AuthConfiguration": {
                "HmacAuthConfiguration": {
                    "Algorithm": "SHA256",
                    "Encoding": "BASE64",
                    "SignedMessageComposition": "MESSAGE_ID_DOT_TIMESTAMP_DOT_BODY",
                    "SignatureHttpHeader": "webhook-signature",
                    "SignaturePrefix": "v1,",
                    "Delimiter": " ",
                    "MessageIdHttpHeader": "webhook-id",
                    "TimestampHttpHeader": "webhook-timestamp",
                    "SecretEncoding": "BASE64",
                    "SecretValue": "{{your-provider-signing-secret}}"
                }
            },
            "RoleArn": "arn:aws:iam::111122223333:role/orders-provider-webhook-role"
        }
    }'
```

Supply the signing secret your provider issues in `SecretValue`. EventBridge reads the message ID from the `webhook-id` header and the timestamp from the `webhook-timestamp` header, verifies the base64 signature carried as a space-delimited list of `v1,`-prefixed values in the `webhook-signature` header, and rejects requests whose timestamp falls outside `TimestampToleranceInSeconds` (300 seconds by default).

If your provider issues a signing secret with a `whsec_` prefix (the Standard Webhooks convention) and you set `SecretEncoding` to `BASE64`, EventBridge removes the `whsec_` prefix before it decodes the secret. With `SecretEncoding` set to `RAW` (the default), EventBridge uses the secret exactly as you provide it, including any prefix.

## Static token authentication
<a name="eb-custom-bus-webhook-auth-static"></a>

With static token authentication, the sending system includes a fixed secret token in a header that you name, and EventBridge compares the header value to the stored token. Configure `StaticTokenAuthConfiguration`:

`TokenHttpHeader` (required)  
The header that carries the token.

`SecretValue` (optional, 6 to 512 characters)  
The token value. If you omit it, EventBridge generates one. See [How the credential is stored](#eb-custom-bus-webhook-auth-secrets).

Static token authentication verifies the caller but does not protect the integrity of each request. For stronger protection, use HMAC signature verification with a timestamp, which adds message integrity and replay-attack protection. See [HMAC signature verification](#eb-custom-bus-webhook-auth-hmac).

## Basic authentication
<a name="eb-custom-bus-webhook-auth-basic"></a>

With basic authentication, the sending system authenticates with a user name and password using HTTP basic authentication. Configure `BasicHttpAuthConfiguration` with `Username` (1 to 512 characters) and `Password` (6 to 512 characters).

Supply both values or omit both. If you omit both, EventBridge generates the user name and password. If you supply only one of the two, EventBridge rejects the request with an `InvalidInputException` (HTTP 400).

Basic authentication verifies a user name and password but does not protect the integrity of each request. For stronger protection, use HMAC signature verification with a timestamp, which adds message integrity and replay-attack protection. See [HMAC signature verification](#eb-custom-bus-webhook-auth-hmac).

## How the credential is stored
<a name="eb-custom-bus-webhook-auth-secrets"></a>

For every authentication type, EventBridge stores the credential as a secret in Secrets Manager in your account and verifies incoming requests against it. EventBridge returns the ARN of that secret, not the secret value, in the `EventSourceDetails.WebhookDetails.SecretArn` field of the `CreateEventSource` and `DescribeEventSource` responses.

Service-generated credential  
Omit the secret value (`SecretValue` for HMAC and static token, or both `Username` and `Password` for basic authentication). EventBridge generates a credential, stores it, and returns the secret ARN.

Bring your own credential  
Provide the secret value in the authentication configuration. EventBridge stores the value you provide. You do not pass a secret ARN; EventBridge creates the secret and returns its ARN.

**Important**  
EventBridge never returns the secret value from any operation, including `DescribeEventSource`. Only the secret's ARN is returned. When EventBridge generates the credential for you, retrieve its value from Secrets Manager and configure it in the sending system, so that the sending system authenticates with the same credential EventBridge verifies against.

You can encrypt the secret with a customer managed AWS KMS key by specifying `KmsKeyIdentifier`. Secrets Manager calls AWS KMS on behalf of the identity that uses the secret, so the key policy must allow that identity: your identity when you create or rotate the credential, and the event source's role (`RoleArn`) when EventBridge reads the secret to verify requests. If you omit `KmsKeyIdentifier`, EventBridge encrypts the secret with the AWS managed key for Secrets Manager (`aws/secretsmanager`). You can change the key after creation; see [Updating your webhook event source](#eb-custom-bus-webhook-auth-immutable).

## Rotating the credential
<a name="eb-custom-bus-webhook-auth-rotate"></a>

Use `RotateWebhookCredentials` to replace the credential without changing the webhook URL or the secret ARN. EventBridge stores the new credential as a new version of the same secret and invalidates the previous one. For basic authentication, only the password is replaced; the user name doesn't change.

```bash
aws eventsv2 rotate-webhook-credentials \
    --event-source-arn arn:aws:events:us-east-1:111122223333:event-sourcev2/webhook/orders-provider/EXAMPLE1234567890abcde
```

The response returns only the `SecretArn`, which does not change on rotation. `RotateWebhookCredentials` does not return the new credential; to read a generated value, call `secretsmanager:GetSecretValue` on that secret. After rotation, EventBridge continues to accept the previous credential for 15 minutes, so update the sending system within that window.

**Note**  
To supply your own new credential instead of having EventBridge generate one, pass it to `RotateWebhookCredentials`. If you don't supply a value, EventBridge generates a new credential. The credential changes only through `RotateWebhookCredentials`; `UpdateEventSource` doesn't accept a secret value, user name, or password.

## Updating your webhook event source
<a name="eb-custom-bus-webhook-auth-immutable"></a>

Some parts of a webhook event source are fixed when you create it:
+ The authentication type, and the HMAC `SecretEncoding`, cannot be changed after creation. You can change other HMAC settings, such as the header names, signed-message composition, prefixes, and timestamp tolerance, with `UpdateEventSource`.
+ The webhook URL and the secret ARN do not change for the life of the event source. `UpdateEventSource` never changes either one, and rotating the credential does not change them.

You can change the AWS KMS key after creation with `UpdateEventSource`: switch to a different customer managed key, or between a customer managed key and the AWS managed key for Secrets Manager. AWS KMS key rotation does not affect the secret.

To change the authentication type, create a new webhook event source. To replace the credential, rotate it as described in [Rotating the credential](#eb-custom-bus-webhook-auth-rotate).