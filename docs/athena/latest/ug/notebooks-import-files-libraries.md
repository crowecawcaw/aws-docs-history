# Import files and Python libraries to Athena for Spark

This document provides examples of how to import files and Python libraries to Amazon Athena
for Apache Spark.

## Considerations and Limitations

- Python version – Currently, Athena for
  Spark uses Python version 3.9.16. Note that Python packages are sensitive to
  minor Python versions.
- Athena for Spark architecture – Athena for
  Spark uses Amazon Linux 2 on ARM64 architecture. Note that some Python libraries
  do not distribute binaries for this architecture.
- Binary shared objects (SOs) – Because
  the SparkContext [addPyFile](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.addPyFile.html "https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.addPyFile.html") method does not detect binary shared objects, it cannot
  be used in Athena for Spark to add Python packages that depend on shared
  objects.
- Resilient Distributed Datasets (RDDs) –
  [RDDs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html "https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html") are not supported.
- Dataframe.foreach – The PySpark [DataFrame.foreach](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.foreach.html "https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.foreach.html") method is not supported.

## Examples

The examples use the following conventions.

- The placeholder Amazon S3 location `s3://amzn-s3-demo-bucket`.
  Replace this with your own S3 bucket location.
- All code blocks that execute from a Unix shell are shown as
  `directory_name`
  `$`. For example, the command `ls` in the directory
  `/tmp` and its output are displayed as follows:

```
/tmp $ ls
```

**Output**

```
file1 file2
```

## Import text files for use in calculations

The examples in this section show how to import text files for use in calculations in
your notebooks in Athena for Spark.

The following example shows how to write a file to a local temporary
directory, add it to a notebook, and test it.

```
import os
from pyspark import SparkFiles
tempdir = '/tmp/'
path = os.path.join(tempdir, "test.txt")
with open(path, "w") as testFile:
    _ = testFile.write("5")
sc.addFile(path)

def func(iterator):
    with open(SparkFiles.get("test.txt")) as testFile:
        fileVal = int(testFile.readline())
        return [x * fileVal for x in iterator]

#Test the file
from pyspark.sql.functions import udf
from pyspark.sql.functions import col

udf_with_import = udf(func)
df = spark.createDataFrame([(1, "a"), (2, "b")])
df.withColumn("col", udf_with_import(col('_2'))).show()
```

**Output**

```
Calculation completed.
+---+---+-------+
| _1| _2|    col|
+---+---+-------+
|  1|  a|[aaaaa]|
|  2|  b|[bbbbb]|
+---+---+-------+
```

The following example shows how to import a file from Amazon S3 into a notebook and
test it.

###### To import a file from Amazon S3 into a notebook

1. Create a file named `test.txt` that has a single
   line that contains the value `5`.
2. Add the file to a bucket in Amazon S3. This example uses the location
   `s3://amzn-s3-demo-bucket`.
3. Use the following code to import the file to your notebook and test
   the file.

```
from pyspark import SparkFiles
sc.addFile('s3://amzn-s3-demo-bucket/test.txt')

def func(iterator):
   with open(SparkFiles.get("test.txt")) as testFile:
       fileVal = int(testFile.readline())
       return [x * fileVal for x in iterator]

#Test the file
from pyspark.sql.functions import udf
from pyspark.sql.functions import col

udf_with_import = udf(func)
df = spark.createDataFrame([(1, "a"), (2, "b")])
df.withColumn("col", udf_with_import(col('_2'))).show()
```

**Output**

```
Calculation completed.
+---+---+-------+
| _1| _2|    col|
+---+---+-------+
|  1|  a|[aaaaa]|
|  2|  b|[bbbbb]|
+---+---+-------+
```

## Add Python files

The examples in this section show how to add Python files and libraries to your Spark
notebooks in Athena.

The following example shows how to add Python files from Amazon S3 to your
notebook and register a UDF.

###### To add Python files to your notebook and register a UDF

1. Using your own Amazon S3 location, create the file
   `s3://amzn-s3-demo-bucket/file1.py` with the
   following contents:

```
def xyz(input):
    return 'xyz  - udf ' + str(input);
```

2. In the same S3 location, create the file
   `s3://amzn-s3-demo-bucket/file2.py` with the
   following contents:

```
from file1 import xyz
def uvw(input):
    return 'uvw -> ' + xyz(input);
```

3. In your Athena for Spark notebook, run the following commands.

