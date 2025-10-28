# Get a secret value using the AWS CLI

**Required permissions:** `secretsmanager:GetSecretValue`

###### Example Retrieve the encrypted secret value of a secret

The following [`get-secret-value`](../../../cli/latest/reference/secretsmanager/get-secret-value.md "../../../cli/latest/reference/secretsmanager/get-secret-value.md") example gets the current secret value.

```
aws secretsmanager get-secret-value \
    --secret-id MyTestSecret
```

###### Example Retrieve the previous secret value

The following [`get-secret-value`](../../../cli/latest/reference/secretsmanager/get-secret-value.md "../../../cli/latest/reference/secretsmanager/get-secret-value.md") example gets the previous secret value.

```
aws secretsmanager get-secret-value \
        --secret-id MyTestSecret
        --version-stage AWSPREVIOUS
```

## Get a group of secrets in a batch using the AWS CLI

**Required permissions:**

- `secretsmanager:BatchGetSecretValue`
- `secretsmanager:GetSecretValue` permission for each secret you want to retrieve.
- If you use filters, you must also have `secretsmanager:ListSecrets`.

For an example permissions policy, see [Example: Permission to retrieve a group of secret values in a batch](auth-and-access_iam-policies.md#auth-and-access_examples_batch "auth-and-access_iam-policies.md#auth-and-access_examples_batch").

###### Important

If you have a VPCE policy that denies permission to retrieve an individual secret in the group you are retrieving, `BatchGetSecretValue` will not return any secret values, and it will return an error.

###### Example Retrieve the secret value for a group of secrets listed by name

The following [`batch-get-secret-value`](../../../cli/latest/reference/secretsmanager/batch-get-secret-value.md "../../../cli/latest/reference/secretsmanager/batch-get-secret-value.md") example gets the secret value for three secrets.

```
aws secretsmanager batch-get-secret-value \
          --secret-id-list MySecret1 MySecret2 MySecret3
```

###### Example Retrieve the secret value for a group of secrets selected by filter

The following [`batch-get-secret-value`](../../../cli/latest/reference/secretsmanager/batch-get-secret-value.md "../../../cli/latest/reference/secretsmanager/batch-get-secret-value.md") example gets the secret value for the secrets that have a tag named "Test".

```
aws secretsmanager batch-get-secret-value \
          --filters Key="tag-key",Values="Test"
```
