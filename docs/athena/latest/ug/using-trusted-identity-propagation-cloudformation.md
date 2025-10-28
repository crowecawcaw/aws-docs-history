# Configure and deploy resources using AWS CloudFormation

You can configure and deploy resources using AWS CloudFormation templates to start using Trusted
Identity Propagation with Athena drivers as following.

1. Download an AWS CloudFormation template to set up the IAM Identity Center customer managed application
   and access roles along with workgroup and IAM Identity Center application tags. You can
   download it from this [AWS CloudFormation template link](https://downloads.athena.us-east-1.amazonaws.com/drivers/CFNTemplate/AthenaDriversTrustedIdentityPropagationCFNTemplate.yaml "https://downloads.athena.us-east-1.amazonaws.com/drivers/CFNTemplate/AthenaDriversTrustedIdentityPropagationCFNTemplate.yaml").
2. Run the `create-stack` AWS CLI command to deploy the AWS CloudFormation stack that
   will provision the configured resources as following.

```
aws cloudformation create-stack \
    --stack-name my-stack \
    --template-url URL_of_the_file_that_contains_the_template_body \
    --parameters file://params.json
```

3. To view the status of the resources provisioning, navigate to the AWS CloudFormation
   console. After the cluster creation completes, view the new IAM Identity Center application in
   Identity Center console. You can view the IAM roles in the IAM console.

The tags will be associated in Workgroup as well as IAM Identity Center application. 4. Using the created roles and application, you can use the Athena drivers
immediately. To use JDBC driver, see [JDBC auth plugin connection
parameters](jdbc-v3-driver-jwt-tip-credentials.md "jdbc-v3-driver-jwt-tip-credentials.md"). To use ODBC driver, see [ODBC auth plugin connection
parameters](odbc-v2-driver-jwt-tip.md "odbc-v2-driver-jwt-tip.md").
