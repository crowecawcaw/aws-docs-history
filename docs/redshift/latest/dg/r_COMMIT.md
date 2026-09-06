

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# COMMIT
<a name="r_COMMIT"></a>

Commits the current transaction to the database. This command makes the database updates from the transaction permanent.

## Syntax
<a name="r_COMMIT-synopsis"></a>

```
COMMIT [ WORK | TRANSACTION ]
```

## Parameters
<a name="r_COMMIT-parameters"></a>

WORK  
Optional keyword. This keyword isn't supported within a stored procedure. 

TRANSACTION  
Optional keyword. WORK and TRANSACTION are synonyms. Neither is supported within a stored procedure. 

For information about using COMMIT within a stored procedure, see [Managing transactions](stored-procedure-transaction-management.md). 

## Examples
<a name="r_COMMIT-examples"></a>

Each of the following examples commits the current transaction to the database:

```
commit;
```

```
commit work;
```

```
commit transaction;
```