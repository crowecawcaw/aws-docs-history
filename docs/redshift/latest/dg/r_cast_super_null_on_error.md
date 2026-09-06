

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# cast\_super\_null\_on\_error
<a name="r_cast_super_null_on_error"></a>

## Values (default in bold)
<a name="r_cast_super_null_on_error-values"></a>

**on**, off

## Description
<a name="description"></a>

Specifies that when you try to access a nonexistent member of an object or element of an array, Amazon Redshift returns a NULL value if your query is run in the default lax mode.