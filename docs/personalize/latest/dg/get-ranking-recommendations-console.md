# Getting a personalized ranking (console)

To get a personalized ranking for a user from the Amazon Personalize console, choose the campaign that you are using and
then provide their user ID, specify the list of items you want ranked for the user, optionally choose a filter,
and optionally provide any context data.

###### To get a personalized ranking for a user

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign into your account.
2. Choose the dataset group that contains the campaign you are using.
3. In the navigation pane, choose **Campaigns**.
4. On the **Campaigns** page, choose the target campaign.
5. Under **Test campaign results**, enter the **User ID** of the
   user that you want to get recommendations for.
6. For **Item IDs**, enter the list of items to be ranked for the user.
7. Optionally choose a filter. For more information,
   see [Filtering recommendations and user segments](filter.md "filter.md").
8. If you enabled metadata in recommendations for your campaign, for **Items dataset columns**, choose the metadata columns that
   you want to include in recommendation results.
   For information about enabling metadata, see [Item metadata in recommendations](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").
9. If your campaign uses contextual metadata
   (for requirements see [Increasing recommendation relevance with contextual metadata](contextual-metadata.md "contextual-metadata.md"))
   optionally provide context data.

For each context, for the **Key**, enter the metadata field, and for the
**Value**, enter the context data. 10. Choose **Get personalized item
rankings**. A table containing the items ranked in order of predicted interest for the user appears.
