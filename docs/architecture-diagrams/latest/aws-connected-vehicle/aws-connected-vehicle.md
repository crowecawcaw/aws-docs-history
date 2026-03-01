# AWS Connected Vehicle Reference Architecture

Publication date: **January 17, 2024 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture enables you to use AWS IoT Core to modernize workloads, process vehicle data, and secure your connected vehicles.

## AWS Connected Vehicle - Modernization Diagram

Use AWS IoT Core and MQTT5 to modernize your broker to gather, collect, and distribute data with your connected vehicle workloads.

![Reference architecture diagram showing how to use AWS IoT Core and MQTT5 to modernize your broker to gather, collect, and distribute data with your connected vehicle workloads.](images/1-modernization.png)

1. Embedded in-vehicle devices with a unique identity principal (X.509 certificate)
   publish telemetry data to **AWS IoT Core** by using MQTT. To minimize in-vehicle software,
   only libraries necessary to connect to AWS IoT Core are implemented. All traffic is
   sent over MQTT protocol secured using mTLS.
2. Use **AWS PrivateLink** and a private cellular network to connect your own
   **AWS IoT Core** endpoint to **AWS IoT Core**.
3. Shared subscriptions on **AWS IoT Core** help client workers process data payloads
   coming in from millions of vehicles by load balancing across topics. By implementing
   the topic alias feature, you can reduce payload size over the cellular connection,
   saving power consumption and cost.
4. Use **Amazon Elastic Container Service** (Amazon ECS) to decode, process, and persist
   the telemetry data. **Amazon ECS** supports the scalability necessary to handle the
   messages at peak demand and not run into concurrency bottlenecks.
5. Using a specialized message header, **AWS IoT Core** routes encoded messages to their
   destination. For compressed payloads, the routing mechanism is placed in the payload
   header, routing without human readable format to send messages downstream. The
   descriptor file is stored in **Amazon Simple Storage Service** (Amazon S3) to inform
   the rule how to decode the payload.
6. The request/response messaging pattern in **AWS IoT Core** tracks
   responses to client requests in an asynchronous way. The customer submits a remote command
   to their vehicle using an interface built by **AWS Amplify**
   through **Amazon API Gateway**. The command is persisted to
   **Amazon DynamoDB** and delivered as a request to the device
   by using a request IoT topic. After implementation, the vehicle responds on the
   response IoT Topic to report success or failure. This same pattern can be used
   for vehicle-to-cloud to report state.
7. For the same remote command, using the Message Expiry feature of AWS IoT Core,
   you can specify how long to attempt to unlock a vehicle door, before expiring
   the message. This allows for much more flexible control of devices.
8. Critical system messages sent from the original equipment manufacturer (OEM)
   to the vehicle can use the **AWS IoT Core** Retained Messages function. The OEM can
   set a retained message flag on the payload to ensure the command is in the
   topic when the vehicle comes back online.

## AWS Connected Vehicle - Gather, Process, Analyze Diagram

Gather, process, analyze, and act on connected vehicle data using AWS IoT Core.

![Reference architecture diagram showing how to gather, process, analyze, and act on connected vehicle data using AWS IoT Core.](images/2-gather-process-analyze-data.png)

1. The connected vehicle, acting as an IoT device, with a unique identity principal (X.509 certificate),
   uses sensors to collect, analyze and act upon data using **AWS IoT Core**
   as an edge-to-cloud communication mechanism.
2. The **AWS IoT FleetWise** Edge Agent communicates with the vehicle’s network,
   decoding signals and sending data payloads through **AWS IoT Core**
   as defined by data campaigns. With **AWS IoT FleetWise**, you control
   every step of the process and maintain full data ownership and control of proprietary
   information.
3. Use **AWS IoT Core** together with **Amazon Route 53** to
   choose an AWS Region based on geo location or latency. Register your devices automatically
   when they connect for the first time to **AWS IoT Core**. The DNS
   lookup returns an IoT endpoint from one of many Regions depending on device location.
4. **AWS IoT** supports client certificates signed by any root or
   intermediate certificate authorities (CA) that are registered with **AWS IoT Core**.
   Upon connecting with the private certificate, the **AWS Lambda** function
   validates the Gateway and creates the IoT thing, policy, and certificate. The vehicle is registered.
5. **AWS IoT FleetWise** helps you more intelligently collect vehicle data. You
   can improve data relevance by creating time and event-based data collection campaigns that
   send the exact data you need to the cloud to **Amazon Timestream** or
   **Amazon S3**.
6. Use **Amazon SageMaker AI** to improve ADAS/AV models and optimize
   vehicle design for performance and efficiency. Use **Amazon Quick**
   to continually improve vehicle quality, safety, and autonomy using near real-time
   data from **AWS IoT FleetWise**.
