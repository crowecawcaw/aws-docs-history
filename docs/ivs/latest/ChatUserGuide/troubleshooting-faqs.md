# Troubleshooting IVS Chat

This document describes best practices and troubleshooting tips for Amazon Interactive
Video Service (IVS) Chat. Behaviors related to IVS Chat often are distinct from behaviors related to IVS video.
For more information, see [Getting Started with
Amazon IVS Chat](getting-started-chat.md "getting-started-chat.md").

Topics:

- [Why were IVS chat connections
  not disconnected when the room was deleted?](#chat-connections-not-disconnected "#chat-connections-not-disconnected")

## Why were IVS chat connections

not disconnected when the room was deleted?

When a chat-room resource is deleted, if the room is actively being used, the chat
clients that are connected to the room are not automatically disconnected. The
connection is dropped if/when the chat application refreshes the chat token.
Alternately, a manual disconnect of all users must be done to remove all users from
the chat room.
