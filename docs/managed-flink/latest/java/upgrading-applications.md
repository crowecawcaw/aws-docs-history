Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Upgrade applications using in-place version

upgrades for Apache Flink

Before you begin, we recommend that you watch this video: [In-Place Version
Upgrades](https://www.youtube.com/watch?v=f1qGGdaP2XI "https://www.youtube.com/watch?v=f1qGGdaP2XI").

To perform in-place version upgrades for Apache Flink, you can use the AWS CLI,
AWS CloudFormation, AWS SDK, or the AWS Management Console. You can use this feature with any existing
applications that you use with Managed Service for Apache Flink in a `READY` or
`RUNNING` state. It uses the UpdateApplication API to add the ability to
change the Flink runtime.

## Before upgrading: Update your Apache Flink

application

When you write your Flink applications, you bundle them with their dependencies
into an application JAR and upload the JAR to your Amazon S3 bucket. From there,
Amazon Managed Service for Apache Flink runs the job in the new Flink runtime that you've selected. You might have
to update your applications to achieve compatibility with the Flink runtime you want
to upgrade to. There can be inconsistencies between Flink versions that cause the
version upgrade to fail. Most commonly, this will be with connectors for sources
(ingress) or destinations (sinks, egress) and Scala dependencies. Flink 1.15 and
later versions in Managed Service for Apache Flink are Scala-agnostic, and your JAR must contain the
version of Scala you plan to use.

**To update your application**

1. Read the advice from the Flink community on upgrading applications with
   state. See [Upgrading Applications and Flink Versions](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/upgrading/ "https://nightlies.apache.org/flink/flink-docs-master/docs/ops/upgrading/").
2. Read the list of knowing issues and limitations. See [Precautions and known issues with application
   upgrades](precautions.md "precautions.md").
3. Update your dependencies and test your applications locally. These
   dependencies typically are:
   1. The Flink runtime and API.
   2. Connectors recommended for the new Flink runtime. You can find
      these on [Release versions](release-version-list.md "release-version-list.md") for the specific runtime you want to
      update to.
   3. Scala – Apache Flink is Scala-agnostic starting with and including
      Flink 1.15. You must include the Scala dependencies you want to use
      in your application JAR.

4. Build a new application JAR on zipfile and upload it to Amazon S3. We recommend
   that you use a different name from the previous JAR/zipfile. If you need to
   roll back, you will use this information.
5. If you are running stateful applications, we strongly recommend that you
   take a snapshot of your current application. This lets you roll back
   statefully if you encounter issues during or after the upgrade.
