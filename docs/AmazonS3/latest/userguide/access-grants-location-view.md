# View the details of a registered location

You can get the details of a location that's registered in your S3 Access Grants instance by using the
Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and the AWS SDKs.

###### To view the locations registered in your S3 Access Grants instance

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Access
   Grants**.
3. On the **S3 Access Grants** page, choose the Region that contains
   the S3 Access Grants instance that you want to work with.
4. Choose **View details** for the instance.
5. On the details page for the instance, choose the
   **Locations** tab.
6. Find the registered location that you want to view. To filter the list of
   registered locations, use the search box.
   To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

To use the following example command, replace the `user input
 placeholders` with your own information.

###### Example – Get the details of a registered location

```
aws s3control get-access-grants-location \
--account-id `111122223333` \
--access-grants-location-id `default`

```

Response:

```
{
    "CreatedAt": "`2023-05-31T18:23:48.107000+00:00`",
    "AccessGrantsLocationId": "`default`",
    "AccessGrantsLocationArn": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/location/`default`",
    "IAMRoleArn": "arn:aws:iam::`111122223333`:role/`accessGrantsTestRole`"
}
```

###### Example – List all of the locations that are registered in an S3 Access Grants instance

To restrict the results to an S3 prefix or bucket, you can optionally use the
`--location-scope
 s3://`bucket-and-or-prefix`` parameter.

```
aws s3control list-access-grants-locations \
--account-id `111122223333` \
--region `us-east-2`
```

Response:

```
{"AccessGrantsLocationsList": [
  {
    "CreatedAt": "`2023-05-31T18:23:48.107000+00:00`",
    "AccessGrantsLocationId": "default",
    "AccessGrantsLocationArn": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/location/default",
    "LocationScope": "s3://"
    "IAMRoleArn": "arn:aws:iam::`111122223333`:role/`accessGrantsTestRole`"
     },
  {
    "CreatedAt": "`2023-05-31T18:23:48.107000+00:00`",
    "AccessGrantsLocationId": "`635f1139-1af2-4e43-8131-a4de006eb456`",
    "AccessGrantsLocationArn": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/location/`635f1139-1af2-4e43-8131-a4de006eb888`",
    "LocationScope": "s3://`amzn-s3-demo-bucket/prefixA*`",
    "IAMRoleArn": "arn:aws:iam::`111122223333`:role/`accessGrantsTestRole`"
     }
   ]
  }
```

For information about the Amazon S3 REST API support for getting the details of a registered
location or listing all of the locations that are registered with an S3 Access Grants
instance, see the following sections in the
_Amazon Simple Storage Service API Reference_:

- [GetAccessGrantsLocation](../API/API_control_GetAccessGrantsLocation.md "../API/API_control_GetAccessGrantsLocation.md")
- [ListAccessGrantsLocations](../API/API_control_ListAccessGrantsLocations.md "../API/API_control_ListAccessGrantsLocations.md")
  This section provides examples of how to get the details of a registered location
  or list all of the registered locations in an S3 Access Grants instance by using the AWS
  SDKs.

To use the following examples, replace the `user input
 placeholders` with your own information.

Java

###### Example – Get the details of a registered location

```
public void getAccessGrantsLocation() {
GetAccessGrantsLocationRequest getAccessGrantsLocationRequest = GetAccessGrantsLocationRequest.builder()
.accountId("`111122223333`")
.accessGrantsLocationId("default")
.build();
GetAccessGrantsLocationResponse getAccessGrantsLocationResponse = s3Control.getAccessGrantsLocation(getAccessGrantsLocationRequest);
LOGGER.info("GetAccessGrantsLocationResponse: " + getAccessGrantsLocationResponse);
}
```

Response:

```
GetAccessGrantsLocationResponse(
CreatedAt=`2023-06-07T04:35:10.027Z`,
AccessGrantsLocationId=default,
AccessGrantsLocationArn=arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/location/default,
LocationScope= s3://,
IAMRoleArn=arn:aws:iam::`111122223333`:role/`accessGrantsTestRole`
)
```

###### Example – List all registered locations in an S3 Access Grants

instance

To restrict the results to an S3 prefix or bucket, you can
optionally pass an S3 URI, such as `s3://`bucket-and-or-prefix``, in the `LocationScope` parameter.

```
public void listAccessGrantsLocations() {

ListAccessGrantsLocationsRequest listRequest =   ListAccessGrantsLocationsRequest.builder()
.accountId("`111122223333`")
.build();

ListAccessGrantsLocationsResponse listResponse = s3Control.listAccessGrantsLocations(listRequest);
LOGGER.info("ListAccessGrantsLocationsResponse: " + listResponse);
}
```

Response:

```
ListAccessGrantsLocationsResponse(
AccessGrantsLocationsList=[
ListAccessGrantsLocationsEntry(
CreatedAt=`2023-06-07T04:35:11.027Z`,
AccessGrantsLocationId=default,
AccessGrantsLocationArn=arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/location/default,
LocationScope=s3://,
IAMRoleArn=arn:aws:iam::`111122223333`:role/`accessGrantsTestRole`
),
ListAccessGrantsLocationsEntry(
CreatedAt=`2023-06-07T04:35:10.027Z`,
AccessGrantsLocationId=`635f1139-1af2-4e43-8131-a4de006eb456`,
AccessGrantsLocationArn=arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/location/`635f1139-1af2-4e43-8131-a4de006eb888`,
LocationScope=s3://`amzn-s3-demo-bucket/prefixA*`,
IAMRoleArn=arn:aws:iam::`111122223333`:role/`accessGrantsTestRole`
)
]
)
```
