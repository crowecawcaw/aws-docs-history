

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CURRENT\_DATABASE
<a name="r_CURRENT_DATABASE"></a>

Returns the name of the database where you are currently connected. 

## Syntax
<a name="r_CURRENT_DATABASE-synopsis"></a>

```
current_database()
```

## Return type
<a name="r_CURRENT_DATABASE-return-type"></a>

Returns a CHAR or VARCHAR string. 

## Example
<a name="r_CURRENT_DATABASE-example"></a>

The following query returns the name of the current database. 

```
select current_database();

current_database
------------------
tickit
(1 row)
```