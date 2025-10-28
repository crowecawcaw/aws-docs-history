For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Timestream for LiveAnalytics specific error codes

This section contains the specific error codes for Timestream for LiveAnalytics.

## Timestream for LiveAnalytics write API errors

\***\*InternalServerException\*\***

HTTP Status Code: 500

**ThrottlingException**

HTTP Status Code: 429

**ValidationException**

HTTP Status Code: 400

**ConflictException**

HTTP Status Code: 409

**AccessDeniedException**

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**ServiceQuotaExceededException**

HTTP Status Code: 402

**ResourceNotFoundException**

HTTP Status Code: 404

**RejectedRecordsException**

HTTP Status Code: 419

**InvalidEndpointException**

HTTP Status Code: 421

## Timestream for LiveAnalytics query API errors

**ValidationException**

HTTP Status Code: 400

**QueryExecutionException**

HTTP Status Code: 400

**ConflictException**

HTTP Status Code: 409

**ThrottlingException**

HTTP Status Code: 429

**InternalServerException**

HTTP Status Code: 500

**InvalidEndpointException**

HTTP Status Code: 421
