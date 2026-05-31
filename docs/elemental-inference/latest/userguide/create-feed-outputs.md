# Configuring each feature

Following are details about how to configure each feature (output) that you
include in a Elemental Inference feed.

## Configuring event clipping

In **Callback config**, you can enter a string that you want
Elemental Inference to always include in the event clipping metadata for this output. This
information is useful when you later work with Elemental Inference events in Amazon EventBridge. You
will be able to filter events using this information, in order to find the
events for one feed. The string might identify the sports event in the feed, for
example.

## Configuring smart crop

There is no specific configuration for smart crop.

## Configuring smart subtitles

Smart subtitles uses automatic speech recognition (ASR) to generate TTML
subtitles from the audio in your source media. Configure the following settings
for the smart subtitles output:

- **Language** (required) – The
  language of the audio in the source media. Elemental Inference uses this setting to
  optimize transcription accuracy. Supported values:
  - `deu` – German
  - `eng` – English
  - `eng-au` – English (Australia)
  - `eng-gb` – English (Great Britain)
  - `eng-us` – English (United States)
  - `fra` – French
  - `ita` – Italian
  - `por` – Portuguese
  - `spa` – Spanish

- **Aspect ratio** (optional) – The
  width and height of the output video, specified as integer values. Elemental Inference
  uses the aspect ratio to determine subtitle layout and line
  lengths.
- **Dictionary** (optional) – The ID
  of a custom dictionary to improve transcription accuracy for
  domain-specific terminology. For information about creating and managing
  dictionaries, see [Managing dictionaries](#create-feed-console-dictionaries "#create-feed-console-dictionaries").
- **Profanity filter** (optional) –
  Controls how profanity is handled in the generated subtitles. Supported
  values:
  - `DISABLED` – No filtering (default). All
    words appear as transcribed.
  - `CENSOR` – Replace profanity with
    asterisks.
  - `DROP` – Remove profanity from the
    transcript entirely.

**CLI example**

The following example shows how to include a smart subtitles output when
creating a feed using the CLI:

```
aws elemental-inference create-feed \
  --name "my-feed" \
  --outputs '[{
    "name": "subtitles",
    "status": "ENABLED",
    "outputConfig": {
      "subtitling": {
        "language": "eng",
        "aspectRatio": {"width": 16, "height": 9},
        "profanityFilter": "DISABLED"
      }
    }
  }]'
```

## Managing dictionaries

A dictionary contains custom words and phrases that the ASR engine might not
recognize, such as brand names, technical terms, or proper nouns. You can
reference a dictionary when configuring a smart subtitles output to improve
transcription accuracy for domain-specific terminology.

Use the Elemental Inference dictionary API operations to manage dictionaries:

- `CreateDictionary` – Create a new dictionary.
  Specify a name, language, and optionally provide entries.
- `GetDictionary` – Retrieve details about a
  dictionary.
- `UpdateDictionary` – Update the name, language, or
  entries of a dictionary.
- `ExportDictionaryEntries` – Export the entries from
  a dictionary.
- `ListDictionaries` – List all dictionaries in your
  account.
- `DeleteDictionary` – Deletes a dictionary. You
  cannot delete a dictionary that is referenced by a feed. To delete a
  dictionary, first update or delete any feeds that reference it.

**Dictionary validation rules**

When creating or updating a dictionary, the following validation rules
apply:

- **Name**
  - 1–128 characters
  - Must start and end with an alphanumeric character
  - Allowed characters: letters, digits, hyphen (-), underscore
    (\_)

- **Language**

One of: `deu`, `eng`, `fra`,
`ita`, `por`, `spa`

Regional language variants (such as `eng-au`,
`eng-gb`, `eng-us`) are not supported for
dictionaries. Use the base language code (for example,
`eng`) instead.

- **Entries** (JSON payload)
  - Must be a valid JSON array. A top-level object or scalar is
    rejected.
  - Maximum 40 KB serialized payload size.
  - Each entry must include a `content` field that is
    not blank.
  - Each entry may optionally include a
    `sounds_like` field. If provided, it must be an
    array of non-blank strings.
  - Each `sounds_like` hint must contain only
    characters from the dictionary language's primary script.
    Currently, all supported languages use Latin script (Latin
    alphabet, accented letters, and script-neutral punctuation are
    accepted; non-Latin scripts are rejected).
