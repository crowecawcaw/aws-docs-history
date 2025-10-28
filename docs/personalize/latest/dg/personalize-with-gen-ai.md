# Amazon Personalize and generative AI

Amazon Personalize works well with generative artificial intelligence (generative AI). Amazon Personalize Content Generator, with the help
of generative AI, can add engaging themes to batch recommendations for related items.
_Content Generator_ is a generative AI capability managed by Amazon Personalize.

You can also use Amazon Personalize recommendations to integrate Amazon Personalize with your generative AI workflow and enhance your users'
experience. For example, you can add recommendations to generative AI prompts to create marketing content tailored to each of
your user's interests. You can also generate concise summaries for recommended content, or recommend products or content
through chat bots.

The following video shows how you can enhance recommendations with Amazon Personalize and generative AI.

The following Amazon Personalize features use generative AI or can help you build generative AI solutions that create personalized
content. For sample Jupyter notebooks that show how to use Amazon Personalize with generative AI, see [Generative AI with
Amazon Personalize](https://github.com/aws-samples/amazon-personalize-samples/tree/master/next_steps/generative_ai "https://github.com/aws-samples/amazon-personalize-samples/tree/master/next_steps/generative_ai") in the [Amazon Personalize samples](https://github.com/aws-samples/amazon-personalize-samples "https://github.com/aws-samples/amazon-personalize-samples")
repository.

###### Topics

- [Recommendations with themes from Content Generator](#gen-ai-themed-rec "#gen-ai-themed-rec")
- [Recommendation metadata](#gen-ai-metadata "#gen-ai-metadata")
- [Pre-configured LangChain code for personalization](#gen-ai-langchain "#gen-ai-langchain")

## Recommendations with themes from Content Generator

Amazon Personalize Content Generator can add descriptive themes to batch recommendations.
_Content Generator_ is a generative AI
capability managed by Amazon Personalize.

When you get batch recommendations with themes, Amazon Personalize Content Generator adds a descriptive theme for each set of similar items. For example, if you get similar items
recommendations for a breakfast food item, Amazon Personalize might generate a theme like _Rise and shine_ or _Morning essentials_.
You might use the theme to replace a generic carousel title, like _Frequently bought together_. Or you
might incorporate the theme in a promotional email or marketing campaign for new menu options.

To generate themes, you import data into Item interactions and Items datasets, create a custom solution with the
Similar-Items recipe, and generate batch recommendations. Your item data must include item description and title
information. Detailed item descriptions and titles help Content Generator create more accurate and engaging themes.

- For information about the Amazon Personalize workflow, see [Amazon Personalize workflow details](personalize-workflow.md "personalize-workflow.md").
- For information about batch recommendations, see [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").
- For information about generating item recommendations with themes, see [Batch recommendations with themes from Content Generator](themed-batch-recommendations.md "themed-batch-recommendations.md").

## Recommendation metadata

When you get recommendations, you can have Amazon Personalize return metadata about each recommended item from your Items dataset.
You can add this metadata, along with Amazon Personalize recommendations, to your generative AI prompts to generate more compelling
content.

For example, you might use generative AI to create marketing emails. You can use Amazon Personalize recommendations and their
metadata, such as movie genres, as part of prompt engineering for generative AI. With personalized prompts, you can use
generative AI to create engaging marketing emails tailored to each of your customer's interests.

To get recommendation metadata, you first complete the Amazon Personalize workflow to import data and create domain or custom
resources. When you create an Amazon Personalize _recommender_ or a _campaign_, enable the option to include
metadata in recommendations. When you get recommendations, you can specify which columns of item data you want to include.

- For information about the Amazon Personalize workflow, see [Amazon Personalize workflow details](personalize-workflow.md "personalize-workflow.md").
- For information about enabling metadata for a recommender, see [Enabling
  metadata in recommendations (domain resources)](create-recommender-return-metadata.md "create-recommender-return-metadata.md").
- For information about enabling metadata for a campaign, see [Enabling
  metadata in recommendations (custom resources)](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").
- For more information about how you can use Amazon Personalize with generative AI to create marketing campaigns, see [Elevate your marketing solutions with Amazon Personalize and generative AI](https://aws.amazon.com/blogs/machine-learning/elevate-your-marketing-solutions-with-amazon-personalize-and-generative-ai/ "https://aws.amazon.com/blogs/machine-learning/elevate-your-marketing-solutions-with-amazon-personalize-and-generative-ai/").

## Pre-configured LangChain code for personalization

LangChain is a framework for developing applications powered by language models. It features code built for Amazon Personalize. You
can use this code to integrate Amazon Personalize recommendations with your generative AI solution.

For example, you can use the following code to add Amazon Personalize recommendations for a user to your chain.

```
from aws_langchain import AmazonPersonalize
from aws_langchain import AmazonPersonalizeChain
from langchain.llms.bedrock import Bedrock

recommender_arn="`RECOMMENDER ARN`"

bedrock_llm = Bedrock(model_id="anthropic.claude-v2", region_name="us-west-2")
client=AmazonPersonalize(credentials_profile_name="default",region_name="us-west-2",recommender_arn=recommender_arn)
# Create personalize chain
# Use return_direct=True if you do not want summary
chain = AmazonPersonalizeChain.from_llm(
    llm=bedrock_llm,
    client=client,
    return_direct=False
)
response = chain({'user_id': '1'})
print(response)
```

- For information about getting started with LangChain, see the [Introduction](https://python.langchain.com/v0.2/docs/introduction/ "https://python.langchain.com/v0.2/docs/introduction/") in the LangChain documentation.
- For information about using LangChain code built for Amazon Personalize, including more advanced code samples, see [Amazon Personalize LangChain extensions](https://github.com/aws-samples/amazon-personalize-langchain-extensions "https://github.com/aws-samples/amazon-personalize-langchain-extensions") in the [AWS samples](https://github.com/aws-samples/ "https://github.com/aws-samples/") repository.
