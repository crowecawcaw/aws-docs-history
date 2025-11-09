# Electric Vehicle Charging OCPP Handler

Publication date: **November 15, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

This reference architecture demonstrates how to build a highly-scalable,
low-latency electric vehicle (EV) charge point operator system based on the
EV industry standard, Open Charge Point Protocol (OCPP), using AWS services
like AWS IoT Core and AWS Lambda.

## Electric Vehicle Charging OCPP Handler Diagram

![Reference architecture diagram demonstrating how to build a highly-scalable, low-latency electric vehicle (EV) charge point operator system based on the EV industry standard, Open Charge Point Protocol (OCPP), using AWS services like AWS IoT Core and AWS Lambda.](images/electric-vehicle-charging-ocpp-handler.png)

1. An electric vehicle arrives to a charge point and connects to the charge
   cable. The customer swipes their RFID card to initiate charging.
2. The charge point performs a DNS lookup and receives a response from a
   record registered in **Amazon Route 53**.
3. The charge point connects to the resolved OCPP endpoint through
   a Network Load Balancer (NLB).
4. The NLB redirects the connection to a containerized instance of
   the OCPP Handler running on **AWS Fargate**.
5. The OCPP Handler application authenticates the charge point and
   establishes a bi-directional WebSockets connection to the charge point.
6. The OCPP Handler application established a bi-directional MQTT connection
   to **AWS IoT Core** using the charge point ID as its identifier.
7. OCPP messages received from the charge point are published to an MQTT topic
   identified by the charge point ID and the topic path `/in`.
8. An IoT rule subscribes to specific MQTT messages (such as Heartbeat)
   that are passed to and handled by an **AWS Lambda**
   function for auto-responses.
9. An IoT rule subscribes to all MQTT messages that include the topic path
   `/in` and forwards the message payload to an **Amazon Simple Queue Service**
   (Amazon SQS) queue.
10. An **AWS Step Functions** instance is initiated by the **Amazon SQS**
    queue and orchestrates the interpretation of the message payload and execution of
    the appropriate business logic based on the OCPP message payload.
11. OCPP messages sent from the Charging Station Management System (CSMS) to the charge
    point are published as a MQTT message to the topic using the charge point ID and the
    topic path `/out`.
12. The OCPP Handler application subscribes to all MQTT messages for the topic using
    the charge point ID and the topic path `/out`. The OCPP Handler forwards
    the OCPP response message over the WebSocket connection associated with the
    charge point ID.
13. The charge point receives the OCPP response and acts upon it. In this case,
    it initiates the delivery of power to the electric vehicle.
14. Telemetry and metrics from the charge point are added to the appropriate data
    stores. Analytics and visualizations can be performed against this data.
15. Charge point operator administrators can access a web-based user interface
    portal to monitor system help, view data, or initiate configuration and firmware changes.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/electric-vehicle-charging-ocpp-handler.md "samples/electric-vehicle-charging-ocpp-handler.md") which contains an editable PowerPoint.

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
- [Blog: Building an OCPP-compliant electric vehicle charge point operator solution using AWS IoT Core](https://aws.amazon.com/blogs/iot/building-an-ocpp-compliant-electric-vehicle-charge-point-operator-solution-using-aws-iot-core/ "https://aws.amazon.com/blogs/iot/building-an-ocpp-compliant-electric-vehicle-charge-point-operator-solution-using-aws-iot-core/")
- [GitHub: Building an OCPP-Compliant electric vehicle charge point operator solution using AWS IoT Core](https://github.com/aws-samples/aws-ocpp-gateway "https://github.com/aws-samples/aws-ocpp-gateway")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date              |
| ------------------- | ----------------------------------------------- | ----------------- |
| Initial publication | Reference architecture diagram first published. | November 15, 2023 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
