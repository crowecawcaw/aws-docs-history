# Integrations

## AWS Services

### Amazon S3

actions allow you to store and retrieve files and data.

**Available Actions**

- **Download File** - Downloads a file from Amazon S3 and returns a file object handle.
- **Upload File** - Uploads a file object handle to Amazon S3.
- **Copy Object** - Creates a copy of an object that is already stored in Amazon S3 from one source file to a destination location.
- **Delete Object** - Deletes a specified object from an S3 bucket.
- **List Objects** - Lists all of the objects in the given bucket. Can be filtered using a prefix.

###

actions allow you to connect to foundation models (FMs) from leading AI companies through a single API.

- **Basic model converse** - Sends a prompt to an AI model. Use natural language to generate text, analyze content, and get AI-powered responses.
- **Advanced model converse** - Prompts model with more options. Advanced options include custom message formats, tool integrations, and granular control over model behavior.

### Agents

Agent actions allows you to invoke AI assistants that can connect to your data sources, APIs, and backend systems.

- **Basic agent invoke** - Sends a request to an AI agent. Use for simple interactions that don't require file attachments, user input, or custom configurations.
- **Advanced agent invoke** - Calls an agent with more options. Used for advanced interactions that require file attachments, user input, or custom configurations.

### Data Automation

Bedrock Data Automation (BDA) simplifies the process of extracting valuable insights from unstructured content using generative AI.

**Available Actions**

- **Invoke Data Automation Async** - Process data with a data automation project or blueprints. Starts asynchronous data processing and returns an invocation ID.
- **Get Data Automation Status** - Gets details about a data automation invocation status and output location.

### Amazon Textract

Amazon Textract helps you add document text detection and analysis to your automations.

- **Basic document query** - Extracts data based on questions. Each query contains the question you want to ask and the alias you want to associate. Textract provides the text answer to each question and a confidence score.
- **Basic document analysis** - Extracts data from documents. Automatically detects and extracts forms (key-value pairs), tables (structured data), and text while preserving document layout and data relationships.

###

is a natural language processing (NLP) service for gaining insight into document content. It helps analyze text to extract key phrases, identify sentiment, and classify documents.

**Available Actions**

- **Classify Document** - Creates a classification request to analyze a single document in real-time using a custom model endpoint. Supports text input or document files (PDF, Word, or image).
- **Detect Key Phrases** - Detects the key noun phrases found in the text, identifying important concepts and topics within the content.

## External Applications

### Microsoft Outlook

The Microsoft Outlook actions allow your automations to manage emails and calendars.

- Email
  - **Send User Email** - Send an email message on behalf of a specific user.
  - **Reply to Email** - Reply to the sender of a message.
  - **List Folder Messages** - Get the messages in a specific folder of the signed-in user's mailbox.
  - **List User Mails** - Get the messages in the signed-in user's mailbox (including Deleted Items and Clutter folders).
  - **View Email** - Retrieve the properties and relationships of a specific message object.
  - **Update Email** - Update the properties of a message object.
  - **Delete Email** - Delete a message in the specified user's mailbox.
  - **List Email Attachments** - Retrieve a list of attachment objects attached to a message.
  - **Get Attachment** - Read the properties, relationships, or raw contents of an attachment.

- Folders
  - **List Mail Folders** - Get the mail folder collection directly under the root folder of the signed-in user.
  - **Move Email to Folder** - Move a message to another folder within the specified user's mailbox.
  - **Get Mailbox Settings** - Get the user's mailbox settings, such as automatic replies, date format, and time zone.

- Calendar
  - **List Calendar Events** - Fetch a list of calendar events for the specified user or resource from Microsoft Outlook.
  - **Create Calendar Event** - Create an event in the user's default calendar or specified calendar.
  - **Update Calendar Event** - Update the properties of an existing event object.

- Other
  - **List Places** - Get a collection of place objects (rooms or room lists) defined in the tenant.
  - **List Users** - Retrieve a list of users in the organization from Microsoft Outlook with their basic information.
  - **List Contacts** - Get a contact collection from the default contacts folder of the signed-in user.

### Microsoft Teams

The Microsoft Teams actions allow your automations to communicate with team members through channels and chat messages, as well as manage meetings.

- Messages
  - **List Chats** - View all chat conversations
  - **Create Chat** - Start a new chat conversation
  - **Get Individual Chat** - View details of a specific chat
  - **List All Chat Messages** - View messages in a chat conversation
  - **Send Chat Message** - Send a new message in a chat

- Teams
  - **List Teams** - View all teams accessible to the authenticated user
  - **Get Team** - View detailed information about a specific team
  - **List All Team Members** - View members of a team
  - **Invite User To Team** - Add a new member to a team

