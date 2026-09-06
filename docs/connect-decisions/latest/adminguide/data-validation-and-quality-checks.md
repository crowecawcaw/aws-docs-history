

# Data Validation and Quality Checks
<a name="data-validation-and-quality-checks"></a>

## Overview
<a name="data-validation-overview"></a>

Data validation ensures your data meets quality requirements before Amazon Connect Decisions capabilities execute. The system validates data based on your configured plans, metrics, and rules to identify issues that could block or degrade performance.

## How Data Validation Works
<a name="data-validation-how-it-works"></a>

### Validation Triggers
<a name="data-validation-triggers"></a>

Data validation runs automatically at the following times:
+ **Insights configuration changes**: When you create or modify metrics, rules, or other configurations
+ **Plan creation**: When you create an ad-hoc plan or at each scheduled plan run
+ **Data refresh**: After each data refresh to your Destination flows
+ **Capability execution**: Before or during AI teammate operations (e.g., when root-causing an exception or determining recommendations)

### Validation Types
<a name="data-validation-types"></a>

Amazon Connect Decisions performs two types of validation:

**Data Presence Validation** verifies that required datasets and fields are loaded based on your configured resources (metrics, rules, plans).

**Data Quality Validation** validates that provided data meets quality requirements based on your setup configuration, including:
+ **Setup Criteria Validation**: Confirms products and sites match your rule criteria (e.g., product categories, site locations)
+ **Hierarchy Validation**: Identifies missing hierarchical relationships if you use hierarchies in your setup
+ **Scope Validation**: Confirms all necessary data exists for identified products and sites
+ **Quality Assessment**: Evaluates data quality and usability for operational requirements

### Progressive Validation
<a name="data-validation-progressive"></a>

Amazon Connect Decisions enables capabilities for products and sites with valid data rather than blocking functionality for your entire dataset. When validation issues affect specific products or sites, the system continues processing products and sites with valid data, identifies products or sites with data issues, and alerts you to the specific items requiring attention. This allows you to begin using capabilities while resolving the remaining data issues.

## Accessing Data Validation Errors
<a name="data-validation-accessing-errors"></a>

You can view data validation errors through three entry points:

1. "Data Validation Errors" metric on the home page

1. Data validation errors topic card on the home page

1. "Data Management" in the left navigation > "Errors" tab

## Reviewing Validation Errors
<a name="data-validation-reviewing-errors"></a>

The Errors page displays all open and resolved validation errors. You can search and filter by any of the following columns:
+ **ID**: Unique identifier for the validation error
+ **Status**
  + **Open**: Error has not been resolved
  + **Resolved**: Error has been fixed and validated
+ **Description**: Explanation of the data quality issue
+ **Issue Type**
  + **Missing required data**: Mandatory data is not provided to trigger an operation (e.g., no outbound\_order\_line source table for Supply Plan)
  + **Invalid data values**: Data exists but contains incorrect values (e.g., negative product cost)
  + **Missing relationships**: Required hierarchical or reference relationships are missing (e.g., missing product hierarchies)
  + **Insufficient data**: Not enough data available to perform required operations (e.g., demand plan requires 12 months of historical order data but only 3 months exist)
+ **Capability**: The affected capability or resource
  + Supply Plan
  + Demand Plan
  + Insight (includes Exceptions, Recommendations, and RCA for Supply or Demand)
+ **Destination**: Impacted destination flow
+ **Priority**
  + **Critical**: At least one capability is fully blocked and cannot execute
  + **High**: At least one capability is partially blocked (some products or sites cannot be processed)
  + **Medium**: At least one capability has reduced accuracy (will run but with degraded results)
+ **Created at**: Timestamp showing when the error was first detected

## Viewing Error Details
<a name="data-validation-viewing-error-details"></a>

Select any error to view detailed information. The detail screen displays the above information along with a Last Occurred On timestamp, related resource and link (the metric, rule, or plan representing the capability impacted by the issue), and a preview of up to 100 rows of impacted data showing how the data validation error is manifesting.

### Available Actions
<a name="data-validation-available-actions"></a>

From the error detail screen, you can:
+ **Troubleshoot**: Launch the AI teammate to assist with troubleshooting the issue in natural language and receive detailed remediation guidance
+ **Resolve Error**: Manually mark the error as resolved if you have fixed the underlying issue
+ **Download**: Download the complete affected dataset for detailed analysis and correction

## Resolving Data Validation Errors
<a name="data-validation-resolving-errors"></a>

### Resolution Workflow
<a name="data-validation-resolution-workflow"></a>

1. Review the error description and priority to understand the impact

1. Check the impacted data preview to see which specific records are affected

1. Follow the specific recommendation provided for remediation

1. Choose an appropriate action:
   + **For configuration issues**: Work with your managers and planners to adjust the metric, rule, or plan configuration
   + **For mapping issues**: Correct uploaded source data or update data transformations and mappings
   + **For missing or invalid data**: Upload corrected data

1. Manually mark the error as resolved once you have addressed the underlying issue

### Working with the AI Teammate
<a name="data-validation-working-with-ai-teammate"></a>

Use the Troubleshoot option to ask questions like "What errors should I focus on first?" or "Which errors are blocking my demand plan?", receive detailed explanations of the issue and its impact, get step-by-step guidance on resolution approaches, and understand how the error affects your specific configuration. The AI teammate can act as a guide to resolving the issue within Amazon Connect Decisions and within your source data systems.

## Best Practices
<a name="data-validation-best-practices"></a>
+ **Prioritize by severity**: Focus on Critical errors first, as they fully block capabilities from executing. Then address High priority errors that partially block processing, followed by Medium priority issues that reduce accuracy.
+ **Review recommendations carefully**: Each error includes specific, actionable guidance tailored to the issue based on your configuration.
+ **Use progressive validation to your advantage**: Don't wait to resolve every error before using capabilities. The system enables functionality for valid products and sites while you work on resolving issues for others.
+ **Monitor after data refreshes**: Check for new validation errors after each data update to catch issues early before they impact production workflows.
+ **Download impacted data strategically**: Use the download option when you need to analyze all affected records beyond the preview, or when you need to provide the complete dataset to your data team.
+ **Use the AI teammate for complex issues**: The Troubleshoot option provides contextual assistance that adapts to your specific situation and configuration.
+ **Verify resolution**: After fixing data issues, manually mark errors as resolved to confirm your fix was successful and remove them from the Open list.