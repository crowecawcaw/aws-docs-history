# Improving speech recognition with a custom vocabulary

You can give Amazon Lex V2 more information about how to process audio
conversations with a bot by creating a custom vocabulary in a specific
language. A _custom vocabulary_ is a list of specific
phrases that you want Amazon Lex V2 to recognize in the audio input. These are
generally proper nouns or domain-specific words that Amazon Lex V2 doesn't
recognize.

For example, suppose that you have a tech support bot. You can add
"backup" to a custom vocabulary to help the bot transcribe the audio
correctly as "backup," even when the audio sounds like "pack up." A
custom vocabulary can also help recognize rare words in the audio such
as "solvency" for financial services or proper nouns such as "Cognito"
or "Monitron."

## Custom vocabulary basics

- A custom vocabulary works on the transcription of audio
  input to a bot. You must provide sample utterances to
  recognize an intent or slot value.
- A custom vocabulary is unique to a specific language. You
  must configure custom vocabularies independently for each
  language. Custom vocabularies are supported for the
  following languages: English (UK), English (US), Korean (Korea),
  Italian (Italy), German (Germany), French (Canada), French (France),
  Spanish (Spain), Spanish (US), Japanese (Japan), Mandarin (PRC),
  Swedish (Sweden), Gulf Arabic (United Arab Emirates), Hindi (India),
  Dutch (The Netherlands), Norwegian (Norway), Polish (Poland),
  Finnish (Finland), Portuguese (Portugal), Portuguese (Brazil),
  Catalan (Spain).
- Custom vocabularies are available with [contact center integrations](contact-center.md "contact-center.md")
  supported by Amazon Lex V2. The [test window](test-bot.md "test-bot.md") in the Amazon Lex V2
  console supports custom vocabularies for all Amazon Lex V2 bots built on
  or after July 31, 2022. If you experience issues with custom
  vocabularies in the test window, rebuild the bot and try again.

Amazon Lex V2 uses custom vocabularies to elicit both intents and slots.
The same custom vocabulary file is used for intents and slots.
You can selectively turn off the custom vocabulary capability
for a slot when you add a slot type.

**Eliciting an intent** – You
can create a custom vocabulary for eliciting an intent. These
phrases are used to transcription when your bot is determining the
user's intent. For example, if you configured the phrase "backup" in
your custom vocabulary, Amazon Lex V2 transcribes the user input to "can
you please backup my photos?"—even when the audio sounds like
"can you please pack up my photos." You can specify the degree
of boosting for each phrase by configuring a weight of 0, 1, 2, or 3. You can also specify an alternate representation for the
phrase in the final speech to text output by adding
a `displayAs` field.

The custom vocabulary phrases used for improving transcription
during intent elicitation don't affect transcriptions while eliciting
slots. For more information about creating a custom vocabulary for
eliciting intents, see [Creating a custom vocabulary for
eliciting intents and slots](#vocab-create "#vocab-create").

**Eliciting custom slots** –
You can use a custom vocabulary to improve slot recognition for
audio conversations. To improve your Amazon Lex V2 bot's ability to
recognize slot values, create a custom slot and add the slot values
to the custom slot, then choose **Use slot values as custom
vocabulary**. Examples of slot values include product
names, catalogs, or proper nouns. You shouldn't use common words or
phrases such as "yes" and "no" in custom vocabularies.

After the slot values are added, these values are used for
improving slot recognition when the bot is expecting input for the
custom slot. These values aren't used for transcription when
eliciting an intent. For more information, see [Adding slot types](add-slot-types.md "add-slot-types.md").

## Best practices for creating a custom

vocabulary

**Eliciting an intent**

- Custom vocabularies work best when used to target specific
  words or phrases. Only add words to a custom vocabulary if
  they are not readily recognized by Amazon Lex V2.
- Decide how much weight to give a word based on how often
  the word isn't recognized in the transcription and how rare
  the word is in the input. Difficult to pronounce words
  require a higher weight.
- Use a representative test set to determine if a weight is
  appropriate. You can collect an audio test set by turning on
  audio logging in conversation logs.
- Avoid using short words like "on," "it," "to," "yes," "no"
  in a custom vocabulary.

**Eliciting a custom slot**

- Add the values to the custom slot type that you expect to
  be recognized. Add all the possible slot values for the
  custom slot type, no matter how common or rare the slot
  value is.
- Enable the option only when the custom slot type contains
  a list of catalog values or entities such as product names
  or mutual funds.
- Disable the option if the slot type is used to capture
  generic phrases such as "yes," "no," "I don't know,"
  "maybe," or generic words such as "one," "two,"
  "three."
- Limit the number of slot values and synonyms to 500 or
  less for best performance.

Enter acronyms or other words whose letters should be pronounced
individually as single letters separated by a period and a space.
Don't use individual letters unless they are part of a phrase, such
as "J. P. Morgan" or "A. W. S." You can use
upper- or lower-case letters to define an acronym.

## Creating a custom vocabulary for

eliciting intents and slots

You can use the Amazon Lex V2 console to create and manage a custom
vocabulary, or you can use Amazon Lex V2 API operations. There are 2 ways
of creating a custom vocabulary through the console:

###### Import custom vocabulary in the console:

1. Open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home "https://console.aws.amazon.com/lexv2/home")
2. From the list of bots, choose the bot which you
   want to add the custom vocabulary.
