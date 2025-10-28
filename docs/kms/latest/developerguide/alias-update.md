# Update aliases

Because an alias is an independent resource, you can change the KMS key associated with
an alias. For example, if the `test-key` alias is associated with one KMS key,
you can use the [UpdateAlias](../APIReference/API_UpdateAlias.md "../APIReference/API_UpdateAlias.md") operation
to associate it with a different KMS key. This is one of several ways to [manually rotate a KMS key](rotate-keys.md "rotate-keys.md") without changing its key material.
You might also update a KMS key so that an application that was using one KMS key for new
resources is now using a different KMS key.

You cannot update an alias in the AWS KMS console. Also, you cannot use
`UpdateAlias` (or any other operation) to change an alias name. To change an
alias name, delete the current alias and then create a new alias for the KMS key.

When you update an alias, the current KMS key and the new KMS key must be the same
type (both symmetric or asymmetric or HMAC). They must also have the same key usage
(`ENCRYPT_DECRYPT` or `SIGN_VERIFY` or GENERATE_VERIFY_MAC). This
restriction prevents cryptographic errors in code that uses aliases.

The following example begins by using the [ListAliases](../APIReference/API_ListAliases.md "../APIReference/API_ListAliases.md") operation to show that the `test-key` alias is currently
associated with KMS key `1234abcd-12ab-34cd-56ef-1234567890ab`.

```
`$` `aws kms list-aliases --key-id 1234abcd-12ab-34cd-56ef-1234567890ab`
`{
 "Aliases": [
 {
 "AliasName": "alias/test-key",
 "AliasArn": "arn:aws:kms:us-west-2:111122223333:alias/test-key",
 "TargetKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "CreationDate": 1593622000.191,
 "LastUpdatedDate": 1593622000.191
 }
 ]
}`
```

Next, it uses the `UpdateAlias` operation to change the KMS key that is
associated with the `test-key` alias to KMS key `0987dcba-09fe-87dc-65ba-ab0987654321`.
You don't need to specify the currently associated KMS key, only the new ("target")
KMS key. The alias name is case sensitive.

```
`$` `aws kms update-alias --alias-name 'alias/test-key' --target-key-id 0987dcba-09fe-87dc-65ba-ab0987654321`
```

To verify that the alias is now associated with the target KMS key, use the
`ListAliases` operation again. This AWS CLI command uses the `--query`
parameter to get only the `test-key` alias. The `TargetKeyId` and
`LastUpdatedDate` fields are updated.

```
`$` `aws kms list-aliases --query 'Aliases[?AliasName==`alias/test-key`]'`
`[
 {
 "AliasName": "alias/test-key",
 "AliasArn": "arn:aws:kms:us-west-2:111122223333:alias/test-key",
 "TargetKeyId": "0987dcba-09fe-87dc-65ba-ab0987654321",
 "CreationDate": 1593622000.191,
 "LastUpdatedDate": 1604958290.154
 }
]`
```
