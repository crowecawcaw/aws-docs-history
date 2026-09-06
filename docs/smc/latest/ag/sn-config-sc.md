

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring AWS Service Catalog
<a name="sn-config-sc"></a>

This section provides the configurations you need to integrate AWS services in ServiceNow. 

**To configure Service Catalog**

1. Follow the steps to [create a Service Catalog portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/portfoliomgmt-create.html). 

1. To add the Amazon S3 bucket product to the portfolio you created in Step 1, go to the Service Catalog console. In the **Upload new product** page, enter the product details.

1. For **Select template**, choose the Amazon S3 bucket CloudFormation template you saved to your device.

1. Set **Constraint type** to **Launch** for the product that you created now with the `SCConnectLaunch` role in the baseline permissions. For additional launch constraint instructions, see [AWS Service Catalog Launch Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html).
**Note**  
The AWS configuration design requires each Service Catalog product to have a launch constraint. Failure to follow this step could result in an *Unable to Retrieve Parameter* message in the ServiceNow Service Catalog. 

1. Add the SMEndUser user to the Service Catalog portfolio. For additional user access instructions, see [Granting Access to Users](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html). 

**Note**  
 The AWS configuration design requires each Service Catalog product to have either a launch constraint or a stack set constraint. Failure to follow this step could result in an *Unable to Retrieve Parameter* error in the ServiceNow Service Catalog. 