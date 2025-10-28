# FROM clause

The FROM clause is the source of rows for a query.

````
 <from-clause> :=
    FROM <table-reference> { , <table-reference> }...
 <table-reference> :=
    <table-name> [ <table-name> ] [ <correlation> ]
| <joined-table> <table-name> :=  <identifier> <table-over> :=  OVER <window-specification> <window-specification> := (   <window-name>
| <query_partition_clause>
| ORDER BY <order_by_clause>
| <windowing_clause> ) <windowing-clause> := { ROWS | RANGE } { BETWEEN { UNBOUNDED PRECEDING
| CURRENT ROW
| <value-expression> { PRECEDING | FOLLOWING } } AND { UNBOUNDED FOLLOWING
| CURRENT ROW
| <value-expression> { PRECEDING | FOLLOWING } }
| { UNBOUNDED { PRECEDING | FOLLOWING }
| CURRENT ROW
| <value-expression> { PRECEDING | FOLLOWING } } } ``` For charts on window-specification and windowing-clause, see the [WINDOW Clause (Sliding Windows)](sql-reference-window-clause.md "sql-reference-window-clause.md") under the Window statement. ``` <correlation> := [ AS ] <correlation-name> [ '(' <column> { , <column> }... ')' ] <joined-table> := <table-reference> CROSS JOIN <table-reference>
| <table-reference> NATURAL <join-type> JOIN <table-reference> | <table-reference> <join-type> JOIN <table-reference> [ USING '(' <column> { , <column>}... ')'
| ON <condition> ] <join-type> := INNER | <outer-join-type> [ OUTER ] <outer-join-type> := LEFT
| RIGHT | FULL ``` ###### Relations Several types of relation can appear in a FROM clause: <br>• A named relation (table, stream) <br>• A subquery enclosed in parentheses. <br>• A join combining two relations (see the topic JOIN in this guide). <br>• A transform expression. Subqueries are described in more detail in the topic Query in this guide. Here are some examples of subqueries: ``` // set operation as subquery // (finds how many departments have no employees) SELECT COUNT(*) FROM ( SELECT deptno FROM Dept EXCEPT SELECT deptno FROM Emp); // table-constructor as a subquery, // combined with a regular table in a join SELECT * FROM Dept AS d JOIN (VALUES ('Fred', 10), ('Bill', 20)) AS e (name, deptno) ON d.deptno = e.deptno; ``` Unlike subqueries in other parts of the SELECT statement, such as in the [WHERE clause](sql-reference-where-clause.md "sql-reference-where-clause.md") clause (WHERE [Condition Clause](sql-reference-conditions.md "sql-reference-conditions.md")), a subquery in the FROM clause cannot contain correlating variables. For example: ``` // Invalid query. Dept.deptno is an illegal reference to // a column of another table in the enclosing FROM clause. SELECT * FROM Dept, (SELECT * FROM Emp WHERE Emp.deptno = Dept.Deptno) ``` ## FROM clause with multiple relations If a FROM clause contains multiple, comma-separated relations, the query constructs the cartesian product of those relations; that is, it combines each row from each relation with each row from every other relation. The comma in the FROM clause is therefore equivalent to the CROSS JOIN operator. ## Correlation names Each relation in the FROM clause can have a correlation name assigned using AS correlation-name. This name is an alternative name by which the relation can be referenced in expressions throughout the query. (Even though the relation may be a subquery or stream, it is conventionally called a 'table alias' to distinguish it from column aliases defined in the SELECT clause.) Without an AS clause, a named relation's name becomes its default alias. (In streaming queries, the OVER clause does not prevent this default assignment from happening.) An alias is necessary if a query uses the same named relation more than once, or if any of the relations are subqueries or table expressions. For example, in the following query, the named relation EMPS is used twice; once with its default alias EMPS, and once with an assigned alias MANAGERS: ``` SELECT EMPS.NAME || ' is managed by ' || MANAGERS.NAME FROM LOCALDB.Sales.EMPS, LOCALDB.Sales.EMPS AS MANAGERS WHERE MANAGERS.EMPNO = EMPS.MGRNO ``` An alias can optionally be followed by a list of columns: ``` SELECT e.empname, FROM LOCALDB.Sales.EMPS AS e(empname, empmgrno) ``` ## OVER clause The OVER clause is only applicable for streaming joins. For more detail, see the topic [JOIN clause](sql-reference-join-clause.md "sql-reference-join-clause.md") in this guide.
````
