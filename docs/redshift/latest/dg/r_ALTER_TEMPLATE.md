

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ALTER TEMPLATE
<a name="r_ALTER_TEMPLATE"></a>

Changes the definition of an existing template. Use this command to rename a template, change the owner of a template, add or remove parameters from the template definition, or set parameter values.

## Required privileges
<a name="r_ALTER_TEMPLATE-privileges"></a>

To alter a template, you must have one of the following:
+ Superuser privileges
+ ALTER TEMPLATE privilege and USAGE privilege on the schema containing the template

## Syntax
<a name="r_ALTER_TEMPLATE-synopsis"></a>

```
ALTER TEMPLATE [database_name.][schema_name.]template_name
{
RENAME TO new_name
| OWNER TO new_owner
| ADD  parameter [AS] [value]
| DROP parameter
| SET parameter TO value1 [, parameter2 TO value2 , ...]
};
```

## Parameters
<a name="r_ALTER_TEMPLATE-parameters"></a>

 *database\_name*   
(Optional) The name of the database in which the template is created. If not specified, the current database is used. 

 *schema\_name*   
(Optional) The name of the schema in which the template is created. If not specified, the template is searched for in the current search path. 

 *template\_name*   
The name of the template to be altered. 

RENAME TO   
A clause that renames the template. 

 *new\_name*   
The new name of the template. For more information about valid names, see [Names and identifiers](r_names.md). 

OWNER TO   
A clause that changes the owner of the template. 

 *new\_owner*   
The new owner of the template. 

ADD *parameter* [AS] [*value*]  
Adds a new parameter to the template.  
+ For keyword-only parameters (such as CSV or GZIP), specify just the parameter name.
+ For parameters that require values, specify the parameter name followed by the value. You can optionally include AS between the parameter and value. 

DROP *parameter*  
Removes the specified parameter from the template. Cannot drop multiple parameters with a single DROP command.

SET *parameter* TO *value1* [, *parameter2* TO *value2* , ...]  
Updates the values of existing template parameters. Only use for parameters that already have values. Multiple parameters can be updated in a single command.

## Examples
<a name="r_ALTER_TEMPLATE-examples"></a>

The following example renames the test\_template template to demo\_template.

```
ALTER TEMPLATE test_template
RENAME TO demo_template;
```

The following example gives ownership of the demo\_template schema to the user bob.

```
ALTER TEMPLATE demo_template
OWNER TO bob;
```

The following example adds parameter `CSV` to template demo\_template

```
ALTER TEMPLATE demo_template
ADD CSV;
```

The following example adds parameter `TIMEFORMAT 'auto'` to template demo\_template

```
ALTER TEMPLATE demo_template
ADD TIMEFORMAT 'auto';
```

The following example drops parameter `ENCRYPTED` from template demo\_template

```
ALTER TEMPLATE demo_template
DROP ENCRYPTED;
```

The following example sets the `DELIMITER` parameter to `'|'` and the `TIMEFORMAT` parameter to `'epochsecs'`:

```
ALTER TEMPLATE demo_template
SET DELIMITER TO '|', TIMEFORMAT TO 'epochsecs';
```