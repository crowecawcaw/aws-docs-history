# Integrate Visual Studio with AWS CodeCommit

You can use Visual Studio to make code changes in a CodeCommit repository. The AWS Toolkit for Visual Studio now includes
features that make working with CodeCommit easier and more convenient when working in Visual
Studio..
The Toolkit for Visual Studio integration is designed to work with Git credentials and an IAM user. You can
clone existing repositories, create repositories, commit and push code changes to a
repository, and more.

###### Important

The Toolkit for Visual Studio is available for installation on Windows operating systems
only. If you are
looking for information about working with Visual Studio Code, see [AWS Toolkit for Visual Studio Code](../../../toolkit-for-vscode/latest/userguide/welcome.md "../../../toolkit-for-vscode/latest/userguide/welcome.md").

If you've used the Toolkit for Visual Studio before, you're probably already familiar with setting up AWS
credential profiles that contain an access key and secret key. Credential profiles are used
in the Toolkit for Visual Studio to enable calls to AWS service APIs (for example, to Amazon S3 to list buckets or
to CodeCommit to list repositories). To pull and push code to a CodeCommit repository, you also need
Git credentials. If you don't have Git credentials, the Toolkit for Visual Studio can generate and apply those
credentials for you. This can save you a lot of time.

To use Visual Studio with CodeCommit, you need the following:

- An IAM user with a valid set of credentials (an access key and secret key)
  configured for it. This IAM user should also have:

One of the CodeCommit managed policies and the
IAMSelfManageServiceSpecificCredentials
managed policy applied to it.

OR

If the IAM user already has Git credentials configured, one of the CodeCommit
managed policies or equivalent permissions.

For more information, see [AWS managed policies for
CodeCommit](security-iam-awsmanpol.md "security-iam-awsmanpol.md") and [Understanding and Getting Your
Security Credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md").

- The AWS Toolkit for Visual Studio installed on the computer where you've installed Visual Studio. For more
  information, see [Setting Up the
  AWS Toolkit for Visual Studio](../../../AWSToolkitVS/latest/UserGuide/getting-set-up.md "../../../AWSToolkitVS/latest/UserGuide/getting-set-up.md").
  For more information on using AWS Toolkit for Visual Studio with CodeCommit, see [Using AWS CodeCommit with Visual Studio Team Explorer](../../../toolkit-for-visual-studio/latest/user-guide/using-aws-codecommit-with-team-explorer.md "../../../toolkit-for-visual-studio/latest/user-guide/using-aws-codecommit-with-team-explorer.md") in the
  _Toolkit for Visual Studio User Guide_.
