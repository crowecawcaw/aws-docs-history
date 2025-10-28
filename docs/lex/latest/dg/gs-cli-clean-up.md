End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Exercise 6: Clean Up (AWS CLI)

Delete the resources that you created and clean up your account.

You can delete only resources that are not in use. In general, you should delete
resources in the following order.

1. Delete aliases to free up bot resources.
2. Delete bots to free up intent resources.
3. Delete intents to free up slot type resources.
4. Delete slot types.
   To run the commands in this exercise, you need to know the region where the commands
   will be run. For a list of regions, see [Model Building
   Quotas](gl-limits.md#gl-limits-model-building "gl-limits.md#gl-limits-model-building") .

###### To clean up your account (AWS CLI)

1. In the AWS CLI command line, delete the alias:

```
aws lex-models delete-bot-alias \
    --region `region` \
    --name PROD \
    --bot-name OrderFlowersBot
```

2. In the AWS CLI command line, delete the bot:

```
aws lex-models delete-bot \
    --region `region` \
    --name OrderFlowersBot
```

3. In the AWS CLI command line, delete the intent:

```
aws lex-models delete-intent \
    --region `region` \
    --name OrderFlowers
```

4. From the AWS CLI command line, delete the slot type:

```
aws lex-models delete-slot-type \
    --region `region` \
    --name FlowerTypes
```

You have removed all of the resources that you created and cleaned up your
account.
