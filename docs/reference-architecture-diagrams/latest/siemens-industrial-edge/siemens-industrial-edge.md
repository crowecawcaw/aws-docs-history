

# Siemens Industrial Edge on AWS
<a name="siemens-industrial-edge"></a>

Publication date: **May 13, 2024 ([Diagram history](#sie-diagram-history))**

With this architecture, you can integrate [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/) Edge on Siemens Industrial Edge for decentralized data acquisition, storage, analytics, AI, and connectivity to AWS. Siemens Industrial Edge is an open software platform for shop-floor IT. This architecture uses AWS IoT SiteWise, [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/), and Amazon Managed Grafana.

## Siemens Industrial Edge architecture diagram
<a name="sie-diagram"></a>

![Architecture diagram for integrating AWS IoT SiteWise Edge on Siemens Industrial Edge with AWS cloud services for industrial data and ML.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/siemens-industrial-edge/images/siemens-industrial-edge-on-aws-ra.png)


The following steps describe the architecture:

1. Siemens Industrial Edge is an open software platform for shop-floor IT. Industrial Edge Management allows remote and central management of edge devices and applications.

1. Southbound connector applications on Industrial Edge Devices collect data from industrial assets. You create apps through Mendix on Edge, Flow Creator, or Docker.

1. AWS IoT SiteWise Edge on Industrial Edge devices collects and aggregates data. It then sends this data to AWS IoT SiteWise in the AWS Cloud.

1. Use AWS IoT SiteWise Monitor, AWS IoT TwinMaker, or [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/) to visualize collected industrial data.

1. Use [Athena](https://docs.aws.amazon.com/athena/latest/ug/) to query cold IoT data from [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for analytics with Grafana, [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html), or Mendix apps.

1. Use AWS AI and ML services with data from Amazon S3 to train ML models. Combine with the Siemens AI SDK to package and deploy models back to the edge.

1. Siemens AI Model Manager deploys and manages ML models on the edge. AI Inference Server runs models. AI Model Monitor monitors them.

## Further reading
<a name="sie-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Siemens Teamcenter Product Lifecycle Management on AWS](../siemens-teamcenter-plm/siemens-teamcenter-plm.html)

## Diagram history
<a name="sie-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#sie-diagram-history) | Reference architecture diagram first published. | May 13, 2024 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.