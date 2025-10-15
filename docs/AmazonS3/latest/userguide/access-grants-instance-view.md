# Get the details of an S3 Access Grants instance

You can get the details of your Amazon S3 Access Grants instance in a particular AWS Region. You can get the details of your S3 Access Grants instance by using the
 Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and the AWS SDKs.

###### To get the details of an S3 Access Grants instance

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose
 **Access Grants**.
3. On the **S3 Access Grants** page, choose the Region that contains
 the S3 Access Grants instance that you want to work with.
4. The **S3 Access Grants** page lists your S3 Access Grants instances
 and any cross-account instances that have been shared with your account. To
 view the details of an instance, choose **View details**.
To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") in the *AWS Command Line Interface User Guide*. 

To use the following example command, replace the ``user input
 placeholders`` with your own information.

###### Example – Get the details of an S3 Access Grants instance


```
aws s3control get-access-grants-instance \
 --account-id `111122223333` \
 --region `us-east-2` 

```
Response:


```
{
    "AccessGrantsInstanceArn": "arn:aws:s3:`us-east-2`: `111122223333`:access-grants/default",
    "AccessGrantsInstanceId": "default",
    "CreatedAt": "`2023-05-31T17:54:07.893000+00:00`"
}

```
For information about the Amazon S3 REST API support for managing an S3 Access Grants instance, see the
 following sections in the *Amazon Simple Storage Service API Reference*:


* [GetAccessGrantsInstance](../API/API_control_GetAccessGrantsInstance.md "../API/API_control_GetAccessGrantsInstance.md")
* [GetAccessGrantsInstanceForPrefix](../API/API_control_GetAccessGrantsInstanceForPrefix.md "../API/API_control_GetAccessGrantsInstanceForPrefix.md")
This section provides examples of how to get the details of an S3 Access Grants instance by
 using the AWS SDKs.

To use the following examples, replace the ``user input
 placeholders`` with your own information.


Java
###### Example – Get an S3 Access Grants instance


```
public void getAccessGrantsInstance() {
GetAccessGrantsInstanceRequest getRequest = GetAccessGrantsInstanceRequest.builder()
.accountId("`111122223333`")
.build();
GetAccessGrantsInstanceResponse getResponse = s3Control.getAccessGrantsInstance(getRequest);
LOGGER.info("GetAccessGrantsInstanceResponse: " + getResponse);
}
```
Response:


```
GetAccessGrantsInstanceResponse(
AccessGrantsInstanceArn=arn:aws:s3:`us-east-2`: `111122223333`:access-grants/default,
CreatedAt=`2023-06-07T01:46:20.507Z`)
```
