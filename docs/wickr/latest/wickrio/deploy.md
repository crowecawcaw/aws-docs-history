This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Deploy

In this section you can deploy your custom integration using the Wickr IO Docker
container. These commands should be run on a host which has Docker installed, access to the
internet, and has the `software.tar.gz` archive for your custom integration on its
file system.

If you haven't already created your bot user in the AWS Wickr console, do that now.
You'll need the bot username and password in order to register your bot user for your new
custom integration.

## Create a bot data directory

Complete the following procedure to create a bot data directory.

1. On your server, create a new directory for all of the files which will be associated
   with your bot. In this directory, you will place the `software.tar.gz` file,
   a client configuration file, and a directory to hold all of the data for the Wickr IO
   container.

```

mkdir -p emoji-bot/data
cd emoji-bot
cp ../path/to/software.tar.gz . # Update this path to the correct location

```

2. Create a file named `clientConfig.json` which contains the information
   needed to start your bot. Replace `BOT_USERNAME` and
   `BOT_PASSWORD` with the credentials for your bot.

```

{
  "clients": [
    {
      "integration": "wickrio-emoji-bot",
      "name": "BOT_USERNAME",
      "password": "BOT_PASSWORD",
      "tokens": []
    }
  ]
}

```

Your directory should have the following structure:

```

.
├── clientConfig.json  # Your bot client's configuration file
├── data               # The data directory for the WickrIO container
└── software.tar.gz    # Your custom integration code

```

## Start the container

You can now start the Wickr IO container to bring your new custom integration online.
The directory which the `software.tar.gz` file is mounted to must match the
integration named supplied in your `clientConfig.json` file.

In the example, the integration is named `wickrio-emoji-bot`. The tarball
must be mounted to `/usr/lib/wickr/integrations/software/wickrio-emoji-bot/` .

```

docker run -d --restart=always \
    -v ./data:/opt/WickrIO \
    -v ./clientConfig.json:/usr/local/wickr/WickrIO/clientConfig.json:ro \
    -v ./software.tar.gz:/usr/lib/wickr/integrations/software/wickrio-emoji-bot/software.tar.gz:ro \
    public.ecr.aws/x3s2s6k3/wickrio/bot-cloud:latest

```

You can now interact with your new integration by sending it the `/emoji`
command in your AWS Wickr client.
