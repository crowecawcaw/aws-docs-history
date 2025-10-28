# Use AMS SSP to provision Amazon MQ in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon MQ capabilities directly in your AMS managed account. Amazon MQ is a managed message broker service for Apache ActiveMQ that helps you to set up and operate message brokers in the cloud.
Message brokers allow different software systems, often using different programming languages and on different platforms, to communicate and
exchange information. Amazon MQ reduces your operational load by managing the provisioning, setup, and maintenance of ActiveMQ, a
popular open-source message broker. Connecting your current applications to Amazon MQ uses industry standard APIs and
protocols for messaging, including JMS, NMS, AMQP, STOMP, MQTT, and WebSocket. Using standards means that, in most cases,
there’s no need to rewrite any messaging code when you migrate to AWS. To learn more, see
[What Is Amazon MQ?](../../../amazon-mq/latest/developer-guide/welcome.md "../../../amazon-mq/latest/developer-guide/welcome.md")

## Amazon MQ in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon MQ in my AMS account?**

Utilization of Amazon MQ in your AMS account is a two-step process:

1. Provision the Amazon MQ Broker. To do this, submit a CFN Template, with the Amazon MQ
   Broker included, through an RFC with the Deployment | Ingestion | Stack from CloudFormation
   Template | Create change type (ct-36cn2avfrrj9v), or submit an RFC with the
   Management | Other | Other | Create change type (ct-1e1xtak34nx76)
   change type requesting that Amazon MQ Broker be provisioned in your account.
2. Access the Amazon MQ console. After the Amazon MQ Broker is provisioned, obtain access to the Amazon MQ
   console by submitting an RFC with the Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct). This
   RFC provisions the following IAM role to your account: `customer_mq_console_role`.

After the role is provisioned in your account, you must onboard it in your federation solution.

**Q: What are the restrictions to using Amazon MQ in my AMS account?**

Full functionality of Amazon MQ is available in your AMS account; however, provisioning Amazon MQ Broker is not available through the
policy due to the elevated permission required. See above for details on how to provision Amazon MQ broker in your accounts.

**Q: What are the prerequisites or dependencies to using Amazon MQ in my AMS account?**

There are no prerequisites or dependencies to use Amazon MQ in your AMS account.
