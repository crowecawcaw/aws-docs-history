# Converting embedded SQL in Java

applications

When you use AWS DMS and DMS Schema Conversion to migrate a database, you might need to convert the
embedded SQL in your application to be compatible with your target database. Rather than
converting it manually, you can use Amazon Q in the IDE to automate the conversion. Amazon Q
uses metadata from a DMS Schema Conversion to convert embedded SQL in your application to a version
that is compatible with your target database. Amazon Q will detect Oracle SQL code in your
application and convert them into PostgreSQL syntax. For more information, see [Converting embedded SQL in Java applications with Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/transform-sql.md "../../../amazonq/latest/qdeveloper-ug/transform-sql.md").

###### Downloading metadata file for embedded SQL conversion in a Java

Application

1. Once you complete the conversion, close the project and go to the S3 bucket
   where your project is stored.
2. Open the folder and find the project folder (“sct-project”).
3. Download the object inside the project folder. This will be a zip file.
4. Use the downloaded zip file as an input to your transformation with Amazon Q:
   [Converting embedded
   SQL in Java applications with Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/transform-sql.md "../../../amazonq/latest/qdeveloper-ug/transform-sql.md").
