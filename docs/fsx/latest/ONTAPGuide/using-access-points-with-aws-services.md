

# Using access points with AWS services
<a name="using-access-points-with-aws-services"></a>

You can use Amazon S3 access points attached to FSx for ONTAP volumes with AWS services that integrate with Amazon S3. This lets you analyze, process, and build Amazon S3-based applications on file data stored in FSx for ONTAP without copying it to an Amazon S3 bucket.

The following sample use cases walk through common integrations step by step. Each tutorial uses an Amazon S3 access point attached to an FSx for ONTAP volume so that AWS services can read and write your file data without having to copy and synchronize data to an Amazon S3 bucket.
+ **[Query files with SQL using Amazon Athena](tutorial-query-data-with-athena.md)** — Run ad-hoc SQL queries against files on your FSx for ONTAP volume using Amazon Athena and the AWS Glue Data Catalog. For data analysts who need SQL access to data that lands on an NFS or SMB file share.
+ **[Process files serverlessly using Lambda](tutorial-process-files-with-lambda.md)** — Trigger Lambda functions against files on your FSx for ONTAP volume to run serverless processing workloads. Examples include generating image thumbnails, extracting text from documents, and transcribing audio.
+ **[Build ETL pipelines using AWS Glue](tutorial-transform-data-with-glue.md)** — Read, transform, enrich, or partition data on your FSx for ONTAP volume using AWS Glue with Apache Spark, Python shell, or Ray, and write the results back to the same volume. For data engineering teams building curated datasets from files produced by legacy or on-premises systems.
+ **[Build a RAG application using Amazon Bedrock Knowledge Bases](tutorial-build-rag-with-bedrock.md)** — Build a retrieval-augmented generation (RAG) application that grounds foundation model responses in documents stored on your FSx for ONTAP volume. For teams building generative AI experiences over an existing document repository.
+ **[Run Spark jobs using Amazon EMR Serverless](tutorial-run-spark-with-emr-serverless.md)** — Run PySpark and Spark SQL workloads against files on your FSx for ONTAP volume without provisioning clusters. For data engineering teams running heavy Spark workloads that exceed the scope of AWS Glue.
+ **[Stream video using CloudFront](tutorial-stream-video-with-cloudfront.md)** — Deliver HLS adaptive-bitrate video from your FSx for ONTAP volume using CloudFront, with edge caching for performance. For media and entertainment teams whose production workflows write finished content to a file share.
+ **Transfer files using AWS Transfer Family** — Expose your FSx for ONTAP volume to external partners as an SFTP, FTPS, or FTP endpoint using AWS Transfer Family over an Amazon S3 access point. For setup instructions, see [Access your FSx for ONTAP file systems with Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/fsx-s3-access-points.html) in the *AWS Transfer Family User Guide*.

**Topics**
+ [Query files with SQL using Amazon Athena](tutorial-query-data-with-athena.md)
+ [Process files serverlessly using Lambda](tutorial-process-files-with-lambda.md)
+ [Build ETL pipelines using AWS Glue](tutorial-transform-data-with-glue.md)
+ [Build a RAG application using Amazon Bedrock Knowledge Bases](tutorial-build-rag-with-bedrock.md)
+ [Run Spark jobs using Amazon EMR Serverless](tutorial-run-spark-with-emr-serverless.md)
+ [Stream video using CloudFront](tutorial-stream-video-with-cloudfront.md)