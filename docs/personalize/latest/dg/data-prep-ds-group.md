# Creating an Amazon Personalize dataset group

After you [create schema JSON files for your data](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md"),
you are ready to create a dataset group. In Amazon Personalize, a _dataset group_ is a container
for Amazon Personalize resources, including datasets, domain recommenders, and custom resources. A dataset group organizes your resources into independent collections, where resources from one dataset
group can't influence resources in any other dataset group.

You create a dataset group for each of your business domains.
For example, you might have an application that provides
recommendations for streaming video and another that provides recommendations for audio books. In Amazon Personalize, you
would create a dataset group for each application. This way, the data from one application
does not influence the recommendations Amazon Personalize generates for the other application.

You can create a Domain dataset group or a Custom dataset group:

- With a _Domain dataset group_, you create resources that are pre-configured and optimized for
  different use cases. When you create a dataset group, you make it a Domain dataset group by specifying a domain of
  VIDEO_ON_DEMAND or ECOMMERCE.

If you have a streaming video or e-commerce application, we recommend that you create a Domain dataset group. You
can still add custom resources, such as solutions and solution versions trained for custom use cases. You can't create next best action resources, including Actions and Action Interactions datasets, in a domain dataset group.

- A _Custom dataset group_ includes only custom resources that you configure depending on your use
  case. With custom resources, you train and deploy configurable solutions and solution versions (a trained Amazon Personalize
  recommendation model) based on your business needs. If don't have a VIDEO_ON_DEMAND or ECOMMERCE application, we recommend
  that you create a Custom dataset group. Otherwise, we recommend starting with a Domain dataset group and adding custom
  resources as necessary.
  You can create a dataset group with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

###### Topics

- [Creating a dataset group (console)](#data-prep-creating-ds-group-console "#data-prep-creating-ds-group-console")
- [Creating a dataset group (AWS CLI)](#data-prep-creating-ds-group-cli "#data-prep-creating-ds-group-cli")
- [Creating a dataset group (AWS SDKs)](#data-prep-creating-ds-group-sdk "#data-prep-creating-ds-group-sdk")

## Creating a dataset group (console)

Create a dataset group by specifying the dataset group name in the Amazon Personalize console.

###### To create a dataset group

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
2. Choose **Create dataset group**.
3. If this is your first time using Amazon Personalize, on the **Create dataset group** page, in **New
   dataset group**, choose **Get started**.
4. In **Dataset group details**, for **Dataset group name**, specify a name for your
   dataset group.
5. Choose your **Domain**:
   - Choose **E-commerce** to create an ECOMMERCE Domain dataset group.
   - Choose **Video on demand** to create a VIDEO_ON_DEMAND Domain dataset group.
   - Choose **Custom** to create a Custom dataset group with only custom resources, such as
     solutions, campaigns, and batch inference jobs.

6. For **Tags**, optionally add any tags. For more information about tagging Amazon Personalize resources, see
   [Tagging Amazon Personalize resources](tagging-resources.md "tagging-resources.md").
7. Choose **Create dataset group**. The **Overview** page displays. You are now ready
   to create a schema and a dataset. See [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md").

## Creating a dataset group (AWS CLI)

To create a dataset group, use the `create-dataset-group` operation. To create a Domain dataset group, for
domain specify `ECOMMERCE` or `VIDEO_ON_DEMAND`. To create a Custom dataset group, don't specify a
domain. You can use the Tags parameter to optionally tag resources in Amazon Personalize. For a sample see [Adding tags (AWS CLI)](tags-add.md#add-tag-cli "tags-add.md#add-tag-cli").

The following code creates a Domain dataset group for the `VIDEO_ON_DEMAND` domain.

```
aws personalize create-dataset-group \
--name `dataset-group-name` \
--domain VIDEO_ON_DEMAND
```

If successful, the dataset group Amazon Resource Name (ARN) display as follows.

```
{
  "datasetGroupArn": "arn:aws:personalize:us-west-2:acct-id:dataset-group/DatasetGroupName"
}
```

Record this value for future use. To display the dataset group that you created, use the
`describe-dataset-group` command and specify the returned dataset group ARN.

```
aws personalize describe-dataset-group \
--dataset-group-arn `dataset group arn`

```

The dataset group and its properties display as follows.

```
{
    "datasetGroup": {
        "name": "DatasetGroupName",
        "datasetGroupArn": "arn:aws:personalize:us-west-2:acct-id:dataset-group/DatasetGroupName",
        "status": "ACTIVE",
        "creationDateTime": 1542392161.262,
        "lastUpdatedDateTime": 1542396513.377
    }
}
```

When the dataset group's `status` is ACTIVE, you are ready
to create a schema and a dataset. See [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md").

## Creating a dataset group (AWS SDKs)

Use the following code to create a Domain dataset group. Give the Domain dataset group a name, and for
`domain`, specify either `ECOMMERCE` or `VIDEO_ON_DEMAND`. To create a
Custom dataset group, modify the code to remove the domain parameter.

For more information about the API operation, see [CreateDatasetGroup](API_CreateDatasetGroup.md "API_CreateDatasetGroup.md") in the API reference section. You can use the Tags parameter to optionally tag resources in Amazon Personalize. For a sample see [Adding tags (AWS SDKs)](tags-add.md#add-tag-sdk "tags-add.md#add-tag-sdk").

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

response = personalize.create_dataset_group(
  name = '`dataset group name`',
  domain = '`business domain`'
)
dsg_arn = response['datasetGroupArn']

description = personalize.describe_dataset_group(datasetGroupArn = dsg_arn)['datasetGroup']

print('Name: ' + description['name'])
print('ARN: ' + description['datasetGroupArn'])
print('Status: ' + description['status'])
```

SDK for Java 2.x

```
public static String createDomainDatasetGroup(PersonalizeClient personalizeClient,
                                              String datasetGroupName,
                                              String domain) {

    try {
        CreateDatasetGroupRequest createDatasetGroupRequest = CreateDatasetGroupRequest.builder()
                .name(datasetGroupName)
                .domain(domain)
                .build();
        return personalizeClient.createDatasetGroup(createDatasetGroupRequest).datasetGroupArn();
    } catch (PersonalizeException e) {
        System.out.println(e.awsErrorDetails().errorMessage());
    }
    return "";
}
```

SDK for JavaScript v3

```
// Get service clients module and commands using ES6 syntax.
import { CreateDatasetGroupCommand } from "@aws-sdk/client-personalize";
import { personalizeClient } from "./libs/personalizeClients.js";

// Or, create the client here.
// const personalizeClient = new PersonalizeClient({ region: "REGION"});

// Set the domain dataset group parameters.
export const domainDatasetGroupParams = {
  name: "NAME" /* required */,
  domain:
    "DOMAIN" /* required for a domain dsg, specify ECOMMERCE or VIDEO_ON_DEMAND */,
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateDatasetGroupCommand(domainDatasetGroupParams),
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```

The [DescribeDatasetGroup](API_DescribeDatasetGroup.md "API_DescribeDatasetGroup.md") operation returns the
`datasetGroupArn` and the status of the operation. When the dataset group's `status` is ACTIVE, you are ready
to create a schema and a dataset. See [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md").