3. On the bot detail page, from the **Add
   languages** section, choose
   **View languages**.
4. From the list of languages, choose the language to
   which you want to add the custom vocabulary.

###### Create a new custom vocabulary directly through the console:

1. Click on **Create** in the
   **Custom Vocabulary** section of the language
   details page. This will open an editing window with no custom
   vocabulary present.
2. Add inputs for phrase, DisplayAs, and weight as required. You
   can further make inline edits to added items by updating their
   fields or deleting them from the list.
3. Click on **Save**. Please note: the new
   custom vocabulary is only saved in your bot after you click
   on **Save**.
4. You can continue making inline edits in this page and
   click **Save** when are done.
5. This page also allows you import, export, and delete a custom
   vocabulary file from the drop-down menu on the top right.

###### Use the `ListCustomVocabularyItems` API to view the

custom vocabulary entries:

1. Use the `ListCustomVocabularyItems` operation
   to view the custom vocabulary entries. The request body
   will look like this:

```
{
   "maxResults": number,
   "nextToken": "string"
}
```

2. Please note that `maxResults` and `nextToken`
   are optional fields for the request body.
3. The response from the `ListCustomVocabularyItems`
   operation looks like this:

```
{
   "botId": "string",
   "botVersion": "string",
   "localeId": "string",
   "customVocabularyItems": [
        {
            "itemId": "string",
            "phrase": "string",
            "weight": number,
            "displayAs": "string"
        }
   ]
}
```

###### Use the `BatchCreateCustomVocabularyItem` API to

create new custom vocabulary entries:

1. If your bot’s locale does not have a custom vocabulary created
   yet, please follow the steps to use the [StartImport](../APIReference/API_StartImport.md "../APIReference/API_StartImport.md") to
   create a custom vocabulary.
2. After the custom vocabulary has been created, use the
   `BatchCreateCustomVocabularyItem` operation to
   create new custom vocabulary entries. The request body will
   look like this:

```
{
   "customVocabularyItemList": [
        {
            "phrase": "string",
            "weight": number,
            "displayAs": "string"
        }
   ]
}
```

3. Please note that `weight` and `displayAs`
   are optional fields for the request body.
4. The response from the `BatchCreateCustomVocabularyItem`
   will look like this:

```
{
    "botId": "string",
    "botVersion": "string",
    "localeId": "string",
    "errors": [
        {
            "itemId": "string",
            "errorMessage": "string",
            "errorCode": "string"
        }
    ],
    "resources": [
        {
            "itemId": "string",
            "phrase": "string",
            "weight": number,
            "displayAs": "string"
        }
    ]
}
```

5. As this is a batch operation, the request will not fail if
   one of the items fails to create. The errors list will contain
   information about why the operation failed for that specific
   entry. The resources list will contain all of the entries that
   were successfully created.
6. For `BatchCreateCustomVocabularyItem`, you can
   expect see these types of errors:
   - `RESOURCE_DOES_NOT_EXIST`: The custom
     vocabulary does not exist. Follow the steps for creating
     a custom vocabulary before calling this operation.
   - `DUPLICATE_INPUT`: The list of inputs
     contains duplicate phrases.
   - `RESOURCE_ALREADY_EXISTS`: The given phrase
     for the entry already exists in your custom vocabulary.
   - `INTERNAL_SERVER_FAILURE`: There was an error in
     the backend while processing your request. This may indicate
     a service outage or another issue.

###### Use the `BatchDeleteCustomVocabularyItem` API to

delete existing custom vocabulary entries:

1. If your bot’s locale does not have a custom vocabulary created
   yet, please follow the steps for Use the [StartImport](../APIReference/API_StartImport.md "../APIReference/API_StartImport.md") to create
   a custom vocabulary to create one.
2. After the custom vocabulary has been created, use the
   `BatchDeleteCustomVocabularyItem` operation to delete
   existing custom vocabulary entries. The request body will look
   like this:

```
{
   "customVocabularyItemList": [
        {
            "itemId": "string"
        }
   ]
}
```

3. The response from the `BatchDeleteCustomVocabularyItem`
   will look like this:

