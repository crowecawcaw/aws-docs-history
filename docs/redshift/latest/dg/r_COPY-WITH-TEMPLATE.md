

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# COPY with TEMPLATE
<a name="r_COPY-WITH-TEMPLATE"></a>

You can use Redshift templates with COPY commands to simplify command syntax and maintain consistency across data loading operations. Instead of specifying the same formatting parameters repeatedly, you define them once in a template and reference the template in your COPY commands. When you use a template, the COPY command combines the parameters from the template with any parameters specified directly in the command. If the same parameter appears in both the template and the command, the command parameter takes precedence. For more information, see [CREATE TEMPLATE](r_CREATE_TEMPLATE.md). 

Templates for the COPY command can be created with:
+ [Data format parameters](copy-parameters-data-format.md)
+ [File compression parameters](copy-parameters-file-compression.md)
+ [Data conversion parameters](copy-parameters-data-conversion.md)
+ [Data load operations](copy-parameters-data-load.md)

For a complete list of supported parameters, see [COPY](r_COPY.md) command.

## Required permission
<a name="r_COPY-WITH-TEMPLATE-privileges"></a>

To use a template in a COPY command, you must have:
+ All required permissions to execute the COPY command (see [Required permissions](r_COPY.md#r_COPY-permissions) )
+ One of the following template permissions:
  + Superuser privileges
  + USAGE privilege on the template and USAGE privilege on the schema containing the template

## Syntax
<a name="r_COPY-WITH-TEMPLATE-syntax"></a>

```
COPY target_table FROM 's3://...'
authorization
[ option, ...]
USING TEMPLATE [database_name.][schema_name.]template_name;
```

## Parameters
<a name="r_COPY-WITH-TEMPLATE-parameters"></a>

 *database\_name*   
(Optional) The name of the database where the template exists. If not specified, the current database is used.

 *schema\_name*   
(Optional) The name of the schema where the template exists. If not specified, the template is searched for in the current search path.

 *template\_name*   
The name of the template to use in COPY. 

## Usage notes
<a name="r_COPY-WITH_TEMPLATE-usage-notes"></a>
+ Command-specific parameters (source, destination, authorization) must still be specified in the COPY command.
+ Templates cannot contain manifest file specifications for COPY commands.

## Examples
<a name="r_COPY-WITH-TEMPLATE-examples"></a>

The following examples show how to create a template and use it in COPY commands:

```
CREATE TEMPLATE public.test_template FOR COPY AS
CSV DELIMITER '|' IGNOREHEADER 1 MAXERROR 100;

COPY public.target_table
FROM 's3://amzn-s3-demo-bucket/staging-folder'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyLoadRoleName'
USING TEMPLATE public.test_template;
```

When a parameter exists in both the template and the command, the command parameter takes precedence. In this example, if the template `public.test_template` contains `DELIMITER '|'` but the COPY command specifies `DELIMITER ','`, the comma delimiter (`,`) from the command will be used instead of the pipe delimiter (`|`) from the template. 

```
COPY public.target_table
FROM 's3://amzn-s3-demo-bucket/staging-folder'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyLoadRoleName'
DELIMITER ','
USING TEMPLATE public.test_template;
```