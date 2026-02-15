# `CREATE TABLE`

`CREATE TABLE` defines a new table.

```
CREATE TABLE [ IF NOT EXISTS ] table_name ( [
  { column_name data_type [ column_constraint [ ... ] ]
    | table_constraint
    | LIKE source_table [ like_option ... ] }
    [, ... ]
] )

where column_constraint is:

[ CONSTRAINT constraint_name ]
{ NOT NULL |
  NULL |
  CHECK ( expression )|
  DEFAULT default_expr |
  GENERATED ALWAYS AS ( generation_expr ) STORED |
  GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY ( sequence_options ) |
  UNIQUE [ NULLS [ NOT ] DISTINCT ] index_parameters |
  PRIMARY KEY index_parameters |

and table_constraint is:

[ CONSTRAINT constraint_name ]
{ CHECK ( expression ) |
  UNIQUE [ NULLS [ NOT ] DISTINCT ] ( column_name [, ... ] ) index_parameters |
  PRIMARY KEY ( column_name [, ... ] ) index_parameters |

and like_option is:

{ INCLUDING | EXCLUDING } { COMMENTS | CONSTRAINTS | DEFAULTS | GENERATED | IDENTITY | INDEXES | STATISTICS | ALL }

index_parameters in UNIQUE, and PRIMARY KEY constraints are:
[ INCLUDE ( column_name [, ... ] ) ]
```

## Identity columns

###### Note

When using identity columns, the cache value should be
carefully considered. For more information, see the Important callout on the [CREATE SEQUENCE](create-sequence-syntax-support.md "create-sequence-syntax-support.md") page.

For guidance on how best to use identity columns based on workload patterns,
see [Working with sequences and identity columns](sequences-identity-columns-working-with.md "sequences-identity-columns-working-with.md").

The `GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY ( `sequence_options` )`
clause creates the column as an _identity column_. It will have an implicit
sequence attached to it and in newly-inserted rows the column will automatically have values
from the sequence assigned to it. Such a column is implicitly `NOT NULL`.

The clauses `ALWAYS` and `BY DEFAULT` determine how explicitly
user-specified values are handled in `INSERT` and `UPDATE`
commands.

In an `INSERT` command, if `ALWAYS` is selected, a user-specified
value is only accepted if the `INSERT` statement specifies `OVERRIDING SYSTEM
 VALUE`. If `BY DEFAULT` is selected, then the user-specified value takes
precedence.

In an `UPDATE` command, if `ALWAYS` is selected, any update of the
column to any value other than `DEFAULT` will be rejected. If `BY
 DEFAULT` is selected, the column can be updated normally. (There is no
`OVERRIDING` clause for the `UPDATE` command.)

The `sequence_options` clause can be used to override the
parameters of the sequence. The available options include those shown for
[CREATE SEQUENCE](create-sequence-syntax-support.md "create-sequence-syntax-support.md"), plus `SEQUENCE NAME
 `name``. Without `SEQUENCE NAME`, the system chooses
an unused name for the sequence.
