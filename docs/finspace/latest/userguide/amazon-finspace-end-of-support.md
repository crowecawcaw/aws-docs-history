After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Amazon FinSpace end of support

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal, including creating new resources and onboarding new accounts. Additionally, AWS will continue to provide critical security and availability updates to Amazon FinSpace during this period. After October 7, 2026, you will no longer be able to access the Amazon FinSpace Dataset Browser or Amazon FinSpace Managed kdb Insights features.

This topic provides instructions and best practices to transition your usage of Amazon FinSpace Dataset Browser and Amazon FinSpace Managed kdb Insights to other options on AWS.

## Amazon FinSpace Dataset Browser

Existing Dataset Browser customers can now use
for their business data catalog needs, for
Apache Spark for their data processing, and SageMaker AI Studio for their notebooks.
If you are currently using Dataset Browser and need help with migration, contact
[AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") for assistance with migration
options. For other question related to Dataset Browser end of life, you can review
the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or reach out to
[AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

## Amazon FinSpace Managed kdb Insights

To migrate your kdb Insights application to self-managed on AWS, you need to first extract the database contents and the application code to an Amazon S3 location on AWS. Then you will need to setup kdb on AWS, using your choice of compute and storage options. Finally, you will import the contents of your kdb database files.

1. **Export Database Contents**

To extract your data from Amazon FinSpace, you can leverage python, along with kdb's pyKX feature, to connect to your Amazon FinSpace HDBs and then extract database table contents, store in CSV format, and then import into your new self-managed kdb Insights environment.

Please see this re:Post article for details: [Extract and Save Data from FinSpace with Managed kdb Insights](https://repost.aws/articles/ARhGEL13bTQh-CxbZqc6O0Ng/extract-and-save-data-from-finspace-with-managed-kdb-insights "https://repost.aws/articles/ARhGEL13bTQh-CxbZqc6O0Ng/extract-and-save-data-from-finspace-with-managed-kdb-insights"). 2. **Setup new kdb application on AWS**

AWS continues to provide a broadest set of infrastructure resources to build and operate your kdb applications. There are many different architectures and services you can leverage to meet your cost, performance, and integration needs. In addition, we have a broad number of technical people with kdb experience who can help you. For assistance with making these architecture decisions, please reach out to your AWS technical account team and they can work with you.
