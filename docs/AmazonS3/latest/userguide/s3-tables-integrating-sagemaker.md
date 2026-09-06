

# Getting started querying S3 Tables with Amazon SageMaker Unified Studio
<a name="s3-tables-integrating-sagemaker"></a>

Amazon SageMaker Unified Studio is a comprehensive analytics service that enables you to query and derive insights from your data using SQL, natural language, and interactive notebooks. It supports team collaboration and analysis workflows across AWS data repositories and third-party sources within a unified interface. SageMaker Unified Studio integrates directly with S3 Tables, providing a seamless transition from data storage to analysis within the Amazon S3 console.

You can integrate S3 Tables with SageMaker Unified Studio through the Amazon S3 console or SageMaker Unified Studio console.

For setup through the SageMaker Unified Studio console, see the [SageMaker Unified Studio documentation](https://docs.aws.amazon.com/next-generation-sagemaker/latest/userguide/s3-tables-integration.html).

## Requirements for querying S3 Tables with SageMaker Unified Studio
<a name="sagemaker-unified-studio-requirements"></a>

Using SageMaker Unified Studio with S3 Tables requires the following:
+ Your table buckets have been integrated with AWS analytics services in the current Region. For more information, see [Integrating S3 Tables with AWS analytics services](s3-tables-integrating-aws.md).
+ You are using an IAM role with permissions to create and view resources in SageMaker Unified Studio. For more information, see [Setup IAM-based domains in SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/setup-iam-based-domains.html).
+ You have a SageMaker domain and project. For more information, see [Domains](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/working-with-domains.html) in the *SageMaker Unified Studio Administrator Guide*, and [Projects](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/projects.html) in the *SageMaker Unified Studio User Guide*.

If you haven't already performed these actions or created these resources, S3 Tables can automatically complete this set up for you so you can begin querying with SageMaker Unified Studio.

## Getting started querying S3 Tables with SageMaker Unified Studio
<a name="sagemaker-unified-studio-getting-started"></a>

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Table buckets**.

1. On the **Table buckets** page, choose the bucket that contains the table that you want to query.

1. On the bucket details page, select the table that you want to query.

1. Choose **Query**. 

1. Then, choose **Query table in SageMaker Unified Studio**.

   1. If you've already configured SageMaker Unified Studio for your tables the SageMaker Unified Studio console opens to the query editor with a sample `SELECT` query loaded for you. Modify this query as needed for your use case.

   1. If you haven't already configured SageMaker Unified Studio for S3 Tables, a set up page appears with a single step to enable Integration with AWS analytics services which integrates your tables with services like SageMaker Unified Studio. This step will execute automatically then you will be redirected to a page in the SageMaker Unified Studio console with the following options to configure your account for querying S3 Tables:

      1. In **Setting you up as an administrator**, your current federated IAM role is selected. If your current role does not already have the required permissions, you will need to [setup an IAM-based domain in SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/setup-iam-based-domains.html) and assign permissions to your role so you can login to SageMaker Unified Studio.

      1. In **Project data and administrative control**, select **Auto-create a new role with required permissions** to automatically create a role with the required permissions, or select **Use an existing role** and choose a role. If the chosen role does not already have the required permissions, you will need to [setup an IAM-based domain in SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/setup-iam-based-domains.html) and assign permissions to your admin execution role so you can access data in SageMaker Unified Studio.

      1. In **Data encryption** select **Use AWS owned key** to let AWS own and manage a key for you or **Choose a different AWS AWS KMS key (advanced)** to use an existing key or to create a new one.

      1. Select **Set up SageMaker Unified Studio**.

      1. Next, the SageMaker Unified Studio console opens to the query editor with a sample `SELECT` query loaded for you. Modify this query as needed for your use case.

         In the query editor, the **Catalog** field should be populated with `s3tablescatalog/` followed by the name of your table bucket, for example, `s3tablescatalog/amzn-s3-demo-table-bucket`. The **Database** field is populated with the namespace where your table is stored.