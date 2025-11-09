# Introduction to IVS Real-Time

Streaming

This section lists prerequisites for using real-time streaming and introduces key
terminology.

## Prerequisites

Before you use Real-Time Streaming for the first time, complete the following
tasks. For instructions, see [Getting Started with
IVS Low-Latency Streaming](../LowLatencyUserGuide/getting-started.md "../LowLatencyUserGuide/getting-started.md").

- Create an AWS Account
- Set Up Root and Administrative Users

## Other References

- [IVS Web Broadcast SDK Reference](https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference "https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-reference")
- [IVS Android Broadcast SDK Reference](https://aws.github.io/amazon-ivs-broadcast-docs/latest/android/ "https://aws.github.io/amazon-ivs-broadcast-docs/latest/android/")
- [IVS iOS Broadcast SDK Reference](https://aws.github.io/amazon-ivs-broadcast-docs/latest/ios/ "https://aws.github.io/amazon-ivs-broadcast-docs/latest/ios/")
- [IVS Real-Time Streaming API Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md")

## Real-Time Streaming

Terminology

| Term              | Description                                                              |
| ----------------- | ------------------------------------------------------------------------ |
| Stage             | A virtual space where participants can exchange video in real<br>time.   |
| Host              | A participant that sends local video to the stage.                       |
| Viewer            | A participant that receives video of the hosts.                          |
| Participant       | A user connected to the stage as a host or viewer.                       |
| Participant token | A token that authenticates a participant when they join a<br>stage.      |
| Broadcast SDK     | A client library that enables participants to send and receive<br>video. |

## Overview of Steps

1. [Set up IAM
   Permissions](getting-started-iam-permissions.md "getting-started-iam-permissions.md") — Create an AWS Identity and Access Management (IAM)
   policy that gives users a basic set of permissions and assign that policy to
   users.
2. [Create a stage](getting-started-create-stage.md "getting-started-create-stage.md") —
   Create a virtual space where participants can exchange video in real
   time.
3. [Distribute participant
   tokens](getting-started-distribute-tokens.md "getting-started-distribute-tokens.md") — Send tokens to participants so they can join your
   stage.
4. [Integrate the IVS Broadcast
   SDK](getting-started-broadcast-sdk.md "getting-started-broadcast-sdk.md") — Add the broadcast SDK to your app to enable participants to
   send and receive video: [Web](getting-started-broadcast-sdk.md#getting-started-broadcast-sdk-web "getting-started-broadcast-sdk.md#getting-started-broadcast-sdk-web"),
   [Android](getting-started-broadcast-sdk.md#getting-started-broadcast-sdk-android "getting-started-broadcast-sdk.md#getting-started-broadcast-sdk-android"), and [iOS](getting-started-broadcast-sdk.md#getting-started-broadcast-sdk-ios "getting-started-broadcast-sdk.md#getting-started-broadcast-sdk-ios").
5. [Publish and subscribe to
   video](getting-started-pub-sub.md "getting-started-pub-sub.md") — Send your video to the stage and receive video from other
   hosts: [IVS console](getting-started-pub-sub.md#getting-started-pub-sub-console "getting-started-pub-sub.md#getting-started-pub-sub-console"),
   [Publish & Subscribe with the IVS
   Web Broadcast SDK](getting-started-pub-sub-web.md "getting-started-pub-sub-web.md"), [Publish & Subscribe with the
   IVS Android Broadcast SDK](getting-started-pub-sub-android.md "getting-started-pub-sub-android.md"), and [Publish & Subscribe with the IVS
   iOS Broadcast SDK](getting-started-pub-sub-ios.md "getting-started-pub-sub-ios.md").
