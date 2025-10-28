# AWS Service Catalog Notification Constraints

###### Note

AWS Service Catalog does not support notification constraints for Terraform Open Source or Terraform Cloud products.

A notification constraint specifies an Amazon SNS topic to receive notifications about stack
events.

Use the following procedure to create an SNS topic and subscribe to it.

###### To create an SNS topic and a subscription

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. Choose **Create topic**.
3. Type a topic name and then choose **Create topic**.
4. Choose **Create subscription**.
5. For **Protocol**, select **Email**.
   For **Endpoint**, type an email address that you can use to receive notifications.
   Choose **Create subscription**.
6. You'll receive a confirmation email with the subject line `AWS
 Notification - Subscription Confirmation`. Open the email and follow the
   directions to complete your subscription.
   Use the following procedure to apply a notification constraint using the SNS topic
   that you created using the previous procedure.

###### To apply a notification constraint to a product

1. Open the Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/").
2. Choose the portfolio that contains the product.
3. Expand **Constraints** and choose **Add constraints**.
4. Choose the product from **Product** and set **Constraint type**
   to **Notification**. Choose **Continue**.
5. Choose **Choose a topic from your account** and select
   the SNS topic that you created from **Topic Name**.
6. Choose **Submit**.
