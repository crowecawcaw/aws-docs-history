# About aliases

Learn how aliases work in AWS Payment Cryptography.

**An alias is an independent AWS resource**

An alias is not a property of an AWS Payment Cryptography key. The actions that you take on the alias
don't affect its associated key. You can create an alias for an AWS Payment Cryptography key and then
update the alias so it's associated with a different AWS Payment Cryptography key. You can even delete the
alias without any effect on the associated AWS Payment Cryptography key. If you delete a
AWS Payment Cryptography key, all aliases associated with that key will become unassigned.

If you specify an alias as the resource in an IAM policy, the policy refers to the
alias, not to the associated AWS Payment Cryptography key.

**Each alias has a friendly name**

When you create an alias, you specify the alias name prefixed by `alias/`. For instance `alias/test_1234`

**Each alias is associated with one AWS Payment Cryptography key at a time**

The alias and its AWS Payment Cryptography key must be in the same account and Region.

An AWS Payment Cryptography key can be associated with more than one alias concurrently, but each
alias can only be mapped to a single key

For example, this `list-aliases`
output shows that the `alias/sampleAlias1` alias is associated with exactly one target
AWS Payment Cryptography key, which is represented by the `KeyArn` property.

```
`$` `aws payment-cryptography list-aliases`

```

```

`{
 "Aliases": [
 {
 "AliasName": "alias/sampleAlias1",
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h"
 }
 ]
}`

```

**Multiple aliases can be associated with the same AWS Payment Cryptography key**

For example, you can associate the `alias/sampleAlias1;` and
`alias/sampleAlias2` aliases with the same key.

```
`$` `aws payment-cryptography list-aliases`
```

```

`{
 "Aliases": [
 {
 "AliasName": "alias/sampleAlias1",
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h"
 },
 {
 "AliasName": "alias/sampleAlias2",
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h"
 }
 ]
 }`

```

**An alias must be unique for a given account and Region**

For example, you can have only one `alias/sampleAlias1` alias in each account and
Region. Aliases are case-sensitive, but we recommend against using aliases that only differ in capitalization as they can be prone to error.
You cannot change an alias name. However, you can delete the
alias and create a new alias with the desired name.

**You can create an alias with the same name in different Regions**

For example, you can have alias `alias/sampleAlias2` in US East (N. Virginia) and
alias `alias/sampleAlias2` in US West (Oregon). Each alias would be
associated with an AWS Payment Cryptography key in its Region. If your code refers to an alias name like
`alias/finance-key`, you can run it in multiple Regions. In each Region, it
uses a different alias/sampleAlias2. For details, see [Using aliases in your applications](alias-using.md "alias-using.md").

**You can change the AWS Payment Cryptography key associated with an alias**

You can use the `UpdateAlias`
operation to associate an alias with a different AWS Payment Cryptography key. For example, if the
`alias/sampleAlias2` alias is associated with the `arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h`
AWS Payment Cryptography key, you can update it so it is associated with the
`arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi` key.

###### Warning

AWS Payment Cryptography doesn't validate that the old and new keys have all the same attributes such as key usage. Updating with a
different key type may result in problems in your application.

**Some keys don't have aliases**

An alias is an optional feature and not all keys will have aliases unless you choose to operate your environment in this way. Keys can be
associated with Aliases using the `create-alias` command. Also, you can use the
update-alias operation to change the
AWS Payment Cryptography key associated with an alias and the delete-alias operation to delete an alias. As a result, some AWS Payment Cryptography keys might
have several aliases, and some might have none.

**Mapping a key to an alias**

You can map a key (represented by an ARN) to one or more aliases using the `create-alias`
command. This command is not idempotent - to update an alias, use the update-alias command.

```
`$` `aws payment-cryptography create-alias --alias-name alias/sampleAlias1 \
 --key-arn arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h`
```

```
`{
 "Alias": {
 "AliasName": "alias/alias/sampleAlias1",
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h"
 }
}`
```
