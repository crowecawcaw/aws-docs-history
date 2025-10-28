# AWS Incident Detection and Response monitoring and observability

AWS Incident Detection and Response offers you expert guidance on defining observability across your workloads from the application layer to the underlying infrastructure.
Monitoring tells you that something is wrong. Observability uses data collection to tell you what is wrong and why it happened.

The Incident Detection and Response system monitors your AWS workloads for failures and performance degradation by leveraging
native AWS services such as Amazon CloudWatch and Amazon EventBridge to detect events that may impact your workload. Monitoring provides
you notification of imminent, on-going, receding, or potential failures or of performance degradation. When you onboard your account to Incident Detection and Response, you
select which alarms in your account should be monitored by the Incident Detection and Response monitoring
system and you associate those alarms with an application and a runbook used during incident management.

Incident Detection and Response uses Amazon CloudWatch and other AWS services to build your observability solution. AWS Incident Detection and Response helps you with observability in two ways:

- **Business Outcome metrics**: Observability on AWS Incident Detection and Response starts with defining the key metrics that monitor the
  outcomes of your workloads or end-user experience. AWS experts work with you to understand the objectives of your workload, the key
  outputs or factors that may impact user-experience, and to define the metrics and alerts that capture any degradation in those key metrics.
  For example a key business metric for a mobile calling application is the _Call Setup Success Rate_ (monitors the success rate of user call attempts),
  and a key metric for a website is _page speed_. Incident engagement is triggered based on business outcome metrics.
- **Infrastructure level metrics**: At this stage, we identify the underlying AWS services and infrastructure supporting your application and define
  metrics and alarms to track the performance of these infrastructure services. These may include
  metrics such as `ApplicationLoadBalancerErrorCount` for Application Load Balancer instances. This starts after the workload has been onboarded and monitoring set up.

## Implementing observability on AWS Incident Detection and Response

Because observability is a continuous process that may not be completed in one exercise or time frame, AWS Incident Detection and Response implements observability in two phases:

- **Onboarding phase**: Observability during onboarding is focused on detecting when the business outcomes of your application are impaired.
  To this end, observability during the onboarding phase is focused on defining the key business outcome metrics at the application layer to notify
  AWS of disruptions to your workloads. This way AWS can promptly respond to these disruption and provide you help toward recovery.
- **Post-onboarding phase**: AWS Incident Detection and Response offers a number of proactive services for observability including the definition of infrastructure
  level metrics, metric tuning, and setting up traces and logs depending, on the maturity level of the customer. The implementation of these services
  may span several months and involve multiple teams. AWS Incident Detection and Response provides guidance on observability setup and customers
  are required to implement the required changes in their workload environment. For help with hands-on implementation of observability
  features, raise a request to your technical account managers (TAMs).
