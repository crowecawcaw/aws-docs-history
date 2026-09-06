

# Smart Metering for Water Utilities
<a name="smart-metering-for-water-utilities"></a>

Publication date: **March 16, 2022 ([Diagram history](#diagram-history))**

This architecture shows how AWS IoT Core for [LoRaWAN](https://lora-alliance.org/about-lorawan/) can be used to reliably collect water meter readings from multiple metering devices. Transfer the data to the cloud, detect water leakage in the grid, and gain deeper insights on water consumption, while monitoring and managing the fleet of meters. 

## Smart Metering for Water Utilities
<a name="diagram1"></a>

![Reference architecture diagram showing how AWS IoT Core for LoRaWAN can be used to reliably collect water meter readings from multiple metering devices. Transfer the data to the cloud, detect water leakage in the grid, and gain deeper insights on water consumption, while monitoring and managing the fleet of meters.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/smart-metering-for-water-utilities/images/smart-metering-water-utilities.png)


1. The purpose-built devices in the meter box use **FreeRTOS **as their operating system (OS). The meter collects water consumption, the valve interrupts water flow, both devices communicate via BLE with the hub, which uses the LoRaWAN protocol to send telemetry to the cloud. The hub runs in Class B mode, which enables it to receive commands from the gateway in defined timeframes. 

1. In-home displays or mobile apps are used to perform a local update process, connection is established via BLE. 

1. The LoRa gateway receives the meter data from the hub and forwards them to the **AWS IoT Core for LoRaWAN** service. The CUPS protocol is used to keep compatible gateways up-to-date. 

1. **AWS IoT Core for LoRaWAN** sends the payload to the Rules Engine (through a LoRaWAN destination) where an **AWS Lambda** function decodes the binary device payload before data can be further processed. 

1. **Amazon CloudWatch** monitors the state of your gateways and devices. **AWS IoT Events** tracks message deliveries to detect whether devices are still sending meter readings. 

1. Management Services is a custom-built layer to manage devices and schedule downlink messages. 

1. The data storage layer stores the meter readings on **Amazon S3** or in a purpose-built data store such as **Amazon Timestream**. 

1. The backend services use the incoming meter readings to generate further insights. 

1. **Amazon Managed Service for Grafana** is used for creating dashboards, while **AWS Amplify** and **Amazon API Gateway** enable access for third parties. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [IoT Lens Checklist — AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens-checklist/overview.html) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.