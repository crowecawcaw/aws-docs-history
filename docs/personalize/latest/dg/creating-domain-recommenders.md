# Creating domain recommenders in Amazon Personalize

You can create recommenders with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs. The following
includes detailed steps to create recommenders with the Amazon Personalize console and code examples
that show how to create a recommender with only the required fields.

- For code samples that show how to enable metadata in recommendations, see [Enabling metadata in recommendations](create-recommender-return-metadata.md "create-recommender-return-metadata.md").
- For code samples that show how to configure the columns used when training the models backing your recommender, see [Configuring columns used when creating an Amazon Personalize domain
  recommender](create-recommender-configure-columns.md "create-recommender-configure-columns.md").
- For code samples that show how to configure exploration for the `Top picks for your` or `Recommended for you` use cases, see [Configuring exploration for a domain recommender](create-recommender-configure-exploration.md "create-recommender-configure-exploration.md").

###### Topics

- [Creating recommenders (console)](#creating-recommenders-console "#creating-recommenders-console")
- [Creating a recommender (AWS CLI)](#create-recommender-cli "#create-recommender-cli")
- [Creating a recommender (AWS SDKs)](#create-recommender-sdk "#create-recommender-sdk")

## Creating recommenders (console)

###### Important

A high `minRecommendationRequestsPerSecond` will increase your bill. We recommend starting with 1 for
`minRecommendationRequestsPerSecond` (the default). Track your usage using Amazon CloudWatch metrics, and increase
the `minRecommendationRequestsPerSecond` as necessary. For more information, see [Minimum recommendation requests per second and
auto-scaling](creating-recommenders.md#min-rrps-auto-scaling "creating-recommenders.md#min-rrps-auto-scaling").

Create recommenders for each of your use cases with the Amazon Personalize console as follows. If you just created your
Domain dataset group and you are already on the **Overview** page, skip to step 3.

###### To create recommenders

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
2. On the **Dataset groups** page, choose your Domain dataset group.
3. In **Step 3**, choose **Use <domain name> recommenders** and choose
   **Create recommenders**.
4. On the **Choose use cases** page, choose the use cases you want to create recommenders and give
   each a **Recommender name**. Amazon Personalize creates a recommender for each use case that you choose. The
   available use cases depend on your domain. For information on choosing a use case see [Choosing a use case](domain-use-cases.md "domain-use-cases.md").
5. Choose **Next**.
6. On the **Advanced configuration** page, configure each recommender depending on your business
   needs:
   - For each dataset used by the recommender's use case, you can choose the columns Amazon Personalize considers when training
     the models backing your recommender. By default, Amazon Personalize uses all columns that can be used when training. For more
     information, see [Configuring columns used when creating an Amazon Personalize domain
     recommender](create-recommender-configure-columns.md "create-recommender-configure-columns.md").
   - You can modify **Minimum recommendation requests per second** to specify a new minimum
     request capacity for your recommender. A high `minRecommendationRequestsPerSecond` will increase your
     bill. We recommend starting with 1 (the default). Track your usage using Amazon CloudWatch metrics, and increase the
     `minRecommendationRequestsPerSecond` as necessary. For more information see [Minimum recommendation requests per second and
     auto-scaling](creating-recommenders.md#min-rrps-auto-scaling "creating-recommenders.md#min-rrps-auto-scaling").
   - If you want the ability to include Items dataset metadata with recommendations, choose **Return items metadata in recommendation results**. If enabled, you can specify the columns from your
     Items dataset in your request for recommendations or personalized ranking. Amazon Personalize returns this data for each item
     in the recommendation response.

   To enable metadata, you must have an Items dataset with a column of metadata.
   - For `Top picks for your` or `Recommended for you` use cases, optionally make changes to
     exploration configuration. Exploration involves testing different item recommendations to learn how users respond
     to items with very little interaction data. Use the following fields to configure exploration:
     - Emphasis on exploring less relevant items (exploration weight) – Configure how
       much to explore. Specify a decimal value between 0 to 1. The default is 0.3. The closer the value is to 1, the more exploration. With more exploration,
       recommendations include more items with less item interactions data or relevance based on previous behavior. At zero, no
       exploration occurs and recommendations are based on current data
       (relevance).
     - Exploration item age cutoff – Specify the maximum item age in days since
       the latest interaction across all items in the Item interactions dataset. This defines the scope of item exploration based on
       item age. Amazon Personalize determines item age based on its creation timestamp or, if creation timestamp data is missing, item interactions data. For
       more information how Amazon Personalize determines item age, see [Creation timestamp data](items-datasets.md#creation-timestamp-data "items-datasets.md#creation-timestamp-data").

     To increase the items Amazon Personalize considers
     during exploration, enter a greater value. The minimum is 1 day and the default is 30 days. Recommendations might include items
     that are older than the item age cut off you specify. This is because these items are
     relevant to the user and exploration didn't identify them.

   - For **Tags**, optionally add any tags. For more information about tagging Amazon Personalize resources, see
     [Tagging Amazon Personalize resources](tagging-resources.md "tagging-resources.md").

7. To create recommenders for each of your use cases, choose **Create recommenders**.

You can monitor the status of each recommender on the **Recommenders** page. When your
recommender status is Active, you can use it in your application to get recommendations.

## Creating a recommender (AWS CLI)

Use the following AWS CLI code to create a recommender for a domain use case. Run this code for each of your domain use
cases. For `recipeArn`, provide the Amazon Resource Name (ARN) for your use case. The available use cases
depend on your domain. For a list of use cases and their ARNs see [Choosing a use case](domain-use-cases.md "domain-use-cases.md").

```
aws personalize create-recommender \
--name `recommender name` \
--dataset-group-arn `dataset group ARN` \
--recipe-arn `recipe ARN`
```

## Creating a recommender (AWS SDKs)

Create a recommender for a domain use case with the following code. Give your recommender a name and provide your
Domain dataset group's Amazon Resource Name (ARN). For `recipeArn`, provide the ARN for your use case. Run
this code for each of your domain use cases. The available use cases depend on your domain. For a list of use cases, their
ARNs, and their requirements, see [Choosing a use case](domain-use-cases.md "domain-use-cases.md").

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

create_recommender_response = personalize.create_recommender(
  name = '`recommender name`',
  recipeArn = '`recipe ARN`',
  datasetGroupArn = '`dataset group ARN`'
)

recommender_arn = create_recommender_response['recommenderArn']

print('Recommender ARN:' + recommender_arn)
```

SDK for Java 2.x

```
    public static String createRecommender(PersonalizeClient personalizeClient,
            String name,
            String datasetGroupArn,
            String recipeArn) {

        long maxTime = 0;
        long waitInMilliseconds = 30 * 1000; // 30 seconds
        String recommenderStatus = "";

        try {
            CreateRecommenderRequest createRecommenderRequest = CreateRecommenderRequest.builder()
                    .datasetGroupArn(datasetGroupArn)
                    .name(name)
                    .recipeArn(recipeArn)
                    .build();

            CreateRecommenderResponse recommenderResponse = personalizeClient
                    .createRecommender(createRecommenderRequest);
            String recommenderArn = recommenderResponse.recommenderArn();
            System.out.println("The recommender ARN is " + recommenderArn);

            DescribeRecommenderRequest describeRecommenderRequest = DescribeRecommenderRequest.builder()
                    .recommenderArn(recommenderArn)
                    .build();

            maxTime = Instant.now().getEpochSecond() + 3 * 60 * 60;

            while (Instant.now().getEpochSecond() < maxTime) {

                recommenderStatus = personalizeClient.describeRecommender(describeRecommenderRequest).recommender()
                        .status();
                System.out.println("Recommender status: " + recommenderStatus);

                if (recommenderStatus.equals("ACTIVE") || recommenderStatus.equals("CREATE FAILED")) {
                    break;
                }
                try {
                    Thread.sleep(waitInMilliseconds);
                } catch (InterruptedException e) {
                    System.out.println(e.getMessage());
                }
            }
            return recommenderArn;

        } catch (PersonalizeException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return "";
    }

```

SDK for JavaScript v3

```
// Get service clients and commands using ES6 syntax.
import { CreateRecommenderCommand, PersonalizeClient } from
  "@aws-sdk/client-personalize";

// create personalizeClient
const personalizeClient = new PersonalizeClient({
  region: "REGION"
});

// set the recommender's parameters
export const createRecommenderParam = {
  name: "RECOMMENDER_NAME",                    /* required */
  recipeArn: "RECIPE_ARN",                     /* required */
  datasetGroupArn: "DATASET_GROUP_ARN"         /* required */
}

export const run = async () => {
  try {
    const response = await personalizeClient.send(new CreateRecommenderCommand(createRecommenderParam));
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```
