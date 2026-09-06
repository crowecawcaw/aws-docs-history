

# Using aliases
<a name="keys-managealias"></a>

 An *alias* is a friendly name for an AWS Payment Cryptography key. For example, an alias lets you refer to a key as `alias/test-key` instead of `arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h`. 

You can use an alias to identify a key in most key management (control plane) operations, and in [cryptographic (data plane) operations](data-operations.md). 

You can also allow and deny access to AWS Payment Cryptography key based on their aliases without editing policies or managing grants. This feature is part of the service's support for [attribute-based access control](security.md) (ABAC).

Aliases also make it easier to reuse the same code in different AWS Regions. Create aliases with the same name in multiple Regions and associate each alias with an AWS Payment Cryptography key in its Region. When the code runs in each Region, the alias refers to the associated AWS Payment Cryptography key in that Region.

You can create an alias for an AWS Payment Cryptography key by using the `CreateAlias` API.

The AWS Payment Cryptography API provides full control of aliases in each account and Region. The API includes operations to create an alias (CreateAlias), view alias names and the linked keyARN (**list-aliases**), change the AWS Payment Cryptography key associated with an alias (**update-alias**), and delete an alias (**delete-alias**).

**Topics**
+ [About aliases](alias-about.md)
+ [Using aliases in your applications](alias-using.md)
+ [Related APIs](#w2aac12c30c21)

## Related APIs
<a name="w2aac12c30c21"></a>

**[Tags](tagging-keys.md)**  
Tags are key and value pairs that act as metadata for organizing your AWS Payment Cryptography keys. They can be used to flexibly identify keys or group one or more keys together. 