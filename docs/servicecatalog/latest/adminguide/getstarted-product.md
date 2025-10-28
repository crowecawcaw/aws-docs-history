# Step 4: Create a new product in the portfolio

After you have created a portfolio, you are ready to create a product within the portfolio.
For this tutorial, you will create a product called **Linux Desktop**, a
cloud development environment that runs on Amazon Linux, inside of the
**Engineering Tool** portfolio.

###### To create a product within a portfolio

1. If you've just completed the previous step, the **Portfolios** page is already
   displayed. Otherwise, open [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/").
2. Choose and open the **Engineering Tool** portfolio you created
   in Step 2.
3. Choose **Upload new product.**
4. On the **Create product** page in the Product details section, enter
   the following:
   - **Product name** –
     `Linux Desktop`
   - **Product description** – `Cloud
development environment configured for engineering staff. Runs AWS
Linux.`
   - **Owner** – `IT`
   - **Distributor** –
     _(blank)_

5. On the **Version details** page, choose **Use a CloudFormation template**. Then choose **Specify an Amazon S3 template URL** and enter the following:
   - **Select template** – `https://awsdocs.s3.amazonaws.com/servicecatalog/development-environment.template`
   - **Version title** – `v1.0`
   - **Description** – `Base
Version`

6. In the **Support details** section, enter the following:
   - **Email contact** –
     `ITSupport@example.com`
   - **Support link** –
     `https://wiki.example.com/IT/support`
   - **Support description** – `Contact the
IT department for issues deploying or connecting to this product.`

7. Choose **Create product**.
