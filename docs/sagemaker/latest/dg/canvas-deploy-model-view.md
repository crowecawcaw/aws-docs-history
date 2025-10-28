# View your deployments

You might want to check the status or details of a model deployment in Amazon SageMaker Canvas. For
example, if your deployment failed, you might want to check the details to
troubleshoot.

You can view your Canvas model deployments from the Canvas application or from
the Amazon SageMaker AI console.

To view deployment details from Canvas, choose one of the following
procedures:

To view your deployment details from the **ML Ops** page, do the
following:

1. Open the SageMaker Canvas application.
2. In the left navigation pane, choose **ML Ops**.
3. Choose the **Deployments** tab.
4. Choose your deployment by name from the list.
   To view your deployment details from a model version’s page, do the following:

5. In the SageMaker Canvas application, go to your model version’s details page.
6. Choose the **Deploy** tab.
7. On the **Deployments** section that lists all of the
   deployment configurations associated with that model version, find your
   deployment.
8. Choose the **More options** icon (
   ![More options icon for the output CSV file.](images/studio/canvas/more-options-icon.png)
   ), and then select **View details** to open
   the details page.
   The details page for your deployment opens, and you can view information such as the
   time of the most recent prediction, the endpoint’s status and configuration, and the
   model version that is currently deployed to the endpoint.

You can also view your currently active Canvas workspace instances and active
endpoints from the **SageMaker AI dashboard** in the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/"). Your Canvas endpoints
are listed alongside any other SageMaker AI Hosting endpoints that you’ve created, and you can
filter them by searching for endpoints with the Canvas tag.

The following screenshot shows the SageMaker AI dashboard. In the
**Canvas** section, you can see that one workspace instance is in
service and four endpoints are active.

![Screenshot of the SageMaker AI dashboard showing the active Canvas workspace instances and endpoints.](images/studio/canvas/canvas-sagemaker-dashboard.png)
