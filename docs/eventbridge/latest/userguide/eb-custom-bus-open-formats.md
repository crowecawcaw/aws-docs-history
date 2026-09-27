

# Supported content types: JSON, Avro, Protobuf, and raw bytes
<a name="eb-custom-bus-open-formats"></a>

`PutRawEvents` accepts any bytes. Each entry's `SystemMetadata.ContentType` tells EventBridge what the bytes are, and that value decides whether EventBridge deserializes the payload before it filters and delivers the event. For Avro and Protobuf, EventBridge deserializes the payload against a schema registry that you name on the request, so subscribers filter, transform, and receive the event as JSON. For opaque bytes, EventBridge delivers the payload untouched.


| `ContentType` | What EventBridge does with the payload | Schema registry | 
| --- | --- | --- | 
| application/json | Filters and transforms on the JSON content | Not used | 
| application/avro | Deserializes the Avro binary to JSON, then filters and transforms on that JSON | Required | 
| application/protobuf | Deserializes the Protobuf binary to JSON, then filters and transforms on that JSON | Required | 
| application/octet-stream | Does not deserialize or inspect the payload. Delivers the bytes as sent | Not used | 

## How EventBridge deserializes a payload
<a name="eb-custom-bus-open-formats-how"></a>

When an entry's `ContentType` is `application/avro` or `application/protobuf`, EventBridge performs the following steps for that entry.

1. EventBridge reads the schema identifier that the registry's serializer wrote into the payload bytes.

1. EventBridge fetches the matching schema from the registry you name in `SchemaRegistryConfiguration.RegistryUri`, and deserializes the payload to JSON. If the schema cannot be found or read, or the payload cannot be deserialized against it, the entry fails with a per-entry error and the other entries in the request are unaffected.

1. If a subscriber defines filters, EventBridge evaluates them against the deserialized JSON.

1. EventBridge applies the subscriber's transformation to the deserialized JSON and delivers JSON to the target.

You name the registry on each `PutRawEvents` request, in `SchemaRegistryConfiguration.RegistryUri`. The setting belongs to the request, not to the bus, and EventBridge ignores it for JSON entries in the same request. EventBridge reads the registry with the caller's credentials, so the identity that publishes needs read access to the registry.

After deserializing, the event behaves like any JSON event published with `PutRawEvents`. A filter with a scope of `DATA` matches fields of the deserialized record by their schema names, a JSONata transformer addresses them under `$events.Data`, and a target receives JSON. EventBridge also sets three keys in the delivered `SystemMetadata`.
+ `aws:SchemaId`: the identifier of the schema EventBridge deserialized with; a UUID for AWS Glue, an integer for Confluent.
+ `aws:RegistryType`: the registry that decoded the event, `Glue` or `Confluent`. Events published with `PutEvents` never carry it.
+ `ContentType`: the content type of the published entry, for example `application/avro`.

## Choosing how EventBridge delivers your payload
<a name="eb-custom-bus-open-formats-delivery"></a>

`ContentType` selects one of two delivery paths.
+ **Deserialize to JSON.** Set `ContentType` to `application/avro` or `application/protobuf`. EventBridge deserializes the payload against your schema registry, and subscribers filter on `DATA`, transform with JSONata, and receive JSON. Use this path when you want content-based routing and reshaping of schema-encoded events.
+ **Deliver bytes untouched.** Set `ContentType` to `application/octet-stream`. EventBridge does not deserialize or inspect the payload, no schema registry is involved, and the subscriber receives the exact bytes you sent. Use this path when you deserialize the payload yourself at the target, or when the content is a format EventBridge does not deserialize.

## Deserializing with the AWS Glue Schema Registry
<a name="eb-custom-bus-open-formats-glue"></a>

Set `RegistryUri` to the registry ARN, of the form `arn:aws:glue:{{region}}:{{account-id}}:registry/{{name}}`. Encode the payload with the AWS Glue Schema Registry serializer for your language before publishing; the serializer embeds the schema reference that EventBridge uses to resolve and deserialize the event.

