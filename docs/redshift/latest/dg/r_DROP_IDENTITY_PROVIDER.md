Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# DROP IDENTITY PROVIDER

Deletes an identity provider. This command isn't reversible. Only a superuser can
drop an identity provider.

## Syntax

```
DROP IDENTITY PROVIDER *identity\_provider\_name* [ CASCADE ]
```

## Parameters

_identity\_provider\_name_

Name of the identity provider to delete.

CASCADE

Deletes users and roles attached to the identity provider, when it is
deleted.

## Example

The following example deletes the _oauth\_provider_ identity
provider.

```
DROP IDENTITY PROVIDER oauth_provider;
```

If you drop the identity provider, some users may not be able to log in or use client
tools configured to use the identity provider.
