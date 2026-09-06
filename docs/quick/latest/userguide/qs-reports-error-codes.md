

# Error codes for failed PDF export jobs
<a name="qs-reports-error-codes"></a>

When you generate PDF reports in Amazon Quick Sight, you may encounter instances where your request to generate a PDF report fails. There are many reasons why a failure might occur. Quick Sight provides error codes that can help you understand why the error occurred and provide guidance to troubleshoot the issue. The following table lists the error codes that Quick Sight returns when a PDF export job fails.


| Error code | Guidance | 
| --- | --- | 
| INVALID\_DATAPREP\_SYNTAX | Check the syntax for your calculated fields, and try again. | 
| POST\_AGGREGATED\_METRIC\_AS\_DIMENSION | Aggregated metrics/operands can't be used as visual's grouping dimensions. Choose a valid visual's grouping dimensions, and try again. | 
| SPICE\_TABLE\_NOT\_FOUND | The dataset has been deleted or is unavailable. Import a valid dataset, and try again. | 
| FIELD\_NOT\_FOUND | A field is no longer available. Update or replace the missing fields in this dataset, and try again. | 
| FIELD\_ACCESS\_DENIED | You don't have access to some fields in this dataset. Request access, and try again.  | 
| PERMISSIONS\_DATASET\_INVALID\_COLUMN\_VALUE | An invalid row level permission column value was found. Check your parent dataset rules, and try again. | 
| COLUMN\_NOT\_FOUND | Replace the missing columns in your filters or parameters, and try again. | 
| INVALID\_COLUMN\_TYPE | Some fields' data types have been changed and can not be automatically updated. Adjust these fields in your dataset, and try again. | 
| PERMISSIONS\_DATASET\_USER\_DENIED | You don't have access to this dataset. Request access to this dataset, and try again. | 
| DATA\_SOURCE\_TIMEOUT | Your query has timed out. Reduce the amount of data, or import the data into SPICE, and try again. | 
| MAX\_PAGE\_EXCEEDED\_ERROR | Your file is ready but content is not complete. PDFs have a 1,000 page limit. Choose a shorter PDF, and try again. | 
| INSUFFICIENT\_BODY\_HEIGHT\_ERROR | Adjust the header and footer to be less than the page height, and try again. | 
| FIRST\_PAGE\_HEIGHT\_TOO\_SMALL\_ERROR | Adjust sections to make room for your tables, and try again. | 
| INTERNAL\_ERROR | We can't create your PDF right now. Wait a few minutes, and try again. | 