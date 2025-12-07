# Review findings from a design review

Review findings help you understand which security requirements are met, which need attention, and what actions to take to improve your design’s security posture before implementation begins.

In this procedure, you’ll learn how to access, filter, and interpret design review findings to address security findings effectively.

## Prerequisites

Before you begin, ensure you have:

- A completed design review
- Access to the AWS Security Agent web application
- Familiarity with your organization’s enabled security requirements

## Step 1: Access the design review

Navigate to your design review to view the findings and summary information.

1. Log in to the AWS Security Agent web application.
2. Navigate to the **Design reviews** section.
3. Select the design review you want to examine from the list.

###### Tip

The design review details page displays a summary of review status, completion date, and the number of files reviewed.

## Step 2: Review the findings summary

Examine the high-level summary to understand the overall security posture of your design.

1. Locate the **Summary** section near the top of the page.
2. Review the count for each compliance status category: **Compliant**, **Non-compliant**, **Insufficient data**, and **Not applicable**.

###### Note

The summary provides counts for each status type, helping you quickly assess the number of findings requiring attention. For detailed explanations of each status, see Step 4.

## Step 3: Filter and navigate findings

Use the filtering and search capabilities to focus on specific findings or compliance statuses.

1. In the **Review findings** section, locate the filter controls.
2. To filter by status:
   1. Click the status dropdown menu.
   2. Select a specific compliance status to view only findings with that status.

3. To search for specific security requirements:
   1. Enter keywords in the search field.
   2. Results update automatically as you type.

4. Use the pagination controls to navigate through multiple pages of findings.

###### Tip

Filter by **Non-compliant** status first to prioritize findings that require immediate attention in your design.

## Step 4: Understand compliance statuses

Each finding displays a compliance status that indicates how your design addresses a specific security requirement:

- **Compliant** – Your design meets the security requirement based on the analysis
- **Non-compliant** – Your design violates or inadequately addresses the security requirement
- **Insufficient data** – The uploaded files lack enough information to determine compliance
- **Not applicable** – The security requirement doesn’t apply to your system design

###### Important

Focus on **Non-compliant** and **Insufficient data** statuses, as these require action. Address non-compliant findings by updating your design, and resolve insufficient data findings by uploading additional design documentation.

## Step 5: View finding details

Select individual findings to view detailed justification and remediation guidance.

1. In the findings table, click on a security requirement name.
2. Review the finding details, which include:
   - The specific security requirement being evaluated
   - A comment explaining why the finding received its compliance status, including specific details about what’s missing or non-compliant
   - Recommended remediation guidance to address the finding
   - Links to your organization’s internal documentation or standards for the security requirement

###### Note

The comment explains AWS Security Agent’s reasoning with specific details. For insufficient data findings, the comment identifies what information is missing, such as "The design documents don’t mention authentication mechanisms" or "No information found about data encryption at rest."

## Step 6: Address findings

Take action on findings that require attention to improve your design’s security posture.

For **Non-compliant** findings:

1. Review the recommended remediation guidance.
2. Review any linked internal documentation for additional context.
3. Update your design documents to address the security requirement.
4. Document the changes you make for future reference.

For **Insufficient data** findings:

1. Read the comment carefully to understand what specific information is missing.
2. Create or update design documents with the missing details.
3. Prepare the updated files for resubmission.

## Next steps

After reviewing your design findings:

- Download the findings report as a CSV file for sharing with your team
- Update design documents to address non-compliant findings
- Create additional documentation for insufficient data findings
- Share findings with your development team for discussion
- Clone this design review to create a new review with the original documents pre-loaded, allowing you to update the name and run the analysis again to verify improvements
- Proceed with implementation for designs that meet compliance requirements

For more information about managing security requirements, see [Manage security requirements](security-requirements.md "security-requirements.md").

For more information about creating design reviews, see [Create a design review](perform-design-review.md "perform-design-review.md").
