

# Webhook Events for a Custom Event Bus

With Webhook Events, you receive events from an external system, such as a software-as-a-service (SaaS) provider or your own application, that sends them to your Custom Event Bus over HTTPS. To use the feature, you create a *webhook event source*. EventBridge generates a unique HTTPS URL and a credential, and you configure that URL in the sending system. The sending system then makes an HTTPS `POST` request to the URL for each event, EventBridge verifies the request, and publishes the event to your bus, where your subscribers can filter, transform, and deliver it.

A webhook event source is one kind of *event source*, alongside AWS service event sources and partner event sources. For those other origin types, see [Event sources for a Custom Event Bus](eb-custom-bus-event-sources.md).

You do not run a server or manage an endpoint to receive webhook events. EventBridge hosts the endpoint, verifies each request against the credential you configure, and publishes accepted events to your bus.

This section contains the following topics:
+ [How webhook event sources work](#eb-custom-bus-webhook-sources-how)
+ [Create a webhook event source](#eb-custom-bus-webhook-sources-create)
+ [Securing a webhook event source](eb-custom-bus-webhook-auth.md)
+ [The event published to your bus](#eb-custom-bus-webhook-sources-event)
+ [Deduplicate webhook events](#eb-custom-bus-webhook-sources-dedup)
+ [Managing and revoking a webhook event source](#eb-custom-bus-webhook-sources-lifecycle)
+ [When a request is rejected](#eb-custom-bus-webhook-sources-errors)
+ [Troubleshooting webhook authentication errors](#eb-custom-bus-webhook-sources-troubleshooting)

## How webhook event sources work
<a name="eb-custom-bus-webhook-sources-how"></a>

A webhook event source has three pieces that EventBridge creates and manages for you:

The webhook URL  
A unique HTTPS URL that the sending system calls. EventBridge generates the URL when you create the event source, and it does not change for the life of the event source. Use the URL exactly as EventBridge returns it, and do not modify or recreate it yourself: configure it in the sending system exactly as returned, and store it securely.

The secret  
A secret that EventBridge uses to verify that each request genuinely comes from the sending system. EventBridge stores it as an AWS Secrets Manager secret in your account and returns the secret's ARN, not the secret value. You can let EventBridge generate the secret for you, or provide your own existing secret value when you create the event source. You choose how requests are verified, HMAC signature, a static token, or basic authentication, when you create the event source. For details, see [Securing a webhook event source](eb-custom-bus-webhook-auth.md).

The event source on your bus  
The resource that ties the URL and credential to your Custom Event Bus. Accepted events are published to this bus, where your subscribers receive them like any other event.

## Create a webhook event source
<a name="eb-custom-bus-webhook-sources-create"></a>

You create a webhook event source with the `CreateEventSource` operation, passing a webhook configuration that specifies how EventBridge verifies incoming requests and, optionally, which AWS KMS key encrypts the credential. You must also provide `RoleArn`, the IAM role EventBridge assumes both to read the signing secret and to publish the webhook's events to your bus. The role must belong to your account, trust `events.amazonaws.com`, and allow `events:PutWebhookEvents` on the destination bus, `secretsmanager:GetSecretValue` on the event source's secret, and, when you encrypt the secret with a customer managed AWS KMS key, `kms:Decrypt` on that key. A role that cannot read the secret causes EventBridge to reject every request with a `403` response.

The following example shows a least-privilege permissions policy for the role. Include the `kms:Decrypt` statement only when a customer managed key encrypts the credential; with the default Secrets Manager key, no AWS KMS grant is required. The role's trust policy must allow `events.amazonaws.com` to assume it.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublishWebhookEvents",
            "Effect": "Allow",
            "Action": "events:PutWebhookEvents",
            "Resource": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef"
        },
        {
            "Sid": "ReadWebhookSecret",
            "Effect": "Allow",
            "Action": "secretsmanager:GetSecretValue",
            "Resource": "arn:aws:secretsmanager:us-east-1:111122223333:secret:events-webhook!*"
        },
        {
            "Sid": "DecryptWithCustomerManagedKey",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ]
}
```

The following AWS CLI example creates a webhook event source that verifies requests with an HMAC signature. Because the example does not supply a secret value, EventBridge generates one for you.

```bash
aws eventsv2 create-event-source \
    --name orders-provider \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --configuration '{
        "WebhookEventsConfiguration": {
            "AuthConfiguration": {
                "HmacAuthConfiguration": {
                    "Algorithm": "SHA256",
                    "Encoding": "HEX",
                    "SignatureHttpHeader": "X-Signature",
                    "SignedMessageComposition": "BODY"
                }
            },
            "RoleArn": "arn:aws:iam::111122223333:role/orders-provider-webhook-role",
            "KmsKeyIdentifier": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    }'
```

```json
{
    "EventSourceArn": "arn:aws:events:us-east-1:111122223333:event-sourcev2/webhook/orders-provider/EXAMPLE1234567890abcde",
    "Name": "orders-provider",
    "EventBusArn": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef",
    "State": "ACTIVE",
    "EventSourceDetails": {
        "WebhookDetails": {
            "WebhookUrl": "https://<generated-at-creation>",
            "SecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:events-webhook!EXAMPLE-a1b2c3"
        }
    }
}
```

The response returns the webhook details, in `EventSourceDetails.WebhookDetails`, that you need to configure the sending system:

`WebhookUrl`  
The HTTPS URL to configure in the sending system.

`SecretArn`  
The ARN of the Secrets Manager secret, in your account, that holds the credential EventBridge verifies against.

**Note**  
The webhook URL and the credential are both sensitive, and EventBridge handles them differently:  
The *webhook URL* is returned by `CreateEventSource` and `DescribeEventSource`. Treat it as sensitive: anyone who has the URL and a valid credential can send events to your bus. EventBridge redacts the URL in AWS CloudTrail and in logs, so capture it from the `CreateEventSource` or `DescribeEventSource` response, rather than from logs, and store it securely.
The *credential* (the secret itself) is never returned by any EventBridge operation, including `CreateEventSource` and `DescribeEventSource`. These operations return only the secret's ARN (`SecretArn`), not its value, so that you can locate the secret in Secrets Manager. When EventBridge generates the credential for you, retrieve its value from Secrets Manager and configure it in the sending system, so that the sending system authenticates with the same credential EventBridge verifies against.

You can encrypt the credential with a customer managed AWS KMS key by setting `KmsKeyIdentifier`. If you omit it, EventBridge encrypts the secret with the AWS managed key for Secrets Manager (`aws/secretsmanager`). The authentication type is set when you create the event source and cannot be changed afterward; you can change the AWS KMS key later. For the full set of authentication options, how to supply your own credential, and what you can change later, see [Securing a webhook event source](eb-custom-bus-webhook-auth.md).

## The event published to your bus
<a name="eb-custom-bus-webhook-sources-event"></a>

When EventBridge accepts a webhook request, it publishes the request body to your bus as an event. The event's `Data` is the raw request body exactly as received, with a content type of `application/json`. Unlike events from AWS service and partner event sources, a webhook event does not set the `aws:Source` or `aws:DetailType` system metadata fields; its content is the raw request body in `Data`. Subscribers receive the event like any other event on a Custom Event Bus and can filter, transform, and deliver it. For the shape of the delivered event, including the `Data`, `Metadata`, and `SystemMetadata` components, see [Event structure: data, metadata, and system metadata](eb-custom-bus-addressing.md). To create a subscriber that receives these events, see [Subscribing to events on a Custom Event Bus](eb-custom-bus-subscribers.md).

By default, a webhook event carries only the request body in `Data`. To include selected request headers in the event, list their names in `MetadataHttpHeaders` on the webhook configuration. EventBridge copies each listed header from the incoming request into the event's `Metadata`, under the header's lowercase name, so that subscribers can read and filter on them. You can list up to 20 headers; header names are case-insensitive and can't repeat, and you can change the list later with `UpdateEventSource`.

When EventBridge copies a header, a header that appears more than once in the request is combined into a single value with its parts separated by a comma and a space. EventBridge drops a metadata value longer than 1,024 UTF-8 bytes, and a header that has an empty value; in both cases the event is still published.

Some headers can't be listed, and EventBridge rejects a configuration that includes them with an `InvalidInputException` (HTTP `400`): headers that carry credentials (such as `Authorization`), the header that carries your static token, the HMAC signature header, and headers that describe the network path (such as `Host` and the `X-Forwarded-*` headers).

## Deduplicate webhook events
<a name="eb-custom-bus-webhook-sources-dedup"></a>

A sending system can deliver the same webhook request more than once, for example when it retries after a network timeout. To have EventBridge detect and drop repeat events before they reach your bus, set `DeduplicationConfiguration` on the webhook configuration. If you omit it, EventBridge deduplicates nothing and publishes every accepted request.

Webhook events are deduplicated by content. Set `DeduplicationType` to `CONTENT_BASED`, and EventBridge detects duplicates from a hash of the event content within a 5-minute window. The hash covers the request body and any headers copied to event metadata, so a header whose value changes between requests, such as a timestamp or message-ID header, produces a different hash and defeats deduplication. When two requests produce the same content hash within 5 minutes, EventBridge publishes the first and drops the later ones. Deduplicating by a caller-supplied identifier is not available for a webhook event source: EventBridge deduplicates webhook events only by content, and does not use an identifier supplied in the request.

```bash
aws eventsv2 create-event-source \
    --name orders-provider-dedup \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --configuration '{
        "WebhookEventsConfiguration": {
            "AuthConfiguration": {
                "HmacAuthConfiguration": {
                    "Algorithm": "SHA256",
                    "Encoding": "HEX",
                    "SignatureHttpHeader": "X-Signature",
                    "SignedMessageComposition": "BODY"
                }
            },
            "RoleArn": "arn:aws:iam::111122223333:role/orders-provider-webhook-role",
            "DeduplicationConfiguration": {
                "DeduplicationType": "CONTENT_BASED"
            }
        }
    }'
```

## Managing and revoking a webhook event source
<a name="eb-custom-bus-webhook-sources-lifecycle"></a>

Use `DescribeEventSource` to view a webhook event source, including its state and the `WebhookUrl` and `SecretArn` in `EventSourceDetails.WebhookDetails`. Use `ListEventSources` to list the event sources on a bus.

To rotate the credential without changing the URL, use `RotateWebhookCredentials`. See [Securing a webhook event source](eb-custom-bus-webhook-auth.md).

To stop accepting events, you can revoke the event source, delete it, or deny access with an IAM policy:

Revoke  
The bus owner can revoke a webhook event source with `RevokeResource`. Revocation is terminal. After a source is revoked, EventBridge rejects subsequent requests to its URL with HTTP `403 Forbidden` and does not publish an event.

Delete  
Use `DeleteEventSource` to remove the event source. After deletion, requests to the URL are no longer accepted.

Deny with IAM  
The bus owner can add a `Deny` statement for the `events:PutWebhookEvents` action to the event bus resource policy, with the event source's role as the principal. EventBridge evaluates the bus resource policy when it forwards a webhook request, so a matching `Deny` stops events from being published. Unlike revocation, this is reversible: remove the statement to resume acceptance.

## When a request is rejected
<a name="eb-custom-bus-webhook-sources-errors"></a>

EventBridge verifies every incoming request before it publishes the event. If a request fails verification, EventBridge rejects it and does not publish an event. The sending system receives one of the following HTTP responses:


| HTTP status | Meaning | Common causes | 
| --- | --- | --- | 
| 200 OK | The request was accepted and the event was published to your bus, or dropped as a duplicate when deduplication is enabled. | Valid request that passed verification. | 
| 400 Bad Request | The request was malformed. | Missing or unreadable body; a request body that is not valid JSON; a request larger than the maximum size of 1 MB, counting the body plus any headers copied to event metadata; or a request method other than POST. | 
| 403 Forbidden | The request was not authorized. | Signature or token does not match the configured credential; a required signature or timestamp header is missing; the request timestamp is outside the allowed tolerance; the event source has been revoked; or EventBridge can no longer access the secret used to verify the request. | 
| 404 Not Found | The URL could not be resolved to a servable event source. | The URL has been altered, or the event source or its event bus no longer exists. EventBridge returns the same response for an unknown and an altered URL. | 
| 429 Too Many Requests | The request was throttled. | The request rate exceeded the allowed limit. | 
| 500 Internal Server Error | EventBridge could not process the request. | A transient service-side error; the sending system should retry. | 

EventBridge does not publish a webhook-specific request rate limit. A throttled request receives a `429 Too Many Requests` response, and the sending system should retry it with backoff.

## Troubleshooting webhook authentication errors
<a name="eb-custom-bus-webhook-sources-troubleshooting"></a>

Use the following symptom, cause, and solution to diagnose a webhook authentication failure.

Symptom  
The sending system reports that its webhook requests are failing with an authentication or signature error.

Cause  
The signature the sending system computes does not match the way the webhook event source is configured to verify it, or the configured credential does not match the one the sending system uses.

Solution  
Confirm the sending system's signing settings match the event source's authentication configuration, and that the credential matches.

Verification  
Resend a request from the sending system and confirm EventBridge accepts it and the event reaches your subscribers.