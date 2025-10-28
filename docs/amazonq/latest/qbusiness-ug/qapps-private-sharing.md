# Sharing Amazon Q Apps

Amazon Q Apps allows you to privately share your Q Apps with specific users within
your Q Business application environment. This private sharing capability enables app
creators to restrict app access to select users, providing more granular control over
app visibility and usage within organizations.

## Benefits

- **Controlled Access**: Share your Q Apps with
  only the intended users, maintaining privacy and security.
- **Run-Only Mode**: Shared users can view and
  run the Q App but cannot make structural changes. To make structural
  changes, they will first need to duplicate it, which creates their separate,
  editable copy of the Q App.

## Key Concepts

- Owner: The owner is the user who creates and has full editing rights over
  the Q App. As the owner, you can:
  - Privately share the Q App with other users by full email
    address.
  - Revoke access for shared users.
  - Edit the category for the shared Q App, which affects where it
    appears in the shared app user's library.

- App User: A shared app user is a user within your organization's Q
  Business environment that the owner has shared the Q App with by email. As a
  shared user, you can:
  - View and run the shared Q App.
  - Duplicate the Q App to create an editable version.
  - Cannot directly edit the original shared Q App.

Shared users do not receive a notification when a Q App is shared with them. You
need to send them the link from the share modal.

## Prerequisites for Private Sharing

Before your web experience users can use sharing you will need to update the web
experience IAM role to enable private sharing in the web experience. We recommend
updating the `DescribeQAppPermissions`
`UpdateQAppPermissions` statement of the IAM policy attached to this role
to include the action as follows:

```

{
    "Sid": "QAppsAppOwnerPermissions",
    "Effect": "Allow",
    "Action": [
        "qapps:GetQApp",
        "qapps:CopyQApp",
        "qapps:UpdateQApp",
        "qapps:DeleteQApp",
        "qapps:ImportDocument",
        "qapps:ImportDocumentToQApp",
        "qapps:CreateLibraryItem",
        "qapps:UpdateLibraryItem",
        "qapps:StartQAppSession",
        "qapps:DescribeQAppPermissions",
        "qapps:UpdateQAppPermissions"
    ],
    "Resource": "arn:aws:qapps:{{region}}:{{source_account}}:application/{{application_id}}/qapp/*",
    "Condition": {
        "StringEqualsIgnoreCase": {
            "qapps:UserIsAppOwner": "true"
        }
    }
}

{
    "Sid": "QAppsPublishedAppPermissions",
    "Effect": "Allow",
    "Action": [
        "qapps:GetQApp",
        "qapps:CopyQApp",
        "qapps:AssociateQAppWithUser",
        "qapps:GetLibraryItem",
        "qapps:CreateLibraryItemReview",
        "qapps:AssociateLibraryItemReview",
        "qapps:DisassociateLibraryItemReview",
        "qapps:StartQAppSession",
        "qapps:DescribeQAppPermissions"
    ],
    "Resource": "arn:aws:qapps:{{region}}:{{source_account}}:application/{{application_id}}/qapp/*",
    "Condition": {
        "StringEqualsIgnoreCase": {
            "qapps:AppIsPublished": "true"
        }
    }
}

```

### Sharing Amazon Q Apps

Web Experience

###### To privately share your Q App

1. Open the Q App you want to share.
2. Choose on the "Share" button in the top right
   corner.
3. In the share modal, enter the email addresses of the users
   you want to share with, or you can toggle ‘Share with all’
   to give access to everyone in your Q Apps organization.
4. Edit the category(s) for the shared Q App, which affects
   where it appears in the shared user's library.
5. (Optional) Choose the copy icon to obtain the link; this
   can then be sent to shared users via your preferred method
   (e.g., email or Slack).
6. Choose "Share" to complete the sharing process.

The shared users will now be able to access and run your Q App
from the library or via the shareable link you provide them.

AWS CLI
To privately share your Q App with AWS CLI, use the
`DescribeQAppPermissions` command.

```

aws qapps describe-q-app-permissions \
            --instance-id `instanceId` \
            --app-id `appId`

```

## Managing Shared Users

As the owner, you can manage who has access to your shared Q App by revisiting
the share modal:

Web Experience

1. To revoke access, choose the "Remove" button next to the
   user's email address.
2. To grant access to new users, enter their email
   addresses.
3. Choose "Share" to apply the changes.

AWS CLI
To manage share user access with AWS CLI, use
`UpdateQAppPermissions`.

```

aws qapps update-q-app-permissions \
            --instance-id `instanceId` \
            --app-id `appId` \
            --grant-permissions `listOfPermissions to be granted` \
            --revoke-permissions `listOfPermissions to be revoked` \

```
