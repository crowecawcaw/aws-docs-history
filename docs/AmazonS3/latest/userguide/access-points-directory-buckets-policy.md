

# Viewing, editing or deleting access point policies
<a name="access-points-directory-buckets-policy"></a>

You can use an AWS Identity and Access Management (IAM) access point policy to control the principal and resource that can access the access point. The access point scope manages the prefixes and API permissions for the access point. You can create, edit, and delete an access point policy using the AWS Command Line Interface, REST API, or AWS SDKs. For more information about access point scope, see [Manage the scope of your access points for directory buckets](access-points-directory-buckets-manage-scope.md).

**Note**  
Since directory buckets use session-based authorization, your policy must always include the `s3express:CreateSession` action.

## Using the S3 console
<a name="access-point-directory-bucket-edit-policy-console"></a>

**To view, edit, or delete an access point policy**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region that you want to list access points for. 

1. In the navigation pane on the left side of the console, choose **Access points for directory buckets**.

1. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.

1. Choose the name of the access point you want to manage.

1. Choose the **Permissions** tab.

1. To create or edit the access point policy, in **Access point policy**, choose **Edit**. Edit the policy. Choose **Save**.

1. To delete the access point policy, in **Access point policy**, choose **Delete**. In the **Delete access point policy** window, type **confirm** and choose **Delete**.

## Using the AWS CLI
<a name="access-points-directory-buckets-edit-policy-cli"></a>

You can use the `get-acccess-point-policy`, `put-access-point-policy`, and `delete-access-point-policy` commands to view, edit, or delete an access point policy. For more information, see [get-access-point-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point-policy.html#get-access-point-policy), [put-access-point-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-access-point-policy.html#put-access-point-policy), or [delete-access-point-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point-policy.html#delete-access-point-policy) in the AWS CLI Command Reference.

## Using the REST API
<a name="access-points-directory-buckets-edit-policy-rest"></a>

You can use the REST API `GetAccessPointPolicy`, `DeleteAccessPointPolicy`, and `PutAccessPointPolicy` operations to view, delete, or edit an access point policy. For more information, see [PutAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html), [GetAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html), or [DeleteAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html) in the Amazon Simple Storage Service API Reference.

## Using the AWS SDKs
<a name="access-points-directory-buckets-edit-policy-sdk"></a>

You can use the AWS SDKs to view, delete, or edit an access point policy. For more information, see the list of supported SDKs for [GetAccessControlPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html#API_control_PutAccessPointPolicy_SeeAlso), [DeleteAccessControlPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html#API_control_PutAccessPointPolicy_SeeAlso), and [PutAccessControlPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html#API_control_PutAccessPointPolicy_SeeAlso) in the Amazon Simple Storage Service API Reference.