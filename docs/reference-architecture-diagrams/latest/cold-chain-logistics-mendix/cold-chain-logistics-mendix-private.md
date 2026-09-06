

# Cold Chain Logistics Powered by Mendix: Private Cloud
<a name="cold-chain-logistics-mendix-private"></a>

Publication date: **April 29, 2022 ([Diagram history](#ccm-private-history))**

With this architecture, you can deploy Mendix cold chain logistics applications on your own [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) cluster. Mendix for Private Cloud supports the full application lifecycle on Kubernetes. Simplify lifecycle management with the Mendix Operator and connect securely with the Mendix Gateway.

## Cold chain logistics Mendix Private Cloud diagram
<a name="ccm-private-diagram"></a>

![Reference architecture diagram showing cold chain logistics on Mendix for Private Cloud by using Amazon EKS, AWS IoT Core, and Amazon Rekognition.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/cold-chain-logistics-mendix/images/cold-chain-logistics-mendix-private.png)


The following steps describe the private cloud deployment for this architecture:

1. Publish telemetry messages from IoT sensors to [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/). Process messages according to custom rules and forward them into the backend.

1. Feed information from external systems into the [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) data lake.

1. Use Mendix IoT connectors to publish or subscribe to devices by using the MQTT protocol. Control actuators by updating device shadows.

1. Register your private Amazon EKS cluster in the Mendix private cloud portal. Deploy apps to the cluster by using the Mendix Operator.

1. Incorporate external databases directly in your app by using a JDBC driver with the Mendix database connector.

1. Upload, modify, and delete files by using the Mendix Amazon S3 connector. Back up data for long-term storage.

1. Analyze images by using the [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/) connector microflows.

1. Explore topics and publish messages by using the Mendix [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) connector.

1. Access backend services through [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) with Signature V4 authentication.

1. Retrieve and analyze data by using standard SQL with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/).

1. Store time-series data in [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/). Query records by using the JDBC database connector.

## Further reading
<a name="ccm-private-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="ccm-private-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](cold-chain-logistics-mendix-cloud.md#ccm-cloud-history) | Reference architecture diagram first published. | April 29, 2022 | 
| [Initial publication](#ccm-private-history) | Reference architecture diagram first published. | April 29, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.