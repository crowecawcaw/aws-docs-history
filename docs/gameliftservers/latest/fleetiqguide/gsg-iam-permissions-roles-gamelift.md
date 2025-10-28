# Create a role for Amazon GameLift Servers FleetIQ

This role allows Amazon GameLift Servers FleetIQ to access and modify your Amazon EC2 instances, Auto Scaling groups, and
lifecycle hooks as part of its Spot balancing and automatic scaling activities.

Use the IAM console or the AWS CLI to create a role for Amazon GameLift Servers FleetIQ and attach a managed
policy with the necessary permissions. For more information on IAM roles and managed
policies, see [Creating a Role for an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console "../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console") and [AWS
Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

Console
These steps describe how to create a service role with a managed policy for Amazon GameLift Servers
using the AWS Management Console.

1. Open the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam") and choose
   **Roles: Create role**.
2. For **Select type of trusted entity**, choose **AWS
   service**.
3. For **Choose a use case**, choose
   **GameLift** from the list of services. Under **Select
   your use case**, the appropriate Amazon GameLift Servers use case is automatically
   selected. To continue, choose **Next: Permissions**.
4. The list **Attached permissions policies** should contain one
   policy: **GameLiftGameServerGroupPolicy** . If this policy is not
   shown, check the filters or use the search feature to add it to the role. You can
   view a policy's syntax (choose the ▶ icon to expand), but you cannot change
   the syntax. When the role is created, you can update the role and attach
   additional policies to add or remove permissions.

For **Set permissions boundary**, keep the default setting
(Create role without a permissions boundary). This is an advanced setting that is
not required. To continue, choose **Next: Tags**. 5. **Add tags** is an optional setting for resource management.
For example, you might want to add tags to this role to track project-specific
resource usage by role. To see more information on tagging for IAM roles and
other uses, follow the **Learn more** link. To continue, choose
**Next: Review**. 6. On the **Review** page, make the following changes as needed:

    * Enter a role name and optionally update the description.
    * Verify the following:




    	+ **Trusted entities** is set to "AWS service:
    	 gamelift.amazonaws.com". This value must be updated once the role has been
    	 created.
    	+ **Policies** includes
    	 GameLiftGameServerGroupPolicy.

To complete the task, choose **Create role**. 7. Once the new role has been created, you must manually update the role's trust
relationship. Go to the **Roles** page and choose the new role
name to open its summary page. Open the **Trust relationships**
tab and choose **Edit trust relationship**. In the policy
document, update the `Service` property to include
`autoscaling.amazonaws.com`. The revised `Service`
property should look like this:

```
        "Service": [
          "gamelift.amazonaws.com",
          "autoscaling.amazonaws.com"
        ]
```

To save your change, choose **Update Trust Policy**.

The role is now ready. Take note of the role's ARN value, which is displayed at
the top of the role's summary page. You will need this information when setting up
Amazon GameLift Servers FleetIQ game server groups.

AWS CLI
These steps describe how to create a service role with a managed policy for Amazon GameLift Servers
using the AWS CLI.

1. Create a trust policy file (example:
   `FleetIQtrustpolicyGameLift.json`) with the following JSON
   syntax.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "gamelift.amazonaws.com",
 "autoscaling.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Create a new IAM role with [iam create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") and associate it with the trust policy JSON file that
   you just created.

Windows:

```
AWS iam create-role --role-name FleetIQ-role-for-GameLift --assume-role-policy-document file://C:\policies\FleetIQtrustpolicyGameLift.json
```

Linux:

```
AWS iam create-role --role-name FleetIQ-role-for-GameLift --assume-role-policy-document file://policies/FleetIQtrustpolicyGameLift.json
```

When the request is successful, the response includes the properties of the
newly created role. Take note of the ARN value. You will need this information
when setting up Amazon GameLift Servers FleetIQ game server groups. 3. Use [iam
attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") to attach the managed permissions policy
"GameLiftGameServerGroupPolicy".

```
AWS iam attach-role-policy --role-name FleetIQ-role-for-GameLift --policy-arn arn:aws:iam::aws:policy/GameLiftGameServerGroupPolicy
```

To verify that the permissions policy is attached, call [iam
list-attached-role-policies](../../../cli/latest/reference/iam/list-attached-role-policies.md "../../../cli/latest/reference/iam/list-attached-role-policies.md") with the new role's name.

The role is now ready. You can verify that the IAM role is configured correctly by
calling [gamelift
create-game-server-group](../../../cli/latest/reference/gamelift/create-game-server-group.md "../../../cli/latest/reference/gamelift/create-game-server-group.md") with the `role-arn` property set to the
new role's ARN value. When the `GameServerGroup` enters ACTIVE state, this
indicates that Amazon GameLift Servers FleetIQ is able to modify Amazon EC2 and Auto Scaling resources in your account, as
expected.
