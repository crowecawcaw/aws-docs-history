# Oracle UTL_FILE and MySQL integration with Amazon S3

With AWS DMS, you can seamlessly migrate Oracle databases utilizing `UTL_FILE` and MySQL databases with Amazon S3 integration to AWS. The following sections outline the steps to configure and utilize `UTL_FILE` with Oracle and MySQL integration with Amazon S3 through AWS DMS.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                              |
| ------------------------------ | ---------------------------------- | ------------------------- | -------------------------------------------------------------------------------------------- |
| Two star feature compatibility | No automation                      | N/A                       | MySQL doesn’t support `UTL_FILE` but Aurora MySQL has a built-in integration with Amazon S3. |

## Oracle usage

Oracle `UTL_FILE` PL/SQL package enables you to access files stored outside of the database such as files stored on the operating system, the database server, or a connected storage volume. `UTL_FILE.FOPEN`, `UTL_FILE.GET_LINE`, and `UTL_FILE.PUT_LINE` are procedures within the `UTL_FILE` package used to open, read, and write files.

### Examples

Run an anonymous PL/SQL block that reads a single line from file1 and writes it to file2.

- Use `UTL_FILE.FILE_TYPE` to create a handle for the file.
- Use `UTL_FILE.FOPEN` to open stream access to the file and specify:
  - The logical Oracle directory object pointing to the O/S folder where the file resides.
  - The file name.
  - The file access mode: 'A'=append mode, 'W'=write mode

- Use `UTL_FILE.GET_LINE` to read a line from the input file into a variable.
- Use `UTL_FILE.PUT_LINE` to write a single line to the output file.

```
DECLARE
strString1 VARCHAR2(32767);
fileFile1 UTL_FILE.FILE_TYPE;
BEGIN
fileFile1 := UTL_FILE.FOPEN('FILES_DIR','File1.tmp','R');
UTL_FILE.GET_LINE(fileFile1,strString1);
UTL_FILE.FCLOSE(fileFile1);
fileFile1 := UTL_FILE.FOPEN('FILES_DIR','File2.tmp','A');
utl_file.PUT_LINE(fileFile1,strString1);
utl_file.fclose(fileFile1);
END;
/
```

