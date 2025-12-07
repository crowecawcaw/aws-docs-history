# Predictive Insights

(Preview)

_Predictive Insights_ (Preview) is a feature of
Amazon Connect Customer Profiles that uses artificial intelligence to generate personalized product and
content recommendations for your customers. By analyzing customer interaction data,
Predictive Insights helps you provide more relevant experiences across all customer
touchpoints.

## How Predictive Insights works

Predictive Insights (preview) uses AI models to analyze customer behavior patterns and
generate real-time recommendations. The service processes your customer interaction
data, such as purchase history and browsing activity, to identify patterns and
preferences.

- **Step 1:** Add interaction data to profiles
  using existing data connectors to train AI models with your customer interaction
  data
- **Step 2:** Add item catalog to S3 to allow Customer Profiles
  to access your item data through the AWS Management Console
- **Step 3:** Create recommendations by defining
  recommendation types (similar items, frequently paired items, popular items)
- **Step 4:** Apply recommendations across Amazon Connect ecosystem including Agent Workspace, Flows, and Connect AI agents

## Prerequisites

- **Enable Data Store in Customer Profiles**

To train AI models using your Customer Profiles, you need to enable data
store. See details under Customer Profile Data Store to learn more.

- **KMS**

You have configured Customer Profiles to encrypt your data under a
AWS KMS key.

- **Security Profiles**

You have configured Security Profiles to support View (list and view
predictive insights), Create (create recommendations), Delete (delete
recommendations), and Edit (update recommendations) permissions with Predictive
insights enabled.

## Benefits of using Predictive

Insights

Using Predictive Insights provides several key benefits:

- Improve customer experience with personalized recommendations
- Increase sales opportunities through relevant product suggestions
- Save agent time by automatically surfacing relevant recommendations
- Deliver consistent recommendations across all customer touchpoints
- Update suggestions in real time as customer behavior changes

## Data Considerations

The following sections provide guidance on how to match use-cases and assess data
readiness for Predictive Insights.

### Have you matched your use cases to Predictive

Insights?

Predictive Insights personalization types can address the following use
cases:

- Generating personalized recommendations for a user
- Recommending similar or related items
- Recommending trending or popular items
- Re-ordering items by relevance

### Do you have enough item interaction

data?

For all use cases and personalization types, you must have at minimum 1,000 item
interactions for 25 unique users with at least two interactions each. For quality
recommendations, we recommend that you have at minimum 50,000 item interactions from
at least 1,000 users with two or more item interactions each.

### Do you have a real-time event streaming

architecture in place?

If you have the ability to stream real-time events to Connect Customer Profiles,
you will be able to take advantage of real-time personalization. With some
personalization types, Predictive Insights can learn from your user’s most recent
activity and update recommendations as they use your application.

### Is your data optimized for Predictive

Insights?

We recommend you check for the following in your data:

- Check for missing values. We recommend that a minimum of 70% of your
  records have data for every attribute. We recommend columns that allow null
  values be at least 70% complete.
- Fix any inaccuracies or issues in your data, such as inconsistent naming
  conventions, duplicate categories for an item, mismatched IDs across
  datasets, or duplicate IDs. These issues can negatively impact
  recommendations or lead to unexpected behavior. For example, you might have
  both “N/A” and “Not Applicable” in your data, but filter out recommendations
  based on only “N/A”. Items marked "Not Applicable" would not be removed by
  the filter.
- If an item, user, or action can have multiple categories, such as a movie
  with multiple genres, combine the categorical values into one attribute and
  separate each value with the | operator. For example, a movie’s GENRES data
  might be Action | Adventure | Thriller.
- Avoid having more than 1000 possible categories for a column (unless the
  column contains data for only filtering purposes).
