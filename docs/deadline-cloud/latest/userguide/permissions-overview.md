

# How permissions work in Deadline Cloud
<a name="permissions-overview"></a>

AWS Deadline Cloud (Deadline Cloud) controls access with two systems. *Access levels* control what you can see and do when you sign in to the Deadline Cloud monitor or submit jobs from your workstation. *AWS Identity and Access Management (IAM) policies* control what AWS credentials can do, such as administering farms in the Deadline Cloud console or calling the API from a pipeline script.

When you sign in to the monitor, AWS IAM Identity Center (IAM Identity Center) authenticates you, and your access levels govern what you can do. Your requests also carry your identity, so Deadline Cloud records who created or last updated each job. IAM policies govern programmatic access, such as pipeline automation and worker hosts. You can also use IAM credentials, for example to administer farms in the Deadline Cloud console, but Deadline Cloud attributes those requests to the IAM role or user, so jobs submitted with a shared role all show the same identity.


| Who | Signs in with | Access controlled by | Where you grant it | 
| --- | --- | --- | --- | 
| People using the monitor or the integrated submitters, such as artists and researchers | The monitor URL, through IAM Identity Center | Access levels on farms, queues, and fleets | The Deadline Cloud console, on each resource's **Access management** tab | 
| Administrators working in the Deadline Cloud console | The AWS Management Console | IAM policies | IAM | 
| Pipeline scripts and automation that call the Deadline Cloud API or CLI with AWS credentials | An IAM role or user | IAM policies | IAM | 
| Worker hosts in your fleets | The fleet's IAM role | Service roles on the fleet and queue | IAM, when you create the fleet or queue | 

## Where you grant access levels
<a name="permissions-where-granted"></a>

You grant each user or group one of four access levels: viewer, contributor, manager, and owner. Each level includes everything from the levels before it. For the exact permissions at each level, see [What each access level allows](#permissions-access-levels) at the end of this topic.

You assign access levels on farms, queues, and fleets in the Deadline Cloud console. The Deadline Cloud documentation and API call each assignment a *membership*. A grant on the farm applies to every queue and fleet in the farm. A grant on a queue or fleet applies only to that resource, so you can give a team the contributor level on its own queue and the viewer level everywhere else.

A grant on a group applies to whoever is in the group when they make a request. When you add a user to the group in your identity source, that user gets the group's access without any change to the grant, and when you remove a user from the group, that user loses the group's access the same way. The group's membership on the farm, queue, or fleet stays in place; you don't update or refresh it as the group's members change.

When a user has grants at more than one level, Deadline Cloud applies the highest one. For example, a user with the viewer level on the farm and the manager level on one queue has manager permissions on that queue and viewer permissions everywhere else in the farm. A lower-level grant can't reduce a farm-level grant.

Access levels control what you can see and manage. Access levels don't decide where jobs run: the service schedules jobs based on queue–fleet associations and each job's host requirements. For example, a grant on a fleet lets users see the fleet and its workers; it doesn't route their jobs to that fleet. To divide your farm so that permissions and hardware both land where you want them, see [Organize your farms, queues, and fleets](organize-farms-queues-fleets.md).

If you have no membership on a farm, queue, or fleet, you can't see that resource in the monitor, even though you can sign in. If your only membership is on a queue or fleet, you don't see the farm in your farm list, but you can still work with that queue or fleet. To also control who can sign in to the monitor at all, see [Restricting which users can access the monitor](restrict-user-management-visibility.md).

## How access levels relate to IAM
<a name="permissions-and-iam"></a>

Access levels are enforced through IAM, but you don't write IAM policies to use them. When you sign in to the monitor, IAM Identity Center authenticates you, and the monitor makes AWS requests on your behalf using the *monitor role*, an IAM role in your account. The AWS managed policies attached to the monitor role allow each operation based on your access level on the farm, queue, or fleet involved. Although these requests use an IAM role, they keep your identity, so jobs still record which person created or updated them. The monitor desktop application also shares these credentials with the Deadline Cloud CLI and the integrated submitters, so the same access levels apply there.

The credentials that the monitor issues are temporary. When you remove a user's access or disable the user in your identity source, the user can't sign in again or get new credentials, but credentials already issued keep working until they expire, at most 15 minutes later.

If you sign in through the monitor, you don't need an IAM user or policies of your own. To change what an access level allows, for example to let contributors cancel their own jobs, add a policy to the monitor role. For more information, see [Monitor role](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security-iam-service-roles.html#monitor-role) in the *Deadline Cloud Developer Guide*.

## When to grant IAM permissions instead
<a name="permissions-iam-direct"></a>

If you use AWS credentials directly, for example in a pipeline script or in the Deadline Cloud console, your permissions come from IAM policies, and access levels don't apply. Grant IAM permissions for:
+ **Console administration** – Creating farms, queues, and fleets, and assigning access levels, are Deadline Cloud console operations that require IAM permissions. See [Policy to access the console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-console-access).
+ **Pipeline automation** – A submission service or CI system calls the Deadline Cloud API with an IAM role scoped to the operations it needs. For example policies, see [Identity-based policy examples for Deadline Cloud](security_iam_id-based-policy-examples.md).
+ **Worker hosts** – Workers use the fleet role and queue roles that you configure when creating those resources. For more information, see [Service roles for Deadline Cloud](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security-iam-service-roles.html) in the *Deadline Cloud Developer Guide*.

For the full IAM reference for Deadline Cloud, including supported actions, resources, and condition keys, see [Identity and Access Management in Deadline Cloud](security-iam.md).

## What each access level allows
<a name="permissions-access-levels"></a>

The following tables list the permissions at each access level for each resource type that a grant can be placed on, with the default AWS managed policies. A grant on a farm also confers the queue and fleet permissions on every queue and fleet in that farm. Budgets and usage data appear only in the farm table. The owner level on a queue or fleet doesn't include them; you grant them with the owner level on the farm. To change what a level allows, see [How access levels relate to IAM](#permissions-and-iam). To grant an access level, see [Assign permissions to users and groups](assign-permissions-procedure.md).


**Farm permissions by access level**  

| Permission | Viewer | Contributor | Manager | Owner | 
| --- | --- | --- | --- | --- | 
| View farm details | Yes | Yes | Yes | Yes | 
| View queues and fleets | Yes | Yes | Yes | Yes | 
| Submit jobs | No | Yes | Yes | Yes | 
| Manage user access | No | No | Yes | Yes | 
| View and create budgets | No | No | No | Yes | 
| View usage data | No | No | No | Yes | 


**Queue permissions by access level**  

| Permission | Viewer | Contributor | Manager | Owner | 
| --- | --- | --- | --- | --- | 
| View queue details | Yes | Yes | Yes | Yes | 
| View jobs in queue | Yes | Yes | Yes | Yes | 
| Submit jobs to queue | No | Yes | Yes | Yes | 
| Edit and cancel jobs | No | No | Yes | Yes | 
| Manage queue user access | No | No | Yes | Yes | 


**Fleet permissions by access level**  

| Permission | Viewer | Contributor | Manager | Owner | 
| --- | --- | --- | --- | --- | 
| View fleet details | Yes | Yes | Yes | Yes | 
| View workers in fleet | Yes | Yes | Yes | Yes | 
| Manage fleet user access | No | No | Yes | Yes | 