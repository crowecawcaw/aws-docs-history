

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Considerations for data sharing with data lake tables in Amazon Redshift
<a name="considerations-datashare-datalake"></a>

The following are considerations when working with data lake tables in Amazon Redshift:
+ To data share data lake tables from an encrypted AWS Glue catalog, you must delegate AWS KMS operations to an IAM role by following the instructions in [Encrypting your Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/encrypt-glue-data-catalog.html).
+  External tables that explicitly specify manifest files in the `LOCATION` clause aren't supported for data sharing. This includes the following tables that Amazon Redshift Spectrum supports: 
  +  Delta Lake 
  +  Hudi 