

# Connecting your data

## 4. Prerequisites
<a name="connecting-your-data-prerequisites"></a>

Before starting data onboarding, ensure you have:

1. Amazon Connect Decisions Instance

   1. Your instance should already be created with an associated S3 bucket

1. Data Prepared

   1. Work with your Amazon Customer Success counterpart to determine which data you need based on how you plan to use Amazon Connect Decisions. Base data requirements include:

      1. Sales/Order History: 12\+ months of transaction records

      1. Product Details: Complete product catalog with specifications

      1. Site/Location Information: Warehouses, distribution centers, retail locations

      1. Current Inventory Holdings: On-hand inventory at each location

   1. All source data in CSV format with UTF-8 encoding

## 5. First Time Login: Onboarding Questionnaire
<a name="connecting-your-data-first-time-login"></a>

When you log in to Amazon Connect Decisions for the first time, the system presents a guided Onboarding Questionnaire. This personalization wizard helps the Decisions teammates contextualize the capabilities most relevant to your business. The questionnaire collects information about your industry, primary business challenges, and preferred approach for planning. Your responses will help optimize the onboarding steps based on your selection, allowing the system to streamline subsequent setup workflows and surface the most relevant configuration paths for your business. You must complete all steps before accessing the full application. The Decisions Teammate is available throughout the onboarding process via the right sidebar to answer questions in real time.

**Note**  
This is a onetime selection on first login only. Your responses provide additional context to optimize subsequent onboarding steps and help agents understand your business environment. All capabilities remain fully accessible regardless of your selections.

**Step 1: Select Industry**

**What you see: **A welcome message and a set of radio buttons prompting you to select the industry that best describes your business.
+ Select the radio button that best represents your business.
+ If none of the predefined options apply, select **Other**.

![Step 1 of the onboarding questionnaire: select your industry.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-step1-select-industry.png)


**Step 2: Define Your Biggest Challenge**

**What you see: **Your Step 1 response is displayed with an edit option. Below it, you are asked to identify your primary business challenge from three options. A feature comparison table is displayed to help you understand which capabilities are associated with each selection.
+ Review the options. See Table 1 below for the available Options and What They Mean.
+ Select the radio button that represents your most pressing challenge.
+ Optionally, review the feature comparison table below the options to understand what is included with each selection.

**Table 1**


| Option | Description | Key Features Enabled | 
| --- | --- | --- | 
| Maintain optimal inventory levels | Choose this if your primary challenge is avoiding stockouts while minimizing excess inventory. | Inventory optimization; Stockout prevention; Excess inventory reduction; Supply planning; Vendor lead time tracking | 
| Improve demand forecast accuracy | Choose this if your primary challenge is creating more accurate forecasts for better planning decisions. | Baseline forecasting; Consensus planning; Forecast accuracy tracking | 
| Both | Choose this if you need to address both inventory optimization and demand forecast accuracy simultaneously. | All supply specific and demand specific features are enabled | 

![Step 2 of the onboarding questionnaire: define your biggest challenge, with a feature comparison table.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-step2-biggest-challenge.png)


**Step 3: Choose Your Inventory Planning Approach**

**What you see:** Steps 1 and 2 are displayed as completed (indicated by green checkmarks) with your responses shown and editable. Step 3 asks how you would like to approach inventory planning, with two options highlighted.
+ Review the two inventory planning options. See Table 2 below for the available Options and What They Mean.
+ Select the radio button for the approach that matches your current state.

**Table 2**


| Option | Description | Best For | 
| --- | --- | --- | 
| Generate inventory plans with Amazon Connect Decisions | The system uses your historical sales and inventory data to create plans tailored to your business. | Organizations that do not have an existing planning solution or want to leverage AI generated plans from their historical data. | 
| Bring in existing inventory projections or plans | Upload your existing inventory plans or projections so you can use decisioning capabilities immediately. The system will help you upload and map your data. | Organizations that already have established planning processes and want to leverage monitoring, insight generation, and recommendation capabilities without changing their plan source. | 

![Step 3 of the onboarding questionnaire: choose your inventory planning approach.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-step3-inventory-planning.png)


**Step 4: Choose Your Demand Planning Approach**

**What you see:** Steps 1 through 3 are displayed as completed. Step 4 asks how you would like to approach demand planning.
+ Review the two demand planning options. See Table 3 below for the Available Options and What They Mean.
+ Select the radio button for the approach that matches your current state.
+ Click **Submit** to finalize the onboarding questionnaire.

**Note**  
Remember: This onboarding questionnaire is a onetime contextual input that helps optimize the onboarding steps based on your selections. It does not alter agent behavior or restrict access to any capabilities. All features of Amazon Connect Decisions remain fully available to you.

