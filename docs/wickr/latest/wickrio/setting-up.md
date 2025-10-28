This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Setting up for Wickr IO

This section is intended for systems administrators and/or developers to deploy a
Wickr-provided bot within their Wickr network or to build and integrate a custom bot of their
own.

The following sections will be of interest to all users:

- [Quick start](quick-start.md "quick-start.md"): Describes a quick guide from creation to running and
  interacting with your Wickr bot clients.
- [Available Bot Integrations](available-bot-integrations.md "available-bot-integrations.md"): Contains descriptions of current Wickr IO integrations
  that you can use.
- [Wickr IO Command
  Line Interface (CLI)](cli-commands.md "cli-commands.md"): Describes all of the commands that are available from the Wickr
  IO command line interface.
  Developers have access to several levels of APIs when developing Wickr IO integration
  software. Familiarity with all aspects of the Wickr IO system will be helpful when developing
  Wickr IO integrations. The following sections give details on the available APIs and any other
  integration components you will need to deal with:

- [Wickr IO
  Node.js Addon API](nodejs-addon-api.md "nodejs-addon-api.md"): The main software API you will use to access the Wickr messaging
  capabilities.
- [Wickr IO bot
  API](nodejs-bot-api.md "nodejs-bot-api.md"): A higher level software API that provides additional capabilities above the main
  addon APIs, basically a bot development toolkit.
- [Integration
  setup](integration-setup.md "integration-setup.md"): Information about integration software modules you will need to maintain that
  will be used to integrate your Wickr IO integration into the Wickr IO Integration
  Gateway.
- [Wickr IO Web Interface Integration:](webinterface-integration.md "webinterface-integration.md") Information about how to use the REST API as a
  way to integrate your software.
  If you are planning on developing Wickr IO integrations, you should read this entire
  document. Administrators may skip the development sections.

## Installation

Once you have a host machine setup and Docker installed, the installation of Wickr IO
software is as simple as pulling the appropriate Wickr IO Docker container. For more
information on using Docker, see [Get Started
with Docker](https://www.docker.com/get-started/ "https://www.docker.com/get-started/").

The Wickr IO Docker images are hosted on Public ECR. You can pull down the Wickr IO
Docker image located at the following public ECR repository:

[Wickr IO bot
cloud](https://gallery.ecr.aws/x3s2s6k3/wickrio/bot-cloud "https://gallery.ecr.aws/x3s2s6k3/wickrio/bot-cloud").

The docker image can be pulled down to the host machine using the following command:

```

docker pull public.ecr.aws/x3s2s6k3/wickrio/bot-cloud:latest

```

###### Note

Depending on your use case, you may want to pull a particular version. For more information
on available versions, see [Wickr IO bot cloud](https://gallery.ecr.aws/x3s2s6k3/wickrio/bot-cloud "https://gallery.ecr.aws/x3s2s6k3/wickrio/bot-cloud").

In case, you do not have access to public ECR, the docker image can also be pulled down,
from the [Dockerhub repository](https://hub.docker.com/r/wickr/bot-cloud "https://hub.docker.com/r/wickr/bot-cloud"), to
the host machine using the following command:

```

docker pull wickr/bot-cloud:latest

```

###### Note

The Docker Hub repository will soon be deprecated and the bot images will only be available
on public ECR.

## Wickr IO Components

The Wickr IO Docker container contains the Wickr IO client software and the client
service and configuration software. The Wickr IO client, as opposed to the Wickr client,
provides a software interface (API) to the Wickr capabilities, instead of through a graphical
user interface (GUI). This software interface can be leveraged either through the native Node.js
add-on APIs or an optional REST API (using the Web Interface integration) to provide the ability
to send and receive messages, as well as create secure rooms and group conversations.

The Wickr IO bot software is distributed as a Docker image. There are different Docker
images depending on the type of Wickr environment you are using. Each Wickr IO Docker
container has the following components:

- **Wickr IO client**: The Wickr IO client is a Wickr client that
  interacts with integration software through an API. Using this software API, the integration
  software can access the Wickr messaging capabilities. The Wickr IO client is associated
  with a Wickr user account and interacts with other Wickr clients as a Wickr bot
  user.
- **Wickr IO Node.js API**: This software provides an API that allows
  native Node.js programs (integrations) to interact with the Wickr IO client. This software is
  distributed via the public Node Package Manager (NPM) registry. For more information, see
  [Node.js Addon
  API](nodejs-addon-api.md "nodejs-addon-api.md").
- **Wickr IO Integration Software**: The Wickr IO integration software
  is written using Node.js and uses the Wickr IO Node-js add-on API to implement the
  integration functionality. The Wickr IO Bot Docker container includes a few Wickr IO
  integrations that are maintained by AWS Wickr team, and a few sample integrations are
  available on the public NPM Registry. You can use the sample integrations as examples to build
  your own. For more information, see [Available Bot
  Integrations](available-bot-integrations.md "available-bot-integrations.md").
- **Wickr IO console**: This console software provides a command line
  interface that is used to maintain the operation of your Wickr IO clients. The command line
  interface supports adding, modifying, deleting Wickr IO clients and the associated
  integration software. You will also use the command line interface to start and stop running
  the Wickr IO clients. For more information, see [CLI commands](cli-commands.md "cli-commands.md").
