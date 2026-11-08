

# Using the AWS assistant
<a name="using-assistant"></a>

Use the AWS assistant to ask about AWS architecture, services, recommended practices, and documentation. In the AWS Management Console, you can also ask about your resources, costs, telemetry, and operations. The following topics say where each capability is available.

**Topics**
+ [Manage console conversations](#manage-conversations)
+ [Navigate the chat panel](#navigate-panel)
+ [Chat settings](#chat-settings)
+ [Use visualizations](#visual-responses)
+ [Use the prompt library](#prompt-library)
+ [Chatting about your AWS resources](resources.md)
+ [Chatting about your AWS costs](costs.md)
+ [Using service-specific insights](service-insights.md)
+ [Using plugins with the AWS assistant](plugins.md)
+ [Diagnosing console errors with the AWS assistant](diagnose-errors.md)
+ [Contacting AWS Support with the AWS assistant](support.md)

## Manage console conversations
<a name="manage-conversations"></a>

The AWS assistant maintains the questions and responses in a conversation as context for later responses. You can save up to 80 conversations in the AWS Management Console.

To start a new conversation, choose the plus icon (\+) in the chat panel header. To name a conversation, choose the conversation name field and enter a name. If you don't name it, the AWS assistant generates a title from the selected prompt or the first questions in the conversation.

To switch conversations, choose the clock icon in the chat panel header. The **Conversations** pop-up opens. Choose the conversation that you want to resume. To delete a conversation, choose the delete icon next to its name.

The AWS assistant deletes a conversation when you don't ask a new question in it for 90 days. It also deletes messages older than 90 days, even when the conversation remains active. In the AWS Management Console, the AWS assistant keeps your current conversation and context when you navigate to another console page or browser tab. In the AWS Console Mobile Application, navigating to a new page starts a conversation without the previous context.

## Navigate the chat panel
<a name="navigate-panel"></a>
+ To expand the panel to full screen, choose the maximize icon in the chat panel header. To exit full-screen mode, choose the resize icon.
+ Use the divider to adjust the panel width.
+ To close the panel, choose < in the chat panel header. To close the panel with visualizations, choose X. To reopen the panel, choose the AWS assistant icon in the navigation bar.
+ Your work is saved when you switch between the assistant and service console views.

## Chat settings
<a name="chat-settings"></a>

To view chat settings, choose the gear icon in the chat panel header. When you open the panel in the AWS Management Console, the AWS assistant uses the AWS Region that is selected on the console for resource questions, unless you specify another Region. To use a different Region, change the console Region or specify a Region in your prompt. The console Region doesn't determine where the AWS assistant processes your requests. For more information, see [Cross-Region processing in the AWS assistant](cross-region-processing.md).

## Use visualizations
<a name="visual-responses"></a>

With the AWS assistant, you can get responses that include visualizations, such as tables, charts, dashboards, time series graphs, and key-value pairs. When you ask a natural language question about resources or costs, the AWS assistant determines whether a visual response would be useful. It opens the visual response in a panel next to the conversation.

Resource tables can group resources by requested properties and include deep links to their pages in the applicable service console. Cost responses can include chart widgets for historical costs, forecasts, pricing, budgets, coverage, and utilization. You can paginate, filter, and sort results directly within the response.

**Note**  
All data associated with AWS assistant visualizations is stored in US East (N. Virginia).

Example visualization prompts include:
+ List my running EC2 instances.
+ Create a chart of my costs by Region last month.
+ Show me a bar chart of potential savings by optimization recommendation.
+ Check traffic and internet accessibility to EC2 resources.

## Use the prompt library
<a name="prompt-library"></a>

The AWS assistant recommends prompts when you start a conversation. To browse supported prompts, choose the book icon in the chat panel header. You can filter prompts by table or visualization response type.

Other example prompts include:
+ List RDS databases without Amazon CloudWatch alarms.
+ When should I put my resources in a VPC?
+ Which container service should I use for a workload when I need to keep costs low?
+ Create a short AWS Command Line Interface (AWS CLI) script to list my AWS Lambda functions.