**Table 3**


| Option | Description | Best For | 
| --- | --- | --- | 
| Generate demand forecasts with Amazon Connect Decisions | The system uses your historical sales and order data to create demand forecasts tailored to your business. Amazon Connect Decisions orchestrates 18\+ forecasting tools to produce accurate baseline forecasts. | Organizations that do not have an existing forecasting solution or want to replace their current approach with AI generated forecasts. | 
| Bring in existing forecasts | Upload your existing demand forecasts so you can use decisioning capabilities immediately. The system will help you map and import your forecast data. | Organizations that already have established forecasting processes and want to leverage the monitoring, insight generation, and recommendation capabilities without changing their forecast source. | 

![Step 4 of the onboarding questionnaire: choose your demand planning approach.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-step4-demand-planning.png)


**After Completing the Questionnaire**

Click **Submit** after completing all four steps:

![Submitting the completed onboarding questionnaire.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-questionnaire-submit.png)

+ You will be **redirected to the Homepage** with dashboard and topic cards designed to guide you through the remaining onboarding steps.
+ The system will provide **onboarding instructions** in the natural language interface based on your selections. (You will see the below screenshots if you selected “Improve demand forecast” or “Both” in Step 2)

![Onboarding instructions shown in the natural language interface after submitting the questionnaire.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-onboarding-instructions-1.png)


![Additional onboarding instructions shown in the natural language interface.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-onboarding-instructions-2.png)


## 6. Creating Your First Source Flow
<a name="connecting-your-data-first-source-flow"></a>

Option 1: To start onboarding your data, click on **Let’s start** for the **Connect data** topic card on the homepage. The system will redirect you to the **Data Management** Page where you can upload your data.

![The Connect data topic card on the homepage.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-connect-data-topic-card.png)


Option 2: Navigate to the **Data Management** tab in the ‘Hamburger Menu’ in Amazon Connect Decisions. Here you can see Data flows. If you have not set one up yet, click **“Connect New Source”** to begin.

![The Data Management page with the Connect New Source option.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-connect-new-source.png)


## 7. Upload Your Source Data
<a name="connecting-your-data-upload-source-data"></a>

Upload your CSV files containing source data based on the required CDM tables for your use case. You can choose how you want to handle data updates:
+ **Append**: Add new data to existing data
+ **Replace**: Replace existing data with new data

![Uploading source data with Append or Replace update options.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-upload-append-replace.png)


**Note**  
Refer to the **Data Preparation Guide** to identify required source files from standard ERPs like SAP and Oracle NetSuite.

![Uploading CSV source files on the Data Management page.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-upload-source-files.png)


![Loading uploaded source data.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-load-data.png)


When you upload files by clicking on **Load Data**, Amazon Connect Decisions automatically creates a **Data Dictionary** which is agents’ interpretation of ingested source data in free text and **a folder structure in S3** for that data including:
+ A parent folder named after your selected source system
+ A subfolder named after your selected source table name
+ All files under a subfolder are saved against the same source table
+ This file structure is also used to create the Amazon S3 folder path

**Note**  
You need to click on a Source Data to view the S3 folder details.

![Viewing the S3 folder details for a source dataset.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-s3-folder-details.png)


## 8. Source-to-CDM Destination Mapping
<a name="connecting-your-data-source-to-cdm-mapping"></a>

Once your files are uploaded, Amazon Connect Decisions begins analyzing your data and map it automatically to one or many of Amazon Connect Decisions’s CDM destination tables.

**What to Expect**
+ This step can take between 10-15 minutes depending on the amount of data uploaded
+ The Data Agent works in the background to identify the best CDM destination datasets for your source data.
+ *Navigating away from this page will cause automated mappings to fail.* While waiting, please keep the Amazon Connect Decisions and Data Management tab open to ensure automated mapping completes.

![Automated source-to-destination mapping in progress.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-mapping-in-progress.png)


Once complete, the Data Agent provides rationale on source-to-destination mappings based on overlapping data which you can review and ask questions to the agent on any mapping results.

![The Data Agent provides rationale for source-to-destination mappings.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-mapping-rationale.png)


To review and edit mappings, you can:
+ Interact directly with the Data Agent using natural language to update source-destination mappings.
+ Turn on the **Advanced **switch and Click on the **Amazon Connect Decisions Data **you want to edit.

![Turning on the Advanced switch to edit mappings.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-advanced-switch.png)


![Selecting the Amazon Connect Decisions data to edit.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-edit-destination-data.png)


### Editing Mappings
<a name="connecting-your-data-editing-source-destination-mappings"></a>

