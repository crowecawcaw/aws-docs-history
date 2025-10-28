Defect Detection App is in preview release and is subject to change.

# Deploying your model to a station

To use your model you must deploy to a station. During deployment the station must be online
and able to reach the Defect Detection App. To check if the model is already deployed,
choose the **Station deployments** tab on the model's details page.

You can also use the Station App to view the models that are deployed to a station.

###### To deploy a model

1. If you're not on the project details page, do the following:
   1. [Sign in](dda-signin-dda-web-app.md "dda-signin-dda-web-app.md") to the Defect Detection App Console.
   2. In the top navigation pane, choose **Projects**.
   3. On the projects page, choose the project. The console opens the project details page.

2. From the **Model versions** tab,choose the model that you want to deploy.
3. On the model details page, choose **Deploy**.
4. On the **Select station** page, select the station where you want to
   deploy the model.
5. Choose **Next**.
6. Use the **Review** page to make sure the deployment details are correct.
   If not, choose **Previous** to make changes, or choose
   **Cancel** to cancel the deployment.

###### Note

The station must be online during the deployment for the deployment to succeed. 7. If you are ready to deploy the model, choose **Deploy model**. The
console opens the **Station deployments** tab of the project details page.
While the station is deploying the model, the **Operation status** is
**Updating station**. 8. When the **Operation status** is no longer **Updating
station**, perform the following steps to confirm that the model has deployed to the
station.

    1. From the **Station deployments** tab of the project details page,
     choose the station to open the station details page.
    2. In the **Models** section, check that the model is listed.

9. Next step: [Analyzing images with the Defect Detection Station App](dda-inference.md "dda-inference.md").
