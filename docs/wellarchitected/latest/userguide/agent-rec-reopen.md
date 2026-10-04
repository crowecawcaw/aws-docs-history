

AWS Well-Architected Agent is in preview release and is subject to change.

# Reopen recommendations in AWS Well-Architected Agent
<a name="agent-rec-reopen"></a>

You can reopen recommendations that are marked as complete or suppressed. Reopened recommendations return to your recommendations list and follow the regularly scheduled refresh cycle.

**To reopen a recommendation**

1. In the AWS WA Agent dashboard, choose **View archived recommendations**.

1. Locate the recommendation that you want to reopen from the recommendations list.

1. Choose the recommendation to view its details page.

1. In the recommendation details page, choose **Reopen**.

1. In the confirmation dialog, review the recommendation details and choose **Reopen** to confirm.

After you reopen a recommendation, AWS WA Agent displays a confirmation message indicating that the recommendation has been reopened and will follow the regularly scheduled refresh cycle. The recommendation returns to your recommendations list where you can view updated details, impacts, and guided actions based on your current AWS environment.

**Note**  
When you reopen a recommendation, AWS WA Agent analyzes your current AWS environment to provide updated insights and impact calculations. The reopened recommendation may show different details than when it was originally generated if your infrastructure has changed.