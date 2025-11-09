# Authenticate and authorize with Inbound Auth and Outbound Auth

This section shows you how to implement authentication and authorization for your agent
runtime using OAuth and JWT bearer tokens with [AgentCore Identity](identity.md "identity.md"). You'll learn how to set up Cognito user pools,
configure your agent runtime for JWT authentication (Inbound Auth), and implement OAuth-based access to
third-party resources (outbound Auth).

For a complete example, see [https://github.com/awslabs/amazon-bedrock-agentcore-samples/](https://github.com/awslabs/amazon-bedrock-agentcore-samples/ "https://github.com/awslabs/amazon-bedrock-agentcore-samples/").

For information about using OAuth with an MCP server, see [Deploy MCP servers in AgentCore Runtime](runtime-mcp.md "runtime-mcp.md").

Amazon Bedrock AgentCore runtime provides two authentication mechanisms for hosted agents:

**IAM SigV4 Authentication**

The default authentication and authorization mechanism that works
automatically without additional configuration, similar to other AWS
APIs.

**X-Amzn-Bedrock-AgentCore-Runtime-User-Id Header**

If your solution requires the hosted agent to retrieve OAuth tokens on behalf
of end users (using Authorization Code Grant), you can specify the user
identifier by including the `X-Amzn-Bedrock-AgentCore-Runtime-User-Id` header in
your requests.

###### Note

Invoking InvokeAgentRuntime with the
`X-Amzn-Bedrock-AgentCore-Runtime-User-Id header` will require a new IAM
action: `bedrock-agentcore:InvokeAgentRuntimeForUser`, in addition to the
existing `bedrock-agentcore:InvokeAgentRuntime` action.

**Security Best Practices for X-Amzn-Bedrock-AgentCore-Runtime-User-Id Header**

While IAM authentication secures the API access, the
`X-Amzn-Bedrock-AgentCore-Runtime-User-Id` header requires additional security
considerations. Only trusted principals with the
`bedrock-agentcore:InvokeAgentRuntimeForUser` permission should be allowed to set
this header. The user-id value should ideally be derived from the authenticated
principal’s context (for example, IAM context or user token) rather than accepting
arbitrary values. This prevents scenarios where an authenticated user could
potentially impersonate another user by manually specifying a different `user-id`.

Implement audit logging to track the relationship between the authenticated
principal and the `user-id` being passed.

Remember that Amazon Bedrock AgentCore
treats this header value as an opaque identifier and relies on your
application's logic to maintain the security boundary between authenticated
users and their corresponding `user-id` values.

**JWT Bearer Token Authentication**

You can configure your agent runtime to accept JWT bearer tokens by providing
authorizer configuration during agent creation.

This configuration requires:

- Discovery URL - A string that must match the pattern
  `^.+/\.well-known/openid-configuration$` for OpenID
  Connect discovery URLs
- Allowed audiences - A list of permitted audiences that will be
  validated against the aud claim in the JWT token
- Allowed clients - A list of permitted client identifiers that will be
  validated against the client_id claim in the JWT token

###### Note

An AgentCore Runtime can support either IAM SigV4 or JWT Bearer Token based inbound auth, but not both simultaneously.
You can always create different versions of your AgentCore Runtime and configure them for different
inbound authorization types.

When you create a runtime with Amazon Bedrock AgentCore, a Workload Identity is created
automatically for your runtime with AgentCore Identity service.

###### Topics

- [JWT inbound authorization and OAuth outbound access sample](#oauth-sample-overview "#oauth-sample-overview")
- [Prerequisites](#oauth-prerequisites "#oauth-prerequisites")
- [Step 1: Prepare your agent](#prepare-agent "#prepare-agent")
- [Step 2: Set up AWS Cognito user pool and add a user](#setup-cognito "#setup-cognito")
- [Step 3: Deploy your agent](#deploy-agent "#deploy-agent")
- [Step 4: Use bearer token to invoke your agent](#invoke-agent "#invoke-agent")
- [Step 5: Set up your agent to access tools using OAuth](#oauth-outbound-access "#oauth-outbound-access")
- [Step 6: (Optional) Propagate a JWT token to AgentCore Runtime](#oauth-propagate-jwt-token "#oauth-propagate-jwt-token")
- [Troubleshooting](#troubleshooting "#troubleshooting")

## JWT inbound authorization and OAuth outbound access sample

This guide walks you through the process of setting up your agent runtime to be
invoked with an OAuth compliant access token using JWT format. The sample agent will be
authorized using AWS Cognito access tokens. Later, you'll also learn how the agent
code can fetch Google tokens on behalf of the user to check Google Drive and fetch
contents.

###### What you'll learn

In this guide, you'll learn how to:

- Set up Cognito user pool, add a user, and get a bearer token for the
  user
- Set up your agent runtime to use the Cognito user pool for
  authorization
- Set up your agent code to fetch OAuth tokens on behalf of the user to call
  tools

## Prerequisites

Before you begin, make sure you have:

- An AWS account with appropriate permissions
- Basic understanding of Python programming
- Familiarity with Docker containers (for advanced deployment)
- Set up a basic agent with runtime successfully
- Basic understanding of OAuth authorization, mainly JWT bearer tokens, claims,
  and the various grant flows

## Step 1: Prepare your agent

Start by creating a basic agent with the following structure:

```
## Project Folder Structure

your_project_directory/
├── agent_example.py # Your main agent code
├── requirements.txt # Dependencies for your agent
└── __init__.py # Makes the directory a Python package
```

Create the following files with their respective contents:

###### agent_example.py

This is your main agent code:

```
from strands import Agent
from bedrock_agentcore.runtime import BedrockAgentCoreApp

agent = Agent()
app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload):
    """Process user input and return a response"""
    user_message = payload.get("prompt", "Hello")
    response = agent(user_message)
    return str(response) # response should be json serializable

if __name__ == "__main__":
    app.run()
```

###### requirements.txt

This file lists the dependencies for your agent:

```
strands-agents
bedrock-agentcore
```

## Step 2: Set up AWS Cognito user pool and add a user

To set up a Cognito user pool and create a user, you'll use a shell script that
automates the process.

For more information, see [Step 2: Set up an OAuth 2.0 Credential
Provider](identity-getting-started-google.md#identity-getting-started-step2 "identity-getting-started-google.md#identity-getting-started-step2").

###### To set up Cognito user pool and create a user

- Create a file named `setup_cognito.sh` with the following
  content:

```
#!/bin/bash

# Create User Pool and capture Pool ID directly
export POOL_ID=$(aws cognito-idp create-user-pool \
  --pool-name "MyUserPool" \
  --policies '{"PasswordPolicy":{"MinimumLength":8}}' \
  --region $REGION | jq -r '.UserPool.Id')

# Create App Client and capture Client ID directly
export CLIENT_ID=$(aws cognito-idp create-user-pool-client \
  --user-pool-id $POOL_ID \
  --client-name "MyClient" \
  --no-generate-secret \
  --explicit-auth-flows "ALLOW_USER_PASSWORD_AUTH" "ALLOW_REFRESH_TOKEN_AUTH" \
  --region $REGION | jq -r '.UserPoolClient.ClientId')

# Create User
aws cognito-idp admin-create-user \
  --user-pool-id $POOL_ID \
  --username $USERNAME \
  --region $REGION \
  --message-action SUPPRESS > /dev/null

# Set Permanent Password
aws cognito-idp admin-set-user-password \
  --user-pool-id $POOL_ID \
  --username $USERNAME \
  --password $PASSWORD \
  --region $REGION \
  --permanent > /dev/null

# Authenticate User and capture Access Token
export BEARER_TOKEN=$(aws cognito-idp initiate-auth \
  --client-id "$CLIENT_ID" \
  --auth-flow USER_PASSWORD_AUTH \
  --auth-parameters USERNAME=$USERNAME,PASSWORD=$PASSWORD \
  --region $REGION | jq -r '.AuthenticationResult.AccessToken')

# Output the required values
echo "Pool id: $POOL_ID"
echo "Discovery URL: https://cognito-idp.$REGION.amazonaws.com/$POOL_ID/.well-known/openid-configuration"
echo "Client ID: $CLIENT_ID"
echo "Bearer Token: $BEARER_TOKEN"
```

Open a terminal window and set the following environment variables:

    + `REGION` – the AWS Region that you want to use
    + `USERNAME` – the user name for the new user
    + `PASSWORD` – the password for the new user

```
export REGION=`us-east-1` // set your desired Region
export USERNAME=`USER NAME`
export PASSWORD=`PASSWORD`
```

In the terminal window, run the script:

```
source setup_cognito.sh
```

Note the output from the script. You'll need these values in the next steps.

This script creates a Cognito user pool, a user pool client, adds a user, and
generates a bearer token for the user. The token is valid for 60 minutes by
default.

## Step 3: Deploy your agent

###### Service-Linked Role Change - Effective October 13, 2025

Starting **October 13, 2025**, Amazon Bedrock AgentCore uses a Service-Linked Role (SLR) for workload identity permissions instead of requiring manual IAM policy configuration for new agents.

The Service-Linked Role details:

- **Name:** `AWSServiceRoleForBedrockAgentCoreRuntimeIdentity`
- **Service Principal:** `runtime-identity.bedrock-agentcore.amazonaws.com`
- **Purpose:** Manages workload identity access tokens and OAuth credentials
  Ensure the role you use to invoke AgentCore Control APIs has permission to create the Service-Linked Role:

```
{
    "Sid": "CreateBedrockAgentCoreIdentityServiceLinkedRolePermissions",
    "Effect": "Allow",
    "Action": "iam:CreateServiceLinkedRole",
    "Resource": "arn:aws:iam::*:role/aws-service-role/runtime-identity.bedrock-agentcore.amazonaws.com/AWSServiceRoleForBedrockAgentCoreRuntimeIdentity",
    "Condition": {
        "StringEquals": {
            "iam:AWSServiceName": "runtime-identity.bedrock-agentcore.amazonaws.com"
        }
    }
}
```

**Benefit**: The Service-Linked Role automatically provides the necessary permissions for workload identity access without requiring manual policy configuration.

For detailed information about the service-linked role, see [Identity service-linked role](service-linked-roles.md#identity-service-linked-role "service-linked-roles.md#identity-service-linked-role").

Now you'll deploy your agent with JWT authorization using the Cognito user pool you
created. You will need to create an agent with authorizer configuration. The following table
represents the various authorizer configuration parameters and how we use them to
validate the incoming token.

| authorizer_configuration | claim in decoded token | Notes                                                                                                              |
| ------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------ |
| discovery url → issuer   | iss                    | The discovery url should point to an issuer url. This should match the iss claim in the decoded token.             |
| allowedClients           | client_id              | client_id in the token should match one of the allowed clients specified in the authorizer                         |
| allowedAudience          | aud                    | One of the values in aud claim from the token should match one of the allowed audience specified in the authorizer |

If both client_id and aud is provided, the agent runtime authorizer will verify both.

Starter toolkit

###### To configure and deploy your agent

1. Configure your agent runtime with the following command, replacing the
   placeholder values with your actual values:

```
agentcore configure --entrypoint agent_example.py \
--name hello_agent \
--execution-role your-execution-role-arn \
--disable-otel \
--requirements-file requirements.txt \
--authorizer-config "{\"customJWTAuthorizer\":{\"discoveryUrl\":\"$DISCOVERY_URL\",\"allowedClients\":[\"$CLIENT_ID\"]}}"
```

Replace `$DISCOVERY_URL` with the Discovery URL from Step 2, and
`$CLIENT_ID` with the Client ID from Step 2. 2. Deploy your agent:

```
agentcore launch
```

3. Note the agent runtime ARN from the output. You'll need this in the next
   step.

###### Tip

You can also run the configure command with just the entry point file for a fully
interactive experience:

```
agentcore configure --entrypoint agent_example.py
```

Python

```
import boto3

# Create the client
client = boto3.client('bedrock-agentcore-control', region_name="us-east-1")


# Call the CreateAgentRuntime operation
response = client.create_agent_runtime(
    agentRuntimeName='hello_agent',
    agentRuntimeArtifact={
        'containerConfiguration': {
            'containerUri': '111122223333.dkr.ecr.us-east-1.amazonaws.com/my-agent:latest'
        }
    },
    authorizerConfiguration={
        "customJWTAuthorizer": {
            "discoveryUrl": 'COGNITO_DISCOVERY_URL',
            "allowedClients": ['COGNITO_CLIENT_ID']
        }
    },
    networkConfiguration={"networkMode":"PUBLIC"},
    roleArn='arn:aws:iam::111122223333:role/AgentRuntimeRole'
)
```

## Step 4: Use bearer token to invoke your agent

Now that your agent is deployed with JWT authorization, you can invoke it using the
bearer token.

###### Legacy Agent Permissions

**Important for existing users**: Agents created **before October 13, 2025** will continue to use the agent execution role for identity permissions and **require** the above policy to be attached to the agent's execution role.

**New agents**: For agents created **on or after October 13, 2025**, this policy is **not required**
as permissions are handled automatically by the Service-Linked Role.

```
{
    "Sid": "GetAgentAccessToken",
    "Effect": "Allow",
    "Action": [
        "bedrock-agentcore:GetWorkloadAccessToken",
        "bedrock-agentcore:GetWorkloadAccessTokenForJWT",
        "bedrock-agentcore:GetWorkloadAccessTokenForUserId"
    ],
    # point to the workload identity for the runtime; the workload identity can be found in
    # the GetAgentRuntime response and has your agent name in it.
    "Resource": [
        "arn:aws:bedrock-agentcore:`region`:`account-id`:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:`region`:`account-id`:workload-identity-directory/default/workload-identity/`agentname`-*"
    ]
}
```

**Invoke the agent**

Fetch a bearer token for the user you created with Amazon Cognito.

```
# use the password and other details used when you created the cognito user
            export TOKEN=$(aws cognito-idp initiate-auth \
            --client-id "$CLIENT_ID" \
            --auth-flow USER_PASSWORD_AUTH \
            --auth-parameters USERNAME='testuser',PASSWORD='`PASSWORD`' \
            --region us-east-1 | jq -r '.AuthenticationResult.AccessToken')
```

Proceed to invoke the agent with the rest of the following instructions.

Invoke the agent with OAuth.

Use cURL

```
// Invoke with OAuth token
export PAYLOAD='{"prompt": "hello what is 1+1?"}'
export BEDROCK_AGENT_CORE_ENDPOINT_URL="https://bedrock-agentcore.us-east-1.amazonaws.com"
curl -v -X POST "${BEDROCK_AGENT_CORE_ENDPOINT_URL}/runtimes/${ESCAPED_AGENT_ARN}/invocations?qualifier=DEFAULT" \
-H "Authorization: Bearer ${TOKEN}" \
-H "X-Amzn-Trace-Id: your-trace-id" \
-H "Content-Type: application/json" \
-H "X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: your-session-id" \
-d ${PAYLOAD}
```

Use Python
Since boto3 doesn't support invocation with bearer tokens, you'll need to use an HTTP
client like the requests library in Python.

###### To invoke your agent with a bearer token

1. Create a Python script named `invoke_agent.py` with the
   following content:

```
import requests
import urllib.parse
import json
import os

# Configuration Constants
REGION_NAME = "`AWS_REGION`"

# === Agent Invocation Demo ===
invoke_agent_arn = "`YOUR_AGENT_ARN_HERE`"
auth_token = os.environ.get('TOKEN')
print(f"Using Agent ARN from environment: {invoke_agent_arn}")

# URL encode the agent ARN
escaped_agent_arn = urllib.parse.quote(invoke_agent_arn, safe='')

# Construct the URL
url = f"https://bedrock-agentcore.{REGION_NAME}.amazonaws.com/runtimes/{escaped_agent_arn}/invocations?qualifier=DEFAULT"

# Set up headers
headers = {
    "Authorization": f"Bearer {auth_token}",
    "X-Amzn-Trace-Id": "your-trace-id",
    "Content-Type": "application/json",
    "X-Amzn-Bedrock-AgentCore-Runtime-Session-Id": "testsession123"
}

# Enable verbose logging for requests
import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("urllib3.connectionpool").setLevel(logging.DEBUG)

invoke_response = requests.post(
    url,
    headers=headers,
    data=json.dumps({"prompt": "Hello what is 1+1?"})
)

# Print response in a safe manner
print(f"Status Code: {invoke_response.status_code}")
print(f"Response Headers: {dict(invoke_response.headers)}")

# Handle response based on status code
if invoke_response.status_code == 200:
    response_data = invoke_response.json()
    print("Response JSON:")
    print(json.dumps(response_data, indent=2))
elif invoke_response.status_code >= 400:
    print(f"Error Response ({invoke_response.status_code}):")
    error_data = invoke_response.json()
    print(json.dumps(error_data, indent=2))

else:
    print(f"Unexpected status code: {invoke_response.status_code}")
    print("Response text:")
    print(invoke_response.text[:500])
```

2. Replace `AWS_REGION` with the AWS Region that you are using.
   from Step 3.
3. Replace `YOUR_AGENT_ARN_HERE` with your actual agent runtime ARN
   from Step 3.
4. Run the script:

```
python invoke_agent.py
```

Use starter toolkit
REplace `ADD_TOKEN_HERE` with your bearer token.

```
agentcore invoke '{"prompt": "Hello what is 1+1?"}' --bearer-token `ADD_TOKEN_HERE`
```

## Step 5: Set up your agent to access tools using OAuth

In this section, you'll learn how to connect your agent code with AgentCore Credential
Providers for secure access to external resources using OAuth2 authentication.

The example below demonstrates how your agent running in Agent Runtime can request
OAuth consent from users, enabling them to authenticate with their Google account and
authorize the agent to access their Google Drive contents.

For more information about setting up identity, see [Get started with AgentCore Identity](identity-getting-started.md "identity-getting-started.md").

### Step 5.1: Set up Credential Providers

To set up a Google Credential Provider, you need to:

1. Register your application with Google to obtain client ID and client
   secret
2. Create an OAuth credential provider using the AWS CLI. Replace `your-client-id` and `your-client-secret` with your actual Google OAuth2 client ID and client secret:

```
aws bedrock-agentcore-control create-oauth2-credential-provider \
  --name "google-provider" \
  --credential-provider-vendor "GoogleOauth2" \
  --oauth2-provider-config-input '{
      "googleOauth2ProviderConfig": {
        "clientId": "`your-client-id`",
        "clientSecret": "`your-client-secret`"
      }
    }'
```

Make sure your invocation role has the necessary permissions for accessing the
credential provider.

### Step 5.2: Enable agent to read Google Drive contents

Create a tool with agent core SDK annotations as shown below to automatically
initiate the three-legged OAuth process. When your agent invokes this tool, users
will be prompted to open the authorization URL in their browser and grant consent
for the agent to access their Google Drive.

```
import asyncio
from bedrock_agentcore.identity.auth import requires_access_token, requires_api_key

# This annotation helps agent developer to obtain access tokens from external applications
@requires_access_token(
    provider_name="google-provider",
    scopes=["https://www.googleapis.com/auth/drive.metadata.readonly"], # Google OAuth2 scopes
    auth_flow="USER_FEDERATION", # 3LO flow
    on_auth_url=lambda x: print("Copy and paste this authorization url to your browser", x), # prints authorization URL to console
    force_authentication=True,
)
async def read_from_google_drive(*, access_token: str):
    print(access_token) #You can see the access_token
    # Make API calls...
    main(access_token)

asyncio.run(read_from_google_drive(access_token=""))
```

###### What happens behind the scenes

When this code runs, the following process occurs:

1. Agent Runtime authorizes the inbound token according to the configured
   authorizer.
2. Agent Runtime exchanges this token for a Workload Access Token via
   `bedrock-agentcore:GetWorkloadAccessTokenForJWT` API and
   delivers it to your agent code via the payload header
   `WorkloadAccessToken`.
3. During tool invocation, your agent uses this Workload Access Token to call
   Token Vault API `bedrock-agentcore:GetResourceOauth2Token` and
   generate a 3LO authentication URL.
4. Your agent sends this URL to the client application as specified in the
   `on_auth_url` method.
5. The client application presents this URL to the user, who grants consent
   for the agent to access their Google Drive.
6. AgentCore Identity service securely receives and caches the Google access
   token until it expires, enabling subsequent requests from the user to use
   this token without needing the user to provide consent for every
   request.

###### Note

AgentCore Identity Service stores the Google access token in the AgentCore
Token Vault using the agent workload identity and user ID (from the inbound JWT
token, such as AWS Cognito token) as the binding key, eliminating repeated
consent requests until the Google token expires.

## Step 6: (Optional) Propagate a JWT token to AgentCore Runtime

Optionally, you can pass an Authorization header to an AgentCore Runtime
to extract claims. This can be done by using the request header allowlist
configuration. For more information, see
[RequestHeaderConfiguration](../../../bedrock-agentcore-control/latest/APIReference/API_RequestHeaderConfiguration.md "../../../bedrock-agentcore-control/latest/APIReference/API_RequestHeaderConfiguration.md").

### Step 6.1: Modify your agent code to read headers

In this step you make changes to your agent code so that you can decode
and extract claims from a JWT token using PyJWT library.

###### requirements.txt

Add PyJWT dependency to your requirements.txt file.

```
PyJWT
```

###### agent_example.py

Change your main agent code as shown in the following code. You can skip
validating the token signature here since it has already been validated by
AgentCore Runtime when the inbound authorization was done.

```

import jwt
import json
....

@app.entrypoint
def invoke(payload, context):
    auth_header = context.request_headers.get('Authorization')
    if not auth_header:
        return None

    # Remove "Bearer " prefix if present
    token = auth_header.replace('Bearer ', '') if auth_header.startswith('Bearer ') else auth_header
    try:
        # Skip signature validation as agent runtime has validated the token already.
        claims = jwt.decode(token, options={"verify_signature": False})
        app.logger.info("Claims: %s", json.dumps(claims))
    except jwt.InvalidTokenError as e:
        app.logger.exception("Invalid JWT token: %s", e)

    .....
```

### Step 6.2: Create the agent with request header allowlist

Use the AgentCore starter toolkit to create the agent with request header allowlist.

```
agentcore configure --entrypoint agent_example.py \
 --name hello_agent \
--execution-role your-execution-role-arn \
--disable-otel \
--requirements-file requirements.txt \
--authorizer-config "{\"customJWTAuthorizer\":{\"discoveryUrl\":\"$DISCOVERY_URL\",\"allowedClients\":[\"$CLIENT_ID\"]}}" \
--request-header-allowlist "Authorization"

// now launch the agent runtime
agentcore launch
```

### Step 6.3: Invoke your agent

[Invoke](#invoke-agent "#invoke-agent") your agent using OAuth and you should see the claims in your agent logs in CloudWatch Logs.

## Troubleshooting

### How to debug token related issues

If you encounter issues with token authentication, you can decode the token to
inspect its contents:

```
echo "$TOKEN" | cut -d '.' -f2 | tr '_-' '/+' | awk '{ l=4 - length($0)%4; if (l<4) printf "%s", $0; for (i=0; i<l; i++) printf "="; print "" }' | base64 -D | jq
```

This will output the token's payload, which looks similar to:

```
{
    "sub": "subid",
    "iss": "https://cognito-idp.us-east-1.amazonaws.com/userpoolid",
    "client_id": "clientid",
    "origin_jti": "originjti",
    "event_id": "eventid",
    "token_use": "access",
    "scope": "aws.cognito.signin.user.admin",
    "auth_time": 1752275688,
    "exp": 1752279288,
    "iat": 1752275688,
    "jti": "jti",
    "username": "username"
}
```

When troubleshooting token issues, check the following:

- Issuer url pointed to by the discovery url in the agent authorizer should
  match the issuer claim in the token. Do the following to confirm they match:
  - Select the discovery url you provided in the authorizer
    configuration when you created the agent, for example:
    `https://cognito-idp.us-east-1.amazonaws.com/us-east-1_nnnnnnnnn/.well-known/openid-configuration`
    - Check the issuer url - `"issuer":
"https://cognito-idp.us-east-1.amazonaws.com/us-east-1_12345566"`.
      This should match the iss claim value in the token.

- `client_id` claim in the token must match one of the authorizer
  allowedClients entries if provided
  - Note the client id you provided when you created the agent
  - Confirm this matches the client_id claim in the decoded
    token

- `aud` claim in the token must match one of the authorizer `allowedAudience`
  entries, if provided
  - Note the audience list you provided when you created the
    agent
  - Confirm this matches the `aud` claim in the decoded token

- Tokens are only valid
  for several minutes (the default Amazon Cognito expiry is 60 minutes). Fetch a new
  token as needed.
