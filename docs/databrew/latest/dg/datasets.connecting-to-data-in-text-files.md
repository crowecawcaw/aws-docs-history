# Connecting to data in a text file with DataBrew

You can configure the following format options for the input files that DataBrew supports:

- **Comma-separated value (CSV) files**
  - **Delimiters**

  The default delimiter is a comma for .csv files.
  If your file uses a different delimiter, choose the delimiter for **CSV
  delimiter** in the **Additional configurations**
  section when you create your dataset. The following delimiters are supported for
  .csv files:

      - Comma (,)
      - Colon (:)
      - Semi-colon (;)
      - Pipe (|)
      - Tab (\t)
      - Caret (^)
      - Backslash (\)
      - Space

  - **Column header values**

  Your CSV file can include a header row as the first row of the file. If it
  doesn't, DataBrew creates a header row for you.

      - If your CSV file includes a header row, choose **Treat first
       row as header**. If you do, the first row of your CSV file is treated as
       containing the column header values.
      - If your CSV file doesn't include a header row, choose
       **Add default
       header**. If you do, DataBrew creates a header row for
       the file and doesn't treat your first row of data as
       containing header values. The headers that DataBrew creates consist
       of an underscore and a number for each column in the file, in
       the format `Column_1`, `Column_2`,
       `Column_3`, and so on.

- **JSON files**

DataBrew supports two formats for JSON files, JSON Lines and JSON
document. JSON Lines files contain one row per line. In JSON document files, all
rows are contained in a single JSON structure or an array. You can specify your
JSON file type in the **Additional configurations** section
when you create a JSON dataset. The default format is JSON Lines.

- **Excel files**

The following apply to Excel sheets in DataBrew:

    + **Excel sheet loading**


    By default, DataBrew loads the first sheet in your Excel file. However,
     you can specify a different sheet number or sheet name in the
     **Additional configurations** section when you create an
     Excel dataset.
    + **Column header values**


    Your Excel sheets can include a header row as the first row of the file, but if they
     don't, DataBrew will create a header row for you.




    	- If your Excel sheets include a header row, choose **Treat first
    	 row as header**. If you do, the first row of your Excel sheets is treated
    	 as containing the column header values.
    	- If your Excel file doesn't include a header row, choose **Add default
    	 header**. By doing this, you specify that DataBrew
    	 should create a header row for the file and not treat your first
    	 row of data as containing header values. The headers that DataBrew
    	 creates consist of an underscore and a number for each column in
    	 the file, in the format `Column_1`,
    	 `Column_2`, `Column_3`, and so
    	 on.
