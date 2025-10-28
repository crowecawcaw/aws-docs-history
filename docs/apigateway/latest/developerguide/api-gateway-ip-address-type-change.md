# Change the IP address type of a REST API

You can change the IP address type by updating the API’s configuration. You can update the API's configuration
by using the AWS Management Console, the AWS CLI, AWS CloudFormation, or an AWS SDK. If you change the API’s IP address type, you don't redeploy
your API for the changes to take effect. Before you change the IP address type, confirm that any policies
controlling access to your APIs have been updated to account for IPv6 calls.

AWS Management Console###### To change the IP address type of a REST API

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. Choose a REST API.
3. Choose **API settings**, and then choose
   **Edit**.
4. For IP address type, select either **IPv4** or **Dualstack**.
5. Choose **Save changes**.

The change to your API's configuration will take effect immediately.

AWS CLI
The following [update-rest-api](../../../cli/latest/reference/apigateway/update-rest-api.md "../../../cli/latest/reference/apigateway/update-rest-api.md")
command updates an API to have an IP address type of dualstack:

```
aws apigateway update-rest-api \
    --rest-api-id abcd1234 \
    --patch-operations "op='replace',path='/endpointConfiguration/ipAddressType',value='dualstack'"
```

The output will look like the following:

```
{
    "id": "abcd1234",
    "name": "MyAPI",
    "description": "My API with a dualstack IP address type",
    "createdDate": "2025-02-04T11:47:06-08:00",
    "apiKeySource": "HEADER",
    "endpointConfiguration": {
        "types": [
            "REGIONAL"
        ],
        "ipAddressType": "dualstack"
    },
    "tags": {},
    "disableExecuteApiEndpoint": false,
    "rootResourceId": "efg456"
}
```