```
sc.addPyFile('s3://amzn-s3-demo-bucket/file1.py')
sc.addPyFile('s3://amzn-s3-demo-bucket/file2.py')

def func(iterator):
    from file2 import uvw
    return [uvw(x) for x in iterator]

from pyspark.sql.functions import udf
from pyspark.sql.functions import col

udf_with_import = udf(func)

df = spark.createDataFrame([(1, "a"), (2, "b")])

df.withColumn("col", udf_with_import(col('_2'))).show(10)
```

**Output**

```
Calculation started (calculation_id=1ec09e01-3dec-a096-00ea-57289cdb8ce7) in (session=c8c09e00-6f20-41e5-98bd-4024913d6cee). Checking calculation status...
Calculation completed.
+---+---+--------------------+
| _1| _2|                 col|
+---+---+--------------------+
| 1 |  a|[uvw -> xyz - ud... |
| 2 |  b|[uvw -> xyz - ud... |
+---+---+--------------------+
```

You can use the Python `addPyFile` and `import` methods
to import a Python .zip file to your notebook.

###### Note

The `.zip` files that you import to Athena Spark may
include only Python packages. For example, including packages with C-based
files is not supported.

###### To import a Python `.zip` file to your notebook

1. On your local computer, in a desktop directory such as
   `\tmp`, create a directory called
   `moduletest`.
2. In the `moduletest` directory, create a file named
   `hello.py` with the following contents:

```
def hi(input):
    return 'hi ' + str(input);
```

3. In the same directory, add an empty file with the name
   `__init__.py`.

If you list the directory contents, they should now look like the
following.

```
/tmp $ ls moduletest
__init__.py       hello.py
```

4. Use the `zip` command to place the two module files into a
   file called `moduletest.zip`.

```
moduletest $ zip -r9 ../moduletest.zip *
```

5. Upload the `.zip` file to your bucket in
   Amazon S3.
6. Use the following code to import the Python`.zip`
   file into your notebook.

```
sc.addPyFile('s3://amzn-s3-demo-bucket/moduletest.zip')

from moduletest.hello import hi

from pyspark.sql.functions import udf
from pyspark.sql.functions import col

hi_udf = udf(hi)

df = spark.createDataFrame([(1, "a"), (2, "b")])

df.withColumn("col", hi_udf(col('_2'))).show()
```

**Output**

```
Calculation started (calculation_id=6ec09e8c-6fe0-4547-5f1b-6b01adb2242c) in (session=dcc09e8c-3f80-9cdc-bfc5-7effa1686b76). Checking calculation status...
Calculation completed.
+---+---+----+
| _1| _2| col|
+---+---+----+
|  1|  a|hi a|
|  2|  b|hi b|
+---+---+----+
```

The following code examples show how to add and import two different versions
of a Python library from a location in Amazon S3 as two separate modules. The code
adds each the library file from S3, imports it, and then prints the library
version to verify the import.

```
sc.addPyFile('s3://amzn-s3-demo-bucket/python-third-party-libs-test/simplejson_v3_15.zip')
sc.addPyFile('s3://amzn-s3-demo-bucket/python-third-party-libs-test/simplejson_v3_17_6.zip')

import simplejson_v3_15
print(simplejson_v3_15.__version__)
```

**Output**

```
3.15.0
```

```
import simplejson_v3_17_6
print(simplejson_v3_17_6.__version__)
```

**Output**

```
3.17.6
```

