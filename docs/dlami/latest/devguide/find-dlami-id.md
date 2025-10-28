# Finding the ID of a DLAMI

Each DLAMI has a unique identifier (ID). When you launch a DLAMI instance using the Amazon EC2 console, you can optionally use the DLAMI ID to search for the DLAMI that you want to use. When you launch a DLAMI instance using the AWS Command Line Interface (AWS CLI), this ID is required.

You can find the ID for the DLAMI of your choice by
using an AWS CLI command for either Amazon EC2 or Parameter Store, a capability of AWS Systems Manager. For instructions on installing and configuring
the AWS CLI, see [Get started with the
AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the _AWS Command Line Interface User Guide_.

Using Parameter Store

###### To find a DLAMI ID using **ssm get-parameter**

In the following [**ssm get-parameter**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter.html") command, for the `--name` option, the parameter name format is `/aws/service/deeplearning/ami/$architecture/$ami_type/latest/ami-id`. In this name format, `architecture` can be either `x86_64` or `arm64`. Specify the `ami_type` by taking the DLAMI name and removing the keywords "deep", "learning", and "ami". AMI Name can be found in [Deep Learning AMIs Release Notes](appendix-ami-release-notes.md "appendix-ami-release-notes.md").

###### Important

To use this command, the AWS Identity and Access Management (IAM) principal that you use must have the `ssm:GetParameter` permission. For more information about IAM principals, see the [Additional resources](../../../IAM/latest/UserGuide/id_roles.md#id_roles_additional-resources "../../../IAM/latest/UserGuide/id_roles.md#id_roles_additional-resources") section of **IAM roles** in the _IAM User Guide_.

- ```
  aws ssm get-parameter --name `/aws/service/deeplearning/ami/x86_64/base-oss-nvidia-driver-ubuntu-22.04/latest/ami-id`  \
  --region `us-east-1` --query "Parameter.Value" --output text
  ```

```

The output should look similar to the following:



```

ami-09ee1a996ac214ce7

````

###### Tip

For some currently supported DLAMI frameworks, you can find more specific example **ssm get-parameter** commands in [Deep Learning AMIs Release Notes](appendix-ami-release-notes.md "appendix-ami-release-notes.md"). Choose the link to the release notes of your chosen DLAMI, and then find its ID query in the release notes.


Using Amazon EC2 CLI
###### To find a DLAMI ID using **ec2 describe-images**

In the following [**ec2 describe-images**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html") command, for the value of the filter `Name=name`, enter the DLAMI name. You can specify a release version for a given framework, or you can get the latest release by replacing the version number with a question mark (?).

* ```
aws ec2 describe-images --region `us-east-1` --owners amazon \
--filters 'Name=name,Values=`Deep Learning Base OSS Nvidia Driver GPU AMI (Ubuntu 22.04) ????????`' 'Name=state,Values=available' \
--query 'reverse(sort_by(Images, &amp;CreationDate))[:1].ImageId' --output text
````

The output should look similar to the following:

```
ami-09ee1a996ac214ce7
```

###### Tip

For an example **ec2 describe-images** command that's specific to the DLAMI of your choice, see [Deep Learning AMIs Release Notes](appendix-ami-release-notes.md "appendix-ami-release-notes.md"). Choose the link to the release notes of your chosen DLAMI, and then find its ID query in the release notes.

###### Next step

[Launching a DLAMI instance](launch.md "launch.md")
