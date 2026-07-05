Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# CURRENT\_USER

Returns the user name of the current "effective" user of the database, as applicable
to checking permissions. Usually, this user name will be the same as the session user;
however, this can occasionally be changed by superusers.

###### Note

Do not use trailing parentheses when calling CURRENT\_USER.

## Syntax

```
current_user
```

## Return type

CURRENT\_USER returns a NAME data type and can be cast as a CHAR or VARCHAR string.

## Usage notes

If a stored procedure was created using the SECURITY DEFINER option of the CREATE\_PROCEDURE command, when invoking the CURRENT\_USER function from within the stored procedure, Amazon Redshift returns the user name of the owner of the stored procedure.

## Example

The following query returns the name of the current database user:

```
select current_user;

current_user
--------------
dwuser
(1 row)
```
