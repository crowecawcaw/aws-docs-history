# Amazon GameLift Servers FlexMatch API reference (AWS SDK)

This topic provides a task-based list of API operations for Amazon GameLift Servers FlexMatch. The Amazon GameLift Servers FlexMatch
service API is packaged into the AWS SDK in the `aws.gamelift` namespace.
[Download the
AWS SDK](https://aws.amazon.com/tools/#SDKs "https://aws.amazon.com/tools/#SDKs") or [view the Amazon GameLift Servers API
reference documentation](../../../gamelift/latest/apireference.md "../../../gamelift/latest/apireference.md").

Amazon GameLift Servers FlexMatch provides matchmaking services for use with games that are hosted with Amazon GameLift Servers
hosting solutions (including managed hosting for custom game servers or Amazon GameLift Servers Realtime, and hosting
on Amazon EC2 with Amazon GameLift Servers FleetIQ), as well as with other hosting systems such as peer-to-peer,
on-premises, or cloud compute primitives. See the [Amazon GameLift Servers Developer Guide](../../../gamelift/latest/developerguide/gamelift-intro.md "../../../gamelift/latest/developerguide/gamelift-intro.md") for more information
on other Amazon GameLift Servers hosting options.

###### Topics

- [Set up matchmaking rules and
  processes](#reference-awssdk-flex-configure "#reference-awssdk-flex-configure")
- [Request a match for a player or
  players](#reference-awssdk-flex-place "#reference-awssdk-flex-place")
- [Available programming languages](#reference-awssdk-langlist "#reference-awssdk-langlist")

## Set up matchmaking rules and

processes

Call these operations to create a FlexMatch matchmaker, configure the matchmaking process
for your game, and define a set of custom rules for creating matches and teams.

**Matchmaking configuration**

- [CreateMatchmakingConfiguration](../../../gamelift/latest/apireference/API_CreateMatchmakingConfiguration.md "../../../gamelift/latest/apireference/API_CreateMatchmakingConfiguration.md") – Create a matchmaking
  configuration with instructions for evaluating groups of players and building
  player teams. When using Amazon GameLift Servers for hosting, also specify how to create a new
  game session for the match.
- [DescribeMatchmakingConfigurations](../../../gamelift/latest/apireference/API_DescribeMatchmakingConfigurations.md "../../../gamelift/latest/apireference/API_DescribeMatchmakingConfigurations.md") – Retrieve matchmaking
  configurations defined a Amazon GameLift Servers region.
- [UpdateMatchmakingConfiguration](../../../gamelift/latest/apireference/API_UpdateMatchmakingConfiguration.md "../../../gamelift/latest/apireference/API_UpdateMatchmakingConfiguration.md") – Change settings for
  matchmaking configuration. queue.
- [DeleteMatchmakingConfiguration](../../../gamelift/latest/apireference/API_DeleteMatchmakingConfiguration.md "../../../gamelift/latest/apireference/API_DeleteMatchmakingConfiguration.md") – Remove a matchmaking
  configuration from the region.

**Matchmaking rule set**

- [CreateMatchmakingRuleSet](../../../gamelift/latest/apireference/API_CreateMatchmakingRuleSet.md "../../../gamelift/latest/apireference/API_CreateMatchmakingRuleSet.md") – Create a set of rules to use when
  searching for player matches.
- [DescribeMatchmakingRuleSets](../../../gamelift/latest/apireference/API_DescribeMatchmakingRuleSets.md "../../../gamelift/latest/apireference/API_DescribeMatchmakingRuleSets.md") – Retrieve matchmaking rule sets
  defined in a Amazon GameLift Servers region.
- [ValidateMatchmakingRuleSet](../../../gamelift/latest/apireference/API_ValidateMatchmakingRuleSet.md "../../../gamelift/latest/apireference/API_ValidateMatchmakingRuleSet.md") – Verify syntax for a set of
  matchmaking rules.
- [DeleteMatchmakingRuleSet](../../../gamelift/latest/apireference/API_DeleteMatchmakingRuleSet.md "../../../gamelift/latest/apireference/API_DeleteMatchmakingRuleSet.md") – Remove a matchmaking rule set
  from the region.

## Request a match for a player or

players

Call these operations from your game client service to manage player matchmaking
requests.

- [StartMatchmaking](../../../gamelift/latest/apireference/API_StartMatchmaking.md "../../../gamelift/latest/apireference/API_StartMatchmaking.md")
  – Request matchmaking for one player or a group who want to play in the
  same match.
- [DescribeMatchmaking](../../../gamelift/latest/apireference/API_DescribeMatchmaking.md "../../../gamelift/latest/apireference/API_DescribeMatchmaking.md") – Get details on a matchmaking request,
  including status.
- [AcceptMatch](../../../gamelift/latest/apireference/API_AcceptMatch.md "../../../gamelift/latest/apireference/API_AcceptMatch.md") – For
  a match that requires player acceptance, notify Amazon GameLift Servers when a player accepts a
  proposed match.
- [StopMatchmaking](../../../gamelift/latest/apireference/API_StopMatchmaking.md "../../../gamelift/latest/apireference/API_StopMatchmaking.md")
  – Cancel a matchmaking request.
- [StartMatchBackfill](../../../gamelift/latest/apireference/API_StartMatchBackfill.md "../../../gamelift/latest/apireference/API_StartMatchBackfill.md") - Request additional player matches to fill
  empty slots in an existing game session.

## Available programming languages

The AWS SDK with support for Amazon GameLift Servers is available in the following languages. For information
about support for development environments, see the documentation for each language.

- C++ ([SDK docs](https://aws.amazon.com/sdk-for-cpp/ "https://aws.amazon.com/sdk-for-cpp/")) ([Amazon GameLift Servers](https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_game_lift.html "https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_game_lift.html"))
- Java ([SDK docs](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/")) ([Amazon GameLift Servers](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/gamelift/package-summary.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/gamelift/package-summary.html"))
- .NET ([SDK docs](https://aws.amazon.com/sdk-for-net/ "https://aws.amazon.com/sdk-for-net/"))
  ([Amazon GameLift Servers](../../../sdkfornet/v3/apidocs/items/GameLift/NGameLift.md "../../../sdkfornet/v3/apidocs/items/GameLift/NGameLift.md"))
- Go ([SDK docs](https://aws.amazon.com/sdk-for-go/ "https://aws.amazon.com/sdk-for-go/")) ([Amazon GameLift Servers](../../../sdk-for-go/api/service/gamelift.md "../../../sdk-for-go/api/service/gamelift.md"))
- Python ([SDK docs](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/")) ([Amazon GameLift Servers](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html"))
- Ruby ([SDK docs](https://aws.amazon.com/sdk-for-ruby/ "https://aws.amazon.com/sdk-for-ruby/")) ([Amazon GameLift Servers](../../../sdk-for-ruby/v3/api/Aws/GameLift.md "../../../sdk-for-ruby/v3/api/Aws/GameLift.md"))
- PHP ([SDK docs](https://aws.amazon.com/sdk-for-php/ "https://aws.amazon.com/sdk-for-php/")) ([Amazon GameLift Servers](../../../aws-sdk-php/v3/api/class-Aws.GameLift.md "../../../aws-sdk-php/v3/api/class-Aws.GameLift.md"))
- JavaScript/Node.js ([SDK docs](https://aws.amazon.com/sdk-for-node-js/ "https://aws.amazon.com/sdk-for-node-js/")) ([Amazon GameLift Servers](../../../AWSJavaScriptSDK/v3/latest/clients/client-gamelift/index.md "../../../AWSJavaScriptSDK/v3/latest/clients/client-gamelift/index.md"))
