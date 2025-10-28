# Using a grant token

The AWS KMS API follows an [eventual
consistency](grants.md#terms-eventual-consistency "grants.md#terms-eventual-consistency") model. When you create a grant, the grant might not be effective
immediately. There might be a brief delay before the change is available throughout AWS KMS. It
typically takes less than a few seconds for the change to propagate throughout the system, but
in some cases it can take several minutes. Once the change has fully propagated throughout the
system, the grantee principal can use the permissions in the grant without specifying the
grant token or any evidence of the grant. However, if a grant that is so new that it is not
yet known to all of AWS KMS, the request might fail with an `AccessDeniedException`
error.

To use the permissions in a new grant immediately, use the [grant token](grants.md#grant_token "grants.md#grant_token") for the grant. Save the grant token that the [CreateGrant](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md") operation returns. Then submit
the grant token in the request for the AWS KMS operation. You can submit a grant token to any
AWS KMS [grant operation](grants.md#terms-grant-operations "grants.md#terms-grant-operations") and you can submit
multiple grant tokens in the same request.

The following example uses the `CreateGrant` operation to create a grant that
allows the [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") and
[Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") operations. It saves the grant
token that `CreateGrant` returns in the `token` variable. Then, in a
call to the `GenerateDataKey` operation, it uses the grant token in the
`token` variable.

```
# Create a grant; save the grant token
`$` `token=$(aws kms create-grant \
 --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
 --grantee-principal arn:aws:iam::111122223333:user/appUser \
 --retiring-principal arn:aws:iam::111122223333:user/acctAdmin \
 --operations GenerateDataKey Decrypt \
 --query GrantToken \
 --output text)`

# Use the grant token in a request
`$` `aws kms generate-data-key \
 --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
 –-key-spec AES_256 \
 --grant-tokens $token`
```

Principals with permission can also use a grant token to retire a new grant even before
the grant is available throughout AWS KMS. (The `RevokeGrant` operation doesn't accept
a grant token.) For details, see [Retiring and revoking grants](grant-delete.md "grant-delete.md").

```
# Retire the grant
`$` `aws kms retire-grant --grant-token $token`
```
