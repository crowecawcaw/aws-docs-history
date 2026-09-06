

# Working with data in apps in Quick
<a name="working-with-data-apps"></a>

You can persist and manage data within your apps in Quick apps in multiple ways.

## Built-in app storage
<a name="apps-builtin-storage"></a>

The simplest way to persist data is with built-in app storage. It is a key-value system that requires no external setup and scales to support large numbers of records.

### Storage scopes
<a name="apps-storage-scopes"></a>
+ **Private storage** — Data visible only to the current user. Use for personal settings, preferences, saved filters, bookmarks, and per-user state.
+ **Shared storage** — Data visible to anyone with app access. Use for collaborative lists, comments, votes, shared configuration, and team data.

### Storage operations
<a name="apps-storage-operations"></a>


| Operation | Private | Shared | Description | 
| --- | --- | --- | --- | 
| Put Item | Yes | Yes | Store or update a key-value item. | 
| Get Item | Yes | Yes | Retrieve an item by key. | 
| List Items | Yes | Yes | List items with optional key prefix filter. | 
| Delete Item | Yes | Yes | Remove an item by key. | 
| List by Tag | No | Yes | Query shared items by tag (secondary index). | 

### Key concepts
<a name="apps-storage-concepts"></a>
+ **Tables** — Logical groupings for your data. You define table names; no setup is required.
+ **Keys** — Each item has a unique key within its table. Keys can be up to 255 characters.
+ **Values** — String values up to 350 KB. Use JSON serialization for structured data.
+ **Tags (shared only)** — Optional categorization strings on shared items. Tags enable efficient querying by category.
+ **Write modes** — UPSERT (default) overwrites existing items. INSERT fails if the key already exists, which is useful for preventing duplicates.

**Note**  
Each app has completely separate storage. Data persists across user sessions and app reloads.

**Note**  
In public apps, anonymous viewers can read from and write to shared storage but cannot access private storage. Design your data model accordingly if you plan to publish your app publicly.

## Exporting data
<a name="apps-exporting-data"></a>

You can ask the agent to add export functionality. Apps in Quick supports exporting data as CSV, JSON, PDF, and Excel files through the bridge API. You can also have your app write data snapshots to a connected space. This serves as a backup and makes the data available to other Quick capabilities.

## Handling write approvals when AI inference is active
<a name="apps-write-approvals"></a>

When an app uses AI inference and writes data (to shared storage or through an action connector), you must review and approve each write payload. This security measure ensures that you review AI-generated content before the app persists it.

Three strategies can reduce the frequency of approval prompts:

1. **Batch writes** — Collect all items and save them under a single storage key in one operation.

1. **Separate AI from writes** — Design the app so that AI processing and data persistence happen in distinct user actions.

1. **Remove AI inference when not needed** — If your app does not use AI-generated content, ensure the AI inference integration is not registered. Without AI inference, you can choose "Allow on this app" for write operations. The permission persists across sessions.

## Accessing user information
<a name="apps-user-identity"></a>

With apps in Quick, you can access the current user's identity at runtime. This lets you personalize the app experience, display the user's name, or implement per-user logic.

Available user information includes email, first name, last name, and identity name.

**Tip**  
Combine user identity with private storage to build personalized experiences such as greetings, saved preferences, bookmarks, and custom dashboards per user.