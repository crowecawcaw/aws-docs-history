

# Use theme detection in Connect Customer conversational analytics to discover issues with contacts
<a name="use-theme-detection"></a>

Use theme detection to discover previously unknown or emerging contact themes from thousands of customer interactions. For example, you can spot common reasons for customer outreach such as "cancel reservation" or "delayed order." You can then take appropriate actions to improve the customer experience by expediting issue resolution, and improving IVR options, knowledge base articles, and agent training.

## Important things to know
<a name="important-td"></a>
+ Theme detection is available in the following languages supported by Connect Customer conversational analytics:     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/use-theme-detection.html)
+ Theme detection is supported on contacts that were created on or after January 30, 2023.
+ The **Generate themes report** button is enabled only when your saved search contains at least 300 contacts with issues detected by conversational analytics. 
+ The theme detection report is generated for the 3,000 most recent contacts.
+ Theme detection reports are available for 30 days after they are created. After 30 days, the reports are deleted from the database and cannot be retrieved. 
+ The most recent 20 theme reports for a saved search are available in the **View theme reports** dropdown menu, as shown in the following image.  
![The contact search page, the view theme reports dropdown menu.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-view-theme-reports.png)

## How to generate a theme report
<a name="generate-theme-report"></a>

1. Login to Connect Customer using an account that has the following security profile permissions:
   + **Contact search - View**
   + **conversational analytics - theme detection - Create**
   + **conversational analytics - theme detection - View**

1. In Connect Customer, on the left navigation menu, choose **Analytics and optimization**, **Contact search**.

1. On the **Contact search** page, apply filters to select a group of contacts that have been analyzed by conversational analytics.
**Important**  
Your search query must return at least 300 contacts with issues detected by conversational analytics. Otherwise, the **Generate themes report** button is not enabled.

1. Choose **Save search** to save your results. Assign a name to your search.

1. Choose **Generate themes report**.

   Conversational analytics applies machine learning to automatically group contacts with similar issues. When the report is generated, a banner displays a link to the theme report. An example banner is shown in the following image.  
![The contact search page, the theme detection banner.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-theme-detection-banner.png)

1. Choose the link for the theme report.

   The theme report is displayed. It includes theme labels and a list of contacts, as shown in the following image.   
![A theme report with several theme labels.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-theme-detection-drilldown.png)

1. Choose the theme labels to view associated contacts, listen to specific recordings, and read transcripts for deeper analysis.