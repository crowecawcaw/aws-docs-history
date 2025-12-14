# Definitions

The AWS Well-Architected Framework is based on six pillars: operational excellence,
security, reliability, performance efficiency, cost optimization, and sustainability. AWS
provides multiple core components that allow you to design state-of-the-art architectures for
your game workloads. In this section, we will present an overview of key definitions.

For the purposes of this paper, a game architecture encompasses the backend technical
infrastructure required to build and operate a game. Some games may not have social,
multiplayer, or other online features and may not require the use of certain aspects of backend
technical infrastructure that are described in this paper. For a detailed discussion of the
different types of workloads that are frequently deployed to support a game architecture, see
Scenarios.

The AWS Cloud infrastructure is built around Regions and Availability Zones.

- A _Region_ is a physical location in the world where we have
  multiple Availability Zones.
- _Availability Zones_ consist of one or more discrete data centers, each
  with redundant power, networking, and connectivity, housed in separate facilities.
  Depending on the characteristics of your game, you may want to deploy certain components of
  your game architecture into multiple Regions for reasons such as improving performance for
  players, or to deliver customized experiences for players depending on their location.

There are many different types of games, and the backend technical infrastructure required
to support a game differs depending on the type of game being developed. For example, popular
types of games may include first person shooters (FPS), role playing games (RPG), massively
multiplayer online games (MMOG), battle royales (BR), sports games, puzzle games, and more.
There are also different game interaction modes that influence the architecture of the game,
such as turn-based and simultaneous play, with different performance characteristics.

Games are developed to be played on one or more gaming systems including desktop, web,
mobile, consoles, and newer interaction modes such as augmented reality (AR), virtual reality
(VR), and game streaming solutions. Games commonly support cross-system gameplay, which means
that players can save their game progression and resume gameplay on other systems, as well as
initiate gameplay sessions with players on other systems.

Video game monetization enables game publishers to generate revenue using different
strategies like advertising, digital and retail-based game purchases, in-game purchases of
downloadable content (DLC) known as microtransactions, and through required paid subscriptions
to play the game. Some of the most common key performance indicators (KPIs) in the games
industry include:

- Daily active users (DAU)
- Monthly active users (MAU)
- Concurrent users (CCU)
- Session duration
- Cost per install (CPI)
- Player lifetime value (LTV)
- Average revenue per user (ARPU)

## Gaming system

Video games are developed to be played on a gaming system that provides client input
controls, graphics, client software (known as the game client) and hardware, and in some cases
system-exclusive features to support gameplay.

Gaming systems are generally separated into the following categories:

- **Consoles**: Purpose-built entertainment systems that are
  designed for playing games, including popular examples such as the Sony PlayStation,
  Microsoft Xbox, and Nintendo Switch. Consoles provide the ability to play games by
  installing physical or digitally distributed game content onto the console hardware that
  is manufactured by the gaming system provider. In this definition, a console may be
  handheld or stationary and intended to be used in a home entertainment scenario.
- **Personal computer (PC)**: Games that are played using
  computer software that is installed onto a client machine that can be customized by the
  player. For this reason, PC gaming is popular among players because of the flexibility and
  control that it provides.
- **Web**: Games that are designed to be played using a web
  browser and which usually provide the benefit of enabling a player to access the game
  irrespective of their operating system.
- **Mobile:** Games that are developed to be played on a mobile
  phone, usually a smartphone operating system. Mobile games are usually downloaded from a
  digital app store and installed onto the phone.

In addition to the previously mentioned systems, there are also nascent systems that are
still relatively new and growing and have much smaller market share compared to the more
predominant systems. Examples of gaming systems in this category include AR, VR, and game
streaming, sometimes referred to as cloud gaming.

_Game streaming_ involves rendering the gameplay in the cloud and streaming
to thin client, typically a browser. Game streaming allows a player to play a game that is
entirely hosted remotely, typically in the cloud by a game streaming service provider. In game
streaming, the player connects to a cloud-based game through a browser or a thin client
provided by the cloud gaming service provider (gaming system).

