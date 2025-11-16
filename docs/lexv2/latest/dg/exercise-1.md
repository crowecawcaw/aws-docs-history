# Exercise 1: Create a chatbot from a

template

In this exercise, you create your first Amazon Lex V2 chatbot and test it
in the Amazon Lex V2 console. For this exercise, you use the
**OrderFlowers** template, which demonstrates a practical, real-world use case for e-commerce.

## OrderFlowers Bot Example

You use the **OrderFlowers** template to
create an Amazon Lex V2 chatbot that can handle flower ordering requests. This example demonstrates how businesses can automate order taking with intelligent chatbots. For more information about the
structure of a bot, see [Amazon Lex V2 core concepts](how-it-works.md "how-it-works.md").

- **Intents** –
  The bot includes one main intent:
  - `OrderFlowers` - Handles flower ordering requests by collecting the flower type, pickup date, and pickup time

- **Slot types**
  – The bot uses built-in slot types that automatically recognize and handle common data formats:
  - [AMAZON.Date](built-in-slot-date.md "built-in-slot-date.md") - Recognizes dates like "tomorrow", "next Friday", or "March 15th"
  - [AMAZON.Time](built-in-slot-time.md "built-in-slot-time.md") - Recognizes times like "2 PM", "noon", or "quarter past three"
  - `FlowerTypes` (custom) - Specific flower varieties like "roses", "tulips", "lilies"

- **Slots** – The
  OrderFlowers intent requires the following information before the bot can fulfill the flower order:
  - `FlowerType` (FlowerTypes custom type) - The type of flowers to order
  - `PickupDate` ([AMAZON.Date](built-in-slot-date.md "built-in-slot-date.md") type) - When to pick up the flowers
  - `PickupTime` ([AMAZON.Time](built-in-slot-time.md "built-in-slot-time.md") type) - What time to pick up the flowers

- **Sample Utterances** –
  The following sample utterances show natural ways users might request flower orders:
  - "I would like to pick up flowers"
  - "I want to order some flowers"
  - "Can I get flowers for pickup?"
  - "I need to buy flowers"

- **Prompts** –
  After the bot identifies the intent, it uses the
  following prompts to fill the slots:
  - Prompt for the `FlowerType`
    slot – "What type of flowers would you
    like to order?"
  - Prompt for the `PickupDate`
    slot – "What day do you want the
    {FlowerType} to be picked up?"
  - Prompt for the `PickupTime`
    slot – "At what time do you want the
    {FlowerType} to be picked up?"
  - Confirmation statement – "Okay, your
    {FlowerType} will be ready for pickup by
    {PickupTime} on {PickupDate}. Does this
    sound okay?"

## Create Your Bot

###### To create an Amazon Lex V2 bot (Console)

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. Choose **Create bot**.
3. For the **Creation method**, choose
   **Start with an example**.
4. In the **Example bots** section,
   choose **OrderFlowers** from the
   list.
5. In the **Bot configuration** section
   give the bot a name and an optional description. The name must be
   unique in your account.
6. In the **Permissions** section,
   choose **Create a new role with basic Amazon Lex
   permissions**. This will create an
   AWS Identity and Access Management (IAM) role with the permissions that Amazon Lex V2
   needs to run your bot.
7. In the **Children's Online Privacy Protection
   Act (COPPA)** section, make the appropriate
   choice.
8. In the **Session timeout** and
   **Advanced settings** sections,
   leave the defaults.
9. Choose **Next**. Amazon Lex V2 creates your
   bot.

## Add a Language to Your Bot

After you create your bot, you must add one or more languages
that the bot supports. A language contains the intents, slot
types, and slots that the bot uses to converse with
users.

###### To add a language to a bot

1. In the **Language** section, choose a
   supported language, and add a description.
2. Leave the **Voice interaction** and
   **Intent classification confidence score
   threshold** fields with their
   defaults.
3. Choose
   **Done** to add the language to the bot.

## Test Your Bot

After you choose **Done**, the console opens
the intent editor. You can use the intent editor to examine the
intents used by the bot. When you are done examining the bot,
you can test it.

###### To test the OrderFlowers bot

1. Choose
   **Build** at the top of the page. Wait for the bot to
   build.
2. When the build is complete, choose
   **Test** to open the test
   window.
3. Test the bot. Start the conversation with one of the
   sample utterances, such as "I would like to pick up
   flowers."

## Enable NLU to Improve Understanding

Now that you have a working chatbot, let's enhance it with Assisted NLU to improve intent recognition and slot resolution. Assisted NLU uses Large Language Models (LLMs) to better understand user requests, even when they use different phrasing than your training examples.

###### To enable Assisted NLU

1. In the Amazon Lex V2 console, navigate to your bot's settings.
2. In the left navigation pane, choose **Bot settings**.
3. Under **Assisted NLU**, choose **Enable**.
4. Choose **Save** to apply the changes.
5. Build your bot again to apply the Assisted NLU enhancement.

**Test the Improvement:** Try these variations in your test console to see how Assisted NLU handles different phrasings:

- "I want to buy some roses" (should trigger OrderFlowers intent and capture FlowerType)
- "Can I get flowers delivered tomorrow?" (should trigger OrderFlowers intent and capture PickupDate)
- "I need tulips for pickup at 3 PM" (should trigger OrderFlowers intent and capture FlowerType and PickupTime)

Notice how the chatbot can understand these natural variations without requiring you to add them as explicit sample utterances. This is powered by Assisted NLU, which uses AI to improve natural language understanding.

## Next steps

Now that you've created you first bot using a template, you
can use the console to create your own bot. For instruction on
creating a custom bot, and for more information about creating
bots, see [Working with Amazon Lex V2 bots](building-bots.md "building-bots.md").
