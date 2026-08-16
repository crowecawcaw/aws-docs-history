# Disallowed output columns

The `disallowedOutputColumns` control in the custom analysis rule lets you
define the list of columns that cannot be projected in the query result. Any reference to a
disallowed column through transformation, aliasing, or other means cannot appear in the final
SELECT (projection) of the query.

The control prohibits direct projection but does not fully prevent values from being
indirectly inferred. You can still use disallowed columns in a projection inside a subquery or
common table expression (CTE), as long as they are not referenced in the final
projection.

###### CACHE TABLE constraint

AWS Clean Rooms enforces the disallowed output columns constraint on cached tables. A cached table
cannot reference a disallowed output column in its SELECT clause. To use a
column with a disallowed output column constraint in a subsequent part of your query,
convert the cached table to a CTE.

The following example adds `user_id` to the
`disallowedOutputColumns` control:

```
{
  "disallowedOutputColumns": [
    "user_id"
  ]
}
```

For more information about how disallowed columns work with configured tables, see [Configured table disallowed columns](disallowed-columns.md "disallowed-columns.md").
