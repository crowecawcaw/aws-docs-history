# MLSEC-13: Monitor human interactions with data for anomalous activity

Ensure that data access logging is enabled. Audit for
anomalous data access events, such as access events from
abnormal locations, or activity exceeding the baseline for
that entity. Use services and tools that support anomalous
activity alerting, and combine their use with data
classification to assess risk. Evaluate using services to aid
in monitoring data access events.

## Implementation plan

- **Enable data access
  logging** - Verify that you have data access
  logging for all human CRUD (create, read, update, and
  delete) operations, including the details of who
  accessed what elements, what action they took, and at
  what time.
- **Classify your data** -
  Use
  [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/") for protecting and classifying training and
  inference data in
  [Amazon S3](https://aws.amazon.com/pm/serv-s3/?trk=ps_a134p000004f2aOAAQ&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_US&sc_publisher=Google&sc_category=Storage&sc_country=US&sc_geo=NAMER&sc_outcome=acq&sc_detail=amazon%20s3&sc_content=S3_e&sc_matchtype=e&sc_segment=488982706722&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CStorage%7CS3%7CUS%7CEN%7CText&s_kwcid=AL!4422!3!488982706722!e!!g!!amazon%20s3&ef_id=EAIaIQobChMItci3jY-78gIVkOCzCh3rmQRFEAAYASAAEgJcJvD_BwE%3AG%3As&s_kwcid=AL!4422!3!488982706722!e!!g!!amazon%20s3 "https://aws.amazon.com/pm/serv-s3/?trk=ps_a134p000004f2aOAAQ&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_US&sc_publisher=Google&sc_category=Storage&sc_country=US&sc_geo=NAMER&sc_outcome=acq&sc_detail=amazon%20s3&sc_content=S3_e&sc_matchtype=e&sc_segment=488982706722&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CStorage%7CS3%7CUS%7CEN%7CText&s_kwcid=AL!4422!3!488982706722!e!!g!!amazon%20s3&ef_id=EAIaIQobChMItci3jY-78gIVkOCzCh3rmQRFEAAYASAAEgJcJvD_BwE%3AG%3As&s_kwcid=AL!4422!3!488982706722!e!!g!!amazon%20s3"). Amazon Macie is a fully managed security
  service. It uses ML to automatically discover, classify,
  and protect sensitive data in AWS. The service
  recognizes sensitive data, such as personally
  identifiable information (PII) or intellectual property.
- **Monitor and protect** -
  Use
  [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") to monitor for malicious and
  unauthorized activities. This will enable protecting AWS accounts, workloads, and data stored in
  [Amazon S3](https://aws.amazon.com/pm/serv-s3/?trk=ps_a134p000004f2aOAAQ&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_US&sc_publisher=Google&sc_category=Storage&sc_country=US&sc_geo=NAMER&sc_outcome=acq&sc_detail=amazon%20s3&sc_content=S3_e&sc_matchtype=e&sc_segment=488982706722&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CStorage%7CS3%7CUS%7CEN%7CText&s_kwcid=AL!4422!3!488982706722!e!!g!!amazon%20s3&ef_id=EAIaIQobChMItci3jY-78gIVkOCzCh3rmQRFEAAYASAAEgJcJvD_BwE%3AG%3As&s_kwcid=AL!4422!3!488982706722!e!!g!!amazon%20s3 "https://aws.amazon.com/pm/serv-s3/?trk=ps_a134p000004f2aOAAQ&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_US&sc_publisher=Google&sc_category=Storage&sc_country=US&sc_geo=NAMER&sc_outcome=acq&sc_detail=amazon%20s3&sc_content=S3_e&sc_matchtype=e&sc_segment=488982706722&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CStorage%7CS3%7CUS%7CEN%7CText&s_kwcid=AL!4422!3!488982706722!e!!g!!amazon%20s3&ef_id=EAIaIQobChMItci3jY-78gIVkOCzCh3rmQRFEAAYASAAEgJcJvD_BwE%3AG%3As&s_kwcid=AL!4422!3!488982706722!e!!g!!amazon%20s3").

##   Documents

- [Amazon SageMaker AI Incident Response](../../../sagemaker/latest/dg/sagemaker-incident-response.md "../../../sagemaker/latest/dg/sagemaker-incident-response.md") -
  [Logging
  & Monitoring](../../../sagemaker/latest/dg/logging-cloudwatch.md "../../../sagemaker/latest/dg/logging-cloudwatch.md")
- [Amazon GuardDuty S3 Finding Types - which aid in anomaly
  detection for S3 resource access events.](../../../guardduty/latest/ug/guardduty_finding-types-s3.md "../../../guardduty/latest/ug/guardduty_finding-types-s3.md")

## Blogs

- [Building
  a Self-Service, Secure, & Continually Compliant
  Environment on AWS](https://aws.amazon.com/blogs/architecture/building-a-self-service-secure-continually-compliant-environment-on-aws/ "https://aws.amazon.com/blogs/architecture/building-a-self-service-secure-continually-compliant-environment-on-aws/")
- [How
  to Use New Advanced Security Features for Amazon Cognito user pools](https://aws.amazon.com/blogs/security/how-to-use-new-advanced-security-features-for-amazon-cognito-user-pools/ "https://aws.amazon.com/blogs/security/how-to-use-new-advanced-security-features-for-amazon-cognito-user-pools/")
- [Best
  practices for setting up Amazon Macie with AWS Organizations](https://aws.amazon.com/blogs/security/best-practices-for-setting-up-amazon-macie-with-aws-organizations/ "https://aws.amazon.com/blogs/security/best-practices-for-setting-up-amazon-macie-with-aws-organizations/")

## Videos

- [Protect
  Your Data in S3 with Amazon Macie and Amazon GuardDuty -
  AWS Online Tech Talks](https://www.youtube.com/watch?v=lvPT71jAIXk "https://www.youtube.com/watch?v=lvPT71jAIXk")
- [AWS re:Invent 2020: Protecting sensitive data with Amazon Macie and Amazon GuardDuty](https://www.youtube.com/watch?v=h7pq95RMuEQ "https://www.youtube.com/watch?v=h7pq95RMuEQ")

## Examples

- [Controlling
  and auditing data exploration activities with Amazon SageMaker AI Studio and AWS Lake](https://awsfeed.com/whats-new/machine-learning/controlling-and-auditing-data-exploration-activities-with-amazon-sagemaker-studio-and-aws-lake-formation "https://awsfeed.com/whats-new/machine-learning/controlling-and-auditing-data-exploration-activities-with-amazon-sagemaker-studio-and-aws-lake-formation")
  [Formation](https://awsfeed.com/whats-new/machine-learning/controlling-and-auditing-data-exploration-activities-with-amazon-sagemaker-studio-and-aws-lake-formation "https://awsfeed.com/whats-new/machine-learning/controlling-and-auditing-data-exploration-activities-with-amazon-sagemaker-studio-and-aws-lake-formation")
