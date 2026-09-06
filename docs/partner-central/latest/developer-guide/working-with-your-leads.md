

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Manage leads using the AWS Partner Central Selling API
<a name="working-with-your-leads"></a>

## What is a Lead?
<a name="what-is-a-lead"></a>

In business-to-business (B2B) sales, a lead represents a potential customer who has expressed interest in a company's products or services but has not yet been fully qualified as a sales opportunity. Leads are the initial stage of the sales pipeline and require nurturing and qualification before they can be converted into opportunities for active co-selling with AWS.

Leads shared by AWS with partners are based on customer engagement signals such as webinar attendance, campaign participation, or partner solution inquiries. These leads include valuable context like customer company information, business problems, and engagement details to help partners prioritize and qualify potential opportunities.

## Working with Lead Invitations
<a name="working-with-lead-invitations"></a>

Partners receive lead invitations from AWS when potential customers express interest in partner solutions or services. The lead invitation process allows partners to evaluate leads before committing to engagement, ensuring efficient resource allocation and higher conversion rates.

### Receiving Lead Invitations
<a name="receiving-lead-invitations"></a>

AWS creates lead invitations and shares them with partners through the Selling API. When a new lead invitation is available, AWS sends an Engagement Invitation with the Lead context to eligible partners.

Partners should monitor the `Engagement Invitation Created` event using Amazon EventBridge. This event notification includes the `payloadType` field set to `LeadInvitation`, allowing partners to distinguish lead invitations from opportunity invitations. Upon receiving the event, partners can retrieve invitation details to evaluate the lead.

### Listing Lead Invitations
<a name="listing-lead-invitations"></a>

Partners can view all their lead invitations using the `ListEngagementInvitations` API action. This action retrieves invitations where the calling principal is either a sender or receiver.

To filter specifically for lead invitations, partners should use the `payloadType` filter with the value `LeadInvitation`. This filter ensures that only lead invitations are returned, excluding opportunity invitations from the results.

Lead invitations can be in the following states:
+ **Pending**: Awaiting partner acceptance or rejection
+ **Accepted**: Partner has accepted the invitation and gained access to full lead details
+ **Rejected**: Partner has declined the invitation
+ **Expired**: Invitation has passed its expiration date without action

## Evaluating Lead Invitations
<a name="evaluating-lead-invitations"></a>

Before accepting a lead invitation, partners should retrieve detailed invitation information using the `GetEngagementInvitation` API action. This provides essential context for making informed accept or reject decisions.

The lead invitation payload includes:

**Customer Information (available pre-acceptance):**
+ Company name, industry, and country
+ Website URL
+ Market segment (Enterprise, Large, Medium, Small, Micro)
+ AWS maturity level (Evaluating, Single-Account, Multi-Account)

**Customer Interactions:**
+ Source type and campaign information
+ Customer action taken (form completion, webinar attendance, etc.)
+ Business problem description provided by the customer
+ Use case category
+ Contact title (provides Authority context for BANT qualification)

**Important**  
Customer contact information (name, email, phone number) is not visible at the invitation stage. Contact details become available only after accepting the invitation, ensuring customer privacy and preventing lead farming behavior.

## Accepting Lead Invitations
<a name="accepting-lead-invitations"></a>

When a partner decides to pursue a lead, they must accept the invitation using the `AcceptEngagementInvitation` API action. This action adds the partner to the engagement and grants access to full lead details, including customer contact information.

After acceptance:
+ The partner is added as a member of the engagement
+ Customer contact information becomes visible through the engagement Lead context
+ The lead is classified as a Partner Qualified Lead (PQL) in AWS systems
+ The lead appears in the partner's active leads list
+ Partners can begin nurturing the lead and establishing customer contact

Partners can accept multiple lead invitations programmatically by calling `AcceptEngagementInvitation` for each invitation, enabling efficient bulk processing of high-quality leads.

## Rejecting Lead Invitations
<a name="rejecting-lead-invitations"></a>

If a lead does not align with the partner's capabilities, capacity, or business focus, partners can decline the invitation using the `RejectEngagementInvitation` API action. When rejecting a lead invitation, partners should provide a rejection reason to help AWS improve lead routing and matching. Common rejection reasons include:
+ Lack of geographic coverage
+ Insufficient technical expertise for the use case
+ Current capacity constraints
+ Customer industry mismatch
+ Budget misalignment

After rejection:
+ The lead is removed from the partner's pending invitations queue
+ Customer contact information is never shared with the partner
+ The lead is classified as a Partner Rejected Lead (PRL) in AWS systems
+ The invitation remains visible in the partner's rejected invitations list for reference

