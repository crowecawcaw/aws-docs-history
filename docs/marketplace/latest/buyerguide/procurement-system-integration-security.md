

# Security for procurement system integration

Three things make up the security of this integration: the ways you can stop purchases reaching your procurement system, the credential the two systems share, and the record of what you and your approvers have done.

## Stopping approvals from reaching your procurement system
<a name="procurement-system-security-blocking"></a>

There are three ways to cut the route, and they differ in how much of your purchasing they affect.

Change or remove the rule  
Affects only the purchases that rule matched. Purchases that no longer match a rule complete without approval, and purchases that match a changed rule go wherever you send them instead. Buyers already waiting for approval continue unaffected. This is usually the option you want.

Disable the connection  
Affects every purchase that connection carried, and you can reverse it. The approval requirement itself remains: purchases still need approval, and AWS Marketplace tells the buyer that it can't be delivered. For more information about turning off the integration, see [Turning off a procurement system integration](procurement-integration-disabling.md).

Remove the permissions your buyers rely on  
Affects all purchasing, not just routing. Purchasing through this integration needs `aws-marketplace:Subscribe`, `aws-marketplace:StartAgreementApprovals`, and `aws-marketplace:AcceptAgreementRequest`. Without them your buyers can't make purchases at all, so choose this to stop purchasing rather than to change where approvals go.

