# Integrate Incident Detection and Response with Amazon CloudWatch

AWS Incident Detection and Response uses the service-linked role (SLR) that you turned on during access provisioning to create an Amazon EventBridge-managed rule in your AWS account named `AWSHealthEventProcessor-DO-NOT-DELETE`. Incident Detection and Response uses this rule to ingest Amazon CloudWatch alarms from your accounts. Additional steps aren't required to ingest alarms from CloudWatch.
