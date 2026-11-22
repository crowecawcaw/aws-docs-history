

# Ingress point use cases and recommendations

Create separate ingress endpoints when email flows have different sources, authentication requirements, accepted recipients, processing actions, destinations, or operational owners. For example, internet email can enter through a public open ingress endpoint, while an application sends through a separate authenticated ingress endpoint.

Each ingress endpoint references one traffic policy and one rule set. Multiple ingress endpoints can share either resource when their requirements are identical. Use separate resources when a change for one flow must not affect another flow.

## Choosing an ingress point type
<a name="eb-ingress-use-cases-choose-type"></a>

The following table maps common connection requirements to an ingress endpoint type.


| Connection requirement | Type | Network | Recommendation | 
| --- | --- | --- | --- | 
| Receive email from any internet SMTP sender | OPEN | Public | Use DENY as the traffic policy default. Allow only the required recipients, such as members of an Address List. | 
| Receive from an application or mail server that supports a password | AUTH | Public or private | Store the password in AWS Secrets Manager, require TLS, and use a separate ingress endpoint for each independently managed sender group. | 
| Receive from systems that use client certificates | MTLS | Public or private | Use separate client certificates, maintain CRLs, and rotate CAs with an overlap period. | 
| Receive only from workloads with private Amazon VPC connectivity | OPEN, AUTH, or MTLS | Private | Choose the authentication type independently from the network. Use AUTH or MTLS when the sender must also prove its identity. | 

## Receive internet email and relay it to hosted mailboxes
<a name="eb-ingress-use-case-inbound-gateway"></a>
+ **Source** – Internet senders delivering email for a domain such as `example.com`.
+ **Ingress point** – A public `OPEN` ingress endpoint used as the domain's MX destination. The endpoint is reachable by any internet SMTP sender.
+ **Traffic policy** – Use `DENY` as the default action. Allow only intended recipient domains or recipients in an Address List. Add sender IP, TLS, or Email Add On conditions when required.
+ **Rule set** – Archive or inspect the message, and then use an SMTP relay action to deliver it to the hosted mailbox provider.
+ **Recommendation** – Test accepted and rejected recipients with traffic-policy debug logs before changing the domain's MX record.

