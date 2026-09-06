

# Authentication troubleshooting
<a name="authentication-troubleshooting"></a>

## Problem: WebSocket connection returns HTTP 401
<a name="problem-websocket-401"></a>

The Fleet Manager UI cannot establish a WebSocket connection for real-time telemetry. The browser developer tools show the WebSocket upgrade request returning HTTP 401. This occurs because the `$connect` route on the WebSocket API requires a valid Cognito JWT, passed as the `token` query parameter on the upgrade URL.

### Diagnosis
<a name="diagnosis-7"></a>

1. Confirm the WebSocket endpoint is the correct one from the CloudFormation outputs:

   ```
   STAGE=staging
   aws cloudformation describe-stacks \
     --stack-name cms-$STAGE-ui \
     --query "Stacks[0].Outputs[?OutputKey=='WebSocketEndpoint'].OutputValue" \
     --output text
   ```

1. Test the endpoint directly using a WebSocket client. The upgrade URL must include the `?token=<jwt>` query parameter. An upgrade without the parameter, or with an expired token, returns HTTP 401:

   ```
   # Install wscat if needed: npm install -g wscat
   JWT=<id-token-from-cognito>
   WS_ENDPOINT=<websocket-endpoint-from-cfn-outputs>
   wscat -c "$WS_ENDPOINT?token=$JWT"
   ```

1. If the endpoint returns HTTP 401 even with a valid token, check the authorizer Lambda logs:

   ```
   aws logs tail /aws/lambda/cms-$STAGE-websocket-authorizer \
     --since 5m --follow
   ```

### Resolution
<a name="resolution-25"></a>

 **If the upgrade request lacks the token parameter:** 

The WebSocket client must append `?token=<cognito-id-token>` to the upgrade URL. In the Fleet Manager UI, the `runtimeConfig.wsEndpoint` field supplies the base URL; the UI code appends the token automatically when the user is authenticated. If the UI is not appending the token, verify that the `wsEndpoint` field in `runtimeConfig.json` is populated (see [Problem: Fleet Manager UI shows missing endpoints after fresh deploy](runtimeconfig-troubleshooting.md#problem-runtimeconfig-endpoint-race)).

 **If the token is present but expired:** 

Cognito ID tokens expire after one hour by default. The UI refreshes tokens automatically using the refresh token flow. If the user has been inactive long enough for the refresh token to expire, they must sign in again. The session lifetime is configurable via the Cognito User Pool token expiry settings.

 **If the WebSocket API is deployed with `cms.allow_unauth_websocket=true`:** 

This CDK context flag disables the `$connect` authorizer and allows anonymous WebSocket connections. This setting is intended only for demos. In production, ensure `cms.allow_unauth_websocket` is set to `false` (the default). Redeploy the UI stack with the flag absent or explicitly set to false:

```
cd deployment
cdk deploy cms-$STAGE-ui \
  --context cms.allow_unauth_websocket=false \
  --require-approval never
```

 **For fleet-operator users:** 

Fleet-operator connections must include both `?token=<jwt>` and `?fleetId=<fleet-id>` on the upgrade URL. Platform-admin users connect without the `fleetId` parameter and receive all-fleet telemetry.

If these instructions do not address your issue, visit the [Issues](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws/issues) section of the GitHub repository or contact [AWS Support](https://support.console.aws.amazon.com/support/home#/).