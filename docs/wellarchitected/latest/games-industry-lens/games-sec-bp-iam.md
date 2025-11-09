# Identity and access management

| GAMESEC01: How do you manage player identity and access<br>management? |
| ---------------------------------------------------------------------- |
|                                                                        |

When developing a game, you must determine how you will provide players with access to
your game and related services. This decision is influenced by player acquisition and
monetization strategy, player experience, and other factors such as the existing
capabilities that might be provided by your game publishing partners. For example, a
game might require purchases and require a player to create a user profile to associate
real-money payment methods with their account.

Alternatively, a game may desire to reduce the barrier to entry for first-time player experiences by removing the need to create a user account before playing the game, thereby improving the chance that a player will try the game for the first time. Typically, games will implement one or more combinations of player identity and access management approaches for their game.

**Unauthenticated or anonymous access:** This access level
is useful in situations where a game does not require a player to create a new user
account or link with their identity on social networks and gaming platforms. This is the
simplest and quickest way for player to start to play a game and is particularly useful
in mobile games where a game developer may want to reduce the barrier to entry for the
initial first time experience. In this access scenario, if you want to identify usage
from the game installation, you can do so by programming the game client to generate and
store a unique identiﬁer onto the player's device that is used to identify the player
across game sessions on their device and allow analytics reporting on usage over time.
At a later date, if a player chooses to create an account, then you can associate their
new user account to their previously generated unique identiﬁer to link the player's
historical usage such as stats and game achievements to their new player identity. If a
player does not eventually create and link an account, the device that the player uses
to interact with the game can be uniquely identiﬁed, but any recoverable information
about the player is not collected and stored. Thus, if the player breaks the device, the
previous stored data associated with the device is also lost and might not be
recoverable.

**Authentication with username and password:**
A game may allow players to create their own user accounts with a username and password that is stored within the game's backend. Typical reasons for this are when a game developer is collaborating with a game publisher who already has an existing player account system that the developer can integrate with, or when a developer who may publish their own games wants to simplify the player experience by allowing players to create a single user account for access across all of the game they publish.

**Authentication and account linking with third-party social
networks and gaming platforms:** It is common for online games and games with social features to provide third-party identity provider federation as a way to simplify the player experience. Instead of asking players to create a username and password combination to authenticate, you can use identity federation to allow players to authenticate using their third-party accounts with social networks and gaming platforms. This login process simpliﬁes sign-in and registration experience and it provides a convenient alternative to mandatory account creation and a frictionless method for players to access games. For game developers, federated login can oﬀer a streamlined player veriﬁcation workﬂow and may also provide a more reliable way to manage player data for personalization because you do not need to ask players to provide you with certain data that they likely have already provided to the third-party identity provider. Additionally, these platforms provide integration with additional social features such as allowing you to link players with their friends.

The following best practices can help you to incorporate secure access control for your game:

**GAMESEC_BP01: Requests to game backend services are
authenticated.**

Any requests sent to game backend services should be authenticated to prevent unwanted requests to your game backend.

