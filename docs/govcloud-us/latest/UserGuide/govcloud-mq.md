

# Amazon MQ in AWS GovCloud (US)
<a name="govcloud-mq"></a>

 Amazon MQ is a managed message broker service that makes it easy to migrate to a message broker in the cloud. A *message broker* allows software applications and components to communicate using various programming languages, operating systems, and formal messaging protocols. Currently, Amazon MQ supports [Apache ActiveMQ](http://activemq.apache.org/) and [RabbitMQ](https://www.rabbitmq.com/) engine types.

 Amazon MQ works with your existing applications and services without the need to manage, operate, or maintain your own messaging system.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon MQ differs
<a name="govcloud-mq-diffs"></a>

The following differences apply to Amazon MQ:
+ The AWS Free Tier is not available in GovCloud, meaning users cannot access the free resources offered in commercial Regions.
+  Amazon MQ in GovCloud Regions does not support cross-Region data replication.
+ The instance types supported by Amazon MQ in GovCloud differ from those in commercial Regions. Users should consult the Amazon MQ pricing page for the specific instance types available in their Region.
+  Amazon MQ does not support CRDR in AWS GovCloud (US) regions.

## Documentation
<a name="govcloud-mq-docs"></a>
+  [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq) 

## Export-controlled content
<a name="govcloud-mq-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon MQ metadata is not permitted to contain export-controlled data. For example, do not enter export-controlled data into user input fields such as the following:
  + Broker name
  + Configuration name
  + Resource tag/key value pairs