From here, you can:
+ Update source and destination mapping manually if needed
+ Ask questions using the Data Agent on the right-hand side of the screen to confirm the mappings
+ Reference [user guides](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/data-model-asc.html) to learn more about specific datasets

![Editing source-to-destination mappings.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-editing-source-mappings.png)


## 9. Column/Data Mapping
<a name="connecting-your-data-column-data-mapping"></a>

After source-to-destination mapping is complete, Amazon Connect Decisions will automatically create SQL transformation queries from your source dataset to CDM destination. After any of your mappings complete, you will receive a notification from the Data Agent detailing the result of the mapping.

![Notification from the Data Agent about a completed column mapping.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-column-mapping-notification.png)


**From here, you should review the SQL generated for mappings by selecting “Review SQL” from the Action menu.**

Reviewing the mapping (SQL), you’ll see:
+ Source dataset columns you’ve added
+ Destination CDM table columns for reference
+ The transformation SQL connecting them
+ Rationale for mapping provided by the Data Agent

![Reviewing the generated SQL transformation for a mapping.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-review-sql.png)


### Editing Mappings
<a name="connecting-your-data-editing-column-mappings"></a>

You have two options for editing any mappings:

1. **Work with Data Agent**: Use natural language to ask questions, manage, and update the mappings

1. **Edit SQL Directly**: If you’re familiar with SQL, you can modify the query directly

### Testing Your Changes
<a name="connecting-your-data-testing-your-changes"></a>

As you edit the mapping query, continue to test it using the **“Test Query”** functionality which will give you a scrollable preview of how a sample of how your data is being transformed into destination CDM. Use this to ensure your transformation runs properly and to validate any appropriate updates from your source-to-destination CDM.

Once you are satisfied with the mapping output, select “**Save Query**” to save the transformation query for that source-destination pair.

![Testing and saving a transformation query.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-test-query-save.png)


## 10. Review and Accept Mappings
<a name="connecting-your-data-review-accept-mappings"></a>

Review the remaining mappings for each of your source datasets. The Data Agent remains persistent on the right-hand side of the screen for questions or troubleshooting help.

Once you’re satisfied with all mappings, accept them to complete data onboarding by clicking on **Accept mappings.**

![Accepting mappings to complete data onboarding.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-accept-mappings.png)


**Handle Failed Mappings**

If any mappings failed, you can select **“Restart mapping”** to restart all mappings, or manually retry a single mapping from the Actions menu via **“Retry SQL generation”**. The Data Agent can also retry mappings using natural language and will continue to help you identify and resolve issues if errors continue to persist.

![Handling failed mappings with restart and retry options.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-failed-mappings.png)


## 11. Monitor Your Flows
<a name="connecting-your-data-monitor-your-flows"></a>

### Destinations Tab
<a name="connecting-your-data-destinations-tab"></a>

Upon accepting mappings, you’ll be navigated to the **Destinations** tab within **Data Management** where you can:
+ Review destination flows
+ Manage and edit mappings (“Manage Flow”)
+ Delete obsolete flows
+ Review execution status for these flows

![The Destinations tab in Data Management.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-destinations-tab.png)


Selecting **“Manage Flow”** will bring you back to the Data Mapping experience where you can continue to work with the Data Agent to refine mappings over time.

![Managing a flow from the Destinations tab.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-manage-flow.png)


### Sources Tab
<a name="connecting-your-data-sources-tab"></a>

Navigating back to the **Sources** tab you can find:
+ The source dataset that has been created
+ Its associated S3 bucket
+ Options to:
  + Append more source data via another file upload
  + Manage the flow
  + Delete the flow
  + Review executions

Selecting **“Manage Flow”** will bring you back to the Data Mapping experience where you can continue to work with the Data Agent to refine mappings over time.

You also have access to **Create a New Source** as needed to restart the Data Onboarding process for any new data sources.

![The Sources tab in Data Management.](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/connecting-your-data-sources-tab.png)


## 12. Best Practices
<a name="connecting-your-data-best-practices"></a>

**Data Preparation**
+ Follow steps in the [4. Prerequisites](#connecting-your-data-prerequisites) section
+ Use UTF-8 encoding for all CSV files
+ Ensure filenames are unique
+ Validate data quality before uploading

**Working with Data Agent**
+ Be specific in your requests
+ Ask for explanations when you don’t understand any of its decisions
+ Test all SQL changes before accepting
+ Use the Preview feature to verify transformations

**Ongoing Maintenance**
+ Keep your source data updated
+ Monitor flow execution regularly
+ Address data errors promptly when notified
+ Document custom transformations for your team