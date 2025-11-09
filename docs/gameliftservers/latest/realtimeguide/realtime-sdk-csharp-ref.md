# Amazon GameLift Servers Realtime client API (C#) reference

Use this reference guide to understand how to implement Realtime client API functionality into your
multiplayer game clients. For guidance on how to integrate
this API into your game clients, see [Integrate a game client for Amazon GameLift Servers Realtime](realtime-client.md "realtime-client.md").

The Realtime client API includes a set of synchronous API calls
and asynchronous callbacks that enable a game client to connect to a Realtime server and
exchange messages and data with other game clients via the server.

This API is defined in the following libraries:

Client.cs

- [Synchronous actions](realtime-sdk-csharp-ref-actions.md "realtime-sdk-csharp-ref-actions.md")
- [Asynchronous
  callbacks](realtime-sdk-csharp-ref-callbacks.md "realtime-sdk-csharp-ref-callbacks.md")
- [Data types](realtime-sdk-csharp-ref-datatypes.md "realtime-sdk-csharp-ref-datatypes.md")

###### To set up the Realtime client API

1. **Download the [Amazon GameLift ServersRealtime client
   SDK](https://aws.amazon.com/gamelift/getting-started "https://aws.amazon.com/gamelift/getting-started").**
2. **Build the C# SDK libraries.** Locate the solution
   file `GameLiftRealtimeClientSdkNet45.sln`. See the
   `README.md` file for the C# Server SDK for minimum
   requirements and additional build options. In an IDE, load the solution file. To
   generate the SDK libraries, restore the NuGet packages and build the
   solution.
3. **Add the Realtime Client libraries to your game client
   project.**
