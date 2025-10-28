**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Grant Amazon Pinpoint

permission to invoke the Lambda function

You can use the AWS Command Line Interface (AWS CLI) to add permissions to the Lambda function policy
assigned to your Lambda function. To allow Amazon Pinpoint to invoke a function, use the Lambda
[add-permission](../../../cli/latest/reference/lambda/add-permission.md "../../../cli/latest/reference/lambda/add-permission.md")
command, as shown by the following example:

```
`aws lambda add-permission \``--function-name `myFunction` \``--statement-id sid0 \``--action lambda:InvokeFunction \``--principal pinpoint.`us-east-1`.amazonaws.com \``--source-arn arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/*``--source-account `111122223333``

```

In the preceding command, do the following:

- Replace `myFunction` with the name of the Lambda
  function.
- Replace `us-east-1` with the AWS Region where
  you use Amazon Pinpoint.
- Replace `111122223333` with your AWS
  account ID.
  When you run the `add-permission` command, Lambda returns the
  following output:

```
`{
 "Statement": "{\"Sid\":\"sid\",
 \"Effect\":\"Allow\",
 \"Principal\":{\"Service\":\"pinpoint.us-east-1.amazonaws.com\"},
 \"Action\":\"lambda:InvokeFunction\",
 \"Resource\":\"arn:aws:lambda:us-east-1:111122223333:function:myFunction\",
 \"Condition\":
 {\"ArnLike\":
 {\"AWS:SourceArn\":
 \"arn:aws:mobiletargeting:us-east-1:111122223333:apps/*\"}},
 {\"StringEquals\":
 {\"AWS:SourceAccount\":
 \"111122223333\"}}}
}`
```

The `Statement` value is a JSON string version of the statement added
to the Lambda function policy.

## Further

restricting the execution policy

You can modify the execution policy by restricting it to a specific Amazon Pinpoint
project. To do this, replace the `*` in the preceding example with
the unique ID of the project. You can further restrict the policy by limiting it
to a specific campaign. For example, to restrict the policy to only allow a
campaign with the campaign ID `95fee4cd1d7f5cd67987c1436example` in a
project with the project ID `dbaf6ec2226f0a9a8615e3ea5example`, use
the following value for the `source-arn` attribute:

```
arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/dbaf6ec2226f0a9a8615e3ea5example/campaigns/95fee4cd1d7f5cd67987c1436example
```

###### Note

If you do restrict execution of the Lambda function to a specific campaign,
you first have to create the function with a less restrictive policy. Next,
you have to create the campaign in Amazon Pinpoint and choose the function. Finally,
you have to update the execution policy to refer to the specified
campaign.
