

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DROP LIBRARY
<a name="r_DROP_LIBRARY"></a>

Removes a custom Python library from the database. Only the library owner or a superuser can drop a library. 

DROP LIBRARY can't be run inside a transaction block (BEGIN … END). For more information about transactions, see [Isolation levels in Amazon Redshift](c_serial_isolation.md). 

This command isn't reversible. The DROP LIBRARY command commits immediately. If a UDF that depends on the library is running concurrently, the UDF might fail, even if the UDF is running within a transaction.

For more information, see [CREATE LIBRARY](r_CREATE_LIBRARY.md). 

## Required privileges
<a name="r_DROP_LIBRARY-privileges"></a>

Following are required privileges for DROPLIBRARY:
+ Superuser
+ Users with the DROP LIBRARY privilege
+ Library owner

## Syntax
<a name="r_DROP_LIBRARY-synopsis"></a>

```
DROP LIBRARY library_name
```

## Parameters
<a name="r_DROP_LIBRARY-parameters"></a>

 *library\_name*   
The name of the library.