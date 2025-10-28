End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Exercise 5: Create an Alias (AWS CLI)

An alias is a pointer to a specific version of a bot. With an alias you can easily
update the version that your client applications are using. For more information, see
[Versioning and Aliases](versioning-aliases.md "versioning-aliases.md").To run the
commands in this exercise, you need to know the region where the commands will be run.
For a list of regions, see [Model Building
Quotas](gl-limits.md#gl-limits-model-building "gl-limits.md#gl-limits-model-building") .

###### To create an alias (AWS CLI)

1. In the AWS CLI, get the version of the `OrderFlowersBot` bot that you
   created in [Exercise 4: Publish a Version (AWS CLI)](gs-cli-publish.md "gs-cli-publish.md").

```
aws lex-models get-bot \
    --region `region` \
    --name OrderFlowersBot \
    --version-or-alias `version` > OrderFlowersBot_V5.json
```

2. In a text editor, open `OrderFlowersBot_v5.json`. Find
   and record the version number.
3. In the AWS CLI, create the bot alias:

```
aws lex-models put-bot-alias  \
    --region `region` \
    --name PROD \
    --bot-name OrderFlowersBot \
    --bot-version `version`
```

The following is the reponse from the server:

```
{
    "name": "PROD",
    "createdDate": timestamp,
    "checksum": "checksum",
    "lastUpdatedDate": timestamp,
    "botName": "OrderFlowersBot",
    "botVersion": "1"
}}

```

## Next Step

[Exercise 6: Clean Up (AWS CLI)](gs-cli-clean-up.md "gs-cli-clean-up.md")
