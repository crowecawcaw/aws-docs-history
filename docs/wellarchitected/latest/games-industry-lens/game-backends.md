# Game backends

Game backends are used to manage game and player state, as well as
integrate social and system-level features into the game that
support the gaming experience. Player profile management, item and
inventory storage, and stats and leaderboards are examples of
services hosted in game backends.

Game backends are typically built as REST APIs that are accessed
by clients using HTTPS. However, other approaches are also common,
such as WebSockets that provide bidirectional channels for use
cases such as client notifications for in-game chat and presence.
Game backends can be deployed using a variety of different
deployment architectures, including using instances, containers,
or a serverless architecture.
