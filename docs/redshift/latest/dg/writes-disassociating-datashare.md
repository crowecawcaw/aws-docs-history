Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Removing association of a

datashare from data consumers in a different AWS account in Amazon Redshift

With Amazon Redshift, you can remove association from datashares shared by other
AWS accounts. Datashares are shareable database objects that encapsulate data
from one or more Redshift databases. The following sections demonstrate the
process of disassociating datashares within your Redshift environment.

Console
As a consumer administrator, you can remove association of datashares
from data consumers on the console.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Datashares**.
   The datashare list page appears.
3. Choose **From other accounts**.
4. In the **Datashares from other accounts**
   section, choose the datashare to remove association from data
   consumers.
5. In the **Data consumers** section, choose one
   or more data consumers to remove association from. Then choose
   **Remove association**.
6. When the Remove association page appears, choose
   **Remove association**.

After association is removed, data consumers will lose access to the
datashare. You can change the data consumer association at any
time.

SQL

###### Note

The steps in this section are performed after the producer
administrator grants specific actions on the shared database objects
and, if the datashare is being shared with another account, the
producer security administrator authorizes access.

The consumer security administrator can disassociate the datashare
with the following command:

```
disassociate-data-share-consumer
--data-share-arn <value>
```

For more information about the command, see [disassociate-data-share-consumer](../../../cli/latest/reference/redshift/disassociate-data-share-consumer.md "../../../cli/latest/reference/redshift/disassociate-data-share-consumer.md").
