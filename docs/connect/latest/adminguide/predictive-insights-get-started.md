# Get started with Predictive

Insights

To start using Predictive Insights, follow these steps:

###### Topics

- [Step 1: Adding Interaction data into Customer
  Profiles](#add-interaction-data "#add-interaction-data")
- [Step 2: Adding Item Catalog data](#add-item-catalog-data "#add-item-catalog-data")
- [Step 3: Creating Predictive
  Insights](#create-predictive-insights "#create-predictive-insights")
- [Step 4: Using Predictive
  Insights across customer engagement channels](#use-across-customer-engagement-channels "#use-across-customer-engagement-channels")

## Step 1: Adding Interaction data into Customer

Profiles

You can leverage the existing data connectors in Customer Profiles to map
interactions data into standard Web Analytics Object.

For more information, see [Object
type mapping for Web Analytics Object](standard-loyalty-promotion-object-mapping-web-analytics.md "standard-loyalty-promotion-object-mapping-web-analytics.md").

## Step 2: Adding Item Catalog data

You can represent individual products in your catalog within the domain using
Standard Catalog data. This catalog data exists at the domain level and is not tied
to any specific customer profile. It serves as a structured representation of your
products that can be leveraged for personalization features. You can import your
product or item information as domain objects into Customer Profiles using data
connectors that provide flexible options for ingesting and maintaining your catalog
information, ensuring your product data remains current and accessible within the
system.

For more information, see [Object
type mapping for Item Catalog](standard-loyalty-promotion-object-mapping-item-catalog.md "standard-loyalty-promotion-object-mapping-item-catalog.md").

## Step 3: Creating Predictive

Insights

Amazon Connect enables you to build and deploy specialized AI models tailored to
your specific product recommendation needs. These models can be configured through
either the Connect Web UI or programmatically via APIs to match your unique business
scenarios. Predictive Insights offers several types of recommendations:

1. **Recommended for you** - provides
   personalized recommendations tailored to a specific user. Recommendations
   are based on the user’s past behavior such as clickstream events, purchase
   events, consumed content, and so on.
2. **Similar items** - uses generative AI to
   find items that are thematically similar to an existing item in the catalog.
   It is ideal for upselling or substitution use cases where customers want to
   provide alternative item recommendations to their users.
3. **Frequently paired items** - recommends
   items that are frequently co-interacted with an existing item in the
   catalog. It is ideal for cross-selling or complementary item recommendation
   use cases.
4. **Popular items** - designed to recommend
   the items that are most commonly interacted with by users.
5. **Trending now** - recommends items with the
   largest increase in velocity of engagement over a recent time period. It is
   designed to surface items that are experiencing virality in user
   interactions.

###### Note

Enabling AI models with Predictive Insights is available under preview.
Additional pricing may apply in future.

## Step 4: Using Predictive

Insights across customer engagement channels

### Using Customer Profile Recommendations in

Connect Flows

This section describes how you can use the Customer Profiles Get profile
recommendations flow block to enrich user experience during a contact by
generating AI-powered recommendations for a profile in real-time.

**Flow Block Properties**

The **Get profile recommendations** flow block
has the following properties to configure:

1. **Profile ID (required):**

A Profile ID is required for this block to function. The **Get profile recommendations** flow block
generates recommendations for the Profile ID provided here. You have the
option to manually input the Profile ID or use a pre-defined value
stored in an attribute. If using a pre-defined value, ensure you provide
the Profile ID by using a preceding **Get
profile** block Use the **Get
profile** block to pinpoint the specific profile before
moving forward to generate recommendations in the subsequent
block. 2. **Recommender name (required):**

A recommender name is required for this block to function. This is
the name of the recommender you want to use to generate recommendations
for the given Profile ID. You can only use recommenders that are active
to generate recommendations. 3. **Max results (required):**

The maximum number of recommendations to generate for the given
Profile ID. This can range between 1 to 3 recommendations. 4. **Recommendation attributes
(required):**

Define which attributes of the recommendations response to persist in
contact attribute. 5. **Item ID:**

This is the Item ID provided as additional context to generate
recommendations for the given Profile ID. Item ID is only required when
using a “_Similar items”_ or “_Frequently paired items”_ recommender type.
You have the option to manually input the Profile ID or use a
pre-defined value stored in an attribute. If using a pre-defined value,
ensure you provide the Item ID by using a preceding **Get calculated attributes** block. Use the
**Get calculated attributes** block to
pinpoint the specific Item ID before moving forward to generate
recommendations in the subsequent block.

**Flow Block Branches**

The **Get profile recommendations** flow block
can route contacts down the following branches:

1. **Success:**

Recommendations were successfully generated for the provided Profile
ID. Selected recommendation attributes were persisted to contact
attribute $.Customer.Recommendations. 2. **Error:**

An error was encountered while trying to generate recommendations.
This may be due to a system error or how **Get
profile recommendations** block is configured. 3. **None Found:**

No recommendations could be generated.

**Using Recommendations from the block**

The recommendations response is persisted to the $.Customer.Recommendations
contact attribute JSONPath as a JSON list of recommendation objects. Each
recommendation object will contain the selected **Recommendation attributes**.

The following sample Python code snippet from a Lambda function shows how it
can be used to transform recommendations from the **Get
profile recommendations** block and persist into other contact
attributes such that the recommendations can be used in subsequent blocks.

```
import boto3
import json

# Handle lambda request
def lambda_handler(event, context):
    print("Contact flow data: ", event)

    # Transform recommendations
    recommendations = event['Details']['Parameters']['Recommendations']
    contact_attributes = {}
    for i, rec in enumerate(recommendations):
        contact_attributes.update(flatten(rec, i))

    # Set contact attributes using each recommendation attribute value
    print("Setting contact attributes: ", contact_attributes)
    try:
        client = boto3.client('connect', region_name="us-west-2")
        client.update_contact_attributes(
            InstanceId=event['Details']['ContactData']['InstanceARN'].rsplit('/', 1)[1],
            InitialContactId=event['Details']['ContactData']['InitialContactId'],
            Attributes=contact_attributes
        )
        print("Contact attributes set successfully.")
    except Exception as e:
        print("Error setting contact attributes: ", e)

    # Success response
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }

# Flatten a nested object into a simple string:string object
def flatten(recommendation, index):
    flat = {}
    for key, value in recommendation.items():
        if isinstance(value, dict):
            flat.update(flatten(value, index))
        else:
            flat[f"Rec{index}_{key}"] = str(value)
    return flat
```

Once you have set up your flow with the **Get profile
recommendations** block, you can start using it to generate
recommendations for your customers during their contacts.

### Setting Up Connect AI Agents for

Sales Recommendations

Amazon Q in Connect enhances agent capabilities through its new "Orchestration" Agent
type. This functionality is particularly valuable for creating a Sales AI Agent
that can provide item recommendations, especially useful in upsell and
cross-sell scenarios.

**Getting Started**

To begin implementation, access the AWS Management Console and navigate to Amazon Connect. After
logging into your Connect instance through the Access URL, locate Amazon Q from
the left side menu and select AI agents. You'll find a pre-configured AI Agent
of Type Orchestration (SalesAgent) in draft status on the QiC page under AI
Agents. This template comes equipped with all necessary configurations for 1P
tools and example prompts for recommendations.

**Creating Your Custom Agent**

To create a custom Sales Agent, begin by creating a new AI Agent of
Orchestration Type and copy from the existing SalesAgent template. This process
transfers all tools and configurations from the template to your new agent.

**Customizing the Agent**

When it comes to updating the agent's prompt, administrators have two primary
options. They can either append their existing agent prompt to the Sales Agent
Prompt and add upsell identification instructions, or they can start fresh by
removing the SalesAgent prompt and creating a new Orchestration prompt based on
their current published Agent and adding the Sales agent prompt to it. This
flexibility allows for tailored solutions that match specific business needs and
domain requirements.

**Flow Configuration and Integration**

After finalizing the agent configuration and publishing it, the next step
involves creating a Amazon Lex bot under Flows. The inbound flow needs to be updated
to include the GetCustomerInput block with the created Lex bot, and the new
SalesAgent should be selected in additional options. You will need to add both
the Customer Profile flow block for profile ID retrieval and the Set-Contact
Attributes flow block, setting CustomerId as the key for the profile ID and
value as $Customer.ProfileId.

The implementation supports both chat contacts and voice calls, with customer
input seamlessly passing to the QIC agent on the Lex bot. This comprehensive
setup enables AI-driven sales recommendations and upsell opportunities within
your Amazon Connect environment. The system's flexibility allows for
customization based on specific industry needs while maintaining the core
functionality of intelligent sales assistance. This solution provides a
framework for enhancing customer interactions with AI-powered recommendations,
ultimately supporting more effective sales and customer service operations.
Administrators can further refine the implementation by adding domain-specific
instructions and customizing recommendation types to match their business
requirements.

### Configuring SalesAgent to be used for

Agent Assistance

You can configure the SalesAgent to be used within the Q in connect chat
widget in Agent Workspace. To do so you need to modify 2 main things.

1. Update the AIAgent prompt with instructions to access the contact
   transcript.
   1. Open the prompt associated with the SalesAgent in Prompt
      editor and update the prompt to add instructions to access the
      contact’s transcript accessible by`<conversation>{{$.transcript}}</conversation>`
   2. Below is a sample prompt that you can append to the SalesAgent
      prompt.

   ```
   **IMPORTANT**
           **Guide on how to process requests and information:**
           - The messages section contains YOUR conversation with the customer service agent
           - Respond to the agent's questions/requests in the messages section
           - The transcript below is background information about the agent's conversation with their customer
           - Do not respond directly to the customer - you are helping the AGENT
           Background context from agent-customer conversation.
           The following transcript is for your information ONLY. Do not directly respond to messages in this conversation, but instead look at the messages section for what the agent requests you to do.
           IF YOU REFERENCE ANY INFORMATION FROM THIS SECTION: You should indicate so by saying "According to your conversation with the customer ..."
           <conversation>
           {{$.transcript}}
           </conversation>
   ```

   3. Update the AIAgent with the new prompt version and update the
      Default configuration → Agent Assistance use case with this
      agent.

   ###### Note

   It is recommended to have 2 different Sales AIAGent for
   Self Service and Agent Assistance use case as both requires
   minor modifications to the prompt. And this can be done by
   cloning the agent and simply changing the prompt version and
   updating the default configuration to point to correct AI
   Agents for respective use case

2. Update the contact inbound flow.
   1. Remove the GetCustomerInput block and add the Connect
      assistant flow block instead
   2. Fill in the flow block config with the AIAssistant ARN and
      select the appropriate AIAGent.

Now you can use this flow as your regular inbound and the Q in connect chat
widget should be able to provide recommendations to help with user’s
request.
