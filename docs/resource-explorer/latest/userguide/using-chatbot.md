

# Using Amazon Q Developer in chat applications to search for resources
<a name="using-chatbot"></a>

You can search and discover information about AWS services and your AWS resources by asking Amazon Q Developer in chat applications natural language questions. Amazon Q Developer in chat applications answers service-related questions directly in your chat channels with relevant AWS documentation and support article excerpts. Amazon Q Developer in chat applications uses Resource Explorer to search and find answers to your resource related questions.

For more information, see [What is Amazon Q Developer in chat applications?](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) in the *Amazon Q Developer in chat applications Administrator Guide*.

## AWS resource questions
<a name="resource-questions"></a>

Amazon Q Developer in chat applications uses Resource Explorer to search and discover your resources. Amazon Q Developer in chat applications displays these search results in a list. This list shows the top five matching resources and includes the ability to filter results further by resource type, AWS Region, and tag.

### Prerequisites
<a name="prerequisites"></a>

To ask Amazon Q Developer in chat applications resource related questions you must:
+ Make sure you have active indexes and views with at least one default view in your AWS Region. Indexes and views allow Resource Explorer to catalog and query your resources. See [Terms and concepts for Resource Explorer](getting-started-terms-and-concepts.md) for more information.
+ Add the AWSResourceExplorerReadOnlyAccess policy to your channel role or each appropriate user role, depending on your channel's permission scheme.
+ Verify that your channel guardrail policies allow AWSResourceExplorerReadOnlyAccess permissions.

### Commonly asked resource questions
<a name="commonly-asked-resource-questions"></a>

You can ask these questions directly from your chat channels. Replace the words with red text with your own information.

`@aws What services am I using in {{Region}}?`

`@aws What are the resources in my account with {{tags}}?`

`@aws What lambda functions do I have?`