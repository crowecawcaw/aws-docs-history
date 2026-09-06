

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# use\_fips\_ssl
<a name="use_fips_ssl"></a>

## Values (default in bold)
<a name="use_fips_ssl-values"></a>

true, **false**

## Description
<a name="description"></a>

A parameter group value that specifies if FIPS-compliant SSL mode is used. If `use_fips_ssl` is `true`, then FIPS-compliant SSL mode is used. If `use_fips_ssl` is `false`, then FIPS-compliant SSL mode is not used. For more information, see [Configuring security options for connections](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html) in the *Amazon Redshift Management Guide*. 

To configure parameters for an Amazon Redshift provisioned cluster, see [About parameter groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Management Guide*. To configure parameters for Redshift Serverless, see [Configuring a FIPS-compliant SSL connection to Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-connecting.html#serverless_secure-fips-ssl) in the *Amazon Redshift Management Guide*, and [CreateWorkgroup](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateWorkgroup.html) or [UpdateWorkgroup](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateWorkgroup.html) in the *Redshift Serverless API Reference*. 