# Setting up AWS Elemental MediaLive Anywhere

Read this section if you plan to deploy AWS Elemental MediaLive Anywhere, which lets you run MediaLive channels on
on-premises hardware located in your organization's data center. The MediaLive channels can include
standard MediaLive inputs, but can also include inputs such as SDI inputs that apply only to MediaLive Anywhere.

This section describes how to integrate the on-premises nodes into your organization's
network and how to configure MediaLive Anywhere to organize nodes into clusters connected to your
network.

MediaLive Anywhere uses a shared-responsibility model. You are responsible for securing access to your
node to protect the fidelity of the running channels and the published logs and metrics. AWS is
responsible for managing the encoding traffic and for managing the software, including
continually upgrading the software. For more information about the shared-responsibility model,
see [Security in AWS Elemental MediaLive](security.md "security.md").
