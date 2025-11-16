# Creating a test case within a test set using Test

Workbench

The Test Workbench results are dependent on the bot definition and its
corresponding test set. You can generate a test set with the information from the
bot definition to pinpoint areas that need improvement. Create a test dataset with
examples that you suspect (or know) will be challenging for the bot to interpret
correctly considering the current bot design and your knowledge of your customer
conversations.

Review your intents based on learnings from your production bot on a regular
basis. Continue to add to and adjust the bot’s sample utterances and slot values.
Consider improving slot resolution by using the available options, such as runtime
hints. The design and development of your bot is an iterative process that is a
continuous cycle.

Here are some other tips for optimizing your test set:

- Select the most common use cases with frequently used intents and slots in
  the test set.
- Explore different ways a customer could refer to your intents and slots.
  This can include user inputs in the forms of statements, questions, and
  commands that vary in length from minimal to extended.
- Include user inputs with a varied number of slots.
- Include commonly used synonyms or abbreviations of custom slot values
  supported by your bot (for example, “root canal”, “canal”, or “RC”).
- Include variations of built-in slot values (for example, “tomorrow”,
  “asap”, or "the next day").
- Examine the bot robustness for spoken modality by collecting user inputs
  that can be misinterpreted (for example, “ink”, “ankle”, or
  "anchor").
