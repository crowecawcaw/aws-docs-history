

# View CloudWatch metrics with the API dashboard in API Gateway
<a name="how-to-api-dashboard"></a>

You can use the API dashboard in the API Gateway Console to display the CloudWatch metrics of your deployed API in API Gateway. These are shown as a summary of API activity over time. 

**Topics**
+ [Prerequisites](#how-to-api-dashboard-prerequisites)
+ [Examine API activities in the dashboard](#how-to-api-dashboard-console)

## Prerequisites
<a name="how-to-api-dashboard-prerequisites"></a>

1. You must have an API created in API Gateway. Follow the instructions in [Develop REST APIs in API Gateway](rest-api-develop.md).

1. You must have the API deployed at least once. Follow the instructions in [Deploy REST APIs in API Gateway](how-to-deploy-api.md).

## Examine API activities in the dashboard
<a name="how-to-api-dashboard-console"></a>

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose an API.

1. In the main navigation pane, choose **Dashboard**.

1. For **Stage**, choose the desired stage.

1. Choose **Date range** to specify a range of dates.

1. Refresh, if needed, and view individual metrics displayed in separate graphs titled **API calls**, **Latency**, **Integration latency**, **Latency**, **4xx error** and **5xx error**.
**Tip**  
To examine method-level CloudWatch metrics, make sure that you have enabled CloudWatch Logs on a method level. For more information about how to set up method-level logging, see [Override stage-level settings](set-up-stages.md#how-to-method-override).