EventBridge reads the schema as the publishing caller, so grant the publishing identity read access to the registry and its schemas. The following policy grants the minimum permission, scoped to one registry.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "glue:GetSchemaVersion",
            "Resource": [
                "arn:aws:glue:us-east-1:111122223333:registry/orders",
                "arn:aws:glue:us-east-1:111122223333:schema/orders/*"
            ]
        }
    ]
}
```

Publish the schema-encoded bytes with the Glue registry ARN in `RegistryUri`.

```
aws eventsv2 put-raw-events \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --schema-registry-configuration RegistryUri=arn:aws:glue:us-east-1:111122223333:registry/orders \
    --entries '[
        {
            "Data": "{{base64-encoded-avro-bytes}}",
            "SystemMetadata": { "ContentType": "application/avro", "EventGroupId": "order-1001" }
        }
    ]'
```

A subscriber then filters on the deserialized record. If the Avro schema has a field named `orderId`, the following filter matches one order.

```
{ "Scope": "DATA", "Pattern": "{\"orderId\":[\"1001\"]}" }
```

## Deserializing with a Confluent Schema Registry
<a name="eb-custom-bus-open-formats-confluent"></a>

Set `RegistryUri` to the registry's HTTPS URL. An HTTPS registry also requires `SchemaRegistryConfiguration.ConfluentPublicRegistryConfiguration.ConnectionArn`, the ARN of an EventBridge connection that holds the registry's API key or OAuth credentials. The connection must belong to the calling account; a cross-account connection is rejected. Create the connection before the first publish. Encode the payload with the Confluent serializer for your language before publishing; the serializer embeds the schema reference that EventBridge uses to resolve and deserialize the event.

EventBridge reads the registry credentials through the connection you name. Grant the publishing identity permission to read that connection's credentials.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "events:RetrieveConnectionCredentials",
            "Resource": "arn:aws:events:us-east-1:111122223333:connection/confluent-registry/*"
        },
        {
            "Effect": "Allow",
            "Action": ["secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret"],
            "Resource": "arn:aws:secretsmanager:us-east-1:111122223333:secret:events!connection/confluent-registry/*",
            "Condition": { "Bool": { "aws:ViaAWSService": "true" } }
        }
    ]
}
```

If the connection secret is encrypted with a customer managed AWS KMS key, also grant `kms:Decrypt` on that key.

Publish the schema-encoded bytes with the Confluent URL and connection ARN.

```
aws eventsv2 put-raw-events \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --schema-registry-configuration '{
        "RegistryUri": "https://psrc-example.us-east-1.aws.confluent.cloud",
        "ConfluentPublicRegistryConfiguration": {
            "ConnectionArn": "arn:aws:events:us-east-1:111122223333:connection/confluent-registry/EXAMPLE-1234-5678-abcd"
        }
    }' \
    --entries '[
        {
            "Data": "{{base64-encoded-protobuf-bytes}}",
            "SystemMetadata": { "ContentType": "application/protobuf" }
        }
    ]'
```

### Connection authentication options
<a name="eb-custom-bus-open-formats-confluent-auth"></a>

Configure the connection with the authentication type the Confluent registry expects. EventBridge reads only the authentication headers the connection produces; it never sees the raw secret, and it refreshes OAuth tokens automatically.

**API key.** Confluent Schema Registry typically uses HTTP Basic authentication with the schema registry API key as the user name and the API secret as the password.

```
aws events create-connection \
    --name confluent-registry \
    --authorization-type API_KEY \
    --auth-parameters '{
        "ApiKeyAuthParameters": {
            "ApiKeyName": "Authorization",
            "ApiKeyValue": "Basic {{base64(srApiKey:srApiSecret)}}"
        }
    }'
```

**OAuth client credentials.** EventBridge fetches and refreshes the token. You must include `grant_type=client_credentials` as a body parameter; EventBridge does not add it for you.

