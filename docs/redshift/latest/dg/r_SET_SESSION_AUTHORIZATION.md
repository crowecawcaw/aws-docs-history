Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SET SESSION AUTHORIZATION

Sets the user name for the current session.

You can use the SET SESSION AUTHORIZATION command, for example, to test database access
by temporarily running a session or transaction as an unprivileged user. You must be a
database superuser to run this command.

## Syntax

```
SET [ LOCAL ] SESSION AUTHORIZATION { *user\_name* | DEFAULT }
```

## Parameters

LOCAL

Specifies that the setting is valid for the current transaction. Omitting
this parameter specifies that the setting is valid for the current
session.

_user_name_

Name of the user to set. The user name may be written as an identifier or a
string literal.

DEFAULT

Sets the session user name to the default value.

## Examples

The following example sets the user name for the current session to
`dwuser`:

```
SET SESSION AUTHORIZATION 'dwuser';
```

The following example sets the user name for the current transaction to
`dwuser`:

```
SET LOCAL SESSION AUTHORIZATION 'dwuser';
```

This example sets the user name for the current session to the default user
name:

```
SET SESSION AUTHORIZATION DEFAULT;
```
