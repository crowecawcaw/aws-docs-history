

# Amazon GameLift Servers FlexMatch API reference (AWS SDK)
<a name="reference-awssdk-flex"></a>

This topic provides a task-based list of API operations for Amazon GameLift Servers FlexMatch. The Amazon GameLift Servers FlexMatch service API is packaged into the AWS SDK in the `aws.gamelift` namespace. [Download the AWS SDK](https://aws.amazon.com/tools/#SDKs) or [view the Amazon GameLift Servers API reference documentation](https://docs.aws.amazon.com/gamelift/latest/apireference/). 

Amazon GameLift Servers FlexMatch provides matchmaking services for use with games that are hosted with Amazon GameLift Servers hosting solutions (including managed hosting for custom game servers or Amazon GameLift Servers Realtime, and hosting on Amazon EC2 with Amazon GameLift Servers FleetIQ), as well as with other hosting systems such as peer-to-peer, on-premises, or cloud compute primitives. See the [Amazon GameLift Servers Developer Guide](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-intro.html) for more information on other Amazon GameLift Servers hosting options.

**Topics**
+ [Set up matchmaking rules and processes](#reference-awssdk-flex-configure)
+ [Request a match for a player or players](#reference-awssdk-flex-place)
+ [Available programming languages](#reference-awssdk-langlist)

## Set up matchmaking rules and processes
<a name="reference-awssdk-flex-configure"></a>

Call these operations to create a FlexMatch matchmaker, configure the matchmaking process for your game, and define a set of custom rules for creating matches and teams.

**Matchmaking configuration**
+ [CreateMatchmakingConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateMatchmakingConfiguration.html) – Create a matchmaking configuration with instructions for evaluating groups of players and building player teams. When using Amazon GameLift Servers for hosting, also specify how to create a new game session for the match. 
+ [DescribeMatchmakingConfigurations](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeMatchmakingConfigurations.html) – Retrieve matchmaking configurations defined in an Amazon GameLift Servers region.
+ [UpdateMatchmakingConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateMatchmakingConfiguration.html) – Change settings for matchmaking configuration. queue.
+ [DeleteMatchmakingConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeleteMatchmakingConfiguration.html) – Remove a matchmaking configuration from the region.

**Matchmaking rule set**
+ [CreateMatchmakingRuleSet](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateMatchmakingRuleSet.html) – Create a set of rules to use when searching for player matches. 
+ [DescribeMatchmakingRuleSets](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeMatchmakingRuleSets.html) – Retrieve matchmaking rule sets defined in an Amazon GameLift Servers region.
+ [ValidateMatchmakingRuleSet](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ValidateMatchmakingRuleSet.html) – Verify syntax for a set of matchmaking rules. 
+ [DeleteMatchmakingRuleSet](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeleteMatchmakingRuleSet.html) – Remove a matchmaking rule set from the region.

## Request a match for a player or players
<a name="reference-awssdk-flex-place"></a>

Call these operations from your game client service to manage player matchmaking requests.
+ [StartMatchmaking](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartMatchmaking.html) – Request matchmaking for one player or a group who want to play in the same match. 
+ [DescribeMatchmaking](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeMatchmaking.html) – Get details on a matchmaking request, including status.
+ [AcceptMatch](https://docs.aws.amazon.com/gamelift/latest/apireference/API_AcceptMatch.html) – For a match that requires player acceptance, notify Amazon GameLift Servers when a player accepts a proposed match. 
+ [StopMatchmaking](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopMatchmaking.html) – Cancel a matchmaking request. 
+ [StartMatchBackfill](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartMatchBackfill.html) - Request additional player matches to fill empty slots in an existing game session.

## Available programming languages
<a name="reference-awssdk-langlist"></a>

The AWS SDK with support for Amazon GameLift Servers is available in the following languages. For information about support for development environments, see the documentation for each language.
+ C\+\+ ([SDK docs](https://aws.amazon.com/sdk-for-cpp/)) ([Amazon GameLift Servers](https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_game_lift.html))
+ Java ([SDK docs](https://aws.amazon.com/sdk-for-java/)) ([Amazon GameLift Servers](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/gamelift/package-summary.html))
+ .NET ([SDK docs](https://aws.amazon.com/sdk-for-net/)) ([Amazon GameLift Servers](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/GameLift/NGameLift.html))
+ Go ([SDK docs](https://aws.amazon.com/sdk-for-go/)) ([Amazon GameLift Servers](https://docs.aws.amazon.com/sdk-for-go/api/service/gamelift/))
+ Python ([SDK docs](https://aws.amazon.com/sdk-for-python/)) ([Amazon GameLift Servers](https://docs.aws.amazon.com/boto3/latest/reference/services/gamelift.html))
+ Ruby ([SDK docs](https://aws.amazon.com/sdk-for-ruby/)) ([Amazon GameLift Servers](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/GameLift.html))
+ PHP ([SDK docs](https://aws.amazon.com/sdk-for-php/)) ([Amazon GameLift Servers](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.GameLift.GameLiftClient.html))
+ JavaScript/Node.js ([SDK docs](https://aws.amazon.com/sdk-for-node-js/)) ([Amazon GameLift Servers](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-gamelift/index.html))