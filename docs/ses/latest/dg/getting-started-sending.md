

# Getting started with sending email

Follow this page to set up Amazon Simple Email Service (Amazon SES) to send email. By the end, you have a verified domain, safe account defaults, and your first email sent. Each step gives AWS CLI and console instructions, and then explains what it set up, with links to the full topics. The resources that you create might result in charges to your AWS account, and the last section explains how to clean them up.

**Tip**  
Using an AI coding agent? Connect it to AWS with the [Agent setup guide](agent-setup-guide.md), and then ask it to set up your domain for Amazon SES.

## Before you begin
<a name="setting-up"></a>
+ An AWS account. For more information, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html).
+ The AWS CLI, installed and signed in, if you follow the AWS CLI steps. For instructions, see [Setting up the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html).
+ Permission to use SES. For more information, see [Identity and access management in Amazon SES](control-user-access.md).
+ A domain where you can add Domain Name System (DNS) records, such as `example.com`. To send from a subdomain such as `mail.example.com`, use the subdomain everywhere this page says domain.

SES settings apply to one AWS Region. Use the Region where your application runs.

For more information about the Regions where SES is available, see [Regions and Amazon SES](regions.md). If you aren't sure which Region to use, run `aws configure get region` to see the one that your AWS CLI already uses.

If you use the AWS CLI, set these variables once. In every command on this page, replace each value in angle brackets, such as `<YOUR_DOMAIN>`, with your own:

```bash
export DOMAIN="<YOUR_DOMAIN>"        # your sending domain, such as example.com
export AWS_REGION="<YOUR_REGION>"    # the Region where your application runs, such as us-east-1
```

