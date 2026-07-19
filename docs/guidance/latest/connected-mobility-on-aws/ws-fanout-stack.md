# WebSocket telemetry fan-out (WsFanoutStack)

The WsFanoutStack deploys an ECS Fargate task that consumes per-fleet Kafka topics and pushes live telemetry updates to connected Fleet Manager UI clients over WebSocket.

## Fan-out architecture

The ECS Fargate worker maintains an active Kafka consumer group (`cms-{stage}-ws-fanout-consumer`) and subscribes to per-fleet telemetry topics derived from the MSK cluster.
On each Kafka message, the worker queries the `cms-{stage}-storage-ws-connections` DynamoDB table to find all active WebSocket connection IDs for the vehicle’s fleet, then calls the API Gateway Management API (`@connections/{connectionId}`) to push the telemetry payload to each connected browser.

**Key components:**

- **MSK consumer** — Reads from per-fleet telemetry topics using SASL/IAM authentication.
- **DynamoDB connections table** (`cms-{stage}-storage-ws-connections`) — Stores active connection ID, fleet ID, and connection timestamp for each connected client.
- **API Gateway WebSocket API** — Manages WebSocket lifecycle (`$connect`, `$disconnect`, `$default` routes).
- **`$connect` Lambda authorizer** — A Cognito JWT REQUEST authorizer validates the `?token=<jwt>` query parameter on every WebSocket upgrade request.
  Connections without a valid token receive HTTP 401 and are rejected before establishing.
  Fleet-operator connections are scoped to their authorized fleet IDs from the JWT `custom:fleetIds` claim.

## WebSocket security posture

Anonymous WebSocket upgrades are disabled by default.
The `cms.allow_unauth_websocket` CDK context flag (default `false`) controls whether the `$connect` authorizer allows unauthenticated connections.
Set this flag to `true` only for demo or development environments where anonymous map access is acceptable.
