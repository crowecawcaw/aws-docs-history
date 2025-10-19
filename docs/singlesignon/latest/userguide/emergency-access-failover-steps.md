# Emergency failover process

When an IAM Identity Center instance isn't available and you determine that you must provide emergency access to the AWS Management Console, we recommend the following failover process.


1. The IdP administrator enables the direct IAM federation application in your IdP.
2. Users request access to the temporary operations group through your existing mechanism, such
 as an email request, Slack channel, or other form of communication.
3. Users that you add to your emergency access groups sign in to the IdP, select the emergency
 access account, and, users choose a role to use in the emergency access account. From
 these roles, they can assume roles in corresponding workload accounts that have
 cross-account trust with the emergency account role.
