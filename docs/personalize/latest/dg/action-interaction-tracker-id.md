# Finding the ID of your action interaction event tracker

When you create an Action interactions dataset, Amazon Personalize automatically creates an _action interaction_ event tracker for
you. You specify the tracker's ID in the PutActionInteractions API operation. Amazon Personalize uses it to
direct new data to the _Action interactions dataset_ in your
dataset group.

You can find your event tracker's ID on the details page of your Action interactions dataset in the Amazon Personalize console. And you
can find the ID by calling the DescribeDataset API operation. The following Python code prints the tracking ID for an
Action interactions dataset.

```
import boto3

personalize = boto3.client(service_name='personalize')

response = personalize.describe_dataset(
  datasetArn="`Action interactions dataset ARN`"
)

print(response['trackingId'])
```
