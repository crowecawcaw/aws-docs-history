# Spark native fine-grained access control alllowlisted PySpark API

To maintain security and data access controls, Spark fine-grained access control
(FGAC) restricts certain PySpark functions. These restrictions are enforced
through:

- Explicit blocking that prevents function execution
- Architecture incompatibilities that make functions non-functional
- Functions that may throw errors, return access denied messages, or do
  nothing when called
  The following PySpark features aren't supported in Spark FGAC:

- RDD operations (blocked with SparkRDDUnsupportedException)
- Spark Connect (unsupported)
- Spark Streaming (unsupported)
  While we've tested the listed functions in a Native Spark FGAC environment and
  confirmed they work as expected, our testing typically covers only basic usage of
  each API. Functions with multiple input types or complex logic paths may have
  untested scenarios.

For any functions not listed here and not clearly part of the unsupported
categories above, we recommend:

- Testing them first in a gamma environment or small-scale deployment
- Verifying their behavior before using them in production

###### Note

If you see a class method listed but not its base class, the method should
still work—it just means we haven't explicitly verified the base class
constructor.

The PySpark API is organized into modules. General support for methods within each
module is detailed in the table below.

| Module name                 | Status       | Notes                                                                                                                                     |
| --------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| pyspark_core                | Supported    | This module contains the main RDD classes, and these functions<br>are mostly unsupported.                                                 |
| pyspark_sql                 | Supported    |                                                                                                                                           |
| pyspark_testing             | Supported    |                                                                                                                                           |
| pyspark_resource            | Supported    |                                                                                                                                           |
| pyspark_streaming           | Blocked      | Streaming usage is blocked in Spark FGAC.                                                                                                 |
| pyspark_mllib               | Experimental | This module contains RDD based ML operations, and these<br>functions are mostly unsupported. This module isn't thoroughly<br>tested.      |
| pyspark_ml                  | Experimental | This module containes DataFrame based ML operations, and these<br>functions are mostly supported. This module isn't thoroughly<br>tested. |
| pyspark_pandas              | Supported    |                                                                                                                                           |
| pyspark_pandas_slow         | Supported    |                                                                                                                                           |
| pyspark_connect             | Blocked      | Spark Connect usage is blocked in Spark FGAC.                                                                                             |
| pyspark_pandas_connect      | Blocked      | Spark Connect usage is blocked in Spark FGAC.                                                                                             |
| pyspark_pandas_slow_connect | Blocked      | Spark Connect usage is blocked in Spark FGAC.                                                                                             |
| pyspark_errors              | Experimental | This module is not thoroughly tested. Custom error classes<br>can't be utilized.                                                          |

**API Allowlist**

For a downloadable and easier to search list, a file with the modules and classes
is available at [Python functions allowed in Native FGAC](samples/Python functions allowed in Native FGAC.md "samples/Python functions allowed in Native FGAC.md").
