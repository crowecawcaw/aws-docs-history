# Deleting a proxy endpoint

To delete an endpoint for your proxy, follow these instructions:

###### Note

You can't delete the default proxy endpoint that RDS Proxy automatically creates for each proxy.

When you delete a proxy, RDS Proxy automatically deletes all the associated endpoints.

###### To delete a proxy endpoint using the AWS Management Console

1. In the navigation pane, choose **Proxies**.
2. In the list, choose the proxy whose endpoint you want to endpoint. Click the proxy name to view its
   details page.
3. In the **Proxy endpoints** section, choose the endpoint that you want to delete. You
   can select one or more endpoints in the list, or click the name of a single endpoint to view the
   details page.
4. On the proxy details page, under the **Proxy endpoints** section, choose
   **Delete**. Or, on the proxy endpoint details page, for **Actions**,
   choose **Delete**.

To delete a proxy endpoint, run the
[delete-db-proxy-endpoint](../../../cli/latest/reference/rds/delete-db-proxy-endpoint.md "../../../cli/latest/reference/rds/delete-db-proxy-endpoint.md") command with
the following required parameters:

- `--db-proxy-endpoint-name`

The following command deletes the proxy endpoint named `my-endpoint`.

For Linux, macOS, or Unix:

```
aws rds delete-db-proxy-endpoint \
  --db-proxy-endpoint-name `my-endpoint`

```

For Windows:

```
aws rds delete-db-proxy-endpoint ^
  --db-proxy-endpoint-name `my-endpoint`

```

To delete a proxy endpoint with the RDS API, run the
[DeleteDBProxyEndpoint](../APIReference/API_DeleteDBProxyEndpoint.md "../APIReference/API_DeleteDBProxyEndpoint.md") operation. Specify
the name of the proxy endpoint for the `DBProxyEndpointName` parameter.
