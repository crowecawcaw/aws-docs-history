

# Agent identity for domain-joined fleets

On a domain-joined fleet, Windows must log the user on to the Active Directory domain, and an agent can't type a password. Instead, certificate-based authentication logs the user on with a short-lived certificate that WorkSpaces Applications issues for the session. To issue that certificate, WorkSpaces Applications needs the user's Active Directory identity, which your identity provider (IdP) supplies in a SAML assertion.

The agent therefore runs two on-behalf-of (OBO) exchanges from the same user token:
+ **An OIDC exchange**. The agent exchanges the resulting token for temporary AWS credentials and signs its Model Context Protocol (MCP) requests with them. This is the same exchange as for non-domain-joined fleets, and it carries the agent and user identities into CloudTrail.
+ **A SAML exchange**. The agent passes the resulting SAML assertion to the MCP server. WorkSpaces Applications uses it to establish the streaming session and to issue the logon certificate for the user's Active Directory account.

The steps in this topic use Microsoft Entra ID. To use another IdP, it must be able to return a SAML assertion from the OBO or token exchange, with the attributes listed in [Step 2: Configure the SAML attributes](#agent-access-agent-identity-dj-attributes).

To set up agent identity, complete the following steps:

1. [Step 1: Create a SAML application in your identity provider](#agent-access-agent-identity-dj-saml-app)

1. [Step 2: Configure the SAML attributes](#agent-access-agent-identity-dj-attributes)

1. [Step 3: Configure IAM for SAML](#agent-access-agent-identity-dj-iam)

1. [Step 4: Connect the agent](#agent-access-agent-identity-dj-connect)

1. [Step 5: Verify agent identity](#agent-access-agent-identity-dj-verify)

## Prerequisites
<a name="agent-access-agent-identity-dj-prereqs"></a>
+ A stack with agent access turned on, associated with a running domain-joined fleet.
+ Certificate-based authentication turned on for the directory configuration, and working for human users. If a user can't log on with certificate-based authentication, an agent can't either. For more information, see [Certificate-Based Authentication](certificate-based-authentication.md).
+ The OIDC configuration for agent identity, which you complete in [Step 1: Configure your identity provider](agent-access-agent-identity-ndj.md#agent-access-agent-identity-ndj-idp) and [Step 2: Configure IAM](agent-access-agent-identity-ndj.md#agent-access-agent-identity-ndj-iam) for non-domain-joined fleets. The agent uses that configuration for its AWS credentials.
+ (Optional) A CloudTrail trail that logs data events for agent access, if you want tool calls recorded. For more information, see [Monitoring](agent-access-mcp-server-monitoring.md).

## Step 1: Create a SAML application in your identity provider
<a name="agent-access-agent-identity-dj-saml-app"></a>

Create a SAML application for AWS that the agent can request an assertion from in an OBO exchange. This application is separate from the AWS federation application that you created for the OIDC exchange.

**To create the SAML application in Microsoft Entra ID**

1. Register an application with the reply URL `https://signin.aws.amazon.com/saml`, create its service principal with SAML as the single sign-on mode, and add `urn:amazon:webservices` as an identifier URI.

   If another application in your tenant already uses `urn:amazon:webservices`, add a fragment, such as `urn:amazon:webservices#{{app-name}}`. AWS ignores the fragment when it matches the audience. Use the same value as the scope prefix in the OBO exchange.

1. Add an application-specific token signing certificate to the service principal. Entra can't issue a SAML assertion in an OBO exchange without one.

1. Expose a scope named `access_as_agent` on the SAML application, and grant the agent application consent to it. This consent is separate from the consent for the scope on the AWS federation application. Without it, the SAML exchange fails even when the OIDC exchange works.

1. Create a claims-mapping policy with the following definition. It emits the attributes in [Step 2: Configure the SAML attributes](#agent-access-agent-identity-dj-attributes). Replace the role ARN, the IAM SAML identity provider ARN, and the domain name with your own values.

   ```json
   {
       "ClaimsMappingPolicy": {
           "Version": 1,
           "IncludeBasicClaimSet": "false",
           "ClaimsSchema": [
               { "Source": "user", "ID": "userprincipalname",
                 "SamlClaimType": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier" },
               { "Value": "arn:aws:iam::{{111122223333}}:role/{{role-name}},arn:aws:iam::{{111122223333}}:saml-provider/{{AgentAccessSAML}}",
                 "SamlClaimType": "https://aws.amazon.com/SAML/Attributes/Role" },
               { "Source": "user", "ID": "userprincipalname",
                 "SamlClaimType": "https://aws.amazon.com/SAML/Attributes/RoleSessionName" },
               { "Source": "user", "ID": "mailnickname",
                 "SamlClaimType": "https://aws.amazon.com/SAML/Attributes/SourceIdentity" },
               { "Source": "application", "ID": "objectid",
                 "SamlClaimType": "https://aws.amazon.com/SAML/Attributes/PrincipalTag:AgentAccessAgentId" },
               { "Source": "application", "ID": "displayname",
                 "SamlClaimType": "https://aws.amazon.com/SAML/Attributes/PrincipalTag:AgentAccessAgentName" },
               { "Source": "user", "ID": "mailnickname",
                 "SamlClaimType": "https://aws.amazon.com/SAML/Attributes/PrincipalTag:AgentAccessUserId" },
               { "Source": "user", "ID": "userprincipalname",
                 "SamlClaimType": "https://aws.amazon.com/SAML/Attributes/PrincipalTag:UserPrincipalName" },
               { "Source": "user", "ID": "onpremisesecurityidentifier",
                 "SamlClaimType": "https://aws.amazon.com/SAML/Attributes/PrincipalTag:ObjectSid" },
               { "Value": "{{corp.example.com}}",
                 "SamlClaimType": "https://aws.amazon.com/SAML/Attributes/PrincipalTag:Domain" }
           ]
       }
   }
   ```

   The `Domain` entry is optional. Include it only when the UPN suffix differs from the domain name.

1. Create the policy and assign it to the service principal of the SAML application with the Microsoft Graph API. You can't create or assign a claims-mapping policy in the Microsoft Entra admin center. For example, with the Azure CLI:

   ```
   # Create the policy. In the request body, pass the definition as a single JSON string:
   # { "displayName": "AgentAccessSAMLClaims", "definition": [ "{{policy-definition}}" ] }
   az rest --method POST \
       --url https://graph.microsoft.com/v1.0/policies/claimsMappingPolicies \
       --headers Content-Type=application/json \
       --body @{{claims-policy-request.json}}
   
   # Assign the policy to the service principal of the SAML application
   az rest --method POST \
       --url 'https://graph.microsoft.com/v1.0/servicePrincipals/{{saml-sp-object-id}}/claimsMappingPolicies/$ref' \
       --headers Content-Type=application/json \
       --body '{"@odata.id": "https://graph.microsoft.com/v1.0/policies/claimsMappingPolicies/{{policy-id}}"}'
   ```

1. Set `acceptMappedClaims` to `true` on the SAML application. Without it, Entra rejects the token request.

   ```
   az rest --method PATCH \
       --url https://graph.microsoft.com/v1.0/applications/{{saml-app-object-id}} \
       --headers Content-Type=application/json \
       --body '{"api": {"acceptMappedClaims": true}}'
   ```

For more information about SAML federation with WorkSpaces Applications, see [Setting Up SAML](external-identity-providers-setting-up-saml.md).

## Step 2: Configure the SAML attributes
<a name="agent-access-agent-identity-dj-attributes"></a>

The SAML assertion must carry the agent and user identities, and the Active Directory attributes that WorkSpaces Applications uses to build the logon certificate. Except for the name ID, each attribute name starts with `https://aws.amazon.com/SAML/Attributes/`.


**SAML attributes for agent identity on domain-joined fleets**  

| Attribute | Value | 
| --- | --- | 
| Name ID | The user's UPN, in the format {{user}}@{{ad-dns-name}}. Source it from the user's userprincipalname attribute. Entra ignores a constant value for the name ID. WorkSpaces Applications writes the name ID into the subject alternative name of the logon certificate. | 
| Role | The role ARN and the IAM SAML identity provider ARN, separated by a comma | 
| RoleSessionName | The user's UPN | 
| SourceIdentity | The user's short name | 
| PrincipalTag:AgentAccessAgentId | The agent's immutable object ID | 
| PrincipalTag:AgentAccessAgentName | (Optional) The agent's display name | 
| PrincipalTag:AgentAccessUserId | The user's short name | 
| PrincipalTag:UserPrincipalName | The user's UPN | 
| PrincipalTag:ObjectSid | The security identifier (SID) of the Active Directory user, such as S-1-5-21-{{...}}. WorkSpaces Applications adds it to the certificate as the strong certificate mapping that domain controllers require. | 
| PrincipalTag:Domain | (Optional) The fully qualified domain name of the Active Directory domain. Use it when the UPN suffix differs from the domain name. | 

Keep the following in mind when you configure the attributes:
+ In Microsoft Entra ID, set `IncludeBasicClaimSet` to `false` in the claims-mapping policy. Additional claims cause AWS Sign-In to show an interactive role selection page, which an agent can't complete.
+ Use the same values for `SourceIdentity` and `PrincipalTag:AgentAccessUserId` as in the OIDC exchange, such as the user's `mailnickname` for the short name. The streaming session takes the user from the SAML assertion, and the MCP events in CloudTrail take it from the OIDC token. If the values differ, the two name different users.
+ For users synchronized from Active Directory, source `PrincipalTag:ObjectSid` from `onpremisesecurityidentifier`. For other users, that attribute is empty, and the logon certificate can't be mapped to the account.
**Important**  
For testing only, you can emit the SID of an Active Directory account as a constant value. A constant value in a claims-mapping policy applies to every user of the application, so every user would get the same SID. Use a constant only for a single test user, or with a separate SAML application and policy for each user. Don't use a constant SID in production. To read the SID, run `Get-ADUser -Identity {{user-name}} -Properties objectSid` on a domain-joined computer.
+ You don't need `TransitiveTagKeys`, because this flow doesn't chain roles. If you include it, emit one attribute value for each tag key. A single comma-separated value isn't a valid tag key, and the role assumption fails.

## Step 3: Configure IAM for SAML
<a name="agent-access-agent-identity-dj-iam"></a>

**To configure IAM for the SAML exchange**

1. Download the federation metadata of the SAML application from your IdP, and create an IAM SAML identity provider from it.

   ```
   aws iam create-saml-provider --name {{AgentAccessSAML}} \
       --saml-metadata-document file://{{saml-metadata.xml}}
   ```

1. Add the following statements to the trust policy of the role that you created for the OIDC exchange. The role then trusts both identity providers. As in the OIDC trust policy, the `Null` conditions are in a separate statement from `sts:SetSourceIdentity`.

   ```json
   {
       "Sid": "AssumeRoleWithSAMLBothIdentities",
       "Effect": "Allow",
       "Principal": {
           "Federated": "arn:aws:iam::{{111122223333}}:saml-provider/{{AgentAccessSAML}}"
       },
       "Action": [
           "sts:AssumeRoleWithSAML",
           "sts:TagSession"
       ],
       "Condition": {
           "StringEquals": { "SAML:aud": "https://signin.aws.amazon.com/saml" },
           "Null": {
               "aws:RequestTag/AgentAccessAgentId": "false",
               "aws:RequestTag/AgentAccessUserId": "false"
           }
       }
   },
   {
       "Sid": "SAMLSetSourceIdentity",
       "Effect": "Allow",
       "Principal": {
           "Federated": "arn:aws:iam::{{111122223333}}:saml-provider/{{AgentAccessSAML}}"
       },
       "Action": "sts:SetSourceIdentity",
       "Condition": {
           "StringEquals": { "SAML:aud": "https://signin.aws.amazon.com/saml" }
       }
   }
   ```

1. Allow the role to stream from the stack. Without this permission, the streaming session can't be established.

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "appstream:Stream",
               "Resource": "arn:aws:appstream:{{region}}:{{111122223333}}:stack/{{stack-name}}"
           }
       ]
   }
   ```

## Step 4: Connect the agent
<a name="agent-access-agent-identity-dj-connect"></a>

The agent runs both exchanges from the same user token. It signs MCP requests with the credentials from the OIDC exchange, as shown in [Step 3: Connect the agent](agent-access-agent-identity-ndj.md#agent-access-agent-identity-ndj-connect), and passes the SAML assertion and the stack ARN in the `_meta` field of every request. SAML assertions are too large for HTTP headers.

Microsoft Entra ID returns the assertion from the OBO exchange as a bare SAML assertion, encoded in base64url. AWS Sign-In expects a SAML response, so the agent wraps the assertion in an unsigned `samlp:Response` element. AWS Sign-In validates the signature of the assertion inside it.

```python
import base64
import json
import uuid
from datetime import datetime, timezone

import requests
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import Credentials

REGION = "{{region}}"
MCP_URL = f"https://agentaccess-mcp.{REGION}.api.aws/mcp"

# 1. SAML on-behalf-of exchange, from the same user token as the OIDC exchange
obo_saml = requests.post(
    "https://login.microsoftonline.com/{{tenant-id}}/oauth2/v2.0/token",
    data={
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "client_id": "{{agent-client-id}}",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": client_assertion(),
        "assertion": user_token,
        "requested_token_use": "on_behalf_of",
        "requested_token_type": "urn:ietf:params:oauth:token-type:saml2",
        "scope": "urn:amazon:webservices/.default",
    },
).json()

# 2. Decode the base64url assertion and wrap it in a SAML response
raw = obo_saml["access_token"]
assertion_xml = base64.urlsafe_b64decode(raw + "=" * (-len(raw) % 4)).decode()
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
saml_response = base64.b64encode((
    '<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" '
    f'ID="_{uuid.uuid4()}" Version="2.0" IssueInstant="{now}" '
    'Destination="https://signin.aws.amazon.com/saml">'
    '<samlp:Status><samlp:StatusCode '
    'Value="urn:oasis:names:tc:SAML:2.0:status:Success"/></samlp:Status>'
    f'{assertion_xml}</samlp:Response>'
).encode()).decode()

# 3. Send signed MCP requests with the OIDC credentials (creds),
#    with the SAML assertion and the stack ARN in _meta
credentials = Credentials(
    creds["AccessKeyId"], creds["SecretAccessKey"], creds["SessionToken"]
)
auth_meta = {
    "aws.agentaccess/workspacesApplicationsSamlAssertion": saml_response,
    "aws.agentaccess/workspacesApplicationsStackArn": "arn:aws:appstream:{{region}}:{{111122223333}}:stack/{{stack-name}}",
}
session_id = None

def mcp_request(method, params=None, request_id=1):
    """Send one JSON-RPC request. _meta is added before the body is signed."""
    params = dict(params or {})
    params["_meta"] = auth_meta
    body = json.dumps(
        {"jsonrpc": "2.0", "id": request_id, "method": method, "params": params}
    ).encode()
    headers = {"Content-Type": "application/json"}
    if session_id:
        headers["Mcp-Session-Id"] = session_id
    request = AWSRequest(method="POST", url=MCP_URL, data=body, headers=headers)
    SigV4Auth(credentials, "agentaccess-mcp", REGION).add_auth(request)
    # Send exactly the bytes that were signed
    response = requests.post(MCP_URL, data=body, headers=dict(request.headers))
    response.raise_for_status()
    return response

init = mcp_request("initialize", {
    "protocolVersion": "2025-03-26",
    "capabilities": {},
    "clientInfo": {"name": "{{my-agent}}", "version": "1.0"},
})
session_id = init.headers["Mcp-Session-Id"]

tools = mcp_request("tools/list", request_id=2).json()["result"]["tools"]
screenshot = mcp_request(
    "tools/call", {"name": "agentaccess___screenshot", "arguments": {}}, request_id=3
).json()
```

The desktop can take a few moments to connect after `initialize`. If the first `tools/list` or tool call fails, wait and retry. To end the session, send a signed `DELETE` request to the endpoint with the `Mcp-Session-Id` header.

The example follows these rules. Follow them in your own client too:
+ Include `_meta` on every request, not only on `initialize`. If it's missing from a later request, the streaming session is lost.
+ Compute the SigV4 signature over the exact bytes that you send, including `_meta`. If you change the body after you sign it, the request fails with a signature mismatch or a `Content-Length` error.
+ The `initialize` response returns an `Mcp-Session-Id` header. Send it on every later request. Without it, the service returns HTTP 400 with the message `Missing Mcp-Session-Id header`.
+ Send the SAML assertion and the stack ARN only in `_meta`. The service rejects a request that also sends them as headers.

The stack ARN must be in the same AWS account as the credentials that sign the request.

The SAML assertion is valid for a short time. When the agent starts a new session, it runs both exchanges again. Both exchanges require a valid token for the user, so the agent must refresh the user's token when it expires, as described in [Step 3: Connect the agent](agent-access-agent-identity-ndj.md#agent-access-agent-identity-ndj-connect) for non-domain-joined fleets.

The example signs every request with the same static credentials, so requests fail after the role session expires. Before that happens, run both exchanges again and sign later requests with the new credentials and SAML assertion.

## Step 5: Verify agent identity
<a name="agent-access-agent-identity-dj-verify"></a>

The following signals confirm that agent identity works on a domain-joined fleet. Each one proves something different.

1. **Both identities reached AWS**. In CloudTrail, the `AssumeRoleWithSAML` event for the role contains `AgentAccessAgentId`, `AgentAccessUserId`, `UserPrincipalName`, and `ObjectSid` in `principalTags`, and the user in `sourceIdentity`. The `ObjectSid` tag shows that the security identifier for the logon certificate arrived. The event can take several minutes to appear in CloudTrail.

1. **The user is recorded on agent actions**. Events with the event source `agentaccess-mcp.amazonaws.com` show the user in `userIdentity.sessionContext.sourceIdentity`. These events belong to the OIDC role session, because the agent signs MCP requests with the OIDC credentials. The SAML assertion establishes the streaming session but doesn't sign AWS requests.
**Note**  
Agent actions (tool calls, recorded as `CallReadOnlyTool` or `CallPrivilegedTool`) are data events. They appear in CloudTrail only if your trail logs data events for agent access. Without data events, you see only management events, such as `Initialize`, and not the agent's tool calls. For more information, see [Monitoring](agent-access-mcp-server-monitoring.md).

1. **Windows logged on with the certificate**. On the domain controller, the Security log shows event 4768 with pre-authentication type 16 and a certificate thumbprint, followed by events 4769 and 4624. Event 4771 indicates a failed certificate logon.

1. **The agent can act**. A successful `tools/list` request shows that the session is established. A successful `tools/call`, such as taking a screenshot, shows that the agent can act on the desktop.

## Troubleshooting
<a name="agent-access-agent-identity-dj-troubleshooting"></a>


**Troubleshooting agent identity on domain-joined fleets**  

| Symptom | Possible cause | Solution | 
| --- | --- | --- | 
| The SAML exchange fails, but the OIDC exchange works | The agent application doesn't have consent to the access\_as\_agent scope of the SAML application, or the SAML application has no application-specific signing certificate. | Grant the consent and add the certificate, as described in [Step 1: Create a SAML application in your identity provider](#agent-access-agent-identity-dj-saml-app). | 
| The MCP request fails with 403 Access denied by IAM policy | The role doesn't allow agentaccess-mcp actions. | Add the permissions in [Step 2: Configure IAM](agent-access-agent-identity-ndj.md#agent-access-agent-identity-ndj-iam). | 
| The streaming session fails with INVALID\_AUTH\_POLICY | The role doesn't allow appstream:Stream on the stack, or the stack ARN in the request isn't the one in the policy. | Allow appstream:Stream on the stack, as described in [Step 3: Configure IAM for SAML](#agent-access-agent-identity-dj-iam), and send the same stack ARN in \_meta. | 
| The session fails with CBA certificate fetch failed | WorkSpaces Applications can't issue the logon certificate from your private CA, because certificate-based authentication isn't working for the directory. | Confirm that certificate-based authentication works for a human user. For more information, see [Certificate-Based Authentication](certificate-based-authentication.md). | 