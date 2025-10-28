# Amazon Inspector Lambda code scanning

###### Important

This feature captures snippets of Lambda functions to highlight detected vulnerabilities.
These snippets can show hardcoded credentials and other sensitive materials.

With this feature, Amazon Inspector scans application code in a Lambda function for code vulnerabilities based on AWS security best practices to detect data leaks, injection flaws, missing encryption, and weak cryptography.
Amazon Inspector uses automated reasoning and machine learning to evaluate your Lambda function application code.
It also uses internal detectors that are developed in collaboration with Amazon Q to identify policy violations and vulnerabilities.

Amazon Inspector generates a [code vulnerability](findings-types.md#findings-types-code "findings-types.md#findings-types-code") when it detects a vulnerability in your Lambda function application code.
This finding type includes a code snippet showing the issue and where you can find the issue in your code.
It also suggests how to remediate the issue.
The suggestion includes plug-and-play code blocks that you can use to replace vulnerable lines of code.
These code fixes are provided in addition to general code remediation guidance for this finding type.

Code remediation suggestions is powered by automated reasoning.
Some code remediation suggestions might not work as intended.
You are responsible for the code remediation suggestions you adopt.
Always review code remediation suggestions before adopting them.
You might need to edit them to make sure your code performs as intended.
For more information, see the [Responsible AI Policy](https://aws.amazon.com/machine-learning/responsible-ai/policy/ "https://aws.amazon.com/machine-learning/responsible-ai/policy/").

If you want to activate Lambda code scanning, you must activate Lambda standard scanning first.
For more information, see [Activating a scan type](activate-scans.md "activate-scans.md").
For information about which AWS Regions support this feature, see [Region-specific feature
availability](inspector_regions.md#ins-regional-feature-availability "inspector_regions.md#ins-regional-feature-availability").

## Encrypting your code in code vulnerability findings

Amazon Q stores code snippets that are detected to be in connection with a code vulnerability finding using Lambda code scanning.
By default, Amazon Q controls [the AWS owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") used to encrypt your code.
However, you can use your own customer managed key for encryption through the Amazon Inspector API.
For more information, see [Encryption at rest for code in your findings](encryption-rest.md#encryption-code-snippets "encryption-rest.md#encryption-code-snippets").
