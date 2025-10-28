# Known limitations for the Microsoft Yammer

connector

The Microsoft Yammer connector has the following known limitations:

- Due to API limitations, an incremental sync will not update deleted
  **Messages**, **Attachments**,
  **Communities** and **Users**. To update deleted
  entities, you must run a full sync.
