Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP IDENTITY PROVIDER

Deletes an identity provider. This command isn't reversible. Only a superuser can
drop an identity provider.

## Syntax

```
DROP IDENTITY PROVIDER *identity\_provider\_name* [ CASCADE ]
```

## Parameters

_identity_provider_name_

Name of the identity provider to delete.

CASCADE

Deletes users and roles attached to the identity provider, when it is
deleted.

## Example

The following example deletes the _oauth_provider_ identity
provider.

```
DROP IDENTITY PROVIDER oauth_provider;
```

If you drop the identity provider, some users may not be able to log in or use client
tools configured to use the identity provider.
