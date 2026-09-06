

# `SET CONSTRAINTS`
<a name="set-constraints-syntax-support"></a>

`SET CONSTRAINTS` sets the behavior of foreign key constraint checking within the current transaction.

## Supported syntax
<a name="set-constraints-supported-syntax"></a>

```
SET CONSTRAINTS { ALL | name [, ...] } { DEFERRED | IMMEDIATE }
```

## Description
<a name="set-constraints-description"></a>

`SET CONSTRAINTS` sets the behavior of constraint checking within the current transaction. `IMMEDIATE` constraints are checked at the end of each statement. `DEFERRED` constraints aren't checked until the transaction commits. Each constraint has its own `IMMEDIATE` or `DEFERRED` mode.

When you create a constraint, you assign it one of three characteristics: `DEFERRABLE INITIALLY DEFERRED`, `DEFERRABLE INITIALLY IMMEDIATE`, or `NOT DEFERRABLE`. The third class is always `IMMEDIATE`, and the `SET CONSTRAINTS` command doesn't change it. The first two classes start every transaction in the indicated mode, but their behavior can be changed within a transaction by `SET CONSTRAINTS`.

`SET CONSTRAINTS` with a list of constraint names changes the mode of just those constraints. All named constraints must be deferrable. `SET CONSTRAINTS ALL` changes the mode of all deferrable constraints.

When `SET CONSTRAINTS` changes the mode of a constraint from `DEFERRED` to `IMMEDIATE`, the new mode takes effect retroactively. Aurora DSQL immediately checks any outstanding data modifications that would otherwise have been deferred to the end of the transaction. If any such constraint is violated, the `SET CONSTRAINTS` command fails and doesn't change the constraint mode.

For a description of the deferrability options (`DEFERRABLE`, `NOT DEFERRABLE`, `INITIALLY DEFERRED`, `INITIALLY IMMEDIATE`), see [Deferrability](create-table-syntax-support.md#create-table-fk-deferrability) on the [`CREATE TABLE`](create-table-syntax-support.md) page.

**Foreign key constraints only**  
In Aurora DSQL, `SET CONSTRAINTS` applies to foreign key constraints only. Primary key, unique, `NOT NULL`, and `CHECK` constraints are always checked immediately when a row is inserted or modified, even when you run `SET CONSTRAINTS ALL DEFERRED`.

## Notes
<a name="set-constraints-notes"></a>

Aurora DSQL changes the behavior of constraints only within the current transaction. To use `SET CONSTRAINTS`, run it inside an explicit transaction block.

## Compatibility
<a name="set-constraints-compatibility"></a>

This command complies with the behavior defined in the SQL standard, with the restriction that Aurora DSQL supports deferral for foreign key constraints only.