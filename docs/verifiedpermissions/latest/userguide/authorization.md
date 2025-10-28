# Implementing authorization in Amazon Verified Permissions

After you build your policy store, policies, templates, schema, and authorization model, you're
ready to start authorizing requests using Amazon Verified Permissions. To implement Verified Permissions authorization, you
must combine configuration of authorization policies in AWS with integration in an application. To
integrate Verified Permissions with your application, add an AWS SDK and implement the methods that
invoke the Verified Permissions API and generate authorization decisions against your policy store.

Authorization with Verified Permissions is useful for _UX permissions_
and _API permissions_ in your applications.

**UX permissions**

Control user access to your application UX. You can permit a user to view only
the exact forms, buttons, graphics and other resources that they need to access.
For example, when a user signs in, you might want to determine whether a
"Transfer funds" button is visible in their account. You can also control
actions that a user can take. For example, in same banking app you might want to
determine whether your user is permitted to change the category of a
transaction.

**API permissions**

Control user access to data. Applications are often part of a distributed
system and bring in information from external APIs. In the example of the
banking app where Verified Permissions has permitted the display of a "Transfer funds" button,
a more complex authorization decision must be made when your user initiates a
transfer. Verified Permissions can authorize the API request that lists the destination
accounts that are eligible transfer targets, and then the request to push the
transfer to the other account.

The examples that illustrate this content come from a [sample policy store](policy-stores-create.md#policy-stores-create.title "policy-stores-create.md#policy-stores-create.title"). To follow along, create the
**DigitalPetStore** sample policy store in your testing environment.

For an end to end sample application that implements UX permissions using batch
authorization, see [Use Amazon Verified Permissions for fine-grained authorization at scale](https://aws.amazon.com/blogs/security/use-amazon-verified-permissions-for-fine-grained-authorization-at-scale/ "https://aws.amazon.com/blogs/security/use-amazon-verified-permissions-for-fine-grained-authorization-at-scale/") on the _AWS
Security Blog_.

###### Topics

- [Available API operations for authorization](#authorization-operations "#authorization-operations")
- [Testing your authorization model](authorization-testing.md "authorization-testing.md")
- [Integrating your authorization models with applications](authorization-sdk.md "authorization-sdk.md")

## Available API operations for authorization

The Verified Permissions API has the following authorization operations.

**[IsAuthorized](../apireference/API_IsAuthorized.md "../apireference/API_IsAuthorized.md")**

The `IsAuthorized` API operation is the entry point to
authorization requests with Verified Permissions. You must submit principal, action,
resource, context, and entities elements. Verified Permissions evaluates your request
against all policies in the requested policy store that apply to the entities in the
request.

**[IsAuthorizedWithToken](../apireference/API_IsAuthorizedWithToken.md "../apireference/API_IsAuthorizedWithToken.md")**

The `IsAuthorizedWithToken` operation generates an
authorization request from user data in JSON web tokens (JWTs). Verified Permissions
works directly with OIDC providers like Amazon Cognito as an identity source in your policy store. Verified Permissions
populates all attributes to the principal in your request from the claims in
users' ID or access tokens. You can authorize actions and resources from
user attributes or group membership in an identity source.

You can't include information about group or user principal types in an
`IsAuthorizedWithToken` request. You must populate all
principal data to the JWT that you provide.

**[BatchIsAuthorized](../apireference/API_BatchIsAuthorized.md "../apireference/API_BatchIsAuthorized.md")**

The `BatchIsAuthorized` operation processes multiple
authorization decisions for a single principal or resource in a single API
request. This operation groups requests into a single batch operation that
minimizes [quota usage](quotas.md#quotas-tps.title "quotas.md#quotas-tps.title") and returns
authorization decisions for each of up to 30 complex nested actions. With
batch authorization for a single resource, you can filter the actions that a
user can take on a resource. With batch authorization for a single
principal, you can filter for the resources that a user can take action
on.

**[BatchIsAuthorizedWithToken](../apireference/API_BatchIsAuthorizedWithToken.md "../apireference/API_BatchIsAuthorizedWithToken.md")**

The `BatchIsAuthorizedWithToken` operation processes multiple
authorization decisions for a single principal in one API request. The
principal is provided by your policy store identity source in an ID or access token.
This operation groups requests into a single batch operation that minimizes
[quota usage](quotas.md#quotas-tps.title "quotas.md#quotas-tps.title") and returns
authorization decisions for each of up to 30 requests for actions and
resources. In your policies, you can authorize their access from their
attributes or their group membership in a user directory.

Like with `IsAuthorizedWithToken`, you can't include
information about group or user principal types in a
`BatchIsAuthorizedWithToken` request. You must populate all
principal data to the JWT that you provide.
