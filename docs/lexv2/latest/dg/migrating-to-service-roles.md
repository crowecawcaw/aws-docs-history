# Migrating to service roles for Amazon Lex V2

Amazon Lex V2 is transitioning from AWS-managed
_service-linked roles_ (SLRs) to customer-managed [service roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") for bot runtime permissions. This topic explains why
Amazon Lex V2 is making this change, how to migrate your existing bots, and
the timeline for the transition.

## Why Amazon Lex V2 is moving to service roles

A service-linked role is an IAM role that is linked directly to
Amazon Lex V2 and is managed by AWS. Service-linked roles do not honor the
service control policies (SCPs) that you configure in AWS
Organizations.

A service role is an IAM role that you own and manage in your own
account. Because a service role is a standard customer-managed role, it
respects the service control policies (SCPs) that you configure in your
organization. This gives you full control over the permissions that
Amazon Lex V2 uses on your behalf. Moving to service roles aligns
Amazon Lex V2 with IAM best practices and improves your security and
compliance posture.

## Migrate an existing bot to a service role

You can migrate an existing bot that uses a service-linked role to a
customer-managed service role directly from the Amazon Lex V2
console.

###### Note

Amazon Lex V2 plans to make single-bot migration using the
**Migrate to Service Role** button available before
September 1, 2026. After the button is available, complete the following
steps to migrate a bot.

1. Open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home "https://console.aws.amazon.com/lexv2/home").
2. In the left navigation pane, choose **Bots**, and
   then choose the bot that you want to migrate.
3. On the bot's **Draft version** page, if the bot is
   using a service-linked role, a banner appears indicating that the bot
   is using a service-linked role. Choose **Migrate to Service
   Role**.
4. Amazon Lex V2 creates a new customer-managed service role,
   attaches the permissions that your bot requires, and updates the bot to
   use the new role.
5. When the migration completes, the service-linked role banner and
   the **Migrate to Service Role** button no longer
   appear for the bot, confirming that the bot now uses a service
   role.

###### Note

The **Migrate to Service Role** button appears only
for a bot that is using a service-linked role. Migration does not modify
or delete your original service-linked role. If the migration does not
complete, your bot continues to use its existing service-linked role and
remains fully functional.

## Migration timeline

The transition from service-linked roles to service roles follows the
timeline described in the following list.

- **New bots** – New bots created
  in the console now default to a service role. We recommend creating new
  bots with a service role.
- **Migrating a single bot** – The
  one-click **Migrate to Service Role** button appears
  only for bots that use a service-linked role. With one click, you can
  migrate a bot to a service role. Amazon Lex V2 plans to make this
  available before September 1, 2026.
- **Migrating multiple bots** – A
  wizard lists your bots so that you can select multiple service-linked
  role bots and migrate them to service roles at once. Amazon Lex V2
  plans to make this available by September 15, 2026.
- **End of support for service-linked
  roles** – Support for service-linked roles ends by the
  end of 2026.
