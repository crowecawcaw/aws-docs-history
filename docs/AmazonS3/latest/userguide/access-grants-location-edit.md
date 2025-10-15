# Update a registered location

You can update the AWS Identity and Access Management (IAM) role of a location that's registered in your Amazon
 S3 Access Grants instance. For each new IAM role that you use to register a location in S3 Access Grants, be
 sure to give the S3 Access Grants service principal (`access-grants.s3.amazonaws.com`)
 access to this role. To do this, add an entry for the new IAM role in the same trust
 policy JSON file that you used when you first [registered the
 location](access-grants-location.md "access-grants-location.md"). 

You can update a location in your S3 Access Grants instance by using the Amazon S3 console, the AWS Command Line Interface
 (AWS CLI), the Amazon S3 REST API, and the AWS SDKs.

###### To update the IAM role of a location registered with your S3 Access Grants
 instance

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose
 **Access Grants**.
3. On the **S3 Access Grants** page, choose the Region that contains
 the S3 Access Grants instance that you want to work with.
4. Choose **View details** for the instance.
5. On the details page for the instance, choose the
 **Locations** tab.
6. Find the location that you want to update. To filter the list of
 locations, use the search box.
7. Choose the options button next to the registered location that you want to
 update.
8. Update the IAM role, and then choose **Save
 changes**.
To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") in the *AWS Command Line Interface User Guide*. 

To use the following example command, replace the ``user input
 placeholders`` with your own information.

###### Example – Update the IAM role of a registered location


```
aws s3control update-access-grants-location \
--account-id `111122223333` \
--access-grants-location-id `635f1139-1af2-4e43-8131-a4de006eb999` \
--iam-role-arn arn:aws:iam::`777788889999`:role/`accessGrantsTestRole`

```
Response:


```
{
    "CreatedAt": "`2023-05-31T18:23:48.107000+00:00`",
    "AccessGrantsLocationId": "`635f1139-1af2-4e43-8131-a4de006eb999`",
    "AccessGrantsLocationArn": "arn:aws:s3:`us-east-2`:`777788889999`:access-grants/default/location/`635f1139-1af2-4e43-8131-a4de006eb888`",
    "LocationScope": "s3://`amzn-s3-demo-bucket/prefixB*`",
    "IAMRoleArn": "arn:aws:iam::`777788889999`:role/`accessGrantsTestRole`"
}
```
For information on the Amazon S3 REST API support for updating a location in an S3 Access Grants
 instance, see [UpdateAccessGrantsLocation](../API/API_control_UpdateAccessGrantsLocation.md "../API/API_control_UpdateAccessGrantsLocation.md") in the
 *Amazon Simple Storage Service API Reference*.

This section provides examples of how to update the IAM role of a registered
 location by using the AWS SDKs.

To use the following example, replace the ``user input
 placeholders`` with your own information.


Java
###### Example – Update the IAM role of a registered location


```
public void updateAccessGrantsLocation() {
UpdateAccessGrantsLocationRequest updateRequest = UpdateAccessGrantsLocationRequest.builder()
.accountId("`111122223333`")
.accessGrantsLocationId("`635f1139-1af2-4e43-8131-a4de006eb999`")
.iamRoleArn("arn:aws:iam::`777788889999`:role/`accessGrantsTestRole`")
.build();
UpdateAccessGrantsLocationResponse updateResponse = s3Control.updateAccessGrantsLocation(updateRequest);
LOGGER.info("UpdateAccessGrantsLocationResponse: " + updateResponse);
}
```
Response:


```
UpdateAccessGrantsLocationResponse(
CreatedAt=`2023-06-07T04:35:10.027Z`,
AccessGrantsLocationId=`635f1139-1af2-4e43-8131-a4de006eb999`,
AccessGrantsLocationArn=arn:aws:s3:`us-east-2`:`777788889999`:access-grants/default/location/`635f1139-1af2-4e43-8131-a4de006eb888`,
LocationScope=s3://`amzn-s3-demo-bucket/prefixB*`,
IAMRoleArn=arn:aws:iam::`777788889999`:role/`accessGrantsTestRole`
)
```
