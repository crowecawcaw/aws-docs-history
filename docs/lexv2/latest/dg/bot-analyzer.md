

# Optimize Bot using AI-powered Bot Analyzer
<a name="bot-analyzer"></a>

Analyze your Amazon Lex V2 bot configuration against AWS best practices using AI-powered recommendations. Bot Analyzer uses Amazon Bedrock's generative AI capabilities to identify configuration issues and provide actionable guidance to improve intent classification and slot resolution performance.

Bot Analyzer automatically evaluates your bot's intent configurations and provides recommendations to:
+ **Improve intent separation** - Identify and resolve generic intents that group multiple concepts
+ **Eliminate intent overlap** - Detect similar meanings and phrasings between intents that cause routing errors
+ **Optimize slot usage** - Recommend proper use of slots to combine similar intents and improve entity extraction
+ **Enhance utterance quality** - Analyze sample utterance coverage and diversity for better intent classification

Before using Bot Analyzer, ensure:
+ Your bot locale is built successfully
+ Your bot version for analysis is `DRAFT`
+ Your bot locale is one of the supported English locales: `en_AU`, `en_GB`, `en_IN`, `en_US`, `en_ZA`

You can use Bot Analyzer with either the console or the API.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home).

1. Select your bot and navigate to the bot locale you want to analyze.

1. In the bot locale editor, click the **Analyze** dropdown menu.

1. Select **Start** to begin the analysis.

![Analyze dropdown with Start option](http://docs.aws.amazon.com/lexv2/latest/dg/images/bot-analyzer/analyze-dropdown-start.jpeg)


The analysis typically completes within minutes. During analysis, the **Start** button changes to **Stop Analyzing** if you need to cancel.

Once analysis completes, recommendations appear in the **Recommendations** panel on the right side.

![Recommendations panel](http://docs.aws.amazon.com/lexv2/latest/dg/images/bot-analyzer/recommendations-panel.jpeg)


Each recommendation includes:
+ **Priority** - High, Medium, or Low severity
+ **Issue Location** - The specific intent affected
+ **Issue Description** - What configuration problem was detected
+ **Proposed Fix** - Actionable steps to resolve the issue

To see previous analyses:

1. Click the **Analyze** dropdown menu.

1. Select **History**.

1. The **Analysis History** panel displays past analysis requests with their status and timestamps.

![Analysis History panel](http://docs.aws.amazon.com/lexv2/latest/dg/images/bot-analyzer/analysis-history-panel.png)


To remove analysis results:

1. Click the **Analyze** dropdown menu.

1. Select **Delete**.

1. Confirm deletion of the current recommendations.

![Delete confirmation dialog](http://docs.aws.amazon.com/lexv2/latest/dg/images/bot-analyzer/delete-confirmation.png)


------
#### [ API ]

Send a `StartBotAnalyzer` request to initiate analysis for your bot locale. The response returns an HTTP 202 status with a `botAnalyzerRequestId`. Take note of this ID and you'll need it to check the analysis status and retrieve recommendations.

Send a `DescribeBotAnalyzerRecommendation` request using the `botAnalyzerRequestId` from the previous step. Include the `botId` in the request path.

If the `botAnalyzerStatus` in the response is `Available`, the analysis is complete and the `botAnalyzerRecommendationList` field will be populated with recommendations. Each recommendation includes:
+ `issueLocation` - The location where the issue was detected
+ `priority` - High, Medium, or Low severity
+ `issueDescription` - Details about the configuration problem
+ `proposedFix` - Actionable guidance to resolve the issue

If you need to cancel an analysis in progress, send a `StopBotAnalyzer` request with the `botId` and `botAnalyzerRequestId`.

To retrieve a list of previous analyses for a bot locale, send a `ListBotAnalyzerHistory` request. Specify the `botId` and `localeId` to see all past analysis requests with their status and timestamps.

To remove analysis results, send a `DeleteBotAnalyzerRecommendation` request with the `botId` and `botAnalyzerRequestId`. This permanently deletes the recommendations associated with that analysis.

**Note**  
Recommendations are automatically deleted after 15 days.

------
+ [Best practices for creating Amazon Lex interaction models](https://aws.amazon.com/blogs/machine-learning/best-practices-for-creating-amazon-lex-interaction-models/)
+ [Improve intent classification and slot resolution in Lex V2 with assisted NLU](assisted-nlu.md)
+ [Using assisted slot resolution to clarify slot values in Amazon Lex V2](assisted-slot.md)