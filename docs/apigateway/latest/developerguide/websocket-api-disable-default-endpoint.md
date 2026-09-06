

# Disable the default endpoint for WebSocket APIs
<a name="websocket-api-disable-default-endpoint"></a>

By default, clients can invoke your API by using the `execute-api` endpoint that API Gateway generates for your API. To ensure that clients can access your API only by using a custom domain name, disable the default `execute-api` endpoint. When you disable the default endpoint, it affects all stages of an API.

The following procedure shows how to disable the default endpoint for a WebSocket API.

------
#### [ AWS Management Console ]

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose an WebSocket API.

1. Choose **API settings**.

1. On **API details**, choose **Edit**.

1. For **Default endpoint**, select **Inactive**.

1. Choose **Save changes**.

1. On the main navigation pane, choose **Routes**.

1. Choose **Deploy**, and then redeploy your API or create a new stage for the change to take effect.

------
#### [ AWS CLI ]

The following [update-api](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/update-api.html) command disables the default endpoint for an WebSocket API:

```
aws apigatewayv2 update-api \
    --api-id {{abcdef123}} \
    --disable-execute-api-endpoint
```

After you disable the default endpoint, you must deploy your API for the change to take effect.

The following AWS CLI command creates a deployment.

```
aws apigatewayv2 create-deployment \
    --api-id {{abcdef123}} \
    --stage-name {{dev}}
```

------