# How to change a security policy

You can change the security policy for your API. If you are sending traffic to your APIs through your custom
domain name, the API and the custom domain name don't need to have the same security policy. When you invoke that
custom domain name, API Gateway uses the security policy of the API to negotiate the TLS handshake. However, for
consistency, we recommend that you use the same security policy for your custom domain name and API.

If you change your security policy, it takes about 15 minutes for the update to complete. You can monitor the
`apiStatus` of your API. As your API updates, the `apiStatus` is
`UPDATING` and when it completes, it will be `AVAILABLE`. When your API is updating, you can
still invoke it.

AWS Management Console###### To change the security policy of an API

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. Choose a REST API.
3. Choose **API settings**, and then choose
   **Edit**.
4. For **Security policy**, select a new policy that starts with `SecurityPolicy_`.
5. For **Endpoint access mode**, choose **Strict**.
6. Choose **Save changes**.

Redeploy your API for the changes to take effect. Because you changed the endpoint access mode to
strict, it will take about 15 minutes for the changes to fully propagate.

AWS CLI
The following [update-rest-api](../../../cli/latest/reference/apigateway/update-rest-api.md "../../../cli/latest/reference/apigateway/update-rest-api.md") command
updates an API to use the `SecurityPolicy_TLS13_1_3_2025_09` security policy:

```
aws apigateway update-rest-api \
    --rest-api-id abcd1234 \
    --patch-operations '[
        {
            "op": "replace",
            "path": "/securityPolicy",
            "value": "SecurityPolicy_TLS13_1_3_2025_09"
        },
        {
            "op": "replace",
            "path": "/endpointAccessMode",
            "value": "STRICT"
        }
    ]'
```

The output will look like the following:

```
{
    "id": "abcd1234",
    "name": "MyAPI",
    "description": "My API with a new security policy",
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
    "securityPolicy": "SecurityPolicy_TLS13_1_3_2025_09",
    "endpointAccessMode": "STRICT"
    "rootResourceId": "efg456"
}
```

The following [update-rest-api](../../../cli/latest/reference/apigateway/update-rest-api.md "../../../cli/latest/reference/apigateway/update-rest-api.md") command
updates a API that was using an enhanced security policy to use the `TLS_1_0` security
policy.

```
aws apigateway update-rest-api \
    --rest-api-id abcd1234 \
    --patch-operations '[
        {
            "op": "replace",
            "path": "/securityPolicy",
            "value": "TLS_1_0"
        },
        {
            "op": "replace",
            "path": "/endpointAccessMode",
            "value": ""
        }
    ]'
```

The output will look like the following:

```
{
    "id": "abcd1234",
    "name": "MyAPI",
    "description": "My API with a new security policy",
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
    "securityPolicy": "TLS_1_0",
    "rootResourceId": "efg456"
}
```
