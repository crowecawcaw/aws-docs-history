# Setting up a MediaConnect Router input

This section describes how to create a MediaConnect Router input. With a MediaConnect Router input,
the service provider pushes content through AWS Elemental MediaConnect to MediaLive. (From the point of view
of MediaLive, the upstream system is MediaConnect. The upstream system is not the service
provider.)

To perform this setup, you must work with an AWS Elemental MediaConnect user or a user with rights to both services.

It's important to note there are several considerations to consider when you want to use a MediaConnect Router input.

- First, a MediaConnect Router Input can not be updated. That means its settings are set at creation.
- Second, you cannot delete the MediaConnect Router Input if its connected to a router output in MediaConnect.
- Finally, a MediaConnect Router Input can only be attached to one router output in MediaConnect.

###### Topics

- [Create a MediaConnect Router input](setup-input-mediaconnect-router.md "setup-input-mediaconnect-router.md")
