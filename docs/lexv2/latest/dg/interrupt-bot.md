# Enabling your Amazon Lex V2 bot

to be interrupted by the user

When you start a bidirectional audio stream between an Amazon Lex V2 bot
and your application, you can configure the bot to listen for user
input while it is sending back a prompt. This input can be set as an interrupt.
With this, the user can
interrupt the prompt before the bot has finished playing it back.
You can use this configuration for situations where the user might
already know the answer to a question, such as when they're being
prompted to provide a CVV code.

A bot knows when the user interrupts a prompt when it detects user
input before your application can send back a
`PlaybackCompletion` event. When the user interrupts
a bot, the bot sends a
`PlaybackInterruptionEvent`.

By default, the user can interrupt any prompt that the bot is
streaming to your application. You can change this setting in the
Amazon Lex V2 console.

You can change how a user can respond to a prompt by editing a
slot. A slot is part of an intent, and it is the means by which the
user provides you the information you want. Each slot has a prompt
for the user to provide you with that information. To learn more
about slots, see [Amazon Lex V2 core concepts](how-it-works.md "how-it-works.md").

###### To change whether the user can interrupt a prompt

(console)

1. Sign in to AWS Management Console and open the Amazon Lex V2 console at [Amazon Lex V2
   console](https://console.aws.amazon.com/lexv2/ "https://console.aws.amazon.com/lexv2/").
2. Under **Bots**, select a bot.
3. Under **Language**, select the language
   of the bot.
4. Choose **View intents**.
5. Choose the intent.
6. For **Slots**, choose a slot.
7. Under **Advanced options**, choose
   **Slot prompts**.
8. Choose **More prompt options**.
9. Select or deselect **Users can interrupt the
   prompt when it is being read**.
   You can test this functionality by creating a bot with two slots
   and specifying that users can't interrupt a prompt for one slot. If
   you interrupt an interruptible prompt, the bot sends a playback
   interruption event. If you interrupt an uninterruptible, the prompt
   continues to play.
