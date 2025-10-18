# QueryStatisticsForDescribeQuery

Gets metadata about a query, including the number of events that were matched, the total
 number of events scanned, the query run time in milliseconds, and the query's creation
 time.


## Contents





**BytesScanned** 


The total bytes that the query scanned in the event data store. This value matches the
 number of bytes for which your account is billed for the query, unless the query is still
 running.


Type: Long


Required: No




**CreationTime** 


The creation time of the query.


Type: Timestamp


Required: No




**EventsMatched** 


The number of events that matched a query.


Type: Long


Required: No




**EventsScanned** 


The number of events that the query scanned in the event data store.


Type: Long


Required: No




**ExecutionTimeInMillis** 


The query's run time, in milliseconds.


Type: Integer


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/QueryStatisticsForDescribeQuery "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/QueryStatisticsForDescribeQuery")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/QueryStatisticsForDescribeQuery "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/QueryStatisticsForDescribeQuery")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/QueryStatisticsForDescribeQuery "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/QueryStatisticsForDescribeQuery")
