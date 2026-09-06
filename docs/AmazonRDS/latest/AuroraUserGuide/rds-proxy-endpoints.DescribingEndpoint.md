

# Viewing proxy endpoints
<a name="rds-proxy-endpoints.DescribingEndpoint"></a>

To view existing proxy endpoints, follow these instructions:

## Console
<a name="rds-proxy-endpoints.DescribingEndpoint.CON"></a>

**To view the details for a proxy endpoint**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1.  In the navigation pane, choose **Proxies**. 

1.  In the list, choose the proxy whose endpoint you want to view. Click the proxy name to view its details page. 

1.  In the **Proxy endpoints** section, choose the endpoint that you want to view. Click its name to view the details page. 

1.  Examine the parameters whose values you're interested in. You can check properties such as the following: 
   +  Whether the endpoint is read/write or read-only.
   +  The endpoint address that you use in a database connection string.
   +  The VPC, subnets, and security groups associated with the endpoint.

## AWS CLI
<a name="rds-proxy-endpoints.DescribingEndpoint.CLI"></a>

 To view one or more proxy endpoints, use the AWS CLI [describe-db-proxy-endpoints](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-proxy-endpoints.html) command.

 You can include the following optional parameters: 
+  `--db-proxy-endpoint-name` 
+  `--db-proxy-name` 

 The following example describes the `my-endpoint` proxy endpoint. 

**Example**  
For Linux, macOS, or Unix:  

```
aws rds describe-db-proxy-endpoints \
  --db-proxy-endpoint-name {{my-endpoint}}
```
For Windows:  

```
aws rds describe-db-proxy-endpoints ^
  --db-proxy-endpoint-name {{my-endpoint}}
```

## RDS API
<a name="rds-proxy-endpoints.DescribingEndpoint.API"></a>

 To describe one or more proxy endpoints, use the RDS API [DescribeDBProxyEndpoints](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxyEndpoints.html) operation. 