# Delete a stage

When you no longer need a stage, you can delete it to avoid paying for unused resources.
The following steps show you how to use the API Gateway console to delete a
stage.

###### Warning

Deleting a stage might cause part or all of the corresponding API to be unusable by
API callers. Deleting a stage cannot be undone, but you can recreate the stage and
associate it with the same deployment.

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. Choose a REST API.
3. In the main navigation pane, choose **Stages**.
4. In the **Stages** pane, choose the stage you want to delete,
   and then choose **Stage actions**, **Delete stage**.
5. When you're prompted, enter `confirm`, and then choose **Delete**.
