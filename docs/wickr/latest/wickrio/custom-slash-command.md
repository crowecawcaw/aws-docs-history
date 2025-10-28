This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Add a custom slash command

To add custom behavior, you have to make changes to `index.js`.

Complete the following procedure to add a custom slash command.

1. Add a `getEmoji` function. This will return a random emoji.
2. Modify the `listen` function. This will allow it to respond to the
   slash-command /emoji with a random emoji from the list.

```
// index.js
const WickrIOBotAPI = require('wickrio-bot-api')

const bot = new WickrIOBotAPI.WickrIOBot()
const WickrIOAPI = bot.getWickrIOAddon()

function getEmoji() {
  const emojis = [
    "🦩", "🌋", "🎪", "🎭", "🌮", "🦊", "🎨", "🎡", "🌎", "🦄", "🍕",
    "🎸", "🌈", "🦋", "🎯", "🎠", "🦜", "🎂", "🌺", "🎮"
  ]

  return emojis[Math.floor(Math.random() * emojis.length)]
}

async function listen(input) {
  const msg = bot.parseMessage(input)
  if (!msg) return

  switch (msg.command) {
    case "/emoji":
      await WickrIOAPI.cmdSendRoomMessage(msg.vgroupid, getEmoji())
      break
  }
}

async function main() {
  const username = process.argv[2]
  if (!username) throw new Error('Missing username')

  const status = await bot.start(username)
  if (!status) throw new Error('Unable to start bot')

  bot.startListening(listen)
}

main()

```