- Channels
  - **List All Channels** - View all channels within a specific team
  - **Create Channel** - Create a new channel within a team
  - **Get Channel** - View detailed information about a specific channel
  - **List All Channel Messages** - View messages posted in a channel
  - **Send Channel Message** - Post a new message to a channel
  - **Reply To Channel Message** - Add a reply to an existing channel message
  - **Invite Channel Member** - Add a member to a specific channel

- Meetings
  - **Create Online Teams Meeting** - Schedule a new online meeting
  - **Get Online Teams Meeting** - View details of a specific meeting
  - **List All Recordings** - View recordings from a meeting
  - **List All Transcripts** - View transcripts from a meeting

- Users
  - **List Users** - View list of users in the organization

### Microsoft SharePoint

The Microsoft SharePoint allows you to centrally store, manage, and share documents and information through your automations.

- Lists and items
  - **Get List** - Get a list of operations associated with a list
  - **Create Item** - Create a new list Item in a list
  - **Update Item** - Update the properties on a listItem
  - **Delete Item** - Removes an item from a list
  - **Get Item** - Returns the metadata for an item in a list
  - **List Item** - Get the collection of items in a list

- Sheets and files
  - **Add Sheet** - Add a new worksheet to the workbook
  - **Delete Sheet** - Remove worksheet from workbook
  - **Update Sheet** - Edit worksheet properties (rename, visibility)
  - **List Sheets** - Retrieve a list of worksheet objects
  - **Read Sheet** - Retrieve properties of a worksheet
  - **Upload File** - Creates or updates a workbook file

- Ranges and cells
  - **Read Range** - Retrieves values from a specified range
  - **Delete Range** - Deletes cells in a specified range
  - **Write Range** - Updates values in a specified range
  - **Get Used Range** - Returns the used range of the given worksheet
  - **Clear Range** - Clear range values including format, fill, and border
  - **Read Cell** - Gets the value from a specific cell
  - **Write Cell** - Sets the value of a specific cell

### Microsoft OneDrive

Microsoft OneDrive actions allow you to store, sync, and share files. You can interact directly with Microsoft Excel files saved to OneDrive for spreadsheet actions.

- File management
  - **Get Item** - View details of a specific file or folder
  - **Get Drive** - View OneDrive account details and storage information
  - **List Items** - View all files and folders in a drive
  - **Create Item / Create Folder** - Create a new folder or item in OneDrive
  - **List Children** - View items contained within a specific folder
  - **Delete Item** - Remove a file or folder
  - **Update Item / Move Item** - Update metadata or move files between folders
  - **Copy Item** - Create a copy of a file or folder in a different location
  - **Add Permissions** - Configure sharing and access permissions for files
  - **Upload File** - Add new files to OneDrive

- Excel
  - **Add Sheet** - Create a new worksheet in an Excel workbook
  - **Clear Range** - Remove content and formatting from a range of cells
  - **Delete Range** - Remove cells, rows, or columns from a worksheet
  - **Delete Sheet** - Remove a worksheet from a workbook
  - **List Sheets** - View all worksheets in a workbook
  - **Read Cell** - Get the value of a specific cell
  - **Read Range** - Get values from a range of cells
  - **Read Sheet** - View contents of an entire worksheet
  - **Read Used Range** - Get the range of cells that contain data
  - **Update Sheet** - Modify worksheet properties
  - **Write Cell** - Set the value of a specific cell
  - **Write Range** - Set values for a range of cells

### Salesforce

Salesforce actions allow you to automate the process of managing customer relationships across cases, opportunities, leads, campaigns, contacts and more.

- Cases
  - **Get Case List** - Gets a list of customer support cases from Salesforce, including their metadata and recent items.
  - **Get Case** - View details of a specific case
  - **Create Case** - Create a new support case
  - **Delete Case** - Remove an existing case
  - **Update Case** - Edit case details and information

- Opportunities, Leads, Campaigns, Feed Items, Contacts, Users, System

### Jira

Jira actions allow you to automate managing issues, projects, sprints and more.

- Issues, Comments, Projects, Sprints, Users

### ServiceNow

ServiceNow actions allow you to automate IT service management of incidents, change requests, and more.

- Incidents, Change Requests, Knowledge Base Articles, Problem Records, Attachments, System

### SAP

SAP actions allow you to automate processes involving business partner data, material stocks, bills of material, product masters, and physical inventory.

- SAP Business Partners, SAP Material Stock, SAP Bill Of Material, SAP Product Master, SAP Physical Inventory

## Custom REST APIs

Actions for working with any REST API endpoint.

- **Get request** - Retrieves data from a REST API. Used to fetch information from web services and APIs.
- **Post request** - Sends data to a REST API. Used to create or submit information to web services and APIs.
- **Put request** - Replaces data in a REST API endpoint. Used to update existing information through web services and APIs.
