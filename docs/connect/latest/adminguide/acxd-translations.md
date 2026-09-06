# Translations

Translations help you create multilingual conversational AI applications in agentic CX designer.

Use Translations to manage localized content across your workspace so users can
interact with your application in supported languages and regional dialects.
This includes:

- Predefined flow messages
- Custom slot values
- Knowledge base content invoked via knowledge base node
  Translations help keep multilingual experiences easier to manage because localized
  content can be reviewed from one place instead of editing every resource individually.

To access Translations, select **Translations** from your workspace menu.

Agentic CX designer supports multilingual application development across
supported languages and locales.

For voice-enabled experiences, language may also depend on the voice provider
configured in the contact flow in Amazon Connect Customer.

## Adding a language

Before translating content, add the languages your workspace should support.

###### To add a language

1. Open **Translations**.
2. Select the **Languages** tab.
3. Choose **Add language**.
4. Select the language or locale you want to support.
5. Save your selection.
6. Choose **Publish language** to make the language available across the workspace.

After a language is added, it can be used for translatable resources such as flows,
slots, application messages, and supported knowledge base content.

## Manual translation

You can add or edit translations directly in the workspace.

Use manual translation when:

- Exact wording is important
- Legal, compliance, or brand language must be approved
- A human translator needs to review AI-generated content
- Certain terms should not be translated literally
- Regional or dialect-specific phrasing matters

When reviewing translations, check that the localized content preserves the original
intent, tone, and required business meaning.

Translations can be managed offline by downloading and uploading translation files, when supported.

Use this workflow when:

- A localization team needs to translate content outside the workspace
- Translations require legal, brand, or regional review
- You want to bulk edit many translation values at once
- Your team uses an external translation management process

After uploading translated content, review it in the workspace before building and
deploying the application.

## Auto-translate

Auto-translate helps generate localized content for selected resources.

Use auto-translation as a starting point, especially when you need to quickly
prepare draft translations across many resources. Review auto-translated content
before using it in a live customer experience.

###### To request auto-translation

1. Open **Translations**.
2. Select the **Auto-translate** tab.
3. Choose **New translation job**.
4. Select whether to translate specific resources or filter by application.
5. Choose one or more target languages.
6. Select **Start**.

Optional settings may include:

|                       |                                                                   |
| --------------------- | ----------------------------------------------------------------- |
| **Preserve existing** | Keeps existing translated content from being overwritten.         |
| **Mark as complete**  | Marks generated translations as completed after the job finishes. |

Each auto-translation job displays status details so you can track progress.

|               |                                                                           |
| ------------- | ------------------------------------------------------------------------- |
| **Status**    | Whether the translation job is completed or still in progress.            |
| **Languages** | The target language or languages included in the job.                     |
| **Progress**  | How many resources were translated successfully out of the total checked. |
| **Created**   | When the translation job was created.                                     |

Review job results after completion and check any resources that did not translate successfully.

After adding or updating translations, create a new application build so the latest
language content is included in the application package.

If translated content belongs to a Q&A knowledge base, publish the updated
knowledge base content as needed so the latest translated entries are available.

## Testing multilingual changes

Before deploying multilingual changes, test the application in each target language
to confirm:

- The correct language appears
- Flow messages are translated
- Slot values and choices work as expected
- Knowledge base answers return appropriately
