

# Setting up Dynamic Flows
<a name="managing-flows-dynamic"></a>

A Dynamic Flow calls your own HTTPS endpoint at runtime to fetch screen content and decide navigation. Static Flows define all screens in the Flow JSON. Dynamic Flows instead use the `data_exchange` action to request data from your endpoint each time a user navigates between screens. This enables personalized, data-driven experiences such as showing a user their open orders, validating input server-side, or branching based on a backend decision.

When a user interacts with a Dynamic Flow, Meta calls your endpoint directly with an encrypted request. Your endpoint decrypts the request, runs your business logic, encrypts the response, and returns it to Meta. The encrypted request and response pass directly between Meta and your endpoint, so AWS End User Messaging Social never has access to the decrypted content of these exchanges. AWS End User Messaging Social manages the control plane: creating and updating Flows, uploading the encryption public key, and delivering Flow health webhooks.

To set up a Dynamic Flow, you complete the following steps:

1. Deploy an HTTPS endpoint.

1. Upload a business public key for encryption.

1. Create the Flow with your endpoint URI.

1. Attach your Meta app for request verification.

1. Publish the Flow.

## Step 1: Deploy an HTTPS endpoint
<a name="managing-flows-dynamic-endpoint"></a>

Your endpoint must meet the following requirements:
+ Publicly accessible HTTPS URL with a valid TLS certificate.
+ Responds within 10 seconds. Meta enforces a hard timeout and monitors p90 latency. Endpoints that consistently exceed the latency threshold or return errors may be throttled or blocked.
+ Accepts POST requests containing encrypted JSON payloads.
+ Returns encrypted responses as `text/plain` (base64-encoded).

