

# Oracle external tables and MySQL integration with Amazon S3
<a name="chap-oracle-aurora-mysql.special.external"></a>

With AWS DMS, you can integrate Oracle databases and MySQL databases with Amazon S3 using external tables and the AWS-developed MySQL integration. External tables allow Oracle databases to directly access and query data stored in Amazon S3, while the MySQL integration lets MySQL databases treat Amazon S3 as a storage engine.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Creating Tables](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.tables)  | Use Aurora MySQL integration with Amazon S3. Different paradigm and syntax. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.special.external.oracle"></a>

The Oracle external tables feature allows you to create a table in your database that reads data from a source located outside your database (externally).

Beginning with Oracle 12.2, the external table can be partitioned, providing all the benefits of a regular partitioned table.

Oracle 18c adds support for inline external tables, which is a way to get data from external source in a SQL query without having to define and create external table first.

```
SELECT * FROM EXTERNAL ((i NUMBER, d DATE)
TYPE ORACLE_LOADER
DEFAULT DIRECTORY data_dir
ACCESS PARAMETERS (
RECORDS DELIMITED BY NEWLINE
FIELDS TERMINATED BY '|')
LOCATION ('test.csv')
REJECT LIMIT UNLIMITED)
tst_external;
```

### Examples
<a name="chap-oracle-aurora-mysql.special.external.oracle.examples"></a>

Use `CREATE TABLE` with `ORGANIZATION EXTERNAL` to identify it as an external table. Specify the `TYPE` to let the database choose the right driver for the data source, the options are:
+  `ORACLE_LOADER` — The data must be sourced from text data files. This is the default option.
+  `ORACLE_DATAPUMP` — The data must be sourced from binary dump files. You can write dump files only as part of creating an external table with the `CREATE TABLE AS SELECT` statement. Once the dump file is created, it can be read any number of times, but it can’t be modified. This means that no DML operations can be performed.
+  `ORACLE_HDFS` — Extracts data stored in a Hadoop Distributed File System (HDFS).
+  `ORACLE_HIVE` — Extracts data stored in Apache HIVE.
+  `DEFAULT DIRECTORY` — In database definition for the directory path.
+  `ACCESS PARAMETER` — Defines the delimiter character and the query fields.
+  `LOCATION` — The file name in the first two data source types or URI in the Hadoop data source (not in use with hive data source).

```
CREATE TABLE emp_load
(id CHAR(5), emp_dob CHAR(20), emp_lname CHAR(30),
  emp_fname CHAR(30),emp_start_date DATE) ORGANIZATION EXTERNAL
(TYPE ORACLE_LOADER DEFAULT DIRECTORY data_dir ACCESS PARAMETERS
(RECORDS DELIMITED BY NEWLINE FIELDS (id CHAR(2), emp_dob CHAR(20),
  emp_lname CHAR(18), emp_fname CHAR(11), emp_start_date CHAR(10)
  date_format DATE mask "mm/dd/yyyy"))
LOCATION ('info.dat'));
```

