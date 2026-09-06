

# Oracle and MySQL inline views
<a name="chap-oracle-aurora-mysql.special.inlineviews"></a>

With AWS DMS, you can migrate data from Oracle and MySQL databases to Aurora or using inline views. Inline views are virtual tables that combine data from one or more tables using a `SELECT` statement. They are useful for querying complex data sets, joining data across tables, and simplifying data transformations during migration.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Five star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-5.png)  |  ![Five star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-5.png)  | N/A | N/A | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.special.inlineviews.oracle"></a>

Inline views refer to `SELECT` statements located in the `FROM` clause of secondary `SELECT` statement. Inline views can help make complex queries simpler by removing compound calculations or eliminating join operations while condensing several separate queries into a single simplified query.

### Examples
<a name="chap-oracle-aurora-mysql.special.inlineviews.oracle.examples"></a>

The SQL statement marked in red represents the inline view code. The query returns each employee matched to their salary and department id. In addition, the query returns the average salary for each department using the inline view column `SAL_AVG`.

```
SELECT A.LAST_NAME, A.SALARY, A.DEPARTMENT_ID, B.SAL_AVG
FROM EMPLOYEES A,
(SELECT DEPARTMENT_ID, ROUND(AVG(SALARY))
AS SAL_AVG FROM EMPLOYEES GROUP BY DEPARTMENT_ID)
WHERE A.DEPARTMENT_ID = B.DEPARTMENT_ID;
```

## MySQL usage
<a name="chap-oracle-aurora-mysql.special.inlineviews.mysql"></a>

MySQL semantics may refer to inline views as sub select or as subquery. In either case, the functionality is the same. Running the preceding Oracle inline view example, as is, will result in the following error: `SQL Error[1248][4200]: Every derived table must have its own alias`. This error occurs because Oracle supports omission of aliases for the inner statement while in MySQL aliases are mandatory. Mandatory aliases are the only major difference when migrating Oracle inline views to MySQL.

### Examples
<a name="chap-oracle-aurora-mysql.special.inlineviews.mysql.examples"></a>

The following example uses `B` as an alias.

```
SELECT A.LAST_NAME, A.SALARY, A.DEPARTMENT_ID, B.SAL_AVG
FROM EMPLOYEES A,
(SELECT DEPARTMENT_ID, ROUND(AVG(SALARY)) AS SAL_AVG
FROM EMPLOYEES GROUP BY DEPARTMENT_ID) B
WHERE A.DEPARTMENT_ID = B.DEPARTMENT_ID;
```