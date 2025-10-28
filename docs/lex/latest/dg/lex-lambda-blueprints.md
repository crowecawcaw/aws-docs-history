End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Amazon Lex and AWS Lambda

Blueprints

The Amazon Lex console provides example bots (called bot
blueprints) that are preconfigured so you can quickly create and
test a bot in the console. For each of these bot blueprints, Lambda
function blueprints are also provided. These blueprints provide
sample code that works with their corresponding bots. You can use
these blueprints to quickly create a bot that is configured with a
Lambda function as a code hook, and test the end-to-end setup without
having to write code.

You can use the following Amazon Lex bot blueprints and the
corresponding AWS Lambda function blueprints as code hooks for bots:

- Amazon Lex blueprint —
  `OrderFlowers`
  - AWS Lambda blueprint —
    `lex-order-flowers-python`

- Amazon Lex blueprint —
  `ScheduleAppointment`
  - AWS Lambda blueprint —
    `lex-make-appointment-python`

- Amazon Lex blueprint — `BookTrip`

      + AWS Lambda blueprint —
       `lex-book-trip-python`

  To create a bot using a blueprint and configure it to use a Lambda
  function as a code hook, see [Exercise 1: Create an Amazon Lex Bot Using a
  Blueprint (Console)](gs-bp.md "gs-bp.md"). For an example of using other
  blueprints, see [Additional Examples: Creating Amazon Lex Bots](additional-exercises.md "additional-exercises.md").

## Updating a Blueprint

for a Specific Locale

If you are using a blueprint in a locale other than English
(US) (en-US), you need to update the name of any intents to
include the locale. For example, if you are using the
`OrderFlowers` blueprint, you need to do the
following.

- Find the `dispatch` function near the end
  of the Lambda function code.
- In the `dispatch` function, update the name
  of the intent to include the locale that you are using.
  For example, if you are using the English (Australian)
  (en-AU) locale, change the line:

`if intent_name == 'OrderFlowers':`

to

`if intent_name ==
 'OrderFlowers_enAU':`

Other blueprints use other intent names, they should be
updated as above before you use them.