For more information, see [External Tables Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/18/sutil/oracle-external-tables-concepts.html#GUID-44323E01-7D72-45EC-915A-99E596769D9E) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.special.external.mysql"></a>

Aurora MySQL has a capability similar to Oracle’s External Tables, but requires a significant amount of syntax modifications. The main difference is that there is no open link to files and the data must be transferred from and to MySQL if you need all data.

There are two important operations for MySQL and S3 integration:
+ Saving data to an S3 file.
+ Loading data from an S3 file.

Aurora MySQL must have permissions to the S3 bucket.

In Oracle 18c, the inline external table feature was introduced. This cannot be achieved in Aurora for MySQL and it depends on the use case but other services can be considered. For ETLs, for example, AWS Glue can be considered.

### Saving data to Amazon S3
<a name="chap-oracle-aurora-mysql.special.external.mysql.save"></a>

You can use the `SELECT INTO OUTFILE S3` statement to query data from an Amazon Aurora MySQL DB cluster and save it directly into text files stored in an Amazon S3 bucket. Use this functionality to avoid transferring data to the client first, and then copying the data from the client to Amazon S3.

**Note**  
The default file size threshold is six gigabytes (GB). If the data selected by the statement is less than the file size threshold, a single file is created. Otherwise, multiple files are created.

If the `SELECT` statement fails, files that are already uploaded to Amazon S3 remain in the specified Amazon S3 bucket. You can use another statement to upload the remaining data instead of starting over again.

If the amount of data to be selected is more than 25 GB, it is recommended to use multiple `SELECT INTO OUTFILE S3` statements to save data to Amazon S3.

Metadata, such as table schema or file metadata, isn’t uploaded by Aurora MySQL to Amazon S3.

 **Examples** 

The following statement selects all data in the employees table and saves the data into an Amazon S3 bucket in a different region from the Aurora MySQL DB cluster. The statement creates data files in which each field is terminated by a comma `,` character and each row is terminated by a newline `\n` character. The statement returns an error if files that match the `sample_employee_data` file prefix exist in the specified Amazon S3 bucket.

```
SELECT * FROM employees INTO OUTFILE S3
's3-us-west-2://aurora-select-into-s3-pdx/sample_employee_data'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
```

The following statement selects all data in the employees table and saves the data into an Amazon S3 bucket in the same region as the Aurora MySQL DB cluster. The statement creates data files in which each field is terminated by a comma `,` character and each row is terminated by a newline `\n` character. It also creates a manifest file. The statement returns an error if files that match the `sample_employee_data` file prefix exist in the specified Amazon S3 bucket.

```
SELECT * FROM employees INTO OUTFILE S3
's3://aurora-select-into-s3-pdx/sample_employee_data'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
MANIFEST ON;
```

The following statement selects all data in the employees table and saves the data into an Amazon S3 bucket in a different region from the Aurora DB cluster. The statement creates data files in which each field is terminated by a comma `,` character and each row is terminated by a newline `\n` character. The statement overwrites any existing files that match the `sample_employee_data` file prefix in the specified Amazon S3 bucket.

```
SELECT * FROM employees INTO OUTFILE S3
's3-us-west-2://aurora-select-into-s3-pdx/sample_employee_data'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' OVERWRITE ON;
```

The following statement selects all data in the employees table and saves the data into an Amazon S3 bucket in the same region as the Aurora MySQL DB cluster. The statement creates data files in which each field is terminated by a comma `,` character and each row is terminated by a newline `\n` character. It also creates a manifest file. The statement overwrites any existing files that match the `sample_employee_data` file prefix in the specified Amazon S3 bucket.

```
SELECT * FROM employees INTO OUTFILE S3
's3://aurora-select-into-s3-pdx/sample_employee_data'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
MANIFEST ON OVERWRITE ON;
```

For more information, see [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.SaveIntoS3.html) in the *User Guide for Aurora*.

### Loading data from Amazon S3
<a name="chap-oracle-aurora-mysql.special.external.mysql.load"></a>

You can use the `LOAD DATA FROM S3` or `LOAD XML FROM S3` statement to load data from files stored in an Amazon S3 bucket.

Also, you can use the `LOAD DATA FROM S3` statement to load data from any text file format supported by the MySQL `LOAD DATA INFILE` statement such as comma-delimited text data. Compressed files aren’t supported.

 **Examples** 

The following example runs the `LOAD DATA FROM S3` statement with the manifest from the previous example. This manifest has the `customer.manifest` name. After the statement completes, an entry for each successfully loaded file is written to the `aurora_s3_load_history` table.

```
LOAD DATA FROM S3 MANIFEST
's3-us-west-2://aurora-bucket/customer.manifest'
INTO TABLE CUSTOMER FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(ID, FIRSTNAME, LASTNAME, EMAIL);
```

Each successful `LOAD DATA FROM S3` statement updates the `aurora_s3_load_history` table in the mysql schema with an entry for each file loaded.

After you run the `LOAD DATA FROM S3` statement, you can verify which files were loaded by querying the `aurora_s3_load_history` table. To see the files that were loaded from one execution of the statement, use the `WHERE` clause to filter the records on the Amazon S3 URI for the manifest file used in the statement. If you have used the same manifest file before, filter the results using the timestamp field.

```
select * from mysql.aurora_s3_load_history
  where load_prefix = 'S3_URI';
```

The following table describes the fields in the `aurora_s3_load_history` table:


| Field | Description | 
| --- | --- | 
| load\_prefix | The URI specified in the load statement. This URI can map to any of the following:+  A single data file for a `LOAD DATA FROM S3 FILE` statement. <br />+  An Amazon S3 prefix that maps to multiple data files for a `LOAD DATA FROM S3 PREFIX` statement. <br />+  A single manifest file containing the names of files to be loaded for a `LOAD DATA FROM S3 MANIFEST` statement.  | 
| file\_name | The name of a file loaded into Aurora from Amazon S3 using the URI identified in the `load_prefix` field. | 
| version\_number | The version number of the file identified by the file\_name field that was loaded if the Amazon S3 bucket has a version number. | 
| bytes\_loaded | The size of the file loaded in bytes. | 
| load\_timestamp | The timestamp when the `LOAD DATA FROM S3` statement completed. | 

 **Examples** 

The following statement loads data from an Amazon S3 bucket in the same region as the Aurora DB cluster. The statement reads the comma-delimited data in the `customerdata.txt` file in the `dbbucket` Amazon S3 bucket and then loads the data into the `store-schema.customer-table` table.

```
LOAD DATA FROM S3 's3://dbbucket/customerdata.csv'
INTO TABLE store-schema.customer-table
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(ID, FIRSTNAME, LASTNAME, ADDRESS, EMAIL, PHONE);
```

The following statement loads data from an Amazon S3 bucket in a different region from the Aurora DB cluster. The statement reads the comma-delimited data from all files matching the `employee-data` object prefix in the `mydata` Amazon S3 bucket in the us-west-2 region and then loads data into the `employees` table.

```
LOAD DATA FROM S3 PREFIX
's3-us-west-2://my-data/employee_data'
INTO TABLE employees
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(ID, FIRSTNAME, LASTNAME, EMAIL, SALARY);
```

The following statement loads data from the files specified in a JSON manifest file named `q1_sales.json` into the `sales` table.

```
LOAD DATA FROM S3 MANIFEST
's3-us-west-2://aurora-bucket/q1_sales.json'
INTO TABLE sales
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(MONTH, STORE, GROSS, NET);
```

### Loading XML FROM S3
<a name="chap-oracle-aurora-mysql.special.external.mysql.loadxml"></a>

You can use the `LOAD XML FROM S3` statement to load data from XML files stored on an Amazon S3 bucket in one of three different XML formats as shown following.

Column names are attributes of a `<row>` element. The attribute value identifies the contents of the table field.

```
<row column1="value1" column2="value2" .../>
```

Column names are child elements of a `<row>` element. The value of the child element identifies the contents of the table field.

```
<row>
<column1>value1</column1>
<column2>value2</column2>
</row>
```

Column names are in the name attribute of `<field>` elements in a `<row>` element. The value of the `<field>` element identifies the contents of the table field.

```
<row>
<field name='column1'>value1</field>
<field name='column2'>value2</field>
</row>
```

The following statement loads the first column from the input file into the first column of table1 and sets the value of the `table_column2` column in `table1` to the input the value of the second column divided by 100.

```
LOAD XML FROM S3
's3://mybucket/data.xml'
INTO TABLE table1 (column1, @var1)
SET table_column2 = @var1/100;
```

The following statement sets the first two columns of `table1` to the values in the first two columns from the input file and then sets the value of the column3 in `table1` to the current time stamp.

```
LOAD XML FROM S3
's3://mybucket/data.xml'
INTO TABLE table1 (column1, column2)
SET column3 = CURRENT_TIMESTAMP;
```

You can use subqueries in the right side of `SET` assignments. For a subquery that returns a value to be assigned to a column, you can use only a scalar subquery. Also, you can’t use a subquery to select from the table that is being loaded.

For more information, see [Loading data into an Amazon Aurora MySQL DB cluster from text files in an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.LoadFromS3.html) in the *Amazon RDS user guide*.