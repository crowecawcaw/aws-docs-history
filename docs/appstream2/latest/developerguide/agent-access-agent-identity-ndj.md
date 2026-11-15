

# Agent identity for non-domain-joined fleets
<a name="agent-access-agent-identity-ndj"></a>

For a non-domain-joined fleet, the agent runs one on-behalf-of (OBO) exchange at your identity provider (IdP), exchanges the resulting token for temporary AWS credentials, and connects to the Model Context Protocol (MCP) server with those credentials. The MCP server creates the streaming session for the user named in the source identity.

To set up agent identity, complete the following steps:

1. [Step 1: Configure your identity provider](#agent-access-agent-identity-ndj-idp)

1. [Step 2: Configure IAM](#agent-access-agent-identity-ndj-iam)

1. [Step 3: Connect the agent](#agent-access-agent-identity-ndj-connect)

1. [Step 4: Verify agent identity](#agent-access-agent-identity-ndj-verify)

## Prerequisites
<a name="agent-access-agent-identity-ndj-prereqs"></a>
+ A stack with agent access turned on, associated with a running non-domain-joined fleet. For more information, see [Prerequisites](agent-access-mcp-prerequisites.md).
+ An IdP that supports OpenID Connect (OIDC), an OBO or token exchange grant, and custom claims in access tokens. Examples include Microsoft Entra ID, Okta, Ping Identity, Auth0, and Keycloak.
+ Permissions to register applications and configure claims in your IdP, and to create IAM identity providers and roles in the AWS account that owns the stack.
+ A current version of the AWS CLI.
+ (Optional) A CloudTrail trail that logs data events for agent access, if you want tool calls recorded. Without it, CloudTrail records the role assumption and the MCP `initialize` request, but not the tool calls that follow. For more information, see [Monitoring](agent-access-mcp-server-monitoring.md).

## Step 1: Configure your identity provider
<a name="agent-access-agent-identity-ndj-idp"></a>

In your IdP, you create two applications and configure the claims that identify the agent and the user.
+ **The AWS federation application** represents AWS as the resource that the agent requests access to. It exposes a scope that the agent requests in the OBO exchange, such as `access_as_agent`. You configure the identity claims on this application, so that one configuration covers every agent.
+ **The agent application** represents the agent. The agent uses its client ID and credentials to run the OBO exchange. Create one agent application for each agent that needs a distinct identity.

### Microsoft Entra ID
<a name="agent-access-agent-identity-ndj-entra"></a>

**To configure Microsoft Entra ID for agent identity**

1. Register the AWS federation application. Set an Application ID URI, such as `api://{{federation-app-client-id}}`, expose a scope named `access_as_agent`, and grant admin consent for it.

1. Register the agent application as a standard app registration. Add a delegated API permission for the `access_as_agent` scope of the federation application, and grant admin consent.

1. Add a certificate credential to the agent application. The agent signs a client assertion with the matching private key each time it calls the token endpoint. To keep the private key out of the agent, you can create an asymmetric AWS KMS key for signing, build an X.509 certificate for its public key, and sign assertions with the AWS KMS `Sign` operation.

1. Create a claims-mapping policy with the following definition, and assign it to the service principal of the AWS federation application. Because the policy is on the resource application, `application` claims resolve to whichever agent calls it, so one policy covers every agent.

   ```
   {
       "ClaimsMappingPolicy": {
           "Version": 1,
           "IncludeBasicClaimSet": "true",
           "ClaimsSchema": [
               { "Source": "application", "ID": "objectid",
                 "JwtClaimType": "https://aws.amazon.com/tags/principal_tags/AgentAccessAgentId" },
               { "Source": "application", "ID": "displayname",
                 "JwtClaimType": "https://aws.amazon.com/tags/principal_tags/AgentAccessAgentName" },
               { "Source": "user", "ID": "mailnickname",
                 "JwtClaimType": "https://aws.amazon.com/tags/principal_tags/AgentAccessUserId" },
               { "Source": "user", "ID": "mailnickname",
                 "JwtClaimType": "https://aws.amazon.com/source_identity" }
           ]
       }
   }
   ```

   For users that are synchronized from Active Directory, you can use `onpremisessamaccountname` instead of `mailnickname`. The `onpremises` attributes are empty for cloud-only users, and Entra omits a claim that has no value instead of returning an error.

1. On the AWS federation application, set `acceptMappedClaims` to `true` and `requestedAccessTokenVersion` to `2`. Without `acceptMappedClaims`, Entra rejects the token request.

For more information, see [Microsoft identity platform and OAuth 2.0 On-Behalf-Of flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow) and [Claims customization](https://learn.microsoft.com/en-us/entra/identity-platform/reference-claims-customization) in the Microsoft Entra documentation.

### Okta
<a name="agent-access-agent-identity-ndj-okta"></a>

You can use Okta if it meets the requirements in [Prerequisites](#agent-access-agent-identity-ndj-prereqs). Configure Okta to add the claims listed in [Identity attributes](agent-access-agent-identity.md#agent-access-agent-identity-attributes) to the access token that it issues in the token exchange.

### Other identity providers
<a name="agent-access-agent-identity-ndj-other-idps"></a>

If your IdP can add arbitrary claims to access tokens, you can emit all the session tags in one nested claim instead of one claim for each tag. Tag values must be arrays, even when there is only one value.

```
{
    "https://aws.amazon.com/tags": {
        "principal_tags": {
            "AgentAccessAgentId": ["{{agent-id}}"],
            "AgentAccessUserId": ["{{user-name}}"]
        }
    },
    "https://aws.amazon.com/source_identity": "{{user-name}}"
}
```

Transitive tag keys aren't required, because this flow doesn't chain roles. For more information about the claim formats, see [Pass session tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html) in the *IAM User Guide*.

## Step 2: Configure IAM
<a name="agent-access-agent-identity-ndj-iam"></a>

In the AWS account that owns the stack, register your IdP and create the role that the agent assumes.

**To configure IAM for agent identity**

1. Register your IdP as an IAM OIDC identity provider. The URL must match the `iss` claim of the token exactly. For Microsoft Entra ID, the URL is `https://login.microsoftonline.com/{{tenant-id}}/v2.0`.

   ```
   aws iam create-open-id-connect-provider \
       --url {{https://login.microsoftonline.com/tenant-id/v2.0}} \
       --client-id-list {{agent-1-client-id}} {{agent-2-client-id}}
   ```

   For `--client-id-list`, specify the client ID of each agent application. If you created more than one agent application, include all of their client IDs. AWS STS rejects a token from an agent whose client ID isn't on the list. To add an agent later, use the `aws iam add-client-id-to-open-id-connect-provider` command.

1. Create a role with the following trust policy. The `Null` conditions reject any token that doesn't carry both identities. They're in a separate statement from `sts:SetSourceIdentity`, because session tags aren't part of the request for that action, so the conditions would deny it.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "AssumeRoleWithBothIdentities",
               "Effect": "Allow",
               "Principal": {
                   "Federated": "arn:aws:iam::{{111122223333}}:oidc-provider/{{login.microsoftonline.com/tenant-id/v2.0}}"
               },
               "Action": [
                   "sts:AssumeRoleWithWebIdentity",
                   "sts:TagSession"
               ],
               "Condition": {
                   "StringEquals": {
                       "{{login.microsoftonline.com/tenant-id/v2.0}}:aud": "{{agent-client-id}}"
                   },
                   "Null": {
                       "aws:RequestTag/AgentAccessAgentId": "false",
                       "aws:RequestTag/AgentAccessUserId": "false"
                   }
               }
           },
           {
               "Sid": "SetSourceIdentity",
               "Effect": "Allow",
               "Principal": {
                   "Federated": "arn:aws:iam::{{111122223333}}:oidc-provider/{{login.microsoftonline.com/tenant-id/v2.0}}"
               },
               "Action": "sts:SetSourceIdentity",
               "Condition": {
                   "StringEquals": {
                       "{{login.microsoftonline.com/tenant-id/v2.0}}:aud": "{{agent-client-id}}"
                   }
               }
           }
       ]
   }
   ```

   For Microsoft Entra ID, the `:aud` condition key matches the `azp` claim of the token, which is the client ID of the agent application. This limits the role to that agent. To let several agents use the same role, list each client ID in the `:aud` condition.

1. Attach a permissions policy that allows the agent to call the MCP server and to start streaming sessions on the stack.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "agentaccess-mcp:*",
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "appstream:ListAssociatedFleets",
                   "appstream:DescribeFleets",
                   "appstream:CreateStreamingURL"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

1. (Optional) To require that the user tag matches the user of the streaming session, attach the following statement to the role. It denies MCP requests from any session whose `AgentAccessUserId` tag differs from its source identity. We recommend this statement when one role serves more than one user.

   ```
   {
       "Sid": "UserTagMustMatchSourceIdentity",
       "Effect": "Deny",
       "Action": "agentaccess-mcp:*",
       "Resource": "*",
       "Condition": {
           "Null": { "aws:PrincipalTag/AgentAccessUserId": "false" },
           "StringNotEquals": {
               "aws:PrincipalTag/AgentAccessUserId": "${aws:SourceIdentity}"
           }
       }
   }
   ```

## Step 3: Connect the agent
<a name="agent-access-agent-identity-ndj-connect"></a>

The agent runs the OBO exchange, assumes the role, and connects to the MCP server with the resulting credentials. The following Python example uses Microsoft Entra ID. In it, `user_token` is the token that the agent received when the user signed in, and `client_assertion()` returns a client assertion signed with the agent's private key.

```
import boto3
import requests
from botocore.credentials import Credentials
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

REGION = "{{region}}"

# 1. On-behalf-of exchange: the agent acts for the signed-in user
obo = requests.post(
    "https://login.microsoftonline.com/{{tenant-id}}/oauth2/v2.0/token",
    data={
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "client_id": "{{agent-client-id}}",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": client_assertion(),
        "assertion": user_token,
        "requested_token_use": "on_behalf_of",
        "scope": "{{api://federation-app-client-id}}/.default",
    },
).json()

# 2. Exchange the token for temporary AWS credentials.
#    The session tags and source identity come from the token.
creds = boto3.client("sts", region_name=REGION).assume_role_with_web_identity(
    RoleArn="arn:aws:iam::{{111122223333}}:role/{{agent-role}}",
    RoleSessionName="{{agent-session}}",
    WebIdentityToken=obo["access_token"],
)["Credentials"]

# 3. Connect to the MCP server. The user comes from the source identity,
#    so the user ID header isn't needed.
async with aws_iam_streamablehttp_client(
    endpoint=f"https://agentaccess-mcp.{REGION}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region=REGION,
    credentials=Credentials(
        creds["AccessKeyId"], creds["SecretAccessKey"], creds["SessionToken"]
    ),
    headers={
        "x-amzn-agentaccess-workspaces-applications-stack": "{{stack-name-or-arn}}",
    },
) as (read, write, _):
    ...
```

The MCP server uses the source identity as the user of the streaming session. The user name must be 2 to 32 characters long. You don't need the `x-amzn-agentaccess-workspaces-applications-user-id` header. If you send it, it must match the source identity, or the request is rejected. For more information about the connection options, see [Connecting with non-domain-joined fleets](agent-access-mcp-server-endpoint.md#agent-access-mcp-server-connect-ndj).

The credentials expire at the end of the role session. To continue after they expire, the agent runs a new OBO exchange and assumes the role again, so your IdP makes a new access decision each time.

The OBO exchange requires a valid token for the user. When the user's token expires, the agent must get a new one before it can run another OBO exchange, either by using a refresh token or by asking the user to sign in again. One sign-in doesn't let the agent run indefinitely. How long the agent can continue without the user signing in again depends on the token lifetime and refresh token policies in your IdP.

## Step 4: Verify agent identity
<a name="agent-access-agent-identity-ndj-verify"></a>

In CloudTrail, confirm that both identities reached AWS:

1. Find the `AssumeRoleWithWebIdentity` event for the role. Under `requestParameters`, `principalTags` contains `AgentAccessAgentId` and `AgentAccessUserId`, and `sourceIdentity` contains the user. The event can take several minutes to appear in CloudTrail.

1. Find the `Initialize` event, which has the event source `agentaccess-mcp.amazonaws.com`. Under `userIdentity.sessionContext`, `sourceIdentity` contains the user, and `webIdFederationData.federatedProvider` names your OIDC identity provider. The session tags don't appear on this event. That's expected, and it's why the source identity is required.

1. To confirm that the user is recorded on the agent's actions, find a `CallReadOnlyTool` or `CallPrivilegedTool` event (`eventCategory` is `Data`). Under `userIdentity.sessionContext`, `sourceIdentity` contains the user.
**Note**  
Tool call events appear only if your trail logs data events for agent access. Without data events, you see only management events, such as `Initialize`, and not the agent's tool calls.

```
aws cloudtrail lookup-events --region {{region}} \
    --lookup-attributes AttributeKey=EventSource,AttributeValue=agentaccess-mcp.amazonaws.com \
    --query 'Events[0].CloudTrailEvent' --output text
```

The `lookup-events` command returns management events only, such as `AssumeRoleWithWebIdentity` and `Initialize`. It never returns tool call events, because those are data events. To find tool call events, search the log files that your trail delivers to Amazon S3, or send the trail events to CloudWatch Logs and query them there.

Your IdP sign-in logs also record the OBO exchange against the agent's client ID and the user. Together with CloudTrail, they show which agent acted for which user, and when. For more information about agent access events, see [Monitoring](agent-access-mcp-server-monitoring.md).