7. Using **AWS IoT Core Device Shadow** can make a vehicle’s
   state available to apps and other downstream services whether the device is connected
   to **AWS IoT Core** or not, providing a built-in
   mechanism to update the vehicle's state from the cloud.
8. Use **AWS IoT Device Management** to implement over-the-air (OTA)
   management through IoT jobs and use **AWS IoT** fleet
   indexing to manage state, connectivity, and device violations and to organize,
   investigate, and troubleshoot your fleet of devices.
9. Use the power of **AWS IoT Core** integrations with
   downstream services to enable use cases to empower your different user
   personas from fleet aggregators to data scientists and vehicle owners.

## AWS Connected Vehicle - Operational Certificate Lifecycle Diagram

Secure your connected vehicles with provisioning, OCSP, and certificate rotation.

![Reference architecture diagram showing how to secure your connected vehicles with provisioning, OCSP, and certificate rotation.](images/3-operational-certificate-lifecycle.png)

1. A subordinate CA is created in **AWS Private Certificate Authority** (AWS Private CA) with
   a CA certificate signed by the offline root CA. The subordinate CA certificate is
   registered with **AWS IoT Core**.
2. The electronic control unit (ECU) generates a private key and certificate signing
   request (CSR) and uses its existing attestation certificate to authenticate to the
   certificate broker. The certificate broker issues the operational certificate by
   calling **AWS Private CA**. The broker sends the
   signed operational certificate to the ECU.
3. The ECU uses TLS with the operational certificate to connect to **AWS IoT Core**,
   which validates the client certificate was signed by the registered CA certificate
   and that the certificate is not expired. Because this is the first use of the
   certification, it is not registered with **AWS IoT Core**;
   **AWS IoT Core** creates a pending activation
   certificate and the ECU is disconnected. **AWS IoT Core**
   publishes a message to a reserved MQTT topic.
4. An IoT rule on the reserved MQTT topic invokes the **Lambda**
   registration function. The function implements custom logic like generating
   an **AWS IoT Core** policy specific to the ECU using
   information from a **DynamoDB** table, and custom
   authentication such as checking the certificate against the Online Certificate
   Status Protocol (OCSP) responder provided by **AWS Private CA**.
5. The function then creates an IoT thing and policy, and changes the certificate
   status to active. The ECU can retry the connection and communicate to topics
   in **AWS IoT Core**.
6. **AWS IoT Device Defender** publishes audit findings
   such as certificate expiring and certificate revoked to **AWS Security Hub CSPM**.
   **Security Hub CSPM** sends events to **Amazon EventBridge**,
   which initiates targets such as an **AWS Step Functions** workflow
   to rotate the certificate. **EventBridge** can also send audit
   findings to your vehicle security operations center.
7. The workflow orchestrates **Lambda** functions that
   use IoT jobs to push the ECU to generate a new CSR and send it to a topic. Upon
   receiving the CSR, it issues a new operational certificate by
   calling **AWS Private CA** to sign the certificate, registers
   the certificate in **AWS IoT Core** with a policy,
   and sends the certificate to the ECU. Once the ECU has successfully installed
   and tested the new operational certificate, the workflow revokes the old certificate.
8. You can invoke the **AWS Private CA** APIs to revoke a certificate
   and update the certificate status in **AWS IoT Core**.

## AWS Connected Vehicle - Encryption and Monitoring Security Diagram

Secure your connected vehicles with AWS encryption and monitoring services.

![Reference architecture diagram showing how to secure your connected vehicles with AWS encryption and monitoring services.](images/4-encryption-and-monitoring-security.png)

1. An ECU with a unique identity principal (X.509 operational certificate) publishes
   telemetry by using MQTT to **AWS IoT Core**. The ECU can
   either run a generic HTTP or MQTT stack or accelerate development using the
   **AWS IoT** Device SDK.
2. During the TLS handshake, **AWS IoT Core** validates
   the client certificate expiry, and checks that the certificate is registered
   and active. **AWS IoT Core** retrieves policies
   attached to both the certificate and thing groups for the thing attached to
   the certificate in order to authorize operations performed by the ECU.
3. **AWS Key Management Service** (AWS KMS) lets you create, manage,
   and control cryptographic keys across your applications and AWS services.
   Encryption at rest on the server side is available for all the services
   in the diagram.
4. You can choose to encrypt highly sensitive payload data on the client side before
   sending it to **AWS IoT Core** in addition to
   encryption-in-transit using mTLS. The vehicle can use the AWS encryption SDK
   using keys in **AWS KMS** for client-side encryption.
   The ECU can get temporary API credentials from the IoT credential provider to
   call **AWS KMS** APIs. You can also implement your
   own key management system for encryption keys.