## Game server

Game servers represent one of the most important aspects of the compute infrastructure
for your game. Game servers, sometimes referred to as dedicated game servers, are used when
developing a multiplayer game or when server authoritative processing of gameplay events is
required. The game server is at the center of the game architecture, serving as the location
where the core logic runs, which includes managing player and game state as well as managing
the interactions between the connected game clients and the game server. The game server is
usually one of the most performance-sensitive aspects of a game architecture because it is
responsible for processing the inputs from a player's game client and properly distributing it
to other connected players in real-time. A poorly performing game server impacts the overall
performance of the game experience. Therefore, you should optimize game server performance and
provide sufficient capacity, especially at game launch or peak gameplay periods.

For the purposes of this document, a game server or game server instance refers to the
compute, such as a virtual machine, that hosts one or more game server processes. A game
server process represents a single instance of your game server build hosting a game session,
which is an instance of your running game that players can connect to through a player
session. For this reason, we often refer to game server process or game session
interchangeably due to the implied one to one relationship between a game session and the game
server process that is hosting it. In AWS, there are multiple options for compute to host
game servers, which provide access to scalable cloud-based capacity through elastic
provisioning of resources.

Amazon EC2 provides cloud-based virtual servers, known as instances, with support for multiple
versions of Linux and Windows. You can create instances and manage them directly like another
server or virtual machine. Typically, multiple game server processes are deployed to an
instance to improve efficiency and reduce costs. Amazon EC2 is a good choice for game servers if
you desire the most control over the compute infrastructure.

Amazon GameLift provides a fully managed solution for dedicated game server hosting in
the cloud as well as additional features such as matchmaking with GameLift FlexMatch. GameLift
provides a layer of abstraction on top of Amazon EC2 to make game server management straightforward
and is available in most AWS Regions so that you can host game servers close to players to
reduce latency, achieve high availability, and significantly reduce costs by using Spot
Instances. While GameLift can be integrated into existing game backends, it is especially
useful for game developers who do not want to develop their own game server management and
matchmaking solutions and prefer a solution that is managed by AWS and can scale as their
game grows.

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that you can use to
run Docker-based containers. You can also use Amazon Elastic Kubernetes Service (Amazon EKS) to run Docker-based containers
that are built using Kubernetes. Using container technologies such as those provided by Amazon ECS
and Amazon EKS can assist you to improve your compute utilization by efficiently packing many game
server processes or other game application instances into an EC2 instance.

The use of containers can also improve developer productivity by hosting applications
using the same Docker image operating runtime used by developers on their local machines
during development. You can further reduce operational overhead by using AWS Fargate, which
is a serverless compute solution for running containers and is compatible with both Amazon EKS and
Amazon ECS. Fargate is best suited for use cases where you want to run game servers in containers
without responsibility for operating the underlying instances that the containers run on.

You can use AWS Outposts to run AWS infrastructure and services in a data center or
on-premises facility, which can enable games to run in on-premises environments and AWS
using the same infrastructure to support a hybrid cloud adoption strategy. AWS Local Zones
serve as extensions of AWS Regions that allow your game servers and other latency-sensitive
workloads to run more closely to your players or development teams. Additionally, to reduce
global network latency for your game servers, you can use AWS Global Accelerator to improve performance
for player traffic to your game servers.

AWS Lambda is a serverless compute service that runs code without provisioning or managing
servers, which makes it useful for asynchronous game server use cases such as turn-based games
or those that have lightweight compute requirements, a small codebase, and where gameplay
functionality can be designed using a stateless microservices architecture. It is important to
keep in mind that Lambda functions run on an event-driven, per-request basis, rather than
running a long-running game server process. Lambda provides the most runtime abstraction of the
options in this paper because the underlying application is readily available for developers
to choose from to host their code.