For a complete Google Workspace and Microsoft 365 walkthrough, see [AWS Messaging Blog: How to use SES Mail Manager SMTP Relay action to deliver inbound email to Google Workspace and Microsoft 365](https://aws.amazon.com/blogs/messaging-and-targeting/how-to-use-ses-mail-manager-smtp-relay-action-to-deliver-inbound-email-to-google-workspace-and-microsoft-365/).

## Send application or mail server email through a managed SMTP pipeline
<a name="eb-ingress-use-case-authenticated-smtp"></a>
+ **Source** – An application, Postfix server, appliance, or other system that supports SMTP authentication.
+ **Ingress point** – An `AUTH` ingress endpoint that uses an AWS Secrets Manager password. Use a private ingress endpoint when every client can reach the associated Amazon VPC endpoint.
+ **Traffic policy** – Use `DENY` as the default action. Allow approved recipient domains and require the needed TLS version. Set the maximum message size for the receiving systems.
+ **Rule set** – Archive the message, apply security checks, and then use the send-to-internet action.
+ **Recommendation** – Use separate ingress endpoints for sender groups with different credentials, destinations, or operational owners. Rotate each secret independently.

For a walkthrough in a Region without the classic SES SMTP endpoint, see [AWS Messaging Blog: Using Amazon Mail Manager SMTP to send email using Amazon Simple Email Service](https://aws.amazon.com/blogs/messaging-and-targeting/using-amazon-mail-manager-smtp-to-send-email-using-amazon-simple-email-service/).

For an outbound security, address-list, archive, and delivery example, see [AWS Messaging Blog: Streamlining outbound emails with Amazon SES Mail Manager](https://aws.amazon.com/blogs/messaging-and-targeting/streamlining-outbound-emails-with-amazon-ses-mail-manager/).

## Convert authenticated email to SMS
<a name="eb-ingress-use-case-email-to-sms"></a>
+ **Source** – Applications or users that send to an address such as `12065550100@sms.example.com`.
+ **Ingress point** – An `AUTH` ingress endpoint prevents an unauthenticated internet sender from submitting messages for conversion. Use private Amazon VPC connectivity when the source is an internal application.
+ **Traffic policy** – Allow only the email-to-SMS recipient domain and expected message size. Add stable sender IP ranges when available.
+ **Rule set** – Write the email to Amazon S3. An Amazon S3 event invokes Lambda, which extracts the destination number and submits the SMS message through AWS End User Messaging SMS.
+ **Recommendation** – Keep this flow on a separate ingress endpoint so its credentials, accepted address format, message-size limit, and rate controls do not apply to other mail.

For the complete architecture, see [AWS Messaging Blog: AT&T email-to-text service migration: AWS solution implementation](https://aws.amazon.com/blogs/messaging-and-targeting/att-email-to-text-service-migration-aws-solution-implementation/).

## Process documents submitted by email
<a name="eb-ingress-use-case-document-intake"></a>
+ **Source** – Customers or partner systems submitting invoices, contracts, or other documents to dedicated addresses.
+ **Ingress point** – Use `AUTH` when submitters can use managed credentials. Use public `OPEN` when arbitrary internet senders must submit documents, and restrict the accepted recipient addresses with the traffic policy.
+ **Traffic policy** – Use `DENY` as the default action. Allow only active intake addresses, preferably through an Address List, and set the maximum message size for expected attachments.
+ **Rule set** – Scan attachments, return a bounce response for rejected content, archive the message, and invoke Lambda for extraction and classification.
+ **Recommendation** – Give workflows with different data handling or storage requirements separate ingress endpoints and rule sets.

For a multi-tenant attachment pipeline using Lambda, Amazon S3, Amazon DynamoDB, and Amazon Bedrock, see [AWS Messaging Blog: Build an AI email pipeline with Amazon Bedrock and SES Mail Manager](https://aws.amazon.com/blogs/messaging-and-targeting/build-an-ai-email-pipeline-with-amazon-bedrock-and-ses-mail-manager/).

## Inspect and isolate suspicious email
<a name="eb-ingress-use-case-security-gateway"></a>
+ **Source** – Internet mail, partner mail, or outbound email that requires a security inspection point.
+ **Ingress point** – Use public `OPEN` for internet inbound mail. Use `AUTH` or `MTLS` when the upstream sender is controlled.
+ **Traffic policy** – Apply recipient, sender IP, TLS, address-list, and supported Email Add On conditions before the message enters rule processing.
+ **Rule set** – Evaluate security results, add classification headers, isolate suspicious email in Amazon S3, archive when required, and stop processing before delivery.
+ **Recommendation** – Test add-on results against representative legitimate and unwanted traffic before using them to reject mail.

For general security and efficiency patterns, see [AWS Messaging Blog: How Amazon SES Mail Manager Elevates Email Security and Efficiency](https://aws.amazon.com/blogs/messaging-and-targeting/how-amazon-ses-mail-manager-elevates-email-security-and-efficiency/).

For a Vade Advanced Email Security Add On walkthrough, see [AWS Messaging Blog: Improving email security with Amazon SES Mail Manager and Hornetsecurity's Vade Advanced Email Security Add On](https://aws.amazon.com/blogs/messaging-and-targeting/improving-email-security-with-amazon-ses-mail-manager-and-hornetsecuritys-vade-advanced-email-security-add-on/).

## Archive email in transit
<a name="eb-ingress-use-case-archiving"></a>
+ **Source** – Inbound or outbound email that must be retained before mailbox delivery.
+ **Ingress point** – Choose `OPEN`, `AUTH`, or `MTLS` from the source's connection and identity requirements. Use separate ingress endpoints when retention requirements differ by business flow.
+ **Traffic policy** – Accept only the traffic that must enter the archive and delivery workflow.
+ **Rule set** – Run the archive action before the relay or send-to-internet action when every delivered message must have an in-transit archive copy.
+ **Recommendation** – Use separate rule sets when retention periods, encryption keys, or delivery destinations differ.

For the reasons to archive during transit rather than at individual mailboxes, see [AWS Messaging Blog: Email Archiving with Mail Manager: Why To Archive In Transit vs At The Mailbox](https://aws.amazon.com/blogs/messaging-and-targeting/email-archiving-with-mail-manager-why-to-archive-in-transit-vs-at-the-mailbox/).

For the original routing and archiving overview, see [AWS Messaging Blog: Mail Manager – Amazon SES introduces new email routing and archiving features](https://aws.amazon.com/blogs/messaging-and-targeting/mail-manager-amazon-ses-introduces-new-email-routing-and-archiving-features/).

## Separate tenant or business-unit email flows
<a name="eb-ingress-use-case-tenant-isolation"></a>
+ **Source** – Legacy appliances, applications, printers, or mail servers owned by different tenants or business units.
+ **Ingress point** – Use one authenticated ingress endpoint per tenant when the sender-to-tenant mapping is static and separate credentials are acceptable. Use a shared ingress endpoint when rule logic or Lambda must resolve the tenant dynamically.
+ **Traffic policy** – Restrict each per-tenant ingress endpoint to its expected recipient domains, source networks, and message sizes.
+ **Rule set** – Add the applicable `X-SES-TENANT` header before sending the message. A shared flow can invoke Lambda when the tenant cannot be derived from static rule conditions.
+ **Recommendation** – Prefer separate ingress endpoints when tenants need independent credentials, policies, logs, or operational ownership. Prefer a shared ingress endpoint when the number of tenants or mapping frequency makes static endpoints difficult to maintain.

For a comparison of static per-tenant endpoints and dynamic shared-endpoint patterns, see [AWS Messaging Blog: Isolate email reputation in Amazon SES Mail Manager with tenant management](https://aws.amazon.com/blogs/messaging-and-targeting/isolate-email-reputation-in-amazon-ses-mail-manager-with-tenant-management/).

## Authenticate a partner with client certificates
<a name="eb-ingress-use-case-mtls-partner"></a>
+ **Source** – A partner mail server or internal system with a managed certificate lifecycle.
+ **Ingress point** – An `MTLS` ingress endpoint with a trust store containing the issuing CA.
+ **Traffic policy** – Combine expected sender IP ranges, recipients, and TLS version with certificate authentication.
+ **Rule set** – Use client certificate common name, serial number, or Subject Alternative Name conditions when different certificates require different processing.
+ **Recommendation** – Issue separate client certificates, keep CRLs current, monitor expiry fields, and rotate CAs with an overlap period.

For certificate generation, trust-store rotation, monitoring, and CLI examples, see [Mutual TLS ingress points](eb-ingress-mtls.md).

## Recommendations for multiple ingress points
<a name="eb-ingress-use-cases-recommendations"></a>
+ Create separate ingress endpoints for different trust boundaries. Do not use one public open ingress endpoint for internet mail and controlled application submission.
+ Create separate ingress endpoints when credentials, certificates, traffic policies, rule actions, destinations, logs, or operational owners differ.
+ Use `DENY` as the traffic policy default action and add explicit `ALLOW` statements for each flow.
+ Use an Address List for recipient sets that change more often than the traffic policy. For setup and update procedures, see [Address Lists](eb-addlist.md).
+ Reuse a traffic policy or rule set only when a change can safely affect every attached ingress endpoint.
+ Enable `TRAFFIC_POLICY_DEBUG_LOGS` before directing production traffic to a new ingress endpoint. Enable `APPLICATION_LOGS` to inspect accepted messages. For setup, see [Mail Manager logging](eb-logging.md).