# Event message structure

The notification message that Amazon S3 sends to publish an event is in the JSON
 format.

For a general overview and instructions on configuring event notifications, see [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md").

This example shows *version 2.1* of the event notification JSON
 structure. Amazon S3 uses *versions 2.1*, *2.2*, and *2.3* of this event structure. Amazon S3 uses
 version 2.2 for cross-Region replication event notifications. It uses version 2.3 for S3 Lifecycle,
 S3 Intelligent-Tiering, object ACL, object tagging, and object restoration delete events. These
 versions contain extra information specific to these operations. Versions 2.2 and 2.3 are otherwise
 compatible with version 2.1, which Amazon S3 currently uses for all other event notification types.


```
{  
   "Records":[  
      {  
         "eventVersion":"2.1",
         "eventSource":"aws:s3",
         "awsRegion":"us-west-2",
         "eventTime":"`The time, in ISO-8601 format (for example, 1970-01-01T00:00:00.000Z) when Amazon S3 finished processing the request`",
         "eventName":"`The event type`",
         "userIdentity":{  
            "principalId":"`The unique ID of the IAM resource that caused the event`"
         },
         "requestParameters":{  
            "sourceIPAddress":"`The IP address where the request came from`"
         },
         "responseElements":{  
            "x-amz-request-id":"`The Amazon S3 generated request ID`",
            "x-amz-id-2":"`The Amazon S3 host that processed the request`"
         },
         "s3":{  
            "s3SchemaVersion":"1.0",
            "configurationId":"`The ID found in the bucket notification configuration`",
            "bucket":{  
               "name":"`The name of the bucket, for example,` ``amzn-s3-demo-bucket``",
               "ownerIdentity":{  
                  "principalId":"`The Amazon retail customer ID of the bucket owner`"
               },
               "arn":"`The bucket Amazon Resource Name (ARN)`"
            },
            "object":{  
               "key":"`The object key name`",
               "size":"`The object size in bytes (as a number)`",
               "eTag":"`The object entity tag (ETag)`",
               "versionId":"`The object version if the bucket is versioning-enabled; null or not present if the bucket isn't versioning-enabled`",
               "sequencer": "`A string representation of a hexadecimal value used to determine event sequence; only used with PUT and DELETE requests`"
            }
         },
         "glacierEventData": {
            "restoreEventData": {
               "lifecycleRestorationExpiryTime": "`The time, in ISO-8601 format (for example, 1970-01-01T00:00:00.000Z), when the temporary copy of the restored object expires`",
               "lifecycleRestoreStorageClass": "`The source storage class for restored objects`"
            }
         }
      }
   ]
}
```
Note the following about the event message structure:


* The `eventVersion` key value contains a major and minor version in the form
 ``major``.``minor``.


The major version is incremented if Amazon S3 makes a change to the event structure
 that's not backward compatible. This includes removing a JSON field that's
 already present or changing how the contents of a field are represented (for
 example, a date format).


The minor version is incremented if Amazon S3 adds new fields to the event structure. This
 might occur if new information is provided for some or all existing events. This might also occur
 if new information is provided only for newly introduced event types. To stay compatible with new
 minor versions of the event structure, we recommend that your applications ignore new
 fields.


If new event types are introduced, but the structure of the event is otherwise
 unmodified, the event version doesn't change.


To ensure that your applications can parse the event structure correctly, we
 recommend that you do an equal-to comparison on the major version number. To
 ensure that the fields that are expected by your application are present, we
 also recommend doing a greater-than-or-equal-to comparison on the minor
 version.
* The `eventName` key value references the list of [event
 notification types](notification-how-to-event-types-and-destinations.md "notification-how-to-event-types-and-destinations.md") but doesn't contain the `s3:` prefix.
* The `userIdentity` key value references the unique ID of the AWS Identity and Access Management (IAM)
 resource (a user, role, group, and so on) that caused the event. For a definition of each IAM
 identification prefix (for example, AIDA, AROA, AGPA) and information about how to get the unique
 identifier, see [Unique identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html##identifiers-unique-ids "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html##identifiers-unique-ids") in the *IAM User Guide*.
* The `responseElements` key value is useful if you want to trace a request by
 following up with AWS Support. Both `x-amz-request-id` and `x-amz-id-2` help
 Amazon S3 trace an individual request. These values are the same as those that Amazon S3 returns in the
 response to the request that initiates the events. Therefore, you can use these values to match
 the event to the request.
* The `s3` key value provides information about the bucket and object involved
 in the event. The object key name value is URL encoded. For example, `red flower.jpg`
 becomes `red+flower.jpg`. (Amazon S3 returns
 "`application/x-www-form-urlencoded`" as the content type in the response.)


The `ownerIdentity` key value corresponds to the Amazon retail (Amazon.com)
 customer ID of the bucket owner. This ID value is no longer used and is maintained only for
 backward compatibility.
* The `sequencer` key value provides a way to determine the sequence of events.
 Event notifications aren't guaranteed to arrive in the same order that the events occurred.
 However, notifications from events that create objects (`PUT` requests) and delete
 objects contain a `sequencer`. You can use this value to determine the order of events
 for a given object key. 


If you compare the `sequencer` strings from two event notifications
 on the same object key, the event notification with the greater
 `sequencer` hexadecimal value is the event that occurred later.
 If you're using event notifications to maintain a separate database or index of
 your Amazon S3 objects, we recommend that you compare and store the
 `sequencer` values as you process each event notification. 


Note the following:




	+ You can't use the `sequencer` key value to determine the order for
	 events on different object keys.
	+ The `sequencer` strings can be of different lengths. So, to compare
	 these values, first left-pad the shorter value with zeros, and then do a lexicographical
	 comparison.
* The `glacierEventData` key value is only visible for
 `s3:ObjectRestore:Completed` events.
* The `restoreEventData` key value contains attributes that are related to your
 restore request.
* The `replicationEventData` key value is only visible for replication
 events.
* The `intelligentTieringEventData` key value is only visible for
 S3 Intelligent-Tiering events.
* The `lifecycleEventData` key value is only visible for S3 Lifecycle transition
 events.

## Example messages


The following are examples of Amazon S3 event notification messages.


###### Amazon S3 test message


After you configure an event notification on a bucket, Amazon S3 sends the
 following test message.



```
{  
   "Service":"Amazon S3",
   "Event":"s3:TestEvent",
   "Time":"2014-10-13T15:57:02.089Z",
   "Bucket":"``amzn-s3-demo-bucket``",
   "RequestId":"5582815E1AEA5ADF",
   "HostId":"8cLeGAmw098X5cv4Zkwcmo8vvZa3eH3eKxsPzbB9wrR+YstdA6Knx4Ip8EXAMPLE"
}
```

###### Note

The `s3:TestEvent` message uses a different format than regular S3 event
 notifications. Unlike other event notifications that use the `Records` array structure
 shown earlier, the test event uses a simplified format with direct fields. When implementing event
 handling, ensure your code can distinguish between and properly handle both message
 formats.


###### Example message when an object is created using a `PUT` request


The following is an example of a message that Amazon S3 sends to publish an
 `s3:ObjectCreated:Put` event.



```
{  
   "Records":[  
      {  
         "eventVersion":"2.1",
         "eventSource":"aws:s3",
         "awsRegion":"us-west-2",
         "eventTime":"1970-01-01T00:00:00.000Z",
         "eventName":"ObjectCreated:Put",
         "userIdentity":{  
            "principalId":"AIDAJDPLRKLG7UEXAMPLE"
         },
         "requestParameters":{  
            "sourceIPAddress":"172.16.0.1"
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
               "versionId":"096fKKXTRTtl3on89fVO.nfljtsv6qko",
               "sequencer":"0055AED6DCD90281E5"
            }
         }
      }
   ]
}

```