When selecting your approach for game server hosting, consider various requirements
including operational overhead, legacy codebases, performance requirements, and scale. EC2
instances and containers are good options for legacy codebases, as they require the smallest
change to move to the cloud, and you can use EC2 instances to dedicate the resources of a
compute instance, while containers can make management and high utilization simpler to
achieve. Serverless functions offer the highest level of abstraction, which you can use to
define code that only runs in response to events, which can reduce costs.

## Game client

The _game client_ represents the software and hardware device that the
player uses for playing a game. The game client provides the software for translating the
player's inputs into messages that are sent to a server for processing, and it is responsible
for handling the incoming responses from the server and rendering outputs such as graphics to
the player. In real-time networked multiplayer games, the game client usually maintains a
persistent network connection to a game server for the duration of a gameplay session to
reduce network latency and minimize processing time. However, the game client may also
interact using REST with a game server or backend services.

## Messaging

There are typically three primary categories of messages in games: 

- **Player engagement messaging** targeted at a specific user
  or cohort of users, such as game invites or push notifications
- **Group messaging** between players such as in-game chat
- **Service-to-service** messaging, such as JSON messages used
  to integrate two or more applications

A common strategy for sending and receiving these types of messages is to use
publisher-subscriber and asynchronous processing architecture patterns. AWS provides several
services that can assist you to implement messaging in your game.

- **Amazon Simple Notification Service (SNS):** Managed service for delivering messages
  between publishers and subscribers using a pub/sub architecture pattern. Publishers send
  messages using an API to Amazon SNS, which delivers the messages asynchronously to subscribing
  applications and can deliver push notifications directly to mobile clients or desktops
  with support for some of the most widely used push notification services. Amazon SNS can be
  used for push notifications to clients as well as service-to-service messaging use cases.
- **Amazon Simple Queue Service (SQS)**: A fully managed queue service that makes
  it straightforward to integrate game servers and your game regardless of the programming
  language used in each. Many games tasks can be decoupled and handled in the background
  such as updating a leaderboard or playtime values in a database. This approach is an
  effective way to decouple various parts of your game and independently scale the
  player-facing features from backend processing.
- **Amazon Managed Streaming for Apache Kafka (MSK)**: A fully managed service that simplifies
  building data streaming and producer or consumer applications using Apache Kafka, a
  popular open-source solution. Kafka is typically used for ingesting and processing
  real-time streaming data and can be used for service-to-service messaging.
- **Amazon ElastiCache (Redis OSS):** Provides a fully managed in-memory data store
  which includes support for the popular pub/sub feature of Redis that is commonly used for
  developing chat room applications and high-performance service-to-service messaging. Redis
  also supports rich data types such as lists and sets so that developers can use Redis for
  high-performance queuing.
- **Amazon Pinpoint:** Provides user engagement messaging through
  email, SMS, voice, and push notifications. For example, Amazon Pinpoint can be used to deliver
  user engagement messages to players to invite them back to the game and can be used for
  transactional use cases such as supporting multi-factor authentication tokens, order
  confirmations, and password reset emails.

## Live game operations (Live Ops)

_Live game operations_ (Live Ops) is a style of game management and
operations that treats a game as a live service and continually delivers new features,
updates, promotions, in-game events, and improvements to the launched game to improve the
experience for the player community.

Traditionally, games were delivered as products rather than services, and new content and
features were frequently incorporated into subsequent releases or sequels rather than into the
launched product. With a Live Ops approach to game management, a game operations team can
launch a game and maintain an engaged player community through experimentation, promotions,
in-game events, and innovation to keep players entertained.

Although this approach has the benefit of unlocking new player engagement strategies and
delivering recurring revenue streams, it requires more operational expertise. For example, to
implement a successful Live Ops strategy, a developer may need to integrate with cloud
services or operate their own backend technical infrastructure. They also need an effective
way to identify and respond to issues that arise in the game, or within the player community,
that can negatively impact the player experience.
