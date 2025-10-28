# Create a schedule for an existing crawler

Follow these steps to set up a recurring schedule for an existing crawler.

AWS Management Console1. Sign in to the AWS Management Console and open the AWS Glue console at
[https://console.aws.amazon.com/glue/](<https://console.aws.amazon.com/glue\ "https://console.aws.amazon.com/glue">). 2. Choose **Crawlers** in the navigation
pane. 3. Choose a crawler that you want to schedule from the available list. 4. Choose **Edit** from the **Actions menu.** 5. Scroll down to **Step 4: Set output and scheduling**, and choose **Edit**. 6. Update your crawler schedule under **Crawler schedule**. 7. Choose **Update**.

AWS CLI
Use the following CLI command to update an existing crawler configuration:

```
aws glue update-crawler-schedule
   --crawler-name `myCrawler`
   --schedule `cron(15 12 * * ? *)`

```
