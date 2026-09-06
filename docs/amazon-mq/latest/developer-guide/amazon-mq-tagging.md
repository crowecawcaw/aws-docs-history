

# Adding tags to Amazon MQ resources
<a name="amazon-mq-tagging"></a>

To organize and identify your Amazon MQ resources for cost allocation, you can add metadata *tags* that identify the purpose of a broker or configuration. This is especially useful when you have many brokers. You can use cost allocation tags to organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill to include the tag keys and values. For more information, see [Setting Up a Monthly Cost Allocation Report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html#allocation-report) in the *AWS Billing User Guide*.

For instance, you could add tags that represent the cost center and purpose of your Amazon MQ resources:




- **`Broker1`**
  - **Key:** Cost Center / **Value:** 34567
  - **Key:** Stack / **Value:** Production

- **`Broker2`**
  - **Key:** Cost Center / **Value:** 34567
  - **Key:** Stack / **Value:** Production

- **`Broker3`**
  - **Key:** Cost Center / **Value:** 12345
  - **Key:** Stack / **Value:** Development



This tagging scheme allows you to group two brokers performing related tasks in the same cost center, while tagging an unrelated broker with a different cost allocation tag.

## Adding tags in the Amazon MQ Console
<a name="tagging-manage-console"></a>

You can quickly add tags to the resources you are creating in the Amazon MQ console by following these steps: 

1. From the **Create a broker** page, select **Additional settings**.

1. Under **Tags**, select **Add tag**.

1. Enter a **Key** and **Value** pair.

1. (Optional) Select **Add tag** to add multiple tags to your broker.

1. Select **Create broker**.

To add tags as you create a configuration:

1. From the **Create configuration** page, select **Advanced**.

1. Under **Tags** on the **Create configuration** page, select **Add tag**.

1. Enter a **Key** and **Value** pair.

1. (Optional) Select **Add tag** to add multiple tags to your configuration.

1. Select **Create configuration**.

After adding tags, you can view, edit, and remove the tags for your resources in the Amazon MQ console. You can also view the tags of your resources using the REST API. For more information, see the [Amazon MQ REST API Reference](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-tag.html). 