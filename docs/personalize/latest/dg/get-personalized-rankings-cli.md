# Getting a personalized ranking (AWS CLI)

The following code samples show how different variations of how to get a personalized ranking with the AWS CLI.

###### Topics

- [Getting a personalized ranking](#personalized-ranking-cli-sample "#personalized-ranking-cli-sample")
- [Including item metadata in a personalized ranking](#getting-personalized-ranking-with-metadata-cli "#getting-personalized-ranking-with-metadata-cli")

## Getting a personalized ranking

Use the following `get-personalized-ranking` command to get a personalized ranking with the AWS CLI.
Specify the Amazon Resource Name (ARN) for your campaign, the User ID for the user, and provide a list of item IDs for
the items to be ranked for the user (each separated by a space). The items to be ranked must be in the data that you
used to train the solution version. A list of ranked recommendations displays. Amazon Personalize considers the first item in
the list of most interest to the user.

```
aws personalize-runtime get-personalized-ranking \
--campaign-arn `Campaign ARN` \
--user-id `12` \
--input-list `3 4 10 8 12 7`
```

## Including item metadata in a personalized ranking

If you enabled metadata in recommendations for your campaign, you can specify the Items dataset metadata columns
to include in the response. For information about enabling metadata, see [Item metadata in recommendations](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").

The following code sample shows how to specify the metadata columns as part of your request for a personalized ranking.

```
aws personalize-runtime get-personalized-ranking \
--campaign-arn `Campaign ARN` \
--user-id `12` \
--input-list `3 4 10 8 12 7`
--metadata-columns "{\"ITEMS\": ["\"`columnNameA`"\","\"`columnNameB`"\"]}"
```
