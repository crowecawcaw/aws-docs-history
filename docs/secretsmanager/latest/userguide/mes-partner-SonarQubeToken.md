# SonarQube Token

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "token": "`token value`",
  "tokenName": "`token name`",
  "login": "`user that owns the token`",
  "sonarqubeUrl": "https://sonarqube.example.com",
  "tokenType": "USER_TOKEN",
  "projectKey": "`project key`"
}
```

token

The SonarQube token value (starts with `squ_`, `sqa_`, or `sqp_`). The rotation process updates this field.

tokenName

The token name (unique per user). Rotation uses this name to revoke the old token.

login

The SonarQube user that owns the token.

sonarqubeUrl

Your SonarQube instance URL (for example, `https://sonarqube.example.com`). The URL must use HTTPS and must not end with a trailing slash.

tokenType

(Optional) The type of token: `USER_TOKEN` (default), `GLOBAL_ANALYSIS_TOKEN`, or `PROJECT_ANALYSIS_TOKEN`.

projectKey

(Optional) The SonarQube project key. Required only when `tokenType` is `PROJECT_ANALYSIS_TOKEN`.

## Secret Metadata Fields

The following are the metadata fields for SonarQube Token:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:`SonarQubeAdmin`"
}
```

adminSecretArn

(Optional) The Amazon Resource Name (ARN) for a secret of type SonarQubeToken that
contains an admin token. This field is required for Global Analysis and Project Analysis tokens. It is optional
for User Tokens; omit it to enable self-rotation, where the current token generates and
revokes its own replacement.

## Usage Flow

This rotation supports single-secret (self-rotation) for User Tokens and two-secret
(admin-assisted) rotation for Global Analysis and Project Analysis tokens. The `tokenType`
value determines the token scope.

To create your secret, use the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") API call. Set the secret value to the
fields described above and set the secret type to SonarQubeToken. To configure rotation, use the
[RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") API call. In the RotateSecret call, provide a role ARN that grants the
service permission to rotate the secret. For an example permissions policy, see [Security and Permissions](mes-security.md "mes-security.md"). When using admin-assisted rotation,
explicitly grant the rotation role access to the admin secret ARN.

During rotation, the driver generates a new token, stores it as the pending version, verifies it
against the SonarQube API, promotes it to current, then revokes the old token by its
`tokenName`. Applications using the Secrets Manager caching library pick up the new token on their next
refresh.

SonarQube Server is customer-hosted, so your SonarQube instance must be
reachable over HTTPS from the Secrets Manager rotation service. Rotation calls originate from the AWS-managed
prefix list
`com.amazonaws.`region`.secretsmanager-managed-external-secrets`. Allow
inbound access from this prefix list on your instance's security group or firewall, and ensure the
instance presents a publicly trusted TLS certificate. For more information, see
[AWS-managed prefix lists](../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md "../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md") in the _Amazon VPC User Guide_.
Instances that are not reachable over the public internet are not supported.
