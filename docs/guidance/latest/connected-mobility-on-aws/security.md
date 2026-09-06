

# Security
<a name="security"></a>

## Shared responsibility model
<a name="shared-responsibility"></a>

This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](http://aws.amazon.com/security/).

## Security features
<a name="security-features"></a>

Security is built into every layer of the Connected Mobility guidance:

 **Device Authentication** - X.509 certificates provide mutual authentication between vehicles and AWS IoT Core, ensuring only authorized devices can connect.

 **Data in Transit** - All communication uses TLS encryption, including MQTT over TLS for vehicle communication and SASL\_SSL for Kafka communication.

 **Access Control** - IAM roles and policies provide fine-grained access control for all AWS services, following the principle of least privilege.

 **Credential Management** - SCRAM credentials for MSK are securely stored in AWS Secrets Manager with automatic rotation capabilities.

 **Network Security** - MSK clusters deploy in private subnets with security groups restricting access to authorized components only.

 **Data at Rest** - DynamoDB tables and S3 buckets use AWS KMS encryption for data at rest protection.

## Identity and access management
<a name="authentication-and-authorization"></a>

### Amazon Cognito user pools
<a name="cognito-user-pools"></a>

The Fleet Manager UI and all REST API routes authenticate users through an Amazon Cognito user pool. After a user authenticates, Cognito issues a JWT that clients include in every request. The API Gateway REST authorizer validates the token signature against the user pool JWKS before admitting the request to any Lambda handler.

Three Cognito groups govern what an authenticated user can do:


| Group | Permissions | 
| --- | --- | 
|  `platform-admin`  | Cross-fleet authority. Members can manage all fleets, enroll and unenroll vehicles across any fleet, access all administrative API routes, and view all telemetry data regardless of fleet membership. | 
|  `fleet-operator`  | Per-fleet authority, scoped by the `custom:fleetIds` claim in the user’s Cognito attributes. A fleet-operator user can manage vehicles and view telemetry only for the specific fleets listed in that claim. Administrative API routes that mutate fleet state enforce this scope server-side. | 
|  `fleet-viewer`  | Read-only access scoped in the same way as `fleet-operator`. Members can view vehicle state, trip history, safety alerts, and maintenance alerts for their assigned fleets but cannot perform write operations. | 

Add a user to a group with the AWS CLI after deployment:

```
aws cognito-idp admin-add-user-to-group \
  --user-pool-id <UserPoolId> \
  --username <username> \
  --group-name platform-admin
```

### IoT device authentication
<a name="iot-device-auth"></a>

Each vehicle connects to AWS IoT Core using an X.509 client certificate. The provisioning workflow issues a unique certificate per device; the IoT policy attached to the certificate limits that device to publishing on topics scoped to its own vehicle identifier. Certificate rotation and revocation follow standard AWS IoT Core certificate management procedures.

## Security configuration defaults
<a name="security-configuration-defaults"></a>

The guidance ships with three CDK context flags that control security-sensitive behaviors. All three default to `false`, which is the recommended production posture.


| CDK context flag | Default | What it controls | 
| --- | --- | --- | 
|  `cms.allow_self_signup`  |  `false`  | Controls whether Cognito user pool self-registration is enabled. When `false`, new user accounts must be created by an administrator. Set to `true` only in demo environments where unrestricted sign-up is acceptable. | 
|  `cms.allow_unauth_map_auth`  |  `false`  | Controls whether the Cognito identity pool issues credentials to unauthenticated callers. When `false`, the unauthenticated identity role is not created and anonymous callers cannot retrieve map tiles. Set to `true` only for demos that require anonymous map preview. | 
|  `cms.allow_unauth_websocket`  |  `false`  | Controls WebSocket API `$connect` authorization. When `false`, anonymous WebSocket upgrade requests return HTTP 401. When `true`, the `$connect` route accepts unauthenticated connections. Set to `true` only for demos that require anonymous WebSocket access. | 

To opt in for a demo deployment, pass the flags at synth time rather than changing `cdk.json`:

```
cdk synth \
  --context cms.allow_self_signup=true \
  --context cms.allow_unauth_map_auth=true
```

## API and WebSocket security
<a name="websocket-security"></a>

### REST API authorization
<a name="rest-api-auth"></a>

The REST API Gateway uses a Cognito user pool authorizer. Every route under `/api/v1/*` requires a valid, unexpired Cognito ID token in the `Authorization` header. Requests that omit the header or present an invalid token receive HTTP 401 before reaching any Lambda handler.

Administrative routes under `/admin/*` additionally verify that the authenticated user belongs to the `platform-admin` or `fleet-operator` group. A valid token from a `fleet-viewer` user is rejected with HTTP 403 on write routes.

### WebSocket authorization
<a name="websocket-auth"></a>

The real-time telemetry WebSocket API uses a Lambda REQUEST authorizer on the `$connect` route. Clients must include the Cognito ID token as a query parameter on the upgrade URL:

```
wss://<WebSocketEndpoint>/live?token=<jwt>&fleetId=<fleetId>
```

The Lambda authorizer validates the token signature against the Cognito user pool JWKS. An upgrade request that omits the `token` parameter, provides an expired token, or provides a token that does not belong to the configured user pool receives HTTP 401 and the connection is not established.

After a successful `$connect`, the authorized fleet scope governs which telemetry messages the WebSocket server fans out to that connection:
+  `fleet-operator` and `fleet-viewer` connections receive telemetry for the fleets listed in their `custom:fleetIds` claim.
+  `platform-admin` connections receive all-fleet telemetry fanout with no fleet-scope restriction.

When the `cms.allow_unauth_websocket` context flag is `true`, the `$connect` authorizer is replaced with `NONE` and all connections are admitted without a token. This setting is not appropriate for production deployments.

## Encryption
<a name="encryption"></a>

### Encryption at rest
<a name="encryption-at-rest"></a>

All persistent data stores use server-side encryption:
+  **Amazon DynamoDB** - All tables use AWS-managed KMS keys (SSE-KMS). Vehicle telemetry records, trip history, safety events, maintenance alerts, commands, campaign state, and driver data are encrypted at rest.
+  **Amazon S3** - All buckets use AES-256 server-side encryption (SSE-S3). Raw telemetry archives, FleetWise decoder manifests, signal catalogs, and UI static assets are encrypted at rest.
+  **Amazon ElastiCache for Redis** - The Last Known State cache uses at-rest encryption. Cached vehicle state, geolocation data, and time-series streams are protected at the storage layer.
+  **Amazon MSK** - The Kafka cluster uses at-rest encryption for all broker storage. Telemetry events, trip records, and OEM telemetry payloads are encrypted before being written to broker disk.

### Encryption in transit
<a name="encryption-in-transit"></a>

All data movement between services uses transport-layer encryption:
+  **MQTT over TLS** - Vehicles connect to AWS IoT Core over MQTT with TLS 1.2 or later. Mutual authentication uses X.509 certificates; the broker rejects connections that do not present a valid client certificate.
+  **MSK TLS and SASL/SCRAM** - Flink applications and the OEM cloud connector communicate with MSK brokers over TLS. SASL/SCRAM-512 credentials for MSK are stored in AWS Secrets Manager and are not embedded in application configuration.
+  **HTTPS and WSS** - The Fleet Manager UI, REST API, and WebSocket API are served exclusively over HTTPS and WSS (TLS 1.2\+). Unencrypted HTTP connections are not accepted.
+  **Internal service-to-service calls** - Lambda-to-DynamoDB, Lambda-to-ElastiCache, and Flink-to-MSK traffic stays within the VPC and transits over encrypted channels.

## Data retention and deletion
<a name="data-retention"></a>

### S3 bucket retention
<a name="bucket-retain-aspect"></a>

Globally named S3 buckets in the guidance are configured with `RemovalPolicy.RETAIN`. When a CloudFormation stack is deleted, these buckets and their contents are retained and are not removed automatically. This behavior is intentional to prevent accidental data loss during stack teardown.

After uninstalling the guidance, you must delete the retained buckets manually. For step-by-step instructions, see the [Uninstall the guidance](uninstall-the-solution.md) chapter.

### DynamoDB record lifecycle
<a name="dynamodb-ttl"></a>

Certain DynamoDB tables use time-to-live (TTL) attributes to bound record retention:
+  **Command records** - Expire after 7 days.
+  **Telemetry snapshot records** - Expire after 30 days.
+  **Simulation session records** - Expire after 24 hours.

Records past their TTL are deleted asynchronously by DynamoDB at no additional cost.

## Network security
<a name="security-network-isolation"></a>

### VPC isolation
<a name="vpc-isolation"></a>

The guidance deploys compute and data resources in a dedicated Amazon VPC with separate public and private subnet tiers across two Availability Zones:
+  **Private subnets** - MSK brokers, ElastiCache nodes, Flink application workers, and the OEM cloud connector run in private subnets without direct internet egress. Outbound traffic to AWS service endpoints uses VPC Gateway Endpoints (Amazon DynamoDB, Amazon S3) or VPC Interface Endpoints where applicable, so traffic does not leave the AWS network.
+  **IoT Rule VPC Destination** - The IoT Core rule that routes incoming telemetry to MSK uses a VPC Destination, allowing the IoT Rules engine to write to the private MSK cluster without opening MSK broker ports to the internet.

### Security group controls
<a name="security-groups"></a>

Security groups implement a least-privilege inbound allow model between components:
+ MSK brokers accept TLS connections only from the Flink application security group, the OEM connector security group, and the telemetry-integration Lambda security group. No inbound access is permitted from the public subnets.
+ ElastiCache nodes accept connections only from the API handler Lambda security group. Direct access from outside the VPC is not possible.
+ Flink application containers accept management traffic only from the Amazon Managed Service for Apache Flink control plane on the designated management port; application-layer ingress from other components is blocked.

### Optional access restriction for the frontend distribution
<a name="optional-access-restriction"></a>

The Fleet Manager UI is served through Amazon CloudFront. Deployments that require restricting access to a specific set of users can optionally configure a [CloudFront trusted key group](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html) to issue signed cookies or signed URLs. This is a standard CloudFront capability and is not configured by default. When deployed without a trusted key group, the CloudFront distribution is publicly reachable and access control is enforced entirely by the Cognito user pool at the API and WebSocket layers.