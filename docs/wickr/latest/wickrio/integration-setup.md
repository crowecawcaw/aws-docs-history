This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Integration setup

Complete the following procedure to setup a new custom Wickr IO integration.

1. Create a new directory and install the Wickr IO bot API with NPM.

```

mkdir wickrio-emoji-bot
cd wickrio-emoji-bot
npm install wickrio-bot-api

```

2. In the root directory of your new package, create a file named
   `processes.json` with the following contents:

```
{
  "apps": [
    {
      "name": "wickrio-emoji-bot",
      "env": {
        "tokens": {}
      }
    }
  ]
}


```

This file is used by the Wickr IO bot API library to provide custom configuration
for your integration. Values provided in the `env.tokens` property will be set
as environment variables in your integration. 3. In addition to the `processes.json` file, you need to create the following
two scripts in order for your bot to start up successfully:

    1. **install.sh**


    This file is required when creating the bot. There are no special install time
     requirements, you can exit with a successful status (0).



    ```

    #!/bin/sh
    exit 0

    ```
    2. **start.sh**


    This script is used by the Wickr IO integration to start your bot. The code that
     is created below will be in the file `index.js`. Configure the startup
     script to run this file.



    ```

    #!/bin/bash
    node index.js "$@"

    ```

4. Make these scripts executable by running `chmod`:

```

chmod +x {install,start}.sh

```

5. Next, create an `index.js` file which serves as the main entrypoint for our
   bot:

```

// index.js
const WickrIOBotAPI = require('wickrio-bot-api')

const bot = new WickrIOBotAPI.WickrIOBot()
const WickrIOAPI = bot.apiService().WickrIOAPI

async function listen() {}

async function main() {
  const username = process.argv[2]
  if (!username) throw new Error('Missing username')

  const status = await bot.start(username)
  if (!status) throw new Error('Unable to start bot')

  bot.startListening(listen);
}

main()

```
