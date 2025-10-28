# Delete a model deployment

You can delete your model deployments from the Amazon SageMaker Canvas application. This action also
deletes the endpoint from the SageMaker AI console and shuts down any endpoint-related
resources.

###### Note

Optionally, you can delete your endpoint through the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") or using the SageMaker AI
`DeleteEndpoint` API. For more information, see [Delete Endpoints and Resources](realtime-endpoints-delete-resources.md "realtime-endpoints-delete-resources.md"). However, when you delete
the endpoint through the SageMaker AI console or APIs instead of the Canvas application,
the list of deployments in Canvas isn’t automatically updated. You must also
delete the deployment from the Canvas application to remove it from the
list.

To delete a deployment in Canvas, do the following:

1. Open the SageMaker Canvas application.
2. In the left navigation panel, choose **ML Ops**.
3. Choose the **Deployments** tab.
4. From the list of deployments, choose the one that you want to delete.
5. At the top of the deployment details page, choose the **More options**
   icon (
   ![More options icon for the output CSV file.](images/studio/canvas/more-options-icon.png)
   ).
6. Choose **Delete deployment**.
7. In the **Delete deployment** dialog box, choose
   **Delete**.
   Your deployment and SageMaker AI Hosting endpoint should now be deleted from both Canvas and the SageMaker AI console.
