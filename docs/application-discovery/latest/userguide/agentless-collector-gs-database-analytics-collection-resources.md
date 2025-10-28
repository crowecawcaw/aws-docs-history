AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Creating the AWS DMS data collector

Your database and analytics data collection module uses an AWS DMS data collector to
interact with the AWS DMS console. You can view the collected data in the AWS DMS console,
or use it to determine the right-sized AWS target engine. For more information, see
[Using
the AWS DMS Fleet Advisor Target Recommendations feature](../../../dms/latest/userguide/fa-recommendations.md "../../../dms/latest/userguide/fa-recommendations.md").

Before you create an AWS DMS data collector, create an IAM role that your AWS DMS data
collector uses to access your Amazon S3 bucket. You created this Amazon S3 bucket when you
completed the prerequisites in [Prerequisites for
Agentless Collector](agentless-collector-gs-prerequisites.md "agentless-collector-gs-prerequisites.md").

###### To create an IAM role for your AWS DMS data collector to access Amazon S3

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, then choose
   **Create role**.
3. On the **Select trusted entity** page, for **Trusted
   entity type**, choose **AWS Service**. For
   **Use cases for other AWS services**, choose
   **DMS**.
4. Select the **DMS** check box and choose
   **Next**.
5. On the **Add permissions** page, choose
   **FleetAdvisorS3Policy** that you created before. Choose
   **Next**.
6. On the **Name, review, and create** page, enter
   `FleetAdvisorS3Role` for **Role
   name**, then choose **Create role**.
7. Open the role that you created, and choose the **Trust
   relationships** tab. Choose **Edit trust
   policy**.
8. On the **Edit trust policy** page, paste the following JSON
   into the editor, replacing the existing code.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "dms.amazonaws.com",
 "dms-fleet-advisor.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }]
}`

```

9. Choose **Update policy**.
   Now, create a data collector in the AWS DMS console.

###### To create an AWS DMS data collector

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose the AWS Region that you set as your Migration Hub home Region. For more
   information, see [Sign in to Migration Hub and
   choose a home Region](setting-up.md#setting-up-choose-home-region "setting-up.md#setting-up-choose-home-region").
3. In the navigation pane, choose **Data collectors** under
   **Discover**. The **Data collectors** page
   opens.
4. Choose **Create data collector**. The **Create data
   collector** page opens.
5. For **Name** in the **General
   configuration** section, enter a name of your data
   collector.
6. In the **Connectivity** section, choose **Browse
   S3**. Choose the Amazon S3 bucket that you created before from the
   list.
7. For **IAM role**, choose `FleetAdvisorS3Role`
   that you created before.
8. Choose **Create data collector**.
