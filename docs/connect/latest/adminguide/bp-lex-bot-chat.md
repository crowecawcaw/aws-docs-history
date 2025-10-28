# Best practices for using the chat channel and

Amazon Lex

Following are some recommended best practices for using the chat channel and Amazon Lex
together.

- You can use the same bot for both the voice and chat channels. However,
  you may want the bot to respond differently based on the channel. For
  example, you want to return SSML for voice so a number is read as a phone
  number, but you want to return normal text to chat. You can do this by
  passing the **Channel** attribute. For instructions, see
  [How to use the same Amazon Lex bot for voice and
  chat](one-bot-voice-chat.md "one-bot-voice-chat.md").
- For voice, some words are best spelled phonetically to get the correct
  pronunciation, such as last names. If this is the case with your scenario,
  include it in the design of your bot. Or, you can keep the voice and chat
  bots separate.
- Tell agents about the bot. When a contact is connected to the agent, the
  agent sees the entire transcript in their window. The transcript includes
  text from both the customer and the bot.
