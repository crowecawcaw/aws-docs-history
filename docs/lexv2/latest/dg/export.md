# Exporting bots from Lex V2

You export a bot, bot locale, or custom vocabulary using the
console or the `CreatExport` operation. You specify the
resource to export, and you can provide an optional password to help
protect the .zip file when you start an export. After you download
the .zip file, you must use the password to access the file before
you can use it. For more information, see [Using a password when
importing or exporting](import-export-password.md "import-export-password.md").

Exporting is an asynchronous operation. Once you have started the
export, you can use the console or the `DescribeExport`
operation to monitor the progress of the export. Once the export is
complete, the console or the `DescribeExport` operation
shows a status of `COMPLETED`, and the console downloads
the export .zip file to your browser. If you use the
`DescribeExport` operation, Amazon Lex V2 provides a
pre-signed Amazon S3 URL where you can download the results of the
export. The download URL is available for only five minutes, but you
can get a new URL by calling the `DescribeExport`
operation again.

You can see the history of exports for a resource with the console
or with the `ListExports` operation. The results show the
exports along with their current status. An export is available in
the history for seven days.

When you export the `Draft` version of a bot or a bot
locale, it is possible for the definition in the JSON file to be in
an inconsistent state because the `Draft` version of a
bot or bot locale can be changed while an export is in progress. If
the `Draft` version is changed while it is being
exported, the changes may not be included in the export file.

When you export a bot locale, Amazon Lex exports all of the information
that defines the locale, including the locale, custom vocabulary,
intents, slot types, and slots.

When you export a bot, Amazon Lex exports all of the locales defined
for the bot, including the intents, slot types, and slots. The
following items are not exported with a bot:

- Bot aliases
- Role ARN associated with a bot
- Tags associated with bots and bot aliases
- Lambda code hooks associated with a bot alias
  The role ARN and tags are entered as request parameters when you
  import a bot. You need to create bot aliases and assign Lambda code
  hooks after importing, if necessary.

You can remove an export and the associated .zip file using the
console or the `DeleteExport` operation.

For an example of exporting a bot using the console, see [Exporting a Lex V2 bot
(console)](export-console.md "export-console.md").

## IAM permissions required

to export bots in Lex V2

To export bots, bot locales, and custom vocabularies, the user
running the export must have the following IAM
permissions.

| API                                                                                                                        | • Required IAM actions                                                                                                                                                                                          | Resource |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [CreateExport](../APIReference/API_CreateExport.md "../APIReference/API_CreateExport.md")                                  | • CreateExport                                                                                                                                                                                                  | Bot      |
| [UpdateExport](../APIReference/API_UpdateExport.md "../APIReference/API_UpdateExport.md")                                  | • UpdateExport                                                                                                                                                                                                  | Bot      |
| [DescribeExport](../APIReference/API_DescribeExport.md "../APIReference/API_DescribeExport.md")                            | • DescribeExport<br>• DescribeBot<br>• DescribeCustomVocabulary<br>• DescribeLocale<br>• DescribeIntent<br>• DescribeSlot<br>• DescribeSlotType<br>• ListLocale<br>• ListIntent<br>• ListSlot<br>• ListSlotType | Bot      |
| [DescribeExport](../APIReference/API_DescribeExport.md "../APIReference/API_DescribeExport.md") for<br>custom vocabularies | • DescribeExport<br>• DescribeCustomVocabulary                                                                                                                                                                  | bot      |
| [DeleteExport](../APIReference/API_DeleteExport.md "../APIReference/API_DeleteExport.md")                                  | • DeleteExport                                                                                                                                                                                                  | Bot      |
| [ListExports](../APIReference/API_ListExports.md "../APIReference/API_ListExports.md")                                     | • ListExports                                                                                                                                                                                                   | \*       |

For an example IAM policy, see [Allow a user to export bots and bot locales](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-export "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-export") .
