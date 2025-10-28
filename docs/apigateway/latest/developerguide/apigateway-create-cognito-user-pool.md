# Create an Amazon Cognito user pool for a REST API

Before integrating your API with a user pool, you must create the user pool in Amazon Cognito. Your user pool
configuration must follow all
[resource quotas for Amazon Cognito](../../../cognito/latest/developerguide/limits.md "../../../cognito/latest/developerguide/limits.md"). All user-defined Amazon Cognito variables such as groups, users,
and roles should use only alphanumeric characters. For instructions on how to create a user pool, see [Tutorial: Creating a user pool](../../../cognito/latest/developerguide/tutorial-create-user-pool.md "../../../cognito/latest/developerguide/tutorial-create-user-pool.md") in the _Amazon Cognito
Developer Guide_.

Note the user pool ID, client ID, and any client secret. The client must provide
them to Amazon Cognito for the user to register with the user pool, to sign in to the user
pool, and to obtain an identity or access token to be included in requests to call
API methods that are configured with the user pool. Also, you must specify the user
pool name when you configure the user pool as an authorizer in API Gateway, as described
next.

If you're using access tokens to authorize API method calls, be sure to configure the
app integration with the user pool to set up the custom scopes that you want on a given
resource server. For more information about using tokens with Amazon Cognito user pools, see [Using Tokens with User Pools](../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.md "../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.md"). For more information about resource servers, see [Defining Resource
Servers for Your User Pool](../../../cognito/latest/developerguide/cognito-user-pools-define-resource-servers.md "../../../cognito/latest/developerguide/cognito-user-pools-define-resource-servers.md").

Note the configured resource server identifiers and custom scope names. You need them
to construct the access scope full names for **OAuth Scopes**,
which
is used by the `COGNITO_USER_POOLS` authorizer.

![Amazon Cognito user pool resource servers and scopes](images/cognito-user-pool-custom-scopes-new-console.png)
