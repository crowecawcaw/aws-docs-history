

# Modifying a proxy endpoint
<a name="rds-proxy-endpoints.ModifyingEndpoint"></a>

To modify your proxy endpoints, follow these instructions:

## Console
<a name="rds-proxy-endpoints.ModifyingEndpoint.CON"></a>

**To modify one or more proxy endpoints**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1.  In the navigation pane, choose **Proxies**. 

1. In the list, choose the proxy whose endpoint you want to modify. Click the proxy name to view its details page.

1.  In the **Proxy endpoints** section, choose the endpoint that you want to modify. You can select it in the list, or click its name to view the details page. 

1.  On the proxy details page, under the **Proxy endpoints** section, choose **Edit**. Or, on the proxy endpoint details page, for **Actions**, choose **Edit**.

1.  Change the values of the parameters that you want to modify.

1.  Choose **Save changes**. 

## AWS CLI
<a name="rds-proxy-endpoints.ModifyingEndpoint.CLI"></a>

 To modify a proxy endpoint, use the AWS CLI [modify-db-proxy-endpoint](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-proxy-endpoint.html) command with the following required parameters: 
+  `--db-proxy-endpoint-name` 

 Specify changes to the endpoint properties by using one or more of the following parameters: 
+  `--new-db-proxy-endpoint-name` 
+  `--vpc-security-group-ids`. Separate the security group IDs with spaces. 

 The following example renames the `my-endpoint` proxy endpoint to `new-endpoint-name`. 

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-proxy-endpoint \
  --db-proxy-endpoint-name {{my-endpoint}} \
  --new-db-proxy-endpoint-name {{new-endpoint-name}}
```
For Windows:  

```
aws rds modify-db-proxy-endpoint ^
  --db-proxy-endpoint-name {{my-endpoint}} ^
  --new-db-proxy-endpoint-name {{new-endpoint-name}}
```

## RDS API
<a name="rds-proxy-endpoints.ModifyingEndpoint.API"></a>

 To modify a proxy endpoint, use the RDS API [ModifyDBProxyEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBProxyEndpoint.html) operation. 