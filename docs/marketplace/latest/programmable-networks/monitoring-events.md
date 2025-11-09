# Monitoring AWS Programmable Networks events in Amazon EventBridge

You can monitor AWS Programmable Networks events in EventBridge, which delivers a stream of real-time data from
your own applications, software-as-a-service (SaaS) applications, and AWS services. EventBridge
routes that data to targets such as AWS Lambda and Amazon Simple Notification Service. These events are the same as
those that appear in Amazon CloudWatch Events, which delivers a near real-time stream of system events that
describe changes in AWS resources.

The following examples show events for AWS Programmable Networks.

###### Topics

- [eventName event](#eventName "#eventName")

## eventName event

In this example event, .

```
{
   "version": "0",
   "id": "01234567-EXAMPLE",
   "detail-type": "ServiceName ResourceType State Change",
   "source": "aws.servicename",
   "account": "123456789012",
   "time": "2019-06-12T10:23:43Z",
   "region": "us-east-2",
   "resources": [
     "arn:aws:servicename:us-east-2:123456789012:resourcename"
   ],
   "detail": {
     "event": "eventName",
     "detailOne": "something",
     "detailTwo": "12345678-1234-5678-abcd-12345678abcd",
     "detailThree": "something",
     "detailFour": "something"
   }
}
```