This example uses the `pip` command to download a Python .zip file
of the [bpabel/piglatin](https://github.com/bpabel/piglatin "https://github.com/bpabel/piglatin")
project from the [Python Package Index
(PyPI)](https://pypi.org/ "https://pypi.org/").

###### To import a Python .zip file from PyPI

1. On your local desktop, use the following commands to create a
   directory called `testpiglatin` and create a virtual
   environment.

```
/tmp $ mkdir testpiglatin
/tmp $ cd testpiglatin
testpiglatin $ virtualenv .
```

**Output**

```
created virtual environment CPython3.9.6.final.0-64 in 410ms
creator CPython3Posix(dest=/private/tmp/testpiglatin, clear=False, no_vcs_ignore=False, global=False)
seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/user1/Library/Application Support/virtualenv)
added seed packages: pip==22.0.4, setuptools==62.1.0, wheel==0.37.1
activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
```

2. Create a subdirectory named `unpacked` to hold the
   project.

```
testpiglatin $ mkdir unpacked
```

3. Use the `pip` command to install the project into the
   `unpacked` directory.

```
testpiglatin $ bin/pip install -t $PWD/unpacked piglatin
```

**Output**

```
Collecting piglatin
Using cached piglatin-1.0.6-py2.py3-none-any.whl (3.1 kB)
Installing collected packages: piglatin
Successfully installed piglatin-1.0.6
```

4. Check the contents of the directory.

```
testpiglatin $ ls
```

**Output**

```
bin lib pyvenv.cfg unpacked
```

5. Change to the `unpacked` directory and display the
   contents.

```
testpiglatin $ cd unpacked
unpacked $ ls
```

**Output**

```
piglatin piglatin-1.0.6.dist-info
```

6. Use the `zip` command to place the contents of the piglatin
   project into a file called `library.zip`.

```
unpacked $ zip -r9 ../library.zip *
```

**Output**

```
adding: piglatin/ (stored 0%)
adding: piglatin/__init__.py (deflated 56%)
adding: piglatin/__pycache__/ (stored 0%)
adding: piglatin/__pycache__/__init__.cpython-39.pyc (deflated 31%)
adding: piglatin-1.0.6.dist-info/ (stored 0%)
adding: piglatin-1.0.6.dist-info/RECORD (deflated 39%)
adding: piglatin-1.0.6.dist-info/LICENSE (deflated 41%)
adding: piglatin-1.0.6.dist-info/WHEEL (deflated 15%)
adding: piglatin-1.0.6.dist-info/REQUESTED (stored 0%)
adding: piglatin-1.0.6.dist-info/INSTALLER (stored 0%)
adding: piglatin-1.0.6.dist-info/METADATA (deflated 48%)
```

7. (Optional) Use the following commands to test the import
   locally.
   1. Set the Python path to the `library.zip`
      file location and start Python.

   ```
   /home $ PYTHONPATH=/tmp/testpiglatin/library.zip
   /home $ python3
   ```

   **Output**

   ```
   Python 3.9.6 (default, Jun 29 2021, 06:20:32)
   [Clang 12.0.0 (clang-1200.0.32.29)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   ```

   2. Import the library and run a test command.

   ```
   >>> import piglatin
   >>> piglatin.translate('hello')
   ```

   **Output**

   ```
   'ello-hay'
   ```

8. Use commands like the following to add the `.zip`
   file from Amazon S3, import it into your notebook in Athena, and test
   it.

```
sc.addPyFile('s3://amzn-s3-demo-bucket/library.zip')

import piglatin
piglatin.translate('hello')

from pyspark.sql.functions import udf
from pyspark.sql.functions import col

hi_udf = udf(piglatin.translate)

df = spark.createDataFrame([(1, "hello"), (2, "world")])

df.withColumn("col", hi_udf(col('_2'))).show()
```

**Output**

```
Calculation started (calculation_id=e2c0a06e-f45d-d96d-9b8c-ff6a58b2a525) in (session=82c0a06d-d60e-8c66-5d12-23bcd55a6457). Checking calculation status...
Calculation completed.
+---+-----+--------+
| _1|   _2|     col|
+---+-----+--------+
|  1|hello|ello-hay|
|  2|world|orld-way|
+---+-----+--------+
```

This example imports the [md2gemini](https://github.com/makeworld-the-better-one/md2gemini "https://github.com/makeworld-the-better-one/md2gemini") package, which converts text in markdown to [Gemini](https://gemini.circumlunar.space/ "https://gemini.circumlunar.space/") text format, from
PyPI. The package has the following [dependencies](https://libraries.io/pypi/md2gemini "https://libraries.io/pypi/md2gemini"):

```
cjkwrap
mistune
wcwidth
```

###### To import a Python .zip file that has dependencies

1. On your local computer, use the following commands to create a
   directory called `testmd2gemini` and create a virtual
   environment.

```
/tmp $ mkdir testmd2gemini
/tmp $ cd testmd2gemini
testmd2gemini$ virtualenv .
```

2. Create a subdirectory named `unpacked` to hold the
   project.

```
testmd2gemini $ mkdir unpacked
```

3. Use the `pip` command to install the project into the
   `unpacked` directory.

```
/testmd2gemini $ bin/pip install -t $PWD/unpacked md2gemini
```

**Output**

```
Collecting md2gemini
  Downloading md2gemini-1.9.0-py3-none-any.whl (31 kB)
Collecting wcwidth
  Downloading wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Collecting mistune<3,>=2.0.0
  Downloading mistune-2.0.2-py2.py3-none-any.whl (24 kB)
Collecting cjkwrap
  Downloading CJKwrap-2.2-py2.py3-none-any.whl (4.3 kB)
Installing collected packages: wcwidth, mistune, cjkwrap, md2gemini
Successfully installed cjkwrap-2.2 md2gemini-1.9.0 mistune-2.0.2 wcwidth-0.2.5
...
```

4. Change to the `unpacked` directory and check the
   contents.

```
testmd2gemini $ cd unpacked
unpacked $ ls -lah
```

**Output**

```
total 16
drwxr-xr-x  13 user1  wheel   416B Jun  7 18:43 .
drwxr-xr-x   8 user1  wheel   256B Jun  7 18:44 ..
drwxr-xr-x   9 user1  staff   288B Jun  7 18:43 CJKwrap-2.2.dist-info
drwxr-xr-x   3 user1  staff    96B Jun  7 18:43 __pycache__
drwxr-xr-x   3 user1  staff    96B Jun  7 18:43 bin
-rw-r--r--   1 user1  staff   5.0K Jun  7 18:43 cjkwrap.py
drwxr-xr-x   7 user1  staff   224B Jun  7 18:43 md2gemini
drwxr-xr-x  10 user1  staff   320B Jun  7 18:43 md2gemini-1.9.0.dist-info
drwxr-xr-x  12 user1  staff   384B Jun  7 18:43 mistune
drwxr-xr-x   8 user1  staff   256B Jun  7 18:43 mistune-2.0.2.dist-info
drwxr-xr-x  16 user1  staff   512B Jun  7 18:43 tests
drwxr-xr-x  10 user1  staff   320B Jun  7 18:43 wcwidth
drwxr-xr-x   9 user1  staff   288B Jun  7 18:43 wcwidth-0.2.5.dist-info
```

5. Use the `zip` command to place the contents of the
   md2gemini project into a file called
   `md2gemini.zip`.

```
unpacked $ zip -r9 ../md2gemini *
```

**Output**

```
  adding: CJKwrap-2.2.dist-info/ (stored 0%)
  adding: CJKwrap-2.2.dist-info/RECORD (deflated 37%)
  ....
  adding: wcwidth-0.2.5.dist-info/INSTALLER (stored 0%)
  adding: wcwidth-0.2.5.dist-info/METADATA (deflated 62%)
```

6. (Optional) Use the following commands to test that the library works
   on your local computer.
   1. Set the Python path to the `md2gemini.zip`
      file location and start Python.

   ```
   /home $ PYTHONPATH=/tmp/testmd2gemini/md2gemini.zip
   /home python3
   ```

   2. Import the library and run a test.

   ```
   >>> from md2gemini import md2gemini
   >>> print(md2gemini('[abc](https://abc.def)'))
   ```

   **Output**

   ```
   https://abc.def abc
   ```

7. Use the following commands to add the `.zip` file
   from Amazon S3, import it into your notebook in Athena, and perform a non UDF
   test.

```
# (non udf test)
sc.addPyFile('s3://amzn-s3-demo-bucket/md2gemini.zip')
from md2gemini import md2gemini
print(md2gemini('[abc](https://abc.def)'))
```

**Output**

```
Calculation started (calculation_id=0ac0a082-6c3f-5a8f-eb6e-f8e9a5f9bc44) in (session=36c0a082-5338-3755-9f41-0cc954c55b35). Checking calculation status...
Calculation completed.
=> https://abc.def (https://abc.def/) abc
```

8. Use the following commands to perform a UDF test.

```
# (udf test)

from pyspark.sql.functions import udf
from pyspark.sql.functions import col
from md2gemini import md2gemini


hi_udf = udf(md2gemini)
df = spark.createDataFrame([(1, "[first website](https://abc.def)"), (2, "[second website](https://aws.com)")])
df.withColumn("col", hi_udf(col('_2'))).show()
```

**Output**

```
Calculation started (calculation_id=60c0a082-f04d-41c1-a10d-d5d365ef5157) in (session=36c0a082-5338-3755-9f41-0cc954c55b35). Checking calculation status...
Calculation completed.
+---+--------------------+--------------------+
| _1|                  _2|                 col|
+---+--------------------+--------------------+
|  1|[first website](h...|=> https://abc.de...|
|  2|[second website](...|=> https://aws.co...|
+---+--------------------+--------------------+
```
