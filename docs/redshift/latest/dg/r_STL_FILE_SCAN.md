

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_FILE\_SCAN
<a name="r_STL_FILE_SCAN"></a>

Returns the files that Amazon Redshift read while loading data by using the COPY command.

Querying this view can help troubleshoot data load errors. STL\_FILE\_SCAN can be particularly helpful with pinpointing issues in parallel data loads, because parallel data loads typically load many files with a single COPY command.

STL\_FILE\_SCAN is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

**Note**  
STL\_FILE\_SCAN only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters or on serverless namespaces. To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view [SYS\_LOAD\_DETAIL](SYS_LOAD_DETAIL.md) . The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns
<a name="r_STL_FILE_SCAN-table-columns2"></a>


| Column name | Data type | Description | 
| --- | --- | --- | 
| userid | integer | ID of the user who generated the entry. | 
| query  | integer | Query ID. The query column can be used to join other system tables and views. | 
| slice | integer | Number that identifies the slice where the query was running. | 
| name | character(90) | Full path and name of the file that was loaded. | 
| lines | bigint | Number of lines read from the file. | 
| bytes | bigint | Number of bytes read from the file. | 
| loadtime | bigint | Amount of time spent loading the file (in microseconds). | 
| curtime | Timestamp | Timestamp representing the time that Amazon Redshift started processing the file. | 
| is\_partial | integer | Value that if true (1) indicates the input file is split into ranges during a COPY operation. If this value is false (0), the input file isn't split. | 
| start\_offset | bigint | Value that, if the input file is split during a COPY operation, indicates the offset value of the split (in bytes). If the file isn't split, this value is 0.  | 

## Sample queries
<a name="r_STL_FILE_SCAN-sample-queries2"></a>

The following query retrieves the names and load times of any files that took over 1,000,000 microseconds for Amazon Redshift to read.

```
select trim(name)as name, loadtime from stl_file_scan
where loadtime > 1000000;
```

This query returns the following example output.

```
           name            | loadtime
---------------------------+----------
 listings_pipe.txt         |  9458354
 allusers_pipe.txt         |  2963761
 allevents_pipe.txt        |  1409135
 tickit/listings_pipe.txt  |  7071087
 tickit/allevents_pipe.txt |  1237364
 tickit/allusers_pipe.txt  |  2535138
 listings_pipe.txt         |  6706370
 allusers_pipe.txt         |  3579461
 allevents_pipe.txt        |  1313195
 tickit/allusers_pipe.txt  |  3236060
 tickit/listings_pipe.txt  |  4980108
(11 rows)
```