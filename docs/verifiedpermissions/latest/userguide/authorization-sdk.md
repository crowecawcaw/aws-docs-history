# Integrating your authorization models with applications

To implement Amazon Verified Permissions in your application, you must define the policies and schema
that you want your app to enforce. With your authorization model in place and tested,
your next step is to start generating API requests from the point of enforcement. To do
this, you must set up application logic to collect user data and populate it to
authorization requests.

###### How an app authorizes requests with Verified Permissions

1. Gather information about the current user. Typically, a user's details are
   provided in the details of an authenticated session, like a JWT or web session
   cookie. This user data might originate from an Amazon Cognito [identity source](identity-sources.md#identity-sources.title "identity-sources.md#identity-sources.title") linked to your
   policy store or from another [OpenID
   Connect (OIDC) provider](cognito-validation.md#identity-sources-other-idp.title "cognito-validation.md#identity-sources-other-idp.title").
2. Gather information about the resource that a user wants to access. Typically,
   your application will receive information about the resource when a user makes a
   selection that requires your app to load a new asset.
3. Determine the action that your user wants to take.
4. Generate an authorization request to Verified Permissions with the principal, action,
   resource, and entities for your user's attempted operation.Verified Permissions evaluates the
   request against the policies in your policy store and returns an authorization
   decision.
5. Your application reads the allow or deny response from Verified Permissions and enforces the
   decision on the user's request.
   Verified Permissions API operations are built into AWS SDKs. To include Verified Permissions in an app, integrate
   the AWS SDK for your chosen language into the app package.

To learn more and download AWS SDKs, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").

The following are links to documentation for Verified Permissions resources in various AWS SDKs.

- [AWS SDK for .NET](../../../sdkfornet/v3/apidocs/items/VerifiedPermissions/NVerifiedPermissions.md "../../../sdkfornet/v3/apidocs/items/VerifiedPermissions/NVerifiedPermissions.md")
- [AWS SDK for C++](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-verifiedpermissions/html/class_aws_1_1_verified_permissions_1_1_verified_permissions_client.html "https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-verifiedpermissions/html/class_aws_1_1_verified_permissions_1_1_verified_permissions_client.html")
- [AWS SDK for Go](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/verifiedpermissions "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/verifiedpermissions")
- [AWS SDK for Java](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/verifiedpermissions/package-summary.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/verifiedpermissions/package-summary.html")
- [AWS SDK for JavaScript](../../../AWSJavaScriptSDK/v3/latest/client/verifiedpermissions.md "../../../AWSJavaScriptSDK/v3/latest/client/verifiedpermissions.md")
- [AWS SDK for PHP](../../../aws-sdk-php/v3/api/api-verifiedpermissions-2021-12-01.md "../../../aws-sdk-php/v3/api/api-verifiedpermissions-2021-12-01.md")
- [AWS SDK for Python (Boto)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html")
- [AWS SDK for Ruby](../../../sdk-for-ruby/v3/api/Aws/VerifiedPermissions/Client.md "../../../sdk-for-ruby/v3/api/Aws/VerifiedPermissions/Client.md")
- [AWS SDK for Rust](https://docs.rs/aws-sdk-verifiedpermissions/latest/aws_sdk_verifiedpermissions/ "https://docs.rs/aws-sdk-verifiedpermissions/latest/aws_sdk_verifiedpermissions/")
  The following AWS SDK for JavaScript example for `IsAuthorized` originates from [Simplify fine-grained authorization with Amazon Verified Permissions and Amazon Cognito](https://aws.amazon.com/blogs/security/simplify-fine-grained-authorization-with-amazon-verified-permissions-and-amazon-cognito/ "https://aws.amazon.com/blogs/security/simplify-fine-grained-authorization-with-amazon-verified-permissions-and-amazon-cognito/").

```
const authResult = await avp.isAuthorized({
    principal: 'User::"alice"',
    action: 'Action::"view"',
    resource: 'Photo::"VacationPhoto94.jpg"',
    // whenever our policy references attributes of the entity,
    // isAuthorized needs an entity argument that provides
    // those attributes
    entities: {
       entityList: [
         {
            "identifier": {
                "entityType": "User",
                "entityId": "alice"
            },
            "attributes": {
                "location": {
                    "String": "USA"
                }
            }
         }
       ]
    }
});
```

###### More developer resources

- [Amazon Verified Permissions workshop](https://catalog.workshops.aws/verified-permissions-in-action "https://catalog.workshops.aws/verified-permissions-in-action")
- [Amazon Verified Permissions -
  Resources](https://aws.amazon.com/verified-permissions/resources/ "https://aws.amazon.com/verified-permissions/resources/")
- [Implement custom authorization policy provider for ASP.NET
  Core apps using Amazon Verified Permissions](https://aws.amazon.com/blogs/dotnet/implement-a-custom-authorization-policy-provider-for-asp-net-core-apps-using-amazon-verified-permissions/ "https://aws.amazon.com/blogs/dotnet/implement-a-custom-authorization-policy-provider-for-asp-net-core-apps-using-amazon-verified-permissions/")
- [Build an entitlement service for business applications using
  Amazon Verified Permissions](https://aws.amazon.com/blogs/security/build-an-entitlement-service-for-business-applications-using-amazon-verified-permissions/ "https://aws.amazon.com/blogs/security/build-an-entitlement-service-for-business-applications-using-amazon-verified-permissions/")
- [Simplify fine-grained authorization with Amazon Verified Permissions and
  Amazon Cognito](https://aws.amazon.com/blogs/security/simplify-fine-grained-authorization-with-amazon-verified-permissions-and-amazon-cognito/ "https://aws.amazon.com/blogs/security/simplify-fine-grained-authorization-with-amazon-verified-permissions-and-amazon-cognito/")
