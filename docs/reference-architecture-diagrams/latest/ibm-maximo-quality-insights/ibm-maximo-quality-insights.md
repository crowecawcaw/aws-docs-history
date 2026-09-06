

# Computer Vision for Quality Insights with IBM Maximo on AWS
<a name="ibm-maximo-quality-insights"></a>

Publication date: **April 11, 2023 ([Diagram history](#imq-diagram-history))**

With this architecture, you can use IBM Maximo Visual Inspection (MVI) in a modernized AWS environment to detect and classify defects in manufacturing. Red Hat OpenShift on AWS, [Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/documentdb/latest/developerguide/), and AWS storage services provide a scalable, highly available environment. This architecture uses [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/), [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/), and [Amazon Elastic Block Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/).

## IBM Maximo quality insights architecture diagram
<a name="imq-diagram"></a>

![Architecture diagram for computer vision quality insights with IBM Maximo on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ibm-maximo-quality-insights/images/ibm-maximo-quality-insights-ra.png)


The following steps describe the architecture:

1. Ingest training datasets into the MVI training server on Red Hat OpenShift in your VPC. Use the MVI mobile app, MVI edge, or subject matter experts through a web app.

1. Subject matter experts annotate images and train models in the MVI training server.

1. Use MVI edge or the mobile app to create inspections and deploy models. Use Real Time Streaming Protocol (RTSP) for video data.

1. Operator workstations send messages to Message Queuing Telemetry Transport (MQTT) topics. MVI edge and mobile subscribe to and receive messages.

1. Take a photo and perform inference at the edge. Send images with inference results to MVI.

1. Route 53 provides DNS services. Network Load Balancers provide traffic to the OpenShift cluster.

1. Send alerts and inference results to an MQTT topic.

1. Plant managers and technicians review inference results in MVI edge UI, the mobile app, or the training server.

1. Red Hat OpenShift connects Amazon EFS as a network file system and uses Amazon EBS as block storage.

1. Maximo Application Suite (MAS) uses Amazon DocumentDB for the data dictionary and local user management.

## Further reading
<a name="imq-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="imq-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#imq-diagram-history) | Reference architecture diagram first published. | April 11, 2023 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.