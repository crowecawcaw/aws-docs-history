# Definitions

The AWS Well-Architected Framework is based on five pillars: operational excellence, security, reliability,
performance efficiency, and cost optimization. AWS provides multiple core components that allow you to design
state-of-the-art architectures for your game workloads. In this section, we will present an overview of key definitions.

For the purposes of this paper, a game architecture encompasses the backend technical
infrastructure required to build and operate a game. Some games might not have social,
multiplayer, or other online features and might not require the use of certain aspects of
backend technical infrastructure that are described in this paper. Refer to [Scenarios](games-scenarios.md "games-scenarios.md") for a detailed discussion of the different types
of workloads that are frequently deployed to support a game architecture.

The AWS Cloud is built around _AWS Regions_ and
_Availability Zones_. A Region is a physical location in the world where
we have multiple Availability Zones. Availability Zones consist of one or more discrete data
centers, each with redundant power, networking, and connectivity, housed in separate
facilities. Depending on the characteristics of your game, you might want to deploy certain
components of your game architecture into multiple Regions to improve performance for players,
or to deliver customized experiences for players based on their location.

There are many different types of games and the backend technical infrastructure that is
required to support a game will differ depending on the type of game being developed. Popular
types of games include first person shooter (FPS), role playing (RPG), multiplayer online
(MMO), Battle Royale (BR), sports games, and puzzle games. There are also different game
interaction modes that influence the architecture of the game, such as turn-based or
simultaneous play, with very different performance characteristics.

Games are developed to be played on one or more gaming platforms including desktop, web,
mobile, and consoles. They also might feature newer interaction modes, such as augmented
reality (AR), virtual reality (VR), and game streaming platforms. It is becoming a common
trend for games to support cross-platform gameplay, which means that players can save their
game progression and resume gameplay on other platforms. They can also initiate gameplay
sessions with players on other platforms. Video game monetization enables game publishers to
generate revenue using different strategies such as by advertising, digital and retail-based
game purchases, in-game purchases of downloadable content (DLC), known as microtransactions,
and through required paid subscriptions to play the game. Some of the most common key
performance indicators (KPIs) in the games industry include daily active users (DAU), monthly
active users (MAU), concurrent users (CCU), session duration, cost per install (CPI), player
lifetime value (LTV), and variations of average revenue per user (ARPU).

###### Topics

- [Gaming platform](gaming-platform.md "gaming-platform.md")
- [Game server](game-server.md "game-server.md")
- [Game client](game-client.md "game-client.md")
- [Messaging](messaging.md "messaging.md")
- [Live game operations (Live Ops)](live-ops.md "live-ops.md")
