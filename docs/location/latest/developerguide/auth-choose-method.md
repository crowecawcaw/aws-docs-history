# Choosing an authentication method

Amazon Location Service supports three authentication methods. Use the following guidance to choose
the right method for your application.

## Method comparison

Authentication method comparison| Criteria | API keys | Amazon Cognito | IAM |
| --- | --- | --- | --- |
| Supported APIs | Maps, Places, Routes | All APIs | All APIs |
| User authentication required | No | Optional | Yes |
| Relative performance | Faster (fewer round trips, cached tiles) | Slower (token exchange required) | Standard (SigV4 signing) |
| Can combine with other methods | No | Yes | Yes |
| Best for | Public web/mobile apps needing maps, places, or routes | Apps needing anonymous access to all APIs, or custom auth<br>flows | Server-side apps, internal tools, administrative<br>operations |

## When to use API keys

Use API keys when:

- Your application only needs Maps, Places, or Routes APIs.
- You want the simplest integration with the fewest round trips.
- You don't need to authenticate individual users.

API keys are typically faster than Amazon Cognito because simpler authentication means
fewer round trips to the service and cached requests when getting the same map tile
again.

## When to use Amazon Cognito

Use Amazon Cognito when:

- Your application needs access to Geofences, Trackers, or other APIs not
  available with API keys.
- You want to combine multiple authentication providers (social login,
  SAML, or your own identity system).
- You need both authenticated and unauthenticated user support in the same
  application.
- You want IP-based restrictions using IAM policy conditions.

For more information about using Federated Identities with Amazon Cognito, see [Getting Started with Federated Identities](../../../cognito/latest/developerguide/getting-started-with-identity-pools.md "../../../cognito/latest/developerguide/getting-started-with-identity-pools.md") in the
Amazon Cognito Developer Guide.

## When to use IAM

Use IAM when:

- Your application runs on AWS compute services (Amazon EC2, Lambda,
  Amazon ECS).
- You need full control over permissions with resource-level policies and
  conditions.
- You're building server-side or backend services.
- You need audit trails with AWS CloudTrail.
