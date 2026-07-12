# GitLab Access Token

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "token": "`GitLab access token value`",
  "tokenId": "`numeric token ID`",
  "gitlabUrl": "`GitLab instance URL`",
  "projectId": "`project ID (optional)`",
  "groupId": "`group ID (optional)`"
}
```

token

The GitLab access token value (starts with `glpat-`). This is the field that gets rotated.

tokenId

The numeric token ID. Updated each rotation with the new token's ID.

gitlabUrl

Your GitLab instance URL (for example, `https://gitlab.com`). Must use HTTPS.

projectId

(Optional) Numeric project ID. Provide for project access tokens only.

groupId

(Optional) Numeric group ID. Provide for group access tokens only.

## Secret Metadata Fields

The following are the metadata fields for GitLab Access Token:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:`GitLabAdmin`",
  "daysToExpiry": "`30 (optional)`"
}
```

adminSecretArn

(Optional) The Amazon Resource Name (ARN) for a secret of type GitLabAccessToken that contains
an api-scoped GitLab access token used to rotate this secret. If omitted, the token rotates itself
(requires `api` or `self_rotate` scope). For project tokens, the admin token
needs Maintainer role on the project. For group tokens, it needs Owner role on the group.

daysToExpiry

(Optional) Number of days until the new token expires (1–365). Maps to the `expires_at` field in the GitLab rotate API. If omitted, the new token inherits the instance default expiration.

## Usage Flow

This rotation supports both single-secret (self-rotation) and two-secret (admin-assisted) architectures. The token scope is determined by the optional `projectId` and `groupId` fields. If neither field is present, the token is a personal access token. If `projectId` is present, the token is a project access token. If `groupId` is present, the token is a group access token.

Create your secret using the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") call. Set the secret value to the fields described above and set the secret type to GitLabAccessToken. To configure rotation, use the [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call. Provide a role ARN that grants the service the required permissions to rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md "mes-security.md").

When using admin-assisted rotation, the admin secret is also of type `GitLabAccessToken`.
You must explicitly provide the rotation role access to the admin secret. You can do this by
adding a statement scoped to the admin secret ARN directly in the role policy.

During rotation, the driver validates that the current token is active. It then calls the GitLab rotate endpoint, which atomically creates a new token and revokes the old one. Secrets Manager stores the new token value and ID as AWSPENDING, verifies them via the GitLab API, and promotes them to AWSCURRENT. Applications using the Secrets Manager caching library automatically pick up the new token on their next refresh.
