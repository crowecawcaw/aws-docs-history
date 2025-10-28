# Design your game client

service

We recommend that you implement a game client service that authenticates your players and
communicates with the Amazon GameLift Servers API. By implementing a custom game client service, you
can:

- Customize authentication for your players.
- Control how Amazon GameLift Servers matches and starts game sessions.
- Use your player database for player attributes such as skill rating for
  matchmaking instead of trusting the client.
  Using a game client service also reduces security risks introduced by game clients
  interacting directly with your Amazon GameLift Servers API.

## Authenticating

your players

You can use Amazon Cognito and player session IDs to authenticate your game clients. To
manage the lifecycle and properties of your player identities, use Amazon Cognito user pools.

If you prefer, build a custom identity solution and host it on AWS. You can also use
Lambda authorizers for custom authorization logic with API Gateway.

###### Additional resources:

- [Using identity pools
  (federated identities)](../../../cognito/latest/developerguide/identity-pools.md "../../../cognito/latest/developerguide/identity-pools.md") (Amazon Cognito Developer Guide)
- [Getting started with user pools](../../../cognito/latest/developerguide/getting-started-user-pools.md "../../../cognito/latest/developerguide/getting-started-user-pools.md") (Amazon Cognito Developer Guide)
- [How
  to Set Up Player Authentication with Amazon Cognito](https://aws.amazon.com/blogs/gametech/how-to-set-up-player-authentication-with-amazon-cognito/ "https://aws.amazon.com/blogs/gametech/how-to-set-up-player-authentication-with-amazon-cognito/") (AWS for Games
  Blog)
