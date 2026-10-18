

# Twilio Main API Key
<a name="mes-partner-TwilioMainApiKey"></a>

## Secret Value Fields
<a name="w2aac27c13c53b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "accountSid": "{{AC followed by 32 hexadecimal characters}}",
  "adminKeySid": "{{SK followed by 32 hexadecimal characters}}",
  "adminKeySecret": "{{Main API key secret}}"
}
```

accountSid  
The Twilio account SID that owns the Main API Key.

adminKeySid  
The SID of the Main API Key that Secrets Manager uses as the administrator credential.

adminKeySecret  
The secret paired with the Main API Key SID.

## Secret Metadata Fields
<a name="w2aac27c13c53b5"></a>

This secret type has no metadata fields, because Secrets Manager does not rotate it.

## Usage Flow
<a name="w2aac27c13c53b7"></a>

This secret type stores the Twilio Main API Key that Secrets Manager uses to create and delete credentials when it rotates a secret of type TwilioApiKey. Secrets Manager does not rotate a secret of this type.

Twilio provides no API operation that creates a Main API Key, so you manage the lifecycle of this credential in the Twilio console.

You can create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call with the secret value containing the fields mentioned above and secret type as TwilioMainApiKey. Do not configure rotation for this secret. Reference it from a secret of type TwilioApiKey through the `adminSecretArn` rotation metadata field.

To avoid a manually managed administrator credential, point `adminSecretArn` at a secret of type TwilioAuthToken instead. That type rotates itself and needs no administrator credential of its own.