# Updating files in a dataset

To get the latest version of files, you can update files in your dataset. You can
update these types of files:

- Comma-delimited (CSV) and tab-delimited (TSV) text files
- Extended and common log format files (ELF and CLF)
- Flat or semistructured data files (JSON)
- Microsoft Excel (XLSX) files
  Before updating a file, make sure that the new file has the same fields in the same
  order as the original file currently in the dataset. If there are field (column)
  discrepancies between the two files, an error occurs and you need to fix the
  discrepancies before attempting to update again. You can do this by editing the new file
  to match the original. Note that if you want to add new fields, you can append them
  after the original fields in the file. For example, in a Microsoft Excel spreadsheet,
  you can append new fields to the right of the original fields.

###### To update a file in a dataset

1. In Quick Sight, choose **Data** at left.
2. In the **Datasets** tab, choose the dataset that you want to
   update, and then choose **Edit dataset**.
3. On the data preparation page that opens, choose the drop-down list for the
   file that you want to update, and then choose **Update
   file**.
4. On the **Update file** page that opens, choose
   **Upload file**, and then navigate to a file.

Quick Sight scans the file. 5. If the file is a Microsoft Excel file, choose the sheet that you want on the
**Choose your sheet** page that opens, and then choose
**Select**. 6. Choose **Confirm file update** on the following page. A
preview of some of the sheet columns is shown for your reference.

A message that the file updated successfully appears at top right and the
table preview updates to show the new file data.
