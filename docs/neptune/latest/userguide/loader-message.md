

# Neptune Loader Error and Feed Messages
<a name="loader-message"></a>

The following messages are returned by the `status` endpoint of the Neptune Loader. For more information, see [Get-Status API](load-api-reference-status.md).

The following table contains loader feed code and description.


| Error or Feed Code | Description | 
| --- |--- |
| LOAD\_NOT\_STARTED | Load has been recorded but not started. | 
| LOAD\_IN\_PROGRESS | Indicates that loading is in progress and specifies the number of files currently being loaded.<br />When the loader parses a file, it creates one or more chunks to load in parallel. Because a single file can produce multiple chunks, the file count included with this message is usually less than the number of threads being used by the bulk load process. | 
| LOAD\_COMPLETED | Load has completed without any errors or errors within an acceptable threshold. | 
| LOAD\_CANCELLED\_BY\_USER | Load has been cancelled by user. | 
| LOAD\_CANCELLED\_DUE\_TO\_ERRORS | Load has been cancelled by the system due to errors. | 
| LOAD\_UNEXPECTED\_ERROR | Load failed with an unexpected error. | 
| LOAD\_FAILED | Load failed as a result of one or more errors. | 
| LOAD\_S3\_READ\_ERROR | Feed failed due to intermittent or transient Amazon S3 connectivity issues. If any of the feeds receive this error, overall load status is set to LOAD\_FAILED. | 
| LOAD\_S3\_ACCESS\_DENIED\_ERROR | Access was denied to the S3 bucket. If any of the feeds receive this error, overall load status is set to LOAD\_FAILED. | 
| LOAD\_COMMITTED\_W\_WRITE\_CONFLICTS | Loaded data committed with unresolved write conflicts.<br />The loader will try to resolve the write conflicts in separate transactions and update the feed status as the load progresses. If the final feed status is LOAD\_COMMITTED\_W\_WRITE\_CONFLICTS, then try resuming the load and it will likely succeed without write conflicts. A write conflict is not usually related to bad input data, but duplicates in data can increase the likelihood of write conflicts. | 
| LOAD\_DATA\_DEADLOCK | Load was automatically rolled back due to deadlock. | 
| LOAD\_DATA\_FAILED\_DUE\_TO\_FEED\_MODIFIED\_OR\_DELETED | Feed failed because file was deleted or updated after load start. | 
| LOAD\_FAILED\_BECAUSE\_DEPENDENCY\_NOT\_SATISFIED | The load request was not executed because its dependency check fails. | 
| LOAD\_IN\_QUEUE | The load request has been queued up and is waiting to be executed. | 
| LOAD\_FAILED\_INVALID\_REQUEST | The load failed because the request was invalid (for example, the specified source/bucket may not exist, or the file format is invalid). | 