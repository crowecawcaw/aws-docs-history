

# Associate or disassociate your IAM Identity Center instance
<a name="access-grants-instance-idc"></a>

In Amazon S3 Access Grants, you can associate the AWS IAM Identity Center instance of your corporate identity directory with an S3 Access Grants instance. After you do so, you can create access grants for your corporate directory users and groups, in addition to AWS Identity and Access Management (IAM) users and roles. 

If you no longer want to create access grants for your corporate directory users and groups, you can disassociate your IAM Identity Center instance from your S3 Access Grants instance. 

You can associate or disassociate an IAM Identity Center instance by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and the AWS SDKs.

## Using the S3 console
<a name="access-grants-instance-idc-console"></a>

Before you associate your IAM Identity Center instance with your S3 Access Grants instance, you must add your corporate identity directory to IAM Identity Center. For more information, see [S3 Access Grants and corporate directory identities](access-grants-directory-ids.md).

**To associate an IAM Identity Center instance with an S3 Access Grants instance**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Access Grants**. 

1. On the **S3 Access Grants** page, choose the Region that contains the S3 Access Grants instance that you want to work with.

1. Choose **View details** for the instance. 

1. On the details page, in the **IAM Identity Center** section, choose to either **Add** an IAM Identity Center instance or **Deregister** an already associated IAM Identity Center instance. 

## Using the AWS CLI
<a name="access-grants-instance-idc-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*. 

To use the following example command, replace the `{{user input placeholders}}` with your own information.

**Example – Associate an IAM Identity Center instance with an S3 Access Grants instance**  

```
aws s3control associate-access-grants-identity-center \
 --account-id {{111122223333}} \
 --identity-center-arn arn:aws:sso:::instance/ssoins-{{1234a567bb89012c}} \
 --profile {{access-grants-profile}} \
 --region {{eu-central-1}}
     
// No response body
```

**Example – Disassociate an IAM Identity Center instance from an S3 Access Grants instance**  

```
aws s3control dissociate-access-grants-identity-center \
 --account-id {{111122223333}} \
 --profile {{access-grants-profile}} \
 --region {{eu-central-1}}
     
// No response body
```

## Using the REST API
<a name="access-grants-instance-idc-rest-api"></a>

For information about the Amazon S3 REST API support for managing the association between an IAM Identity Center instance and an S3 Access Grants instance, see the following sections in the *Amazon Simple Storage Service API Reference*:
+  [AssociateAccessGrantsIdentityCenter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AssociateAccessGrantsIdentityCenter.html) 
+  [DissociateAccessGrantsIdentityCenter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DissociateAccessGrantsIdentityCenter.html) 