# Grant Your Users Permissions to Build Custom Image and

Text Prediction Models

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

In Amazon SageMaker Canvas, you can build [custom models](canvas-build-model.md "canvas-build-model.md") to meet your
specific business need. Two of these custom model types are single-label image predicion and
multi-category text prediction. The permissions to build these model types are included in the
AWS Identity and Access Management (IAM) policy called [AmazonSageMakerCanvasFullAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess"), which SageMaker AI attaches by default to your user's
IAM execution role if you leave the [Canvas base
permissions turned on](canvas-getting-started.md#canvas-prerequisites "canvas-getting-started.md#canvas-prerequisites"). If you are using a custom IAM configuration, then you must explicitly add
permissions to your user's IAM execution role so that they can build custom image and text
prediction model types. To grant the necessary permissions to build image and text prediction
models, read the following section to learn how to attach a least-permissions policy to your
role.

To add the permissions to the user's IAM role, do the following:

1. Go to the [IAM console](https://console.aws.amazon.com/iamv2 "https://console.aws.amazon.com/iamv2").
2. Choose **Roles**.
3. In the search box, search for the user's IAM role by name and select it.
4. On the page for the user's role, under **Permissions**, choose
   **Add permissions**.
5. Choose **Create inline policy**.
6. Select the JSON tab, and then paste the following least-permissions policy into the
   editor.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateAutoMLJobV2",
 "sagemaker:DescribeAutoMLJobV2"
 ],
 "Resource": "*"
 }
 ]
}`

```

7. Choose **Review policy**.
8. Enter a **Name** for the policy.
9. Choose **Create policy**.
   For more information about AWS managed policies, see [Managed policies and
   inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") in the _IAM User Guide_.
