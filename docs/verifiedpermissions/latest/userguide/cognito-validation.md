# Client and audience validation for Amazon Cognito

When you add an identity source to a policy store, Verified Permissions has configuration options that verify
that ID and access tokens are being used as intended. This validation happens in the
processing of `IsAuthorizedWithToken` and
`BatchIsAuthorizedWithToken` API requests. The behavior differs between
ID and access tokens, and between Amazon Cognito and OIDC identity sources. With Amazon Cognito user pools
providers, Verified Permissions can validate the client ID in both ID and access tokens. With OIDC
providers, Verified Permissions can validate the client ID in ID tokens, and the audience in access
tokens.

A _client ID_ is an identifier associated with the
identity provider instance that your application uses, for example
`1example23456789`. An _audience_ is a
URL path associated with the intended _relying party_,
or destination, of the access token, for example
`https://mytoken.example.com`. When using access tokens, the
`aud` claim is always associated with the audience.

Amazon Cognito ID tokens have an `aud` claim that contains the [app client](../../../cognito/latest/developerguide/user-pool-settings-client-apps.md "../../../cognito/latest/developerguide/user-pool-settings-client-apps.md") ID. Access tokens have a `client_id`
claim that also contains the app client ID.

When you enter one or more values for **Client application
validation** in your identity source, Verified Permissions compares this list
of app client IDs to the ID token `aud` claim or the access token
`client_id` claim. Verified Permissions doesn't validate a relying-party
audience URL for Amazon Cognito identity sources.

## Client-side authorization for

JWTs

You might want to process JSON web tokens in your application and pass their claims to
Verified Permissions without using a policy store identity source. You can extract your entity attributes from
a JSON Web Token (JWT) and parse it into Verified Permissions.

This example shows how you might call Verified Permissions from an application using a
JWT.¹

```
async function authorizeUsingJwtToken(jwtToken) {

    const payload = await verifier.verify(jwtToken);

    let principalEntity = {
        entityType: "PhotoFlash::User", // the application needs to fill in the relevant user type
        entityId: payload["sub"], // the application need to use the claim that represents the user-id
    };
    let resourceEntity = {
        entityType: "PhotoFlash::Photo", //the application needs to fill in the relevant resource type
        entityId: "jane_photo_123.jpg", // the application needs to fill in the relevant resource id
    };
    let action = {
        actionType: "PhotoFlash::Action", //the application needs to fill in the relevant action id
        actionId: "GetPhoto", //the application needs to fill in the relevant action type
    };
    let entities = {
        entityList: [],
    };
    entities.entityList.push(...getUserEntitiesFromToken(payload));
    let policyStoreId = "PSEXAMPLEabcdefg111111"; // set your own policy store id

    const authResult = await client
        .isAuthorized({
        policyStoreId: policyStoreId,
        principal: principalEntity,
        resource: resourceEntity,
        action: action,
        entities,
        })
        .promise();

    return authResult;

}

function getUserEntitiesFromToken(payload) {
  let attributes = {};
  let claimsNotPassedInEntities = ['aud', 'sub', 'exp', 'jti', 'iss'];
  Object.entries(payload).forEach(([key, value]) => {
    if (claimsNotPassedInEntities.includes(key)) {
        return;
    }
    if (Array.isArray(value)) {
      var attibuteItem = [];
      value.forEach((item) => {
        attibuteItem.push({
          string: item,
        });
      });
      attributes[key] = {
        set: attibuteItem,
      };
    } else if (typeof value === 'string') {
      attributes[key] = {
        string: value,
      }
    } else if (typeof value === 'bigint' || typeof value ==='number') {
        attributes[key] = {
            long: value,
          }
    } else if (typeof value === 'boolean') {
        attributes[key] = {
            boolean: value,
       }
    }

  });

  let entityItem = {
    attributes: attributes,
    identifier: {
      entityType: "PhotoFlash::User",
      entityId: payload["sub"], // the application needs to use the claim that represents the user-id
    }
  };
  return [entityItem];
}
```

¹ This code example uses the [aws-jwt-verify](https://github.com/awslabs/aws-jwt-verify "https://github.com/awslabs/aws-jwt-verify") library for
verifying JWTs signed by OIDC-compatible IdPs.
