# Managing S3 Intelligent-Tiering

The S3 Intelligent-Tiering storage class delivers automatic storage cost savings in three
low-latency and high-throughput access tiers. It also offers optional archive capabilities
to help you get the lowest storage costs in the cloud for data that can be accessed in
minutes to hours.

## Identifying which

S3 Intelligent-Tiering access tier objects are stored in

To get a list of your objects and their corresponding metadata, including their
S3 Intelligent-Tiering access tier, you can use [Amazon S3 Inventory](storage-inventory.md "storage-inventory.md"). S3
Inventory provides CSV, ORC, or Parquet output files that list your
objects and their corresponding metadata. You can receive these inventory reports on
either a daily or weekly basis for an Amazon S3 bucket or a shared prefix. (_Shared prefix_ refers to objects that have names that begin
with a common string.)

## Viewing the archive status of an object within

S3 Intelligent-Tiering

To receive notice when an object within the S3 Intelligent-Tiering storage class has
moved to either the Archive Access tier or the Deep Archive Access tier, you can set up
S3 Event Notifications. For more information, see [Enabling event notifications](how-to-enable-disable-notification-intro.md "how-to-enable-disable-notification-intro.md").

Amazon S3 can publish event notifications to an Amazon Simple Notification Service (Amazon SNS) topic, an Amazon Simple Queue Service (Amazon SQS) queue, or an
AWS Lambda function. For more information, see [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md").

The following is an example of a message that Amazon S3 sends to publish an
`s3:IntelligentTiering` event. For more information, see [Event message structure](notification-content-structure.md "notification-content-structure.md").

```
{
   "Records":[
      {
         "eventVersion":"2.3",
         "eventSource":"aws:s3",
         "awsRegion":"us-west-2",
         "eventTime":"1970-01-01T00:00:00.000Z",
         "eventName":"IntelligentTiering",
         "userIdentity":{
            "principalId":"s3.amazonaws.com"
         },
         "requestParameters":{
            "sourceIPAddress":"s3.amazonaws.com"
         },
         "responseElements":{
            "x-amz-request-id":"C3D13FE58DE4C810",
            "x-amz-id-2":"FMyUVURIY8/IgAtTv8xRjskZQpcIZ9KG4V5Wp6S7S/JRWeUWerMUE5JgHvANOjpD"
         },
         "s3":{
            "s3SchemaVersion":"1.0",
            "configurationId":"testConfigRule",
            "bucket":{
               "name":"`amzn-s3-demo-bucket`",
               "ownerIdentity":{
                  "principalId":"A3NL1KOZZKExample"
               },
               "arn":"arn:aws:s3:::`amzn-s3-demo-bucket`"
            },
            "object":{
               "key":"HappyFace.jpg",
               "size":1024,
               "eTag":"d41d8cd98f00b204e9800998ecf8427e",
            }
         },
         "intelligentTieringEventData":{
            "destinationAccessTier": "ARCHIVE_ACCESS"
            }
      }
   ]
}

```

You can also use a [`HEAD` object
request](../API/API_HeadObject.md "../API/API_HeadObject.md") to view an object's archive status. If an object is stored in the
S3 Intelligent-Tiering storage class and is in one of the archive tiers, the
`HEAD` object response shows the current archive tier. To show the
archive tier, the request uses the [x-amz-archive-status](../API/API_HeadObject.md#API_HeadObject_ResponseElements "../API/API_HeadObject.md#API_HeadObject_ResponseElements") header.

The following `HEAD` object request returns the metadata of an object (in
this case, `my-image.jpg`).

```
HEAD /`my-image.jpg` HTTP/1.1
Host: bucket.s3.`region`.amazonaws.com
Date: Wed, 28 Oct 2009 22:32:00 GMT
Authorization: AWS AKIAIOSFODNN7EXAMPLE:02236Q3V0RonhpaBX5sCYVf1bNRuU=
```

You can also use `HEAD` object requests to monitor the status of a
`restore-object` request. If the archive restoration is in progress, the
`HEAD` object response includes the [x-amz-restore](../API/API_HeadObject.md#API_HeadObject_ResponseElements "../API/API_HeadObject.md#API_HeadObject_ResponseElements") header.

The following sample `HEAD` object response shows an object archived by
using S3 Intelligent-Tiering with a restore request in progress.

```
HTTP/1.1 200 OK
x-amz-id-2: FSVaTMjrmBp3Izs1NnwBZeu7M19iI8UbxMbi0A8AirHANJBo+hEftBuiESACOMJp
x-amz-request-id: E5CEFCB143EB505A
Date: Fri, 13 Nov 2020 00:28:38 GMT
Last-Modified: Mon, 15 Oct 2012 21:58:07 GMT
ETag: "1accb31fcf202eba0c0f41fa2f09b4d7"
x-amz-storage-class: 'INTELLIGENT_TIERING'
x-amz-archive-status: 'ARCHIVE_ACCESS'
x-amz-restore: 'ongoing-request="true"'
x-amz-restore-request-date: 'Fri, 13 Nov 2020 00:20:00 GMT'
Accept-Ranges: bytes
Content-Type: binary/octet-stream
Content-Length: 300
Server: AmazonS3
```

## Restoring objects from the

S3 Intelligent-Tiering Archive Access and Deep Archive Access tiers

To access objects in the S3 Intelligent-Tiering Archive Access and Deep Archive Access
tiers, you must initiate a [restore request](restoring-objects.md "restoring-objects.md"), and
then wait until the object is moved into the Frequent Access tier. For more information
about archived objects, see [Working with archived objects](archived-objects.md "archived-objects.md").

When you restore an object from the Archive Access tier or Deep Archive Access tier,
the object moves back into the Frequent Access tier. Afterwards, if the object isn't
accessed for 30 consecutive days, it automatically moves into the Infrequent Access tier.
Then, after a minimum of 90 consecutive days of no access, the object moves into the
Archive Access tier. After a minimum of 180 consecutive days of no access, the object
moves into the Deep Archive Access tier. For more information, see [How S3 Intelligent-Tiering works](intelligent-tiering-overview.md "intelligent-tiering-overview.md").

You can restore an archived object by using the Amazon S3 console, S3 Batch Operations, the Amazon S3
REST API, the AWS SDKs, or the AWS Command Line Interface (AWS CLI). For more information, see [Working with archived objects](archived-objects.md "archived-objects.md").
