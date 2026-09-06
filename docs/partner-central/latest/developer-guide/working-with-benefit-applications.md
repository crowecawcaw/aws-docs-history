

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with Benefit Applications
<a name="working-with-benefit-applications"></a>

A Benefit Application models a partner's request for a specific benefit. It captures all information needed to evaluate and process the request according to benefit-specific conditions. The benefit application lifecycle progresses through multiple states from draft creation to final approval or rejection.

## Creating Benefit Applications
<a name="creating-benefit-applications"></a>

Partners initiate the benefit request process by creating a benefit application using the `CreateBenefitApplication` API action. At creation, the application enters `PENDING_SUBMISSION` status, allowing partners to prepare complete information before submitting for review.

When creating a benefit application, partners must provide:
+ **Benefit Identifier** - The ID or ARN of the benefit being requested
+ **Fulfillment Types** - How the partner expects to receive the benefit (`CREDITS`, `CASH`, `DISCOUNT`, `ACCESS`, `RECOGNITION`, or `RESOURCE`)
+ **Benefit Application Details** - A JSON document containing benefit-specific information as defined by the benefit's request schema
+ **Client Token** - A unique idempotency token to prevent duplicate submissions

Partners can optionally provide:
+ **Name and Description** - Human-readable identifiers for the application
+ **Partner Contacts** - Contact information for the person managing this benefit request (maximum 1 contact)
+ **File Attachments** - Supporting documentation such as project plans, SOWs, proof of cost, or customer satisfaction surveys (maximum 10 files)
+ **Associated Resources** - Links to related opportunities or existing benefit allocations (maximum 10 resources)
+ **Tags** - Key-value pairs for resource organization and tracking (maximum 200 tags)

The `CreateBenefitApplication` API performs soft validation, checking only basic field types and patterns. Full business logic validation occurs during submission, allowing partners to save incomplete applications and return later to complete them.

**Best Practice:** Partners should use the benefit request schema from `GetBenefit` to understand exactly what information is required before creating an application. This reduces the likelihood of submission failures due to missing or invalid data.

## Updating Benefit Applications
<a name="updating-benefit-applications"></a>

Partners can modify draft benefit applications using the `UpdateBenefitApplication` API action. This allows partners to refine information, add documentation, or correct errors before submission.

When updating a benefit application, partners must provide:
+ **Identifier** - The ID or ARN of the benefit application to update
+ **Revision** - The current revision number for optimistic locking
+ **Benefit Application Details** - The complete, updated JSON document

Partners must submit the complete benefit application object, even if only specific fields are changing. The best practice is to first retrieve the latest application details using `GetBenefitApplication`, modify the necessary fields, then submit the full updated payload to `UpdateBenefitApplication`.

**Optimistic Locking:** The revision field ensures that updates are applied only if the application hasn't changed since it was last retrieved. If the revision doesn't match the current database value, the update is rejected with a conflict error. This prevents partners from accidentally overwriting changes made by other processes or systems.

Updates can only be performed while the application is in `PENDING_SUBMISSION` status. Once submitted, applications enter the review process and can no longer be updated through this API.

## Associating Resources with Benefit Applications
<a name="associating-resources-with-benefit-applications"></a>

Partners can link benefit applications to related resources using the `AssociateBenefitApplicationResource` API action. This creates valuable connections between benefits and the business context in which they're being used.

Supported resource types include:
+ **OPPORTUNITY** - Link the benefit application to a specific customer opportunity in . This is particularly useful for opportunity-specific benefits like MAP funding or POC credits tied to customer engagements.
+ **BENEFIT\_ALLOCATION** - Link to existing benefit allocations, enabling partners to chain benefits or demonstrate how previous benefits are being leveraged

Resource association can only occur before submission. Once a benefit application is submitted (status changes to `IN_REVIEW`), no further associations are allowed. Partners can associate up to 10 resources with each benefit application.

To disassociate a resource, partners use the `DisassociateBenefitApplicationResource` API action. Like association, disassociation can only occur in `PENDING_SUBMISSION` status.

**Important**  
Partners must have appropriate permissions to both access the benefit application and read the specific resource being associated. The API validates these permissions during the association operation.

## Submitting Benefit Applications
<a name="submitting-benefit-applications"></a>

When a benefit application is complete and ready for AWS review, partners submit it using the `SubmitBenefitApplication` API action. Submission triggers a state transition from `PENDING_SUBMISSION` to `IN_REVIEW` and initiates the benefit-specific approval workflow.

Upon submission, the API performs comprehensive validation including:
+ **Required fields validation** - Ensures all mandatory fields in the benefit application details are present
+ **Field format validation** - Verifies that field values match expected patterns and data types
+ **Business rule validation** - Applies benefit-specific business logic and constraints
+ **Resource validation** - Confirms that all associated resources are valid and accessible
+ **File validation** - Verifies that all file attachments have completed processing successfully

If validation fails, the API returns a ValidationException with detailed error codes and messages indicating which fields require correction. Partners must address these issues using `UpdateBenefitApplication` before attempting submission again.

**File Processing Requirement:** Benefit applications cannot be submitted if any attached files are still in `PENDING` status. Partners must wait for file processing to complete (status changes to `SUCCEEDED`) before submitting. If files fail processing (status `FAILED`), partners should upload corrected versions.

After successful submission:
+ The application status changes to `IN_REVIEW`
+ The benefit owner's team is notified of the new submission
+ Partners can no longer modify application details through standard update APIs
+ The application enters a defined approval workflow which may include business approval, technical approval, and finance approval stages

