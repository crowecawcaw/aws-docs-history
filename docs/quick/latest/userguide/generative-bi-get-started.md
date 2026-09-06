

# Get started with Generative BI
<a name="generative-bi-get-started"></a>

To get started with Quick Sight Generative BI capabilities, upgrade your account's users to Admin Pro, Author Pro, or Reader Pro roles. Pro roles grant users access to all Generative BI capabilities that are relevant to the role that's assigned to the user. Pro users can share generative Q&A legacy Topics with another user. To understand which Generative BI capabilities are available to the different user roles in Quick, see the table below. To understand how subscription names map to user roles, see [Understanding Amazon Quick subscriptions and roles](https://docs.aws.amazon.com/quicksight/latest/user/user-types.html#subscription-role-mapping).

**Note**  
Non-Pro Authors and Readers can still access Generative Q&A legacy Topics if an Author Pro or Admin Pro user shares the legacy Topic with them. Non-Pro Authors and Readers can also access data stories if a Reader Pro, Author Pro, or Admin Pro shares one with them.


| Feature name | Feature description | Reader | Author | Admin | Reader Pro | Author Pro | Admin Pro | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| [Creating a data story with Generative BI](working-with-stories-create.md) | Build data stories that explain your data with visuals, insights, and ideas to help improve your business. | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| [Viewing a generated data story in Amazon Quick Sight](working-with-stories-view.md) | View narrative data stories that are shared with you. | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes\* | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes\* | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes\* | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| [Authoring Q&A](gen-bi-author-q-and-a.md) | Create and refine legacy Topics that utilize Generative Q&A for Quick Sight dashboards. | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| [Asking and answering questions of data with Generative BI](gen-bi-data-q-and-a.md) | Ask questions about data to accelerate data driven decisions with multi-visual answers. | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes\* | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes\* | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes\* | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| [Creating executive summaries](gen-bi-executive-summaries.md) | Get an executive summary of key insights from a Quick Sight dashboard. | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| [The Generative BI authoring experience](generative-bi-author-experience.md) | Create an analysis to build visuals, calculations, and refine existing visuals with natural language. | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 

\*Non-pro roles in accounts that were created on or after April 30, 2024 can access Q&A legacy Topics that are shared with them. If your Quick account was created before April 30, 2024 and you want to opt-in to this new feature, contct your AWS account team. 

Any Quick administrator can upgrade a user to a Pro role with the following procedure.

**To upgrade a user to a Pro role**

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. Choose the user icon at the top right, and then choose **Manage Quick**.

1. Choose **Manage users** to open the **Manage Users** page.

1. To change the role of an existing user, locate that user on the **Manage Users** table and choose the role that you want to grant them from the **Role** dropdown.

For more information about managing Quick users, see [Managing user access inside Amazon Quick](managing-users.md).