For more information, see [UTL_FILE](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_FILE.html#GUID-EBC42A36-EB72-4AA1-B75F-8CF4BC6E29B4 "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_FILE.html#GUID-EBC42A36-EB72-4AA1-B75F-8CF4BC6E29B4") in the _Oracle documentation_.

## MySQL usage

Aurora MySQL provides similar functionality to Oracle `UTL_FILE` with Amazon S3 integration.

There two important integration aspects between Aurora MySQL and Amazon S3:

- Saving data to an S3 file.
- Loading data from an S3 file.

###### Note

Make sure that Aurora MySQL has permissions to the S3 bucket.

### Saving data to Amazon S3

You can use the `SELECT INTO OUTFILE S3` statement to query data from an Amazon Aurora MySQL DB cluster and save it directly to text files stored in an Amazon S3 bucket. You can use this approach to avoid transferring data first to the client and then copying the data from the client to Amazon S3.

###### Note

The default file size threshold is 6 GB. If the data selected by the statement is less than the file size threshold, a single file is created. Otherwise, multiple files are created.

If the `SELECT` statement failed, files already uploaded to Amazon S3 remain in the specified Amazon S3 bucket. You can use another statement to upload the remaining data instead of starting over.

If the amount of data to be selected is more than 25 GB, it is recommended to use multiple `SELECT INTO OUTFILE S3` statements to save the data to Amazon S3.

Metadata, such as table schema or file metadata, isn’t uploaded by Aurora MySQL to Amazon S3.

#### Examples

The following statement selects all data in the employees table and saves it to an Amazon S3 bucket in a different region from the Aurora MySQL DB cluster. The statement creates data files in which each field is terminated by a comma `,` character and each row is terminated by a newline `\n` character. The statement returns an error if files that match the `sample_employee_data` file prefix already exist in the specified Amazon S3 bucket.

```
SELECT * FROM employees INTO OUTFILE S3
's3-us-west-2://aurora-select-into-s3-pdx/sample_employee_data'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
```

The following statement selects all data in the employees table and saves the data to an Amazon S3 bucket in the same region as the Aurora MySQL DB cluster. The statement creates data files in which each field is terminated by a comma `,` character and each row is terminated by a newline `\n` character. It also creates a manifest file. The statement returns an error if files that match the `sample_employee_data` file prefix already exist in the specified Amazon S3 bucket.

```
SELECT * FROM employees INTO OUTFILE S3
's3://aurora-select-into-s3-pdx/sample_employee_data'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
MANIFEST ON;
```

The following statement selects all data in the employees table and saves the data to an Amazon S3 bucket in a different region from the Aurora database cluster. The statement creates data files in which each field is terminated by a comma `,` character and each row is terminated by a newline `\n` character. The statement overwrites any existing files that match the `sample_employee_data` file prefix in the specified Amazon S3 bucket.

```
SELECT * FROM employees INTO OUTFILE S3 '
s3-us-west-2://aurora-select-into-s3-pdx/sample_employee_data'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' OVERWRITE ON;
```

The following statement selects all data in the employees table and saves the data to an Amazon S3 bucket in the same region as the Aurora MySQL DB cluster. The statement creates data files in which each field is terminated by a comma `,` character and each row is terminated by a newline `\n` character. It also creates a manifest file. The statement overwrites any existing files that match the `sample_employee_data` file prefix in the specified Amazon S3 bucket.

```
SELECT * FROM employees INTO OUTFILE S3
's3://aurora-select-into-s3-pdx/sample_employee_data'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
MANIFEST ON OVERWRITE ON;
```

For more information, see [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3 bucket](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md") in the _User Guide for Aurora_.

### Load XML from Amazon S3

Use the `LOAD DATA FROM S3` or `LOAD XML FROM S3` statement to load data from files stored in an Amazon S3 bucket.

The `LOAD DATA FROM S3` statement can load data from any text file format supported by the MySQL `LOAD DATA INFILE` statement such as comma-delimited text data. Compressed files are not supported.

#### Examples

The following example runs the `LOAD DATA FROM S3` statement with the manifest file named `customer.manifest`. After the statement completes, an entry for each successfully loaded file is written to the `aurora_s3_load_history` table.

```
LOAD DATA FROM S3 MANIFEST
's3-us-west-2://aurora-bucket/customer.manifest'
INTO TABLE CUSTOMER FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(ID, FIRSTNAME, LASTNAME, EMAIL);
```

Every successful `LOAD DATA FROM S3` statement updates the `aurora_s3_load_history` table in the `mysql` schema with an entry for each file that was loaded.

After you run the `LOAD DATA FROM S3` statement, you can verify which files were loaded by querying the `aurora_s3_load_history` table. To see the files that were loaded from one execution of the statement, use the `WHERE` clause to filter the records on the Amazon S3 URI for the manifest file used in the statement. If you have used the same manifest file before, filter the results using the timestamp field.

```
select * from mysql.aurora_s3_load_history where load_prefix = 'S3_URI';
```

The following table describes the fields in the `aurora_s3_load_history` table.

| Field          | Description                                                                                                                                                                                                                                                                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| load_prefix    | The URI specified in the load statement. This URI can map to any of the following:<br>• A single data file for a `LOAD DATA FROM S3 FILE` statement.<br>• An Amazon S3 prefix that maps to multiple data files for a `LOAD DATA FROM S3 PREFIX` statement.<br>• A single manifest file containing the names of files to be loaded for a `LOAD DATA FROM S3 MANIFEST` statement. |
| file_name      | The name of a file that was loaded into Aurora from Amazon S3 using the URI identified in the `load_prefix` field.                                                                                                                                                                                                                                                              |
| version_number | The version number of the file identified by the `file_name` field that was loaded if the Amazon S3 bucket has a version number.                                                                                                                                                                                                                                                |
| bytes_loaded   | The size in bytes of the file loaded.                                                                                                                                                                                                                                                                                                                                           |
| load_timestamp | The timestamp when the `LOAD DATA FROM S3` statement completed.                                                                                                                                                                                                                                                                                                                 |

The following statement loads data from an Amazon S3 bucket in the same region as the Aurora DB cluster. It reads the comma-delimited data in the `customerdata.txt` file residing in the `dbbucket` Amazon S3 bucket and then loads the data into the table `store-schema.customer-table`.

```
LOAD DATA FROM S3 's3://dbbucket/customerdata.csv'
INTO TABLE store-schema.customer-table
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
(ID, FIRSTNAME, LASTNAME, ADDRESS, EMAIL, PHONE);
```

The following statement loads data from an Amazon S3 bucket in a different region from the Aurora DB cluster. The statement reads the comma-delimited data from all files that match the `employee-data` object prefix in the `my-data` Amazon S3 bucket in the us-west-2 region and then loads the data into the employees table.

```
LOAD DATA FROM S3 PREFIX
's3-us-west-2://my-data/employee_data'
INTO TABLE employees
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(ID, FIRSTNAME, LASTNAME, EMAIL, SALARY);
```

The following statement loads data from the files specified in a JSON manifest file named `q1_sales.json` into the sales table.

```
LOAD DATA FROM S3 MANIFEST
's3-us-west-2://aurora-bucket/q1_sales.json'
INTO TABLE sales FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' (MONTH, STORE, GROSS, NET);
```

You can use the `LOAD XML FROM S3` statement to load data from XML files stored on an Amazon S3 bucket in one of three different XML formats as described below.

Column names as attributes of a `<row>` element. The attribute value identifies the contents of the table field.

```
<row column1="value1" column2="value2" .../>
```

Column names as child elements of a `<row>` element. The value of the child element identifies the contents of the table field.

```
<row>
<column1>value1</column1>
<column2>value2</column2>
</row>
```

Column names in the name attribute of `<field>` elements in a `<row>` element. The value of the `<field>` element identifies the contents of the table field.

```
<row>
<field name='column1'>value1</field>
<field name='column2'>value2</field>
</row>
```

The following statement loads the first column from the input file into the first column of table1 and sets the value of the table_column2 column in table1 to the input value of the second column divided by 100.

```
LOAD XML FROM S3 's3://mybucket/data.xml'
INTO TABLE table1 (column1, @var1)
SET table_column2 = @var1/100;
```

The following statement sets the first two columns of table1 to the values in the first two columns from the input file and then sets the value of the column3 in table1 to the current time stamp.

```
LOAD XML FROM S3 's3://mybucket/data.xml'
INTO TABLE table1 (column1, column2)
SET column3 = CURRENT_TIMESTAMP;
```

You can use subqueries in the right side of `SET` assignments. For a subquery that returns a value to be assigned to a column, you can use only a scalar subquery. Also, you cannot use a subquery to select from the table that is being loaded.

For more information, see [Loading data into an Amazon Aurora MySQL DB cluster from text files in an Amazon S3 bucket](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md") in the _User Guide for Aurora_.
