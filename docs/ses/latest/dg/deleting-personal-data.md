# Deleting personal data from Amazon SES

Depending on how you use it, Amazon SES might store certain data that could be considered
personal. For example, in order to send email using Amazon SES, you must provide at least one
verified identity (an email address or a domain). You can use the Amazon SES console or the Amazon SES
API to permanently delete this personal data.

This chapter provides procedures for deleting various types of data that might be
considered personal.

###### Contents

- [Delete Email Addresses
  From the Account-Level Suppression List](#deleting-personal-data-account-suppression-list "#deleting-personal-data-account-suppression-list")
- [Delete Data About Email Sent Using
  Amazon SES](#deleting-personal-data-message-data "#deleting-personal-data-message-data")
- [Delete Data About Identities](#deleting-personal-data-identities "#deleting-personal-data-identities")
- [Delete Sender Authentication
  Data](#deleting-personal-data-sender-authentication "#deleting-personal-data-sender-authentication")
- [Delete Data Related to
  Receiving Rules](#deleting-personal-data-receiving-rules "#deleting-personal-data-receiving-rules")
- [Delete Data Related to IP
  Address Filters](#deleting-personal-data-ip-address-filters "#deleting-personal-data-ip-address-filters")
- [Delete Data in Email
  Templates](#deleting-personal-data-email-templates "#deleting-personal-data-email-templates")
- [Delete Data in Custom
  Verification Email Templates](#deleting-personal-data-cve-templates "#deleting-personal-data-cve-templates")
- [Delete All Personal Data by
  Closing Your AWS Account](#deleting-personal-data-closing-account "#deleting-personal-data-closing-account")

## Delete Email Addresses

From the Account-Level Suppression List

Amazon SES includes an optional account-level suppression list. When you enable this
feature, email addresses are automatically added to a suppression list when they result
in a bounce or complaint. Email addresses remain on this list until you delete them. For
more information about the account-level suppression list, see [Using the Amazon SES account-level suppression
list](sending-email-suppression-list.md "sending-email-suppression-list.md").

You can remove email addresses from the account-level suppression list by using the
`DeleteSuppressedDestination` operation in the [Amazon SES API v2](../APIReference-V2/API_DeleteSuppressedDestination.md "../APIReference-V2/API_DeleteSuppressedDestination.md"). This section includes a procedure for deleting email
addresses by using the AWS CLI. For more information about installing and configuring the
AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### To remove an address from the account-level suppression list by using the

AWS CLI

- At the command line, enter the following command:

```
aws sesv2 delete-suppressed-destination --email-address `recipient@example.com`
```

In the preceding command, replace
`recipient@example.com` with the email address that
you want to remove from the account-level suppression list.

## Delete Data About Email Sent Using

Amazon SES

When you use Amazon SES to send an email, you can send information about that email to
other AWS services. For example, you can send information about email events (such as
deliveries, opens, and clicks) to Firehose. This event data typically contains your email
address and the IP address the email was sent from. It also contains the email addresses
of all the recipients the email was sent to.

You can use Firehose to stream email event data to several destinations—including
Amazon Simple Storage Service, Amazon OpenSearch Service, and Amazon Redshift. To remove this data, you should first stop streaming data
to Firehose, and then delete the data that has already been streamed. To stop streaming
Amazon SES event data to Firehose, you must delete the Firehose event destination.

###### To remove a Firehose event destination by using the Amazon SES console

1. Open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. Under **Email Sending**, choose **Configuration
   Sets**.
3. In the list of configuration sets, choose the configuration set that contains
   the Firehose event destination.
4. Next to the Firehose event destination that you want to delete, choose the
   **delete** (
   ![Close or cancel icon represented by an X symbol in a circular shape.](images/delete_icon.png)
   ) button.
5. If necessary, remove the data that Firehose wrote to other services. For more
   information, see [Remove Stored Event
   Data](#deleting-personal-data-message-data-storage "#deleting-personal-data-message-data-storage").

You can also use the Amazon SES API to delete event destinations. The following procedure
uses the AWS Command Line Interface (AWS CLI) to interact with the Amazon SES API. You can also interact with
the API by using an AWS SDK, or by making HTTP requests directly.

###### To remove a Firehose event destination by using the AWS CLI

1. At the command line, type the following command:

```
aws sesv2 delete-configuration-set-event-destination --configuration-set-name `configSet` \
--event-destination-name `eventDestination`
```

In this command, replace `configSet` with the name of
the configuration set that contains the Firehose event destination. Replace
`eventDestination` with the name of the Firehose event
destination. 2. If necessary, remove the data that Firehose wrote to other services. For more
information, see [Remove Stored Event
Data](#deleting-personal-data-message-data-storage "#deleting-personal-data-message-data-storage").

### Remove Stored Event

Data

For more information about deleting information from other AWS services, see the
following documents:

- [Delete an Object
  and Bucket](../../../AmazonS3/latest/userguide/DeletingAnObjectandBucket.md "../../../AmazonS3/latest/userguide/DeletingAnObjectandBucket.md") in the _Amazon Simple Storage Service User Guide_
- [Delete an OpenSearch Service
  Domain](../../../opensearch-service/latest/developerguide/es-gsg-deleting.md "../../../opensearch-service/latest/developerguide/es-gsg-deleting.md") in the _Amazon OpenSearch Service Developer
  Guide_
- [Deleting a Cluster](../../../redshift/latest/mgmt/managing-clusters-console.md#delete-cluster "../../../redshift/latest/mgmt/managing-clusters-console.md#delete-cluster") in the _Amazon Redshift Cluster Management
  Guide_

You can also use Firehose to stream email data to Splunk, a
third-party service that isn't supported by AWS or managed in the AWS Management Console. For
more information about removing data from Splunk, consult your system administrator
or the documentation on the [Splunk
website](http://docs.splunk.com/Documentation "http://docs.splunk.com/Documentation").

## Delete Data About Identities

Identities include the email addresses and domains that you use to send email using
Amazon SES. In some jurisdictions, email addresses or domains might be considered personally
identifiable data.

###### To delete an identity by using the Amazon SES console

1. Open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. Under **Identity Management**, do one of the
   following:
   - Choose **Domains** if you want to delete a
     domain.
   - Choose **Email Addresses** if you want to delete an
     email address.

3. Choose the identity that you want to delete, and then choose
   **Remove**.
4. On the confirmation dialog box, choose **Yes, Delete
   Identity**.

You can also use the Amazon SES API to delete identities. The following procedure uses the
AWS Command Line Interface (AWS CLI) to interact with the Amazon SES API. You can also interact with the API by
using an AWS SDK, or by making HTTP requests directly.

###### To delete an identity by using the AWS CLI

- At the command line, type the following command:

```
aws ses delete-identity --identity `sender@example.com`
```

In this command, replace `sender@example.com` with
the identity that you want to delete.

## Delete Sender Authentication

Data

Sender authentication refers to the process of configuring Amazon SES so that another user
can send email on your behalf. To enable sender authorization, you must create a policy,
as described in [Using sending authorization with Amazon SES](sending-authorization.md "sending-authorization.md"). These policies contain identities (which
belong to you), in addition to AWS IDs (which are associated with the person or group
that sends email on your behalf). You can remove this personal data by modifying or
deleting the sender authentication policies. The following procedures show you how to
delete these policies.

###### To delete a sender authentication policy by using the Amazon SES console

1. Open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. Under **Identity Management**, do one of the
   following:
   - Choose **Domains** if the sender authentication
     policy you want to delete is associated with a domain.
   - Choose **Email Addresses** if the sender
     authentication policy you want to delete is associated with an email
     address.

3. Under **Identity Policies**, choose the policy you want to
   delete, and then choose **Remove Policy**.

You can also use the Amazon SES API to delete sender authentication policies. The following
procedure uses the AWS Command Line Interface (AWS CLI) to interact with the Amazon SES API. You can also
interact with the API by using an AWS SDK, or by making HTTP requests directly.

###### To delete a sender authentication policy by using the AWS CLI

- At the command line, type the following command:

```
aws ses delete-identity-policy --identity `example.com` --policy-name `samplePolicy`
```

In this command, replace `example.com` with the
identity that contains the sender authentication policy. Replace
`samplePolicy` with the name of the sender
authentication policy.

## Delete Data Related to

Receiving Rules

If you use Amazon SES to receive incoming email, you can create receipt rules that are
applied to one or more identities (email addresses or domains). These rules determine
what Amazon SES does with incoming mail sent to the specified identities.

###### To delete a receipt rule by using the Amazon SES console

1. Open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. Under **Email Receiving**, choose **Rule
   Sets**.
3. If the receipt rule is part of the active rule set, choose **View
   Active Rule Set**. Otherwise, choose the rule set that contains the
   receipt rule that you want to delete.
4. In the list of receipt rules, choose the rule that you want to delete.
5. On the **Actions** menu, choose
   **Delete**.
6. On the confirmation dialog box, choose **Delete**.

You can also use the Amazon SES API to delete receipt rules. The following procedure uses
the AWS Command Line Interface (AWS CLI) to interact with the Amazon SES API. You can also interact with the API
by using an AWS SDK, or by making HTTP requests directly.

###### To delete a receipt rule by using the AWS CLI

- At the command line, type the following command:

```
aws ses delete-receipt-rule --rule-set `myRuleSet` --rule-name `myReceiptRule`
```

In this command, replace `myRuleSet` with the name of
the receipt rule set that contains the receipt rule. Replace
`myReceiptRule` with the name of the receipt rule
that you want to delete.

## Delete Data Related to IP

Address Filters

If you use Amazon SES to receive incoming email, you can create filters to explicitly
accept or block messages that are sent from specific IP addresses.

###### To delete an IP address filter by using the Amazon SES console

1. Open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. Under **Email Receiving**, choose **IP Address
   Filters**.
3. In the list of IP address filters, choose the filter that you want to remove,
   and then choose **Delete**.

You can also use the Amazon SES API to delete IP address filters. The following procedure
uses the AWS Command Line Interface (AWS CLI) to interact with the Amazon SES API. You can also interact with
the API by using an AWS SDK, or by making HTTP requests directly.

###### To delete an IP address filter by using the AWS CLI

- At the command line, type the following command:

```
aws ses delete-receipt-filter --filter-name `IPfilter`
```

In this command, replace `IPfilter` with the name of
the IP address filter you want to delete.

## Delete Data in Email

Templates

If you use email templates for sending email, it's possible that those templates might
contain personal data, depending on how you configured them. For example, you might have
added an email address to the template that recipients could contact for more
information.

You can only delete email templates by using the Amazon SES API.

###### To delete an email template by using the AWS CLI

- At the command line, type the following command:

```
aws ses delete-template --template-name `sampleTemplate`
```

In this command, replace `sampleTemplate` with the
name of the email template that you want to delete.

## Delete Data in Custom

Verification Email Templates

If you use customized templates for verifying new email sending addresses, it's
possible that those templates might contain personal data, depending on how you
configured them. For example, you might have added an email address to the verification
email template that recipients could contact for more information.

You can only delete custom verification email templates by using the Amazon SES API.

###### To delete a custom verification email template by using the AWS CLI

- At the command line, type the following command:

```
aws ses delete-custom-verification-email-template --template-name `verificationEmailTemplate`
```

In this command, replace `verificationEmailTemplate`
with the name of the custom verification email template that you want to
delete.

## Delete All Personal Data by

Closing Your AWS Account

It's also possible to delete all personal data that's stored in Amazon SES by closing your
AWS account. However, this action also deletes all other data—personal or
non-personal—that you have stored in every other AWS service.

When you close your AWS account, the data in your AWS account is retained for 90
days. After that retention period, it's deleted permanently and irreversibly.

###### To close your AWS account

Complete instructions on how to close your AWS account is covered in [Close
an AWS account](../../../accounts/latest/reference/manage-acct-closing.md "../../../accounts/latest/reference/manage-acct-closing.md").
