# Invoking DevOps Agent through Webhook

Webhooks allow external systems to automatically trigger AWS DevOps Agent investigations. This enables integration with ticketing systems, monitoring tools, and other platforms that can send HTTP requests when incidents occur.

## Prerequisites

Before configuring webhook access, ensure you have:

- An Agent Space configured in AWS DevOps Agent
- Access to the AWS DevOps Agent console
- The external system that will send webhook requests

## Webhook types

AWS DevOps Agent supports the following types of webhooks:

- **Integration-specific webhooks** – Automatically generated when you configure third-party integrations like Dynatrace, Splunk, Datadog, New Relic, ServiceNow, or Slack. These webhooks are associated with the specific integration and use authentication methods determined by the integration type
- **Generic webhooks** – Can be manually created for triggering investigations from any source not covered by a specific integration. In the AWS DevOps Agent console, a generic webhook is created as an **Agent Space webhook** (scoped to an Agent Space). When you create a generic webhook, you choose its authentication method: **HMAC** or **API key** (bearer token).
- **Grafana alert webhooks** – Grafana can send alert notifications directly to AWS DevOps Agent through webhook contact points. For setup instructions including a custom notification template, see [Connecting Grafana](connecting-telemetry-sources-connecting-grafana.md "connecting-telemetry-sources-connecting-grafana.md").

## Webhook authentication methods

The authentication method for your webhook depends on which integration it's associated with:

**HMAC authentication** – Used by:

- Dynatrace integration webhooks
- Generic webhooks (select **HMAC** at creation)
- MCP server webhooks (select **HMAC** at creation)

**Bearer token authentication** – Used by:

- Splunk integration webhooks
- Datadog integration webhooks
- New Relic integration webhooks
- ServiceNow integration webhooks
- Slack integration webhooks
- Grafana integration webhooks
- Generic webhooks (select **API key** at creation)
- MCP server webhooks (select **API key** at creation)

### Understanding HMAC authentication

HMAC (Hash-based Message Authentication Code) is a cryptographic mechanism that verifies both the integrity and authenticity of a webhook request. When you send a webhook with HMAC authentication, you generate a signature by hashing the request timestamp and payload together using your secret key with the SHA-256 algorithm. AWS DevOps Agent independently computes the same hash on its side and compares the two signatures. If they match, the request is accepted.

Because the timestamp is included in the signature, HMAC also provides replay protection — AWS DevOps Agent can reject requests with timestamps that are too far in the past, preventing an attacker from capturing and resending a valid request.

### Choosing between HMAC and Bearer token

| Consideration        | HMAC                                                                                                                                     | Bearer token                                                                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Setup complexity     | More complex — your client must compute a signature for each request using the timestamp and payload                                     | Simpler — include a static token in the `Authorization` header                                                                          |
| Payload integrity    | Verified — any modification to the payload after signing invalidates the signature                                                       | Not verified — the token authenticates the sender but does not protect the payload contents                                             |
| Replay protection    | Built-in — the timestamp in the signature allows the server to reject stale requests                                                     | Not built-in — a captured token can be reused until it is rotated                                                                       |
| Secret exposure risk | Lower — the secret is never transmitted in the request; only the computed signature is sent                                              | Higher — the token is sent in every request header, increasing exposure if traffic is intercepted                                       |
| When to use          | Recommended when you need stronger security guarantees, such as for generic webhooks or environments with strict compliance requirements | Suitable when ease of integration is a priority and your network transport is trusted, such as for managed SaaS integrations over HTTPS |

## Configuring webhook access

### Step 1: Navigate to the webhook configuration

1. Sign in to the AWS Management Console and navigate to the AWS DevOps Agent console
2. Select your Agent Space
3. Go to the **Capabilities** tab
4. In the **Webhook** section, choose **Configure**

### Step 2: Generate webhook credentials

**For integration-specific webhooks:**

Webhooks are automatically generated when you complete the configuration of a third-party integration. The webhook endpoint URL and credentials are provided at the end of the integration setup process.

**For generic webhooks:**

1. Choose **Generate webhook**
2. For **Webhook authentication type**, choose **HMAC** or **API key**:

   - **HMAC** – The system generates a webhook signing secret. Your client signs each request and sends the signature in the `x-amzn-event-signature` header (see Version 1 below).
   - **API key** – The system generates an API key (bearer token). Your client sends it in the `Authorization: Bearer <token>` header (see Version 2 below).

3. Securely store the generated secret or API key. You won't be able to retrieve it again.
4. Copy the webhook endpoint URL provided

### Step 3: Configure your external system

