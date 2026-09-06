

# Paddle API Key
<a name="mes-partner-PaddleApiKey"></a>

## Secret Value Fields
<a name="w2aac27c11c35b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "api_key": "{{Paddle API key value}}"
}
```

api\_key  
The Paddle API key value (starts with `pdl_live_`, `pdl_test_`, or `pdl_sdbx_` followed by `apikey_` and the key content). This is the field that gets rotated.

## Secret Metadata Fields
<a name="w2aac27c11c35b5"></a>

The following are the metadata fields for Paddle API Key:

```
{
  "gracePeriodSeconds": "{{300 (optional)}}"
}
```

gracePeriodSeconds  
(Optional) Number of seconds the old API key remains valid after rotation (0–86400). Default: 300. Set to 0 for immediate expiry of the old key. The grace period countdown starts when the new key is first used successfully.

## Usage Flow
<a name="w2aac27c11c35b7"></a>

This rotation uses a single-secret architecture. No admin secret is required. The API key rotates itself through the Paddle rotation endpoint.

Create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call. Set the secret value to the field described above and set the secret type to PaddleApiKey. To configure rotation, use the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. Provide a role ARN that grants the service the required permissions to rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md).

During rotation, the driver extracts the key ID and resolves the Paddle API host from the key prefix. It then calls the Paddle rotation endpoint with a configurable grace period. Secrets Manager stores the new key as AWSPENDING, verifies it by making a non-mutating API call, and promotes it to AWSCURRENT. The old key remains valid for the duration of the grace period (default 300 seconds) before auto-expiring.

The API key must be created with the "rotatable" option enabled in the Paddle Dashboard. Secrets Manager rejects non-rotatable keys with an error.