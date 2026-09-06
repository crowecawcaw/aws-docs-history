

# Specify a workgroup for queries
<a name="specify-wkgroup-to-athena-in-which-to-run-queries"></a>

To specify a workgroup to use, you must have permissions to the workgroup. 

**To specify the workgroup to use**

1. Make sure your permissions allow you to run queries in a workgroup that you intend to use. For more information, see [Use IAM policies to control workgroup access](workgroups-iam-policy.md).

1.  To specify the workgroup, use one of these options: 
   + If you are using the Athena console, set the workgroup by [switching workgroups](switching-workgroups.md).
   + If you are using the Athena API operations, specify the workgroup name in the API action. For example, you can set the workgroup name in [StartQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_StartQueryExecution.html), as follows: 

     ```
     StartQueryExecutionRequest startQueryExecutionRequest = new StartQueryExecutionRequest()
                   .withQueryString(ExampleConstants.ATHENA_SAMPLE_QUERY)
                   .withQueryExecutionContext(queryExecutionContext)
                   .withWorkGroup({{WorkgroupName}})
     ```
   + If you are using the JDBC or ODBC driver, set the workgroup name in the connection string using the `Workgroup` configuration parameter. The driver passes the workgroup name to Athena. Specify the workgroup parameter in the connection string as in the following example: 

     ```
     jdbc:awsathena://AwsRegion={{<AWSREGION>}};UID={{<ACCESSKEY>}};
     PWD={{<SECRETKEY>}};S3OutputLocation=s3://amzn-s3-demo-bucket/{{<athena-output>}}-{{<AWSREGION>}}/;
     Workgroup={{<WORKGROUPNAME>}};
     ```