Rejected leads may be eligible for reassignment to other partners, provided customer consent requirements are met.

## Managing Accepted Leads
<a name="managing-accepted-leads"></a>

After accepting a lead invitation, partners can access complete lead information, nurture customer relationships, and track the lead through qualification stages.

### Viewing Lead Details
<a name="viewing-lead-details"></a>

Partners access full lead details using the `GetEngagement` API action. The engagement contains a Lead context with comprehensive information about the customer and their interactions with AWS.

The Lead context includes:

**Complete Customer Profile:**
+ All company information from the original invitation
+ Full contact details for all customer interactions (name, email, phone, business title)
+ AWS maturity level and market segment

**Interaction History:**
+ Multiple customer touch-points consolidated into a single engagement
+ Each interaction includes source information, customer action, business problem, and contact details
+ Interactions are listed chronologically to provide a complete customer journey view

**Qualification Status:**
+ Current state of lead qualification (Unqualified, Qualified, Disqualified, or custom status)
+ Partners can update this status as they progress through their qualification process

This comprehensive view enables partners to understand the customer's complete engagement history across multiple AWS campaigns and touchpoints, rather than treating each interaction as a separate lead.

### Listing Active Leads
<a name="listing-active-leads"></a>

Partners can retrieve all their active leads using the `ListEngagements` API action with the `contextType` filter set to `Lead`. This returns engagements where the partner is a member and the engagement contains a Lead context.

The list response includes key information such as:
+ Engagement ID and title
+ Customer company name
+ Current engagement score
+ Qualification status
+ Number of interactions
+ Creation and modification timestamps

Partners can use this list to build dashboards, track lead pipeline health, and identify leads requiring attention.

### Enriching Leads with Prospecting Insights
<a name="prospecting-leads"></a>

Partners can enrich accepted leads with AWS insights to better prioritize and qualify them before investing in outreach. Enrichment is performed asynchronously through prospecting tasks, which augment a lead engagement with AWS-derived signals to support qualification decisions.

**Starting a prospecting task**

Partners initiate enrichment using the `StartProspectingFromEngagementTask` API action. This action accepts up to 100 engagement identifiers in a single request, allowing partners to enrich leads in batches. The task runs asynchronously and immediately returns a `TaskId` and `TaskArn` that partners use to track progress. The initial `TaskStatus` is one of `PENDING`, `IN_PROGRESS`, `COMPLETED`, or `FAILED`.

Partners can optionally provide a `TaskName` to label the task and a `ClientToken` to ensure idempotency across retries.

**Polling for results**

Because prospecting is asynchronous, partners poll for completion using the `GetProspectingFromEngagementTask` API action with the `TaskId` returned at start. The response reports the overall task status and a per-engagement result for each identifier submitted.

Each engagement is processed independently, so individual engagements can succeed or fail without affecting the others in the same task. For each engagement, the result includes:
+ **Engagement identifier**: The engagement that was processed.
+ **Status**: `PENDING`, `IN_PROGRESS`, `COMPLETED`, or `FAILED`.
+ **Prospecting context identifier**: Populated when the engagement is processed successfully. This identifier references the enriched prospecting context added to the engagement and can be used in subsequent operations.
+ **Reason code and message**: Populated only when an engagement fails, providing an enumerated failure code and a human-readable description with suggested recovery steps.

**Monitoring multiple tasks**

To track enrichment across many leads, partners use the `ListProspectingFromEngagementTasks` API action. This action lists all prospecting tasks initiated by the caller's account and supports optional filters by task identifier, task name, or start time range, with configurable sorting. The response is paginated; use the `NextToken` value from each response to retrieve subsequent pages.

When enrichment completes successfully, the AWS insights are added to the engagement as a prospecting context. Partners can retrieve the enriched details with `GetEngagement` and use them to set the lead's qualification status and decide which leads to advance toward conversion.

### Updating Lead Information
<a name="updating-lead-information"></a>

As partners nurture leads and gather additional information, they can update lead details using the `UpdateEngagementContext` API action. This action allows partners to modify the Lead context within the engagement.

Partners can update:

**Qualification Status:** Partners should update the qualification status as they progress through their internal qualification process:
+ **Unqualified**: Default status after accepting a lead; indicates the lead requires evaluation
+ **Qualified**: Lead meets qualification criteria and shows high potential for conversion to an opportunity
+ **Disqualified**: Lead does not meet criteria or is not a good fit for the partner's solutions
+ **Custom States**: Partners can define their own qualification states to match their internal processes

**Lead Metadata:** Partners can add or update additional information relevant to their qualification and nurturing processes.