Use the webhook endpoint URL and credentials to configure your external system to send requests to AWS DevOps Agent. The specific configuration steps depend on your external system.

## Managing webhook credentials

Webhook credentials are sensitive. AWS DevOps Agent shows the webhook secret one time, when you create the webhook. It does not return the secret again through the console, the API, or infrastructure as code. The webhook URL stays available. If you lose the secret, or you create the webhook without recording it, rotate the webhook to generate a new secret.

### Rotating webhook credentials

You can rotate the credentials of any webhook from the **Capabilities** tab. Rotation keeps the same webhook URL and generates a new secret. Rotation invalidates the previous secret, so the sender stops until you update it with the new secret. Rotate a webhook when you lose the secret, or when you want to replace a secret that might be compromised.

To rotate a webhook:

1. Sign in to the AWS Management Console and open the AWS DevOps Agent console.
2. Select your Agent Space.
3. Go to the **Capabilities** tab, then find the webhook:

   - For an integration webhook, use the **Capability Webhooks** table. Find the integration by its **Identifier**, for example your ServiceNow instance URL or your Grafana endpoint.
   - For a generic webhook, use the **Agent Space Webhook** section.

4. Open the webhook editor. For an integration webhook, choose **Edit**. For a generic webhook, choose **Actions**, then **Edit**.
5. Choose **Rotate webhook**. The console generates a new secret and keeps the same webhook URL.
6. Choose **Download .csv file** to save the URL and secret, then confirm that you saved them. You cannot retrieve the secret after you leave this page.
7. Update the sender with the new secret. For an integration, expand **Service Setup Instructions** for service-specific steps, or see the connection guide for your integration.

To copy the webhook URL without rotating the secret, choose **Copy URL**.

### Webhooks created with infrastructure as code

When you create a webhook with AWS CloudFormation, the AWS CDK, or Terraform, the stack does not return the webhook secret as an output, because it is a sensitive value. After the deployment completes, get the secret by rotating the webhook, as described in the previous section. Then configure your third-party service with the webhook URL and new secret.

### Removing webhook credentials

To delete a generic webhook, open the **Agent Space Webhook** section, choose **Actions**, then choose **Remove**. After you remove the webhook, the endpoint no longer accepts requests until you create a new webhook.

## Using the webhook

### Webhook request format

To trigger an investigation, your external system should send an HTTP POST request to the webhook endpoint URL.

**For Version 1 (HMAC authentication):**

Headers:

- `Content-Type: application/json`
- `x-amzn-event-signature: <HMAC signature>`
- `x-amzn-event-timestamp: <+%Y-%m-%dT%H:%M:%S.000Z>`

The HMAC signature is generated by signing the request body with your secret key using SHA-256.

**For Version 2 (Bearer token authentication):**

Headers:

- `Content-Type: application/json`
- `Authorization: Bearer <your-token>`

**Request body:**

The request body should include information about the incident:

```
{
  "eventType": "incident",
  "incidentId": "incident-123",
  "action": "created",
  "priority": "HIGH",
  "title": "High CPU usage on production server",
  "description": "High CPU usage on production server host ABC in AWS account 1234 region us-east-1",
  "timestamp": "2025-11-23T18:00:00Z",
  "service": "MyProductionService",
  "data": {
    "metadata": {
      "region": "us-east-1",
      "environment": "production"
    }
  }
}
```

**Payload schema:**

```
{
    eventType: 'incident';
    incidentId: string;
    action: 'created' | 'updated' | 'closed' | 'resolved';
    priority: "CRITICAL" | "HIGH" | "MEDIUM" | "LOW" | "MINIMAL";
    title: string;
    description?: string;
    timestamp?: string;
    service?: string;
    // The original event generated by service is attached here.
    data?: object;
}
```

### Example code

**Version 1 (HMAC authentication) - JavaScript:**

```
const crypto = require('crypto');

// Webhook configuration
const webhookUrl = 'https://your-webhook-endpoint.amazonaws.com/invoke';
const webhookSecret = 'your-webhook-secret-key';

// Incident data
const incidentData = {
    eventType: 'incident',
    incidentId: 'incident-123',
    action: 'created',
    priority: "HIGH",
    title: 'High CPU usage on production server',
    description: 'High CPU usage on production server host ABC in AWS account 1234 region us-east-1',
    timestamp: new Date().toISOString(),
    service: 'MyTestService',
    data: {
      metadata: {
        region: 'us-east-1',
        environment: 'production'
      }
    }
};

// Convert data to JSON string
const payload = JSON.stringify(incidentData);
const timestamp = new Date().toISOString();
const hmac = crypto.createHmac("sha256", webhookSecret);
hmac.update(`${timestamp}:${payload}`, "utf8");
const signature = hmac.digest("base64");

// Send the request
fetch(webhookUrl, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'x-amzn-event-timestamp': timestamp,
    'x-amzn-event-signature': signature
  },
  body: payload
})
.then(res => {
  console.log(`Status Code: ${res.status}`);
  return res.text();
})
.then(data => {
  console.log('Response:', data);
})
.catch(error => {
  console.error('Error:', error);
});
```