You can use any compute option that provides a public HTTPS URL. Common approaches include:
+ **AWS Lambda function URL** — A single function with a built-in HTTPS endpoint. Set the authorization type to `NONE` because Meta does not use . You authenticate requests using the business encryption key pair you configure in [Step 2: Upload a business public key](#managing-flows-dynamic-encryption).
+ **Amazon API Gateway with Lambda** — Provides additional controls such as resource policies to restrict source IPs, AWS WAF rules, and throttling.
+ **Elastic Load Balancing with Lambda targets** — Useful when you want to combine with existing load-balanced infrastructure.
+ Any other HTTPS server (containers, Amazon EC2 instances, or external services).

Your endpoint must implement Meta's data-exchange contract, which handles the following request types:
+ **Health check** — Meta sends periodic `ping` requests to verify your endpoint is available. Respond with `{"data": {"status": "active"}}`.
+ **INIT** — Sent when a user opens the Flow. Return the initial screen and its data.
+ **data\_exchange** — Sent each time a user submits a screen. Return the next screen and its data.
+ **BACK** — Sent when a user navigates back to a previous screen.

For the complete endpoint implementation guide, including encryption and decryption code samples in multiple languages, see [Implementing your Flow endpoint](https://developers.facebook.com/docs/whatsapp/flows/guides/implementingyourflowendpoint) on the Meta for Developers website.

## Step 2: Upload a business public key
<a name="managing-flows-dynamic-encryption"></a>

Meta encrypts all data-exchange requests end-to-end using your RSA (Rivest-Shamir-Adleman) public key. Your endpoint decrypts the requests using the corresponding private key. AWS End User Messaging Social uploads the public key to Meta on your behalf but never accesses or stores the private key.

Use the `PutWhatsAppBusinessPublicKey` API to upload a public key for a phone number. You must provide exactly one of the following:
+ **PEM-encoded RSA public key** — Provide the key directly. Your endpoint holds the corresponding private key for decryption.
+ **AWS Key Management Service key ARN** — Provide the ARN of an asymmetric RSA-2048 KMS key. AWS End User Messaging Social reads only the public half using `kms:GetPublicKey` and uploads it to Meta. The private key never leaves AWS KMS. Your endpoint uses `kms:Decrypt` to decrypt requests at runtime.

Providing both or neither returns an `InvalidParametersException`.

**PEM mode**

Generate an RSA key pair and upload the public key:

```
# Generate a key pair
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem

# Upload the public key
aws social-messaging put-whatsapp-business-public-key \
    --origination-phone-number-id {{{PHONE_NUMBER_ID}}} \
    --business-public-key "$(cat public.pem)"
```

Store the private key securely and make it available to your endpoint for decryption.

**AWS KMS mode**

Create an asymmetric RSA KMS key and upload its ARN:

```
# Create the KMS key
KMS_KEY_ARN=$(aws kms create-key \
    --key-spec RSA_2048 \
    --key-usage ENCRYPT_DECRYPT \
    --description "WhatsApp Dynamic Flow encryption key" \
    --query KeyMetadata.Arn --output text)

# Upload the KMS key ARN
aws social-messaging put-whatsapp-business-public-key \
    --origination-phone-number-id {{{PHONE_NUMBER_ID}}} \
    --kms-key-arn {{$KMS_KEY_ARN}}
```

The KMS key policy must grant the following permissions:
+ `kms:GetPublicKey` to the `social-messaging.amazonaws.com` service principal. This allows AWS End User Messaging Social to read the public key and upload it to Meta.
+ `kms:Decrypt` to your endpoint's execution role. This allows your endpoint to decrypt incoming data-exchange requests. AWS End User Messaging Social never calls `kms:Decrypt` on this key.

**Verifying the key**

Use the `GetWhatsAppBusinessPublicKey` API to verify the stored key and check Meta's signing status:

```
aws social-messaging get-whatsapp-business-public-key \
    --origination-phone-number-id {{{PHONE_NUMBER_ID}}}
```

The response includes the stored PEM and Meta's signing status (`VALID` or `MISMATCH`). A `MISMATCH` status indicates that the stored key does not match what Meta expected. Upload a new key if you see this status.

## Step 3: Create the Flow with an endpoint
<a name="managing-flows-dynamic-create"></a>

When creating a Dynamic Flow, provide the `--endpoint-uri` parameter with your HTTPS endpoint URL. The Flow JSON must also declare `data_api_version`, which tells Meta to call your endpoint during Flow sessions.

```
aws social-messaging create-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-name "{{my_dynamic_flow}}" \
    --categories '["OTHER"]' \
    --flow-json fileb://{{flow.json}} \
    --endpoint-uri "{{https://your-endpoint.example.com/flow}}"
```

You can also add or change the endpoint on an existing DRAFT Flow using `UpdateWhatsAppFlow`:

```
aws social-messaging update-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}} \
    --endpoint-uri "{{https://your-endpoint.example.com/flow}}"
```

**Note**  
When you publish a Dynamic Flow, Meta performs a synchronous health check against your endpoint. If the endpoint does not respond or returns an error, the publish operation fails with a Meta error such as `131000` ("verify that the endpoint is available and that you've implemented a health check"). A missing or invalid business public key can also cause this error. Before publishing, ensure that your endpoint is deployed and responding to `ping` requests, and that you have uploaded a valid business public key (see [Step 2: Upload a business public key](#managing-flows-dynamic-encryption)).

To verify the endpoint and data API version configured for a Flow, use `GetWhatsAppFlow`:

```
aws social-messaging get-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}}
```

The response includes the `endpointUri` as Meta holds it, the `dataApiVersion` declared in the Flow JSON, and the currently attached `application`.

## Step 4: Attach your Meta app for request verification
<a name="managing-flows-dynamic-app"></a>

By default, when you create a Flow through AWS End User Messaging Social, it is associated with the service's Meta app. To verify that data-exchange requests to your endpoint originate from Meta, attach your own Meta app to the Flow. Without your own app attached, request-origin verification is not possible. Attaching your app gives you access to the app secret needed to verify the `X-Hub-Signature-256` HMAC header that Meta includes on each request.

```
aws social-messaging update-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}} \
    --meta-app-id "{{{YOUR_META_APP_ID}}}"
```

The Meta app must be owned by the same business that owns the WhatsApp Business Account (WABA).

**Important**  
Attaching your own Meta app is a one-way operation. After you attach your app, the service's app cannot be reattached. This does not affect Flow functionality. Only a new Flow resets the app association.

You can set `--endpoint-uri` and `--meta-app-id` in the same call or in separate calls. The two fields are independent.

After attaching your app, verify the configuration by calling `GetWhatsAppFlow` and checking the `application` field in the response. The `application.id` should match the Meta app ID you provided.

## Securing your endpoint
<a name="managing-flows-dynamic-security"></a>

Because Meta calls your endpoint directly, consider the following security practices:
+ **Verify request signatures** — If you attached your own Meta app (Step 4), use the app secret to verify the `X-Hub-Signature-256` HMAC-SHA256 header on each request. This confirms the request originated from Meta. Return HTTP status 432 if verification fails.
+ **Validate flow tokens** — Generate a unique, unpredictable `flow_token` for each Flow session when sending the Flow to a user. Your endpoint receives the token inside the encrypted payload and should validate it against active sessions. Reject requests with unknown, expired, or already-completed tokens. This prevents unauthorized or replayed requests from reaching your business logic.
+ **Handle health checks without token validation** — Meta sends periodic `ping` requests to monitor endpoint health. These requests do not contain a `flow_token`. Respond to health checks without requiring token validation, because rejecting them degrades your endpoint's availability score.
+ **Return appropriate status codes** — Return 421 if your endpoint cannot decrypt the request (Meta refetches the public key and retries). Return 427 if the `flow_token` is invalid (Meta disables the Flow button for that session).

## Writing a Dynamic Flow JSON
<a name="managing-flows-dynamic-flow-json"></a>

A Dynamic Flow JSON differs from a static Flow JSON in two ways:

1. The top-level `data_api_version` field is required. This tells Meta to call your endpoint during Flow sessions. Supported values are `"3.0"` and `"4.0"` (recommended).

1. Screen footers use the `data_exchange` action instead of `navigate`. Each `data_exchange` action sends the form data to your endpoint, which returns the next screen and its content.

The following example shows a minimal Dynamic Flow JSON with two screens. The first screen collects a user's name and sends it to the endpoint. The endpoint returns a personalized greeting on the second screen.

```
{
    "version": "6.0",
    "data_api_version": "3.0",
    "routing_model": {
        "INPUT": ["RESULT"],
        "RESULT": []
    },
    "screens": [
        {
            "id": "INPUT",
            "title": "Welcome",
            "data": {
                "greeting": {
                    "type": "string",
                    "__example__": "Tell us your name"
                }
            },
            "layout": {
                "type": "SingleColumnLayout",
                "children": [
                    {
                        "type": "TextBody",
                        "text": "${data.greeting}"
                    },
                    {
                        "type": "Form",
                        "name": "input_form",
                        "children": [
                            {
                                "type": "TextInput",
                                "name": "user_name",
                                "label": "Your name",
                                "input-type": "text",
                                "required": true
                            },
                            {
                                "type": "Footer",
                                "label": "Submit",
                                "on-click-action": {
                                    "name": "data_exchange",
                                    "payload": {
                                        "user_name": "${form.user_name}"
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": "RESULT",
            "title": "Hello",
            "terminal": true,
            "data": {
                "message": {
                    "type": "string",
                    "__example__": "Hello, World!"
                }
            },
            "layout": {
                "type": "SingleColumnLayout",
                "children": [
                    {
                        "type": "TextBody",
                        "text": "${data.message}"
                    },
                    {
                        "type": "Footer",
                        "label": "Done",
                        "on-click-action": {
                            "name": "complete",
                            "payload": {}
                        }
                    }
                ]
            }
        }
    ]
}
```

For the complete Flow JSON schema reference, see [Flow JSON](https://developers.facebook.com/docs/whatsapp/flows/reference/flowjson) on the Meta for Developers website.

## End-to-end example
<a name="managing-flows-dynamic-example"></a>

The following example shows the full sequence of API calls to set up and publish a Dynamic Flow:

```
# 1. Upload the business public key (KMS mode)
aws social-messaging put-whatsapp-business-public-key \
    --origination-phone-number-id {{{PHONE_NUMBER_ID}}} \
    --kms-key-arn {{{KMS_KEY_ARN}}}

# 2. Create the Dynamic Flow with an endpoint
FLOW_ID=$(aws social-messaging create-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-name "{{my_dynamic_flow}}" \
    --categories '["OTHER"]' \
    --flow-json fileb://{{flow.json}} \
    --endpoint-uri "{{https://your-endpoint.example.com/flow}}" \
    --query flowId --output text)

# 3. Attach your Meta app for signature verification
aws social-messaging update-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id $FLOW_ID \
    --meta-app-id "{{{YOUR_META_APP_ID}}}"

# 4. Publish the Flow
aws social-messaging publish-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id $FLOW_ID

# 5. Verify the configuration
aws social-messaging get-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id $FLOW_ID
```

After publishing, the Flow is available for use in template messages. For more information about sending Flows, see [Sending WhatsApp Flows to users](managing-flows-send.md).