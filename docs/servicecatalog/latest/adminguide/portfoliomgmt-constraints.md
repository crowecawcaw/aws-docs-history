# Adding Constraints

You should add constraints to control how users engage with products. For
more information about the types of constraints that AWS Service Catalog supports, see [Using AWS Service Catalog Constraints](constraints.md "constraints.md").

You add constraints to products after they have been placed in a portfolio.

###### To add a constraint to a product

1. Open the Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/").
2. Choose **Portfolios** and select a portfolio.
3. In the portfolio details page, expand the **Create
   constraint** section and choose **Add constraints**.
4. For **Product**, select the product to which to apply the constraint.
5. For **Constraint type**, choose one of the following options:

**Launch** – Allows you to assign an IAM role to
the product that is used to provision the AWS resources. For more information, see [AWS Service Catalog Launch Constraints](constraints-launch.md "constraints-launch.md").

**Notification** – Allows you to stream product
notifications to an Amazon SNS topic. For more information, see [AWS Service Catalog Notification Constraints](constraints-notification.md "constraints-notification.md").

**Template** – Allows you to limit the options
that are available to end users when they launch the product. A Template consists of a
JSON–formatted text file that contains one or more rules. Rules are added to the CloudFormation template used by the product. For more information, see [Template Constraint Rules](reference-template_constraint_rules.md "reference-template_constraint_rules.md").

**Stack Set** – Allows you to configure product deployment across
accounts and regions using CloudFormation StackSets. For more information, see [AWS Service Catalog Stack Set Constraints](constraints-stackset.md "constraints-stackset.md").

**Tag Update** – Allows you to update tags after the product has been provisioned.
For more information, see [AWS Service Catalog Tag Update Constraints.](constraints-resourceupdate.md "constraints-resourceupdate.md") 6. Choose **Continue** and enter the required information.

###### To edit a constraint

1. Sign in to the AWS Management Console and open the AWS Service Catalog administrator console at [https://console.aws.amazon.com/catalog/](https://console.aws.amazon.com/catalog/ "https://console.aws.amazon.com/catalog/").
2. Choose **Portfolios** and select a portfolio.
3. In the **Portfolio details** page, expand the **Create constraint** section and select the constraint to edit.
4. Choose **Edit constraints**.
5. Edit the constraint as needed, and choose **Save**.
