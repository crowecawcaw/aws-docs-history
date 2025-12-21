AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Moving to just-in-time node access from Session Manager

When you enable just-in-time node access, Systems Manager doesn't make any changes to your
existing resources for Session Manager. This ensures there's no disruption to your existing
environment and users can continue to start sessions while you create and validate
approval policies. Once you're ready to test your approval policies, you must modify
your existing IAM policies to complete the transition to just-in-time node access.
This includes adding the required permissions for just-in-time node access to
identities, and removing permission for the `StartSession` API operation for
Session Manager. We recommend testing approval policies with a subset of identities and nodes
in an AWS account and AWS Region.

For more information about the permissions required for just-in-time node access, see
[Setting up
just-in-time access with Systems Manager](systems-manager-just-in-time-node-access-setting-up.md "systems-manager-just-in-time-node-access-setting-up.md").

For more information about modifying and identity's IAM permissions, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the
_IAM User Guide_.

The following describes a detailed method of how you can move to just-in-time node
access from Session Manager.

Moving from Session Manager to just-in-time node access requires careful planning
and testing to ensure a smooth transition without disrupting your operations. The
following sections describe how you can complete this process.

## Prerequisites

Before you begin, ensure that you have completed the following tasks:

- Set up the Systems Manager unified console.
- Verified you have permissions to modify IAM policies in your
  account.
- Identified all IAM policies and roles that currently grant Session Manager
  permissions.
- Documented your current Session Manager configuration, including session
  preferences and logging settings.

## Assessment

Assess your current environment and outline desired approval behaviors by
completing the following tasks:

1. **Inventory your nodes** - Identify all
   nodes that users currently access through Session Manager.
2. **Identify user access patterns** -
   Document which users or roles need access to which nodes, and under what
   circumstances.
3. **Map approval workflows** - Determine
   who should approve access requests for different types of nodes.
4. **Review tagging strategy** - Ensure your
   nodes are properly tagged to support your planned approval
   policies.
5. **Audit existing IAM policies** -
   Identify all policies that include Session Manager permissions.

## Planning

### Phased strategy

When moving from Session Manager to just-in-time node access, we recommend using
a phased approach like the following:

1. **Phase 1: Setup and configuration**

- Enable just-in-time node access without modifying existing
  Session Manager permissions.

2. **Phase 2: Policy development** -
   Create and test approval policies for your nodes.
3. **Phase 3: Pilot migration** - Modify
   a small group of non-critical nodes and users or roles from Session Manager
   to just-in-time node access.
4. **Phase 4: Full migration** -
   Gradually migrate all remaining nodes and users or roles.

### Timeline considerations

Consider the following factors when creating your timeline to move from
Session Manager to just-in-time node access:

- Allow time for user training and adjustment to the new approval
  workflow.
- Schedule migrations during periods of lower operational
  activity.
- Include buffer time for troubleshooting and adjustments.
- Plan for a period of parallel operation where both systems are
  available.

## Implementation steps

### Phase 1: Setup and configuration

1. Enable just-in-time node access in the Systems Manager console. For detailed
   steps, see [Setting up
   just-in-time access with Systems Manager](systems-manager-just-in-time-node-access-setting-up.md "systems-manager-just-in-time-node-access-setting-up.md").
2. Configure session preferences for just-in-time node access to
   match your current Session Manager settings. For more information, see
   [Update just-in-time node access session preferences](systems-manager-just-in-time-node-access-session-preferences.md "systems-manager-just-in-time-node-access-session-preferences.md").
3. Set up notification preferences for access requests. For more
   information, see [Configure
   notifications for just-in-time access requests](systems-manager-just-in-time-node-access-notifications.md "systems-manager-just-in-time-node-access-notifications.md").
4. If you use RDP connections to Windows Server nodes, configure RDP
   recording. For more information, see [Recording
   RDP connections](systems-manager-just-in-time-node-access-rdp-recording.md "systems-manager-just-in-time-node-access-rdp-recording.md").

### Phase 2: Policy development

1. Create IAM policies for just-in-time node access administrators
   and users.
2. Develop approval policies based on your security requirements and
   use case.
3. Test your policies in a non-production environment to ensure they
   work as expected.

### Phase 3: Pilot migration

1. Select a small group of users and non-critical nodes for the
   pilot.
2. Create new IAM policies for pilot users that include
   just-in-time node access permissions.
3. Remove Session Manager permissions (`ssm:StartSession`) from
   the pilot users' IAM policies.
4. Train pilot users on the new access request workflow.
5. Monitor the pilot for issues and gather feedback.
6. Adjust policies and procedures based on pilot results.

###### Example IAM policy modification for pilot users

Original policy with Session Manager permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession",
 "ssm:ResumeSession",
 "ssm:TerminateSession"
 ],
 "Resource": "*"
 }
 ]
}`

```

Modified policy for just-in-time node access:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartAccessRequest",
 "ssm:GetAccessToken",
 "ssm:ResumeSession",
 "ssm:TerminateSession"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Phase 4: Full migration

Develop a schedule for migrating remaining users and nodes in
batches.

## Testing methodology

Throughout the migration process, conduct the following tests:

- **Policy validation** - Verify that
  approval policies correctly apply to the intended nodes and
  users.
- **Access request workflow** - Test the
  complete workflow from access request to session establishment for both
  auto-approval and manual approval scenarios.
- **Notifications** - Verify that approvers
  receive notifications through configured channels (email, Slack,
  Microsoft Teams).
- **Logging and monitoring** - Verify that
  session logs and access requests are properly captured and
  stored.

## Best practices for a successful migration

- **Communicate early and often** - Inform
  users about the migration timeline and benefits of just-in-time node
  access.
- **Start with non-critical systems** -
  Begin migration with development or test environments before moving to
  production.
- **Document everything** - Maintain
  detailed records of your approval policies, IAM policy changes, and
  configuration settings.
- **Monitor and adjust** - Continuously
  monitor access requests and approval workflows, adjusting policies as
  needed.
- **Establish governance** - Create a
  process for regularly reviewing and updating approval policies as your
  environment changes.
