

# Error handling
<a name="error-handling"></a>

Jobs handle errors at both the job level and individual record level. Job-level errors prevent the entire job from completing and are reported through the job status. These include authentication failures, permission issues, and service errors.

Record-level errors affect individual records and are included in the output file with `ErrorType` and `ErrorMessage` fields, allowing you to identify and address problematic records while still processing valid ones. Common record-level errors include invalid input values or missing required fields.