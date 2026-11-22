

# Authenticated ingress points

An authenticated ingress endpoint accepts email from SMTP clients that supply the ingress endpoint ID as the username and the configured password. Use this type for applications, mail servers, and partner systems that support SMTP authentication.

You can store the password in AWS Secrets Manager or provide a Mail Manager-managed SMTP password. The authentication method is fixed when the ingress endpoint is created. You can update the secret ARN or password, but you cannot change an existing ingress endpoint from one storage method to the other.

## Connecting to an authenticated ingress point
<a name="eb-ingress-auth-connection"></a>

The following table lists the supported connection settings.


| Network | Ports | SMTP AUTH | Server name | 
| --- | --- | --- | --- | 
| Public | 25, 587 | LOGIN or PLAIN after STARTTLS | The hostname returned in ARecord. | 
| Private | 25, 587 | LOGIN or PLAIN | A DNS name returned by the associated Amazon VPC endpoint. | 

Configure the SMTP client with the following values.
+ **Username** – The ingress endpoint ID, such as `inp-0123456789abcdef01234567`.
+ **Password** – The plaintext password stored in the configured secret or supplied when the ingress endpoint was created.
+ **Encryption** – Enable STARTTLS and require server-certificate validation.

**Note**  
Provide the username and password to the SMTP client as plaintext values. The `AUTH LOGIN` and `AUTH PLAIN` protocols Base64-encode the credentials on the SMTP connection. Base64 encoding is not encryption, so use STARTTLS before authentication.

The following exchange shows STARTTLS followed by `AUTH LOGIN`. The example username is `inp-0123456789abcdef`. The value {{base64-encoded-SMTP-password}} represents the password after Base64 encoding.

```
S: 220 Ready
C: EHLO client.example.com
S: 250-STARTTLS
C: STARTTLS
S: 220 Ready to start TLS
    [TLS negotiation]
C: EHLO client.example.com
S: 250 AUTH LOGIN PLAIN
C: AUTH LOGIN
S: 334 VXNlcm5hbWU6
C: aW5wLTAxMjM0NTY3ODlhYmNkZWY=
S: 334 UGFzc3dvcmQ6
C: {{base64-encoded-SMTP-password}}
S: 235 Authentication successful
```

Most SMTP libraries perform this encoding and exchange automatically. Do not enter the encoded strings as the username or password in an SMTP client.

## Choosing password storage
<a name="eb-ingress-auth-password-storage"></a>

### Store the password in Secrets Manager
<a name="eb-ingress-auth-secrets-manager"></a>

Using AWS Secrets Manager is recommended when you need automatic rotation or centralized access control. Store the password in a JSON secret with the following structure.

```json
{
  "password": "{{your-SMTP-password}}"
}
```

The key name is `password`. Other JSON properties are ignored during SMTP authentication. Mail Manager also accepts a secret containing only a plaintext password, but the JSON structure is recommended.

