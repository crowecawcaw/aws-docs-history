# Create new catalog table

###### To add data to a catalog

1. In the data explorer, choose the **Add** button.
2. In the Add data dialog, choose one of the options
   - Create table: Upload data files to create a new table
   - Create Amazon S3 Tables catalog: Create a new catalog for your Amazon S3 Tables
   - Add connection: Connect to first and third-party data sources
   - Add Amazon S3 location: Add an existing Amazon S3 location

3. For creating a table from uploaded data:
   1. Choose **Create table** option and select
      **Next**.
   2. In the file upload area, either drag and drop your file or select
      **Choose file** to browse for your data file.
   3. Configure the table properties:
      - Table type: Select Amazon S3/external table
      - Catalog name: Choose the target catalog
      - Database: Select the database
      - Table name: Enter a name for your table

   4. Set the data format options:
      - Data format: Choose CSV, JSON, or Parquet
      - Compression type: Select compression if applicable
      - Delimiter: Specify the field separator for CSV files
      - Ignore first row: Check if the first row contains column headers

   5. Choose **Next** to proceed to schema configuration.
   6. In the Schema section:
      - Review the automatically detected column names and data types.
      - Modify column names by editing the text fields.
      - Change data of columns as needed

   7. Choose **Create table** to complete the process.

4. The new table will appear in your catalog with the specified schema and uploaded
   data.
