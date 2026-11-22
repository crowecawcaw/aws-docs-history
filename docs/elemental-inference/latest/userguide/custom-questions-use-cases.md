

# Use cases for customer decisions

Use customer decisions for things that are specific to your business and that the built-in classifications don't cover. Each decision is answered either yes or no, or with options from a list that you provide. For more information, see [Question types](custom-questions-types.md).

The following examples show which type of question fits each use case:
+ **Detect on-screen graphics** – Ask "Is a scoreboard graphic visible on screen?" for each shot. The answer is yes or no, so use a `yesNo` question.
+ **Track sponsors** – Ask which of your sponsors' logos appear in each shot. List your sponsors as options. Several logos can appear at once, so use a `yesNoPerOption` question, which answers yes or no for each option.
+ **Check ad suitability** – Ask whether a scene is suitable for a specific ad category. The answer is yes or no, so use a `yesNo` question.
+ **Classify the action** – Ask what type of play a shot shows, such as a serve, a rally, a replay, or a crowd shot. List the types as options. A shot shows one type, so use a `chooseOne` question, which picks one option from the list.