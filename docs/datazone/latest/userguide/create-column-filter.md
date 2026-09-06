

# Create column filters in Amazon DataZone
<a name="create-column-filter"></a>

Amazon DataZone enables you to create column filters that you can use when approving subscriptions to make sure that the subscriber can only access columns of data as defined in the column filters. To create a column filter, follow the steps below: 

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and sign in with the AWS account where the domain was created, then choose **Open data portal**.

1. Choose **Select project** from the top navigation pane and select the project to which the asset belongs.

1. Navigate to the **Data** tab for the project.

1. Choose **Published data** from the left navigation pane, then select the asset for which you want to create the column filter. You can add column filters if your data asset in Amazon DataZone is of type AWS Glue table, Amazon Redshift table, or Amazon Redshift view. 

1. On the asset detail page, go to **Asset filters** tab and then choose **Add asset filter**.

1. Configure the following fields:
   + **Name** – the name of the filter
   + **Description** – the description of the filters

1. Under filter type, choose **Column filter**.

1. Select the columns you want to include in the filters using the check boxes again the columns in the data asset. 

1. Choose Create filter

For information on how to apply column filters to a subscription, see [Approve or reject a subscription request in Amazon DataZone](approve-reject-subscription-request.md) .