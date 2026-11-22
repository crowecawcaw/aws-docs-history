

# Update a JWT authorizer

You update a JWT authorizer by replacing its whole configuration. API Gateway accepts a single `replace` operation on the `/jwtConfiguration` path, with the complete configuration as the value. API Gateway keeps nothing from the previous configuration, so any issuer or claim rule that you leave out is removed. API Gateway runs OIDC discovery again for every issuer on each update.

To change one part of the configuration, read the current configuration, edit it, and send it back. The following steps change an authorizer by using the AWS CLI.

**To update a JWT authorizer using the AWS CLI**

1. Read the current configuration with the [get-authorizer](https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-authorizer.html) command and save the `jwtConfiguration` object to a file named `jwt-config.json`.

1. Edit the file. For example, to add a second issuer, append it to the `issuers` list. Keep the issuers that you still trust, because API Gateway removes any issuer that is not in the file. Remove `jwksUri` from each issuer.

1. Send the whole file back as the value of a `replace` operation on the `/jwtConfiguration` path.

   ```shell
   aws apigateway update-authorizer \
       --rest-api-id {{api-id}} \
       --authorizer-id {{authorizer-id}} \
       --patch-operations "$(jq -n --rawfile v jwt-config.json \
           '[{op:"replace",path:"/jwtConfiguration",value:$v}]')"
   ```

This pattern supports an identity provider migration. To migrate, add the new issuer alongside the old one and let clients move over. When all clients use the new issuer, remove the old issuer and update the authorizer again.

The `get-authorizer` response includes a resolved `jwksUri` for each issuer. Remove `jwksUri` from each issuer before you send the configuration back in a `replace` operation. API Gateway resolves `jwksUri` through OIDC discovery. If you include it, API Gateway rejects the request with a `400` error.

## Update a JWT authorizer using the console
<a name="rest-api-jwt-authorizer-update.console"></a>

The following steps show how to update a JWT authorizer by using the console. When you save, the console replaces the authorizer's configuration, so keep the issuers and claim rules that you still need.

**To update a JWT authorizer using the console**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose a REST API.

1. In the main navigation pane, choose **Authorizers**.

1. Select the JWT authorizer that you want to update, and then choose **Edit**.

1. (Optional) For **Authorizer name**, enter a new name.

1. (Optional) For **Identity source**, enter the request header that carries the token.

1. (Optional) For **Allowed signing algorithms**, add or remove algorithms. You must keep at least one algorithm.

1. Under **Issuers**, update the identity providers that issue tokens for this API:

   1. To change an issuer, edit its **Issuer URL** or **Audiences**.

   1. To change an issuer's claim rules, expand **Additional claims - optional**, and then choose **Edit additional claims**. If the issuer has no claim rules, choose **Add additional claims**. Add, change, or remove claim rules, and then choose **Save**.

   1. To add an issuer, choose **Add issuer**, and then enter its details. You can add up to 10 issuers.

   1. To remove an issuer, choose **Remove issuer** for that issuer.

1. Choose **Save changes**.

## Convert an existing authorizer to a JWT authorizer
<a name="rest-api-jwt-authorizer-update.convert"></a>

You can't change an authorizer's type in the console. To convert an authorizer, use the AWS CLI or the API.

You can convert a `TOKEN` authorizer or an Amazon Cognito user pool authorizer to a JWT authorizer. Send a `replace` operation on the `/type` path to set the type to `JWT`, together with a `replace` operation on the `/jwtConfiguration` path that supplies the new configuration, in one request.

When you convert an authorizer to a JWT authorizer, remove the `authorizerUri`, `authorizerCredentials`, `providerARNs`, `identityValidationExpression`, and `authorizerResultTtlInSeconds` fields. For a field that doesn't support a `remove` operation, use a `replace` operation with an empty value. API Gateway returns a `400` error if any of these fields has a value.

After you convert the authorizer, change the authorization type to `JWT` on each method that uses it, and then deploy the API. For more information, see [Attach a JWT authorizer to methods and require scopes](rest-api-jwt-authorizer-methods.md).

**Important**  
Changes to an authorizer take effect only after you deploy the API. After you update an authorizer, deploy the API to a stage. For more information, see [Deploy REST APIs in API Gateway](how-to-deploy-api.md).