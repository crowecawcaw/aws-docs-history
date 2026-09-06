

# Data retrieval APIs for Amazon Lex
<a name="amazonlex"></a>

Amazon Lex provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="lex-GetBot"></a>[GetBot](https://docs.aws.amazon.com/lex/latest/dg/API_GetBot.html) | Returns information for a specific bot. In addition to the bot name, the bot version or alias is required | Read | 
| <a name="lex-GetBotAlias"></a>[GetBotAlias](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotAlias.html) | Returns information about a Amazon Lex bot alias | Read | 
| <a name="lex-GetBotAliases"></a>[GetBotAliases](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotAliases.html) | Returns a list of aliases for a given Amazon Lex bot | List | 
| <a name="lex-GetBotChannelAssociation"></a>[GetBotChannelAssociation](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotChannelAssociation.html) | Returns information about the association between a Amazon Lex bot and a messaging platform | Read | 
| <a name="lex-GetBotChannelAssociations"></a>[GetBotChannelAssociations](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotChannelAssociations.html) | Returns a list of all of the channels associated with a single bot | List | 
| <a name="lex-GetBotVersions"></a>[GetBotVersions](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotVersions.html) | Returns information for all versions of a specific bot | List | 
| <a name="lex-GetBots"></a>[GetBots](https://docs.aws.amazon.com/lex/latest/dg/API_GetBots.html) | Returns information for the $LATEST version of all bots, subject to filters provided by the client | List | 
| <a name="lex-GetBuiltinIntent"></a>[GetBuiltinIntent](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinIntent.html) | Returns information about a built-in intent | Read | 
| <a name="lex-GetBuiltinIntents"></a>[GetBuiltinIntents](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinIntents.html) | Gets a list of built-in intents that meet the specified criteria | Read | 
| <a name="lex-GetBuiltinSlotTypes"></a>[GetBuiltinSlotTypes](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinSlotTypes.html) | Gets a list of built-in slot types that meet the specified criteria | Read | 
| <a name="lex-GetExport"></a>[GetExport](https://docs.aws.amazon.com/lex/latest/dg/API_GetExport.html) | Exports Amazon Lex Resource in a requested format | Read | 
| <a name="lex-GetImport"></a>[GetImport](https://docs.aws.amazon.com/lex/latest/dg/API_GetImport.html) | Gets information about an import job started with StartImport | Read | 
| <a name="lex-GetIntent"></a>[GetIntent](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntent.html) | Returns information for a specific intent. In addition to the intent name, you must also specify the intent version | Read | 
| <a name="lex-GetIntentVersions"></a>[GetIntentVersions](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntentVersions.html) | Returns information for all versions of a specific intent | List | 
| <a name="lex-GetIntents"></a>[GetIntents](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntents.html) | Returns information for the $LATEST version of all intents, subject to filters provided by the client | List | 
| <a name="lex-GetMigration"></a>[GetMigration](https://docs.aws.amazon.com/lex/latest/dg/API_GetMigration.html) | View an ongoing or completed migration | Read | 
| <a name="lex-GetMigrations"></a>[GetMigrations](https://docs.aws.amazon.com/lex/latest/dg/API_GetMigrations.html) | View list of migrations from Amazon Lex v1 to Amazon Lex v2 | List | 
| <a name="lex-GetSession"></a>[GetSession](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_GetSession.html) | Returns session information for a specified bot, alias, and user ID | Read | 
| <a name="lex-GetSlotType"></a>[GetSlotType](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotType.html) | Returns information about a specific version of a slot type. In addition to specifying the slot type name, you must also specify the slot type version | Read | 
| <a name="lex-GetSlotTypeVersions"></a>[GetSlotTypeVersions](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotTypeVersions.html) | Returns information for all versions of a specific slot type | List | 
| <a name="lex-GetSlotTypes"></a>[GetSlotTypes](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotTypes.html) | Returns information for the $LATEST version of all slot types, subject to filters provided by the client | List | 
| <a name="lex-GetUtterancesView"></a>[GetUtterancesView](https://docs.aws.amazon.com/lex/latest/dg/API_GetUtterancesView.html) | Returns a view of aggregate utterance data for versions of a bot for a recent time period | List | 
| <a name="lex-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/lex/latest/dg/API_ListTagsForResource.html) | Lists tags for a Lex resource | Read | 