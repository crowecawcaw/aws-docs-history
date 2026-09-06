

# Disable the default endpoint for HTTP APIs
<a name="http-api-disable-default-endpoint"></a>

By default, clients can invoke your API by using the `execute-api` endpoint that API Gateway generates for your API. To ensure that clients can access your API only by using a custom domain name, disable the default `execute-api` endpoint. When you disable the default endpoint, it affects all stages of an API.

The following procedure shows how to disable the default endpoint for an HTTP API.

------
#### [ AWS Management Console ]

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose an HTTP API.

1. Choose your API's ID to open the **API details** page.

1. On **API details**, choose **Edit**.

1. For **Default endpoint**, select **Disable**.

1. Choose **Save**.

   If you turn on automatic deployments for your stage, you do not need to redeploy your API for the change to take effect. Otherwise, you must redeploy your API.

1. (Optional) Choose **Deploy**, and then redeploy your API or create a new stage for the change to take effect.

------
#### [ AWS CLI ]

The following [update-domain-name](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/update-domain-name.html) command disables the default endpoint for an HTTP API:

```
aws apigatewayv2 update-api \
    --api-id {{abcdef123}} \
    --disable-execute-api-endpoint
```

After you disable the default endpoint, you must deploy your API for the change to take effect, unless automatic deployments are enabled.

The following [create-deployment](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/create-deployment.html) command creates a deployment:

```
aws apigatewayv2 create-deployment \
    --api-id {{abcdef123}} \
    --stage-name {{dev}}
```

------