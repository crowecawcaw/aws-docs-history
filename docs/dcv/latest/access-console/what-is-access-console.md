# What is Amazon DCV Access Console?

###### Note

Amazon DCV was previously known as NICE DCV.

The Amazon DCV Access Console is a web application that helps administrators and end users manage
their Amazon DCV sessions. The Access Console consists of installable software packages that
include a Handler, an Authentication Server, and a Web Client configured to provide a
graphical interface.

The Access Console provides administrators with the following:

- Access to the Amazon DCV Session Manager APIs
- The ability to monitor the host servers running their sessions
- Tools to manage the users who have access to the console
  The Access Console provides end users a way to connect, manage, and launch their own Amazon DCV sessions.

###### Topics

- [How Amazon DCV Access Console works](#how "#how")
- [Features](#features "#features")
- [Limitations](#limitations "#limitations")
- [Pricing](#pricing "#pricing")
- [Requirements](requirements.md "requirements.md")
- [Authentication methods](console-authentication.md "console-authentication.md")
- [Datastore](datastore.md "datastore.md")
- [Certificates](certificates.md "certificates.md")
- [Networking and
  connectivity](networking-connectivity.md "networking-connectivity.md")
- [Open source code](open-source.md "open-source.md")

## How Amazon DCV Access Console works

The following system architecture diagram shows the high-level components of the Amazon DCV Access Console and how they work with each other.

![Amazon DCV Access Console components and how they work with each other.](images/access-console-diagram.png)

Handler

The _Handler_ is an application that helps connect to and manage Amazon DCV sessions by
communicating with the _Session Manager Broker_ using the _Session Manager APIs_.

Authentication Server

The _Authentication Server_ is responsible for
authenticating users using Header based or PAM authentication
methods.

Web Client

The client is the front-end web application you setup to interact with the
_Handler_ (and in turn with the _Session
Manager Broker_). It renders the relevant web pages and serves
to the _Web Browser_.

Session Manager Broker

The _Broker_ is a web server that hosts and exposes the
Session Manager APIs. It receives and processes _API_
requests to manage Amazon DCV sessions from the _client_, and
then passes the instructions to the relevant _Agents_.
The Broker must be installed on a host that's separate from your Amazon DCV
servers. It must also be accessible to the client, and be able to access the
Agents.

## Features

Amazon DCV Access Console offers the following features:

- **Provides Amazon DCV session information**–get information
  about the sessions running on multiple Amazon DCV servers.
- **Manage the lifecycle for multiple Amazon DCV sessions**–create or
  delete multiple sessions for multiple users across multiple Amazon DCV servers with one API request.
- **Supports tags**–use custom tags to target a group of
  Amazon DCV servers when creating sessions.
- **Manages permissions for multiple Amazon DCV sessions**–modify
  user permissions for multiple sessions with one API request.
- **Provides connection information**–retrieve client
  connection information for Amazon DCV sessions.
- **Supports for cloud and on-premises**–use Session Manager on
  AWS, on-premises, or with alternative cloud-based servers.

## Limitations

Amazon DCV Access Console does not provide resource provisioning capabilities. If you are
running Amazon DCV on Amazon EC2 instances, you might need to use additional AWS services, such
as Amazon EC2 Auto Scaling to manage the scaling of your infrastructure.

## Pricing

Amazon DCV Access Console is available at no cost for AWS customers running EC2
instances.

On-premises customers require a Amazon DCV Plus or Amazon DCV Professional Plus license. For
information about how to purchase a Amazon DCV Plus or Amazon DCV Professional Plus license, see
[How to Buy](https://www.nice-software.com/index.html#buy "https://www.nice-software.com/index.html#buy") on the
Amazon DCV website. You can also use the website to find an Amazon DCV distributor or reseller in
your region. Licensing requirements will only be enforced starting with Amazon DCV version
2021.0,so that all on-premises customers can experiment with the Amazon DCV Access
Console.

For more information, see [Licensing the Amazon DCV
Server](../adminguide/setting-up-license.md "../adminguide/setting-up-license.md") in the _Amazon DCV Administrator Guide_.
