# CreateIngestion

Use the `CreateIngestion` to create and start a new SPICE ingestion on a dataset.

Any ingestions operating on tagged datasets inherit the same tags automatically for use in access control. For an example, see [How do I create an IAM policy to control access to Amazon EC2 resources using tags?](https://aws.amazon.com/premiumsupport/knowledge-center/iam-ec2-resource-tags/ "https://aws.amazon.com/premiumsupport/knowledge-center/iam-ec2-resource-tags/") in the AWS Knowledge Center. Tags are visible on the tagged dataset, but not on the ingestion resource.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight create-ingestion
    --data-set-id `DATASETID`
    --ingestionid `INGESTIONID`
    --aws-account-id `AWSACCOUNTID`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight create-ingestion
    --cli-input-json file://`createingestion`.json
```

For more information about the `CreateIngestion` operation, see [CreateIngestion](../APIReference/API_CreateIngestion.md "../APIReference/API_CreateIngestion.md") in the _Quick Sight API Reference_.
