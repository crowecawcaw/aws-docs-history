Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Managed Service for Apache Flink and Studio notebook quota

###### Note

Apache Flink versions **1.6, 1.8, and 1.11** have not
been supported by the Apache Flink community for over three years. We now plan to end
support for these versions in Amazon Managed Service for Apache Flink. From **November 5,
2024**, you will not be able to create new applications for these Flink
versions. You can continue running existing applications at this time.

For all Regions with exception of the China Regions and the AWS GovCloud (US) Regions,
from **February 5, 2025**, you will no longer be able to
create, start, or run applications using these versions of Apache Flink in Amazon Managed Service for Apache Flink.

For the China Regions and the AWS GovCloud (US) Regions, from **March
19, 2025**, you will no longer be able to create, start, or run
applications using these versions of Apache Flink in Amazon Managed Service for Apache Flink.

You can upgrade your applications statefully using the in-place version upgrades
feature in Managed Service for Apache Flink. For more information, see [Use in-place version upgrades for Apache
Flink](how-in-place-version-upgrades.md "how-in-place-version-upgrades.md").

When working with Amazon Managed Service for Apache Flink, note the following quota:

- You can create up to 100 Managed Service for Apache Flink applications per Region in your account. You can
  create a case to request additional applications via the service quota increase
  form. For more information, see the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

For a list of Regions that support Managed Service for Apache Flink, see [Managed Service for Apache Flink Regions and
Endpoints](../../../general/latest/gr/rande.md#ka_region "../../../general/latest/gr/rande.md#ka_region").

- The number of Kinesis processing units (KPU) is limited to 64 by default. For
  instructions on how to request an increase to this quota, see **To request a quota increase** in [Service Quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md"). Make sure you specify the application prefix to which the new KPU limit needs to be applied.

 

With Managed Service for Apache Flink, your AWS account is charged for allocated resources, rather than
resources that your application uses. You are charged an hourly rate based on the
maximum number of KPUs that are used to run your stream-processing application. A
single KPU provides you with 1 vCPU and 4 GiB of memory. For each KPU, the service
also provisions 50 GiB of running application storage.

- You can create up to 1,000 Managed Service for Apache Flink snapshots per application. For more
  information, see [Manage application backups using
  snapshots](how-snapshots.md "how-snapshots.md").
- You can assign up to 50 tags per application.
- The maximum size for an application JAR file is 512 MiB. If you exceed this quota,
  your application will fail to start.
  For Studio notebooks, the following quotas apply. To request higher quotas, [create a support case](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

- `websocketMessageSize` = 5 MiB
- `noteSize` = 5 MiB
- `noteCount` = 1000
- `Max cumulative UDF size` = 100 MiB
- `Max cumulative dependency jar size` = 300 MiB
