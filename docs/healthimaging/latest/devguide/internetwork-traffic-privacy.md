# Network traffic privacy

Traffic is protected both between HealthImaging and on-premises applications and between HealthImaging
and Amazon S3. Traffic between HealthImaging and AWS Key Management Service uses HTTPS by default.

- AWS HealthImaging is a regional service available in
  the US East (N. Virginia), US West (Oregon), Europe (Ireland), and Asia Pacific
  (Sydney) Regions.
- For traffic between HealthImaging and Amazon S3 buckets,
  Transport Layer Security (TLS) encrypts objects in-transit between HealthImaging and
  Amazon S3, and between HealthImaging and customer applications accessing it, you should allow
  only encrypted connections over HTTPS (TLS) using the [`aws:SecureTransport condition`](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean") on Amazon S3 bucket IAM
  policies. Although HealthImaging currently uses the public endpoint to access data in
  Amazon S3 buckets, this does not mean that the data traverses the public internet.
  All traffic between HealthImaging and Amazon S3 is routed over the AWS network and is
  encrypted using TLS.
