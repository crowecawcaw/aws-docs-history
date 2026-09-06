

# Importing bots in Lex V2
<a name="import"></a>

To use the console to import a previously exported bot, bot locale or custom vocabulary, you provide the file location on your local computer and the optional password to unlock the file. For an example, see [Importing a Lex V2 bot (console)](import-console.md).

When you use the API, importing a resource is a three step process:

1. Create an upload URL using the `CreateUploadUrl` operation. You don't need to create an upload URL when you are using the console.

1. Upload the .zip file that contains the resource definition.

1. Start the import with the `StartImport` operation.

The upload URL is a pre-signed Amazon S3 URL with write permission. The URL is available for five minutes after it is generated. If you password protect the .zip file, you must provide the password when you start the import. For more information, see [Using a password when importing or exporting](import-export-password.md).

An import is an asynchronous process. You can monitor the progress of an import using the console or the `DescribeImport` operation. 

When you import a bot or bot locale, there may be conflicts between resource names in the import file and existing resource names in Amazon Lex V2. Amazon Lex V2 can handle the conflict in three ways:
+ **Fail on conflict** – The import stops and no resources are imported from the import .zip file.
+ **Overwrite** – Amazon Lex V2 imports all of the resources from the import .zip file and replaces any existing resource with the definition from the import file. 
+ **Append** – Amazon Lex V2 imports all of the resources from the import .zip file and adds to any existing resource with the definition from the import file. This is available only for the bot locale. 

You can see a list of the imports to a resource using the console or the `ListImports` operation. Imports remain in the list for seven days. You can use the console or the `DescribeImport` operation to see details about a specific import.

You can also remove an import and the associated .zip file using the console or the `DeleteImport` operation.

For an example of importing a bot using the console, see [Importing a Lex V2 bot (console)](import-console.md).

## IAM permissions required to import
<a name="import-permissions"></a>

To import bots, bot locales, and custom vocabularies, the user running the import must have the following IAM permissions. 


| API | Required IAM actions | Resource | 
| --- | --- | --- | 
| [CreateUploadUrl](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateUploadUrl.html) | +  CreateUploadUrl  | \* | 
| [StartImport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartImport.html) for bot and bot locale | +  StartImport <br />+  iam:PassRole <br />+  CreateBot <br />+  CreateCustomVocabulary <br />+  CreateLocale <br />+  CreateIntent <br />+  CreateSlot <br />+  CreateSlotType <br />+  UpdateBot <br />+  UpdateCustomVocabulary <br />+  UpdateLocale <br />+  UpdateIntent <br />+  UpdateSlot <br />+  UpdateSlotType <br />+  DeleteBot <br />+  DeleteCustomVocabulary <br />+  DeleteLocale <br />+  DeleteIntent <br />+  DeleteSlot <br />+  DeleteSlotType  | 1.  To import a new bot: bot, bot alias. <br />2.  To overwrite an existing bot: bot. <br />3.  To import a new locale: bot.  | 
| [StartImport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartImport.html) for custom vocabularies | +  StartImport <br />+  CreateCustomVocabulary <br />+  DeleteCustomVocabulary <br />+  UpdateCustomVocabulary   | bot | 
| [DescribeImport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeImport.html) | +  DescribeImport  | Bot | 
| [DeleteImport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteImport.html) | +  DeleteImport  | Bot | 
| [ListImports](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListImports.html) | +  ListImports  | \* | 

For an example IAM policy, see [Allow a user to import bots and bot locales](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-import).