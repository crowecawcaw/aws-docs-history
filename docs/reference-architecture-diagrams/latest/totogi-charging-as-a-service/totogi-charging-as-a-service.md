# Totogi Charging-as-a-Service for On-Premises 4G/5G

Publication date: **November 16, 2022 ([Diagram history](#totogi-history "#totogi-history"))**

With this architecture, you can connect your on-premises 4G/5G network to the
Totogi Charging-as-a-Service engine on AWS. Totogi is an
AWS-native multi-tenant 4G/5G charging engine and plan-design tool that enables telecom
operators to connect and monetize their core network. The solution uses [AWS Direct Connect](../../../directconnect/latest/UserGuide.md "../../../directconnect/latest/UserGuide.md"), [Amazon Elastic Compute Cloud](../../../AWSEC2/latest/UserGuide.md "../../../AWSEC2/latest/UserGuide.md") Auto Scaling, and [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide.md "../../../amazondynamodb/latest/developerguide.md").

## Totogi Charging-as-a-Service diagram

![Reference architecture diagram showing how to connect on-premises 4G/5G to Totogi charging on AWS by using AWS Direct Connect, Amazon EC2 Auto Scaling, DynamoDB, and Amazon Cognito.](images/totogi-charging-as-a-service.png)

The following steps describe the charging flow and network connectivity for this
architecture:

1. Connect 4G/5G network devices through the Radio Access Network (RAN) to the telco
   data center.
2. Register the subscriber through the core network control plane over the N2 interface
   for 5G and S1 for 4G subscribers.
3. Validate 4G/5G charging over N40 (5G REST) and Gy (4G Diameter)
   towards the multi-tenant Totogi charging engine on AWS.
4. Connect to AWS through AWS Direct Connect to [AWS Transit Gateway](../../../vpc/latest/tgw.md "../../../vpc/latest/tgw.md") in the Amazon VPC that hosts the
   tenant Totogi charging engine.
5. Deploy the Diameter adapter on Amazon EC2 Auto Scaling to transform
   requests and responses between 5G REST and 4G Diameter protocols.
6. Direct 5G REST requests to decision engines through the Network Load Balancer. Get the tenant ID from
   the [Amazon Cognito](../../../cognito/latest/developerguide.md "../../../cognito/latest/developerguide.md") access token.
7. Handle the rating request on the Amazon EC2 Auto Scaling instance decision engine. Look up
   balances and rating rules in DynamoDB. Partition data by tenant ID and subscriber
   ID.
8. Customize the handling of notifications and event detail records (EDRs) by using
   [Amazon EventBridge](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md") and [Amazon Simple Storage Service](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md") buckets.
9. Deliver quotas from the charging engine to validated subscribers for the user
   session.
10. Allow subscribers to access data and voice services over the customer network based on
    the provisioned plan and available credit in Totogi
    Charging-as-a-Service.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/")
- [AWS
  Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To receive updates about this reference architecture diagram, subscribe to the RSS
feed.

| Change              | Description                                     | Date              |
| ------------------- | ----------------------------------------------- | ----------------- |
| Initial publication | Reference architecture diagram first published. | November 16, 2022 |

###### RSS subscription requirement

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are
using.
