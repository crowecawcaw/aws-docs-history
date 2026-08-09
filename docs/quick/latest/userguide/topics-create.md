# Creating Quick Sight Topics

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

|                                                               |
| ------------------------------------------------------------- |
| Intended audience:<br>Amazon Quick administrators and authors |

To create a Topic, you add one or more enriched datasets, define relationships between
them, and optionally add custom instructions that guide how the AI interprets cross-dataset
queries.

## Creating a Topic

Use the following procedure to create a Topic.

###### To create a Topic

1. On the Quick homepage, choose **Data** in
   the navigation pane at left.
2. Choose the **Topics** tab, and then choose
   **Create topic**.
3. Enter a topic name (for example, "Retail Sales Analytics") and an
   optional description, then choose **Create**.
4. Choose **Add dataset** and select the datasets you want
   to include in the Topic (up to 12 datasets).
5. After adding datasets, define the relationships between them. For more
   information, see [Defining relationships between datasets in a Topic](topics-relationships.md "topics-relationships.md").
6. (Optional) Add custom instructions that provide cross-dataset business
   rules. For more information, see [Adding custom instructions to a Topic](topics-custom-instructions.md "topics-custom-instructions.md").
7. Choose **Publish** to make the Topic available to
   users.

After publishing, share the Topic with business users so they can ask natural
language questions or use it in analysis. For more information, see [Sharing Quick Sight Topics](topics-sharing.md "topics-sharing.md").

## Prerequisites

Before creating a Topic, confirm that you have the following:

- Amazon Quick Enterprise Edition enabled with Author or Admin role.
- One or more datasets enriched with semantic metadata (column descriptions,
  synonyms, and semantic types). For more information, see [Data Preparation Experience (New)](data-prep-experience-new.md "data-prep-experience-new.md").
- Datasets representing a dimensional model (fact tables and dimension
  tables) loaded into SPICE or accessible through a supported
  Direct Query source.
- Permissions to create Topics and manage datasets.
