

# GAMEOPS02-BP02 Organize infrastructure resources using resource tagging
<a name="gameops02-bp02"></a>

 To effectively manage and track your [infrastructure resources](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-laying-the-foundation/tagging.html) in AWS, use proper [resource tagging](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) and [grouping](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html) to identify each resource's owner, project, application, cost center, and other data. Tagged resources can be grouped together using [resource groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html), which assists with operational support. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-2"></a>

 Define [tagging policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html). Typical strategies include resource tags for identifying the resource owner, such as team name or individual name, the name of the game, application, or project, the studio name, environment (like development or production), and the role of the resource (such as database server, web server, dedicated game server, app server, or cache server). You can add other tags to assist with business and IT needs. [AWS Config](https://aws.amazon.com/config/) can also enforce a [tagging policy](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) at resource creation and update time. Tags and resource groups are available from the AWS Management Console, the AWS CLI, and API operations. 

### Implementation steps
<a name="implementation-steps-2"></a>
+  Tag resources to identify their owner, project, app, cost center, and other relevant data. 
+  Implement tagging policies including tags for owner, project, studio, environment, and resource role. 
+  Use AWS Config to enforce tagging policies, and manage tags through AWS Management Console, CLI, and API. 