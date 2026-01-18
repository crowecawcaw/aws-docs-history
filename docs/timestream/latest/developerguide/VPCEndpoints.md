For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Creating an interface VPC endpoint for

Timestream for LiveAnalytics

You can create an [interface VPC endpoint](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md") for the Timestream for LiveAnalytics service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). To create a VPC endpoint for Timestream, complete the Timestream-specific steps described below.

###### Note

Before completing the steps below, ensure that you understand [specific considerations for Timestream VPC endpoints.](VPCEndpoints.md "VPCEndpoints.md")

##

Constructing a VPC endpoint service name using your Timestream cell

Because of Timestream's unique architecture,
separate VPC interface endpoints must be created for each SDK (Write and Query).
Additionally, you must specify a Timestream cell endpoint (you will only be able to create an endpoint for the Timestream cell that you are mapped to).
To use Interface VPC Endpoints to directly connect to Timestream from within your VPC,
complete the steps below:

1. First, find an available Timestream cell endpoint. To find an available cell endpoint,
   use the
   [`DescribeEndpoints` action](API_query_DescribeEndpoints.md "API_query_DescribeEndpoints.md")
   (available through both the Write and Query APIs)
   to list the cell endpoints available in your Timestream account.
   See the [example](#VPCEndpoints.vpc-endpoint-create.vpc-endpoint-name.example "#VPCEndpoints.vpc-endpoint-create.vpc-endpoint-name.example") for further details.
2. Once you've selected a cell endpoint to use, create a VPC interface endpoint string for either the Timestream Write or Query API:
   - _For the Write API:_

   ```
   com.amazonaws.`<region>`.timestream.ingest-`<cell>`
   ```

   - _For the Query API:_

   ```
   com.amazonaws.`<region>`.timestream.query-`<cell>`
   ```

where `<region>` is a [valid AWS region code](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md")
and `<cell>`
is one of the cell endpoint addresses (such as `cell1` or `cell2`) returned in the
[Endpoints object](API_query_DescribeEndpoints.md#API_query_DescribeEndpoints_ResponseSyntax "API_query_DescribeEndpoints.md#API_query_DescribeEndpoints_ResponseSyntax")
by the
[DescribeEndpoints action](API_query_DescribeEndpoints.md "API_query_DescribeEndpoints.md").
See the [example](#VPCEndpoints.vpc-endpoint-create.vpc-endpoint-name.example "#VPCEndpoints.vpc-endpoint-create.vpc-endpoint-name.example") for further details. 3. Now that you have constructed a VPC endpoint service name,
[create an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md").
When asked to provide a VPC endpoint service name, use the VPC endpoint service name that you constructed in Step 2.

### Example: Constructing your VPC endpoint service name

In the following example, the `DescribeEndpoints`
action is executed in the AWS CLI using the Write API in the `us-west-2` region:

```
aws timestream-write describe-endpoints --region us-west-2
```

This command will return the following output:

```
{
    "Endpoints": [
        {
            "Address": "ingest-`cell1`.timestream.`us-west-2`.amazonaws.com",
            "CachePeriodInMinutes": 1440
        }
    ]
}
```

In this case, `cell1` is the `<cell>` ,
and `us-west-2` is the `<region>`.
So, the resulting VPC endpoint service name will look like:

```
com.amazonaws.`us-west-2`.timestream.ingest-`cell1`
```

Now that you've created an interface VPC endpoint for Timestream for LiveAnalytics, [create a VPC endpoint policy for Timestream for LiveAnalytics](VPCEndpoints.md "VPCEndpoints.md").
