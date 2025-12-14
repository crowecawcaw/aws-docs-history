# Virtual meetings with AWS Support

Virtual meetings enable you to connect with AWS Support engineers through video calls with screen sharing capabilities. This feature helps you resolve complex technical issues that require visual demonstration or real-time collaboration.

When a support engineer determines that your case requires visual assistance, they can initiate a virtual meeting. You receive a meeting invitation on your case details page in the AWS Support Center. After you accept the invitation, you join a secure video call where you can share your screen and collaborate with the support engineer.

Virtual meetings integrate with Amazon Connect and use WebRTC technology to provide secure, browser-based video conferencing without requiring additional software installation.

Virtual meetings are available in the [commercial AWS Regions](../../../glossary/latest/reference/glos-chap.md#region "../../../glossary/latest/reference/glos-chap.md#region") only.

###### Topics

- [Join a virtual meeting](#virtual-meetings-join "#virtual-meetings-join")
- [Security and privacy during your virtual meeting](#virtual-meetings-security "#virtual-meetings-security")
- [Required IAM permissions for virtual meetings](#virtual-meetings-iam-permissions "#virtual-meetings-iam-permissions")
- [Troubleshooting virtual meetings](#virtual-meetings-troubleshooting "#virtual-meetings-troubleshooting")

## Join a virtual meeting

Virtual meetings are initiated by the AWS Support engineer assisting you with your support case. To join a virtual meeting, complete the following steps.

1. When a support engineer initiates a virtual meeting, you see a meeting invitation on the **Case details** page in your support case. To join the meeting, choose **Join virtual meeting** to accept the invitation.

Meeting invitations expire after 10 minutes. If you don't join within this time, request a new meeting from your support engineer. 2. Grant browser permissions for camera and microphone access when prompted.

The virtual meeting opens in a new window and you're connected to the support engineer. You can mute and unmute your microphone, or disconnect from the meeting, useing the buttons at the bottom of the screen.

## Security and privacy during your virtual meeting

Virtual meetings use the same authentication and authorization mechanisms as other AWS Support operations. The following security measures protect your meetings:

- **Case ownership validation:** You can only join meetings for cases that belong to your AWS account.
- **AWS Identity and Access Management (IAM) based access control:** You must have the appropriate IAM permissions to join virtual meetings.
- **Encrypted connections:** All meeting data is transmitted over encrypted WebRTC connections.
- **Audit logging:** All meeting activities are logged in AWS CloudTrail for compliance and auditing purposes.

###### Important

Virtual meetings are recorded for quality assurance and training purposes. Don't share sensitive information such as passwords or access keys during the meeting.

## Required IAM permissions for virtual meetings

To join virtual meetings, your IAM user or role must have the following permission:

```

 {
     "Version": "2012-10-17",
     "Statement": [{
         "Effect": "Allow",
         "Action": [
             "support:InitiateLiveContactForCase"
         ],
         "Resource": "*"
     }]
 }
```

For more information about AWS Support permissions, see [Manage access to AWS Support Center](accessing-support.md "accessing-support.md").

## Troubleshooting virtual meetings

**I can't see the meeting invitation.**

Verify that your support engineer has initiated the meeting. Refresh the case details page. If the invitation still doesn't appear, contact your support engineer through the case correspondence.

**The meeting invitation expired.**

Meeting invitations expire after 10 minutes for security reasons. Request a new meeting invitation from your support engineer.

**I'm experiencing connection issues.**

Check your internet connection. Ensure that your firewall or network security settings allow WebRTC traffic. Try using a different browser or network connection.

**I receive an authorization error.**

Verify that your IAM user or role has permissions for the `support:InitiateLiveContactForCase` action.
