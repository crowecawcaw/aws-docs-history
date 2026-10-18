

# Twilio API Key
<a name="mes-partner-TwilioApiKey"></a>

## Secret Value Fields
<a name="w2aac27c13c49b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "accountSid": "{{AC followed by 32 hexadecimal characters}}",
  "apiKeySid": "{{SK followed by 32 hexadecimal characters}}",
  "apiKeySecret": "{{API key secret}}",
  "validationUrl": "{{https://api.twilio.com/2010-04-01/Accounts/ACxxxx/Messages.json?PageSize=1}}"
}
```

accountSid  
The Twilio account or subaccount SID that owns the API key.

apiKeySid  
The SID of the current API key. Both Standard and Restricted keys are supported.

apiKeySecret  
The secret paired with the current API key SID. Secrets Manager rotates this field together with `apiKeySid`.

validationUrl  
(Optional) A read-only Twilio API URL that Secrets Manager calls to confirm the new key works. The URL must use HTTPS and a `twilio.com` host.  
This field is required for a Restricted key. A Restricted key can call only the endpoints that its policy permits, so supply an endpoint that you know the policy allows. For a Standard key, Secrets Manager derives a default endpoint.

## Secret Metadata Fields
<a name="w2aac27c13c49b5"></a>

The following are the metadata fields for Twilio API Key:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:{{TwilioMainApiKey}}",
  "retainPreviousKey": "{{false}}",
  "friendlyNamePrefix": "{{aws-sm-api-key}}"
}
```

adminSecretArn  
The Amazon Resource Name (ARN) of the secret that holds the administrator credential. Use a secret of type TwilioMainApiKey or a secret of type TwilioAuthToken.

retainPreviousKey  
(Optional) Whether the previous key stays active after promotion. Default: false, which deletes the previous key immediately. Set this field to true to keep the previous key usable for one rotation cycle, so that applications can refresh cached credentials.

friendlyNamePrefix  
(Optional) The prefix for the friendly name of each replacement key. Default: `aws-sm-api-key`.

## Usage Flow
<a name="w2aac27c13c49b7"></a>

This rotation uses a two-secret architecture. A Twilio API key cannot rotate itself, because the Twilio key management endpoints reject API key authentication. An administrator secret therefore provides the credential that creates and deletes keys.

You can create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call with the secret value containing the fields mentioned above and secret type as TwilioApiKey. The rotation configurations can be set using a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. You must provide the `adminSecretArn` in the rotation metadata. You must also provide a role ARN in the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call which grants the service the required permissions to rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md).

The administrator secret type (`TwilioMainApiKey` or `TwilioAuthToken`) differs from the user secret type (`TwilioApiKey`). Because of this difference, the default rotation role policy scoped by `secretsmanager:resource/Type` does not grant access to the administrator secret. You must explicitly provide the rotation role access to the administrator secret. You can do this by adding a statement scoped to the administrator secret type. Alternatively, specify the administrator secret `ARN` directly in the role policy.

During rotation, Secrets Manager reads the type and the policy of the current key. It creates a replacement key that carries the same type and policy, and stores the replacement as AWSPENDING. It confirms that the new key authenticates against the validation endpoint. It then deletes the previous key and promotes AWSPENDING to AWSCURRENT. If you set `retainPreviousKey` to true, Secrets Manager keeps the previous key and deletes it during the next rotation.

Each replacement key inherits the type and the policy of the key it replaces, so a Restricted key stays Restricted with the same permissions. Rotation fails instead of creating a key with different privileges when Secrets Manager cannot read the type or the policy of the current key.