```
{
    "botId": "string",
    "botVersion": "string",
    "localeId": "string",
    "errors": [
        {
            "itemId": "string",
            "errorMessage": "string",
            "errorCode": "string"
        }
    ],
    "resources": [
        {
            "itemId": "string",
            "phrase": "string",
            "weight": number,
            "displayAs": "string"
        }
    ]
}
```

4. As this is a batch operation, the request will not fail if
   one of the items fails to delete. The errors list will contain
   information about why the operation failed for that specific entry.
   The resources list will contain all of the entries that were
   successfully deleted.
5. For `BatchDeleteCustomVocabularyItem`, you can expect
   see these types of errors:
   - `RESOURCE_DOES_NOT_EXIST`: The custom vocabulary entry
     you are trying to delete does not exist.
   - `INTERNAL_SERVER_FAILURE`: There was an error in the
     backend while processing your request. This may indicate a service
     outage or another issue.

###### Use the `BatchUpdateCustomVocabularyItem` API to

update existing custom vocabulary entries:

1. If your bot’s locale does not have a custom vocabulary
   created yet, please follow the steps for Use the
   [StartImport](../APIReference/API_StartImport.md "../APIReference/API_StartImport.md") to create a custom vocabulary to
   create a custom vocabulary.
2. After the custom vocabulary has been created, use the
   `BatchUpdateCustomVocabularyItem` operation to
   update existing custom vocabulary entries. The request body
   will look like this:

```
{
   "customVocabularyItemList": [
        {
            "itemId": "string",
            "phrase": "string",
            "weight": number,
            "displayAs": "string"
        }
   ]
}
```

3. Please note that `weight` and `displayAs`
   are optional fields for the request body.
4. The response from the `BatchUpdateCustomVocabularyItem`
   will look like this:

```
{
    "botId": "string",
    "botVersion": "string",
    "localeId": "string",
    "errors": [
        {
            "itemId": "string",
            "errorMessage": "string",
            "errorCode": "string"
        }
    ],
    "resources": [
        {
            "itemId": "string",
            "phrase": "string",
            "weight": number,
            "displayAs": "string"
        }
    ]
}
```

5. As this is a batch operation, the request will not
   fail if one of the items fails to delete. The errors
   list will contain information about why the operation
   failed for that specific entry. The resources list will
   contain all of the entries that were successfully
   updated.
6. For `BatchUpdateCustomVocabularyItem`, you
   can expect see these types of errors:
   - `RESOURCE_DOES_NOT_EXIST`: The custom
     vocabulary entry you are trying to update does
     not exist.
   - `DUPLICATE_INPUT`: The list of inputs
     contains duplicate itemIds.
   - `RESOURCE_ALREADY_EXISTS`: The given phrase
     for the entry already exists in your custom
     vocabulary.
   - `INTERNAL_SERVER_FAILURE`: There was an error
     in the backend while processing your request. This may
     indicate a service outage or another issue.

## Creating a custom vocabulary

file

A custom vocabulary file is a tab-separated list of values that
contain the phrase to recognize, a weight to give the boost, and
a `displayAs` field which will replace the phrase in the
speech transcript.
Phrases with a higher boost value are more likely to be used when
they appear in the audio input.

The custom vocabulary file must be named
`CustomVocabulary.tsv`, and must be
compressed in a zip file before it can be imported. The zip file
must be less than 300 MB in size. The maximum number of phrases in a
custom vocabulary is 500.

- **phrase** 1–4 words
  that should be recognized. Separate words in the phrase with
  spaces. You can't have duplicate phrases in the file. The
  phrase field is required.
- **weight** – The degree
  to which the phrase recognition is boosted. The value is an
  integer 0, 1, 2, or 3. If you don't specify a weight, the
  default value is 1. Decide on the weight based on how often
  the word isn't recognized in the transcription and on how
  rare the word is in the input. The weight 0 means that no
  boosting will be applied and the entry will only be used for
  performing replacements using the `displayAs`
  field.
- **displayAs** – Defines
  how you want your phrase to look in your transcription
  output. This is an optional field in the custom
  vocabulary.

The custom vocabulary file must contain a header row with the
headers "phrase," "weight," and "displayAs". The headers can be in
any order, but must follow the above nomenclature.

The following example is a custom vocabulary file. The required tab
character to separate the phrase, the weight, and the displayAs is represented by
the text "[TAB]". If you use this example, replace the text with a
tab character.

```
phrase[TAB]weight[TAB]displayAs
Newcastle[TAB]2
Hobart[TAB]2[TAB]Hobart, Australia
U. Dub[TAB]1[TAB]University of Washington, Seattle
W. S. U.[TAB]3
Issaquah
Kennewick

```
