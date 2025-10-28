For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Implementing the endpoint discovery pattern

To implement the endpoint discovery pattern, choose an API (Write or Query),
create a **DescribeEndpoints** request, and use the
returned endpoint(s) for the duration of the returned TTL value(s). The
implementation procedure is described below.

###### Note

Ensure you are familiar with the [usage
notes](#Using-API.endpoint-discovery.describe-endpoints.usage-notes "#Using-API.endpoint-discovery.describe-endpoints.usage-notes").

## Implementation procedure

1. Acquire the endpoint for the API you would like to make calls against
   ([Write](API_Operations_Amazon_Timestream_Write.md "API_Operations_Amazon_Timestream_Write.md") or [Query](API_Operations_Amazon_Timestream_Query.md "API_Operations_Amazon_Timestream_Query.md")). using the [`DescribeEndpoints`](API_DescribeEndpoints.md "API_DescribeEndpoints.md") request.
   1. Create a request for [`DescribeEndpoints`](API_DescribeEndpoints.md "API_DescribeEndpoints.md") that corresponds
      to the API of interest ([Write](API_Operations_Amazon_Timestream_Write.md "API_Operations_Amazon_Timestream_Write.md") or [Query](API_Operations_Amazon_Timestream_Query.md "API_Operations_Amazon_Timestream_Query.md")) using one of the two endpoints described
      below. There are no input parameters for the request. Ensure
      that you read the notes below.

   _Write SDK:_

   ```
   ingest.timestream.`<region>`.amazonaws.com
   ```

   _Query SDK:_

   ```
   query.timestream.`<region>`.amazonaws.com
   ```

   An example CLI call for region `us-east-1`
   follows.

   ```
   REGION_ENDPOINT="https://query.timestream.us-east-1.amazonaws.com"
   REGION=us-east-1
   aws timestream-write describe-endpoints \
   --endpoint-url $REGION_ENDPOINT \
   --region $REGION
   ```

   ###### Note

   The HTTP "Host" header _must_ also
   contain the API endpoint. The request will fail if the
   header is not populated. This is a standard requirement for
   all HTTP/1.1 requests. If you use an HTTP library supporting
   1.1 or later, the HTTP library should automatically populate
   the header for you.

   ###### Note

   Substitute `<region>`
   with the region identifier for the region the request is
   being made in, e.g. `us-east-1` 2. Parse the response to extract the endpoint(s), and cache TTL
   value(s). The response is an array of one or more [`Endpoint` objects](API_Endpoint.md "API_Endpoint.md") . Each
   `Endpoint` object contains an endpoint address
   (`Address`) and the TTL for that endpoint
   (`CachePeriodInMinutes`).

2. Cache the endpoint for up to the specified TTL.
3. When the TTL expires, retrieve a new endpoint by starting over at
   step 1 of the Implementation.

## Usage notes for the endpoint discovery pattern

- The **DescribeEndpoints** action is the
  only action that Timestream Live Analytics regional endpoints recognize.
- The response contains a list of endpoints to make Timestream Live Analytics API
  calls against.
- On successful response, there should be at least one endpoint in the
  list. If there is more than one endpoint in the list, any of them are
  equally usable for the API calls, and the caller may choose the endpoint
  to use at random.
- In addition to the DNS address of the endpoint, each endpoint in the
  list will specify a time to live (TTL) that is allowable for using the
  endpoint specified in minutes.
- The endpoint should be cached and reused for the amount of time
  specified by the returned TTL value (in minutes). After the TTL expires
  a new call to **DescribeEndpoints** should
  be made to refresh the endpoint to use, as the endpoint will no longer
  work after the TTL has expired.
