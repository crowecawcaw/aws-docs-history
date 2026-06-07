# Connecting your data

## Prerequisites

Before starting data onboarding, ensure you have:

- Amazon Connect Decisions Instance
  - Your instance should already be created with an associated S3 bucket

- Data Prepared
  - Work with your Customer Success counterpart to determine which data you need based on how you plan to use Amazon Connect Decisions. Base data requirements include:
    - Sales/Order History: 12+ months of transaction records
    - Product Details: Complete product catalog with specifications
    - Site/Location Information: Warehouses, distribution centers, retail locations
    - Current Inventory Holdings: On-hand inventory at each location

  - All source data in CSV format with UTF-8 encoding

## Creating your first source flow

To start onboarding your data, navigate to the **Data Management** tab in Amazon Connect Decisions. Here you can see all of your existing source flows. If you have not set one up yet, choose **"Create New Source"** to begin.

## Upload your source data

Upload your CSV files containing source data based on the required CDM tables for your use case. You can choose how you want to handle data updates:

- **Append**: Add new data to existing data
- **Replace**: Replace existing data with new data

When you upload files, Amazon Connect Decisions automatically creates a folder structure in S3 for that data including:

- A parent folder named after your selected source system
- A subfolder named after your selected source table name
- All files under a subfolder are saved against the same source table
- This file structure is also used to create the Amazon S3 folder path

## Source-to-CDM destination mapping

Once your files are uploaded, Amazon Connect Decisions begins analyzing your data and map it automatically to one or many of Amazon Connect Decisions's CDM destination tables.

**What to Expect**

- This step can take between 10-15 minutes depending on the amount of data uploaded
- The Data Agent works in the background to identify the best CDM destination datasets for your source data.
- _Navigating away from this page will cause automated mappings to fail._ While waiting, please keep the Amazon Connect Decisions and Data Management tab open to ensure automated mapping completes.

Once complete, the Data Agent provides rationale on source-to-destination mappings based on overlapping data which you can review and ask questions to the agent on any mapping results.

To review and edit source mappings, you can:

- Interact directly with the Data Agent using natural language to update source-destination mappings.
- Choose the Action options and select **"Edit Sources"**.

### Editing mappings

From here, you can:

- Update source and destination mapping manually if needed
- Ask questions using the Data Agent on the right-hand side of the screen to confirm the mappings

## Column/Data mapping

After source-to-destination mapping is complete, Amazon Connect Decisions will automatically create SQL transformation queries from your source dataset to CDM destination. After any of your mappings complete, you will receive a notification from the Data Agent detailing the result of the mapping:

From here, you should review the SQL generated for mappings by selecting **"Review SQL"** from the Action menu.

Reviewing the mapping (SQL), you'll see:

- Source dataset columns you've added
- Destination CDM table columns for reference
- The transformation SQL connecting them
- Rationale for mapping provided by the Data Agent

### Editing mappings

You have two options for editing any mappings:

- **Work with Data Agent**: Use natural language to ask questions, manage, and update the mappings
- **Edit SQL Directly**: If you're familiar with SQL, you can modify the query directly

### Testing your changes

As you edit the mapping query, continue to test it using the **"Test Query"** functionality which will give you a scrollable preview of how a sample of how your data is being transformed into destination CDM. Use this to ensure your transformation runs properly and to validate any appropriate updates from your source-to-destination CDM.

Once you are satisfied with the mapping output, select "Save Query" to save the transformation query for that source-destination pair.

## Review and accept mappings

Review the remaining mappings for each of your source datasets. The Data Agent remains persistent on the right-hand side of the screen for questions or troubleshooting help.

Once you're satisfied with all mappings, accept them to complete data onboarding.

**Handle Failed Mappings**

If any mappings failed, you can select **"Restart mapping"** to restart all mappings, or manually retry a single mapping from the Actions menu via **"Retry SQL generation"**. The Data Agent can also retry mappings using natural language and will continue to help you identify and resolve issues if errors continue to persist.

## Monitor your flows

### Destinations tab

Upon accepting mappings, you'll be navigated to the **Destinations** tab within **Data Management** where you can:

- Review destination flows
- Manage and edit mappings ("Manage Flow")
- Delete obsolete flows
- Review execution status for these flows

Selecting **"Manage Flow"** will bring you back to the Data Mapping experience where you can continue to work with the Data Agent to refine mappings over time.

### Sources tab

Navigating back to the **Sources** tab you can find:

- The source dataset that has been created
- Its associated S3 bucket
- Options to:
  - Append more source data via another file upload
  - Manage the flow
  - Delete the flow
  - Review executions

Selecting **"Manage Flow"** will bring you back to the Data Mapping experience where you can continue to work with the Data Agent to refine mappings over time.

You also have access to **Create a New Source** as needed to restart the Data Onboarding process for any new data sources.

## Best practices

**Data Preparation**

- Follow steps in the Prerequisites section
- Use UTF-8 encoding for all CSV files
- Ensure filenames are unique
- Validate data quality before uploading

**Working with Data Agent**

- Be specific in your requests
- Ask for explanations when you don't understand any of its decisions
- Test all SQL changes before accepting
- Use the preview feature to verify transformations

**Ongoing Maintenance**

- Keep your source data updated
- Monitor flow execution regularly
- Address data errors promptly when notified
- Document custom transformations for your team