**Tip**  
To run every AWS CLI step at once instead, use the script under [Run every step as one script](#getting-started-script).

## Step 1: Create your domain identity
<a name="getting-started-identity"></a>

A [domain identity](creating-identities.md) tells SES which domain you send from. Once SES verifies the domain, you can send from any address on that domain. This step also sets up email authentication, so mailbox providers can tell that your mail really comes from you.

------
#### [ AWS CLI ]

Create the identity with the following AWS CLI command:

```bash
aws sesv2 create-email-identity \
  --email-identity "$DOMAIN" \
  --dkim-signing-attributes NextSigningKeyLength=RSA_2048_BIT
```

The output lists three DomainKeys Identified Mail (DKIM) tokens and shows `"VerifiedForSendingStatus": false`. That is expected until you publish the DNS records in Step 2.

Then set a Custom MAIL FROM domain with the following AWS CLI command, so that bounces return to your own domain:

```bash
aws sesv2 put-email-identity-mail-from-attributes \
  --email-identity "$DOMAIN" \
  --mail-from-domain "bounce.$DOMAIN" \
  --behavior-on-mx-failure USE_DEFAULT_VALUE
```

This command returns no output.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. Under **Configuration**, choose **Identities**, and then choose **Create identity**.

1. Choose **Domain**, and enter your domain.

1. Select **Use a custom MAIL FROM domain**. Enter `bounce` as the subdomain, and for **Behavior on MX failure**, choose **Use default MAIL FROM domain**.

1. If Route 53 hosts your domain, keep **Enabled** selected for **Publish DNS records to Route53**. SES then publishes the DKIM and MAIL FROM records for you.

1. Choose **Create identity**. Easy DKIM with 2048-bit keys is the default.

------

What this step sets up:

[Easy DKIM](send-email-authentication-dkim-easy.md)  
DKIM is a signature on each message. It lets the receiver confirm that the message came from your domain and wasn't changed on the way. With Easy DKIM, SES signs your mail with a 2048-bit key that it creates and rotates for you.

[Custom MAIL FROM domain](mail-from.md)  
Bounces return to `bounce.`{{your-domain}} instead of `amazonses.com`. Your mail then also passes [Sender Policy Framework (SPF)](send-email-authentication-spf.md), a check that the sending server is allowed to send for your domain. With `USE_DEFAULT_VALUE`, if the `bounce` DNS records ever go missing, SES uses its own MAIL FROM domain instead of rejecting your mail.

For other options, such as using your own DKIM keys, see [Creating a domain identity](creating-identities.md#verify-domain-procedure).

## Step 2: Publish DNS records
<a name="getting-started-dns"></a>

SES verifies your domain by looking up records in your domain's DNS, so add them before you send. In this step, you add six records at your DNS provider. Any DNS provider works: your domain doesn't have to use Route 53.

------
#### [ AWS CLI ]

Get the three DKIM tokens and the signing zone with the following AWS CLI command. You need them for the CNAME records in the table that follows:

```bash
aws sesv2 get-email-identity --email-identity "$DOMAIN" \
  --query 'DkimAttributes.{SigningHostedZone:SigningHostedZone,Tokens:Tokens}'
```

Then add the six records from the table at your DNS provider. If Route 53 hosts your domain, you can publish them with the script under [Optional: Publish the records with Route 53 using the AWS CLI](#getting-started-dns-route53).

------
#### [ Console ]

If you kept **Publish DNS records to Route53** enabled in Step 1, the DKIM and MAIL FROM records are already published; add only the DMARC record from the table that follows. Otherwise, open your domain under **Identities**, expand each **Publish DNS records** section, and copy the records to your DNS provider.

------


**DNS records to publish**  

| Type | Name | Value | 
| --- | --- | --- | 
| CNAME (3 records, one per token) | `{{TOKEN}}._domainkey.{{your-domain}}` | `{{TOKEN}}.{{SIGNING_HOSTED_ZONE}}` | 
| MX | `bounce.{{your-domain}}` | `10 feedback-smtp.{{REGION}}.amazonses.com` | 
| TXT | `bounce.{{your-domain}}` | `"v=spf1 include:amazonses.com ~all"` | 
| TXT | `_dmarc.{{your-domain}}` | `"v=DMARC1; p=none;"`. Skip this record if `_dmarc` already has a value. | 

What these records do:

CNAME records  
Prove that you control the domain, and publish the [Easy DKIM](send-email-authentication-dkim-easy.md) keys that receivers use to check your signature.

MX and TXT records on `bounce`  
Make the [Custom MAIL FROM domain](mail-from.md) work. The mail exchanger (MX) record receives bounces, and the TXT record is the [SPF](send-email-authentication-spf.md) record. Both are on the `bounce` subdomain, so the mail records on your domain stay as they are.

TXT record on `_dmarc`  
Publishes a [Domain-based Message Authentication, Reporting, and Conformance (DMARC)](send-email-authentication-dmarc.md) policy. DMARC tells receivers what to do with mail that fails [DKIM](send-email-authentication-dkim.md) and [SPF](send-email-authentication-spf.md). The `p=none` policy asks them to report that mail without blocking it.

### Optional: Publish the records with Route 53 using the AWS CLI
<a name="getting-started-dns-route53"></a>

This is a shortcut for domains that use Route 53 for DNS. SES doesn't require Route 53; with any other provider, add the records from the table by hand. Set `ZONE_ID` to your hosted zone ID and run these commands. Each record is created with `CREATE`, so an existing record is never overwritten; that command fails instead.

```bash
export ZONE_ID="<YOUR_HOSTED_ZONE_ID>"   # from: aws route53 list-hosted-zones-by-name --dns-name "$DOMAIN"

read -r SIGNING_ZONE T1 T2 T3 <<< "$(aws sesv2 get-email-identity --email-identity "$DOMAIN" \
  --query '[DkimAttributes.SigningHostedZone, DkimAttributes.Tokens[0], DkimAttributes.Tokens[1], DkimAttributes.Tokens[2]]' \
  --output text)"

add_record() {
  aws route53 change-resource-record-sets --hosted-zone-id "$ZONE_ID" --change-batch \
    "{\"Changes\":[{\"Action\":\"CREATE\",\"ResourceRecordSet\":{\"Name\":\"$2\",\"Type\":\"$1\",\"TTL\":1800,\"ResourceRecords\":[{\"Value\":\"$3\"}]}}]}"
}

for T in "$T1" "$T2" "$T3"; do add_record CNAME "$T._domainkey.$DOMAIN" "$T.$SIGNING_ZONE"; done
add_record MX  "bounce.$DOMAIN" "10 feedback-smtp.$AWS_REGION.amazonses.com"
add_record TXT "bounce.$DOMAIN" '\"v=spf1 include:amazonses.com ~all\"'
add_record TXT "_dmarc.$DOMAIN" '\"v=DMARC1; p=none;\"'
```

A command that fails with `InvalidChangeBatch` and `but it already exists` found a record with that name. Leave it in place. For `_dmarc`, this means your domain already has a DMARC policy.

## Step 3: Request production access
<a name="getting-started-production-access"></a>

New accounts start in the [sandbox](request-production-access.md): you can send only to verified addresses and the mailbox simulator, up to 200 messages a day. Production access removes those limits. Request it now, so that you can send to any recipient.

The request asks what kind of email you send. Choose `TRANSACTIONAL` for messages that a user action triggers, such as receipts and password resets, or `MARKETING` for promotional mail, such as newsletters. Give your real website URL and a contact address where you already receive email. Setting up a domain for sending doesn't give it a mailbox, so don't use a new address on that domain.

------
#### [ AWS CLI ]

Submit the request with the following AWS CLI command:

```bash
aws sesv2 put-account-details \
  --production-access-enabled \
  --mail-type TRANSACTIONAL \
  --website-url "<YOUR_WEBSITE_URL>" \
  --contact-language EN \
  --additional-contact-email-addresses "<YOUR_CONTACT_EMAIL>"
```

This command returns no output.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. Choose **Account dashboard**. In the sandbox banner, choose **View Get set up page**, and then choose **Request production access**.

1. Choose the mail type, and enter your website URL and contact addresses. Select the acknowledgement, and choose **Submit request**.

------

AWS sends the decision to the contact address. You don't need to wait for it: continue with the next steps. Step 5 shows how to check the status of your request. For what the review covers, see [Request production access (Moving out of the Amazon SES sandbox)](request-production-access.md).

## Step 4: Apply recommended settings
<a name="getting-started-settings"></a>

To turn these settings off later, see [Clean up resources](#getting-started-clean-up). Your domain can send without this step. These settings protect your sender reputation from the first message: SES stops sending to addresses that bounced or complained, and you can see how your mail performs. Apply them before you send from your application. The configuration set applies to this domain only. The other two settings apply to every domain in your account in this Region.

------
#### [ AWS CLI ]

Create a configuration set with the following AWS CLI commands, and make it the default for your domain. The name is `default-` followed by your domain, with dots replaced by underscores:

```bash
export CONFIG_SET="default-${DOMAIN//./_}"   # for example.com: default-example_com

aws sesv2 create-configuration-set \
  --configuration-set-name "$CONFIG_SET" \
  --delivery-options TlsPolicy=OPTIONAL \
  --reputation-options ReputationMetricsEnabled=true \
  --sending-options SendingEnabled=true

aws sesv2 put-email-identity-configuration-set-attributes \
  --email-identity "$DOMAIN" \
  --configuration-set-name "$CONFIG_SET"
```

If `create-configuration-set` reports `AlreadyExistsException`, keep the existing set and continue. If your domain already had a default configuration set, the second command replaces it.

Then turn on the account-level suppression list and Virtual Deliverability Manager with the following AWS CLI commands:

```bash
aws sesv2 put-account-suppression-attributes --suppressed-reasons BOUNCE COMPLAINT

aws sesv2 put-account-vdm-attributes --vdm-attributes \
  'VdmEnabled=ENABLED,GuardianAttributes={OptimizedSharedDelivery=ENABLED}'
```

None of these commands return output when they succeed. If Virtual Deliverability Manager is already turned on in your account, skip the last command: it replaces your current Virtual Deliverability Manager settings.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. Under **Configuration**, choose **Configuration sets**, and then choose **Create set**. For the name, enter `default-` followed by your domain with dots replaced by underscores, such as `default-example_com`. Under **Reputation options**, select **Enabled**. Leave the other settings as they are, and choose **Create set**.

1. Choose **Identities**, and open your domain. On the **Configuration set** tab, choose **Edit** in the **Default configuration set** container, choose the set that you created, and save your changes.

1. Choose **Suppression list**. In **Account-level settings**, choose **Edit**, and select **Enabled**. For **Suppression reasons**, choose **Bounces and complaints**, and then choose **Save changes**.

1. Choose **Virtual Deliverability Manager**, and then choose **Get started with Virtual Deliverability Manager**. On the **Select Engagement tracking** page, choose **Turn off engagement tracking**, and then choose **Next**. On the **Select Optimized shared delivery** page, keep optimized shared delivery turned on, and choose **Next**. On the **Review and enable** page, choose **Enable Virtual Deliverability Manager**.

------

What this step sets up:

[Configuration set](using-configuration-sets.md)  
A group of rules that SES applies to each message sent with it. This one turns on reputation metrics, so you can see the bounce and complaint rates for your mail, and it encrypts with TLS whenever the receiving server supports it. Making it the default for your domain applies it to every message from that domain, with no change to your application.

[Account-level suppression list](sending-email-suppression-list.md)  
Stops SES from sending again to an address that hard bounced or whose owner reported your mail as spam. Repeated sends to those addresses damage your reputation.

[Virtual Deliverability Manager](vdm.md)  
Shows how your mail performs with each mailbox provider and recommends fixes. This step also turns on optimized shared delivery, which picks the best shared IP addresses for each message. It leaves engagement tracking off, because engagement tracking records opens and clicks by changing the links in your email. To turn it on later, see [Virtual Deliverability Manager settings](vdm-settings.md).

## Step 5: Check that setup is complete
<a name="getting-started-verify"></a>

SES looks for your DNS records on its own. It usually finds them within a few minutes, and it keeps checking for up to 72 hours.

------
#### [ AWS CLI ]

Check the status of your domain with the following AWS CLI command:

```bash
aws sesv2 get-email-identity --email-identity "$DOMAIN" --query '{
  VerifiedForSending: VerifiedForSendingStatus,
  Dkim: DkimAttributes.Status,
  MailFrom: MailFromAttributes.MailFromDomainStatus,
  ConfigurationSet: ConfigurationSetName}'
```

```json
{
    "VerifiedForSending": true,
    "Dkim": "SUCCESS",
    "MailFrom": "SUCCESS",
    "ConfigurationSet": "default-example_com"
}
```

Setup is complete when `VerifiedForSending` is `true`, and `Dkim` and `MailFrom` are `SUCCESS`. `ConfigurationSet` shows the name of your configuration set from Step 4.

Then check your production access request from Step 3 with the following AWS CLI command:

```bash
aws sesv2 get-account --query '{
  ProductionAccess: ProductionAccessEnabled,
  Review: Details.ReviewDetails.Status}'
```

```json
{
    "ProductionAccess": false,
    "Review": "PENDING"
}
```

`Review` is `PENDING` while AWS reviews the request. When it changes to `GRANTED`, `ProductionAccess` is `true` and you can send to any recipient. If it changes to `DENIED`, see the message that AWS sent to your contact address.

------
#### [ Console ]

In the Amazon SES console, under **Identities**, open your domain. The identity status is **Verified**, and DKIM and the Custom MAIL FROM domain show **Successful**. The **Account dashboard** shows your production access status.

------

If DKIM or MAIL FROM shows a failure, a record from Step 2 is missing or has a typo. Fix it, and SES checks again. For other causes, see [Domain and Email address verification problems](troubleshoot-verification.md).

## Step 6: Send your first email
<a name="getting-started-first-send"></a>

Send a message to the [mailbox simulator](send-an-email-from-console.md#send-email-simulator), a set of test addresses that SES provides. Mail to the simulator works in the sandbox, and it doesn't affect your bounce and complaint rates.

------
#### [ AWS CLI ]

Send the message with the following AWS CLI command:

```bash
aws sesv2 send-email \
  --from-email-address "hello@$DOMAIN" \
  --destination ToAddresses=success@simulator.amazonses.com \
  --content 'Simple={Subject={Data="Hello from Amazon SES"},Body={Text={Data="It works."}}}'
```

The output is a message ID. If the command fails with `Email address is not verified`, Step 5 isn't complete yet.

------
#### [ Console ]

In the Amazon SES console, under **Identities**, open your domain and choose **Send test email**. Enter a from address such as `hello`, keep the **Successful delivery** scenario, add a subject and body, and choose **Send test email**.

------

A message ID means SES accepted the message. Accepted is not the same as delivered. Once you have production access, send to your own address to see it in a real inbox. When you no longer need this setup, see [Clean up resources](#getting-started-clean-up). To follow what happens to a message after SES accepts it, see [Monitoring your Amazon SES sending activity](monitor-sending-activity.md).

## Run every step as one script
<a name="getting-started-script"></a>

To skip the individual steps, save this script as `setup-ses.sh` and run `bash setup-ses.sh`. It asks for your domain, your website URL, and a contact email, and it uses the Region that your AWS CLI is set to. If you give it a Route 53 hosted zone ID, it also publishes the DNS records; otherwise it prints them for you to add. It runs Steps 1–6 in order. You can run it again safely: it keeps anything that already exists.

The script requests production access for `TRANSACTIONAL` mail. Change that value to `MARKETING` if you mostly send promotional mail.

### setup-ses.sh
<a name="getting-started-script-code"></a>

```bash
#!/usr/bin/env bash
# Set up Amazon SES for one domain with the defaults on this page.
set -euo pipefail
# Optional: labels these requests so that you can trace them in CloudTrail. You can delete this line.
export AWS_SDK_UA_APP_ID=${AWS_SDK_UA_APP_ID:-AWSDocs-SES-GettingStarted}

# The script needs these values. Set them in your shell first, or answer the prompts.
ask() {  # variable name, prompt
  [ -n "${!1:-}" ] || read -r -p "$2: " "$1" || true
}
ask DOMAIN        "Domain to send from"
ask WEBSITE_URL   "Your website URL, for the production access request"
ask CONTACT_EMAIL "Contact email where you already receive mail"
ask ZONE_ID       "Route 53 hosted zone ID (press Enter to add the DNS records yourself)"
export AWS_REGION=${AWS_REGION:-${AWS_DEFAULT_REGION:-$(aws configure get region)}}

if [ -z "${DOMAIN:-}" ] || [ -z "${WEBSITE_URL:-}" ] || [ -z "${CONTACT_EMAIL:-}" ] || [ -z "$AWS_REGION" ]; then
  echo "Stopped: a domain, a website URL, a contact email, and an AWS Region are required." >&2
  exit 1
fi
ZONE_ID=${ZONE_ID:-}
echo "Setting up $DOMAIN in $AWS_REGION."

CONFIG_SET="default-${DOMAIN//./_}"   # the domain's default configuration set, such as default-example_com
ERR=$(mktemp)

# Run a command, but treat "already exists" as success so a rerun changes nothing.
keep_existing() {
  "$@" > /dev/null 2> "$ERR" || grep -q -i -E "already ?exist|ConflictException" "$ERR" || { cat "$ERR"; exit 1; }
}

# Step 1: the domain identity with 2048-bit Easy DKIM, and the bounce. MAIL FROM domain unless
# the domain already has one.
printf 'Step 1 of 6: Creating your domain identity... '
keep_existing aws sesv2 create-email-identity --email-identity "$DOMAIN" \
  --dkim-signing-attributes NextSigningKeyLength=RSA_2048_BIT
if [ "$(aws sesv2 get-email-identity --email-identity "$DOMAIN" --query MailFromAttributes.MailFromDomain --output text)" = "None" ]; then
  aws sesv2 put-email-identity-mail-from-attributes --email-identity "$DOMAIN" \
    --mail-from-domain "bounce.$DOMAIN" --behavior-on-mx-failure USE_DEFAULT_VALUE
fi
echo "done"

# Step 2: DNS records. With ZONE_ID set, create them in Route 53 (never overwrites); otherwise print them.
read -r SIGNING_ZONE T1 T2 T3 <<< "$(aws sesv2 get-email-identity --email-identity "$DOMAIN" \
  --query '[DkimAttributes.SigningHostedZone, DkimAttributes.Tokens[0], DkimAttributes.Tokens[1], DkimAttributes.Tokens[2]]' \
  --output text)"
add_record() {  # type, name, value
  if [ -n "$ZONE_ID" ]; then
    keep_existing aws route53 change-resource-record-sets --hosted-zone-id "$ZONE_ID" --change-batch \
      "{\"Changes\":[{\"Action\":\"CREATE\",\"ResourceRecordSet\":{\"Name\":\"$2\",\"Type\":\"$1\",\"TTL\":1800,\"ResourceRecords\":[{\"Value\":\"$3\"}]}}]}"
  else
    printf '%-6s %-60s %s\n' "$1" "$2" "${3//\\/}"
  fi
}
if [ -n "$ZONE_ID" ]; then
  printf 'Step 2 of 6: Publishing DNS records in Route 53... '
else
  echo "Step 2 of 6: Add these DNS records at your DNS provider (skip _dmarc if it already has a value):"
fi
for T in "$T1" "$T2" "$T3"; do add_record CNAME "$T._domainkey.$DOMAIN" "$T.$SIGNING_ZONE"; done
add_record MX  "bounce.$DOMAIN" "10 feedback-smtp.$AWS_REGION.amazonses.com"
add_record TXT "bounce.$DOMAIN" '\"v=spf1 include:amazonses.com ~all\"'
add_record TXT "_dmarc.$DOMAIN" '\"v=DMARC1; p=none;\"'
[ -z "$ZONE_ID" ] || echo "done"

# Step 3: request production access, unless the account has it or a request is under review.
printf 'Step 3 of 6: Requesting production access... '
case "$(aws sesv2 get-account --query '[ProductionAccessEnabled, Details.ReviewDetails.Status]' --output text)" in
  True*)    echo "your account already has it" ;;
  *PENDING) echo "your request is already under review" ;;
  *)
    keep_existing aws sesv2 put-account-details --production-access-enabled --mail-type TRANSACTIONAL \
      --website-url "$WEBSITE_URL" --contact-language EN --additional-contact-email-addresses "$CONTACT_EMAIL"
    echo "done" ;;
esac

# Step 4: one configuration set with opportunistic TLS and reputation metrics, made the domain's
# default unless the domain already has one.
printf 'Step 4 of 6: Applying recommended settings... '
keep_existing aws sesv2 create-configuration-set --configuration-set-name "$CONFIG_SET" \
  --delivery-options TlsPolicy=OPTIONAL --reputation-options ReputationMetricsEnabled=true \
  --sending-options SendingEnabled=true
if [ "$(aws sesv2 get-email-identity --email-identity "$DOMAIN" --query ConfigurationSetName --output text)" = "None" ]; then
  aws sesv2 put-email-identity-configuration-set-attributes --email-identity "$DOMAIN" \
    --configuration-set-name "$CONFIG_SET"
fi
# Suppress bounces and complaints account-wide, and turn on Virtual Deliverability Manager with
# optimized shared delivery unless the account already uses it.
aws sesv2 put-account-suppression-attributes --suppressed-reasons BOUNCE COMPLAINT
if [ "$(aws sesv2 get-account --query VdmAttributes.VdmEnabled --output text)" != "ENABLED" ]; then
  aws sesv2 put-account-vdm-attributes --vdm-attributes \
    'VdmEnabled=ENABLED,GuardianAttributes={OptimizedSharedDelivery=ENABLED}'
fi
echo "done"

# Step 5: wait up to 30 minutes for SES to find the DNS records.
echo "Step 5 of 6: Waiting for SES to verify $DOMAIN. This usually takes a few minutes."
for i in $(seq 60); do
  STATUS=$(aws sesv2 get-email-identity --email-identity "$DOMAIN" --output text --query \
    'join(`,`, [to_string(VerifiedForSendingStatus), DkimAttributes.Status, MailFromAttributes.MailFromDomainStatus])') || STATUS=
  [ "$STATUS" = "true,SUCCESS,SUCCESS" ] && break
  sleep 30
done
if [ "$STATUS" != "true,SUCCESS,SUCCESS" ]; then
  echo "Stopped: $DOMAIN is not verified after 30 minutes. Check the DNS records from Step 2, and then run this script again." >&2
  exit 1
fi
echo "             Verified."

# Step 6: send a first message to the mailbox simulator. A message ID means SES accepted it.
printf 'Step 6 of 6: Sending a test email... '
MESSAGE_ID=$(aws sesv2 send-email --from-email-address "hello@$DOMAIN" \
  --destination ToAddresses=success@simulator.amazonses.com \
  --content 'Simple={Subject={Data="Hello from Amazon SES"},Body={Text={Data="It works."}}}' \
  --query MessageId --output text)
echo "done"
echo "Setup complete. SES accepted the test email with message ID $MESSAGE_ID."
```

## What's in your account when you finish
<a name="getting-started-result"></a>


| Item | State after setup | 
| --- | --- | 
| [Domain identity](creating-identities.md#verify-domain-procedure) | {{your-domain}}, verified | 
| [Easy DKIM](send-email-authentication-dkim-easy.md) | Turned on, with 2048-bit keys that SES rotates | 
| [Custom MAIL FROM domain](mail-from.md) | `bounce.`{{your-domain}} | 
| [DMARC policy](send-email-authentication-dmarc.md) | `p=none`, unless your domain already had a policy | 
| [Configuration set](using-configuration-sets.md) | `default-example_com` for the domain `example.com`. It is your domain's default and has reputation metrics turned on. | 
| [Account-level suppression list](sending-email-suppression-list.md) | Turned on for `BOUNCE` and `COMPLAINT` | 
| [Virtual Deliverability Manager](vdm.md) | Turned on, with optimized shared delivery | 
| [Production access](request-production-access.md) | Requested | 

## Clean up resources
<a name="getting-started-clean-up"></a>

To avoid ongoing charges, delete the resources that you created on this page when you no longer need them. For current pricing, see [Amazon SES Pricing](https://aws.amazon.com/ses/pricing/).

Delete the domain identity and the configuration set with the following AWS CLI commands, or delete them in the Amazon SES console under **Identities** and **Configuration sets**:

```bash
aws sesv2 delete-email-identity --email-identity "$DOMAIN"

aws sesv2 delete-configuration-set --configuration-set-name "$CONFIG_SET"
```

Then delete the DNS records that you added in Step 2 at your DNS provider.

The account-level suppression list, Virtual Deliverability Manager, and production access apply to your whole account, so leave them in place if anything else in the account uses SES. If nothing else does, turn off Virtual Deliverability Manager with the following AWS CLI command:

```bash
aws sesv2 put-account-vdm-attributes --vdm-attributes VdmEnabled=DISABLED
```

## Next steps
<a name="getting-started-next-steps"></a>
+ Send from your application: [Sending email through Amazon SES using an AWS SDK](send-an-email-using-sdk-programmatically.md) or [Using SMTP to send email](send-email-smtp.md).
+ Get bounce, complaint, and delivery events: [Step 2: Add an event destination](event-publishing-add-event-destination.md).
+ Raise your sending quota: [Managing your Amazon SES sending limits](manage-sending-quotas.md).
+ Receive email for your domain: [Email receiving with Amazon SES](receiving-email.md).
+ Move from another email provider: [Migrating to Amazon SES from another email-sending solution](send-email-getting-started-migrate.md).

## Console setup wizard
<a name="quick-start-verify-email-addresses"></a>

New accounts with no identities see a **Get started** wizard on the Amazon SES console home page. It verifies a domain and requests production access, but it doesn't apply every default on this page. To add the rest, follow the Console tab in Step 4.