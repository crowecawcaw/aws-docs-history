

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Template validation
<a name="cfn-ingest-validate"></a>

You can self-validate your CloudFormation template before submitting it to AMS.

Templates submitted to AMS CloudFormation ingest are validated to ensure they are safe to deploy within an AMS account. The validation process checks the following:
+ **Supported resources** – Only AMS CloudFormation ingest-supported resources are used. For more information, see [Supported Resources](cfn-ingest-supp-services.md).
+ **Supported AMIs **– The AMI in the template is an AMS-supported AMI. For information about AMS AMIs, see [AMS Amazon Machine Images (AMIs)](ams-amis.md).
+ **AMS Shared Services subnet** – The template does not attempt to launch resources into the AMS Shared Services subnet.
+ **Resource policies** – There are no overly permissive resource policies, such as a publicly readable or writeable S3 bucket policy. AMS doesn't allow publicly readable or writable S3 buckets in AWS accounts.

## Validate with CloudFormation Linter
<a name="cfn-ingest-validate-linter"></a>

You can self-validate your CloudFormation template before submitting it to AMS by using the CloudFormation Linter tool.

The CloudFormation Linter tool is the best way to validate your CloudFormation template as it provides validation for resource/property names, data types, and functions. For more information, see [aws-cloudformation/cfn-python-lint](https://github.com/aws-cloudformation/cfn-python-lint).

The CloudFormation Linter output of the template shown previously is as follows:

```
$ cfn-lint -t ./testtmpl.json
E3002 Invalid Property Resources/SNSTopic/Properties/Name
./testtmpl.json:6:9
```

To assist with offline validation of CloudFormation templates, AMS has developed a set of pluggable custom validation rules for the CloudFormation Linter tool. They're located on the **Developers Resources** page of the AMS console.

Follow these steps to use CloudFormation pre-ingestion validation scripts:

1. Install the CloudFormation Linter tool. For installation instructions, see [aws-cloudformation / cfn-lint ](https://github.com/aws-cloudformation/cfn-python-lint).

1. Download a .zip file with validation scripts:

    [CFN Lint Custom Rules](https://github.com/awslabs/aws-managed-services/tree/main/cfn-lint-custom-rules).

1. Unzip the attached rules to a directory of your choice.

1. Validate your CloudFormation template by running the following command:

   ```
   cfn-lint --template {{{TEMPLATE_FILE}}} --append-rules {{{DIRECTORY_WITH_CUSTOM_RULES}}}
   ```