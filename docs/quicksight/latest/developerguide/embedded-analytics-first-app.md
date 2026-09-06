

# Create your first embedding application
<a name="embedded-analytics-first-app"></a>

The quickest and most flexible way to embed a dashboard in your web application is to get an embed URL through the Quick Sight API and load that onto your application using the Quick Sight [Embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk), in an iFrame. To do so, you will need: 
+ A backend service to generate the embed URL 
+ An endpoint to pass the embed url to your front end application 
+ (Optional) A Javascript-based front-end application that leverages the embedding SDK to load the dashboard within an iFrame
+ (Optional) Front-end methods to customize and integrate with the embedded dashboard seamlessly with your application using functions in the embedding SDK

To embed a dashboard in a React application, see [this example](https://aws.amazon.com/blogs/business-intelligence/level-up-your-react-app-with-amazon-quicksight-how-to-embed-your-dashboard-for-anonymous-access/).

To set up your first embedded dashboard, see [Embedding Quick Sight data dashboards for registered users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-dashboards-for-authenticated-users.html). 

To set up a different kind of embedded asset, shooce one of the following options:

**Embedding options for registered users**
+ [Embedding Quick Sight visuals for registered users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-visuals-for-authenticated-users.html)
+ [Embed the full functionality of the Quick Sight console for registered users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-full-console-for-authenticated-users.html)
+ [Embed the Generative Q&A experience for registered users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-gen-bi-authenticated-users.html)

**Embedding options for anonymous (unregistered) users**
+ [Embed data dashboards for anonymous (unregistered) users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-dashboards-for-everyone.html)
+ [Embed visuals for anonymous (unregistered) users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-visuals-for-everyone.html)
+ [Embed the Generative Q&A experience for anonymous (unregistered) users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-gen-bi-anonymous-users.html)

**1-click embedding options**
+ [Turn on public access to visuals and dashboards with a 1-click embed code](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-1-click-public.html)
+ [Embedding visuals and dashboards for registered users with a 1-click embed code](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-1-click.html)