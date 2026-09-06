

# Using Topics on sheets in Amazon Quick Sight
<a name="using-q-topics-on-sheets"></a>

You can use Quick Sight Topics as the data model for your analysis sheets. When you create an analysis from a Topic, you can select fields from any of the datasets in the Topic and Quick Sight automatically performs runtime inner joins based on the defined relationships. This eliminates the need to pre-join tables into a single flat dataset before building an analysis.

## Creating an analysis from a Topic
<a name="topics-on-sheets-new"></a>

To use a Topic as the data model for an analysis, use the following procedure.

**To create an analysis from a Topic**

1. On the Quick homepage, choose **Data** in the navigation pane, then choose the **Topics** tab.

1. Open the Topic you want to use.

1. Choose **Create analysis**.

1. Select **Interactive sheet** and choose **Create**.

1. In the analysis, the fields list shows columns from all datasets in the Topic. Select fields from multiple datasets and add them to a visual. Quick Sight performs runtime inner joins automatically based on the defined relationships.

The following rules apply when working with Topics in analysis sheets:
+ You must have Owner or Viewer permissions on the Topic to use it in an analysis.
+ When a visual references fields from multiple datasets, Quick Sight uses the defined relationships to determine the join path and performs inner joins at runtime.
+ You can create calculated fields that reference columns from different datasets within the Topic.
+ Row-level security (RLS) rules are enforced during runtime joins. Users see only the intersection of rows they are permitted to access in each dataset.
+ Each dataset in the Topic can have its own independent refresh schedule. Visuals always reflect the latest data available in each dataset.

**Note**  
Runtime joins in analysis sheets use inner join semantics only. Rows without matching keys in both datasets are excluded from visual results. If you need outer join behavior, use the Topic in Amazon Quick chat, where the LLM-powered chat agent can generate SQL with outer joins based on custom instructions.

For more information about creating and configuring Topics, see [Working with Amazon Quick Sight Topics](topics.md).

## Enabling legacy Topics in an analysis
<a name="topics-on-sheets-legacy"></a>

**Note**  
The following applies to legacy Topics only. For information about the differences between new Topics and legacy Topics, see [Working with legacy Topics](legacy-topics.md).

For legacy Topics, you can enable a topic in an analysis to activate the ML-powered automated data prep, which speeds natural language topic creation. Automated data prep automatically selects high-value fields, chooses user-friendly field names and synonyms, and formats data for presentation.

Automated data prep binds the legacy Topic to your analysis and prepares an index for searching in natural language. Dashboard users find that the linked topic is automatically selected in the search bar, making it easier for them to query the dataset.

The following rules apply to working with legacy Topics in an analysis:
+ You must be an owner of the underlying dataset before you can create a legacy Topic using that dataset or an analysis that uses that dataset.
+ You must be an owner of a legacy Topic before you can link it to an analysis.

**To enable a legacy Topic**

1. Open the analysis that you want to use with automated data prep.

1. On the top navigation bar, choose the topic icon.

1. Choose one of the following:
   + To activate a new topic, select **Create new topic** and enter a topic title and optional description.
   + To activate an existing topic, select **Update existing topic** and choose the topic from the list.

1. Choose **ENABLE TOPIC** to confirm your choice.

1. When the topic is finished processing, you can use what it learned from the analysis to ask questions in natural language.

   Now, when users navigate to the dashboard, the linked topic is automatically selected in the search bar.

After a legacy Topic is linked to an analysis, further updates to the analysis are not automatically synced to the topic. Authors need to manage updating topics manually from the **Topics** page.