**Version 1 (HMAC authentication) - cURL:**

```
#!/bin/bash

# Configuration
WEBHOOK_URL="https://event-ai.us-east-1.api.aws/webhook/generic/YOUR_WEBHOOK_ID"
SECRET="YOUR_WEBHOOK_SECRET"

# Create payload
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%S.000Z)
INCIDENT_ID="test-alert-$(date +%s)"

PAYLOAD=$(cat <<EOF
{
"eventType": "incident",
"incidentId": "$INCIDENT_ID",
"action": "created",
"priority": "HIGH",
"title": "Test Alert",
"description": "Test alert description",
"service": "TestService",
"timestamp": "$TIMESTAMP"
}
EOF
)

# Generate HMAC signature
SIGNATURE=$(echo -n "${TIMESTAMP}:${PAYLOAD}" | openssl dgst -sha256 -hmac "$SECRET" -binary | base64)

# Send webhook
curl -X POST "$WEBHOOK_URL" \
-H "Content-Type: application/json" \
-H "x-amzn-event-timestamp: $TIMESTAMP" \
-H "x-amzn-event-signature: $SIGNATURE" \
-d "$PAYLOAD"
```

**Version 2 (Bearer token authentication) - JavaScript:**

```
function sendEventToWebhook(webhookUrl, secret) {
  const timestamp = new Date().toISOString();

  const payload = {
    eventType: 'incident',
    incidentId: 'incident-123',
    action: 'created',
    priority: "HIGH",
    title: 'Test Alert',
    description: 'Test description',
    timestamp: timestamp,
    service: 'TestService',
    data: {}
  };

  fetch(webhookUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-amzn-event-timestamp": timestamp,
      "Authorization": `Bearer ${secret}`,  // Fixed: template literal
    },
    body: JSON.stringify(payload),
  });
}
```

**Version 2 (Bearer token authentication) - cURL:**

```
#!/bin/bash

# Configuration
WEBHOOK_URL="https://event-ai.us-east-1.api.aws/webhook/generic/YOUR_WEBHOOK_ID"
SECRET="YOUR_WEBHOOK_SECRET"

# Create payload
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%S.000Z)
INCIDENT_ID="test-alert-$(date +%s)"

PAYLOAD=$(cat <<EOF
{
"eventType": "incident",
"incidentId": "$INCIDENT_ID",
"action": "created",
"priority": "HIGH",
"title": "Test Alert",
"description": "Test alert description",
"service": "TestService",
"timestamp": "$TIMESTAMP"
}
EOF
)

# Send webhook
curl -X POST "$WEBHOOK_URL" \
-H "Content-Type: application/json" \
-H "x-amzn-event-timestamp: $TIMESTAMP" \
-H "Authorization: Bearer $SECRET" \
-d "$PAYLOAD"
```

## Troubleshooting webhooks

### If you do not receive a 200

A 200 and a message like webhook received indicate the authentication passed and the message has been queued for the system to verify and process. If you do not get a 200 but a 4xx most likely there is something wrong with the authentication or headers. Try sending manually using the curl options to help debug the authentication.

### If you receive a 200 but an investigation does not start

Likely cause is a misformated payload.

1. Check both timestamp and incident id are updated and unique. Duplicate messages are deduplicated.
2. Check the message is valid JSON
3. Check the format is correct

### If you receive a 200 and investigation is immediately cancelled

Most likely you have hit the limit for the month. Please talk to your AWS contact to ask for a rate limit change if appropriate.

## Related topics

- [Creating an Agent Space](getting-started-with-aws-devops-agent-creating-an-agent-space.md "getting-started-with-aws-devops-agent-creating-an-agent-space.md")
- [What is a DevOps Agent Web App?](about-aws-devops-agent-what-is-a-devops-agent-web-app.md "about-aws-devops-agent-what-is-a-devops-agent-web-app.md")
- [DevOps Agent IAM permissions](aws-devops-agent-security-devops-agent-iam-permissions.md "aws-devops-agent-security-devops-agent-iam-permissions.md")
