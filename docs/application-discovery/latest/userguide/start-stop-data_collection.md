AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Starting and stopping data collectors in

the AWS Migration Hub console

Application Discovery Service Agentless Collector (Agentless Collector) and AWS Application Discovery Agent
(Discovery Agent) are the data collection tools that AWS Application Discovery Service (Application Discovery Service) uses to help you
discover your existing infrastructure. The following steps explain how to download and
deploy these discovery data collection tools, [Deploy
Agentless Collector](agentless-collector-deploying.md#agentless-collector-gs-deploy "agentless-collector-deploying.md#agentless-collector-gs-deploy") and [AWS Application Discovery Agent](discovery-agent.md "discovery-agent.md").

These data collection tools store their data in the Application Discovery Service's repository, providing
details about each server and the processes running on them. When either of these tools
is deployed, you can start, stop, and view the collected data from the AWS Migration Hub (Migration Hub)
console.

After the AWS Application Discovery Agent (Discovery Agent) is deployed, you can start or stop the data
collection process on the **Data Collectors** page of the AWS Migration Hub
(Migration Hub) console.

###### To start or stop data collection tools

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub console
   at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the Migration Hub console navigation pane under **Discover**,
   choose **Data collectors**.
3. Choose the **Agents** tab.
4. Select the check box of the collection tool you want to start or stop.
5. Choose **Start data collection** or **Stop data
   collection**.