For the permissions involved, see [Permissions](procurement-system-prerequisites.md#procurement-system-prerequisites-permissions).

## Keeping your shared secret current
<a name="procurement-system-security-shared-secret"></a>

A Coupa connection authenticates with a shared secret that you choose, and both systems hold a copy of it. AWS doesn't rotate it for you, so keeping it current is your responsibility: rotate it on whatever schedule your own security policy sets, and rotate it whenever someone who knew it no longer needs it.

Change it in both places as one piece of work, because the punchout stops working for as long as the two sides disagree. Update the **Shared secret** on the connection, update the matching credential on your Coupa punchout site, and then confirm with a test punchout that your buyers can still reach the catalog. For how to test, see [Testing your procurement system integration](procurement-system-testing.md).

An SAP Ariba integration has no shared secret. It is identified by the buyer and supplier network IDs, and its punchout endpoint is managed on the AWS supplier account in the Ariba Network.

## Finding the CloudTrail records
<a name="buyer-cloudtrail-where-to-look"></a>

AWS Marketplace is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Marketplace. CloudTrail captures API calls for AWS Marketplace as events. The calls captured include calls from the AWS Marketplace website, the AWS Marketplace console, and code calls to the AWS Marketplace API operations. CloudTrail is enabled on your AWS account when you create the account, and you can view the most recent events in the CloudTrail console under **Event history**. For an ongoing record, create a trail, which delivers log files to an Amazon S3 bucket.

Three different parts of AWS carry out the actions involved in a procurement system integration. Each one records them under its own event source. Knowing which source holds what you want saves a good deal of searching.


| What you're looking for | Event source | 
| --- | --- | 
| What you configured: policies, approval rules, approvers, and the connection to your procurement system | marketplacecatalog.amazonaws.com | 
| What a buyer requested, and what each approver decided | agreement-marketplace.amazonaws.com | 
| The connection itself, and electronic invoice delivery | invoicing.amazonaws.com | 

## Configuration CloudTrail events
<a name="buyer-cloudtrail-admin-events"></a>

You configure your policies, rules, approvers, and the connection to your procurement system in Private Marketplace. Those actions are carried out by the AWS Marketplace Catalog API, whether you make them in the console or call the API yourself.

The Catalog API groups one or more changes into a *change set* and runs it with the `StartChangeSet` operation. So the event name you see in CloudTrail is `StartChangeSet`, and the *change types* inside the request tell you what was changed. These CloudTrail events use `marketplacecatalog.amazonaws.com` as the event source.


| Change type | Definition | 
| --- | --- | 
| CreateExperience | Logs the creation of a Private Marketplace experience. | 
| UpdateExperience | Logs an experience being enabled or disabled. | 
| CreateProcurementPolicy | Logs the creation of a policy. A policy has a type, and your approval rules are held in a policy of the approval type, separate from the policy that holds your product rules. | 
| UpdateProcurementPolicy | Logs a change to the contents of a policy. For an approval policy, this is the event that records a change to which purchases need approval, and to where that approval comes from. | 
| AssociateAudience | Logs accounts, organizational units, or your whole organization being added to the accounts an experience applies to. This is part of the record of which accounts your rules govern. | 
| DisassociateAudience | Logs accounts, organizational units, or your whole organization being removed from the accounts an experience applies to. | 
| CreateTrustedActor | Logs the creation of an approver. In the Catalog API, approvers are called trusted actors, and the term covers all three kinds: the connection to your procurement system, an email approver, and an approver who decides in the console. | 
| UpdateTrustedActor | Logs a change to an approver, including an approver being disabled or enabled. | 
| CreateApprovalWorkflow | Logs the creation of a workflow, which is what connects a rule to the approver that acts on it. | 
| RestrictExperience | Logs an experience being archived. | 
| ReviveExperience | Logs an archived experience being reactivated. | 

Change sets are also listed on the **Track changes** page in the AWS Marketplace console, which is easier to read than a log file and shows whether each change succeeded or failed. That page keeps change sets for 90 days, so CloudTrail is the record that lasts. For more information about tracking changes, see [Viewing changes](view-changes.md).

## Purchase and approval CloudTrail events
<a name="buyer-cloudtrail-approval-events"></a>

What a buyer asked for, and what each approver decided, is recorded by the AWS Marketplace Agreements API. These CloudTrail events use `agreement-marketplace.amazonaws.com` as the event source.


| Event name | Definition | 
| --- | --- | 
| CreateAgreementRequest | Logs a buyer submitting a purchase. | 
| GetAgreementRequest | Logs the retrieval of a single submitted purchase. | 
| ListAgreementRequests | Logs the retrieval of a list of submitted purchases. | 
| StartAgreementApprovals | Logs the purchase being evaluated against your rules and the approvals it needs being raised. | 
| GetAgreementRequestApprovalPlans | Logs the retrieval of which approvals a purchase needs, and in what order. | 
| ListAgreementApprovals | Logs the retrieval of the list of approvals available to a buyer or an approver. | 
| GetAgreementApproval | Logs the retrieval of a single approval. | 
| AcceptAgreementApproval | Logs an approver agreeing to a purchase. A management account override is recorded as this event too. | 
| RejectAgreementApproval | Logs an approver declining a purchase. | 
| AcceptAgreementRequest | Logs the purchase completing after every approval it needed was given. | 
| CancelAgreementRequest | Logs a buyer cancelling a submitted purchase. | 
| DescribeAgreement | Logs an agreement being viewed. | 
| GetAgreementTerms | Logs the terms of an agreement being viewed. | 
| SearchAgreements | Logs a search for agreements. | 

**Important**  
CloudTrail records an override as an `AcceptAgreementApproval` event, the same event as an ordinary approval. Two things in the event tell the two apart. The request carries an override parameter naming the approver whose decision was overridden, and the event carries the identity of whoever performed it. So an override is found by looking for that parameter, and attributed by the identity.  
For more information about overrides, see [Overriding an approval](procurement-system-supported-scenarios.md#procurement-system-scenarios-override).

## Invoicing CloudTrail events
<a name="buyer-cloudtrail-invoicing-events"></a>

Invoicing records each connection you create and change, including the electronic invoice delivery settings you add to it. In these events a connection appears under the name invoicing uses for it, `ProcurementPortalPreference`. These CloudTrail events use `invoicing.amazonaws.com` as the event source.


| Event name | Definition | 
| --- | --- | 
| CreateProcurementPortalPreference | Logs the creation of a procurement portal preference. | 
| PutProcurementPortalPreference | Logs a change to a procurement portal preference. | 
| GetProcurementPortalPreference | Logs the retrieval of a procurement portal preference. | 
| ListProcurementPortalPreferences | Logs the retrieval and listing of procurement portal preferences. | 
| ListProcurementPortals | Logs the retrieval and listing of the procurement systems you can connect to. | 
| ListProcurementPortalSuppliers | Logs the retrieval and listing of the AWS suppliers available for a procurement system. | 

## More information about AWS CloudTrail
<a name="buyer-cloudtrail-info"></a>
+ [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/)
+ [Viewing events with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html)