

# Code Editor Connections and Extensions
<a name="code-editor-use-connections-and-extensions"></a>

Code Editor supports IDE connections to AWS services as well as extensions available in the [Open VSX Registry](https://open-vsx.org/). 

## Connections to AWS
<a name="code-editor-use-connections"></a>

Code Editor environments are integrated with the [AWS Toolkit for VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html) to add connections to AWS services. To get started with connections to AWS services, you must have valid AWS Identity and Access Management (IAM) credentials. For more information, see [Authentication and access for the AWS Toolkit for Visual Studio Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/establish-credentials.html).

Within your Code Editor environment, you can add connections to: 
+  [AWS Explorer ](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/aws-explorer.html) – View, modify, and deploy AWS resources in Amazon S3, CloudWatch, and more.

  Accessing certain features within AWS Explorer requires certain AWS permissions. For more information, see [Authentication and access for the AWS Toolkit for Visual Studio Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/establish-credentials.html).
+ [Amazon CodeWhisperer](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/codewhisperer.html) – Build applications faster with AI-powered code suggestions. 

  To use Amazon CodeWhisperer with Code Editor, you must add the following permissions to your SageMaker AI execution role.

------
#### [ JSON ]

****  

  ```
  {
    "Version":"2012-10-17",		 	 	 
    "Statement": [
      {
        "Sid": "CodeWhispererPermissions",
        "Effect": "Allow",
        "Action": ["codewhisperer:GenerateRecommendations"],
        "Resource": "*"
      }
    ]
  }
  ```

------

  For more information, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) and [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*.

## Extensions
<a name="code-editor-use-extensions"></a>

Code Editor supports IDE extensions available in the [Open VSX Registry](https://open-vsx.org/). 

To get started with extensions in your Code Editor environment, choose the **Extensions** icon (![Icon showing two overlapping squares representing multiple windows or instances.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/code-editor/code-editor-extensions-icon.png)) in the left navigation pane. Here, you can configure connections to AWS by installing the AWS Toolkit. For more information, see [Installing the AWS Toolkit for Visual Studio Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html).

In the search bar, you can search directly for additional extensions through the [Open VSX Registry](https://open-vsx.org/), such as the AWS Toolkit, Jupyter, Python, and more.