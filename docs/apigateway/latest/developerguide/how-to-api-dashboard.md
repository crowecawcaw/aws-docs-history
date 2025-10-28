# View CloudWatch metrics with the API dashboard in API Gateway

You can use the API dashboard in the API Gateway Console to display the CloudWatch metrics of your deployed API in API Gateway. These are shown as a summary of API activity over time.

###### Topics

- [Prerequisites](#how-to-api-dashboard-prerequisites "#how-to-api-dashboard-prerequisites")
- [Examine API activities in the dashboard](#how-to-api-dashboard-console "#how-to-api-dashboard-console")

## Prerequisites

1. You must have an API created in API Gateway. Follow the instructions in [Develop REST APIs in API Gateway](rest-api-develop.md "rest-api-develop.md").
2. You must have the API deployed at least once. Follow the instructions in [Deploy REST APIs in API Gateway](how-to-deploy-api.md "how-to-deploy-api.md").

## Examine API activities in the dashboard

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. Choose an API.
3. In the main navigation pane, choose **Dashboard**.
4. For
   **Stage**, choose the desired stage.
5. Choose **Date range** to specify a range of dates.
6. Refresh, if needed, and view individual metrics displayed in separate graphs titled **API
   calls**, **Latency**, **Integration latency**,
   **Latency**, **4xx error** and **5xx error**.

###### Tip

To examine method-level CloudWatch metrics, make sure that you have enabled CloudWatch Logs on a method level. For
more information about how to set up method-level logging, see [Override stage-level settings](set-up-stages.md#how-to-method-override "set-up-stages.md#how-to-method-override").
