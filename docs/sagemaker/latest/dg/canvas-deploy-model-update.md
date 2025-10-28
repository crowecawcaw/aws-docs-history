# Update a deployment configuration

You can update the deployment configuration for models that you've deployed
to endpoints in Amazon SageMaker Canvas. For example, you can deploy an
updated model version to the endpoint, or you can update the instance type or number of
instances behind the endpoint based on your capacity needs.

There are several different ways for you to update your deployment from the Canvas
application. You can use any of the following methods:

- On the **ML Ops** page of the Canvas application, you can
  choose the **Deployments** tab and select the deployment that
  you want to update. Then, choose **Update
  configuration**.
- When on the details page for a model version, on the
  **Deploy** tab, you can view the deployments for that
  version. Next to the deployment, choose the **More options**
  icon (
  ![More options icon for the output CSV file.](images/studio/canvas/more-options-icon.png)
  ) and then choose **Update
  configuration**.
  Both of the preceding methods open the **Update configuration** side
  panel, where you can make changes to your deployment configuration. To update the
  configuration, do the following:

1. For the **Select version** dropdown menu, you can select a
   different model version to deploy to the endpoint.

###### Note

When updating a deployment configuration, you can only choose a different
model version to deploy. To deploy a different model, create a new
deployment. 2. For **Instance type**, you can select a different instance
type for hosting your model. 3. For **Instance count**, you can change the number of active
instances that are used for your endpoint. 4. Choose **Save**.
Your deployment configuration should now be updated.
