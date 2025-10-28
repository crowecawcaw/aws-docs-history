# Disable the default endpoint for HTTP APIs

By default, clients can invoke your API by using the `execute-api` endpoint that API Gateway generates for
your API. To ensure that clients can access your API only by using a custom domain name, disable the default
`execute-api` endpoint. When you disable the default endpoint, it affects all stages of an API.

The following procedure shows how to disable the default endpoint for an HTTP API.

AWS Management Console

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. Choose an HTTP API.
3. Choose your API's ID to open the **API details** page.
4. On **API details**, choose **Edit**.
5. For **Default endpoint**, select **Disable**.
6. Choose **Save**.

If you turn on automatic deployments for your stage, you do not need to redeploy your API for the
change to take effect. Otherwise, you must redeploy your API. 7. (Optional) Choose **Deploy**, and then redeploy your API or create a new stage for
the change to take effect.

AWS CLIThe following [update-domain-name](../../../cli/latest/reference/apigatewayv2/update-domain-name.md "../../../cli/latest/reference/apigatewayv2/update-domain-name.md") command disables the default endpoint for an HTTP API:

```
aws apigatewayv2 update-api \
    --api-id `abcdef123` \
    --disable-execute-api-endpoint
```

After you disable the default endpoint, you must deploy your API for the change to take effect, unless automatic
deployments are enabled.

The following [create-deployment](../../../cli/latest/reference/apigatewayv2/create-deployment.md "../../../cli/latest/reference/apigatewayv2/create-deployment.md") command creates a deployment:

```
aws apigatewayv2 create-deployment \
    --api-id `abcdef123` \
    --stage-name `dev`
```
