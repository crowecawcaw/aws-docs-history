# Inline views

With AWS DMS, you can create and use inline views to streamline data transformations during migration tasks. An inline view is a subquery that acts as a virtual table, allowing you to combine and manipulate data from multiple sources without creating a persistent database object.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Five star feature compatibility | Five star automation level         | N/A                       | N/A             |

## Oracle usage

Inline views refer to a `SELECT` statement located in the `FROM` clause of secondary `SELECT` statement. Inline views can help make complex queries simpler by removing compound calculations or eliminating join operations while condensing several separate queries into a single simplified query.

**Examples**

The SQL statement marked in red represents the inline view code. The query returns each employee matched to their salary and department id. In addition, the query returns the average salary for each department using the inline view column `SAL_AVG`.

```
SELECT A.LAST_NAME, A.SALARY, A.DEPARTMENT_ID, B.SAL_AVG
FROM EMPLOYEES A,
(SELECT DEPARTMENT_ID, ROUND(AVG(SALARY))
AS SAL_AVG FROM EMPLOYEES GROUP BY DEPARTMENT_ID)
WHERE A.DEPARTMENT_ID = B.DEPARTMENT_ID;
```

## PostgreSQL usage

PostgreSQL semantics may refer to inline views as Subselect or as Subquery. In either case, the functionality is the same. Running the Oracle inline view example above, as is, will result in an error: **ERROR: subquery in FROM must have an alias**. This is because Oracle supports omitting aliases for the inner statement while in PostgreSQL the use of aliases is mandatory. The following example uses `B` as an alias.

Mandatory aliases are the only major difference when migrating Oracle inline views to PostgreSQL.

**Examples**

The following example uses `B` as an alias.

```
SELECT A.LAST_NAME, A.SALARY, A.DEPARTMENT_ID, B.SAL_AVG
FROM EMPLOYEES A,
(SELECT DEPARTMENT_ID, ROUND(AVG(SALARY)) AS SAL_AVG
FROM EMPLOYEES GROUP BY DEPARTMENT_ID) B
WHERE A.DEPARTMENT_ID = B.DEPARTMENT_ID;
```
