

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Service Catalog Terraform Open Source product type support
<a name="sn-configure-terraform"></a>

AWS Service Management Connector supports AWS Service Catalog's Terraform open source product type. For more information, review [Getting started with Terraform product](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-Terraform.html) in the *AWS Service Catalog admin guide*. 

As of the 4.8.5 release, you can provision AWS Service Catalog products and their resources using either [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or [Hashicorp Terraform](https://www.terraform.io/) (Terraform open source). 

The **CloudFormation** product type in AWS Service Catalog allows you to request provisioning, create provisioned product plans, perform self-service actions, and request termination or update for the provisioned product. The connector also dynamically makes API calls to list available parameters such as VPC ID, Subnet IDs, and Security Groups in a drop down format. 

When provisioning fails for a CloudFormation product, the provisioned product **Status** changes to `TERMINATED`. 

The **Terraform open source** product type in AWS Service Catalog allows you to request provisioning for Terraform open source products as well as request termination or update for the provisioned product. 

**Note**  
The Terraform open source product type does not support self-service actions and provisioned product plans. 

When the provisioning fails for a Terraform open source product, the provisioned product **Status** changes to `TAINTED`. 