5. Sensitive payload data flows through intermediate systems as opaque ciphertext
   until it arrives at a **Lambda** function that
   has an execution role with permissions to invoke **AWS KMS**.
   The **Lambda** function code uses the AWS encryption
   SDK to decrypt the data key and decrypt the sensitive data.
6. Authenticated users can send authenticated and authorized remote commands to
   applications by using **Amazon API Gateway**. The
   request **Lambda** function with execution role
   permissions can use the AWS encryption SDK using keys in **AWS KMS**
   to encrypt client-side command payloads before sending to the ECU.
7. **AWS IoT Device Defender** monitors devices connected
   to **AWS IoT Core** to detect abnormal behavior using
   rules and by building machine learning (ML) models. **AWS IoT Device Defender**
   can generate a finding when it detects abnormal rates of authorization
   failures (cloud-side metric) or anomalous traffic flow (device-side metrics)
   for an ECU.
8. **AWS IoT Device Defender** sends findings to **AWS Security Hub CSPM**
   where security findings from other AWS services and partner products are
   aggregated and normalized. **Security Hub CSPM** sends findings
   to **EventBridge**, which routes them to a remediation
   workflow implemented using **Step Functions**. You can
   also send findings to your vehicle security operations center.
9. The **Step Functions** remediation workflow can orchestrate
   steps such as modifying the IoT policy for the certificate and changing the
   certificate status to INACTIVE to disconnect the ECU.

## AWS Connected Vehicle - Companion Application

Build a connected vehicle companion application to control your vehicle with AWS IoT Core and AWS AppSync.

![Reference architecture diagram showing how to secure your connected vehicles with AWS encryption and monitoring services.](images/5-companion-application.png)

1. The vehicle establishes an MQTT connection to the **AWS IoT Core** endpoint, and
   then subscribes to the control plane request topics to receive any cloud-side request commands. The
   vehicle also will publish automatically to the **AWS IoT** lifecycle events topic,
   indicating that connectivity is established.
2. The upon connection, **AWS IoT Core** publishes the vehicle’s connected state
   to the lifecycle events topic `$aws/events/subscriptions/subscribed/vehicleId`. This reserved
   topic is where connection events are published automatically upon connection.
3. When a disconnect message is received, your code should wait a period of time and verify the vehicle
   is still offline before taking action. When the topic receives a lifecycle event, you can
   enqueue a message using **Amazon Simple Queue Service** (Amazon SQS) delay queues; when
   that message becomes available and is processed by an **AWS Lambda** function,
   you can first check if the vehicle is still offline before taking further action.
4. The connected state is then sent as a mutation to **AWS AppSync**, which uses a
   custom resolver to persist the state to an **Amazon DynamoDB** table. This
   connected state is then used for logic when a remote command is sent from a companion application.
5. Using **AWS Amplify** managed native applications and web
   applications, a remote command is sent by a secure WebSocket as a mutation to **AWS AppSync**.
   That mutation is persisted to **DynamoDB** and a subscription is then processed
   by **Lambda**.
6. The vehicle state **Lambda** then checks the connected state.
   - If connected, **Lambda** publishes the command payload to the request topic with a
     unique `requestId` and a response topic in the header.
   - If the device is in a disconnected state, the vehicle state **Lambda** then
     sends a command to **Amazon Simple Notification Service** (Amazon SNS), which will send an SMS to
     the dialable MSISDN on the SIM on the TCU to indicate that a command is waiting and to wake
     up and subscribe to command topics.

7. Upon receipt of the command payload in the request topic, the logic is managed by a client application
   on the device and the result is published back to the response topic as success or failure. The
   response payload is then sent to an **Amazon SQS** first-in first-out (FIFO)
   queue for downstream processing by the vehicle state **Lambda** to ensure the
   messages are properly batched prior to processing.
8. The response is then processed by **AWS AppSync** as a mutation and persisted to
   **DynamoDB**. **AWS AppSync** then implements fan-out
   mechanism alerting the companion applications and vehicle management platforms with the updated vehicle
   state.
9. Optimize distribution of your companion applications placing your static assets in
   **Amazon Simple Storage Service** (Amazon S3) and use **Amazon CloudFront** for distribution.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/aws-connected-vehicle.md "samples/aws-connected-vehicle.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Contributors

Contributors to this reference architecture diagram include:

- Andrew Givens, Senior Partner Solutions Architect, AWS
- Omar Zoma, Senior Security Solutions Architect, AWS
- Maitreya Ranganath, Principal Security Solutions Architect, AWS
- Katja-Maja Kroedel, Senior IoT Specialist Solutions Architect, AWS

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                                                    | Date             |
| ------------------- | ------------------------------------------------------------------------------ | ---------------- |
| Diagram updated     | Minor updates to initial diagrams, added \*Companion Application<br>• diagram. | January 17, 2024 |
| Initial publication | Reference architecture diagram first published.                                | June 23, 2023    |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