Updating qualification status helps partners track lead progression, generate accurate pipeline reports, and identify leads ready for conversion to opportunities.

### Monitoring AWS Updates
<a name="monitoring-aws-updates"></a>

AWS may update lead information based on new customer engagement signals or refined engagement scoring. When AWS updates the engagement, partners receive an `Engagement Updated` event via Amazon EventBridge.

These updates may include:
+ Refined engagement scores based on new customer activity
+ Additional customer interactions from new campaigns or touch-points
+ Updated customer information

Partners should monitor these events and call `GetEngagement` to retrieve the latest lead details. This ensures partners have the most current information for prioritizing and nurturing leads.

The `Engagement Updated` event includes the `contextTypes` field, allowing partners to filter specifically for leads (engagements with Lead context).

## Converting a Lead to an Opportunity
<a name="converting-lead-to-opportunity"></a>

When a lead has been qualified and demonstrates serious buying intent, partners can convert it into an opportunity for formal co-selling collaboration with AWS. This conversion marks the transition from lead nurturing (primarily partner-driven) to opportunity management (collaborative with AWS).

### Recommended Approach: Convenience API
<a name="recommended-approach-convenience-api"></a>

Partners can streamline the opportunity creation and linking process by using the `StartOpportunityFromEngagementTask` convenience API action. This task API orchestrates multiple actions automatically:

1. Creates a draft opportunity with preliminary information from the lead context

1. Links the opportunity to the source engagement via resource snapshot

1. Adds the CustomerProject context to the engagement

This convenience method reduces the number of API calls required and ensures proper attribution tracking. Partners using this approach still need to:
+ Complete opportunity details using `UpdateOpportunity`
+ Associate Partner Solutions using `AssociateOpportunity`
+ Submit the opportunity using `StartEngagementFromOpportunityTask` when ready

The convenience API is particularly useful for partners with automated lead-to-opportunity workflows who want to minimize integration complexity.

### Alternative Approach: Step-by-step API
<a name="alternative-approach-step-by-step"></a>

**Creating a Draft Opportunity**

The first step in converting a lead is creating a draft opportunity using the `CreateOpportunity` API action. This creates an opportunity with the `Lifecycle.ReviewStatus` set to `Pending Submission`. At this stage, the opportunity is not yet submitted to AWS for validation.

Partners should populate the opportunity with information gathered during lead nurturing, including:
+ Customer account details
+ Project information and business problem
+ Expected customer spend
+ Target close date
+ Any other relevant details collected during qualification

The draft opportunity allows partners to prepare complete information before submitting to AWS, ensuring higher approval rates and faster validation.

**Linking Opportunity to Lead Engagement**

After creating the draft opportunity, partners must link it to the source lead engagement using the `CreateResourceSnapshot` API action. This step is critical for:
+ **Attribution Tracking**: Establishes the provenance chain from lead invitation through opportunity closure, enabling accurate ROI calculation for marketing campaigns and lead sources.
+ **Conversion Metrics**: Allows AWS and partners to measure lead-to-opportunity conversion rates and identify successful lead sources.
+ **Context Preservation**: Maintains the complete customer journey history, including all original interactions and engagement signals.

When creating the resource snapshot, partners specify:
+ The engagement ID (source lead engagement)
+ The opportunity identifier
+ The resource type (Opportunity)

This action automatically adds a CustomerProject context to the engagement, signaling that the lead has been converted to an active opportunity. The engagement now contains both the original Lead context (preserving history) and the new CustomerProject context (indicating active opportunity).

**Completing Opportunity Details**

Once the opportunity is created and linked, partners must complete additional opportunity requirements before submission. See the `AssociateOpportunity` API action for details.

Updating Project Details: Partners can use the `UpdateOpportunity` API action to refine project information, customer business problems, expected spend, and other relevant details gathered during lead qualification.

**Submitting the Opportunity**

Once all required information is complete, partners submit the opportunity for AWS validation using the `StartEngagementFromOpportunityTask` convenience API. This transitions the opportunity from draft status to the AWS review process.

Validation Requirement: The engagement must have a CustomerProject context before submission. This context is automatically created when using `CreateResourceSnapshot` to link the opportunity to the engagement. If this context is missing, the submission will fail.

After submission:
+ The opportunity's `Lifecycle.ReviewStatus` changes to `Submitted`
+ The lead is classified as a Partner Sales Qualified Lead (PSQL) in AWS systems
+ AWS begins validation to ensure opportunity details are accurate and complete
+ No changes can be made to the opportunity until the review process is complete

The opportunity then follows the standard validation workflow described in the "Working with your opportunities" documentation, progressing through states such as In-Review, Action Required, Approved, or Disqualified.