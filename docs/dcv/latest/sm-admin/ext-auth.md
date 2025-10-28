# Configuring an external authorization server

The authorization server is the server that is responsible for authenticating and authorizing the client SDKs and
Agents.

By default, Session Manager uses the Broker as the authorization server to generate OAuth 2.0
access tokens for client SDKs and software statements for Agents. If you use the Broker as
the authorization server, no additional configuration is required.

You can configure Session Manager to use Amazon Cognito as an external authorization server instead of the Broker. For more information,
about Amazon Cognito, see the [Amazon Cognito Developer Guide](../../../cognito/latest/developerguide/what-is-amazon-cognito.md "../../../cognito/latest/developerguide/what-is-amazon-cognito.md").

###### To use Amazon Cognito as the authorization server

1. Create a new Amazon Cognito user pool. For more information about user pools, see [Features of Amazon Cognito](../../../cognito/latest/developerguide/what-is-amazon-cognito.md#feature-overview "../../../cognito/latest/developerguide/what-is-amazon-cognito.md#feature-overview")
   in the _Amazon Cognito Developer Guide_.

Use the [create-user-pool](../../../cli/latest/reference/cognito-idp/create-user-pool.md "../../../cli/latest/reference/cognito-idp/create-user-pool.md")
command, and specify a pool name and the Region in which to create it.

In this example, we name the pool `dcv-session-manager-client-app` and we create
it in `us-east-1`.

```
`$` aws cognito-idp create-user-pool --pool-name `dcv-session-manager-client-app` --region `us-east-1`
```

Example output

```
{
    "UserPoolClient": {
        "UserPoolId": "us-east-1_QLEXAMPLE",
        "ClientName": "dcv-session-manager-client-app",
        "ClientId": "15hhd8jij74hf32f24uEXAMPLE",
        "LastModifiedDate": 1602510048.054,
        "CreationDate": 1602510048.054,
        "RefreshTokenValidity": 30,
        "AllowedOAuthFlowsUserPoolClient": false
    }
}
```

Make a note of the `userPoolId`, you'll need it in the next step. 2. Create a new domain for your user pool. Use the [create-user-pool-domain](../../../cli/latest/reference/cognito-idp/create-user-pool-domain.md "../../../cli/latest/reference/cognito-idp/create-user-pool-domain.md")
command, and specify a domain name and the `userPoolId` of the user pool that you created in the
previous step.

In this example, the domain name is `mydomain-544fa30f-c0e5-4a02-8d2a-a3761EXAMPLE` and
we create it in `us-east-1`.

```
`$` aws cognito-idp create-user-pool-domain --domain `mydomain-544fa30f-c0e5-4a02-8d2a-a3761EXAMPLE` --user-pool-id `us-east-1_QLEXAMPLE` --region `us-east-1`
```

Example output

```
{
    "DomainDescription": {
        "UserPoolId": "us-east-1_QLEXAMPLE",
        "AWSAccountId": "123456789012",
        "Domain": "mydomain-544fa30f-c0e5-4a02-8d2a-a3761EXAMPLE",
        "S3Bucket": "aws-cognito-prod-pdx-assets",
        "CloudFrontDistribution": "dpp0gtexample.cloudfront.net",
        "Version": "20201012133715",
        "Status": "ACTIVE",
        "CustomDomainConfig": {}
    }
}

```

The format of the user pool domain is as follows: `https://`domain_name`.auth.`region`.amazoncognito.com`.
In this example, the user pool domain is `https://mydomain-544fa30f-c0e5-4a02-8d2a-a3761EXAMPLE.auth.us-east-1.amazoncognito.com`. 3. Create a user pool client. Use the [create-user-pool-client](../../../cli/latest/reference/cognito-idp/create-user-pool-client.md "../../../cli/latest/reference/cognito-idp/create-user-pool-client.md") command and specify the `userPoolId` of the user pool that you created, a name for the
client, and the Region in which to create it. Also, include the `--generate-secret` option to specify that you want to
generate a secret for the user pool client being created.

In this case, the client name is `dcv-session-manager-client-app` and we create it in the `us-east-1` Region.

```
`$` aws cognito-idp create-user-pool-client --user-pool-id `us-east-1_QLEXAMPLE` --client-name `dcv-session-manager-client-app` --generate-secret --region `us-east-1`
```

Example output

```
{
    "UserPoolClient": {
        "UserPoolId": "us-east-1_QLEXAMPLE",
        "ClientName": "dcv-session-manager-client-app",
        "ClientId": "2l9273hp6k2ut5cugg9EXAMPLE",
        "ClientSecret": "1vp5e8nec7cbf4m9me55mbmht91u61hlh0a78rq1qki1lEXAMPLE",
        "LastModifiedDate": 1602510291.498,
        "CreationDate": 1602510291.498,
        "RefreshTokenValidity": 30,
        "AllowedOAuthFlowsUserPoolClient": false
    }
}

```

###### Note

Make a note of the `ClientId` and `ClientSecret`. You'll need to provide
this information to the developers for when they request access tokens for the
API requests. 4. Create a new OAuth2.0 resource server for the user pool. A resource server is a server for access-protected resources. It handles authenticated requests
for access tokens.

Use the [create-resource-server](../../../cli/latest/reference/cognito-idp/create-resource-server.md "../../../cli/latest/reference/cognito-idp/create-resource-server.md") command and specify the `userPoolId` of the user pool, a unique identifier and name for the resource server,
the scope, and the Region in which to create it.

In this example, we use `dcv-session-manager` as the identifier and the name, and we use `sm_scope`
as the scope name and description.

```
`$` aws cognito-idp create-resource-server --user-pool-id `us-east-1_QLEXAMPLE` --identifier `dcv-session-manager` --name `dcv-session-manager` --scopes ScopeName=`sm_scope`,ScopeDescription=`sm_scope` --region `us-east-1`
```

Example output

```
{
    "ResourceServer": {
        "UserPoolId": "us-east-1_QLEXAMPLE",
        "Identifier": "dcv-session-manager",
        "Name": "dcv-session-manager",
        "Scopes": [
        {
            "ScopeName": "sm_scope",
            "ScopeDescription": "sm_scope"
        }]
    }
}
```

5. Update the user pool client.

Use the [update-user-pool-client](../../../cli/latest/reference/cognito-idp/update-user-pool-client.md "../../../cli/latest/reference/cognito-idp/update-user-pool-client.md") command. Specify the `userPoolId` of
the user pool, the `ClientId` of the user pool client, and the Region.
For `--allowed-o-auth-flows`, specify `client_credentials` to
indicate that the client should get access tokens from the token endpoint by using a
combination of a client ID and a client secret. For
`--allowed-o-auth-scopes`, specify the resource server identifier and
the scope name as follows:
``resource_server_identifier`/`scope_name``.
Include the `--allowed-o-auth-flows-user-pool-client` to indicate that
the client is allowed to follow the OAuth protocol when interacting with Cognito
user pools.

```
`$` aws cognito-idp update-user-pool-client --user-pool-id `us-east-1_QLEXAMPLE` --client-id `2l9273hp6k2ut5cugg9EXAMPLE` --allowed-o-auth-flows client_credentials --allowed-o-auth-scopes `dcv-session-manager`/`sm_scope` --allowed-o-auth-flows-user-pool-client --region `us-east-1`
```

Example output

```
{
    "UserPoolClient": {
        "UserPoolId": "us-east-1_QLEXAMPLE",
        "ClientName": "dcv-session-manager-client-app",
        "ClientId": "2l9273hp6k2ut5cugg9EXAMPLE",
        "ClientSecret": "1vp5e8nec7cbf4m9me55mbmht91u61hlh0a78rq1qki1lEXAMPLE",
        "LastModifiedDate": 1602512103.099,
        "CreationDate": 1602510291.498,
        "RefreshTokenValidity": 30,
        "AllowedOAuthFlows": [
            "client_credentials"
        ],
        "AllowedOAuthScopes": [
            "dcv-session-manager/sm_scope"
        ],
        "AllowedOAuthFlowsUserPoolClient": true
    }
}
```

###### Note

The user pool is now ready to provide and authenticate access tokens. In this example, the URL for the authorization
server is `https://cognito-idp.`us-east-1`.amazonaws.com/`us-east-1_QLEXAMPLE`/.well-known/jwks.json`. 6. Test the configuration.

```
`$` curl -H "Authorization: Basic `echo -n `2l9273hp6k2ut5cugg9EXAMPLE`:`1vp5e8nec7cbf4m9me55mbmht91u61hlh0a78rq1qki1lEXAMPLE` | base64`" -H "Content-Type: application/x-www-form-urlencoded" -X POST "https://`mydomain-544fa30f-c0e5-4a02-8d2a-a3761EXAMPLE`.auth.`us-east-1`.amazoncognito.com/oauth2/token?grant_type=client_credentials&scope=`dcv-session-manager`/`sm_scope`"
```

Example output

```
{
"access_token":"eyJraWQiOiJGQ0VaRFpJUUptT3NSaW41MmtqaDdEbTZYb0RnSTQ5b2VUT0cxUUI1Q2VJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIybDkyNzNocDZrMnV0NWN1Z2c5dWg4ZGx0cCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiZGN2LXNlc3Npb24tbWFuYWdlclwvcGVybWlzc2lvbnMiLCJhdXRoX3RpbWUiOjE2MDI1MTMyODMsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy13ZXN0LTIuYW1hem9uYXdzLmNvbVwvdXMtd2VzdC0yX1FMZTA3SU9GViIsImV4cCI6MTYwMjUxNjg4MywiaWF0IjoxNjAyNTEzMjgzLCJ2ZXJzaW9uIjoyLCJqdGkiOiIyMDk2YTg4NS04YWQ0LTRmYjgtYjI2Mi1hMmNkNDk0OGZjNjYiLCJjbGllbnRfaWQiOiIybDkyNzNocDZrMnV0NWN1Z2c5dWg4ZGx0cCJ9.ZLZpS4CiiLq1X_VSm911hNT4g8A0FKZXScVJyyV0ijcyOfUOBcpgSMGqJagLYORFuYwLS5c7g4eO04wIwnw21ABGIDcOMElDPCJkrzjfLEPS_eyK3dNmlXDEvdS-Zkfi0HIDsd6audjTXKzHlZGScr6ROdZtId5dThkpEZiSx0YwiiWe9crAlqoazlDcCsUJHIXDtgKW64pSj3-uQQGg1Jv_tyVjhrA4JbD0k67WS2V9NW-uZ7t4zwwaUmOi3KzpBMi54fpVgPaewiVlUm_aS4LUFcWT6hVJjiZF7om7984qb2gOa14iZxpXPBJTZX_gtG9EtvnS9uW0QygTJRNgsw",
"expires_in":3600,
"token_type":"Bearer"
}

```

7. Register the external authorization server for use with the broker by using the [register-auth-server](register-auth-server.md "register-auth-server.md")
   command.

```
`$` sudo -u root dcv-session-manager-broker register-auth-server --url  https://cognito-idp.`us-east-1`.amazonaws.com/`us-east-1_QLEXAMPLE`/.well-known/jwks.json
```

Developers can now use the server to request access tokens. When requesting access tokens,
provide the client ID, client secret, and server URL generated here. For more information
about requesting access tokens, see [Create get an access token and make an API
request](../sm-dev/request.md "../sm-dev/request.md") in the*Amazon DCV Session Manager Developer
Guide*.