Partners can track submission progress by retrieving the application and monitoring the Stage field, which indicates the current approval stage (e.g., "Business Approval", "Tech Approval", "Finance Approval").

## Managing Submitted Applications
<a name="managing-submitted-applications"></a>

Once submitted, partners have limited options for managing benefit applications, but the API provides specific actions for common scenarios.

### Recalling Benefit Applications
<a name="recalling-benefit-applications"></a>

If a partner discovers an error or needs to make changes after submission, they can recall the application using the `RecallBenefitApplication` API action. Recall transitions the application back to `PENDING_SUBMISSION` status, allowing updates and resubmission.

When recalling an application, partners should provide:
+ **Identifier** - The ID or ARN of the benefit application to recall
+ **Reason** - An optional explanation for the recall (maximum 1000 characters)

The reason field enables better traceability and helps AWS understand common issues that lead to recalls, informing future improvements to the benefit application process.

After recall, partners can use `UpdateBenefitApplication` to make necessary changes, then resubmit using `SubmitBenefitApplication` when ready.

**Important**  
Recall is typically only available during early review stages. Applications that have progressed to later approval stages or have been approved may not be eligible for recall.

### Amending Benefit Applications
<a name="amending-benefit-applications"></a>

For minor corrections after submission, partners can use the `AmendBenefitApplication` API action to update specific fields without recalling the entire application. This is particularly useful when AWS reviewers request clarifications or corrections during the review process.

Amendments use a JSON Patch-style approach where partners specify:
+ **Path** - A JSONPath expression identifying the field to update (e.g., `$.CreditDisbursementDetails.AwsAccountIdForCredits`)
+ **Value** - The new value for the field
+ **Operation** - The operation to perform (currently only `REPLACE` is supported)

Partners can submit up to 10 amendments in a single API call. Each amendment must include an updated revision number for optimistic locking.

Amendments should be used for minor corrections. For substantial changes, partners should use `RecallBenefitApplication` to return the application to draft status for comprehensive updates.

### Canceling Benefit Applications
<a name="canceling-benefit-applications"></a>

If a partner no longer needs a benefit or wishes to withdraw their application, they can cancel it using the `CancelBenefitApplication` API action. Cancellation transitions the application to `CANCELED` status, permanently ending the application process.

When canceling an application, partners should provide:
+ **Identifier** - The ID or ARN of the benefit application to cancel
+ **Reason** - An optional explanation for the cancellation (maximum 1000 characters)

Once canceled, applications cannot be reactivated. If the partner later decides they need the benefit, they must create a new benefit application.

Common reasons for cancellation include:
+ Customer opportunity was lost or delayed
+ Partner capacity constraints changed
+ Business priorities shifted
+ Benefit is no longer needed for the intended purpose

## Viewing Benefit Application Details
<a name="viewing-benefit-application-details"></a>

Partners can retrieve complete information about a benefit application using the `GetBenefitApplication` API action. This provides a comprehensive view of the application including:

**Application Metadata:**
+ Unique identifier (ID) and Amazon Resource Name (ARN)
+ Associated benefit identifier
+ Application name and description
+ Current status (`PENDING_SUBMISSION`, `IN_REVIEW`, `ACTION_REQUIRED`, `APPROVED`, `REJECTED`, or `CANCELED`)
+ Current processing stage

**Status Information:**
+ Status Reason - Human-readable explanation of the current status
+ Status Reason Codes - Structured codes indicating specific issues or requirements (e.g., "Checklist Incomplete", "Project Plan Missing", "Design Win Missing")

**Application Content:**
+ Complete benefit application details JSON document
+ Partner contact information
+ File attachments with processing status
+ Associated resources (opportunities or allocations)
+ Resource tags

**Audit Information:**
+ Creation timestamp
+ Last modification timestamp
+ Current revision number

The status reason codes are particularly valuable when an application is in `ACTION_REQUIRED` status. These codes provide specific, actionable guidance on what partners need to address for the application to proceed.

## Listing Benefit Applications
<a name="listing-benefit-applications"></a>

Partners can view all their benefit applications using the `ListBenefitApplications` API action. This returns a paginated list of application summaries with powerful filtering capabilities.

Partners can filter applications by:
+ **Program** - View applications for specific programs (MAP, MDF, Sandbox, POC, etc.)
+ **Fulfillment Type** - Filter by delivery method (`CREDITS`, `CASH`, `ACCESS`, etc.)
+ **Benefit Identifier** - View applications for a specific benefit
+ **Status** - Filter by application status (`PENDING_SUBMISSION`, `IN_REVIEW`, `APPROVED`, `REJECTED`, `CANCELED`)
+ **Stage** - Filter by approval stage (Business Approval, Tech Approval, Finance Approval)
+ **Associated Resource ARNs** - Find applications linked to specific opportunities or allocations

The list response includes essential summary information such as:
+ Application ID, ARN, and name
+ Associated benefit ID
+ Programs and fulfillment types
+ Current status and stage
+ Creation and modification timestamps
+ Associated resources
+ Current revision number
+ Selected fields from benefit application details (as defined by the benefit owner)

Partners can configure result sorting using the Sort parameter, with options to sort by creation date, status, program, or benefit identifier in ascending or descending order.

**Dashboard Building:** The `ListBenefitApplications` API is designed to support partner dashboard creation. By filtering and sorting applications, partners can build views such as:
+ Applications requiring action (`ACTION_REQUIRED` status)
+ Recently submitted applications (sorted by creation date, `IN_REVIEW` status)
+ Approved applications pending allocation (`APPROVED` status)
+ Applications by program (filtered by specific programs)