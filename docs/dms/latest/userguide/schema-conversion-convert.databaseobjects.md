

# Converting database objects with generative AI
<a name="schema-conversion-convert.databaseobjects"></a>

The DMS Schema Conversion with generative AI feature streamlines the database migration process by offering recommendations to help you convert previously unconverted code objects that typically require complex manual conversion. This feature is available for Oracle to PostgreSQL/Aurora PostgreSQL, SQL Server to PostgreSQL/Aurora PostgreSQL and SAP ASE (Sybase ASE) to PostgreSQL/Aurora PostgreSQL conversions. You can convert an entire database schema or individual database schema objects.

**Warning**  
Generative AI features in DMS Schema Conversion use cross-region inference. For more information, see [Cross-region inference in DMS Schema Conversion](CHAP_Security.DataProtection.CrossRegionInference.md#CHAP_Security.DataProtection.CrossRegionInference.SchemaConversion).

To convert your source database objects with generative AI, follow steps 1 to 6 in [Converting database objects ](schema-conversion-convert.md#schema-conversion-convert-steps) then continue with one of these two methods:
+ Method 1: From the **Actions** menu, select **Convert**. In the conversion dialog box that appears, enable the **Convert schema with Generative AI** option and click **Convert**.
+ Method 2: Click ****Convert schema with Generative AI**** in the top right corner. In the conversion dialog box, ensure the option is enabled and click **Convert**.

To manually adjust this setting at any time in DMS Schema Conversion console:
+ Navigate to the **Settings** tab.
+ In the **Conversion settings section**, enable the **Generative AI** option to approve the use of generative AI.

**Note**  
Supported regions:  
Asia Pacific (Tokyo) (ap-northeast-1)
Asia Pacific (Osaka) (ap-northeast-3)
Asia Pacific (Sydney) (ap-southeast-2)
Canada (Central) (ca-central-1)
Europe (Frankfurt) (eu-central-1)
Europe (Zurich) (eu-central-2)
Europe (Stockholm) (eu-north-1)
Europe (Milan) (eu-south-1)
Europe (Spain) (eu-south-2)
Europe (Ireland) (eu-west-1)
Europe (London) (eu-west-2)
Europe (Paris) (eu-west-3)
US East (N. Virginia) (us-east-1)
US East (Ohio) (us-east-2)
US West (Oregon) (us-west-2)

**Note**  
Supported conversion paths:  
Oracle to Amazon RDS for PostgreSQL
Oracle to Amazon Aurora PostgreSQL
Microsoft SQL Server to Amazon RDS for PostgreSQL
Microsoft SQL Server to Amazon Aurora PostgreSQL
SAP ASE (Sybase ASE) to Amazon RDS for PostgreSQL
SAP ASE (Sybase ASE) to Amazon Aurora PostgreSQL
IBM Db2 for Linux, UNIX and Windows (LUW) to Amazon RDS for PostgreSQL
IBM Db2 for Linux, UNIX and Windows (LUW) to Amazon Aurora PostgreSQL
IBM Db2 for z/OS to Amazon RDS for PostgreSQL
IBM Db2 for z/OS to Amazon Aurora PostgreSQL

## Scope of Generative AI conversion
<a name="schema-conversion-convert.databaseobjects.genai"></a>

Generative AI-assisted schema conversion focuses on specific SQL elements with designated action items. All other SQL elements are converted using default rule-based approaches. The SQL elements within the extended scope of Generative AI conversion include:




- **Oracle to Amazon RDS for PostgreSQL and Oracle to Amazon Aurora PostgreSQL**
  - **Action item:** 5578 / **Message:** AWS DMS Schema Conversion cannot convert the SELECT statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 30415 / **Message:** Your MERGE statement contains a filtering condition in the WHERE clause that is based on a value in a target table column / **Syntax element:** All occurrences except limitations
  - **Action item:** 5591 / **Message:** AWS DMS Schema Conversion cannot convert system objects / **Syntax element:** All occurrences except limitations
  - **Action item:** 5029 / **Message:** AWS DMS Schema Conversion cannot convert the usage of objects with unsupported data types / **Syntax element:** Usage of objects with the unsupported STANDARD.BFILE data type in function and procedure arguments.
  - **Action item:** 5031 / **Message:** AWS DMS Schema Conversion cannot convert CURSOR expressions / **Syntax element:** All occurrences except limitations
  - **Action item:** 5043 / **Message:** AWS DMS Schema Conversion cannot convert hierarchical queries with an asterisk in the SELECT clause / **Syntax element:** All occurrences except limitations
  - **Action item:** 5073 / **Message:** PostgreSQL does not support hierarchical queries with pseudocolumns / **Syntax element:** All occurrences except limitations
  - **Action item:** 5102 / **Message:** PostgreSQL does not support MERGE statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 5585 / **Message:** AWS DMS Schema Conversion cannot convert outer joins into correlated subqueries / **Syntax element:** All occurrences except limitations
  - **Action item:** 5608 / **Message:** AWS DMS Schema Conversion cannot convert UPDATE statements that have a subquery that returns multiple columns in the SET clause / **Syntax element:** All occurrences except limitations
  - **Action item:** 5619 / **Message:** AWS DMS Schema Conversion cannot convert system objects / **Syntax element:** All occurrences except limitations
  - **Action item:** 5852 / **Message:** PostgreSQL supports only tables as a target in the MERGE statement. / **Syntax element:** All occurrences except limitations
  - **Action item:** 5853 / **Message:** AWS DMS Schema Conversion supports only tables, views or sub-queries as a source in the USING clause of the MERGE statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 5855 / **Message:** Your MERGE statement contains a filtering condition in the WHERE clause that is based on a value in a target table column / **Syntax element:** All occurrences except limitations
  - **Action item:** 9996 / **Message:** Internal Converter error occurred / **Syntax element:** All occurrences except limitations
  - **Action item:** 9993 / **Message:** Unable to transform statement due to references to unresolved object / **Syntax element:** All occurrences except limitations
  - **Action item:** 5598 / **Message:** PostgreSQL does not support ROWID / **Syntax element:** All occurrences except limitations
  - **Action item:** 5340 / **Message:** AWS DMS Schema Conversion cannot convert functions / **Syntax element:** All occurrences except limitations
  - **Action item:** 5071 / **Message:** PostgreSQL does not support the INSERT statement for subqueries / **Syntax element:** All occurrences except limitations
  - **Action item:** 5068 / **Message:** PostgreSQL does not support the DELETE statement for subqueries / **Syntax element:** All occurrences except limitations
  - **Action item:** 5065 / **Message:** PostgreSQL does not support the UPDATE statement for subqueries / **Syntax element:** All occurrences except limitations
  - **Action item:** 5586 / **Message:** AWS DMS Schema Conversion cannot convert queries with the NOCYCLE clause / **Syntax element:** All occurrences except limitations
  - **Action item:** 5351 / **Message:** AWS DMS Schema Conversion cannot convert objects / **Syntax element:** All occurrences except limitations
  - **Action item:** 5077 / **Message:** PostgreSQL does not support the PIVOT clause for SELECT statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 5126 / **Message:** PostgreSQL does not support MODEL statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 5121 / **Message:** PostgreSQL does not support FORALL statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 5141 / **Message:** AWS DMS Schema Conversion does not support this type of conversion / **Syntax element:** All occurrences except limitations
  - **Action item:** 5142 / **Message:** AWS DMS Schema Conversion cannot convert nested calls of the same method / **Syntax element:** All occurrences except limitations
  - **Action item:** 5245 / **Message:** PostgreSQL does not support views with nested table columns / **Syntax element:** All occurrences except limitations
  - **Action item:** 5500 / **Message:** AWS DMS Schema Conversion cannot convert database mail sending / **Syntax element:** All occurrences except limitations
  - **Action item:** 5501 / **Message:** AWS DMS Schema Conversion cannot convert scheduled jobs / **Syntax element:** All occurrences except limitations
  - **Action item:** 5645 / **Message:** PostgreSQL does not support BULK COLLECT INTO clauses for several object table targets. / **Syntax element:** All occurrences except limitations
  - **Action item:** 5665 / **Message:** PostgreSQL does not support the collection data type defined with PRAGMA AUTONOMOUS\_TRANSACTION / **Syntax element:** All occurrences except limitations
  - **Action item:** 5637 / **Message:** PostgreSQL does not support bulk collect into VARRAY of VARRAY / **Syntax element:** All occurrences except limitations
  - **Action item:** 5594 / **Message:** AWS DMS Schema Conversion cannot convert date time expressions / **Syntax element:** All occurrences except limitations
  - **Action item:** 5622 / **Message:** AWS DMS Schema Conversion converts the dbms\_transaction.local\_transaction\_id function with the parameter set to true / **Syntax element:** All occurrences except limitations
  - **Action item:** 5643 / **Message:** PostgreSQL does not support BULK COLLECT INTO clauses for multilevel collection types in SELECT statements. / **Syntax element:** All occurrences except limitations
  - **Action item:** 5649 / **Message:** PostgreSQL does not support multiset operators for multilevel collection types. / **Syntax element:** All occurrences except limitations
  - **Action item:** 5651 / **Message:** AWS DMS Schema Conversion cannot convert pipelined table functions / **Syntax element:** All occurrences except limitations
  - **Action item:** 5793 / **Message:** AWS DMS Schema Conversion creates the queue with the GRANT ALL option / **Syntax element:** All occurrences except limitations
  - **Action item:** 5794 / **Message:** PostgreSQL sets the queue mode to ENABLE by default / **Syntax element:** All occurrences except limitations
  - **Action item:** 5795 / **Message:** Amazon Simple Queue Service does not support queues in the DISABLE mode / **Syntax element:** All occurrences except limitations

- **Microsoft SQL Server to Amazon RDS for PostgreSQL and Microsoft SQL Server  to Amazon Aurora PostgreSQL**
  - **Action item:** 7610 / **Message:** AWS DMS Schema Conversion cannot convert unsupported DDL statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7622 / **Message:** AWS DMS Schema Conversion cannot convert the DELETE statement using complex inline functions / **Syntax element:** All occurrences except limitations
  - **Action item:** 7624 / **Message:** AWS DMS Schema Conversion cannot convert the DELETE statement from an inline function for tables without primary keys / **Syntax element:** All occurrences except limitations
  - **Action item:** 7626 / **Message:** AWS DMS Schema Conversion cannot convert the UPDATE statement using complex inline functions / **Syntax element:** All occurrences except limitations
  - **Action item:** 7627 / **Message:** AWS DMS Schema Conversion cannot convert this syntax element / **Syntax element:** All occurrences except limitations
  - **Action item:** 7628 / **Message:** PostgreSQL does not support GOTO statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7637 / **Message:** PostgreSQL does not support global cursors / **Syntax element:** All occurrences except limitations
  - **Action item:** 7639 / **Message:** PostgreSQL does not support dynamic cursors / **Syntax element:** All occurrences except limitations
  - **Action item:** 7644 / **Message:** PostgreSQL does not support the %s clause / **Syntax element:** All occurrences except limitations
  - **Action item:** 7645 / **Message:** PostgreSQL does not support running pass-through commands on linked servers / **Syntax element:** All occurrences except limitations
  - **Action item:** 7653 / **Message:** PostgreSQL does not support GROUP BY ROLLUP clauses / **Syntax element:** All occurrences except limitations
  - **Action item:** 7654 / **Message:** PostgreSQL does not support GROUP BY CUBE clauses / **Syntax element:** All occurrences except limitations
  - **Action item:** 7655 / **Message:** PostgreSQL does not support GROUP BY GROUPING SETS clauses / **Syntax element:** All occurrences except limitations
  - **Action item:** 7672 / **Message:** PostgreSQL does not support EXECUTE statements that run a character string / **Syntax element:** All occurrences except limitations
  - **Action item:** 7683 / **Message:** MERGE is not supported if the target is a view, a materialized view, or an external table / **Syntax element:** All occurrences except limitations
  - **Action item:** 7687 / **Message:** PostgreSQL does not support CONTAINS predicates / **Syntax element:** All occurrences except limitations
  - **Action item:** 7688 / **Message:** PostgreSQL does not support FREETEXT predicates / **Syntax element:** All occurrences except limitations
  - **Action item:** 7691 / **Message:** PostgreSQL does not support the WAITFOR TIME feature / **Syntax element:** All occurrences except limitations
  - **Action item:** 7695 / **Message:** PostgreSQL does not support the call of a procedure as a variable / **Syntax element:** All occurrences except limitations
  - **Action item:** 7696 / **Message:** AWS DMS Schema Conversion cannot convert the object because the %s object is not created / **Syntax element:** All occurrences except limitations
  - **Action item:** 7708 / **Message:** AWS DMS Schema Conversion cannot convert the usage of the unsupported %s data type / **Syntax element:** All occurrences except limitations
  - **Action item:** 7709 / **Message:** AWS DMS Schema Conversion cannot convert the usage of a symmetric key / **Syntax element:** All occurrences except limitations
  - **Action item:** 7773 / **Message:** AWS DMS Schema Conversion cannot convert arithmetic operations with dates / **Syntax element:** All occurrences except limitations
  - **Action item:** 7774 / **Message:** AWS DMS Schema Conversion cannot convert arithmetic operations with mixed types of operands / **Syntax element:** All occurrences except limitations
  - **Action item:** 7794 / **Message:** PostgreSQL does not support user-defined data types / **Syntax element:** All occurrences except limitations
  - **Action item:** 7796 / **Message:** PostgreSQL does not support TOP clauses in UPDATE statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7797 / **Message:** PostgreSQL does not support the DELETED column prefix for OUTPUT clauses in UPDATE statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7798 / **Message:** PostgreSQL does not support TOP clauses in DELETE statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7799 / **Message:** PostgreSQL does not support TOP clauses in INSERT operators / **Syntax element:** All occurrences except limitations
  - **Action item:** 7804 / **Message:** PostgreSQL does not support the bitwise exclusive OR operator / **Syntax element:** All occurrences except limitations
  - **Action item:** 7805 / **Message:** PostgreSQL does not support the \!< / **Syntax element:** All occurrences except limitations
  - **Action item:** 7806 / **Message:** PostgreSQL does not support the \!> (not greater than) operator / **Syntax element:** All occurrences except limitations
  - **Action item:** 7811 / **Message:** PostgreSQL does not support the %s function. AWS DMS Schema Conversion skips this unsupported function in the converted code / **Syntax element:** All occurrences except limitations, excluding DDL
  - **Action item:** 7816 / **Message:** PostgreSQL does not support methods for the XML data type / **Syntax element:** All occurrences except limitations
  - **Action item:** 7817 / **Message:** PostgreSQL does not support the FOR XML PATH option in SQL queries / **Syntax element:** All occurrences except limitations
  - **Action item:** 7818 / **Message:** PostgreSQL does not support arithmetic operations with binary data types / **Syntax element:** All occurrences except limitations
  - **Action item:** 7819 / **Message:** PostgreSQL does not support INSERT...EXECUTE statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7820 / **Message:** PostgreSQL does not support the VALUE() method / **Syntax element:** All occurrences except limitations
  - **Action item:** 7824 / **Message:** RECURSIVE CTE is not supported for MERGE statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 7829 / **Message:** AWS DMS Schema Conversion cannot convert variable assignments with UPDATE statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7830 / **Message:** AWS DMS Schema Conversion cannot convert arithmetic operations with the CASE operand / **Syntax element:** All occurrences except limitations
  - **Action item:** 7832 / **Message:** AWS DMS Schema Conversion cannot convert INSTEAD OF triggers on views / **Syntax element:** All occurrences except limitations
  - **Action item:** 7833 / **Message:** AWS DMS Schema Conversion cannot convert the @@rowcount function in the current context / **Syntax element:** All occurrences except limitations
  - **Action item:** 7836 / **Message:** PostgreSQL does not support write operations for binary data / **Syntax element:** All occurrences except limitations
  - **Action item:** 7840 / **Message:** AWS DMS Schema Conversion cannot convert Database Console Command statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7904 / **Message:** AWS DMS Schema Conversion cannot convert the %s system object / **Syntax element:** All occurrences except limitations
  - **Action item:** 7905 / **Message:** PostgreSQL does not support PIVOT clauses for SELECT statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7906 / **Message:** PostgreSQL does not support UNPIVOT clauses for SELECT statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7909 / **Message:** AWS DMS Schema Conversion cannot convert UPDATE(column) OR COLUMNS\_UPDATED statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7916 / **Message:** AWS DMS Schema Conversion cannot emulate the MERGE statement using the INSERT ON CONFLICT statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 7917 / **Message:** PostgreSQL does not support the %s function / **Syntax element:** All occurrences except limitations
  - **Action item:** 7918 / **Message:** PostgreSQL does not support table-valued functions / **Syntax element:** All occurrences except limitations
  - **Action item:** 7919 / **Message:** PostgreSQL does not support FOR XML with the %s directive / **Syntax element:** All occurrences except limitations
  - **Action item:** 7920 / **Message:** PostgreSQL does not support EXPLICIT mode with FOR XML / **Syntax element:** All occurrences except limitations
  - **Action item:** 7925 / **Message:** PostgreSQL does not support the percent character for OPENXML flags / **Syntax element:** All occurrences except limitations
  - **Action item:** 7927 / **Message:** PostgreSQL does not support OUTER joins for self-referenced tables without a primary key / **Syntax element:** All occurrences except limitations
  - **Action item:** 7929 / **Message:** AWS DMS Schema Conversion cannot convert INSERT from EXEC statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 7939 / **Message:** AWS DMS Schema Conversion cannot convert the %s JSON system function / **Syntax element:** All occurrences except limitations
  - **Action item:** 7940 / **Message:** AWS DMS Schema Conversion cannot convert OPENJSON system table-valued functions / **Syntax element:** All occurrences except limitations
  - **Action item:** 7941 / **Message:** AWS DMS Schema Conversion cannot convert all open datasets because you have multiple open datasets / **Syntax element:** All occurrences except limitations
  - **Action item:** 9996 / **Message:** Internal Converter error occurred / **Syntax element:** All occurrences except limitations

- **SAP ASE (Sybase ASE) to Amazon RDS for PostgreSQL and SAP ASE (Sybase ASE)  to Amazon Aurora PostgreSQL**
  - **Action item:** 3014 / **Message:** Unable to convert functions / **Syntax element:** All occurrences except limitations
  - **Action item:** 3016 / **Message:** PostgreSQL does not support TOP option in the DML operator / **Syntax element:** All occurrences except limitations
  - **Action item:** 3021 / **Message:** Unable to perform an automated migration of the arithmetic operation / **Syntax element:** All occurrences except limitations
  - **Action item:** 3023 / **Message:** PostgreSQL does not support arithmetic operations with binary data types / **Syntax element:** All occurrences except limitations
  - **Action item:** 3025 / **Message:** Date/time format can be not matched / **Syntax element:** All occurrences except limitations
  - **Action item:** 3026 / **Message:** Automatic conversion of the operator WAITFOR with a variable is not supported / **Syntax element:** All occurrences except limitations
  - **Action item:** 3027 / **Message:** PostgreSQL does not support WAITFOR TIME feature / **Syntax element:** All occurrences except limitations
  - **Action item:** 3028 / **Message:** PostgreSQL does not support WAITFOR with instruction / **Syntax element:** All occurrences except limitations
  - **Action item:** 3061 / **Message:** Unable to convert system objects / **Syntax element:** All occurrences except limitations
  - **Action item:** 3064 / **Message:** In PostgreSQL you should not repeat the target table in the FROM clause of an UPDATE statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 3065 / **Message:** DELETE statement with self-reference table in the FROM clause and OUTER JOIN can not be transformed automatically / **Syntax element:** All occurrences except limitations
  - **Action item:** 3069 / **Message:** Unable to convert statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 3081 / **Message:** DMS SC can't convert unsupported DDL statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 3088 / **Message:** PostgreSQL does not support global cursors / **Syntax element:** All occurrences except limitations
  - **Action item:** 3089 / **Message:** PostgreSQL does not support dynamic cursors / **Syntax element:** All occurrences except limitations
  - **Action item:** 3121 / **Message:** DMS SC can't convert the usage of an unsupported data type / **Syntax element:** All occurrences except limitations
  - **Action item:** 3122 / **Message:** DMS SC can't convert arithmetic operations with dates / **Syntax element:** All occurrences except limitations
  - **Action item:** 3123 / **Message:** DMS SC can't convert arithmetic operations with mixed types of operands / **Syntax element:** All occurrences except limitations
  - **Action item:** 3146 / **Message:** PostgreSQL does not support the bitwise exclusive OR operator / **Syntax element:** All occurrences except limitations
  - **Action item:** 3147 / **Message:** PostgreSQL does not support the \!< (not less than) operator / **Syntax element:** All occurrences except limitations
  - **Action item:** 3148 / **Message:** PostgreSQL does not support the \!> (not greater than) operator / **Syntax element:** All occurrences except limitations
  - **Action item:** 3150 / **Message:** DMS SC can't convert functions / **Syntax element:** All occurrences except limitations
  - **Action item:** 3156 / **Message:** PostgreSQL does not support arithmetic operations with binary data types / **Syntax element:** All occurrences except limitations
  - **Action item:** 3162 / **Message:** DMS SC can't convert variable assignments with UPDATE statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 3163 / **Message:** DMS SC can't convert arithmetic operations with the CASE operand / **Syntax element:** All occurrences except limitations
  - **Action item:** 3168 / **Message:** PostgreSQL does not support write operations for binary data / **Syntax element:** All occurrences except limitations
  - **Action item:** 3172 / **Message:** DMS SC can't convert Database Console Command statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 3177 / **Message:** DMS SC can't convert system objects / **Syntax element:** All occurrences except limitations
  - **Action item:** 3182 / **Message:** DMS SC can't convert UPDATE(column) OR COLUMNS\_UPDATED statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 3190 / **Message:** DMS SC can't convert functions / **Syntax element:** All occurrences except limitations
  - **Action item:** 3191 / **Message:** PostgreSQL does not support table-valued functions / **Syntax element:** All occurrences except limitations
  - **Action item:** 9996 / **Message:** Internal Converter error occurred / **Syntax element:** All occurrences except limitations

- **IBM Db2 for Linux, UNIX and Windows (LUW) to Amazon RDS for PostgreSQL and IBM Db2 for Linux, UNIX and Windows (LUW)  to Amazon Aurora PostgreSQL**
  - **Action item:** 4506 / **Message:** PostgreSQL doesn't support view definition that contains set operations at the top level / **Syntax element:** All occurrences except limitations
  - **Action item:** 4523 / **Message:** PostgreSQL doesn't support inserting into query / **Syntax element:** All occurrences except limitations
  - **Action item:** 4524 / **Message:** PostgreSQL doesn't support returning values before calculation in insert statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 4526 / **Message:** PostgreSQL doesn't support the %s function / **Syntax element:** All occurrences except limitations
  - **Action item:** 4527 / **Message:** PostgreSQL doesn't support updating with data using query / **Syntax element:** All occurrences except limitations
  - **Action item:** 4528 / **Message:** PostgreSQL doesn't support returning values before calculation in update statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 4529 / **Message:** PostgreSQL doesn't support returning old values in update statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 4531 / **Message:** PostgreSQL doesn't support INCLUDE columns / **Syntax element:** All occurrences except limitations
  - **Action item:** 4532 / **Message:** PostgreSQL doesn't support INCLUDE columns in insert statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 4533 / **Message:** PostgreSQL doesn't support quantity restriction of rows in update statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 4534 / **Message:** PostgreSQL doesn't support deleting with data using query / **Syntax element:** All occurrences except limitations
  - **Action item:** 4536 / **Message:** PostgreSQL doesn't support quantity restriction of rows in delete statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 4537 / **Message:** PostgreSQL doesn't support period-specification clause / **Syntax element:** All occurrences except limitations
  - **Action item:** 4538 / **Message:** PostgreSQL doesn't support outer-table-reference / **Syntax element:** All occurrences except limitations
  - **Action item:** 4539 / **Message:** PostgreSQL doesn't support continue-handler clause / **Syntax element:** All occurrences except limitations
  - **Action item:** 4541 / **Message:** PostgreSQL doesn't support modules / **Syntax element:** All occurrences except limitations
  - **Action item:** 4549 / **Message:** PostgreSQL doesn't support `GOTO` statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 4556 / **Message:** PostgreSQL error code type is not a number and is incompatible with the number type variables / **Syntax element:** All occurrences except limitations
  - **Action item:** 4558 / **Message:** PostgreSQL doesn't support the typed view / **Syntax element:** All occurrences except limitations
  - **Action item:** 4559 / **Message:** PostgreSQL doesn't support the `MERGE` statement / **Syntax element:** All occurrences except limitations
  - **Action item:** 4572 / **Message:** PostgreSQL doesn't support functions that return a row with using type methods / **Syntax element:** All occurrences except limitations
  - **Action item:** 4573 / **Message:** PostgreSQL doesn't support methods invocation / **Syntax element:** All occurrences except limitations
  - **Action item:** 4575 / **Message:** PostgreSQL doesn't support CREATE GLOBAL TEMPORARY TABLE without name of schema or with name of schema - SESSION / **Syntax element:** All occurrences except limitations
  - **Action item:** 4583 / **Message:** Unable to convert system objects / **Syntax element:** All occurrences except limitations
  - **Action item:** 4597 / **Message:** PostgreSQL does not have functionality similar to UTL\_MAIL module / **Syntax element:** All occurrences except limitations
  - **Action item:** 4598 / **Message:** PostgreSQL does not have functionality similar to UTL\_SMTP module / **Syntax element:** All occurrences except limitations
  - **Action item:** 4605 / **Message:** DMS SC can't convert unsupported clauses in MERGE statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 4606 / **Message:** DMS SC can't convert MERGE statements that include unsupported clauses / **Syntax element:** All occurrences except limitations
  - **Action item:** 4612 / **Message:** PostgreSQL does not support special-register functionality / **Syntax element:** All occurrences except limitations
  - **Action item:** 9996 / **Message:** Internal Converter error occurred / **Syntax element:** All occurrences except limitations

- **IBM Db2 for z/OS to Amazon RDS for PostgreSQL and IBM Db2 for z/OS  to Amazon Aurora PostgreSQL**
  - **Action item:** 8507 / **Message:** PostgreSQL does not support the %s function / **Syntax element:** All occurrences except limitations
  - **Action item:** 8519 / **Message:** FETCH clause is not supported / **Syntax element:** All occurrences except limitations
  - **Action item:** 8521 / **Message:** Positioned deletes are not supported / **Syntax element:** All occurrences except limitations
  - **Action item:** 8542 / **Message:** PostgreSQL doesn’t support default namespaces / **Syntax element:** All occurrences except limitations
  - **Action item:** 8559 / **Message:** DMS SC can’t convert MERGE statements that include unsupported clauses / **Syntax element:** All occurrences except limitations
  - **Action item:** 8560 / **Message:** PostgreSQL doesn’t support the usage of variables or parameters in RAISE statements / **Syntax element:** All occurrences except limitations
  - **Action item:** 8563 / **Message:** PostgreSQL uses different format for interval data types compared to Db2 for z/OS / **Syntax element:** All occurrences except limitations
  - **Action item:** 8566 / **Message:** DMS SC can’t convert bulk and backward data fetching from a cursor / **Syntax element:** All occurrences except limitations
  - **Action item:** 8570 / **Message:** DMS SC can’t convert MERGE statements in FINAL TABLE table references / **Syntax element:** All occurrences except limitations
  - **Action item:** 8581 / **Message:** DMS SC can’t convert UPDATE statements that include unsupported clauses / **Syntax element:** All occurrences except limitations
  - **Action item:** 9996 / **Message:** Internal Converter error occurred / **Syntax element:** All occurrences except limitations



### Limitations
<a name="schema-conversion-convert.databaseobjects.limitations"></a>

The Converting database objects with generative AI feature has the following limitations:
+ Database endpoints supporting generative AI conversion are not visible in the AWS Console. You can view them only by exporting the assessment report as a PDF or CSV file.
+ As a probabilistic system, generative AI-assisted Schema Conversion may not achieve 100 percent accuracy in all conversions. It can also produce different results for the same SQL statements over a period of time. You must review and validate all conversion outputs.
+ Generative AI conversion is not supported for:
  + DEFAULT constraint in a table
  + DEFAULT value for a function or procedure parameter
  + COMPUTE COLUMN in a table
  + TRIGGER
  + COLUMN DATA TYPE
  + Dynamic SQL
  + INDEX
  + CONSTRAINT
+ If the source statement is converted with multiple action items and at least one action item is processed using generative AI, then all Action Items are replaced by one action item 5444 on a target for Oracle and 7744 for Microsoft SQL Server. The action item 9997 is an exception that is saved after processed using generative AI.

**Warning**  
Conversion using generative AI takes longer than basic conversion.

Every AWS account have a per-minute quota limiting the number of SQL statements that can be converted using generative AI. Statements exceeding this limit are queued for processing in subsequent minutes. The quota is as follows:



| Region | SQL Statements per AWS account per minute | 
| --- | --- | 
| Asia Pacific (Tokyo) (ap-northeast-1)<br />Asia Pacific (Osaka) (ap-northeast-3)<br />Asia Pacific (Sydney) (ap-southeast-2)<br />Canada (Central) (ca-central-1)<br />Europe (Zurich) (eu-central-2)<br />Europe (Stockholm) (eu-north-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Spain) (eu-south-2)<br />Europe (Ireland) (eu-west-1)<br />Europe (London) (eu-west-2)<br />Europe (Paris) (eu-west-3)<br />US East (Ohio) (us-east-2) | Up to 48 statements | 
| Europe (Frankfurt) (eu-central-1)<br />US East (N. Virginia) (us-east-1)<br />US West (Oregon) (us-west-2) | Up to 80 statements | 