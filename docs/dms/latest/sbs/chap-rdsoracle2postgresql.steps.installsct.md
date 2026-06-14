# Step 1: Install the SQL Drivers and AWS Schema Conversion Tool on Your Local Computer

To install the SQL drivers and the AWS Schema Conversion Tool (AWS SCT) on your local computer, do the following:

1. Download the JDBC driver for your Oracle database release. For more information, go to https://www.oracle.com/jdbc.
2. Download the PostgreSQL driver ([postgresql-42.2.19.jar](https://jdbc.postgresql.org/download/postgresql-42.2.19.jar "https://jdbc.postgresql.org/download/postgresql-42.2.19.jar")).
3. Install AWS SCT and the required JDBC drivers.

   1. Download AWS SCT from [Installing, verifying, and updating the Schema Conversion Tool](../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md "../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md").
   2. Launch AWS SCT.
   3. In AWS SCT, choose **Global settings** from **Settings**.
   4. In **Global settings**, choose **Driver**, and then choose **Browse** for **Oracle driver path**. Locate the JDBC Oracle driver and choose **OK**.
   5. Choose **Browse** for **PostgreSQL driver path**. Locate the JDBC PostgreSQL driver and choose **OK**.

   ![Drivers](images/sct-drivers.png) 6. Choose **OK** to close the dialog box.
