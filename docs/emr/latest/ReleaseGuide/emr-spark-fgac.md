

# Fine-grained access control with Lake Formation

Lake Formation fine-grained access control (FGAC) lets Spark jobs read tables that have row-level, column-level, and cell-level permissions. Spark shows each job only the rows and columns that the job runtime role can access. The same Spark engine applies these permissions on every supported platform. The setup steps are different on each platform.

## How fine-grained access control works in Spark
<a name="emr-spark-fgac-how-it-works"></a>

When a job uses fine-grained access control, Spark runs your job in two separate parts. Each part has its own driver and executors.
+ **User space** runs your job script and your UDFs. When a Lake Formation policy or view calls a governed UDF, the UDF runs in system space. User space sees only the data that Lake Formation lets the runtime role see. A governed UDF that your query calls sees filtered data. A governed UDF that a Lake Formation policy or view calls sees unfiltered data.
+ **System space** is trusted. On EMR Serverless and AWS Glue, AWS manages it. On Amazon EMR on EC2 and Amazon EMR on EKS, the cluster administrator also manages the cluster. Thus, the data administrator must also trust the cluster administrator. System space reads the table data from Amazon S3. System space always applies the Lake Formation row, column, and cell filters. Then it sends only the filtered data to user space.

Because of this split, system space accepts only the Spark properties and classes that it knows are safe. If your job sets a Spark property that system space does not accept, system space ignores the property. Code that system space must run, for example a function that a row filter calls, must come from a source that Lake Formation governs. For more information, see [Using governed UDFs with Lake Formation fine-grained access control](emr-spark-fgac-governed-udfs.md).

With full table access (FTA), a job reads and writes only tables on which its role has full access. These tables have no row, column, or cell filters. FTA also supports DML on those tables. For more information, see the page for your platform:
+ [Lake Formation full table access for EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/lake-formation-unfiltered-access.html) in the *EMR Serverless User Guide*
+ [Lake Formation full table access for Amazon EMR on EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/lake-formation-unfiltered-ec2-access.html) in the *Amazon EMR Management Guide*
+ [Using AWS Glue with Lake Formation for Full Table Access](https://docs.aws.amazon.com/glue/latest/dg/security-access-control-fta.html) in the *AWS Glue Developer Guide*

## Supported platforms and setup pages
<a name="emr-spark-fgac-platforms"></a>

To set up fine-grained access control, use the page for your platform.


**Fine-grained access control setup by platform**  

| Platform | Setup page | 
| --- | --- | 
| Amazon EMR on EC2 | [Integrate Amazon EMR with Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lake-formation.html) in the Amazon EMR Management Guide | 
| EMR Serverless | [Using Lake Formation with EMR Serverless for fine-grained access control](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable.html) in the EMR Serverless User Guide | 
| Amazon EMR on EKS | [Using Lake Formation with Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_fgac-lf.html) in the Amazon EMR on EKS Development Guide | 
| AWS Glue ETL | [Using AWS Glue with Lake Formation for fine-grained access control](https://docs.aws.amazon.com/glue/latest/dg/security-lf-enable.html) in the AWS Glue Developer Guide | 