The secret resource policy must allow SES to call `secretsmanager:GetSecretValue` for the ingress endpoint. If the secret uses a customer managed AWS KMS key, the key policy must allow the required decrypt operation. See [Secrets Manager secrets resource permission policy for ingress endpoint](eb-policies.md#eb-policies-ingress-secrets) and [KMS customer managed key (CMK) key policy for ingress endpoint](eb-policies.md#eb-policies-ingress-cmk).

### Use a Mail Manager-managed password
<a name="eb-ingress-auth-managed-password"></a>

A Mail Manager-managed password must contain from 8 through 64 characters, with at least one lowercase letter, one uppercase letter, one decimal digit, and one supported special character. It cannot contain whitespace.

**Warning**  
Do not place a production password directly in a shell command. Shell history, process inspection, and command logs can expose command arguments. Use the SES console, an SDK with a protected input source, or `--cli-input-json` with a file whose access is restricted.

## Creating authenticated ingress points with the AWS CLI
<a name="eb-ingress-auth-cli"></a>

### Create an authenticated ingress point that uses Secrets Manager
<a name="eb-ingress-auth-cli-secret"></a>

In the following command, replace the AWS Region, secret ARN, rule set ID, traffic policy ID, and name with your own values.

```bash
PROMPT> aws mailmanager create-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-name {{application-smtp}} \
  --type AUTH \
  --rule-set-id {{rs-0123456789abcdef01234567}} \
  --traffic-policy-id {{tp-0123456789abcdef01234567}} \
  --ingress-point-configuration 'SecretArn={{arn:aws:secretsmanager:us-east-1:123456789012:secret:mail-manager-auth-a1b2c3}}' \
  --network-configuration 'PublicNetworkConfiguration={IpType=IPV4}' \
  --tls-policy REQUIRED
```

### Create an authenticated ingress point with a managed password
<a name="eb-ingress-auth-cli-password"></a>

Save the following request as `create-auth-ingress.json`. Restrict access to the file because it contains a password.

```json
{
  "IngressPointName": "application-smtp",
  "Type": "AUTH",
  "RuleSetId": "rs-0123456789abcdef01234567",
  "TrafficPolicyId": "tp-0123456789abcdef01234567",
  "IngressPointConfiguration": {
    "SmtpPassword": "{{your-SMTP-password}}"
  },
  "NetworkConfiguration": {
    "PublicNetworkConfiguration": {
      "IpType": "IPV4"
    }
  },
  "TlsPolicy": "REQUIRED"
}
```

Run the following command. Replace the AWS Region and request values with your own values.

```bash
PROMPT> aws mailmanager create-ingress-point \
  --region {{us-east-1}} \
  --cli-input-json file://create-auth-ingress.json
```

Delete the local request file securely after the operation completes.

## Rotating SMTP credentials
<a name="eb-ingress-credentials-rotation"></a>

**Warning**  
Rotating a password does not update SMTP clients. A client continues using its configured password until you change the client. Complete client updates before the previous accepted password is removed.

### Rotate a Secrets Manager password
<a name="eb-ingress-auth-secrets-rotation"></a>

For an ingress endpoint that uses AWS Secrets Manager, SMTP authentication checks the `AWSCURRENT` secret version first. If the password does not match, it checks the `AWSPREVIOUS` version. Mail Manager does not set an expiry for `AWSPREVIOUS`. The previous password remains accepted while that staging label identifies a secret version.

A rotation function for this secret follows the standard AWS Secrets Manager `createSecret`, `setSecret`, `testSecret`, and `finishSecret` steps. Mail Manager reads the secret directly, so `setSecret` does not update another resource. The `testSecret` step can validate the pending password format, but it cannot authenticate to the SMTP endpoint because SMTP authentication reads only `AWSCURRENT` and `AWSPREVIOUS`. Test the new password after `finishSecret` promotes it to `AWSCURRENT`.

The following Python example starts from the AWS Secrets Manager generic rotation pattern. It preserves other JSON properties, replaces only `password`, and does not write secret values to logs.

```python
import json
import string

import boto3

SECRETS = boto3.client("secretsmanager")
ALLOWED_SPECIAL = "!@#$%^&*()_+-=[]{}|.,?"
EXCLUDED_CHARACTERS = "".join(
    character for character in string.punctuation
    if character not in ALLOWED_SPECIAL
)


def lambda_handler(event: dict[str, str], _context: object) -> None:
    secret_id = event["SecretId"]
    token = event["ClientRequestToken"]
    step = event["Step"]
    metadata = SECRETS.describe_secret(SecretId=secret_id)
    if rotation_is_complete(metadata, token):
        return
    validate_pending_version(metadata, token)
    handlers = {
        "createSecret": create_secret,
        "setSecret": set_secret,
        "testSecret": test_secret,
        "finishSecret": finish_secret,
    }
    handlers[step](secret_id, token)


def rotation_is_complete(metadata: dict, token: str) -> bool:
    if not metadata.get("RotationEnabled"):
        raise ValueError("Rotation is not enabled for this secret")
    stages = metadata.get("VersionIdsToStages", {}).get(token, [])
    return "AWSCURRENT" in stages


def validate_pending_version(metadata: dict, token: str) -> None:
    stages = metadata.get("VersionIdsToStages", {}).get(token)
    if stages is None:
        raise ValueError("Rotation token has no secret version")
    if "AWSPENDING" not in stages:
        raise ValueError("Rotation token is not marked AWSPENDING")


def create_secret(secret_id: str, token: str) -> None:
    current = read_secret(secret_id, version_stage="AWSCURRENT")
    try:
        read_secret(secret_id, version_id=token, version_stage="AWSPENDING")
        return
    except SECRETS.exceptions.ResourceNotFoundException:
        pass
    current["password"] = generate_password()
    SECRETS.put_secret_value(
        SecretId=secret_id,
        ClientRequestToken=token,
        SecretString=json.dumps(current),
        VersionStages=["AWSPENDING"],
    )


def set_secret(secret_id: str, token: str) -> None:
    read_secret(secret_id, version_id=token, version_stage="AWSPENDING")


def test_secret(secret_id: str, token: str) -> None:
    pending = read_secret(
        secret_id, version_id=token, version_stage="AWSPENDING"
    )
    validate_password(pending["password"])


def finish_secret(secret_id: str, token: str) -> None:
    metadata = SECRETS.describe_secret(SecretId=secret_id)
    current_version = next(
        version_id
        for version_id, stages in metadata["VersionIdsToStages"].items()
        if "AWSCURRENT" in stages
    )
    if current_version == token:
        return
    SECRETS.update_secret_version_stage(
        SecretId=secret_id,
        VersionStage="AWSCURRENT",
        MoveToVersionId=token,
        RemoveFromVersionId=current_version,
    )


def read_secret(
    secret_id: str,
    version_stage: str,
    version_id: str | None = None,
) -> dict[str, str]:
    request = {"SecretId": secret_id, "VersionStage": version_stage}
    if version_id is not None:
        request["VersionId"] = version_id
    value = json.loads(SECRETS.get_secret_value(**request)["SecretString"])
    if not isinstance(value, dict) or "password" not in value:
        raise ValueError("SecretString must contain a password property")
    return value


def generate_password() -> str:
    return SECRETS.get_random_password(
        PasswordLength=32,
        ExcludeCharacters=EXCLUDED_CHARACTERS,
        RequireEachIncludedType=True,
    )["RandomPassword"]


def validate_password(password: str) -> None:
    allowed = set(string.ascii_letters + string.digits + ALLOWED_SPECIAL)
    requirements = (
        len(password) in range(8, 65),
        all(character in allowed for character in password),
        any(character.islower() for character in password),
        any(character.isupper() for character in password),
        any(character.isdigit() for character in password),
        any(character in ALLOWED_SPECIAL for character in password),
    )
    if not all(requirements):
        raise ValueError("Pending password does not meet Mail Manager requirements")
```

The rotation function execution role needs the following permissions.
+ Allow `secretsmanager:DescribeSecret`, `secretsmanager:GetSecretValue`, `secretsmanager:PutSecretValue`, and `secretsmanager:UpdateSecretVersionStage` only for the secret that the function rotates.
+ Allow `secretsmanager:GetRandomPassword`. This action does not support a secret resource ARN.
+ Allow the function to write its Lambda logs.
+ If the secret uses a customer managed AWS KMS key, authorize the rotation role to use that key.

For the complete rotation-function trust policy, resource policy, VPC configuration, and confused-deputy protections, see [Lambda rotation function execution role permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets-required-permissions.html) in the *AWS Secrets Manager User Guide*.

After you create the function and grant AWS Secrets Manager permission to invoke it, the following command configures a 30-day rotation schedule and starts the first rotation. Replace the AWS Region, secret ARN, and function ARN with your own values.

```bash
PROMPT> aws secretsmanager rotate-secret \
  --region {{us-east-1}} \
  --secret-id {{arn:aws:secretsmanager:us-east-1:123456789012:secret:mail-manager-auth-a1b2c3}} \
  --rotation-lambda-arn {{arn:aws:lambda:us-east-1:123456789012:function:rotate-mail-manager-auth}} \
  --rotation-rules '{"ScheduleExpression":"rate(30 days)"}'
```

For the standard rotation contract and deployment procedure, see [Lambda rotation functions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_lambda-functions.html) and [Set up automatic rotation for non-database secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.html).

### Rotate a Mail Manager-managed password
<a name="eb-ingress-auth-managed-rotation"></a>

When `UpdateIngressPoint` supplies a new `SmtpPassword`, the new password becomes current and the former password remains valid for 14 days. After the expiry timestamp, authentication with the former password fails.

`GetIngressPoint` does not return either password. It returns the following metadata in `IngressPointAuthConfiguration.IngressPointPasswordConfiguration`.
+ `SmtpPasswordVersion` identifies the current password version.
+ `PreviousSmtpPasswordVersion` identifies the previous password version.
+ `PreviousSmtpPasswordExpiryTimestamp` shows when the previous password stops working.

Run the following command after an update to inspect this metadata.

```bash
PROMPT> aws mailmanager get-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-id {{inp-0123456789abcdef01234567}} \
  --query 'IngressPointAuthConfiguration.IngressPointPasswordConfiguration'
```

**One update does not immediately revoke the former password**  
If a current password is exposed, one update leaves that password valid as the previous password for 14 days. To invalidate it without waiting 14 days, update the ingress endpoint twice. Wait until the first update finishes and the ingress endpoint returns to `ACTIVE`. Set a temporary password in the first update and a different final password in the second update. Distribute only the final password. The exposed password is no longer the current or previous password.

Use separate protected JSON files for the temporary and final update requests. Each file contains the following structure with a different password.

```json
{
  "IngressPointId": "inp-0123456789abcdef01234567",
  "IngressPointConfiguration": {
    "SmtpPassword": "{{temporary-SMTP-password}}"
  }
}
```

Run the first update, wait for `ACTIVE`, and then run the second update with a different final password.

```bash
PROMPT> aws mailmanager update-ingress-point \
  --region {{us-east-1}} \
  --cli-input-json file://temporary-password-update.json

PROMPT> aws mailmanager get-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-id {{inp-0123456789abcdef01234567}} \
  --query 'Status'

PROMPT> aws mailmanager update-ingress-point \
  --region {{us-east-1}} \
  --cli-input-json file://final-password-update.json
```

### Remove both previously accepted Secrets Manager passwords
<a name="eb-ingress-auth-emergency-secret-rotation"></a>

**Warning**  
One AWS Secrets Manager rotation moves the former `AWSCURRENT` version to `AWSPREVIOUS`, so that password remains accepted. If an accepted password might be exposed, complete two successful rotations with different generated passwords. Wait for the first rotation to complete before starting the second. After the second rotation, neither version that was accepted before the first rotation has the `AWSCURRENT` or `AWSPREVIOUS` label.

Start each immediate rotation with the following command.

```bash
PROMPT> aws secretsmanager rotate-secret \
  --region {{us-east-1}} \
  --secret-id {{arn:aws:secretsmanager:us-east-1:123456789012:secret:mail-manager-auth-a1b2c3}}
```

After each call, use `describe-secret` to inspect `VersionIdsToStages`. Start the second rotation only after the first version is `AWSCURRENT` and no different version remains `AWSPENDING`.

## Monitoring accepted and rejected SMTP traffic
<a name="eb-ingress-auth-logging"></a>

For an accepted message, `APPLICATION_LOGS` identifies the authentication source in `ingress_point_metadata`. A managed-password ingress endpoint includes `password_version`. A Secrets Manager ingress endpoint includes `secrets_manager_arn`. The following fragment shows a message accepted with a managed password.

```json
{
  "ingress_point_type": "AUTH",
  "message_id": "0000llcki1jmushh817gr586f963a5inhkvnh81",
  "ingress_point_metadata": {
    "password_version": "2f6ebf87-c5af-4c14-a643-1ba9e94e6204"
  }
}
```

A traffic-policy rejection occurs after successful SMTP authentication. Use `TRAFFIC_POLICY_DEBUG_LOGS` to see the rejected recipient and matching policy statement. The following fragment shows a rejection.

```json
{
  "ingress_point_type": "AUTH",
  "ingress_point_id": "inp-0123456789abcdef01234567",
  "traffic_policy_id": "tp-0123456789abcdef01234567",
  "traffic_policy_verdict": "REJECT",
  "sender_ip_address": "{{client-ip-address}}",
  "recipient": "blocked@example.com"
}
```

An invalid username or password is rejected before traffic-policy evaluation. The SMTP client receives the following response.

```
535 5.7.8 Authentication Credentials Invalid
```

For log delivery setup, complete schemas, and CloudWatch Logs Insights queries, see [Mail Manager logging](eb-logging.md).

## Recommendations for authenticated ingress points
<a name="eb-ingress-auth-recommendations"></a>
+ Use AWS Secrets Manager when you need scheduled rotation and centralized access control.
+ Require STARTTLS and server-certificate validation for every public connection.
+ Give each independently managed sender group its own ingress endpoint and password. This limits the clients affected by a rotation.
+ Set a rotation interval that gives every SMTP client enough time to adopt the new `AWSCURRENT` password before the next rotation removes the older `AWSPREVIOUS` version.
+ Do not log passwords, secret values, Base64 credential strings, or files that contain them.
+ Use a restrictive traffic policy in addition to SMTP authentication.

**Authenticated ingress point examples**  
For an end-to-end authenticated SMTP setup, see [AWS Messaging Blog: Using Amazon Mail Manager SMTP to send email using Amazon Simple Email Service](https://aws.amazon.com/blogs/messaging-and-targeting/using-amazon-mail-manager-smtp-to-send-email-using-amazon-simple-email-service/). For an outbound filtering, archiving, and delivery example, see [AWS Messaging Blog: Streamlining outbound emails with Amazon SES Mail Manager](https://aws.amazon.com/blogs/messaging-and-targeting/streamlining-outbound-emails-with-amazon-ses-mail-manager/). For an inbound attachment-processing example that uses an authenticated ingress endpoint, see [AWS Messaging Blog: Build an AI email pipeline with Amazon Bedrock and SES Mail Manager](https://aws.amazon.com/blogs/messaging-and-targeting/build-an-ai-email-pipeline-with-amazon-bedrock-and-ses-mail-manager/).