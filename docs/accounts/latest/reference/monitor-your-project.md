# Monitor your project

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

## Monitor your project using AWS CloudTrail

Your project is integrated with AWS CloudTrail, a service that provides a record of
actions taken by a team member or AWS service. CloudTrail captures all API calls for your
project as events. The calls captured include calls from the console and API operations for
all supported AWS services. Using the information collected by CloudTrail, you can determine
the request that was made to your project, the person who made the request, when it was
made, and additional details.

## Use CloudTrail to see who modified your project

This tutorial is for users that are comfortable with the AWS CLI. If you share your
project with multiple team members, you can use CloudTrail to view who modified any
resources in your project. Every action taken by you or team members when they use AWS
Settings or the AWS Management Console to access your project is logged by the
`onBehalfOf` parameter. This parameter shows a user ID and an identity store ID.
Together, these values define a builder ID that you've invited to access your
project.

To find the `onBehalfOf` parameter and connect it to a team member, you'll
need access to the AWS CLI and the AWS Management Console. If you don't have the AWS CLI configured, you can
use AWS CloudShell to access a browser-based, pre-authenticated shell that you can launch
directly from the AWS Management Console and run AWS CLI commands.

### Step 1. To find an AWS CloudTrail Event

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Event history**. You see a
   filtered list of events, with the most recent events showing first. Choose an
   event.
3. In the event record, you'll see the following content:

```
"onBehalfOf": {
            "userId": "00000-e00f-000-000-0000000",
            "identityStoreArn": "arn:aws:identitystore::111122223333:identitystore/000000-0000-0000-0000-60000007"
}
```

This is the identity that defines the team member who created the CloudTrail
event.

### Step 2. To connect the onBehalfOf parameter to a team member

To connect the `onBehalfOf` parameter to a team member using the
AWS CLI:

###### To use the AWS CLI in your terminal

1. Run the following command to sign in to the AWS CLI. You can find your Region using
   [AWS Regions for your projects](project-regions.md "project-regions.md").

```
aws login --region `project-region`
```

2. Run the following command to get the ID for your identity store. The CloudTrail
   event shows the identity store ARN, but does not indicate the identity store ID. You
   always use the AWS Region `us-east-1` when finding the ID for your
   identity store.

```
aws sso-admin list-instances --region us-east-1
```

The output will look like the following:

```
{
    "Instances": [
        {
            "InstanceArn": "arn:aws:sso:::instance/ssoins-0000000000",
            "IdentityStoreId": "d-000000",
            "OwnerAccountId": "111122223333",
            "CreatedDate": "2025-10-26T23:10:58.529000+00:00",
            "Status": "ACTIVE",
            "PrimaryRegion": "us-east-1",
            "Regions": [
                {
                    "RegionName": "us-east-1",
                    "Status": "ACTIVE",
                    "AddedDate": "2025-10-26T23:10:58.529000+00:00",
                    "IsPrimaryRegion": true
                }
            ]
        }
    ]
}
```

You want to copy the identity store ID. In this case, the identity store ID is
`d-000000`. 3. Run the following command to describe the team member who corresponds to the
`onBehalfOf` parameter.

```
aws identitystore describe-user --user-id 00000-e00f-000-000-0000000 --region us-east-1 --identity-store-id d-000000
```

The output will look like the following:

```
{
    "IdentityStoreId": "d-000000",
    "UserId": "00000-e00f-000-000-0000000",
    "UserName": "carlos_salazar",
    "Name": {
        "FamilyName": "Salazar",
        "GivenName": "Carlos"
    },
    "DisplayName": "Carlos",
    "Emails": [
        {
            "Value": "carlos_salazar@example.com",
            "Type": "work",
            "Primary": true
        }
    ],
    "UserStatus": "ENABLED",
    "CreatedAt": "2025-10-26T23:15:27.213000+00:00",
    "CreatedBy": "00000000000",
    "UpdatedAt": "2025-10-26T23:18:55.432000+00:00",
    "UpdatedBy": "0000000000"
}
```

Your team member's display name and emails are provided in this output.

To connect the `onBehalfOf` parameter to a team member using AWS
CloudShell, log into the AWS Management Console and access CloudShell. For more information, see [Getting
started with AWS CloudShell](../../../cloudshell/latest/userguide/getting-started.md#start-session "../../../cloudshell/latest/userguide/getting-started.md#start-session"). You will automatically have the correct IAM
permissions to access CloudShell.
