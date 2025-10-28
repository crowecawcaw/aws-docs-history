Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# UDF security and permissions

To create a UDF, you must have permission for usage on language for SQL or plpythonu
(Python). By default, USAGE ON LANGUAGE SQL is granted to PUBLIC, but you must explicitly
grant USAGE ON LANGUAGE PLPYTHONU to specific users or groups.

To revoke usage for SQL, first revoke usage from PUBLIC. Then grant usage on SQL only to
the specific users or groups permitted to create SQL UDFs. The following example revokes
usage on SQL from PUBLIC. Then it grants usage to the user group `udf_devs`.

```
revoke usage on language sql from PUBLIC;
grant usage on language sql to group udf_devs;

```

To run a UDF, you must have permission to do so for each function. By default,
permission to run new UDFs is granted to PUBLIC. To restrict usage, revoke this permission
from PUBLIC for the function. Then grant the privilege to specific individuals or groups.

The following example revokes execution on function `f_py_greater` from
PUBLIC. Then it grants usage to the user group `udf_devs`.

```
revoke execute on function f_py_greater(a float, b float) from PUBLIC;
grant execute on function f_py_greater(a float, b float) to group udf_devs;
```

Superusers have all privileges by default.

For more information, see [GRANT](r_GRANT.md "r_GRANT.md") and [REVOKE](r_REVOKE.md "r_REVOKE.md").
