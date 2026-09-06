

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# spectrum\_enable\_pseudo\_columns
<a name="r_spectrum_enable_pseudo_columns"></a>

## Values (default in bold)
<a name="r_spectrum_enable_pseudo_columns-values"></a>

**true**, false

## Description
<a name="r_spectrum_enable_pseudo_columns-description"></a>

You can disable the creation of pseudocolumns for a session by setting the `spectrum_enable_pseudo_columns` configuration parameter to `false`.

## Example
<a name="r_spectrum_enable_pseudo_columns-example"></a>

The following command disables the creation of pseudocolumns for a session. 

```
set spectrum_enable_pseudo_columns to false;
```