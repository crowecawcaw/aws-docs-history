# Create an IAM Access Analyzer internal access

analyzer

To enable an internal access analyzer in a Region, you must create an analyzer in that
Region. You must create an internal access analyzer in each Region in which you want to
monitor access to your resources.

IAM Access Analyzer charges for internal access analysis based on the number of resources
monitored per analyzer per month. For more details about pricing, see [IAM Access Analyzer
pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

###### Note

After you create or update an analyzer, it can take time for findings to be
available.

IAM Access Analyzer cannot generate internal access findings for organizations that contain
more than 70,000 principals (IAM users and roles combined).

You can only create one organization-level internal access analyzer in an AWS
organization.

## Create an internal access

analyzer with the AWS account as the zone of trust

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Under **Access analyzer**, choose **Analyzer
   settings**.
3. Choose **Create analyzer**.
4. In the **Analysis** section, choose **Resource
   analysis - Internal access**.
5. In the **Analyzer details** section, confirm that the Region
   displayed is the Region where you want to enable IAM Access Analyzer.
6. Enter a name for the analyzer.
7. Choose **Current account** as the zone of trust for the
   analyzer.

###### Note

If your account is not the AWS Organizations management account or [delegated
administrator](access-analyzer-delegated-administrator.md "access-analyzer-delegated-administrator.md") account, you can create only one analyzer with your
account as the zone of trust. 8. In the **Resources to analyze** section, add resources for
the analyzer to monitor.

    * To add resources by account, choose **Add > Add resources from
     selected accounts**.




    	1. Choose **All supported resource types** or
    	 choose **Define specific resource types** and
    	 select the resource types from the **Resource
    	 type** list.


    	Internal access analyzers support the following resource
    	 types:




    		+ [Amazon Simple Storage Service buckets](access-analyzer-resources.md#access-analyzer-s3 "access-analyzer-resources.md#access-analyzer-s3")
    		+ [Amazon Simple Storage Service directory buckets](access-analyzer-resources.md#access-analyzer-s3-directory "access-analyzer-resources.md#access-analyzer-s3-directory")
    		+ [Amazon Relational Database Service DB snapshots](access-analyzer-resources.md#access-analyzer-rds-db "access-analyzer-resources.md#access-analyzer-rds-db")
    		+ [Amazon Relational Database Service DB cluster snapshots](access-analyzer-resources.md#access-analyzer-rds-db-cluster "access-analyzer-resources.md#access-analyzer-rds-db-cluster")
    		+ [Amazon DynamoDB streams](access-analyzer-resources.md#access-analyzer-ddb-stream "access-analyzer-resources.md#access-analyzer-ddb-stream")
    		+ [Amazon DynamoDB tables](access-analyzer-resources.md#access-analyzer-ddb-table "access-analyzer-resources.md#access-analyzer-ddb-table")
    	2. Choose **Add resources**.
    * To add resources by Amazon Resource Name (ARN), choose **Add
     resources > Add resources by pasting in resource
     ARN**.


    ###### Note

    ARNs must be exact matches – wildcards are not supported.
     For Amazon S3, only bucket ARNs are supported. Amazon S3 object ARNs and
     prefixes are not supported.




    	1. For each resource ARN, enter the account owner ID and the
    	 resource ARN separated by a comma. Enter one account owner ID
    	 and resource ARN per line.
    	2. Choose **Add resources**.
    * To add resources by a CSV file, choose **Add resources > Add
     resources by uploading a CSV**.


    You can use [AWS Resource Explorer](../../../resource-explorer/latest/userguide/using-search.md "../../../resource-explorer/latest/userguide/using-search.md") to search for resources in your accounts and
     export a CSV file. Then you can upload the CSV file to configure the
     resources for the analyzer to monitor.




    	1. Choose **Choose file** and select the CSV
    	 file from your computer.
    	2. Choose **Add resources**.

9. Optional. Add any tags that you want to apply to the analyzer.
10. Choose **Create analyzer**.

When you create an internal access analyzer to enable IAM Access Analyzer, a service-linked
role named `AWSServiceRoleForAccessAnalyzer` is created in your account.

## Create an internal access

analyzer with the organization as the zone of trust

1.  Open the IAM console at
    [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  Under **Access analyzer**, choose **Analyzer
    settings**.
3.  Choose **Create analyzer**.
4.  In the **Analysis** section, choose **Resource
    analysis - Internal access**.
5.  In the **Analyzer details** section, confirm that the Region
    displayed is the Region where you want to enable IAM Access Analyzer.
6.  Enter a name for the analyzer.
7.  Choose **Entire organization** as the zone of trust for the
    analyzer.
8.  In the **Resources to analyze** section, add resources for
    the analyzer to monitor.
    - To add resources for the account, choose **Add resources > Add
      resources from selected accounts**.
      1. Choose **All supported resource types** or
         choose **Define specific resource types** and
         select the resource types from the **Resource
         type** list.

      Internal access analyzers support the following resource
      types:

          + [Amazon Simple Storage Service buckets](access-analyzer-resources.md#access-analyzer-s3 "access-analyzer-resources.md#access-analyzer-s3")
          + [Amazon Simple Storage Service directory buckets](access-analyzer-resources.md#access-analyzer-s3-directory "access-analyzer-resources.md#access-analyzer-s3-directory")
          + [Amazon Relational Database Service DB snapshots](access-analyzer-resources.md#access-analyzer-rds-db "access-analyzer-resources.md#access-analyzer-rds-db")
          + [Amazon Relational Database Service DB cluster snapshots](access-analyzer-resources.md#access-analyzer-rds-db-cluster "access-analyzer-resources.md#access-analyzer-rds-db-cluster")
          + [Amazon DynamoDB streams](access-analyzer-resources.md#access-analyzer-ddb-stream "access-analyzer-resources.md#access-analyzer-ddb-stream")
          + [Amazon DynamoDB tables](access-analyzer-resources.md#access-analyzer-ddb-table "access-analyzer-resources.md#access-analyzer-ddb-table")

      2. To select accounts from your organization, choose
         **Select from organization**. In the
         **Select accounts** section, choose
         **Hierarchy** to select accounts by
         organizational structure or **List** to select
         accounts from a list of all accounts in your
         organization.

      To manually enter accounts from your organization, choose
      **Enter AWS account ID**. Enter one or
      more AWS account IDs separated by commas in the
      **AWS account ID** field. 3. Choose **Add resources**.

    - To add resources by Amazon Resource Name (ARN), choose **Add
      resources > Add resources by pasting in resource
      ARN**.

    ###### Note

    ARNs must be exact matches – wildcards are not supported.
    For Amazon S3, only bucket ARNs are supported. Amazon S3 object ARNs and
    prefixes are not supported.

        1. For each resource ARN, enter the account owner ID and the
         resource ARN separated by a comma. Enter one account owner ID
         and resource ARN per line.
        2. Choose **Add resources**.

    - To add resources by a CSV file, choose **Add resources > Add
      resources by uploading a CSV**.

    You can use [AWS Resource Explorer](../../../resource-explorer/latest/userguide/using-search.md "../../../resource-explorer/latest/userguide/using-search.md") to search for resources in your accounts and
    export a CSV file. Then you can upload the CSV file to configure the
    resources for the analyzer to monitor.

        1. Choose **Choose file** and select the CSV
         file from your computer.
        2. Choose **Add resources**.

9.  Optional. Add any tags that you want to apply to the analyzer.
10. Choose **Submit**.

When you create an internal access analyzer with the organization as the zone of
trust, a service-linked role named `AWSServiceRoleForAccessAnalyzer` is created in each account of
your organization.
