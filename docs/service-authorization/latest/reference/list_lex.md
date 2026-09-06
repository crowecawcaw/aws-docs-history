

# Actions, resources, and condition keys for Amazon Lex
<a name="list_lex"></a>

Amazon Lex (service prefix: `lex`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/lex/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/lex/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/lex/latest/dg/access_permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/lex/lex.json) for this service.

**Topics**
+ [API operations defined by Amazon Lex](#list_lex-operations)
+ [Actions defined by Amazon Lex](#list_lex-actions-as-permissions)
+ [Resource types defined by Amazon Lex](#list_lex-resources-for-iam-policies)
+ [Condition keys for Amazon Lex](#list_lex-policy-keys)

## API operations defined by Amazon Lex
<a name="list_lex-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_lex-actions-as-permissions).




- **   CreateBotVersion  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:CreateBotVersion](#list_lex-action-CreateBotVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSlotTypeVersion  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:CreateSlotTypeVersion](#list_lex-action-CreateSlotTypeVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBot  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:DeleteBot](#list_lex-action-DeleteBot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteBotAlias](#list_lex-action-DeleteBotAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteBotChannel](https://docs.aws.amazon.com/lexv2/latest/dg/deploying-messaging-platform.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteBotLocale](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotLocale.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteBotVersion](#list_lex-action-DeleteBotVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteCustomVocabulary](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteCustomVocabulary.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteIntent](#list_lex-action-DeleteIntent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteResourcePolicy](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteResourcePolicy.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteSlot.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlotType](#list_lex-action-DeleteSlotType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBotAlias  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:DeleteBotAlias](#list_lex-action-DeleteBotAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteResourcePolicy](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteResourcePolicy.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBotChannelAssociation  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:DeleteBotChannelAssociation](#list_lex-action-DeleteBotChannelAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBotVersion  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:DeleteBotVersion](#list_lex-action-DeleteBotVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntent  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:DeleteIntent](#list_lex-action-DeleteIntent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntentVersion  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:DeleteIntentVersion](#list_lex-action-DeleteIntentVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSlotType  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:DeleteSlotType](#list_lex-action-DeleteSlotType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSlotTypeVersion  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:DeleteSlotTypeVersion](#list_lex-action-DeleteSlotTypeVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUtterances  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:DeleteUtterances](#list_lex-action-DeleteUtterances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetBot  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetBot](#list_lex-action-GetBot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBotAlias  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetBotAlias](#list_lex-action-GetBotAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBotAliases  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetBotAliases](#list_lex-action-GetBotAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetBotChannelAssociation  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetBotChannelAssociation](#list_lex-action-GetBotChannelAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBotChannelAssociations  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetBotChannelAssociations](#list_lex-action-GetBotChannelAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetBotVersions  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetBotVersions](#list_lex-action-GetBotVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetBots  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetBots](#list_lex-action-GetBots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetBuiltinIntent  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetBuiltinIntent](#list_lex-action-GetBuiltinIntent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBuiltinIntents  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetBuiltinIntents](#list_lex-action-GetBuiltinIntents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBuiltinSlotTypes  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetBuiltinSlotTypes](#list_lex-action-GetBuiltinSlotTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExport  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetExport](#list_lex-action-GetExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImport  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetImport](#list_lex-action-GetImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntent  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetIntent](#list_lex-action-GetIntent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntentVersions  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetIntentVersions](#list_lex-action-GetIntentVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetIntents  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetIntents](#list_lex-action-GetIntents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetMigration  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetMigration](#list_lex-action-GetMigration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMigrations  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetMigrations](#list_lex-action-GetMigrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetSlotType  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetSlotType](#list_lex-action-GetSlotType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSlotTypeVersions  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetSlotTypeVersions](#list_lex-action-GetSlotTypeVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetSlotTypes  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetSlotTypes](#list_lex-action-GetSlotTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetUtterancesView  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:GetUtterancesView](#list_lex-action-GetUtterancesView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:ListTagsForResource](#list_lex-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutBot  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:PutBot](#list_lex-action-PutBot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBotAlias  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:PutBotAlias](#list_lex-action-PutBotAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:TagResource](#list_lex-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutIntent  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:PutIntent](#list_lex-action-PutIntent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutSlotType  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:PutSlotType](#list_lex-action-PutSlotType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImport  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:CreateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateBotLocale](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBotLocale.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateCustomVocabulary](https://docs.aws.amazon.com/lexv2/latest/dg/vocab.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateSlot.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateSlotType](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateSlotType.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateTestSet](https://docs.aws.amazon.com/lexv2/latest/dg/create-test-set-from-CSV.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteBotLocale](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotLocale.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteCustomVocabulary](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteCustomVocabulary.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteIntent](#list_lex-action-DeleteIntent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteSlot.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlotType](#list_lex-action-DeleteSlotType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:StartImport](#list_lex-action-StartImport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:TagResource](#list_lex-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [lex:UpdateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBot.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateBotLocale](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotLocale.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateCustomVocabulary](https://docs.aws.amazon.com/lexv2/latest/dg/vocab.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateIntent.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateSlot.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateSlotType](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateSlotType.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateTestSet](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateTestSet.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lexv2.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:TagResource](#list_lex-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** lex-models
  - **IAM action:**  [lex:UntagResource](#list_lex-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteSession  **
  - **SDK client:** lex-runtime
  - **IAM action:**  [lex:DeleteSession](#list_lex-action-DeleteSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetSession  **
  - **SDK client:** lex-runtime
  - **IAM action:**  [lex:GetSession](#list_lex-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PostContent  **
  - **SDK client:** lex-runtime
  - **IAM action:**  [lex:PostContent](#list_lex-action-PostContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PostText  **
  - **SDK client:** lex-runtime
  - **IAM action:**  [lex:PostText](#list_lex-action-PostText) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutSession  **
  - **SDK client:** lex-runtime
  - **IAM action:**  [lex:PutSession](#list_lex-action-PutSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Lex
<a name="list_lex-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateBotVersion](https://docs.aws.amazon.com/lex/latest/dg/API_CreateBotVersion.html)  **
  - **Description:** Creates a new version based on the $LATEST version of the specified bot
  - **Resource types (\*required):** [bot](#list_lex-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot version\*](#list_lex-resource-botversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateIntentVersion](https://docs.aws.amazon.com/lex/latest/dg/API_CreateIntentVersion.html)  **
  - **Description:** Creates a new version based on the $LATEST version of the specified intent
  - **Resource types (\*required):** [intent version\*](#list_lex-resource-intentversion)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSlotTypeVersion](https://docs.aws.amazon.com/lex/latest/dg/API_CreateSlotTypeVersion.html)  **
  - **Description:** Creates a new version based on the $LATEST version of the specified slot type
  - **Resource types (\*required):** [slottype version\*](#list_lex-resource-slottypeversion)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteBot](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteBot.html)  **
  - **Description:** Deletes all versions of a bot
  - **Resource types (\*required):** [bot](#list_lex-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot version\*](#list_lex-resource-botversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBotAlias](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteBotAlias.html)  **
  - **Description:** Deletes an alias for a specific bot
  - **Resource types (\*required):** [bot alias\*](#list_lex-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBotChannelAssociation](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteBotChannelAssociation.html)  **
  - **Description:** Deletes the association between a Amazon Lex bot alias and a messaging platform
  - **Resource types (\*required):** [channel\*](#list_lex-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBotVersion](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteBotVersion.html)  **
  - **Description:** Deletes a specific version of a bot
  - **Resource types (\*required):** [bot](#list_lex-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot version\*](#list_lex-resource-botversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntent](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteIntent.html)  **
  - **Description:** Deletes all versions of an intent
  - **Resource types (\*required):** [bot](#list_lex-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [intent version\*](#list_lex-resource-intentversion) / **Condition keys:**  
  - **Access level:** Write

- **   [DeleteIntentVersion](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteIntentVersion.html)  **
  - **Description:** Deletes a specific version of an intent
  - **Resource types (\*required):** [intent version\*](#list_lex-resource-intentversion)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSession](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_DeleteSession.html)  **
  - **Description:** Removes session information for a specified bot, alias, and user ID
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot version](#list_lex-resource-botversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSlotType](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteSlotType.html)  **
  - **Description:** Deletes all versions of a slot type
  - **Resource types (\*required):** [bot](#list_lex-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [slottype version\*](#list_lex-resource-slottypeversion) / **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSlotTypeVersion](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteSlotTypeVersion.html)  **
  - **Description:** Deletes a specific version of a slot type
  - **Resource types (\*required):** [slottype version\*](#list_lex-resource-slottypeversion)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteUtterances](https://docs.aws.amazon.com/lex/latest/dg/API_DeleteUtterances.html)  **
  - **Description:** Deletes the information Amazon Lex maintains for utterances on a specific bot and userId
  - **Resource types (\*required):** [bot](#list_lex-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot version\*](#list_lex-resource-botversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBot](https://docs.aws.amazon.com/lex/latest/dg/API_GetBot.html)  **
  - **Description:** Returns information for a specific bot. In addition to the bot name, the bot version or alias is required
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot version](#list_lex-resource-botversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBotAlias](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotAlias.html)  **
  - **Description:** Returns information about a Amazon Lex bot alias
  - **Resource types (\*required):** [bot alias\*](#list_lex-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBotAliases](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotAliases.html)  **
  - **Description:** Returns a list of aliases for a given Amazon Lex bot
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetBotChannelAssociation](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotChannelAssociation.html)  **
  - **Description:** Returns information about the association between a Amazon Lex bot and a messaging platform
  - **Resource types (\*required):** [channel\*](#list_lex-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBotChannelAssociations](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotChannelAssociations.html)  **
  - **Description:** Returns a list of all of the channels associated with a single bot
  - **Resource types (\*required):** [channel\*](#list_lex-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetBotVersions](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotVersions.html)  **
  - **Description:** Returns information for all versions of a specific bot
  - **Resource types (\*required):** [bot version\*](#list_lex-resource-botversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetBots](https://docs.aws.amazon.com/lex/latest/dg/API_GetBots.html)  **
  - **Description:** Returns information for the $LATEST version of all bots, subject to filters provided by the client
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetBuiltinIntent](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinIntent.html)  **
  - **Description:** Returns information about a built-in intent
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBuiltinIntents](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinIntents.html)  **
  - **Description:** Gets a list of built-in intents that meet the specified criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBuiltinSlotTypes](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinSlotTypes.html)  **
  - **Description:** Gets a list of built-in slot types that meet the specified criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetExport](https://docs.aws.amazon.com/lex/latest/dg/API_GetExport.html)  **
  - **Description:** Exports Amazon Lex Resource in a requested format
  - **Resource types (\*required):** [bot version\*](#list_lex-resource-botversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImport](https://docs.aws.amazon.com/lex/latest/dg/API_GetImport.html)  **
  - **Description:** Gets information about an import job started with StartImport
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIntent](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntent.html)  **
  - **Description:** Returns information for a specific intent. In addition to the intent name, you must also specify the intent version
  - **Resource types (\*required):** [intent version\*](#list_lex-resource-intentversion)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIntentVersions](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntentVersions.html)  **
  - **Description:** Returns information for all versions of a specific intent
  - **Resource types (\*required):** [intent version\*](#list_lex-resource-intentversion)
  - **Condition keys:**  
  - **Access level:** List

- **   [GetIntents](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntents.html)  **
  - **Description:** Returns information for the $LATEST version of all intents, subject to filters provided by the client
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetMigration](https://docs.aws.amazon.com/lex/latest/dg/API_GetMigration.html)  **
  - **Description:** Grants permission to view an ongoing or completed migration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMigrations](https://docs.aws.amazon.com/lex/latest/dg/API_GetMigrations.html)  **
  - **Description:** Grants permission to view list of migrations from Amazon Lex v1 to Amazon Lex v2
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetSession](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_GetSession.html)  **
  - **Description:** Returns session information for a specified bot, alias, and user ID
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot version](#list_lex-resource-botversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSlotType](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotType.html)  **
  - **Description:** Returns information about a specific version of a slot type. In addition to specifying the slot type name, you must also specify the slot type version
  - **Resource types (\*required):** [slottype version\*](#list_lex-resource-slottypeversion)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSlotTypeVersions](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotTypeVersions.html)  **
  - **Description:** Returns information for all versions of a specific slot type
  - **Resource types (\*required):** [slottype version\*](#list_lex-resource-slottypeversion)
  - **Condition keys:**  
  - **Access level:** List

- **   [GetSlotTypes](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotTypes.html)  **
  - **Description:** Returns information for the $LATEST version of all slot types, subject to filters provided by the client
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetUtterancesView](https://docs.aws.amazon.com/lex/latest/dg/API_GetUtterancesView.html)  **
  - **Description:** Returns a view of aggregate utterance data for versions of a bot for a recent time period
  - **Resource types (\*required):** [bot version\*](#list_lex-resource-botversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/lex/latest/dg/API_ListTagsForResource.html)  **
  - **Description:** Lists tags for a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [channel](#list_lex-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PostContent](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html)  **
  - **Description:** Sends user input (text or speech) to Amazon Lex
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot version](#list_lex-resource-botversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PostText](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html)  **
  - **Description:** Sends user input (text-only) to Amazon Lex
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot version](#list_lex-resource-botversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutBot](https://docs.aws.amazon.com/lex/latest/dg/API_PutBot.html)  **
  - **Description:** Creates or updates the $LATEST version of a Amazon Lex conversational bot
  - **Resource types (\*required):** [bot version\*](#list_lex-resource-botversion)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-aws_TagKeys)
  - **Access level:** Write

- **   [PutBotAlias](https://docs.aws.amazon.com/lex/latest/dg/API_PutBotAlias.html)  **
  - **Description:** Creates or updates an alias for the specific bot
  - **Resource types (\*required):** [bot alias\*](#list_lex-resource-botalias)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-aws_TagKeys)
  - **Access level:** Write

- **   [PutIntent](https://docs.aws.amazon.com/lex/latest/dg/API_PutIntent.html)  **
  - **Description:** Creates or updates the $LATEST version of an intent
  - **Resource types (\*required):** [intent version\*](#list_lex-resource-intentversion)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutSession](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PutSession.html)  **
  - **Description:** Creates a new session or modifies an existing session with an Amazon Lex bot
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot version](#list_lex-resource-botversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutSlotType](https://docs.aws.amazon.com/lex/latest/dg/API_PutSlotType.html)  **
  - **Description:** Creates or updates the $LATEST version of a slot type
  - **Resource types (\*required):** [slottype version\*](#list_lex-resource-slottypeversion)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartImport](https://docs.aws.amazon.com/lex/latest/dg/API_StartImport.html)  **
  - **Description:** Starts a job to import a resource to Amazon Lex
  - **Resource types (\*required):** [bot](#list_lex-resource-bot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-aws_TagKeys)
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-aws_TagKeys)
  - **Access level:** Write

- **   [StartMigration](https://docs.aws.amazon.com/lex/latest/dg/API_StartMigration.html)  **
  - **Description:** Grants permission to migrate a bot from Amazon Lex v1 to Amazon Lex v2
  - **Resource types (\*required):** [bot version\*](#list_lex-resource-botversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/lex/latest/dg/API_TagResource.html)  **
  - **Description:** Adds or overwrites tags to a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-resource-bot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-aws_TagKeys)
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-aws_TagKeys)
  - **Resource types (\*required):** [channel](#list_lex-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/lex/latest/dg/API_UntagResource.html)  **
  - **Description:** Removes tags from a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-resource-bot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-aws_TagKeys)
  - **Resource types (\*required):** [bot alias](#list_lex-resource-botalias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-aws_TagKeys)
  - **Resource types (\*required):** [channel](#list_lex-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by Amazon Lex
<a name="list_lex-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [bot](https://docs.aws.amazon.com/lex/latest/dg/API_BotMetadata.html)  | arn:${Partition}:lex:${Region}:${Account}:bot/${BotId}, arn:${Partition}:lex:${Region}:${Account}:bot:${BotName} | [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_) | 
|  [bot alias](https://docs.aws.amazon.com/lex/latest/dg/API_BotAliasMetadata.html)  | arn:${Partition}:lex:${Region}:${Account}:bot-alias/${BotId}/${BotAliasId}, arn:${Partition}:lex:${Region}:${Account}:bot:${BotName}:${BotAlias} | [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_) | 
|  [bot version](https://docs.aws.amazon.com/lex/latest/dg/API_BotMetadata.html)  | arn:${Partition}:lex:${Region}:${Account}:bot:${BotName}:${BotVersion} | [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_) | 
|  [channel](https://docs.aws.amazon.com/lex/latest/dg/API_BotChannelAssociation.html)  | arn:${Partition}:lex:${Region}:${Account}:bot-channel:${BotName}:${BotAlias}:${ChannelName} | [aws:ResourceTag/${TagKey}](#list_lex-aws_ResourceTag___TagKey_) | 
|  [intent version](https://docs.aws.amazon.com/lex/latest/dg/API_Intent.html)  | arn:${Partition}:lex:${Region}:${Account}:intent:${IntentName}:${IntentVersion} |   | 
|  [slottype version](https://docs.aws.amazon.com/lex/latest/dg/API_SlotTypeMetadata.html)  | arn:${Partition}:lex:${Region}:${Account}:slottype:${SlotName}:${SlotVersion} |   | 

## Condition keys for Amazon Lex
<a name="list_lex-policy-keys"></a>

Amazon Lex defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags attached to a Lex resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the set of tag keys in the request | ArrayOfString | 
|   [lex:associatedIntents](https://docs.aws.amazon.com/lex/latest/dg/security_iam_service-with-iam.html)  | Enables you to control access based on the intents included in the request | ArrayOfString | 
|   [lex:associatedSlotTypes](https://docs.aws.amazon.com/lex/latest/dg/security_iam_service-with-iam.html)  | Enables you to control access based on the slot types included in the request | ArrayOfString | 
|   [lex:channelType](https://docs.aws.amazon.com/lex/latest/dg/security_iam_service-with-iam.html)  | Enables you to control access based on the channel type included in the request | String | 