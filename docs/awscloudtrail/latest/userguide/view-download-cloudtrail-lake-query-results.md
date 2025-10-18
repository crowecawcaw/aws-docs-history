# Download saved query results

After you save query results, you need to
 be able to locate the file containing the query results. CloudTrail delivers your query results to an Amazon S3 bucket that you specify when you save the query results.
 

###### Note


 When you save query results, the query results may display in the console 
 before they are viewable in the S3 bucket since CloudTrail delivers the query results after the 
 query scan completes. While most queries complete within a few minutes, 
 depending on the size of your event data store, it can take considerably longer for 
 CloudTrail to deliver query results to your S3 bucket. CloudTrail delivers the query results to the 
 S3 bucket in compressed gzip format. On average, after the query scan completes 
 you can expect a latency of 60 to 90 seconds for every GB of data delivered to the S3 bucket.
 

###### Topics

* [Find your CloudTrail Lake saved query results](#cloudtrail-find-lake-query-results "#cloudtrail-find-lake-query-results")
* [Download your CloudTrail Lake saved query results](#cloudtrail-download-lake-query-results "#cloudtrail-download-lake-query-results")

## Find your CloudTrail Lake saved query results


CloudTrail publishes query result and sign files to your S3 bucket. The query result file contains the output of the saved query and the sign file provides the signature and hash value for the query results. 
 You can use the sign file to validate the query results. For more information about validating query results, see [Validate CloudTrail Lake saved query results](cloudtrail-query-results-validation.md "cloudtrail-query-results-validation.md").


To retrieve a query result or sign file, you can use the Amazon S3 console, the Amazon S3 command line interface
 (CLI), or the API. 


###### To find your query results and sign files with the Amazon S3 console

1. Open the Amazon S3 console.
2. Choose the bucket you specified.
3. Navigate through the object hierarchy until you find the query result and sign files. The query result file has a .csv.gz extension and the sign file has a .json extension.

You will navigate through an object hierarchy that is similar to the following example,
 but with a different bucket name, account ID, date, and query ID. 



```

All Buckets
    amzn-s3-demo-bucket
        AWSLogs
            Account_ID;
                CloudTrail-Lake
                    Query
                        2022
                            06
                              20
                                Query_ID

```

## Download your CloudTrail Lake saved query results


When you save query results, CloudTrail delivers two types of files to your Amazon S3 bucket.



* A sign file in JSON format that you can use to validate the query result files. The sign file is named result\_sign.json. 
 For more information about the sign file, see [CloudTrail sign file structure](cloudtrail-query-results-validation.md#cloudtrail-results-file-validation-sign-file-structure "cloudtrail-query-results-validation.md#cloudtrail-results-file-validation-sign-file-structure").
* One or more query result files in CSV format, which contain the results from the query. The number of query result files delivered is dependent upon the total size of the query results. 
 The maximum file size for a query result file is 1 TB. Each query result file is named result\_`number`.csv.gz. For example, if the total size of the query results was 2 TB, you would have two query result files, result\_1.csv.gz and result\_2.csv.gz.

 CloudTrail query result and sign files are Amazon S3 objects. You can use the S3
 console, the AWS Command Line Interface (CLI), or the S3 API to retrieve query result and sign files. 



 The following procedure describes how to download the query result and sign files with the Amazon S3 console.
 


###### To download your query result or sign file with the Amazon S3 console

1. Open the Amazon S3 console.
2. Choose the bucket and choose the file that you want to
 download.



![CloudTrail query result file](images/lake_query_results_S3.png)
3. Choose **Download** and follow any prompts to save the file.


###### Note

Some browsers, such as Chrome, automatically extract the query result file for you. If
 your browser does this for you, skip to step 5.
4. Use a product such as [7-Zip](https://www.7-zip.org/ "https://www.7-zip.org/") to extract
 the query result file.
5. Open the query result or sign file.
