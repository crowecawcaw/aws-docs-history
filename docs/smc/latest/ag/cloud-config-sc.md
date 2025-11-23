# Configuring AWS Service Catalog integration

This section provides the configurations you need to integrate AWS services in
Jira Service Management Cloud.

###### To configure Service Catalog

1. Follow the steps to [create a Service Catalog portfolio](../../../servicecatalog/latest/adminguide/portfoliomgmt-create.md "../../../servicecatalog/latest/adminguide/portfoliomgmt-create.md") to create a portfolio.
2. To add the Amazon S3 bucket product to the portfolio you created in Step 1, go to
   the Service Catalog console. In the **Upload new product** page, enter the
   product details.
3. For **Select template**, choose the Amazon S3 bucket
   CloudFormation template you saved to your device.
4. Set **Constraint type** to **Launch** for
   the product that you created now with the `SCConnectLaunch` role in
   the baseline permissions. For additional launch constraint instructions, see
   [AWS Service Catalog Launch Constraints](../../../servicecatalog/latest/adminguide/constraints-launch.md "../../../servicecatalog/latest/adminguide/constraints-launch.md").

###### Note

The AWS configuration design requires each Service Catalog product to
have a launch constraint. Failure to follow this step could result in an
_Unable to Retrieve Parameter_ message
in the ServiceNow Service Catalog. 5. Add the _SMEndUser_ IAM user to the Service Catalog portfolio. For additional user access
instructions, see [Granting Access to Users](../../../servicecatalog/latest/adminguide/catalogs_portfolios_users.md "../../../servicecatalog/latest/adminguide/catalogs_portfolios_users.md").

###### Note

The AWS configuration design requires each Service Catalog product to have
either a launch constraint or a stack set constraint. Failure to follow this step
could result in an _Unable to Retrieve Parameter_
error in the ServiceNow Service Catalog.
