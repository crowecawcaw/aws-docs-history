# Managing your streams with Amazon GameLift Streams

This section provides detailed information about how to stream with Amazon GameLift Streams. Learn about
the streaming resources (an _application_ and _stream group_), the properties to scale your streaming (_stream capacity_ and _locations_),
and the stream itself (a _stream session_). You can handle
all of the tasks required to set up streaming with Amazon GameLift Streams by using the Amazon GameLift Streams console or
Amazon GameLift Streams CLI commands.

If it's your first time using Amazon GameLift Streams, then refer to [Starting your first stream in Amazon GameLift Streams](streaming-process.md "streaming-process.md"), which walks you through the whole workflow.

###### Topics

- [Key concepts](#about-streaming-resources "#about-streaming-resources")
- [Prepare an application in Amazon GameLift Streams](applications.md "applications.md")
- [Manage streaming with an Amazon GameLift Streams stream group](stream-groups.md "stream-groups.md")
- [Overview of multi-application stream groups](multi-apps.md "multi-apps.md")
- [Start stream sessions with Amazon GameLift Streams](stream-sessions.md "stream-sessions.md")
- [Export stream session files](stream-sessions-export-files.md "stream-sessions-export-files.md")

## Key concepts

**Application**

An Amazon GameLift Streams application is a resource that contains a game or interactive application that runs on Amazon GameLift Streams infrastructure and delivers gameplay experiences to players
through cloud streaming. The application executes on AWS compute instances and renders game content that is streamed directly to players' devices over the internet, eliminating
the need for players to download, install, or run the game locally.

**Multi-application stream groups**

A stream group that's linked to multiple applications. This many-to-one relationship allows you to stream multiple applications by using the same configuration that you've set up in a single stream group . When you start a stream session, you specify any linked applications. Then, Amazon GameLift Streams streams that application by using available stream capacity in this stream group.

**Multi-location stream groups**

A stream group that's configured to host applications and stream sessions from multiple locations, in addition to the primary location (the AWS Region where you created the stream group).
You manage capacity for each location.

**Multi-tenancy**

_Tenancy_ refers to how many concurrent streams can be supported by a single compute resource in Amazon GameLift Streams.
_Multi-tenancy_ is a feature that enables multiple users to share the same underlying hardware
resources, which can be a cost-effective option for applications that don't require maximum hardware capabilities. A stream
class with multi-tenancy can host multiple streams for the cost of one resource. "High" stream classes support multi-tenancy,
allowing two applications to run concurrently on a single compute resource, while "Ultra" stream classes do not support
multi-tenancy.

**Stream group**

Manage how Amazon GameLift Streams streams your applications by using a stream group. A stream group is a collection of compute resources that Amazon GameLift Streams uses to stream your application to end users.
When you create a stream group, you specify the hardware configuration (CPU, GPU, RAM) that will run your game (known as the _stream class_),
the geographical locations where your game can run,
and the number of streams that can run simultaneously in each location (known as _stream capacity_).
You can link an application when you create the stream group, or wait until later, but you must link at least one application before you can stream from a stream group.
After a stream group has been created, Amazon GameLift Streams allocates compute resources in the locations where you have allocated stream capacity.
At this point, you can also associate additional applications to the stream group so that you have a choice of which one to stream.

**Stream capacity**

Represents
the number of concurrent streams that can be active at a time. You set stream capacity per location in each stream group.
At each location, there are two types of capacity: always-on capacity and on-demand capacity.

**Stream session**

Refers to the stream itself. This is an instance of a stream that Amazon GameLift Streams transmits from the server to the end-user. A stream session runs on a compute resource, or stream capacity, that a stream group has allocated.
Also referred to as _stream_ for short.
