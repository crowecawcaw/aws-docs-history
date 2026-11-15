

# Managed Service for Apache Flink and Studio notebook quota
<a name="limits"></a>

**Note**  
Apache Flink versions **1.6, 1.8, and 1.11** have not been supported by the Apache Flink community for over three years. We now plan to end support for these versions in Amazon Managed Service for Apache Flink. From **November 5, 2024**, you will not be able to create new applications for these Flink versions. You can continue running existing applications at this time.   
For all Regions with exception of the China Regions and the AWS GovCloud (US) Regions, from **February 5, 2025**, you will no longer be able to create, start, or run applications using these versions of Apache Flink in Amazon Managed Service for Apache Flink.   
For the China Regions and the AWS GovCloud (US) Regions, from **March 19, 2025**, you will no longer be able to create, start, or run applications using these versions of Apache Flink in Amazon Managed Service for Apache Flink.   
You can upgrade your applications statefully using the in-place version upgrades feature in Managed Service for Apache Flink. For more information, see [Use in-place version upgrades for Apache Flink](how-in-place-version-upgrades.md).

When working with Amazon Managed Service for Apache Flink, note the following quota:
+ You can create up to 100 Managed Service for Apache Flink applications per Region in your account. You can create a case to request additional applications via the service quota increase form. For more information, see the [AWS Support Center](https://console.aws.amazon.com/support/home#/).

  For a list of Regions that support Managed Service for Apache Flink, see [Managed Service for Apache Flink Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#ka_region).

   
+ The number of Kinesis processing units (KPU) is limited to 64 by default. For instructions on how to request an increase to this quota, see **To request a quota increase** in [Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html). Make sure you specify the application prefix to which the new KPU limit needs to be applied.

   

  With Managed Service for Apache Flink, your AWS account is charged for allocated resources, rather than resources that your application uses. You are charged an hourly rate based on the maximum number of KPUs that are used to run your stream-processing application. A single KPU provides you with 1 vCPU and 4 GiB of memory. For each KPU, the service also provisions 50 GiB of running application storage.

   
+ Managed Service for Apache Flink application snapshots (legacy) are subject to a quota. For more information, see [Manage application backups using snapshots](how-snapshots.md).

   
+ For enhanced snapshots, Managed Service for Apache Flink limits the [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html), [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html), and [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) operations that run at the same time:
  + Each application can have only one enhanced snapshot creation in progress at a time. The next `CreateSnapshot` request returns `ResourceInUseException`.
  + Your account can have up to 10 imports and exports combined in progress in each Region.
  + Each enhanced snapshot can have one export in progress at a time.

  An import or export request over a limit returns `LimitExceededException`. For more information, see [Limits on operations in progress](snapshots-how-it-works.md#snapshots-how-it-works-limits-on-operations-in-progress).

   
+ You can assign up to 50 tags per application.

   
+ You can assign up to 50 tags per enhanced snapshot.

   
+ The maximum size for an application JAR file is 512 MiB. If you exceed this quota, your application will fail to start.

   

For Studio notebooks, the following quotas apply. To request higher quotas, [create a support case](https://console.aws.amazon.com/support/home#/).
+ `websocketMessageSize` = 5 MiB
+ `noteSize` = 5 MiB
+ `noteCount` = 1000
+ `Max cumulative UDF size` = 100 MiB
+ `Max cumulative dependency jar size` = 300 MiB 