```
aws events create-connection \
    --name confluent-registry-oauth \
    --authorization-type OAUTH_CLIENT_CREDENTIALS \
    --auth-parameters '{
        "OAuthParameters": {
            "AuthorizationEndpoint": "https://{{idp-domain}}/oauth/token",
            "HttpMethod": "POST",
            "ClientParameters": {
                "ClientID": "{{oauth-client-id}}",
                "ClientSecret": "{{oauth-client-secret}}"
            },
            "OAuthHttpParameters": {
                "BodyParameters": [
                    { "Key": "grant_type", "Value": "client_credentials", "IsValueSecret": false }
                ]
            }
        }
    }'
```

EventBridge stores either credential in a managed Secrets Manager secret (`events!connection/...`), which the connection reads on your behalf.

## Delivering bytes without deserializing
<a name="eb-custom-bus-open-formats-passthrough"></a>

To have EventBridge deliver a payload exactly as sent, set the entry's `SystemMetadata.ContentType` to `application/octet-stream`. This is a field in each entry, not an HTTP header. EventBridge does not deserialize or inspect the bytes, and no schema registry is involved, so any format works, including Avro or Protobuf that you deserialize yourself at the target. Because the content is opaque, a `DATA` filter cannot match it. Route such events with filters on `METADATA`, using keys you set in the entry's `Metadata` map, or on `SYSTEM_METADATA`. Content-based deduplication still works and hashes the bytes exactly as you sent them. In a transformer, the payload appears as a Base64 string; see [Transforming events with JSONata](eb-custom-bus-transform.md).

## Filtering and transforming deserialized events
<a name="eb-custom-bus-open-formats-filtering"></a>

Once EventBridge deserializes an event to JSON, the payload flows through the normal pipeline. A filter with a scope of `DATA` matches the deserialized fields by their schema names, and a JSONata transformer addresses them under `$events.Data`. An event published as Avro or Protobuf gets the same content-based routing and per-subscriber reshaping as an event published as plain JSON. Write filter patterns against the deserialized JSON, keeping two conversion rules in mind.
+ **Avro** deserializes to standard JSON. The conversion is one-way: the JSON cannot be converted back to an Avro object.
+ **Protobuf** deserializes to JSON with the field names defined in your schema, rather than converting them to camel case as Protobuf tooling typically does. Match on the schema field names.

## Deduplicating events across formats
<a name="eb-custom-bus-open-formats-dedup"></a>

EventBridge supports two deduplication modes: ID-based, where you supply a `DeduplicationId` on the entry, and content-based, where EventBridge computes a SHA-256 hash of the event content. For deserialized events, content-based deduplication hashes the original Avro or Protobuf wire bytes, not the deserialized JSON. Two events are duplicates only when their original payloads are byte-identical. The same logical event published in different formats is therefore not deduplicated: Avro bytes, Protobuf bytes, and raw JSON differ on the wire even when they deserialize to the same data. See [Ordering and deduplicating events on a Custom Event Bus](eb-custom-bus-ordering.md).

## Errors
<a name="eb-custom-bus-open-formats-errors"></a>
+ An Avro or Protobuf entry published without `SchemaRegistryConfiguration` fails as a per-entry error with an `ErrorCode` of `VALIDATION_ERROR` and a message that states `SchemaRegistryConfiguration is required`. The other entries in the request are unaffected.
+ A `ConnectionArn` that does not name a usable connection, or that belongs to another account, fails the entry with `VALIDATION_ERROR` and a message that names the registry.
+ A schema that cannot be found or read, or a payload that cannot be deserialized against it, fails that entry with `VALIDATION_ERROR`. This error is not retryable; fix the request or the caller's registry access before republishing.
+ A registry that cannot be reached fails the request with `SchemaRegistryUnavailableException`. On the Confluent OAuth path, this can occur while the registry access token is being refreshed. This error is transient; retry the request with backoff.

For per-entry results and retry guidance in general, see [Publishing events to a Custom Event Bus](eb-custom-bus-publish.md).