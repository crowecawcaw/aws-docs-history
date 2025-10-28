# AWS Systems Manager in Accelerate

An AWS Systems Manager document (SSM document) defines the actions that Systems Manager performs on your AWS resources. Systems Manager
includes more than a dozen pre-configured documents that you can use by specifying parameters at runtime. Documents
use JavaScript Object Notation (JSON) or YAML, and they include steps and parameters that you specify.

AWS Managed Services (AMS) is a trusted publisher for SSM documents. SSM documents owned by AMS are shared only with onboarded AMS accounts, always begin with a reserved prefix (AWSManagedServices-\*), and show up in the Systems Manager console, as owned by Amazon. The AMS process for SSM document development and publishing follows AWS best practices and requires multiple peer reviews throughout the document life cycle. For more information on AWS best practices for sharing SSM Documents, please visit [Best practices for shared SSM documents](../../../systems-manager/latest/userguide/ssm-before-you-share.md "../../../systems-manager/latest/userguide/ssm-before-you-share.md").

## Available AMS Accelerate SSM documents

AMS Accelerate SSM documents are available exclusively to AMS Accelerate customers, and are used to automate operational
workflow to operate your account.

To see the available AMS Accelerate SSM documents from the AWS Management Console:

1. Open the Systems Managerconsole at [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/documents "https://console.aws.amazon.com/systems-manager/documents").
2. Choose **Shared with me**.
3. In the search bar, filter by **Document name prefix**, then
   **Equals**, and set the value to
   **AWSManagedServices-**.

For AWS CLI instructions, see
[Using
shared SSM documents](../../../systems-manager/latest/userguide/ssm-using-shared.md "../../../systems-manager/latest/userguide/ssm-using-shared.md").

## AMS Accelerate SSM document versions

SSM documents support versioning. AMS Accelerate SSM documents can't be modified from the
customer’s account and can't be re-shared. They're centrally managed and maintained by AMS Accelerate in
order to operate the account.

Version numbers are incremented with each document update in a specific AWS Region. As
new Regions become available, the same document content in two Regions can have different
version numbers; this is typical and doesn't mean their behavior will be different. If you
want to compare two AMS Accelerate SSM documents, we recommend comparing their hashes with the
AWS CLI:

```

      aws ssm describe-document \
      --name AWSManagedServices-*`DOCUMENTNAME`* \
      --output text --query "Document.Hash"

```

Two SSM documents are identical if their hashes match.

## Systems Manager pricing

There is no cost associated with AMS Accelerate SSM document access. Runtime cost varies based on
the type of SSM document, its steps, and runtime duration. For more information, refer to
[AWS Systems Manager
pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").
