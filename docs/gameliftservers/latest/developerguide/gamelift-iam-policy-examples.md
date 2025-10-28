# IAM permission examples for Amazon GameLift Servers

Use the syntax in these examples to set AWS Identity and Access Management (IAM) permissions for users that need
access to Amazon GameLift Servers resources. For more information on managing user permissions, see [Set user permissions for Amazon GameLift Servers](setting-up-aws-login.md#getting-started-create-iam-user "setting-up-aws-login.md#getting-started-create-iam-user").
When managing permissions for users outside of the IAM Identity Center, as a best practice always attach
permissions to IAM roles or user groups, not individual users.

If you're using Amazon GameLift Servers FleetIQ as a standalone solution, see [Set up your AWS account for
Amazon GameLift Servers FleetIQ](../fleetiqguide/gsg-iam-permissions.md "../fleetiqguide/gsg-iam-permissions.md").

## Administration permission examples

These examples give a hosting administrator or developer targeted access to manage Amazon GameLift Servers
game hosting resources.

###### Example Syntax for Amazon GameLift Servers full access resource permissions

The following example extends full access to all Amazon GameLift Servers resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "gamelift:*",
 "Resource": "*"
 }
}`

```

###### Example Syntax for Amazon GameLift Servers resource permissions with support for Regions that aren't enabled by

default

The following example extends access to all Amazon GameLift Servers resources and AWS Regions that
aren't enabled by default. For more
information about Regions that aren't enabled by default and how to enable them, see
[Managing AWS Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in the
_AWS General Reference_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeRegions",
 "gamelift:*"
 ],
 "Resource": "*"
 }
}`

```

###### Example Syntax for Amazon GameLift Servers resource to access container images in Amazon ECR

The following example extends access to Amazon Elastic Container Registry (Amazon ECR) actions that Amazon GameLift Servers users need
when working with managed container fleets.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "ecr:DescribeImages",
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "*"
 }
}`

```

###### Example Syntax for Amazon GameLift Servers resource and `PassRole` permissions

The following example extends access to all Amazon GameLift Servers resources and allows a user to pass an
IAM service role to Amazon GameLift Servers. A service role gives Amazon GameLift Servers limited ability to access other
resources and services on your behalf, as is described in
[Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md "setting-up-role.md"). For example, when responding to
a `CreateBuild` request, Amazon GameLift Servers needs access to your build files in an Amazon S3
bucket. For more information about the `PassRole` action, see [IAM:
Pass an IAM role to a specific AWS service](../../../IAM/latest/UserGuide/reference_policies_examples_iam-passrole-service.md "../../../IAM/latest/UserGuide/reference_policies_examples_iam-passrole-service.md") in the
_IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "gamelift:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "gamelift.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Player user permission examples

These examples allow a backend service or other entity to make API calls to the Amazon GameLift Servers API.
They cover the common scenarios for managing game sessions, player sessions, and matchmaking.
For more details, see [Set up programmatic access for your
game](setting-up-aws-login.md#getting-started-iam-player-user "setting-up-aws-login.md#getting-started-iam-player-user").

###### Example Syntax for game session placement permissions

The following example extends access to the Amazon GameLift Servers APIs that use game session placement
queues to create game sessions and manage player sessions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "PlayerPermissionsForGameSessionPlacements",
 "Effect": "Allow",
 "Action": [
 "gamelift:StartGameSessionPlacement",
 "gamelift:DescribeGameSessionPlacement",
 "gamelift:StopGameSessionPlacement",
 "gamelift:CreatePlayerSession",
 "gamelift:CreatePlayerSessions",
 "gamelift:DescribeGameSessions"
 ],
 "Resource": "*"
 }
}`

```

###### Example Syntax for matchmaking permissions

The following example extends access to the Amazon GameLift Servers APIs that manage FlexMatch matchmaking
activities. FlexMatch matches players for new or existing game sessions and initiates game
session placement for games hosted on Amazon GameLift Servers. For more information about FlexMatch, see [What is
Amazon GameLift Servers FlexMatch?](../flexmatchguide/match-intro.md "../flexmatchguide/match-intro.md")

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "PlayerPermissionsForGameSessionMatchmaking",
 "Effect": "Allow",
 "Action": [
 "gamelift:StartMatchmaking",
 "gamelift:DescribeMatchmaking",
 "gamelift:StopMatchmaking",
 "gamelift:AcceptMatch",
 "gamelift:StartMatchBackfill",
 "gamelift:DescribeGameSessions"
 ],
 "Resource": "*"
 }
}`

```

###### Example Syntax for manual game session placement permissions

The following example extends access to the Amazon GameLift Servers APIs that manually create game
sessions and player sessions on specified fleets. This scenario supports games that don't
use placement queues, such as games that let players join by choosing from a list of
available game sessions (the "list-and-pick" method).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "PlayerPermissionsForManualGameSessions",
 "Effect": "Allow",
 "Action": [
 "gamelift:CreateGameSession",
 "gamelift:DescribeGameSessions",
 "gamelift:SearchGameSessions",
 "gamelift:CreatePlayerSession",
 "gamelift:CreatePlayerSessions",
 "gamelift:DescribePlayerSessions"
 ],
 "Resource": "*"
 }
}`

```
