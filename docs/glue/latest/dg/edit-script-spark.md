# Editing Spark scripts in the AWS Glue console

A script contains the code that extracts data from sources, transforms it, and loads it into
targets. AWS Glue runs a script when it starts a job.

AWS Glue ETL scripts can be coded in Python or Scala. Python scripts use a language that is an extension of the PySpark Python dialect for
extract, transform, and load (ETL) jobs. The script contains _extended constructs_ to
deal with ETL transformations. When you automatically generate the source code logic for your
job, a script is created. You can edit this script, or you can provide your own script to
process your ETL work.

For information about defining and editing scripts in AWS Glue, see [AWS Glue programming guide](edit-script.md "edit-script.md").

## Additional libraries or files

If your script requires additional libraries or files, you can specify them as
follows:

**Python library path**

Comma-separated Amazon Simple Storage Service (Amazon S3) paths to Python libraries that are
required by the script.

###### Note

Only pure Python libraries can be used. Libraries that rely
on C extensions, such as the pandas Python Data Analysis Library, are not yet supported.

**Dependent jars path**

Comma-separated Amazon S3 paths to JAR files that are required by the
script.

###### Note

Currently, only pure Java or Scala (2.11) libraries can be used.

**Referenced files path**

Comma-separated Amazon S3 paths to additional files (for example,
configuration files) that are required by the script.
