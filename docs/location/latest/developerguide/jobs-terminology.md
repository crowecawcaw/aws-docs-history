

# Jobs terminology
<a name="jobs-terminology"></a>

This section provides essential definitions to understand core concepts within Amazon Location Service Jobs, such as job states, data formats, and processing features.

**Job**  
A batch processing operation that performs a specific action on large datasets stored in Amazon S3. Jobs process data asynchronously and return results to a designated output location.

**Job lifecycle**  
The sequence of states a job transitions through from creation to completion, including Pending, Running, Completed, Failed, Cancelling, and Cancelled states.

**Execution role**  
An IAM role that grants Amazon Location permission to access your Amazon S3 buckets on your behalf. The role must have read permissions for input buckets and write permissions for output buckets.

**Apache Parquet**  
A columnar storage file format used for input and output data in Jobs. Parquet provides efficient data compression and encoding schemes for handling complex data in bulk.

**Input schema**  
The required structure and field definitions for input data files. Each job action type has a specific schema that input files must conform to.

**Record-level error**  
An error that affects individual records within a job. These errors are included in the output file with `ErrorType` and `ErrorMessage` fields, allowing valid records to be processed while identifying problematic ones.