You should provide an authentication service for players to login, which should
return secure short-lived tokens, such as JSON Web Token (JWT), to the game client when
a player successfully authenticates. These tokens can include claim assertions
containing player attributes and other relevant metadata that can be used in subsequent
requests sent from the game client to your game backend to authenticate requests and
authorize them in the context of the authenticated player. You have the option to either
design and build your own player authentication system, which would require ongoing
improvement and maintenance, or you can take advantage of the scalable and secure user
sign-up, sign-in, and access control features provided by [Amazon Cognito](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/"). Amazon Cognito User Pools allows you to create
a user directory and provides APIs that you can integrate into your game for sign-up,
sign-in, password reset workflows, and it can be integrated with third-party identity
providers. [Application Load Balancers](../../../elasticloadbalancing/latest/application/listener-authenticate-users.md "../../../elasticloadbalancing/latest/application/listener-authenticate-users.md") and [Amazon
API Gateway](../../../apigateway/latest/developerguide/apigateway-integrate-with-cognito.md "../../../apigateway/latest/developerguide/apigateway-integrate-with-cognito.md") both provide integrations with Cognito to easily integrate user
authentication for requests sent to your custom game backends hosted with these
services.

If your game supports anonymous access and you cannot authenticate a player, you can
use a client authentication approach to provide a secure experience when integrating
with your game backend. If your game client uses AWS services, then requests to these
services must be signed using credentials. To provide credentials to your game client
for unauthenticated users, you can use the AWS SDK to retrieve short-lived credentials
from [Amazon Cognito Identity
Pools](../../../cognito/latest/developerguide/cognito-identity.md "../../../cognito/latest/developerguide/cognito-identity.md") that can be used to sign your requests to AWS services. These
credentials can be refreshed from your game client. In addition to directly integrating
with the AWS SDK from the game client, you can also build your own game backend, using
a service such as Amazon API Gateway, which supports custom authorization. By designing
your own game backend service, you can gain authoritative control over all requests with
custom server-side logic. For more information on building a backend service for games
hosted using Amazon GameLift Servers, refer to [Design your backend service](../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend.md "../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend.md").

**GAMESEC_BP02: Player requests to join a multiplayer game should be validated by your game backend service.**

Typically, in multiplayer games, a player will join a game session by selecting an option directly from a list of available sessions, or they will submit a request to ﬁnd a match, which places the responsibility on the game developer to locate an eligible game session and provide the connection information, usually an IP address and port, back to the player's game client. The implementation may vary depending on the genre of game you are developing, but regardless, it is a security best practice to perform server-side validation of a player’s game join request.

For example, in a session-based multiplayer game, a request from a player to join a
game session should be validated by your game server software with your game backend
matchmaking service before authorizing their connection to the server. When a player
requests to join a game session, the game server should check the request for a unique
identiﬁer, such as a player session ID and server-generated ticket that was previously
provided to the game client by your game backend matchmaking service. Upon initiating
the connection to the game server, your server-side software can use this information to
verify with the matchmaking service that the player's connection request is valid, and
ensure that the player is not joining a spot previously reserved in the game session for
another player. For games hosted using Amazon GameLift Servers, refer to the [Amazon GameLift Servers documentation](../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md#gamelift-sdk-server-validateplayer "../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md#gamelift-sdk-server-validateplayer") for an example of how this type of server-side validation
can be implemented.

**GAMESEC_BP03: Player user accounts that require passwords should enforce a strong security policy.**

If a game provides players with the ability to create a user account with a password, you should require that passwords adhere to strong policies. For example, Amazon Cognito User Pools provides support for [defining password requirements](../../../cognito/latest/developerguide/user-pool-settings-policies.md "../../../cognito/latest/developerguide/user-pool-settings-policies.md") for user accounts.

**GAMESEC_BP04: Provide an option for players to setup multi-factor authentication (MFA) on their accounts.**

Player accounts can be a valuable asset to bad actors, particularly in games that support in-game currency and purchases. Due to the pervasiveness of player account hacking and social engineering against game developer player support teams, it is important to provide players with the option to configure multi-factor authentication (MFA) for their user account to enhance the security of their accounts.

When a player accesses their account using MFA, they are challenged with a temporary
code that is sent to their email, phone number, or a purpose-built multi-factor
authentication mobile app, which they must enter to login within a limited time frame to
successfully authenticate. MFA can also be used to protect an account that is attempting
to authenticate from a new geo-location, accounts that have been flagged by player
support for potential malicious activity, and even for accounts that have not logged
into the game for an extended period of time. For example, Amazon Cognito User Pools
provides support for [configuring
multi-factor authentication](../../../cognito/latest/developerguide/user-pool-settings-mfa.md "../../../cognito/latest/developerguide/user-pool-settings-mfa.md") on user directories.

| GAMESEC02: How do you prevent unauthorized access to game<br>content? |
| --------------------------------------------------------------------- |
|                                                                       |

Modern games include a significant amount of content, including downloadable content (DLC), which is an important aspect of player engagement and game monetization. Players expect an ongoing stream of new characters, levels, and challenges, requiring game developers to keep up with this constant demand for fresh content in order to retain players. The variety and the size of the content can vary greatly depending on the type of the game and also the device the game is played on whether it is PC, console, or mobile. It is important to ensure that game content is protected from unauthorized access.

**GAMESEC_BP05: Restrict access of downloadable content to authorized clients and users.**

Access to game content should be restricted to authorized applications and clients.

Consider using Amazon S3 as a cost-eﬀective and scalable origin for storing downloadable
game content, and Amazon CloudFront to provide globally performant content delivery to
players. Both services provide built-in mechanisms for restricting access to data that
is stored.

When you need to grant access to S3 content, there are several best practices that
should be considered. By default, only the AWS account that created an S3 bucket can
access the objects stored within it. To grant access to your internal applications and
to manage content stored in Amazon S3 buckets, use [Identity and Access Management
(IAM)](../../../AmazonS3/latest/userguide/s3-access-control.md "../../../AmazonS3/latest/userguide/s3-access-control.md") to create policies that provide appropriate access. [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") can be
associated with federated users, systems, or applications hosted in services, such as
Amazon EC2, Lambda, and container-based applications hosted in Amazon EKS and Amazon ECS. For
example, you might use the AWS SDK or AWS CLI to publish and manage game content
assets in S3 buckets. To support this use case, you can create an IAM Role with
appropriate access to read and write game content to your S3 buckets and associate it
the EC2 Instances that host your software and scripts.

Resource-based policies can also defined for your bucket, and for specific objects.
[S3
Bucket Policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md") are associated with the S3 bucket and can be used to restrict
access to the bucket and objects within it, as well as grant access to your S3 resources
from other accounts. For example, in scenarios where multiple teams or separate game
development studios are working on the same game content and require the same access to
centrally hosted content in S3, you can use an S3 bucket policy to define permissions
for cross-account access to the S3 resources. Consider using [S3 Access Points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md") which can
simplify managing data access to shared data by creating access points with names and
permissions specific to each application or sets of applications. The Amazon S3
documentation contains additional [best practices for access control in Amazon S3](../../../AmazonS3/latest/userguide/access-control-best-practices.md#access-control-best-practices-store-share "../../../AmazonS3/latest/userguide/access-control-best-practices.md#access-control-best-practices-store-share").

It is recommended to generate temporary URLs that grant short term access to your
content. Amazon S3 provides support for generating [presigned URLs](../../../AmazonS3/latest/userguide/using-presigned-url.md "../../../AmazonS3/latest/userguide/using-presigned-url.md"), which
allow object owners to share objects with others by generating a presigned URL using
their own security credentials within their backend that grant time-limited permission
to download the objects. By doing so, the end user or application that is being granted
access is not required to have an account or IAM permissions, and instead uses the
presigned URL to access the content. This is a best practice that is commonly used in a
variety of games use cases, such as granting authorized players access to downloadable
content that they have been entitled to, and providing temporary access to limited time
game content. Presigned URLs can also be used to provide temporary permissions to upload
content to your S3 bucket, for example to provide a player with access to upload client
logs to assist your player support team during troubleshooting a player support case.
provides best practices for [limiting presigned URL capabilities.](../../../AmazonS3/latest/userguide/using-presigned-url.md#PresignedUrlUploadObject-LimitCapabilities "../../../AmazonS3/latest/userguide/using-presigned-url.md#PresignedUrlUploadObject-LimitCapabilities")

[S3 Block
Public Access](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") is a set of security controls that ensures S3 buckets and
objects do not have public access by overriding the settings defined by specific users
to enable centralized control across your S3 access points, buckets, and AWS accounts.

While your applications, game developers, artists, and other personnel may need
direct access to the content in S3 buckets for development and management purposes, it
is recommended to use a content delivery network to provide access to content available
publicly to players or other users over the internet. This improves download performance
and reduces costs by caching frequently accessed content. Amazon CloudFront can globally
distribute your content by caching and delivering it closer to your players while
reducing the load on your game’s download origin, such as Amazon S3.

Rather than serving your public content directly from S3 buckets, it is recommended
to keep this content private and serve it publicly using CloudFront, which can be
configured to require that players access your private content, for example a new game
download for paid players only, using either [signed
URLs](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.md") or [signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-signed-cookies.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-signed-cookies.md"). You then develop your application either to create and
distribute signed URLs to authenticated users, or to send set-cookie headers that set
signed cookies for authenticated users. When you create signed URLs or signed cookies to
control access to your files, you can specify an ending date and time, after which the
URL is no longer valid. Optionally, you can also specify the IP address or range of
addresses of the computers that can be used to access your content, which is useful if
you want to restrict access to specific game development studio partners or contractor
networks. Use signed URLs in the cases where you want to restrict access to individual
files or your users are using a client that doesn't support cookies. Use signed cookies
in the cases where you want to provide access to multiple restricted files, or you don't
want to change your current URLs. Signed URLs take precedence over signed cookies.

**GAMESEC_BP06: Limit origin access to authorized content delivery
networks (CDNs).**

You should prevent users from circumventing your content delivery networks to
directly access content from your origin, such as your Amazon S3 buckets. It is
important to restrict access to your origin to only your authorized CDNs, which helps to
reduce data transfer costs from unnecessarily serving content out of the origin. It also
improves security posture by ensuring that all public access to your origin content
flowed through the same entry point, where you can deploy edge security controls such as
AWS WAF layer-7 filtering, injection and inspection of security-related HTTP request
parameters, and Distributed Denial of Service (DDoS) protections. To implement these
controls for an S3 origin, you can use [Amazon CloudFront origin access identity (OAI)](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") which ensures that all
requests to your S3 objects are originating from your CloudFront Distribution. It is
recommended to associate AWS WAF with your CloudFront distribution in order to provide
layer-7 filtering. However, if you are serving content from additional CDNs, you can
configure the CDN to insert one or more custom HTTP headers into origin requests which
can be inspected by AWS WAF to ensure that the incoming traffic originated from your
authorized CDN provider. This approach is also useful to prevent users from
circumventing your CDN providers when your origin is hosted behind an [Application Load Balancer (ALB)](../../../AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.md "../../../AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.md"). ALBs can be associated with AWS WAF for
layer-7 protections, and AWS WAF can be configured to insert a custom HTTP header that
can be inspected by your ALB to ensure that incoming traffic to the load balancer was
first processed and inspected by AWS WAF.

**GAMESEC_BP07: Implement geo-restrictions to prevent unauthorized access.**

When a player requests your content, CloudFront serves the requested content from the
nearest edge location, regardless of where the player is located. However, there may be
scenarios where you need to restrict how your content is accessible by users in specific
parts of the world. For example, you may have a rolling game deployment strategy that
releases content in phases on a country-by-country basis, or you may have to abide by
country-specific access controls. You can use geo restriction, also known as geo
blocking, to prevent players in specific geographic locations from accessing content
that you're distributing through a CloudFront distribution. You can use the CloudFront
geo restriction feature to restrict access to all of the files that are associated with
a distribution and to restrict access at the country level. Alternatively, you can use a
third-party geolocation service to restrict access to a subset of the files that are
associated with a distribution or to restrict access at a finer granularity than the
country level.

Using CloudFront geo restriction, you can allow your players to access your content only if they're in one of the countries on an allow list of approved countries and prevent your players from accessing your content if they're in one of the countries on a deny list of banned countries. If a request is received from a blocked geographic location, CloudFront will return 403 Forbidden HTTP status code to the player.

**GAMESEC_BP08: Restrict access to content with digital rights management (DRM) solutions.**

In addition to the access-control based approach, you can also take an encryption-based approach by encrypting your private content and distributing the decryption keys to authorized players using a digital rights management (DRM) solution. DRM solutions are recommended in situations where you want to allow players to download game content early, but you do not want them to be able to be able to access or play the content until a predetermined time. For example, this is common in situations, typically in PC games, where players are allowed to pre-order a game and conﬁgure their game client to automatically begin downloading the encrypted ﬁles early so that it is downloaded and ready to be played when the game is oﬃcially released. After the game is released, the player's game client can request decryption keys from the DRM backend solution so that it can decrypt the previously downloaded ﬁles and begin playing the game. DRM systems are also used as a way to prevent unauthorized re-distribution and manipulation of games after they have been downloaded and installed by an authorized player. DRM systems require integration with the origin for exchanging encryption keys and authorizing players to retrieve the decryption key. Commercial DRM systems providers oﬀer a range of solutions with particular features and support for diﬀerent devices.
