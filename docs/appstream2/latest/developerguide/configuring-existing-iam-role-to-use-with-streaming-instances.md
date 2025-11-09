# Configuring an Existing IAM Role to Use With WorkSpaces Applications Streaming Instances

This topic describes how to configure an existing IAM role so that you can use it with image builders and fleet streaming instances.

**Prerequisites**

The IAM role that you want to use with an WorkSpaces Applications image builder or fleet streaming instance must meet the following prerequisites:

- The IAM role must be in the same Amazon Web Services account as the WorkSpaces Applications streaming instance.
- The IAM role cannot be a service role.
- The trust relationship policy that is attached to the IAM role must include the WorkSpaces Applications service as the principal. A _principal_ is an entity in AWS that can perform actions and access resources. The policy must also include the
  `sts:AssumeRole` action. This policy configuration defines WorkSpaces Applications as a trusted entity.
- If you are applying the IAM role to an image builder, the image builder must run a version
  of the WorkSpaces Applications agent released on or after September 3, 2019. If you are
  applying the IAM role to a fleet, the fleet must use an image that uses a
  version of the agent released on or after the same date. For more
  information, see [WorkSpaces Applications Agent Release Notes](agent-software-versions.md "agent-software-versions.md").

###### To enable the WorkSpaces Applications service principal to assume an existing IAM role

To perform the following steps, you must sign into the account as an IAM user who has the permissions required to list and update IAM roles. If you don't have the required permissions, ask your Amazon Web Services account administrator either to perform these steps in your account or to grant you the required permissions.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. In the list of roles in your account, choose the name of the role that you want to modify.
4. Choose the **Trust relationships** tab, and then choose **Edit trust relationship**.
5. Under **Policy Document**, verify that the trust relationship policy includes the `sts:AssumeRole` action for the `appstream.amazonaws.com` service principal:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "appstream.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

6. When you are finished editing your trust policy, choose **Update Trust Policy** to save your changes.
7. The IAM role that you selected will display in the WorkSpaces Applications console. This role grants permissions to applications and scripts to perform API actions and management tasks on streaming instances.
