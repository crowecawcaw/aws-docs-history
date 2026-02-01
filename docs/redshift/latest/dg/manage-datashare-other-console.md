Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Managing datashares from other

accounts as a consumer

## Removing association of datashare

from data consumers

As a consumer administrator, you can remove association of datashares from data
consumers.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Datashares**. The
   datashare list page appears.
3. Choose **From other accounts**.
4. In the **Datashares from other accounts** section,
   choose the datashare to remove association from data consumers.
5. In the **Data consumers** section, choose one or more
   data consumers to remove association from. Then choose **Remove
   association**.
6. When the Remove association page appears, choose **Remove
   association**.

After association is removed, data consumers will lose access to the datashare.
You can change the data consumer association at any time.

## Declining datashares

As a consumer administrator, you can reject any datashare whose state is [available or
active](access-cross-account.md#manage-status "access-cross-account.md#manage-status"). After you reject a datashare, consumer cluster users lose
access to the datashare. Amazon Redshift doesn't return the rejected datashare if you
call the `DescribeDataSharesForConsumer` API operation. If the producer
administrator runs the `DescribeDataSharesForProducer` API operation,
they will see that the datashare was rejected. Once a datashare is rejected, the
producer administrator can authorize the datashare to a consumer cluster again,
and the consumer administrator can choose to associate their AWS account with
the datashare or reject it.

If your AWS account has an association to a datashare and a pending
association to a datashare that's managed by Lake Formation, rejecting the datashare
association that's managed by Lake Formation also rejects the original datashare. To reject
a specific association, the producer administrator can remove authorization from a
specified datashare. This action doesn't affect other datashares.

To reject a datashare, use the AWS console, the API operation
`RejectDataShare`, or `reject-datashare` in the
AWS CLI.

###### To reject a datashare using the AWS console:

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. In the navigation menu, choose **Datashares**.
3. Choose **From other accounts**.
4. In the **Datashares from other accounts** section,
   choose the datashare you want to decline. When the **Decline
   datashare** page appears, choose
   **Decline**.

After you decline the datashares, you can't revert the change. Amazon Redshift removes
the datashares from the list. To see the datashare again, the producer
administrator must authorize it again.
