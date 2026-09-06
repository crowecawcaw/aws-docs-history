

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Deleting or removing a data accessor's access from your Amazon Q index
<a name="data-accessors-removing-access"></a>

You can remove a data accessor's permissions to your Amazon Q index using the Amazon Q Business console or the Amazon Q Business API using the AWS SDK, REST API, or AWS CLI. Once deleted, you will have to add the data and reconfigure access to grant the data accessor access again.

The following procedures show how you delete or remove a data accessor using the Amazon Q Business console or the AWS CLI.

**Topics**
+ [Using the Amazon Q Business console](#data-accessors-removing-access-console)
+ [Using the AWS CLI;](#data-accessors-removing-access-cli)

## Using the Amazon Q Business console
<a name="data-accessors-removing-access-console"></a>

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. Choose **Applications**, then select the name of your application environment from the list.

1. From the left navigation, choose **Data accessors**.

1. From the **Data accessor** table, select the data accessor that you want to delete.

1. Choose **Actions**, then choose **Delete**.

1. Confirm your choice.

## Using the AWS CLI;
<a name="data-accessors-removing-access-cli"></a>

```
aws qbusiness delete-data-accessor \
--application-id ${qbusiness_application_id} \
--data-accessors-id ${qbusiness_data_accessor_id}

aws qbusiness disassociate-permission \
--application-id ${qbusiness_application_id} \
--statement-id ${policy_statement_id}
```