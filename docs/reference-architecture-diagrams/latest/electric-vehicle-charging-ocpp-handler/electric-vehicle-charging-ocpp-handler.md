

# Electric Vehicle Charging OCPP Handler
<a name="electric-vehicle-charging-ocpp-handler"></a>

Publication date: **November 15, 2023 ([Diagram history](#diagram-history))**

This reference architecture demonstrates how to build a highly-scalable, low-latency electric vehicle (EV) charge point operator system based on the EV industry standard, Open Charge Point Protocol (OCPP), using AWS services like AWS IoT Core and AWS Lambda.

## Electric Vehicle Charging OCPP Handler Diagram
<a name="diagram1"></a>

![Reference architecture diagram demonstrating how to build a highly-scalable, low-latency electric vehicle (EV) charge point operator system based on the EV industry standard, Open Charge Point Protocol (OCPP), using AWS services like AWS IoT Core and AWS Lambda.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/electric-vehicle-charging-ocpp-handler/images/electric-vehicle-charging-ocpp-handler.png)


1.  An electric vehicle arrives to a charge point and connects to the charge cable. The customer swipes their RFID card to initiate charging. 

1.  The charge point performs a DNS lookup and receives a response from a record registered in **Amazon Route 53**. 

1.  The charge point connects to the resolved OCPP endpoint through a Network Load Balancer (NLB). 

1.  The NLB redirects the connection to a containerized instance of the OCPP Handler running on **AWS Fargate**. 

1.  The OCPP Handler application authenticates the charge point and establishes a bi-directional WebSockets connection to the charge point. 

1.  The OCPP Handler application established a bi-directional MQTT connection to **AWS IoT Core** using the charge point ID as its identifier. 

1.  OCPP messages received from the charge point are published to an MQTT topic identified by the charge point ID and the topic path `/in`. 

1.  An IoT rule subscribes to specific MQTT messages (such as Heartbeat) that are passed to and handled by an **AWS Lambda** function for auto-responses. 

1.  An IoT rule subscribes to all MQTT messages that include the topic path `/in` and forwards the message payload to an **Amazon Simple Queue Service** (Amazon SQS) queue. 

1.  An **AWS Step Functions** instance is initiated by the **Amazon SQS** queue and orchestrates the interpretation of the message payload and execution of the appropriate business logic based on the OCPP message payload. 

1.  OCPP messages sent from the Charging Station Management System (CSMS) to the charge point are published as a MQTT message to the topic using the charge point ID and the topic path `/out`. 

1.  The OCPP Handler application subscribes to all MQTT messages for the topic using the charge point ID and the topic path `/out`. The OCPP Handler forwards the OCPP response message over the WebSocket connection associated with the charge point ID. 

1.  The charge point receives the OCPP response and acts upon it. In this case, it initiates the delivery of power to the electric vehicle. 

1.  Telemetry and metrics from the charge point are added to the appropriate data stores. Analytics and visualizations can be performed against this data. 

1.  Charge point operator administrators can access a web-based user interface portal to monitor system help, view data, or initiate configuration and firmware changes. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [Blog: Building an OCPP-compliant electric vehicle charge point operator solution using AWS IoT Core](https://aws.amazon.com/blogs/iot/building-an-ocpp-compliant-electric-vehicle-charge-point-operator-solution-using-aws-iot-core/) 
+  [GitHub: Building an OCPP-Compliant electric vehicle charge point operator solution using AWS IoT Core](https://github.com/aws-samples/aws-ocpp-gateway) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 15, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.