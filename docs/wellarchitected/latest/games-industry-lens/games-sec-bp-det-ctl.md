# Detective controls

| GAMESEC03: How do you monitor and analyze player usage behavior<br>within your game? |
| ------------------------------------------------------------------------------------ |
|                                                                                      |

To maintain a positive player experience, you should have a process for capturing,
storing, and analyzing relevant data that can help you understand how players engage
with your game's features and with other players.

**GAMESEC_BP09: Collect, store, and analyze player usage logs to detect inappropriate behavior.**

Instrument your game to collect logs that help you understand how players use the
features of your game and how they interact with other players so that you can prevent
unauthorized activity which can degrade the player experience. This can be done by
sending structured log events to the [Game Analytics
Pipeline](https://aws.amazon.com/solutions/implementations/game-analytics-pipeline/ "https://aws.amazon.com/solutions/implementations/game-analytics-pipeline/"), or by using a logging solution such as [Amazon CloudWatch
Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md"), [Amazon OpenSearch
Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/"), or a solution from an AWS Partner such as [Datadog](https://www.datadoghq.com/ "https://www.datadoghq.com/"), [Sumo Logic](https://www.sumologic.com/ "https://www.sumologic.com/"), [New Relic](https://newrelic.com/ "https://newrelic.com/"), [Honeycomb](https://www.honeycomb.io/ "https://www.honeycomb.io/"), or [Splunk](https://www.splunk.com/ "https://www.splunk.com/"). These
player usage logs should be structured so that they can be used to detect when speciﬁc
actions by players need to be investigated.

After you have captured the data, you should consider implementing tools to help you
detect inappropriate usage behavior. For example, if your game has social features such
as in-game player messaging and voice chat, or online forums, it is recommended to save
logs from these player engagements in a format that can be analyzed for moderation
purposes. Conﬁgure your game's voice chat feature to export recordings to Amazon S3 and
use [Amazon Transcribe](https://aws.amazon.com/transcribe "https://aws.amazon.com/transcribe") to convert the
audio speech to text format which can be stored for processing. Alternatively, you can
perform real-time streaming transcription by integrating your game backend voice chat
service directly with the Transcribe API to [transcribe streaming audio](../../../transcribe/latest/dg/streaming.md "../../../transcribe/latest/dg/streaming.md") in
real-time. Moderation teams can manually review the content, and once the content is in
a standard format, you can also use AWS AI/ML services to perform moderation
automatically. [Amazon Comprehend](https://aws.amazon.com/comprehend/ "https://aws.amazon.com/comprehend/") can
be used to perform natural language processing (NLP) to uncover information from the
unstructured text, which can help you classify and organize the conversations into
relevant topics and identify inappropriate behavior such as profanity.

If your game allows players to generate or upload content, consider using [Amazon Rekognition](https://aws.amazon.com/rekognition/ "https://aws.amazon.com/rekognition/") to identify the content
of the images for moderation. For video use cases such as player live streaming, you can
send video streams to [Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/?amazon-kinesis-video-streams-resources-blog.sort-by=item.additionalFields.createdDate&amazon-kinesis-video-streams-resources-blog.sort-order=desc "https://aws.amazon.com/kinesis/video-streams/?amazon-kinesis-video-streams-resources-blog.sort-by=item.additionalFields.createdDate&amazon-kinesis-video-streams-resources-blog.sort-order=desc") which you can integrate with [Amazon Rekognition Video](https://aws.amazon.com/rekognition/video-features "https://aws.amazon.com/rekognition/video-features") or
your own custom application to analyze and moderate in real-time. Your game may provide
players with the ability to contact player support agents through a call center such as
[Amazon Connect](https://aws.amazon.com/connect/ "https://aws.amazon.com/connect/"), or chat bots using
Amazon Lex. Amazon Connect provides support for [monitoring live and
recorded conversations](../../../connect/latest/adminguide/monitoring-amazon-connect.md "../../../connect/latest/adminguide/monitoring-amazon-connect.md"). To analyze interactions between players and player
support chat bots built with Amazon Lex, you can store the [conversation logs](../../../lex/latest/dg/conversation-logs-cw.md "../../../lex/latest/dg/conversation-logs-cw.md") from these
interactions in Amazon CloudWatch Logs which can be exported to S3 and analyzed as
described previously.

You can also integrate your game with [Amazon Fraud Detector](https://aws.amazon.com/fraud-detector/ "https://aws.amazon.com/fraud-detector/"), a fully managed service that uses machine learning to identify potentially fraudulent activity so customers can catch online fraud quickly. You can use Fraud Detector to detect potentially fraudulent activity and flag that activity for review so that you can prevent fraudulent in-game purchases in real-time, detect compromised accounts by looking for behavioral changes and anomalies, and distinguish between legitimate and high-risk new account registrations.

[Amazon Lookout for Metrics](https://aws.amazon.com/lookout-for-metrics/ "https://aws.amazon.com/lookout-for-metrics/")
uses machine learning to automatically detect and diagnose anomalies in your business
and operational data, and monitors the metrics that are most important to your
businesses with greater speed and accuracy. The service also makes it easier to diagnose
the root cause of anomalies such as sudden dips in revenue, logins, transactions, and
retention. It does not require game developers to have any ML experience to setup and
can connect to popular data sources including Amazon S3, Amazon CloudWatch, Amazon RDS,
Amazon Redshift, as well as many SaaS applications. For example, you can [integrate Amazon Lookout for Metrics with the Game Analytics Pipeline](https://aws.amazon.com/blogs/gametech/detect-game-anomalies-amazon-lookout-for-metrics-game-analytics-pipeline/ "https://aws.amazon.com/blogs/gametech/detect-game-anomalies-amazon-lookout-for-metrics-game-analytics-pipeline/") and
other data sources to begin analyzing behavior to detect anomalies.

Alternatively, you may choose to build, train, and host a custom machine learning model using
[Amazon SageMaker](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/")
to address use cases such as content moderation, toxicity detection, cheat detection, fraud detection, and more.

In addition to generating custom game usage logs, it is also recommended to capture
and store system-level logs from relevant services, such as [S3 server access logs](../../../AmazonS3/latest/userguide/ServerLogs.md "../../../AmazonS3/latest/userguide/ServerLogs.md"), [CloudFront access logs](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md"), and [ALB
access logs](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md"). These logs can be stored in an Amazon S3 bucket in your account
and are useful for associating your player usage information from within the game with
system-level information including connection details such as IP addresses, request
headers, and any relevant request manipulation and filtering that you may have
configured within your game backend. These logs can be sent to the same logging
solutions mentioned earlier, and can also be [analyzed using SQL queries
with Amazon Athena](../../../athena/latest/ug/application-load-balancer-logs.md "../../../athena/latest/ug/application-load-balancer-logs.md") without requiring the logs to be moved out of Amazon S3.

[Access Analyzer for S3](../../../AmazonS3/latest/userguide/access-analyzer.md "../../../AmazonS3/latest/userguide/access-analyzer.md")
is a feature that monitors your bucket access policies, ensuring that the policies provide only the intended access to your S3 resources. Access Analyzer for S3 evaluates your bucket access policies and allows you to discover and swiftly remediate buckets with potentially unintended access.

To continuously monitor for malicious activities and unauthorized behaviors within
your AWS environment, consider using [Amazon
GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/"). GuardDuty identifies threats by monitoring account behavior,
network activity, and data access patterns within your environment. It analyzes tens of
billions of events across multiple data sources, such as CloudTrail event logs, Amazon
VPC Flow Logs, and DNS logs for potential threats. By integrating with Amazon CloudWatch
Events and Lambda, GuardDuty alerts can be automatically forwarded to relevant security
teams for further analysis.

[AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") provides a
comprehensive view of your security state in AWS and helps you to check your
environment against security industry standards and best practices. Security Hub
collects security data from across AWS accounts, services, and supported third-party
partner products and helps you to analyze your security trends and identify the highest
priority security issues. The [Amazon GuardDuty integration with Security Hub](../../../securityhub/latest/userguide/securityhub-internal-providers.md "../../../securityhub/latest/userguide/securityhub-internal-providers.md") enables
you to send findings from GuardDuty to Security Hub. Security Hub can then include those
findings in its analysis of your security posture.

It’s common for bad actors to employ bots to take over accounts and cheat in games.
[WAF Bot Control](https://aws.amazon.com/waf/features/bot-control/ "https://aws.amazon.com/waf/features/bot-control/")
gives you visibility and control over common and pervasive bot traffic that can consume excess resources, skew metrics, cause downtime, or perform other undesired activities.

Ransomware is malicious code designed to gain unauthorized access to systems and
datasets and encrypt that data to block access by legitimate players. After ransomware
has locked players out of their systems and encrypted their sensitive data, cyber
criminals demand a ransom before providing a decryption key to unlock the data.
Organizations can be completely shut down by an attack, incurring significant costs and
loss of business productivity. Refer to [Securing
your Cloud Environment from Ransomware](https://d1.awsstatic.com/WWPS/pdf/AWSPS_ransomware_ebook_Apr-2020.pdf "https://d1.awsstatic.com/WWPS/pdf/AWSPS_ransomware_ebook_Apr-2020.pdf") for best practices you can apply to
strengthen your ability to fight ransomware before, during, and after an incident takes
place.

Refer to the Well-Architected Framework whitepaper for additional best practices in the detective controls area for security.
