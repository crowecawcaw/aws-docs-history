# Overcome the 68k code block size limit

Athena for Spark has a known calculation code block size limit of 68000 characters. When
you run a calculation with a code block over this limit, you can receive the following error
message:

**`'...' at 'codeBlock' failed to satisfy constraint: Member must have length
 less than or equal to 68000`**

The following image shows this error in the Athena console notebook editor.

![Code block size error message in the Athena notebook editor](images/notebooks-spark-troubleshooting-code-block-size-limit-1.png)
The same error can occur when you use the AWS CLI to run a calculation that has a large code
block, as in the following example.

```
aws athena start-calculation-execution \
    --session-id "`{SESSION_ID}`" \
    --description "`{SESSION_DESCRIPTION}`" \
    --code-block "`{LARGE_CODE_BLOCK}`"
```

The command gives the following error message:

**``{LARGE_CODE_BLOCK}` at 'codeBlock' failed to satisfy
constraint: Member must have length less than or equal to 68000`**

## Workaround

To work around this issue, upload the file that has your query or calculation code to
Amazon S3. Then, use boto3 to read the file and run your SQL or code.

The following examples assume that you have already uploaded the file that has your
SQL query or Python code to Amazon S3.

### SQL example

The following example code reads the `large_sql_query.sql` file
from an Amazon S3 bucket and then runs the large query that the file contains.

```
s3 = boto3.resource('s3')
def read_s3_content(`bucket_name`, `key`):
    response = s3.Object(`bucket_name`, `key`).get()
    return response['Body'].read()

# SQL
sql = read_s3_content('`bucket_name`', 'large_sql_query.sql')
df = spark.sql(sql)
```

### PySpark example

The following code example reads the `large_py_spark.py` file
from Amazon S3 and then runs the large code block that is in the file.

```
s3 = boto3.resource('s3')

def read_s3_content(`bucket_name`, `key`):
    response = s3.Object(`bucket_name`, `key`).get()
    return response['Body'].read()

# PySpark
py_spark_code = read_s3_content('`bucket_name`', 'large_py_spark.py')
exec(py_spark_code)
```
