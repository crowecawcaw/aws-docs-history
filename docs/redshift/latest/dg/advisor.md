Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Follow recommendations from Amazon Redshift Advisor

To help you improve the performance and decrease the operating costs for your Amazon Redshift
cluster, Amazon Redshift Advisor offers you specific recommendations about changes to make. Advisor
develops its customized recommendations by analyzing performance and usage metrics for your
cluster. These tailored recommendations relate to operations and cluster settings. To help
you prioritize your optimizations, Advisor ranks recommendations by order of impact.

Advisor bases its recommendations on observations regarding performance statistics or
operations data. Advisor develops observations by running tests on your clusters to
determine if a test value is within a specified range. If the test result is outside of
that range, Advisor generates an observation for your cluster. At the same time, Advisor
creates a recommendation about how to bring the observed value back into the best-practice
range. Advisor only displays recommendations that should have a significant impact on
performance and operations. When Advisor determines that a recommendation has been
addressed, it removes it from your recommendation list.

For example, suppose that your data warehouse contains a large number of uncompressed
table columns. In this case, you can save on cluster storage costs by rebuilding tables
using the `ENCODE` parameter to specify column compression. In another example,
suppose that Advisor observes that your cluster contains a significant amount of data in
uncompressed table data. In this case, it provides you with the SQL code block to find the
table columns that are candidates for compression and resources that describe how to
compress those columns.

## Amazon Redshift Regions where Advisor is supported

The Amazon Redshift Advisor feature is available only in the following AWS Regions:

- US East (N. Virginia) Region (us-east-1)
- US East (Ohio) Region (us-east-2)
- US West (N. California) Region (us-west-1)
- US West (Oregon) Region (us-west-2)
- Africa (Cape Town) Region (af-south-1)
- Asia Pacific (Hong Kong) Region (ap-east-1)
- Asia Pacific (Hyderabad) Region (ap-south-2)
- Asia Pacific (Jakarta) Region (ap-southeast-3)
- Asia Pacific (Melbourne) Region (ap-southeast-4)
- Asia Pacific (Malaysia) Region (ap-southeast-5)
- Asia Pacific (Mumbai) Region (ap-south-1)
- Asia Pacific (Osaka) Region (ap-northeast-3)
- Asia Pacific (Seoul) Region (ap-northeast-2)
- Asia Pacific (Singapore) Region (ap-southeast-1)
- Asia Pacific (Sydney) Region (ap-southeast-2)
- Asia Pacific (Tokyo) Region (ap-northeast-1)
- Canada (Central) Region (ca-central-1)
- Canada West (Calgary) Region (ca-west-1)
- China (Beijing) Region (cn-north-1)
- China (Ningxia) Region (cn-northwest-1)
- Europe (Frankfurt) Region (eu-central-1)
- Europe (Ireland) Region (eu-west-1)
- Europe (London) Region (eu-west-2)
- Europe (Milan) Region (eu-south-1)
- Europe (Paris) Region (eu-west-3)
- Europe (Spain) Region (eu-south-2)
- Europe (Stockholm) Region (eu-north-1)
- Europe (Zurich) Region (eu-central-2)
- Israel (Tel Aviv) Region (il-central-1)
- Middle East (Bahrain) Region (me-south-1)
- Middle East (UAE) Region (me-central-1)
- South America (São Paulo) Region (sa-east-1)

###### Topics

- [Viewing Amazon Redshift Advisor recommendations](access-advisor.md "access-advisor.md")
- [Amazon Redshift Advisor recommendations](advisor-recommendations.md "advisor-recommendations.md")
