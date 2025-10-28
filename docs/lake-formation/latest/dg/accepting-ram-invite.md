# Accepting a resource share invitation from AWS RAM

If a Data Catalog resource is shared with your AWS account and your account is not in the same
AWS organization as the sharing account, you do not have access to the shared resource until
you accept a resource share invitation from AWS Resource Access Manager (AWS RAM). As a data lake administrator, you
must first query AWS RAM for pending invitations and then accept the invitation.

You can use the AWS RAM console, API, or AWS Command Line Interface (AWS CLI) to view and accept
invitations.

###### To view and accept a resource share invitation from AWS RAM (console)

1. Ensure that you have the required AWS Identity and Access Management (IAM) permissions to view and accept
   resource share invitations.

For information about the suggested IAM policies for data lake administrators, see [Data lake administrator permissions](permissions-reference.md#persona-dl-admin "permissions-reference.md#persona-dl-admin"). 2. Follow the instructions in [Accepting and Rejecting Invitations](../../../ram/latest/userguide/working-with-shared.md#working-with-shared-invitation "../../../ram/latest/userguide/working-with-shared.md#working-with-shared-invitation") in the
_AWS RAM User Guide_.

###### To view and accept a resource share invitation from AWS RAM (AWS CLI)

1. Ensure that you have the required AWS Identity and Access Management (IAM) permissions to view and accept
   resource share invitations.

For information about the suggested IAM policies for data lake administrators, see [Data lake administrator permissions](permissions-reference.md#persona-dl-admin "permissions-reference.md#persona-dl-admin"). 2. Enter the following command to view pending resource share invitations.

```
aws ram get-resource-share-invitations
```

The output should be similar to the following.

```
{
    "resourceShareInvitations": [
        {
            "resourceShareInvitationArn": "arn:aws:ram:us-east-1:111122223333:resource-share-invitation/a93aa60a-1bd9-46e8-96db-a4e72eec1d9f",
            "resourceShareName": "111122223333-123456789012-uswuU",
            "resourceShareArn": "arn:aws:ram:us-east-1:111122223333:resource-share/2a4ab5fb-d859-4751-84f7-8760b35fc1fe",
            "senderAccountId": "111122223333",
            "receiverAccountId": "123456789012",
            "invitationTimestamp": 1589576601.79,
            "status": "PENDING"
        }
    ]
}

```

Note the status of `PENDING`. 3. Copy the value of the `resourceShareInvitationArn` key to the clipboard. 4. Paste the value into the following command, replacing
`<invitation-arn>`, and enter the command.

```
aws ram accept-resource-share-invitation --resource-share-invitation-arn `<invitation-arn>`
```

The output should be similar to the following.

```
{
    "resourceShareInvitations": [
        {
            "resourceShareInvitationArn": "arn:aws:ram:us-east-1:111122223333:resource-share-invitation/a93aa60a-1bd9-46e8-96db-a4e72eec1d9f",
            "resourceShareName": "111122223333-123456789012-uswuU",
            "resourceShareArn": "arn:aws:ram:us-east-1:111122223333:resource-share/2a4ab5fb-d859-4751-84f7-8760b35fc1fe",
            "senderAccountId": "111122223333",
            "receiverAccountId": "123456789012",
            "invitationTimestamp": 1589576601.79,
            "status": "ACCEPTED"
        }
    ]
}

```

Note the status of `ACCEPTED`.
