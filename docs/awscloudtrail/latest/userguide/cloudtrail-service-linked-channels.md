# Viewing service-linked channels

AWS services can create a service-linked channel to receive CloudTrail events on your
behalf. The AWS service creating the service-linked channel configures advanced event
selectors for the channel and specifies whether the channel applies to all
AWS Regions, or a single AWS Region.

###### Topics

- [Viewing service-linked channels by
  using the console](#viewing-service-linked-channels-console "#viewing-service-linked-channels-console")
- [Viewing service-linked channels by
  using the AWS CLI](#viewing-service-linked-channels-cli "#viewing-service-linked-channels-cli")

## Viewing service-linked channels by

using the console

Using the CloudTrail console, you can view information about any CloudTrail service-linked channels created by AWS services. The table is empty if your account does not have any service-linked channels.

Use the following procedure to view information about a service-linked channel.

1. Choose **Settings** in the left navigation pane of the CloudTrail console.
2. From **Service-linked channels**, choose a service-linked channel to view its details.
3. On the details page, review the configured settings for the service-linked channel.

You can view the following information on the details page.

    * **Channel name** - The full name of the channel. The channel name format is `aws-service-channel/`AWS_service_name`/slc`
     where ``AWS_service_name`` represents the name of the AWS service that manages the channel.
    * **Channel ARN** - The ARN of the channel, which you can use in a API request to get details about the channel.
    * **All regions** - The value is `Yes` if the channel is configured for all AWS Regions.
    * **AWS service** - The name of the AWS service managing the channel.
    * **Management events** - Shows any management events configured for the channel.
    * **Data events** - Shows any data events configured for the channel.

## Viewing service-linked channels by

using the AWS CLI

Using the AWS CLI, you can view information about any CloudTrail service-linked channels created by AWS services.

###### Topics

- [Get a CloudTrail service-linked channel](#get-slc "#get-slc")
- [List all CloudTrail service-linked channels](#view-all-slc "#view-all-slc")
- [AWS service events on service-linked channels](#slc-service-events "#slc-service-events")

### Get a CloudTrail service-linked channel

The following example AWS CLI command returns information about a specific CloudTrail service-linked channel, including
the name of the destination AWS service, any advanced selectors configured for the channel,
and whether the channel applies to all Regions or a single Region.

You must specify an ARN or the ID suffix of an ARN for `--channel`.

```
aws cloudtrail get-channel --channel EXAMPLE-ee54-4813-92d5-999aeEXAMPLE

```

The following is an example response. In this example, `AWS_service_name` represents the name of the AWS service that created the channel.

```
{
    "ChannelArn": "arn:aws:cloudtrail:us-east-1:111122223333:channel/EXAMPLE-ee54-4813-92d5-999aeEXAMPLE",
    "Name": "aws-service-channel/AWS_service_name/slc",
    "Source": "CloudTrail",
    "SourceConfig": {
        "ApplyToAllRegions": false,
        "AdvancedEventSelectors": [
            {
                "Name": "Management Events Only",
                "FieldSelectors": [
                    {
                        "Field": "eventCategory",
                        "Equals": [
                            "Management"
                        ]
                    }
                ]
            }
        ]
    },
    "Destinations": [
        {
            "Type": "AWS_SERVICE",
            "Location": "AWS_service_name"
        }
    ]
}

```

### List all CloudTrail service-linked channels

The following example AWS CLI command returns information about all CloudTrail service-linked
channels that were created on your behalf. Optional parameters include
`--max-results`, to specify a maximum number of results that you want the command
to return on a single page. If there are more results than your specified
`--max-results` value, run the command again adding the returned
`NextToken` value to get the next page of results.

```
aws cloudtrail list-channels

```

The following is an example response. In this example, `AWS_service_name` represents the name of the AWS service that created the channel.

```
{
    "Channels": [
        {
            "ChannelArn": "arn:aws:cloudtrail:us-east-1:111122223333:channel/EXAMPLE-ee54-4813-92d5-999aeEXAMPLE",
            "Name": "aws-service-channel/AWS_service_name/slc"
        }
    ]
}

```

### AWS service events on service-linked channels

The AWS service managing the service-linked channel can initiate actions on the service-linked channel (for example, creating or updating a service-linked channel). CloudTrail logs these actions as [AWS service events](non-api-aws-service-events.md "non-api-aws-service-events.md"), and delivers these events to the
**Event history**, and any active trails and event data stores
configured for management events. For these events, the `eventType` field is
`AwsServiceEvent`.

The following is an example log file entry of an AWS service event for creation of a
service-linked channel.

```
{
   "eventVersion":"1.08",
   "userIdentity":{
      "accountId":"111122223333",
      "invokedBy":"AWS Internal"
   },
   "eventTime":"2022-08-18T17:11:22Z",
   "eventSource":"cloudtrail.amazonaws.com",
   "eventName":"CreateServiceLinkedChannel",
   "awsRegion":"us-east-1",
   "sourceIPAddress":"AWS Internal",
   "userAgent":"AWS Internal",
   "requestParameters":null,
   "responseElements":null,
   "requestID":"564f004c-EXAMPLE",
   "eventID":"234f004b-EXAMPLE",
   "readOnly":false,
   "resources":[
      {
         "accountId":"184434908391",
         "type":"AWS::CloudTrail::Channel",
         "ARN":"arn:aws:cloudtrail:us-east-1:111122223333:channel/7944f0ec-EXAMPLE"
      }
   ],
   "eventType":"AwsServiceEvent",
   "managementEvent":true,
   "recipientAccountId":"111122223333",
   "eventCategory":"Management"
}

```
