Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DESC IDENTITY PROVIDER

Displays information about an identity provider. Only a superuser can describe an
identity provider.

## Syntax

```
DESC IDENTITY PROVIDER *identity\_provider\_name*
```

## Parameters

_identity_provider_name_

The name of the identity provider.

## Example

The following example displays information about the identity provider.

```
DESC IDENTITY PROVIDER azure_idp;
```

Sample output.

```
  uid   |   name    | type  |              instanceid              | namespc |                                                                                                                                                 params                                                                                                                                                  | enabled
--------+-----------+-------+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------
 126692 | azure_idp | azure | e40d4bb2-7670-44ae-bfb8-5db013221d73 | aad     | {"issuer":"https://login.microsoftonline.com/e40d4bb2-7670-44ae-bfb8-5db013221d73/v2.0", "client_id":"871c010f-5e61-4fb1-83ac-98610a7e9110", "client_secret":'', "audience":["https://analysis.windows.net/powerbi/connector/AmazonRedshift", "https://analysis.windows.net/powerbi/connector/AWSRDS"]} | t
(1 row)
```
