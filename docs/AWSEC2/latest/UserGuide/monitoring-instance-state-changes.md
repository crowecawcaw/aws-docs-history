# State change events for Amazon EC2

instances

Amazon EC2 sends an `EC2 Instance State-change Notification` event to Amazon EventBridge
when the state of an instance changes.

The following is example data for this event. In this example, the instance entered
the `pending` state.

```
{
   "id":"7bf73129-1428-4cd3-a780-95db273d1602",
   "detail-type":"EC2 Instance State-change Notification",
   "source":"aws.ec2",
   "account":"123456789012",
   "time":"2021-11-11T21:29:54Z",
   "region":"us-east-1",
   "resources":[
      "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
   ],
   "detail":{
      "instance-id":"i-1234567890abcdef0",
      "state":"pending"
   }
}

```

The possible values for `state` are:

- `pending`
- `running`
- `stopping`
- `stopped`
- `shutting-down`
- `terminated`
  When you launch or start an instance, it enters the `pending` state and
  then the `running` state. When you stop an instance, it enters the
  `stopping` state and then the `stopped` state. When you
  terminate an instance, it enters the `shutting-down` state and then the
  `terminated` state. For more information, see [Amazon EC2 instance state changes](ec2-instance-lifecycle.md "ec2-instance-lifecycle.md").
