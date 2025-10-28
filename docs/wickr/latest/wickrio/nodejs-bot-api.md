This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Node.js Bot API (Development toolkit)

This section describes the Wickr IO Node.js Bot API framework and how to use it with
several examples. This API provides tools for easier and more efficient development of Wickr IO
integration bots. It utilizes the Wickr IO Node.js addon APIs to make it easier to develop
integrations.

The Wickr IO Node.js Bot API is published to the default NPM registry. The name of the
published module is `wickrio-bot-api`.

You will need to have a require() statement to include the Wickr Node.js Bot API in your
integration. Also, since the Wickr IO addon is required you will need to have a require()
statement for it as well. For example:

```
var addon = require('wickrio_addon');
var botapi = require('wickrio-bot-api');
```

start(client_username)

This API is used to start the connection with the Wickr IO client and get it ready for
use. This API uses the Wickr IO addon `clientInit()`, `isConnected()`
and `getClientState()` APIs to make sure the Wickr IO client connection is
initialized, there is a valid connection and the client is in the `RUNNING` state.
This is helpful since it may take the Wickr IO bot client longer to initialize than your
integration.

If you use this API you will not need to call these addon APIs. This API will return true
if successful, else returns false.

**Parameters:**

- client_username(REQUIRED) - The string user name of the Wickr IO client that is going
  to be used.

**Example:**

```
var result = botapi.start(process.argv[2]);
if (result === true) {
  console.log("Client started successfully");
} else {
  console.log("Client failed to start");
  process.exit();
}
```

startListening(callback)

This API initiates the asynchronous reception of received messages from the Wickr IO
client. The passed callback function will be called whenever a message is received from the
Wickr IO client.

**Parameters:**

- callback(REQUIRED) - The callback function that will be called when a message is
  received.

For more information, see [Receive Asynchronous Messages](addon-bot-api-usage-examples.md#receive-asynchronous-messages "addon-bot-api-usage-examples.md#receive-asynchronous-messages").

close()

This API will close the currently open connection to the Wickr IO client. This should be
called when done interacting with the client set up by the start() API.

**Example:**

```
process.on('SIGINT', function() {
  console.log("Received SIGINT. Graceful shutdown ...");
  botapi.close();
  process.exit();
});
```

encryptEnv()

This API encrypts any environment variables that were input in the configuration part and
were saved in the processes.json file, specifically any variables that contain sensitive
information such as API Tokens (ex: Google App Client ID), or bot client specific variables
such as a Bot Client Server.

loadData()

This API reads the encrypted user database from 'users.txt', which is an array of users
personal information with their Wickr emails and any other information that was saved using
the saveData() API. The user database is stored in the wickrUsers variable, which is an array
of users personal information with their Wickr emails and any other information that was
saved.

This API returns nothing.

saveData()

Encrypts the user database array contained in the wickrUsers variable, which is an array
of users personal information with their Wickr emails and any other information that was
saved, and saves it to the 'users.txt' file.

This API returns true if successful, else returns false.

addUser(wickrUser)

This API adds a user to the bot's user database array called wickrUsers, which is an array
of users personal information with their Wickr emails and any other information that was
saved.

**Parameters:**

- wickrUser(REQUIRED) - The WickrUser object to be added to the user database.

This API returns the user object after it is added to the user database.

parseMessage(message)

This API parses and breaks down an incoming received message from the client. If
successful the parsed values will be returned in an object.

**Parameters:**

- message(REQUIRED) - The message object received from the Wickr IO client.

The returned object contains the following properties:

- command - The command portion of the message
- argument - The argument portion of the message
- message - The full message text
- sender - The sender of the message
- vgroupid - The group ID if sent to a group

For more information, see [Receive Asynchronous Messages](addon-bot-api-usage-examples.md#receive-asynchronous-messages "addon-bot-api-usage-examples.md#receive-asynchronous-messages").

getUser(userID)

This API searches the user database for the input user ID and returns the WickrUser
object if found.

**Parameters:**

- userID(REQUIRED) - The string user ID of the user to be retrieved.

This API returns the user object if successful, else returns false.

getUsers()

This API is used to retrieve the entire user database.

Returns the bot's user database array.

deleteUser(userID)

Searches the user database for the passed user, deletes the user and returns the
WickrUser object if successful, else returns false.

**Parameters:**

- userID(REQUIRED) - The string user ID of the user to be deleted.

getVersions(packageFile)

This API returns a string that contains the versions associated with all of the main
components of the WickrIO environment. This includes the WickrIO client version, the
WickrIO addon version, and the WickrIO bot API version.

**Parameters:**

- packageFile(REQUIRED) - The path to the package.json file for the integration.

This API returns a string containing version information for all WickrIO
components.
