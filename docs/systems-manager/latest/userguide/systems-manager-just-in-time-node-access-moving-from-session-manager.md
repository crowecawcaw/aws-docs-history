

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Moving to just-in-time node access from Session Manager
<a name="systems-manager-just-in-time-node-access-moving-from-session-manager"></a>

When you enable just-in-time node access, Systems Manager doesn't make any changes to your existing resources for Session Manager. This ensures there's no disruption to your existing environment and users can continue to start sessions while you create and validate approval policies. Once you're ready to test your approval policies, you must modify your existing IAM policies to complete the transition to just-in-time node access. This includes adding the required permissions for just-in-time node access to identities, and removing permission for the `StartSession` API operation for Session Manager. We recommend testing approval policies with a subset of identities and nodes in an AWS account and AWS Region.

For more information about the permissions required for just-in-time node access, see [Setting up just-in-time access with Systems Manager](systems-manager-just-in-time-node-access-setting-up.md).

For more information about modifying and identity's IAM permissions, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*.

The following describes a detailed method of how you can move to just-in-time node access from Session Manager.

Moving from Session Manager to just-in-time node access requires careful planning and testing to ensure a smooth transition without disrupting your operations. The following sections describe how you can complete this process.

## Prerequisites
<a name="migration-prerequisites"></a>

Before you begin, make sure that you have completed the following tasks:
+ Set up the Systems Manager unified console.
+ Verified you have permissions to modify IAM policies in your account.
+ Identified all IAM policies and roles that currently grant Session Manager permissions.
+ Documented your current Session Manager configuration, including session preferences and logging settings.

## Assessment
<a name="environment-assessment"></a>

Assess your current environment and outline desired approval behaviors by completing the following tasks:

1. **Inventory your nodes** - Identify all nodes that users currently access through Session Manager.

1. **Identify user access patterns** - Document which users or roles need access to which nodes, and under what circumstances.

1. **Map approval workflows** - Determine who should approve access requests for different types of nodes.

1. **Review tagging strategy** - Make sure your nodes are properly tagged to support your planned approval policies.

1. **Audit existing IAM policies** - Identify all policies that include Session Manager permissions.

## Planning
<a name="migration-planning"></a>

### Phased strategy
<a name="migration-planning-strategy"></a>

When moving from Session Manager to just-in-time node access, we recommend using a phased approach like the following:

1. **Phase 1: Setup and configuration** - Enable just-in-time node access without modifying existing Session Manager permissions.

1. **Phase 2: Policy development** - Create and test approval policies for your nodes.

1. **Phase 3: Pilot migration** - Modify a small group of non-critical nodes and users or roles from Session Manager to just-in-time node access.

1. **Phase 4: Full migration** - Gradually migrate all remaining nodes and users or roles.

### Timeline considerations
<a name="migration-planning-timeline"></a>

Consider the following factors when creating your timeline to move from Session Manager to just-in-time node access:
+ Allow time for user training and adjustment to the new approval workflow.
+ Schedule migrations during periods of lower operational activity.
+ Include buffer time for troubleshooting and adjustments.
+ Plan for a period of parallel operation where both systems are available.

## Implementation steps
<a name="migration-implementation"></a>

### Phase 1: Setup and configuration
<a name="migration-implementation-phase1"></a>

1. Enable just-in-time node access in the Systems Manager console. For detailed steps, see [Setting up just-in-time access with Systems Manager](systems-manager-just-in-time-node-access-setting-up.md).

1. Configure session preferences for just-in-time node access to match your current Session Manager settings. For more information, see [Update just-in-time node access session preferences](systems-manager-just-in-time-node-access-session-preferences.md).

1. Set up notification preferences for access requests. For more information, see [Configure notifications for just-in-time access requests](systems-manager-just-in-time-node-access-notifications.md).

1. If you use RDP connections to Windows Server nodes, configure RDP recording. For more information, see [Recording RDP connections](systems-manager-just-in-time-node-access-rdp-recording.md).

### Phase 2: Policy development
<a name="migration-implementation-phase2"></a>

1. Create IAM policies for just-in-time node access administrators and users.

1. Develop approval policies based on your security requirements and use case.

1. Test your policies in a non-production environment to ensure they work as expected.

### Phase 3: Pilot migration
<a name="migration-implementation-phase3"></a>

1. Select a small group of users and non-critical nodes for the pilot.

1. Create new IAM policies for pilot users that include just-in-time node access permissions.

1. Remove Session Manager permissions (`ssm:StartSession`) from the pilot users' IAM policies.

1. Train pilot users on the new access request workflow.

1. Monitor the pilot for issues and gather feedback.

1. Adjust policies and procedures based on pilot results.

**Example IAM policy modification for pilot users**  
Original policy with Session Manager permissions:

------
#### [ JSON ]

****  

```
{
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
}
```

------

Modified policy for just-in-time node access:

------
#### [ JSON ]

****  

```
{
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
}
```

------

### Phase 4: Full migration
<a name="migration-implementation-phase4"></a>

Develop a schedule for migrating remaining users and nodes in batches.

## Testing methodology
<a name="migration-testing"></a>

Throughout the migration process, conduct the following tests:
+ **Policy validation** - Verify that approval policies correctly apply to the intended nodes and users.
+ **Access request workflow** - Test the complete workflow from access request to session establishment for both auto-approval and manual approval scenarios.
+ **Notifications** - Verify that approvers receive notifications through configured channels (email, Slack, Microsoft Teams).
+ **Logging and monitoring** - Verify that session logs and access requests are properly captured and stored.

## Best practices for a successful migration
<a name="migration-best-practices"></a>
+ **Communicate early and often** - Inform users about the migration timeline and benefits of just-in-time node access.
+ **Start with non-critical systems** - Begin migration with development or test environments before moving to production.
+ **Document everything** - Maintain detailed records of your approval policies, IAM policy changes, and configuration settings.
+ **Monitor and adjust** - Continuously monitor access requests and approval workflows, adjusting policies as needed.
+ **Establish governance** - Create a process for regularly reviewing and updating approval policies as your environment changes.