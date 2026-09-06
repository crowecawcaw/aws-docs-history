

# Spark native fine-grained access control allow-listed PySpark API
<a name="clean-rooms-spark-fgac-pyspark-api-allowlist"></a>

To maintain security and data access controls, Spark fine-grained access control (FGAC) restricts certain PySpark functions. These restrictions are enforced through:
+ Explicit blocking that prevents function execution
+ Architecture incompatibilities that make functions non-functional
+ Functions that may throw errors, return access denied messages, or do nothing when called

The following PySpark features aren't supported in Spark FGAC:
+ RDD operations (blocked with SparkRDDUnsupportedException)
+ Spark Connect (unsupported)
+ Spark Streaming (unsupported)

While we've tested the listed functions in a Native Spark FGAC environment and confirmed they work as expected, our testing typically covers only basic usage of each API. Functions with multiple input types or complex logic paths may have untested scenarios.

For any functions not listed here and not clearly part of the unsupported categories above, we recommend:
+ Testing them first in a gamma environment or small-scale deployment
+ Verifying their behavior before using them in production

**Note**  
If you see a class method listed but not its base class, the method should still work—it just means we haven't explicitly verified the base class constructor.

The PySpark API is organized into modules. General support for methods within each module is detailed in the table below.


| Module name | Status | Notes | 
| --- | --- | --- | 
| pyspark\_core | Supported | This module contains the main RDD classes, and these functions are mostly unsupported. | 
| pyspark\_sql | Supported |  | 
| pyspark\_testing | Supported |  | 
| pyspark\_resource | Supported |  | 
| pyspark\_streaming | Blocked | Streaming usage is blocked in Spark FGAC. | 
| pyspark\_mllib | Experimental | This module contains RDD based ML operations, and these functions are mostly unsupported. This module isn't thoroughly tested. | 
| pyspark\_ml | Experimental | This module containes DataFrame based ML operations, and these functions are mostly supported. This module isn't thoroughly tested. | 
| pyspark\_pandas | Supported |  | 
| pyspark\_pandas\_slow | Supported |  | 
| pyspark\_connect | Blocked | Spark Connect usage is blocked in Spark FGAC. | 
| pyspark\_pandas\_connect | Blocked | Spark Connect usage is blocked in Spark FGAC. | 
| pyspark\_pandas\_slow\_connect | Blocked | Spark Connect usage is blocked in Spark FGAC. | 
| pyspark\_errors | Experimental | This module is not thoroughly tested. Custom error classes can't be utilized. | 

**API Allowlist**

For a downloadable and easier to search list, a file with the modules and classes is available at [Python functions allowed in Native FGAC](samples/Python functions allowed in Native FGAC.zip).