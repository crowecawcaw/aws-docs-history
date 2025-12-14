# GAMESEC06-BP02 Use artificial intelligence and machine learning

tools to automate aspects of your infrastructure protection
strategy

[Amazon
Lookout for Metrics](https://aws.amazon.com/lookout-for-metrics/ "https://aws.amazon.com/lookout-for-metrics/") uses machine learning to automatically
detect and diagnose anomalies in your business and operational
data and monitors the metrics that are most important to your
businesses with greater speed and accuracy. The service also makes
it straightforward to diagnose the root cause of anomalies, such
as a sudden dip in revenue, logins, transactions, or retention. It
does not require game developers to have ML experience to set up
and can connect to popular data sources including Amazon S3,
Amazon CloudWatch, Amazon RDS, Amazon Redshift, as well as many
SaaS applications. For example, you
can [integrate
Amazon Lookout for Metrics with the Game Analytics
Pipeline](https://aws.amazon.com/blogs/gametech/detect-game-anomalies-amazon-lookout-for-metrics-game-analytics-pipeline/ "https://aws.amazon.com/blogs/gametech/detect-game-anomalies-amazon-lookout-for-metrics-game-analytics-pipeline/") and other data sources to begin analyzing behavior
to detect anomalies.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Alternatively, you may choose to build, train, and host a custom
machine learning model using
[Amazon SageMaker AI AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") to address use cases such as content
moderation, toxicity detection, cheat detection, fraud detection,
and more.

**Customer example**

AnyCompany Games uses Amazon Lookout for Metrics to automatically
detect unusual patterns in server performance, player login
attempts, or transaction volumes that could indicate threats from
bad actors. Additionally, they have used Amazon SageMaker AI to
develop custom machine learning models that continually analyze
network traffic patterns and player behavior to help identify
coordinated threats, such as bot networks that are attempting to
exploit their virtual economy.

This automated approach allows their security team to focus on
investigating and responding to genuine threats rather than
manually monitoring thousands of metrics, while making sure that
emerging threat patterns are detected and addressed before they
can significantly impact game availability or player safety.

### Implementation steps

- Use Amazon Lookout for Metrics to help automatically detect
  and diagnose anomalies in key business and operational data
- Integrate Amazon Lookout for Metrics with data sources like
  the Game Analytics Pipeline, Amazon S3, or CloudWatch to
  monitor metrics such as revenue, logins, and retention.
- Use Amazon SageMaker AI to build, train, and host custom
  machine learning models for advanced use cases like cheat
  detection, fraud prevention, and content moderation.
