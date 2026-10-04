

# Delete your instance
<a name="getting-started-delete"></a>

When you no longer need an Amazon Connect Talent instance, delete it from the Amazon Connect Talent console. Deleting an instance stops new evaluations and removes the instance, but some resources that were provisioned with the instance remain in your account and continue to count against your service quotas. To fully clean up, delete the instance and then remove the resources that remain.

**Warning**  
Deletion is permanent.  
Deleting a Customer Profiles domain deletes every candidate profile and its related data in that domain.
Deleting the Amazon S3 bucket deletes the interview recordings, chat transcripts, and reports stored in it.
Check your data-retention obligations before you delete either one.

## Step 1: Delete the instance
<a name="getting-started-delete-step1"></a>

1. Open the [Amazon Connect Talent console](https://console.aws.amazon.com/connect/v2/app/hiring).

1. Choose the instance alias you want to delete.

1. Choose **Delete**, then confirm.

1. Wait until the instance no longer appears in the console before you remove the remaining resources.

## Step 2: Remove the resources that remain
<a name="getting-started-delete-step2"></a>

Deleting an instance can leave the following resources in your account. They continue to count against your service quotas until you remove them. You can remove them using either the console or the AWS CLI.


| Resource | Name | 
| --- | --- | 
| Amazon Q in Connect assistant | `Talent AI Assistant ({{instance alias}})` | 
| Amazon Connect Cases domain | `{{instance alias}}` | 
| Amazon Connect Customer Profiles domain | `amazon-connect-hiring-{{instance alias}}` | 
| Amazon Lex V2 bots (3) | `{{instance alias}}-hiring-chat-lex-bot`, `{{instance alias}}-hiring-interview-lex-bot`, `{{instance alias}}-hiring-assessment-lex-bot` | 
| Amazon S3 bucket and IAM roles (console-created instances only) | `amazon-connect-{{id}}`, `AmazonConnectHiringRole-{{instance ID}}`, `AmazonLexTestWorkbenchServiceRole-{{Region code}}-{{instance ID prefix}}` | 

**Note**  
If you create a new instance with the same alias, it reuses the remaining Amazon Connect Cases domain, Amazon Connect Customer Profiles domain, and Amazon Lex bots. It does not reuse the assistant — every new instance creates a new one. Only active assistants count toward the quota, so deleting an assistant that no instance uses frees a slot.

Choose a method:
+ **Using the console** — delete each resource in its service console. Best for a one-time cleanup of a single instance.
+ **Using the AWS CLI** — list and delete the resources with commands. Best when you manage several instances or want to confirm which resources are still in use before deleting.

### Using the console
<a name="getting-started-delete-console"></a>

Delete each remaining resource in its own service console, in this order. Confirm each resource belongs to the deleted instance before you remove it.

1. **Amazon Lex bots** — In the Amazon Lex console, first disassociate each bot from the instance, then delete the three bots named `{{instance alias}}-hiring-chat-lex-bot`, `{{instance alias}}-hiring-interview-lex-bot`, and `{{instance alias}}-hiring-assessment-lex-bot`.

1. **Amazon Connect Customer Profiles domain** — In the Amazon Connect Customer Profiles console, delete the domain named `amazon-connect-hiring-{{instance alias}}`.

1. **Amazon Connect Cases domain** — In the Amazon Connect Cases console, delete the domain named for the instance alias.

1. **Amazon Q in Connect assistant** — In the Amazon Q in Connect console, delete the assistant named `Talent AI Assistant ({{instance alias}})`.

1. **(Console-created instances only) Amazon S3 bucket and IAM roles** — Delete the S3 bucket `amazon-connect-{{id}}` if it holds only the deleted instance's data, and remove the instance-specific IAM roles. Do not delete the shared roles `AWSServiceRoleForLexV2Bots_AmazonConnect_{{account ID}}` and `AmazonConnectEmailSESAccessRole`.

**Note**  
If you can't identify which resources were left behind, contact AWS Support.

### Using the AWS CLI
<a name="getting-started-delete-cli"></a>

Use AWS CLI version 2, with credentials that can list and delete the resources below. Run every command in the same AWS Region as the deleted instance.

```
export AWS_REGION={{region}}        # for example, us-west-2
```

**Step 1: List the resources your active instances use**

Keep this output. Don't delete any resource whose ARN or ID appears in it.

```
for id in $(aws connect list-instances \
    --query "InstanceSummaryList[?InstanceStatus=='ACTIVE'].Id" --output text); do
  aws connect list-integration-associations --instance-id "$id" --integration-type WISDOM_ASSISTANT \
    --query "IntegrationAssociationSummaryList[].IntegrationArn" --output text
  aws connect list-integration-associations --instance-id "$id" --integration-type CASES_DOMAIN \
    --query "IntegrationAssociationSummaryList[].IntegrationArn" --output text
  aws connect list-bots --instance-id "$id" --lex-version V2 \
    --query "LexBots[].LexV2Bot.AliasArn" --output text
done
```

**Step 2: Delete remaining Amazon Q in Connect assistants**

Several assistants can share a name, because each instance creation makes a new one. Compare ARNs, not names. For each assistant whose ARN isn't in the Step 1 output:

```
aws qconnect list-assistants \
  --query "assistantSummaries[?starts_with(name,'Talent AI Assistant')].[assistantId,name,assistantArn]" \
  --output text

aws qconnect delete-assistant --assistant-id {{assistant-id}}
```

**Step 3: Delete the remaining Amazon Connect Cases domain**

A Cases domain has the same name as its instance's alias. Delete it only if its ARN isn't in the Step 1 output.

```
aws connectcases list-domains --query "domains[].[domainId,name,domainArn]" --output text
aws connectcases delete-domain --domain-id {{domain-id}}
```

**Step 4: Delete the remaining Amazon Connect Customer Profiles domain**

The domain name is `amazon-connect-hiring-` followed by the instance alias. If the alias is longer than 42 characters, only its first 42 characters are used. Check which instance it's connected to before deleting.

```
aws customer-profiles list-domains \
  --query "Items[?starts_with(DomainName,'amazon-connect-hiring-')].DomainName" --output text

aws customer-profiles list-integrations --domain-name amazon-connect-hiring-{{alias}} \
  --query "Items[].Uri" --output text

aws customer-profiles delete-domain --domain-name amazon-connect-hiring-{{alias}}
```

If the integrations output shows the ARN of an active instance, keep the domain.

**Step 5: Delete the remaining Amazon Lex bots**

Each instance has three bots: `{{alias}}-hiring-chat-lex-bot`, `{{alias}}-hiring-interview-lex-bot`, and `{{alias}}-hiring-assessment-lex-bot`.

```
aws lexv2-models list-bots --max-results 1000 \
  --filters name=BotName,values={{alias}}-hiring-,operator=CO \
  --query "botSummaries[].[botId,botName]" --output text

aws lexv2-models delete-bot --bot-id {{bot-id}} --skip-resource-in-use-check
```

Include `--max-results 1000`; without it, the command returns only the first 10 bots. A Lex alias ARN contains the bot ID, in the form `bot-alias/{{bot-id}}/{{alias-id}}` — check each bot ID against the Step 1 output before deleting. Each Connect Talent bot has aliases, so the delete fails without `--skip-resource-in-use-check`; that flag also skips Lex's own in-use safety check, so always confirm with Step 1 first.

**Step 6 (console-created instances only): Delete the Amazon S3 bucket and IAM roles**

These don't affect the quotas that limit instance creation. Delete them if you no longer need them.

*Amazon S3 bucket.* The console creates a bucket named `amazon-connect-{{id}}` and stores the instance's data under the prefix `connect/{{alias}}/`. Confirm the bucket belongs to the deleted instance before deleting it.

```
aws s3 ls s3://amazon-connect-{{id}}/connect/
aws s3 rb s3://amazon-connect-{{id}} --force
```

If the bucket has versioning turned on, empty it in the S3 console first; `--force` doesn't delete object versions.

*IAM roles.* IAM is global, so these commands don't depend on the Region.

```
aws iam list-roles --query "Roles[?starts_with(RoleName,'AmazonConnectHiringRole-') || starts_with(RoleName,'AmazonLexTestWorkbenchServiceRole-')].RoleName" --output text

# For each role that belongs to a deleted instance:
aws iam list-attached-role-policies --role-name {{role-name}} --query "AttachedPolicies[].PolicyArn" --output text
aws iam detach-role-policy --role-name {{role-name}} --policy-arn {{policy-arn}}
aws iam list-role-policies --role-name {{role-name}} --query "PolicyNames" --output text
aws iam delete-role-policy --role-name {{role-name}} --policy-name {{policy-name}}
aws iam delete-role --role-name {{role-name}}
```

If a detached policy is named for the deleted instance (ARN `arn:aws:iam::{{account ID}}:policy/service-role/AmazonConnectHiringServicePolicy-{{instance ID}}`), delete it too:

```
aws iam delete-policy --policy-arn {{policy-arn}}
```

Instances created earlier might instead use a shared policy named `AmazonConnectHiringServicePolicy`, with no instance ID. Don't delete the shared policy while other roles still use it — the console shows which roles use it on the policy's **Entities attached** tab. Don't delete the shared roles `AWSServiceRoleForLexV2Bots_AmazonConnect_{{account ID}}` or `AmazonConnectEmailSESAccessRole`; all instances in the account share them.