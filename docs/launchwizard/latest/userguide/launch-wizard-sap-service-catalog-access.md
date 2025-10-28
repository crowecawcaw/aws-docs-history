# Access

AWS Service Catalog products created with AWS Launch Wizard

Perform the following steps to access AWS Service Catalog products created
with AWS Launch Wizard.

In the AWS Service Catalog administrator console, the **Portfolio
details** page lists the portfolio settings. From this page, you can manage
the products in a portfolio, grant users access to products, and apply
`TagOptions` and constraints. You can manage products from the
**Products** page.

###### Access Service Catalog products as a Service Catalog Admin user

1. Navigate to the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog "https://console.aws.amazon.com/servicecatalog").
2. In the left navigation pane, under **Administration**, choose
   **Portfolios**.
3. Choose the portfolio named **AWS Launch Wizard Products**, which is
   the default portfolio created by Launch Wizard.
4. Choose **AWS Launch Wizard products**.
5. The product created by Launch Wizard using AWS CloudFormation templates and user inputs is named
   **[LW Deployment Name]-[Deployment Type]**. You can create
   a new version by choosing **Create new version**.
6. You can associate tags or apply product-specific tags as needed.

###### Access Service Catalog products as an IAM user

1. Navigate to the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog "https://console.aws.amazon.com/servicecatalog").
2. In the left navigation pane. under **Home**, choose
   **Products**.
3. Search for the Launch Wizard SAP product that you saved from the Launch Wizard deployment, and
   select it. The product, won't be visible to any user who has not been granted
   access to it. To grant access to the product, see [Granting Access to Users](../../../servicecatalog/latest/adminguide/catalogs_portfolios_users.md "../../../servicecatalog/latest/adminguide/catalogs_portfolios_users.md").
4. Choose **Launch product**.
5. You will be directed to the AWS Service Catalog
   **Launching** page, which resembles AWS CloudFormation. Most of the
   parameters are specified using your defaults. Enter or replace the default
   values as you require, including passwords and SAPSIDs.
6. After you verify the parameters, choose **Launch product** to
   start the creation of the AWS CloudFormation stack.
