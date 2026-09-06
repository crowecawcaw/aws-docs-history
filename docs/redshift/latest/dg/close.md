

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CLOSE
<a name="close"></a>

(Optional) Closes all of the free resources that are associated with an open cursor. [COMMIT](r_COMMIT.md), [END](r_END.md), and [ROLLBACK](r_ROLLBACK.md) automatically close the cursor, so it isn't necessary to use the CLOSE command to explicitly close the cursor. 

For more information, see [DECLARE](declare.md), [FETCH](fetch.md). 

## Syntax
<a name="close-synopsis"></a>

```
CLOSE cursor
```

## Parameters
<a name="close-parameters"></a>

*cursor*   
Name of the cursor to close. 

## CLOSE example
<a name="close-example"></a>

The following commands close the cursor and perform a commit, which ends the transaction:

```
close movie_cursor;
commit;
```