

# Attach a JWT authorizer to methods and require scopes

After you create a JWT authorizer, you attach it to the methods that it protects. You set the authorization type to `JWT`, reference the authorizer, and optionally require authorization scopes for the method. One authorizer can serve many methods, and each method can require its own scopes.

API Gateway reads a method's scopes from the token's `scope` or `scp` claim. A request passes the scope check when the token carries at least one of the method's scopes. For example, a method that requires `orders:read` accepts a token whose `scope` claim contains `orders:read`, even if the token also carries other scopes. A valid token that carries none of the method's scopes receives a `403 Forbidden` response.

**Note**  
Amazon Cognito names scopes in the form `{{resource-server}}/{{scope}}`, such as `orders/read`. If a JWT authorizer trusts an Amazon Cognito user pool and other issuers, list each scope form that a method accepts. A method passes when the token carries any one of its listed scopes.

You can mix authorizer types across the methods of one API. For example, one method can use a JWT authorizer, and another can use a Lambda authorizer. Each method uses the authorizer that you attach to it.

## Attach a JWT authorizer to a method using the console
<a name="rest-api-jwt-authorizer-methods.console"></a>

The following steps show how to attach a JWT authorizer to a method and require a scope by using the console.

**To attach a JWT authorizer to a method using the console**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose a REST API.

1. In the main navigation pane, choose **Resources**.

1. Choose a method, for example, **GET**.

1. On the **Method request** tab, under **Method request settings**, choose **Edit**.

1. For **Authorization**, choose your JWT authorizer, which appears under **JWT authorizers**.

1. (Optional) For **Authorization scopes**, enter a scope, for example, `orders:read`, and then choose **Add**. Repeat for each scope that the method accepts. A request passes when its token carries at least one of the listed scopes.

1. Choose **Save**.

To require a different scope on another method, repeat these steps for that method. For example, require the `orders:write` scope on the `POST` method of the same resource.

## Attach a JWT authorizer to a method using the AWS CLI
<a name="rest-api-jwt-authorizer-methods.cli"></a>

The following [put-method](https://docs.aws.amazon.com/cli/latest/reference/apigateway/put-method.html) command attaches a JWT authorizer to a method and requires the `orders:read` scope.

```shell
aws apigateway put-method \
    --rest-api-id {{api-id}} \
    --resource-id {{resource-id}} \
    --http-method GET \
    --authorization-type JWT \
    --authorizer-id {{authorizer-id}} \
    --authorization-scopes orders:read
```

To require a different scope on another method, run the command again with that method and its scope. The following command requires the `orders:write` scope on the `POST` method of the same resource.

```shell
aws apigateway put-method \
    --rest-api-id {{api-id}} \
    --resource-id {{resource-id}} \
    --http-method POST \
    --authorization-type JWT \
    --authorizer-id {{authorizer-id}} \
    --authorization-scopes orders:write
```

**Important**  
Changes to a method take effect only after you deploy the API. After you attach an authorizer or change a method's scopes, deploy the API to a stage. For more information, see [Deploy REST APIs in API Gateway](how-to-deploy-api.md).