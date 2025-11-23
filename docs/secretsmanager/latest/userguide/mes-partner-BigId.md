# Big ID Refresh Token

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "hostname": "`Host Name`",
  "refreshToken": "`Refresh Token`"
}
```

hostname

This is the hostname where your BigID instance is hosted. You must enter the fully qualified domain name of your instance.

refreshToken

The JWT user refresh token generated in the BigID Console via Administration → Access Management → Select User → Generate Token → Save

## Usage Flow

You can create your secret using the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") call with the secret
value containing the fields mentioned above and secret type as BigIDClientSecret. The rotation configurations can be set using a
[RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call.
You must also provide a role ARN in the [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call which grants the service the required permissions to rotate the secret. For example of a permissions policy see [Security and Permissions](mes-security.md "mes-security.md"). Note that the rotation metadata field can be left empty for this partner.
