

# Aircraft Predictive Maintenance
<a name="aircraft-predictive-maintenance"></a>

Publication date: **March 10, 2021 ([Diagram history](#predictive-maintenance-history))**

Flight delays and cancellations caused by unscheduled maintenance cost airlines USD $120K to USD $300K per aircraft per year. This potentially translates to USD $60M to USD $150M annually for an airline with 500 aircraft.

Implementing predictive maintenance solutions that use aircraft log, sensor, and maintenance data can reduce this cost by up to 25 percent.

This architecture uses [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) to correlate aircraft fault data with maintenance history. The trained models predict component failures before they cause delays.

## Aircraft predictive maintenance diagram
<a name="predictive-maintenance-diagram"></a>

![Architecture for aircraft predictive maintenance using Amazon SageMaker AI on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/aircraft-predictive-maintenance/images/travel-ra-predictive-maintenance.png)


The following steps describe the architecture:

1. The Aircraft Communications Addressing and Reporting System (ACARS) collects fault logs and pilot reports in real time.

1. The Quick Access Recorder (QAR) collects and uploads data into AWS based on aircraft capability. Frequency varies based on the connectivity package installed.

1. Maintenance and engineering systems provide maintenance logs, part removals, and part repair history periodically.

1. The flight operations system provides scheduled and actual flight information. This correlates delays and cancellations with component failures.

1. You must delete identifying information from QAR data before use.

1. SageMaker AI trains the model to correlate delays and cancellations to fault logs, maintenance logs, part removals, and QAR data. Feature engineering identifies the most significant and predictable chapters and components.

1. Tune models periodically to improve predictions and reduce false positives.

## Further reading
<a name="predictive-maintenance-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="predictive-maintenance-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#predictive-maintenance-history) | Reference architecture diagram first published. | March 10, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.