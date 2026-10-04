

# Operational notes
<a name="rd-operations"></a>

## Authentication and authorisation
<a name="rd-auth"></a>

 **Vehicle to cloud.** mTLS with a per-device certificate, checked by AWS IoT Core against a certificate authority operated by the fleet. Fleet-wide revocation is a certificate CRL update, propagated on the order of minutes. IoT policies attached to the certificate constrain the topics the vehicle may publish and subscribe to, so a compromised device cannot publish on another vehicle’s response topic.

 **Cloud API to cloud handler.** Standard cloud-native authentication and authorisation. The operator UI authenticates a human via the fleet’s identity provider; the resulting token accompanies every diagnostic request. The cloud handler performs fleet-scoped authorisation per vehicle — a caller with scope for fleet A cannot issue diagnostics against a vehicle in fleet B, and a caller with no fleet scope is denied by default. The most common regression to guard against is "empty scope means all scope" — treat an empty caller-scope set as *no* access, not as *unrestricted* access.

 **Cloud handler to vehicle.** The handler publishes with an IAM-authenticated identity. The IoT Rule that catches responses is invoked with a role scoped to the specific tables and buckets involved.

## Secrets posture
<a name="rd-secrets"></a>

No secrets are shipped in the sidecar’s environment. Cross-service credentials (for example, S3 upload of oversized responses) come from a task or instance role, not from environment variables. Runtime task-parameter overrides and Lambda environment variables are readable by the corresponding `Describe*` APIs and should not carry credentials.

## Deployment coupling
<a name="rd-deployment"></a>

Deploying the sidecar and the cloud handler is asynchronous. A cloud handler that supports a new `command_type` before any sidecar knows how to answer it produces `UNSUPPORTED_COMMAND` responses — graceful degradation, not failure. A sidecar that supports a new `command_type` before any cloud handler publishes it is dormant code. The peer-topic pattern makes rolling deployments non-blocking.

## Observability
<a name="rd-observability"></a>

Every request carries an `execId`; every response carries the same value as `correlation_id`. Latency is the response timestamp minus the request timestamp, recorded on the command record. IoT Core emits per-topic publish metrics; DynamoDB emits per-table write metrics; the sidecar emits per-command-type latency and success-rate metrics. A dashboard with four panels — publish rate, SUBACK rate, response latency, success/error breakdown by command\_type — is sufficient to see the entire system.