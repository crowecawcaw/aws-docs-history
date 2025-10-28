This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Addon and Bot API Usage Examples

This section contains several examples of the use of the Wickr IO addon and the Wickr IO
Bot API.

## API Initialization

Before the Wickr IO Node.js addon API can be used you will need to initialize it in your
JavaScript code. This initialization is done by calling the "start()" API (from the Wickr IO
Bot APIs) and passing the client name associated with the Wickr IO client. For
example:

```
const WickrIOAPI = require('wickrio_addon'); //WickrIO node.js addon which allows talking directly to our api
const WickrIOBotAPI = require('wickrio-bot-api'); //Development toolkit to help create bots/integrations
const WickrUser = WickrIOBotAPI.WickrUser;

var bot, tokens, bot_username, bot_client_port, bot_client_server;
var tokens = JSON.parse(process.env.tokens);

async function main() {
  try {
    bot_username = tokens.BOT_USERNAME.value;
    bot = new WickrIOBotAPI.WickrIOBot();
    var status = await bot.start(bot_username)
    if (!status)
      exitHandler(null, {
        exit: true,
        reason: 'Client not able to start'
      });
  } catch (err) {
    console.log(err);
  }
}
```

After the call to the "start()" API the client interface will be fully initialized. At
this point you can start using the other APIs to communicate with the Wickr IO
client.

## Sending message to a room

The following code fragment shows the use of the `cmdSendRoomMessage()` API to
send a message to a specific secure room. Before making the call you will need to get a valid
vGroupID.

```
var msg = "Sorry, I'm not allowed to delete all the files in the directory.";
try {
    var sMessage = WickrIOAPI.cmdSendRoomMessage(vGroupID, msg);
    console.log(sMessage); //if successful should print "Sending message"
} catch(err){
    //Handle error here
    console.log(err);
}
```

## Creating a room and sending an attachment

The following code shows the creation of a secure room and then sending a file to that
room:

```
var members = [{ "name" : "username001" }, { "name" : "username002" }];
var moderators = [{ "name" : "username001" }, { "name" : "username002" }];
var bor = "600";  //OPTIONAL
var ttl = "1000"; //OPTIONAL
var title = "Example Room";
var description = "The Good Room";
var message = "Testing time!"
var attachmentURL = "https://www.alsop-louie.com/wp-content/uploads/2017/03/wickr-logo-2-crop.png"
var displayname = "Logo.png";
try {
    var vGroupID = WickrIOAPI.cmdAddRoom(members, moderators, title, description, ttl, bor);
    //if successful should print a json with vgroupid of the newly created room
    console.log(vGroupID);
    //Notice: in this example the ttl and bor arguments are omitted and command will still work
    var cmd = WickrIOAPI.cmdSendRoomAttachment(vGroupID, attachmentURL, displayname);
    //if successful should print "Sending message"
    console.log(cmd);
} catch(err){
    //Handle errors here
    console.log(err);
}
```

## Receive Asynchronous Messages

There are two types of messaging APIs supported by the Wickr IO Node.js addon:

- synchronous API calls: where a request is made to the Wickr IO client and a response
  is received
- asynchronous messaging: where you specify a callback function which the Wickr IO
  addon will call when a message is received. All synchronous APIs will wait for the
  response to return before proceeding.

The following code shows you how to initiate the asynchronous messaging and shows a
callback function that will process the incoming messages.

```
await bot.startListening(listen); //Passes a callback function that will receive incoming messages into the bot client

async function listen(message) {
  try {
    var parsedMessage = bot.parseMessage(message); //Parses an incoming message and returns and object with command, argument, vGroupID and Sender fields
    if (!parsedMessage) {
      return;
    }
    console.log('parsedMessage:', parsedMessage);
    var wickrUser;
    var command = parsedMessage.command;
    var message = parsedMessage.message;
    var argument = parsedMessage.argument;
    var userEmail = parsedMessage.userEmail;
    var vGroupID = parsedMessage.vgroupid;
    var convoType = parsedMessage.convoType;
    var personal_vGroupID = "";
    if (convoType === 'personal')
      personal_vGroupID = vGroupID;
    var location = bot.findUser(userEmail); //Check if a user exists in the database and get his position in the database
    console.log('location:', location)
    if (location === -1) {
      wickrUser = new WickrUser(userEmail, {
        index: 0,
        personal_vGroupID: personal_vGroupID,
        command: "",
        argument: ""
      });
      var added = bot.addUser(wickrUser);
      console.log(added);
    }
    var user = bot.getUser(userEmail);
    user.token = "example_token_A1234";

    //how to determine the command a user sent and handling it
    if (command === '/help') {
      var reply = "What can I help you with?";
      var sMessage = WickrIOAPI.cmdSendRoomMessage(vGroupID, reply); //Respond back to the user or room with a message(using vGroupID)
      var users = [userEmail];
      var sMessage = WickrIOAPI.cmdSend1to1Message(users, reply); //Respond back to the user(using user wickrEmail)
      console.log(sMessage);
    }
  } catch (err) {
    console.log(err);
  }
}
```

The asynchronous messaging APIs will turn on or off the asynchronous reception of messages
received by the Wickr IO client. After calling the "cmdStartAsyncRecvMessages(callback)"
API, messages received will be sent to the callback function identified in that API. To turn
off the asynchronous reception of messages use the "cmdStopAsyncRecvMessages()" API.

###### Note

Always add try/catch blocks for errors when calling addon APIs

Using the asynchronous messaging does require your program handles the background events
associated with the reception of these messages. This can be tricky based on the single
threaded nature of JavaScript.

## API Shutdown

When you are done using the API you will need to shut it down. This is done by calling the
"close()" Bot API. This will also stop the asynchronous message receiving for the bot.

```
process.stdin.resume(); //so the program will not close instantly

async function exitHandler(options, err) {
  var closed = await bot.close();
  console.log(closed);
  if (err) {
    console.log("Exit Error:", err);
    process.exit();
  }
  if (options.exit) {
    process.exit();
  } else if (options.pid) {
    process.kill(process.pid);
  }
}

//catches ctrl+c and stop.sh events
process.on('SIGINT', exitHandler.bind(null, {
  exit: true
}));

// catches "kill pid" (for example: nodemon restart)
process.on('SIGUSR1', exitHandler.bind(null, {
  pid: true
}));
process.on('SIGUSR2', exitHandler.bind(null, {
  pid: true
}));
```
