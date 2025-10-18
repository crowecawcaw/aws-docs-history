AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Getting started with Amazon CodeCatalyst in
 AWS Cloud9

This section provides an overview of how to get started using CodeCatalyst. The topics in
 this section cover how to use AWS Cloud9 in Amazon CodeCatalyst and how to replicate your AWS Cloud9
 environment in CodeCatalyst. Later topics also detail how to create a CodeCatalyst Dev Environment and
 how to access your Dev Environment using the AWS Cloud9 IDE.

AWS Toolkits are IDE-specific software development kits (SDKs) that provide quick
 access to AWS Cloud accounts, services, and resources. From your CodeCatalyst account in the
 AWS Toolkit, you can view, edit, and manage your CodeCatalyst Dev Environments, Spaces,
 and projects in a convenient interface. To learn more about the AWS Cloud services and
 features that are available through AWS Toolkits, see [What is the
 AWS Toolkit for Visual Studio Code?](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html "https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html"), [AWS Toolkit for
 AWS Cloud9](toolkit-welcome.md "toolkit-welcome.md"), and [What is the
 AWS Toolkit for JetBrains?](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html "https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html").[What is the
 AWS Toolkit for JetBrains](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html "https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html") guides.


To use CodeCatalyst with the AWS Cloud9 IDE, you must have an existing Space, project and Dev Environment that you
 created within the CodeCatalyst console. 


###### Note

Don't create a subfolder named **projects** within a folder of
 the same name within the File System of the AWS Cloud9 IDE for CodeCatalyst. If you do so,
 you can't access any files within this directory. This issue affects the file
 path **/projects/projects**. File paths such as
 **/test/projects** and **/projects/test/projects** aren't affected by this issue. This is a
 known issue and only affects the AWS Cloud9 IDE File Explorer.


###### Note

It is not currently possible to create a subfolder named **projects** within a folder of the same name, using the File System
 of the AWS Cloud9 IDE for CodeCatalyst. You will not be able to access any files within this
 directory from the AWS Cloud9 IDE File Explorer, but you will be able access them
 using the command line. Please use an alternative folder name. This issue only
 affects the file path **/projects/projects**, file
 paths such as **/test/projects** and **/projects/test/projects** should work. This is a known
 issue and only affects the AWS Cloud9 IDE File Explorer.
