# Working with S3 Access Grants instances

To get started with using AmazonS3 Access Grants, you first create an S3 Access Grants instance. You can create
 only one S3 Access Grants instance per AWS Region per account. The S3 Access Grants instance serves as the container
 for your S3 Access Grants resources, which include registered locations and grants. 

With S3 Access Grants, you can create permission grants to your S3 data for AWS Identity and Access Management (IAM) users and
 roles. If you've [added your
 corporate identity directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html "https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html") to AWS IAM Identity Center, you can associate this IAM Identity Center instance
 of your corporate directory with your S3 Access Grants instance. After you've done so, you can create
 access grants for your corporate users and groups. If you haven't yet added your corporate
 directory to IAM Identity Center, you can associate your S3 Access Grants instance with an IAM Identity Center instance later. 

###### Topics

* [Create an S3 Access Grants instance](access-grants-instance-create.md "access-grants-instance-create.md")
* [Get the details of an S3 Access Grants instance](access-grants-instance-view.md "access-grants-instance-view.md")
* [List your S3 Access Grants instances](access-grants-instance-list.md "access-grants-instance-list.md")
* [Associate or disassociate your IAM Identity Center
 instance](access-grants-instance-idc.md "access-grants-instance-idc.md")
* [Delete an S3 Access Grants instance](access-grants-instance-delete.md "access-grants-instance-delete.md")
