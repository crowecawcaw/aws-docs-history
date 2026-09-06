

# Document History
<a name="DocumentHistory"></a>

 The following table describes the documentation for this release of *Amazon SimpleDB*. 

**Relevant Dates to this History:**
+ ****API version: ****2009-04-15
+ ****Lastest document update: ****March 11, 2026


| Change | Description | Date Changed | 
| --- | --- | --- | 
| Amazon SimpleDB now supports domain export | You can now export your domain data from Amazon SimpleDB to Amazon S3 for migration and archival. For more information, see [https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/ExportingDomain.html](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/ExportingDomain.html). | March 11, 2026 | 
| Removed incorrect note. | The Note in the Select operation description was incorrect and has been removed. For more information, see [Select](SDB_API_Select.md). | April 12, 2012 | 
| Added handling response code 503 information. | Added instructions for handling server response code 503. For more information, see [About Response Code 503](APIError.md#ErrorCode503). |  February 20, 2012  | 
| Added HTTP POST request information | Added instructions for forming HTTP POST requests. For more information, see [Making REST Requests](MakingRESTRequests.md). |  February 20, 2012  | 
| Revised AWS version 2 signing information | Revised AWS version 2 signing instructions. For more information, see [HMAC-SHA Signature](HMACAuth.md). |  February 20, 2012  | 
| Support for AWS Security Token Service | Amazon SimpleDB now supports the AWS Security Token Service. For more information, see [Using Temporary Security Credentials](UsingTemporarySecurityCredentials_SDB.md). | 01 Sept 2011 | 
| SOAP support deprecated | Amazon SimpleDB no longer supports requests using SOAP. | 01 Sept 2011 | 
| New Tuning Queries section in documentation | A section was added to the Tuning Queries topic covering the use of composite attributes to improve query performance. For more information see [Tuning Your Queries Using Composite Attributes](BoxUsageTuning.md).  | 20 May 2011 | 
| New link | This service's endpoint information is now located in the Amazon Web Services General Reference. For more information, go to Regions and Endpoints in the [Amazon Web Services General Reference](http://docs.aws.amazon.com/general/latest/gr/index.html?rande.html).  | 02 March 2011 | 
| BatchDeleteAttributes |  Amazon SimpleDB can now perform multiple delete operations at once. For more information, see [BatchDeleteAttributes](SDB_API_BatchDeleteAttributes.md). | 03 December 2010 | 
| Asia Pacific Region |  Amazon SimpleDB now supports the Asia Pacific region. For more information, see [Region Endpoints](Endpoints.md). | 28 April 2010 | 
| Consistent read |  GetAttributes and Select can now perform consistent reads, which always return the most recently written data. For more information, see [Consistency](ConsistencySummary.md).  | 24 February 2010 | 
| Conditional put |  Amazon SimpleDB now supports conditional put, which enables you to perform a put if a specific condition is met. For more information, see [Conditionally Putting and Deleting Data](ConditionalPutDelete.md) and [PutAttributes](SDB_API_PutAttributes.md).  | 24 February 2010 | 
| Conditional delete |  Amazon SimpleDB now supports conditional delete, which enables you to delete data if a specific condition is met. For more information, see [Conditionally Putting and Deleting Data](ConditionalPutDelete.md) and [DeleteAttributes](SDB_API_DeleteAttributes.md).  | 24 February 2010 | 
| New Data Center in Europe | Amazon SimpleDB is now available in Europe. For more information, see [Region Endpoints](Endpoints.md).  | 23 September 2009 | 
| contains | You can now search whether attribute values contain a specified string using like. For more information, see [Comparison Operators](UsingSelectOperators.md).  | 18 May 2009 | 
| Sort and Execute Queries by itemName() | Select can now use where and order by with itemNames(). For more information, see [Comparison Operators](UsingSelectOperators.md).  | 18 May 2009 | 
| IS NULL Sort | Sort can now be applied to expressions that contain the is null predicate operator, as long as is null is not applied to the attribute that being sorted on. For more information about Select, see [Sort](SortingDataSelect.md).  | 18 May 2009 | 
| Increased Item Limit | Select can now return up to 2500 items. For more information about Select, see [Limits](SDBLimits.md).  | 18 May 2009 | 
| Query and QueryWithAttributes Deprecated | Amazon SimpleDB replaced Query and QueryWithAttributes with Select, a query function that is similar to the standard SQL SELECT statement. For more information, see [Using Select to Create Amazon SimpleDB Queries](UsingSelect.md).  | 18 May 2009 | 
| SSL Required | All requests to Amazon SimpleDB must be made over SSL (https://). For more information, see [Request Authentication](RequestAuthentication.md).  | 18 May 2009 | 