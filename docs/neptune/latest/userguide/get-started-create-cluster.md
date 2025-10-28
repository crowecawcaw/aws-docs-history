# Creating an Amazon Neptune cluster

The easiest way to create a new Amazon Neptune DB cluster is to use an AWS CloudFormation template
that creates all the required resources for you, without having to do everything by hand.
The AWS CloudFormation template performs much of the setup for you, including creating an Amazon Elastic Compute Cloud
(Amazon EC2) instance:

###### To launch a new Neptune DB cluster using an AWS CloudFormation template

1. Create a new IAM user with the permissions you will need for
   working with your Neptune DB cluster, as explained in [IAM user permissions](manage-console-iam-user.md "manage-console-iam-user.md").
2. Set up additional prerequisites needed to use the AWS CloudFormation template, as explained
   in [Prerequisites for setting up Amazon Neptune using AWS CloudFormation](get-started-prereqs.md "get-started-prereqs.md").
3. Invoke the AWS CloudFormation stack, as described in [Creating an Amazon Neptune cluster using AWS CloudFormation](get-started-cfn-create.md "get-started-cfn-create.md").
   You can also create a [Neptune global database](neptune-global-database.md "neptune-global-database.md")
   that spans multiple AWS Regions, enabling low-latency global reads and providing fast
   recovery in the rare case where an outage affects an entire AWS Region.

For information about creating an Amazon Neptune cluster manually using the AWS Management Console, see
[Launching a Neptune DB cluster using the AWS Management Console](manage-console-launch-console.md "manage-console-launch-console.md").

You can also use an AWS CloudFormation template to create a Lambda function to use with Neptune (see
[Using AWS CloudFormation to Create a Lambda Function to Use in
Neptune](get-started-cfn-lambda.md "get-started-cfn-lambda.md") ).

For general information about managing clusters and instances in Neptune, see
[Managing Your Amazon Neptune Database](manage-console.md "manage-console.md").
