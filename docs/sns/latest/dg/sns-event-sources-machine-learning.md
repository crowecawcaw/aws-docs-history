

# Machine learning services
<a name="sns-event-sources-machine-learning"></a>

The following table describes how Amazon SNS integrates with AWS machine learning services, such as Amazon CodeGuru, Amazon DevOps Guru, Amazon Lookout for Metrics, Amazon Rekognition, and Amazon SageMaker AI, to provide notifications for anomalies, operational insights, and data labeling activities. 

These integrations allow you to monitor application performance, receive alerts for data irregularities, and streamline the deployment of machine learning models with real-time updates.


| AWS service | Benefit of using with Amazon SNS | 
| --- | --- | 
| [Amazon CodeGuru](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html) – Collects runtime performance data from your live applications, and provides recommendations that can help you fine-tune your application performance. | Receive notifications when anomalies occur. For more information, see [Working with anomalies and recommendation reports](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-recommendation-reports.html) in the *Amazon CodeGuru User Guide*. | 
| [Amazon DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html) – Generates operational insights using machine learning to help you improve the performance of your operational applications. | Forward insights and confirmations. For more information, see [Deliver ML-powered operational insights to your on-call teams using PagerDuty with Amazon DevOps Guru](https://aws.amazon.com/blogs/mt/deliver-ml-powered-operational-insights-to-your-on-call-teams-via-pagerduty-with-amazon-devops-guru/) on the *AWS Management & Governance Blog*. | 
| [Amazon Lookout for Metrics](https://docs.aws.amazon.com/lookoutmetrics/latest/dev/lookoutmetrics-welcome.html) – Finds anomalies in your data, determines their root causes, and enables you to quickly take action. | Receive notifications of anomalies. For more information, see [Using Amazon SNS with Lookout for Metrics](https://docs.aws.amazon.com/lookoutmetrics/latest/dev/services-sns.html) in the *Amazon Lookout for Metrics Developer Guide*. | 
| [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) – Lets you add image and video analysis to your applications | Receive notifications of request results. For more information, see [Reference: Video analysis results notification](https://docs.aws.amazon.com/rekognition/latest/dg/video-notification-payload.html) in the *Amazon Rekognition Developer Guide*. | 
| [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) – Enables data scientists and developers to build and train machine learning models, and then directly deploy them into a production-ready hosted environment. | Receive notifications when a data object is labeled. For more information, see [Creating a streaming labeling job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-create-job.html) in the *Amazon SageMaker AI Developer Guide*. | 