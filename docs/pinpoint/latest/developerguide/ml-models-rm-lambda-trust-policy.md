**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Assign a Lambda function policy to authorize Amazon Pinpoint to process recommendation data

Before you can use your Lambda function to process recommendation data, you must authorize
Amazon Pinpoint to invoke the function. To grant invocation permission, assign a Lambda function policy
to the function. A _Lambda function policy_ is a
resource-based permissions policy that designates which entities can use a function and what
actions those entities can take. For more information, see [Using Resource-Based Policies for
AWS Lambda](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md") in the _AWS Lambda Developer Guide_.

The following example policy allows the Amazon Pinpoint service principal to use the
`lambda:InvokeFunction` action for a particular Amazon Pinpoint campaign
(`campaignId`) in a particular Amazon Pinpoint project
(`projectId`):

```
{
  "Sid": "`sid`",
  "Effect": "Allow",
  "Principal": {
    "Service": "pinpoint.us-east-1.amazonaws.com"
  },
  "Action": "lambda:InvokeFunction",
  "Resource": "{arn:aws:lambda:us-east-1:`accountId`:function:`function-name`}",
  "Condition": {
    "ArnLike": {
      "AWS:SourceArn": "arn:aws:mobiletargeting:us-east-1:`accountId`:recommenders/*"
    }
  }
}
```

The function policy requires a `Condition` block that includes an
`AWS:SourceArn` key. This key specifies which resource is allowed to invoke the
function. In the preceding example, the policy allows one particular campaign to invoke the
function.

You can also write a policy that allows the Amazon Pinpoint service principal to use the
`lambda:InvokeFunction` action for all the campaigns and journeys in a specific
Amazon Pinpoint project (`projectId`). The following example policy shows
this:

```
{
  "Sid": "`sid`",
  "Effect": "Allow",
  "Principal": {
    "Service": "pinpoint.us-east-1.amazonaws.com"
  },
  "Action": "lambda:InvokeFunction",
  "Resource": "{arn:aws:lambda:us-east-1:`accountId`:function:`function-name`}",
  "Condition": {
    "ArnLike": {
      "AWS:SourceArn": "arn:aws:mobiletargeting:us-east-1:`accountId`:recommenders/*"
    }
  }
}
```

Unlike the first example, the `AWS:SourceArn` key in the `Condition`
block of this example allows one particular project to invoke the function. This permission
applies to all the campaigns and journeys in the project.

To write a more generic policy, you can use a multicharacter match wildcard (\*). For
example, you can use the following `Condition` block to allow any Amazon Pinpoint project to
invoke the function:

```
"Condition": {
  "ArnLike": {
    "AWS:SourceArn": "arn:aws:mobiletargeting:us-east-1:`accountId`:recommenders/*"
  }
}
```

If you want to use the Lambda function with all the projects for your Amazon Pinpoint account, we
recommend that you configure the `Condition` block of the policy in the preceding
way. However, as a best practice, you should create policies that include only the permissions
that are required to perform a specific action on a specific resource.
