# Developing with Amazon S3 using the AWS CLI

The Amazon S3 AWS CLI commands are organized into different sets in AWS CLI Command Reference and each has it’s own available commands. If you don't find the command that you're looking for in one set, check one of the other sets. The different sets are as follows:


* `s3` – Describes high-level commands for working with objects and buckets. These include copy, list and move actions. For a complete list of commands in this set, see [s3](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html") in the AWS CLI Command Reference.
* `s3api` – Describes low-level commands that manage S3 resources such as buckets, objects, sessions and multipart uploads. These commands correspond to the [Amazon S3 API](API_Operations_Amazon_Simple_Storage_Service.md "API_Operations_Amazon_Simple_Storage_Service.md") operations. For a complete list of CLI commands in this set, see [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html") in the AWS CLI Command Reference.
* `s3control` – Describes low-level commands that manage all other S3 resources such as Access Grants, Storage Lens groups, and Amazon S3 on Outposts buckets. These commands correspond to the [Amazon S3 Control](API_Operations_AWS_S3_Control.md "API_Operations_AWS_S3_Control.md") API operations. For a complete list of CLI commands in this set, see [s3control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/index.html") in the AWS CLI Command Reference.
If you are having issues setting up the AWS CLI, see [see How do I resolve the "Unable to locate credentials" error in Amazon S3](https://repost.aws/knowledge-center/s3-locate-credentials-error "https://repost.aws/knowledge-center/s3-locate-credentials-error") in the AWS re:Post Knowledge Center.
 

###### Note

Services in AWS, such as Amazon S3, require that you provide credentials when you access
 them. The service can then determine whether you have permissions to access the resources
 that it owns. The console requires your password. You can create access keys for your AWS account to access the AWS CLI or API. However, we don't recommend that you access AWS using
 the credentials for your AWS account. Instead, we recommend that you use AWS Identity and Access Management (IAM).
 Create an IAM user, add the user to an IAM group with administrative permissions, and then
 grant administrative permissions to the IAM user that you created. You can then access AWS
 using a special URL and the credentials of that IAM user. For instructions, go to [Creating Your First IAM user
 and Administrators Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html") in the *IAM User Guide*.


## Learn more about the AWS CLI


To learn more about the AWS, see the following resources: 



* [AWS Command Line Interface](https://aws.amazon.com/cli "https://aws.amazon.com/cli")
* [AWS Command Line Interface User Guide for Version 2](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-welcome.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-welcome.html")
