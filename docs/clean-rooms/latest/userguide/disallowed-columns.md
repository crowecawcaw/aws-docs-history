# Configured table disallowed columns

The disallowed output columns configuration is a control in the AWS Clean Rooms custom analysis rule
that enables you to define the list of columns (if any) that you don’t allow to be projected
in the query result. The columns referenced in this list are considered “disallowed output
columns”. This means that any reference to such column through transformation, aliasing, or
other means may not be present in the final SELECT (projection) of the query.

While the capability prohibits columns from being directly projected in the output, it
doesn't fully prevent underlying values from being indirectly inferred through other
mechanisms. These columns can still be used in a projection clause (such as in a subquery or a
Common Table Expression (CTE)), as long as they aren't referenced in the very final
projection.

The disallowed output columns configuration gives you the flexibility to apply and codify
control on your table in combination with analysis template level reviews based on use cases
and corresponding privacy requirements.

For more information on how to set this configuration, see [Adding a custom analysis rule to a table
(guided flow)](add-analysis-rule.md#add-custom-analysis-rule-wizard "add-analysis-rule.md#add-custom-analysis-rule-wizard").

**Examples**

The following examples display how the disallowed output columns control is applied.

- Member A is in a collaboration with Member B.
- Member B is member who can run queries.
- Member A defines a table _users_ with the columns
  _age_, _gender_, _email_, and
  _name_. The columns _age_ and
  _name_ are disallowed output columns.
- Member B defines a table _pets_ with a similar set of columns
  _age_, _gender_, and
  _owner_name_. However, they don't set any constraints on the output
  columns, meaning that all columns in the table can be projected freely in the
  query.
  If Member B runs the following query, it's blocked because disallowed output columns can't
  be directly projected:

```
SELECT
  age
FROM
  users

```

If Member B runs the following query, it's blocked because disallowed output columns can't
be implicitly projected via project star:

```
SELECT
  *
FROM
  users

```

If Member B runs the following query, it's blocked because transformations of disallowed
output columns can't be projected:

```
SELECT
  COUNT(age)
FROM
  users

```

If Member B runs the following query, it's blocked because disallowed output columns can't
be referenced in final projection using an alias:

```
SELECT
  count_age
FROM
  (SELECT COUNT(age) AS count_age FROM users)

```

If Member B runs the following query, it's blocked because transformed restricted columns
are projected in output:

```
SELECT
  CONCAT(name, email)
FROM
  users

```

If Member B runs the following query, it's blocked because disallowed output columns
defined in CTE can't be referenced in the final projection:

```
WITH cte AS (
  SELECT
    age AS age_alias
  FROM
    users
)
SELECT age_alias FROM cte

```

If Member B runs the following query, it's blocked because disallowed output columns can't
be used as sort or partition keys in the final projection:

```
SELECT
  LISTAGG(gender) WITHIN GROUP (ORDER BY age) OVER (PARTITION BY age)
FROM
  users

```

If Member B runs the following query, it succeeds because columns that are part of the
disallowed output columns can still be used across other constructs in the query, such as in
join or filter clauses.

```
SELECT
  u.name,
  p.gender,
  p.age
FROM
  users AS u
JOIN
  pets AS p
ON
  u.name = p.owner_name

```

In the same scenario, Member B can also use the _name_ column in
_users_ as a filter or sort key:

```
SELECT
  u.email,
  u.gender
FROM
  users AS u
WHERE
  u.name = 'Mike'
ORDER BY
  u.name


```

Additionally, the disallowed output columns from _users_ can be used in
intermediate projections such as subqueries and CTEs, such as:

```
WTIH cte AS (
 SELECT
   u.gender,
   u.id,
   u.first_name
 FROM
   users AS u
)
SELECT
  first_name
FROM
  (SELECT cte.gender, cte.id, cte.first_name FROM cte)

```
