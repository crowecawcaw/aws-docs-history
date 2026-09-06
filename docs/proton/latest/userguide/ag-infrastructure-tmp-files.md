

End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October 7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure will remain intact. For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# AWS Proton infrastructure as code files
<a name="ag-infrastructure-tmp-files"></a>

The primary parts of the template bundle are *infrastructure as code (IaC) files* that define the infrastructure resources and properties that you want to provision. AWS CloudFormation and other infrastructure as code engines use these types of files to provision infrastructure resources.

**Note**  
An IaC file can also be used independently of template bundles, as a direct input to *directly defined components*. For more information about components, see [AWS Proton components](ag-components.md).

AWS Proton currently supports two types of IaC files:
+ *[CloudFormation](ag-infrastructure-tmp-files-cloudformation.md) files* – Used for *AWS-managed provisioning*. AWS Proton uses Jinja on top of the CloudFormation template file format for parametrization.
+ *[Terraform HCL](ag-infrastructure-tmp-files-terraform.md) files* – Used for *Self-managed provisioning*. HCL natively supports parametrization.

You can’t provision AWS Proton resources using a combination of provisioning methods. You must use one or the other. You can’t deploy an AWS-managed provisioning service to a self-managed provisioning environment, or vice versa.

For more information, see [How AWS Proton provisions infrastructure](ag-works-prov-methods.md), [AWS Proton environments](ag-environments.md), [AWS Proton services](ag-services.md), and [AWS Proton components](ag-components.md).