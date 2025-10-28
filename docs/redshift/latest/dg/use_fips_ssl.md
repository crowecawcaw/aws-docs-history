Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# use_fips_ssl

## Values (default in bold)

true, **false**

## Description

A parameter group value that specifies if FIPS-compliant SSL mode is used.
If `use_fips_ssl` is `true`, then FIPS-compliant SSL mode is used.
If `use_fips_ssl` is `false`, then FIPS-compliant SSL mode is not used.
For more information, see
[Configuring security options for connections](../mgmt/connecting-ssl-support.md "../mgmt/connecting-ssl-support.md") in the _Amazon Redshift Management Guide_.

To configure parameters for an Amazon Redshift provisioned cluster, see
[About parameter groups](../mgmt/working-with-parameter-groups.md "../mgmt/working-with-parameter-groups.md") in the _Amazon Redshift Management Guide_.
To configure parameters for Redshift Serverless, see
[Configuring a FIPS-compliant SSL connection to
Amazon Redshift Serverless](../mgmt/serverless-connecting.md#serverless_secure-fips-ssl "../mgmt/serverless-connecting.md#serverless_secure-fips-ssl") in the _Amazon Redshift Management Guide_, and
[CreateWorkgroup](../../../redshift-serverless/latest/APIReference/API_CreateWorkgroup.md "../../../redshift-serverless/latest/APIReference/API_CreateWorkgroup.md")
or [UpdateWorkgroup](../../../redshift-serverless/latest/APIReference/API_UpdateWorkgroup.md "../../../redshift-serverless/latest/APIReference/API_UpdateWorkgroup.md") in the _Redshift Serverless API Reference_.
