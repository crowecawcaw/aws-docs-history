Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# END

Commits the current transaction. Performs exactly the same function as the COMMIT
command.

See [COMMIT](r_COMMIT.md "r_COMMIT.md") for more detailed
documentation.

## Syntax

```
END [ WORK | TRANSACTION ]
```

## Parameters

WORK

Optional keyword.

TRANSACTION

Optional keyword; WORK and TRANSACTION are synonyms.

## Examples

The following examples all end the transaction block and commit the
transaction:

```
end;
```

```
end work;
```

```
end transaction;
```

After any of these commands, Amazon Redshift ends the transaction block and commits the
changes.
