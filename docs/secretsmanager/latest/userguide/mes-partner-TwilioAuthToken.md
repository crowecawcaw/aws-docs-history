

# Twilio Auth Token
<a name="mes-partner-TwilioAuthToken"></a>

## Secret Value Fields
<a name="w2aac27c13c51b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "accountSid": "{{AC followed by 32 hexadecimal characters}}",
  "authToken": "{{32-character hexadecimal Auth Token}}",
  "validationUrl": "{{https://api.twilio.com/2010-04-01/Accounts/ACxxxx/Messages.json?PageSize=1}}"
}
```

accountSid  
The Twilio account SID whose Auth Token Secrets Manager rotates.

authToken  
The current primary Auth Token for the account. Secrets Manager rotates this field.

validationUrl  
(Optional) A read-only Twilio API URL that Secrets Manager calls to confirm the promoted token works. The URL must use HTTPS and a `twilio.com` host. Secrets Manager derives a default endpoint when you omit this field.

## Secret Metadata Fields
<a name="w2aac27c13c51b5"></a>

The following are the metadata fields for Twilio Auth Token:

```
{
  "propagationDelaySeconds": "{{60}}"
}
```

propagationDelaySeconds  
(Optional) The number of seconds that Secrets Manager waits before it validates a promoted Auth Token. The maximum is 300. Default: 60, which covers Twilio Functions propagation.  
The delay extends the window in which AWSCURRENT names the previous token. If your applications do not use Twilio Functions, set this field to 0 to shorten that window.

## Usage Flow
<a name="w2aac27c13c51b7"></a>

This rotation type self-rotates. Secrets Manager authenticates with the current primary Auth Token of the account, so no separate administrator credential is needed and the rotation metadata has no required fields.

You can create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call with the secret value containing the fields mentioned above and secret type as TwilioAuthToken. The rotation configurations can be set using a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. You must provide a role ARN in the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call which grants the service the required permissions to rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md).

During rotation, Secrets Manager creates a secondary Auth Token and stores it as AWSPENDING. It promotes the secondary token to primary, which invalidates the previous primary token immediately. It waits for `propagationDelaySeconds`, confirms that the promoted token authenticates, and promotes AWSPENDING to AWSCURRENT.

Promotion is what makes the new token usable, and it invalidates the previous token at the same time. This type therefore has no overlap window in which both tokens authenticate. Applications that cache the Auth Token should retrieve it when they open a connection, or retry after an authentication failure by re-reading AWSCURRENT. For an overlap window, use Twilio API Key with `retainPreviousKey`.