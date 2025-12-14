# GAMESEC03-BP02 Authenticate requests that are sent to your game

backend service

Authenticating requests that are sent to your game backend service
can block unwanted requests from succeeding.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

You should provide an authentication service for players to log
in, which should return secure short-lived tokens, such as a JSON
Web Token (JWT), to the game client when a player successfully
authenticates.

These tokens can include claim assertions that contain player
attributes and other relevant metadata. This relevant metadata can
be used in subsequent requests that are sent from the game client
to your game backend to authenticate requests and authorize them
in the context of the authenticated player. 

You have the option to either design and build your own player
authentication system, which would require ongoing improvement and
maintenance, or you can use the scalable and secure user sign-up,
sign-in, and access control features provided
by [Amazon Cognito](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/").

Amazon Cognito user pools include a user directory for
authentication and authorization. A user pool provides APIs that
you can integrate into your game for sign-up, sign-in, and
password reset workflows, which can be integrated with third-party
identity
providers. [Application Load Balancers](../../../elasticloadbalancing/latest/application/listener-authenticate-users.md "../../../elasticloadbalancing/latest/application/listener-authenticate-users.md")
and [Amazon API Gateway](../../../apigateway/latest/developerguide/apigateway-integrate-with-cognito.md "../../../apigateway/latest/developerguide/apigateway-integrate-with-cognito.md") both provide integrations with Cognito to
integrate user authentication for requests sent to your custom
game backends hosted with these services.

If your game supports anonymous access and you cannot authenticate
a player, you can use a client authentication approach to provide
a more secure experience when integrating with your game backend.
If your game client uses AWS services directly, requests to these
services must be signed using credentials. To provide credentials
to your game client for unauthenticated users, you can use the AWS
SDK to retrieve short-lived credentials
from [Amazon Cognito identity pools](../../../cognito/latest/developerguide/cognito-identity.md "../../../cognito/latest/developerguide/cognito-identity.md") that can be used to sign your
requests to AWS services. These credentials can be refreshed from
your game client. 

In addition to directly integrating with the AWS SDK from the game
client, you can also build your own game backend, using a service
such as
[Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/"), which supports custom authorization. By designing
your own game backend service, you can gain authoritative control
over requests with custom server-side logic. 

For more information on building a backend service for games
hosted using Amazon GameLift, see
[Design
your game client service](../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend.md "../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend.md").

**Customer example**

AnyCompany Games enhanced the security of their next title by
adopting a managed authentication and authorization approach.
Instead of maintaining a custom username and password system, they
used Amazon Cognito user pools to handle player sign-up and
sign-in, and identity pools to support anonymous access for
players trying the training mode before creating an account. They
also implemented custom authorization logic within the game to
recognize administrator roles defined in Cognito, granting those
users access to special in-game management features.

### Implementation steps

- Use Amazon Cognito user pools to manage authentication with
  secure tokens like JWTs, enabling features like sign-up,
  sign-in, and password resets.
- Retrieve short-lived credentials from Amazon Cognito
  identity pools for anonymous users to securely interact with
  AWS services.
- Implement custom game backends using Amazon API Gateway for
  custom server-side authentication logic.
