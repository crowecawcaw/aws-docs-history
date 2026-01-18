# Vehicle Connectivity and Provisioning

The guidance uses AWS IoT Core as a simple, scalable connectivity layer for vehicle telemetry ingestion. Vehicles connect via MQTT and publish telemetry directly to topics, with IoT Core routing messages to Amazon MSK for processing.

**Simplified IoT Architecture**:

Unlike traditional IoT implementations with complex provisioning workflows, this guidance focuses on IoT Core as a high-performance message broker:

- **No Device Shadows**: Vehicles don’t maintain virtual state representations
- **No Fleet Provisioning**: No automated certificate generation workflows
- **No JITR (Just-in-Time Registration)**: No automatic device registration on first connection
- **Simple Topic-Based Routing**: Vehicles publish to topics, IoT Rules Engine routes to MSK
  This simplified approach reduces operational complexity while maintaining enterprise-scale performance and security.

**MQTT Connectivity**:

Vehicles connect to AWS IoT Core using standard MQTT protocol:

- **Protocol**: MQTT 3.1.1 over TLS 1.2+
- **Authentication**: X.509 client certificates (mutual TLS)
- **Connection Endpoint**: Regional IoT Core endpoint (e.g., `a1b2c3d4e5f6g7.iot.us-east-1.amazonaws.com`)
- **Port**: 8883 (MQTT over TLS)
- **QoS Levels**: QoS 0 (at most once) or QoS 1 (at least once)

**Topic Structure**:

Vehicles publish telemetry to a simple topic structure:

```
fleet/{fleet-id}/vehicle/{vehicle-id}/telemetry
```

Example: `fleet/delivery-fleet-123/vehicle/VIN12345/telemetry`

The IoT Rules Engine uses SQL pattern matching to route all telemetry:

```
 SELECT * FROM 'fleet/+/vehicle/+/telemetry'
```

The `+` wildcard matches any fleet ID and vehicle ID, enabling dynamic vehicle registration without rule updates.

**Certificate Management**:

Vehicles authenticate using X.509 certificates:

- **Certificate Generation**: Certificates generated externally (during manufacturing or dealer activation)
- **Certificate Storage**: Stored securely on vehicle (TPM, secure element, or encrypted filesystem)
- **Certificate Registration**: Certificates registered in IoT Core via AWS CLI, SDK, or Console
- **Certificate Validity**: Typically 10-20 years for vehicle certificates
- **Certificate Revocation**: Compromised certificates can be deactivated in IoT Core

**Basic Certificate Setup**:

```
 # Create certificate and keys
aws iot create-keys-and-certificate \
  --set-as-active \
  --certificate-pem-outfile vehicle-cert.pem \
  --public-key-outfile vehicle-public.key \
  --private-key-outfile vehicle-private.key

# Attach policy to certificate
aws iot attach-policy \
  --policy-name VehicleTelemetryPolicy \
  --target <certificate-arn>
```

- **Rule Name**: `cms_{stage}_iot_msk_rule`
  **IoT Policy**:
  A simple IoT policy grants vehicles permission to connect and publish telemetry:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:Connect",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Publish",
      "Resource": "arn:aws:iot:us-east-1:123456789012:topic/fleet/*/vehicle/*/telemetry"
    }
  ]
}
```

This policy: \* Allows any vehicle with a valid certificate to connect \* Allows publishing to any telemetry topic matching the pattern \* No subscribe permissions (vehicles only publish, do not receive commands)

**VPC Destination**:

IoT Core connects to MSK in private subnets using a VPC destination:

- **VPC ID**: Same VPC as MSK cluster
- **Subnets**: Private subnets where MSK brokers are deployed
- **Security Groups**: MSK security group allowing port 9096 (SASL_SCRAM)
- **ENI Role**: IAM role for IoT Core to create network interfaces

**SCRAM Authentication**:

IoT Core authenticates to MSK using SCRAM credentials:

- **Secret Name**: `AmazonMSK_{cluster-name}_iot_user_credentials`
- **Secret Retrieval**: IoT Rules Engine uses `get_secret()` function to retrieve credentials at runtime
- **KMS Encryption**: Secret encrypted with customer-managed KMS key
- **IAM Permissions**: IoT role has `secretsmanager:GetSecretValue` and `kms:Decrypt` permissions

**Kafka Action Configuration**:

```
 {
  "kafka": {
    "destinationArn": "<vpc-destination-arn>",
    "topic": "cms-telemetry-raw",
    "clientProperties": {
      "bootstrap.servers": "b-1.cluster.kafka.us-east-1.amazonaws.com:9096,b-2.cluster.kafka.us-east-1.amazonaws.com:9096",
      "security.protocol": "SASL_SSL",
      "sasl.mechanism": "SCRAM-SHA-512",
      "sasl.scram.username": "${get_secret(...)}",
      "sasl.scram.password": "${get_secret(...)}"
    }
  }
}
```

**S3 Backup Action**:

All telemetry is also archived to S3 for compliance and analytics:

- **Bucket**: `cms-{stage}-telemetry-backup-{account-id}`
- **Key Pattern**: `raw-telemetry/year=YYYY/month=MM/day=DD/hour=HH/{clientId}-{timestamp}.json`
- **Partitioning**: Date-based partitioning enables efficient Athena queries
- **Lifecycle**: Optional lifecycle policies to transition to Glacier or delete old data

**IoT Lifecycle Tracking (Optional)**:

The guidance includes optional DynamoDB tables for tracking IoT connections and subscriptions:

- **iot-connections**: Track active vehicle connections (client_id, connect_time, disconnect_time)
- **iot-subscriptions**: Track topic subscriptions (client_id, topic_filter)
- **iot-topics**: Track message counts per topic (topic_name, message_count)
  These tables are populated by IoT lifecycle events but are not required for core telemetry processing.

**Scalability**:

- **Connection Limits**: 500,000+ concurrent connections per region (adjustable)
- **Message Throughput**: 1M+ messages per second per region
- **Topic Limits**: No limit on number of topics
- **Rule Execution**: Parallel execution scales automatically with message volume

**Cost Optimization with Basic Ingest**:

Using IoT Rules Engine with Basic Ingest eliminates per-message costs:

- **Standard IoT Core**: $1.00 per million messages
- **Basic Ingest**: $0.00 per million messages (only MSK costs)
- **Savings**: 100% reduction in IoT Core messaging costs

**Security Best Practices**:

- **Unique Certificates**: Each vehicle should have a unique certificate (never share)
- **Certificate Rotation**: Rotate certificates every 1-2 years
- **Secure Storage**: Store certificates in hardware security modules (HSM) or secure elements
- **Least Privilege Policies**: IoT policies grant only necessary permissions
- **Audit Logging**: CloudTrail logs all IoT Core operations

**Monitoring**:

- **CloudWatch Metrics**:
  **`PublishIn.Success`: Successful message publishes**
  `RuleMessageThrottled`: Messages throttled by rules engine
  **`RuleNotFound`: Messages sent to non-existent topics**
  `ParseError`: Malformed messages
- **CloudWatch Logs**:
  **`/aws/iot/rule/errors`: Failed rule executions**Error action logs authentication and connectivity issues

**Extensibility**:

While the current implementation is intentionally simple, it can be extended:

- **Bidirectional Communication**: Add subscribe permissions for vehicle commands
- **Fleet Provisioning**: Implement automated certificate generation workflows
- **Device Shadows**: Add virtual state representation for offline vehicles
- **Custom Authentication**: Integrate with custom authorizers for alternative auth methods
- **Edge Processing**: Deploy AWS IoT Greengrass for local processing
