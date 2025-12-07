# Example: Authorization for the default

gateway and target created by the AgentCore starter toolkit

If you used the AgentCore starter toolkit to create a gateway and a Lambda target,
you'll authorize with the following:

- **Inbound authorization using JWT** –
  Obtain the access token from the Amazon Cognito authorization that was automatically set
  up for you and include it in the authorization header. See the example below to
  learn how to obtain the token.
- **Outbound authorization using IAM** –
  The AgentCore starter toolkit configures the following permissions for you, so
  you don't need any additional setup:

      + Your gateway service role has permissions to invoke all functions in
       Lambda (provided by the [BedrockAgentCoreFullAccess](../../../aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.md "../../../aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.md") managed
       policy).
      + The created Lambda function is configured with your gateway service
       role as a `Principal` that can invoke it.

  You can obtain the access token created for your gateway by the
  AgentCore starter toolkit with the help of Amazon Cognito by collecting the following
  information:

- **Token endpoint** – Find at the **Discovery URL** in the authorizer configuration for the
  gateway. If you use the API, you can find the discovery URL by sending a
  [ListGateways](../../../bedrock-agentcore-control/latest/APIReference/API_ListGateways.md "../../../bedrock-agentcore-control/latest/APIReference/API_ListGateways.md") request or a [GetGateway](../../../bedrock-agentcore-control/latest/APIReference/API_GetGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_GetGateway.md") request for your gateway.
- **Client ID** – Find in the Amazon Cognito user pool
  information. If you use the API, you can send a [ListUserPools](../../../cognito-user-identity-pools/latest/APIReference/API_ListUserPools.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUserPools.md") request or a [DescribeUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.md") request for the user pool associated with your
  gateway.
- **Client secret** – Find in the Amazon Cognito user
  pool app client information. If you use the API, you can send a [DescribeUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.md") request, specifying the client ID and user
  pool ID associated with your gateway.
  First, collect these values with one of the following methods. Select one of the following methods:

Console

1. Get the **token endpoint**:
   1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
   2. From the left navigation pane, choose
      **Gateways**.
   3. In the **Gateways** section, select your
      gateway.
   4. In the **Inbound Identity** section, note
      the following values:
      - **Allowed clients** – The
        client IDs that can access the gateway.
      - **Discovery URL** – The
        format should be
        `https://cognito-idp.`${Region}`.amazonaws.com/`${UserPoolId}`/.well-known/openid-configuration`.
        Store the following values:
        - `${UserPoolId}`
          – Extract from the Discovery URL.
        - **Token
          endpoint** – Select the Discovery
          URL link and find the value in the
          `token_endpoint` field.

2. Get the **client ID** and **client secret**:
   1. Open the Amazon Cognito console at [https://console.aws.amazon.com/cognito](https://console.aws.amazon.com/cognito "https://console.aws.amazon.com/cognito").
   2. From the left navigation pane, select **User
      pools**.
   3. Select the user pool ID associated with your
      gateway.
   4. From the left navigation pane, choose **App
      clients**.
   5. Select an app client whose **Client ID**
      matches the allowed clients for your token endpoint. Store
      the ID value.
   6. Under **Client secret**, select
      **Show client secret** and store that
      value.

AWS CLI

1. Run the AgentCore `get-gateway` command in a terminal
   and specify your gateway ID in the `--gateway-identifier`
   argument, as in the following example:

```
aws bedrock-agentcore-control get-gateway --gateway-identifier `my-gateway-id`
```

2. From the response, note the `discoveryUrl` from the
   `authorizerConfiguration` field:
   - Store the `${UserPoolId}` from
     the URL. The format should be
     `https://cognito-idp.`${Region}`.amazonaws.com/`${UserPoolId}`/.well-known/openid-configuration`.
   - Store the `allowedClients` values. These are
     the client IDs that can access the token endpoint.
   - Navigate to the `discoveryUrl` in a browser and
     store the `token_endpoint` value.

3. Run the Amazon Cognito `describe-user-pool-client` command in a
   terminal and specify the user pool ID in the
   `--user-pool-id` argument and an allowed client ID in
   the `--client-id` field, as in the following
   example:

```
aws cognito-idp describe-user-pool-client --user-pool-id `my-user-pool-id` --client-id `my-client-id`
```

4. Store the `ClientSecret` value.

AWS Python SDK (Boto3)
Run the following Python code to store the token endpoint, client ID, and
client secret as variables:

```
import requests
  import boto3

  # Initialize AWS clients
  agentcore_client = boto3.client("bedrock-agentcore-control")
  cognito_client = boto3.client("cognito-idp")

  # Replace with your actual gateway ID
  gateway_id = "my-gateway-id"

  # Get discovery URL and first allowed client
  auth_config = agentcore_client.get_gateway(gatewayIdentifier=gateway_id)["authorizerConfiguration"]["customJWTAuthorizer"]
  discovery_url, client_id = auth_config["discoveryUrl"], auth_config["allowedClients"][0]

  # Get token endpoint from discovery URL
  discovery_url_json = requests.get(discovery_url).json()
  token_endpoint, user_pool_id = discovery_url_json["token_endpoint"], discovery_url_json["issuer"].split("/")[-1]

  # Get client secret
  client_secret = cognito_client.describe_user_pool_client(
      UserPoolId=user_pool_id,
      ClientId=client_id
  )["UserPoolClient"]["ClientSecret"]
```

Second, use the values you gathered to access the token from the token endpoint.
Select one of the following methods:

curl
Run the following command in a terminal, replacing the token endpoint,
client ID, and client secret values.

```
curl --http1.1 -X POST `${TokenEndpoint}` \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "grant_type=client_credentials&client_id=`${ClientId}`&client_secret=`${ClientSecret}`"
```

The token is in the `access_token` field of the response, while
the `token_type` field should specify `Bearer`.

Python requests package
Run the following Python code to obtain your access token. The code
assumes that you stored the `token_endpoint`,
`client_id`, and `client_secret` values from the
previous step:

```
import requests
  import json

  def get_access_token(token_endpoint, client_id, client_secret):
      headers={
          "Content-Type": "application/x-www-form-urlencoded"
      }

      payload={
          "grant_type": "client_credentials",
          "client_id": client_id,
          "client_secret": client_secret
      }

      response = requests.post(token_endpoint, headers=headers, data=payload)
      return response.json()

  # Replace the argument values as necessary, if you didn't previously store them as these variables
  access_token_response = get_access_token(
      token_endpoint=token_endpoint,
      client_id=client_id,
      client_secret=client_secret
  )

  access_token = access_token_response["access_token"]
```
