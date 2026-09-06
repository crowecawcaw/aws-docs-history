# Service controls and fraud prevention in Connect Customer

Contact centers are frequent targets for fraud attempts such as social engineering attacks
and systematic account takeover attempts. With Connect Customer, you can protect your business through
comprehensive access management, real-time monitoring, and automated threat
detection.

## Managing service limits

You can set precise limitations on your contact center operations as a first line of
defense. With service limits, you control the following:

- Concurrent active calls
- Number of queues and routing profiles
- Countries available for outbound calling
- API request thresholds

These service limits act as guardrails that prevent potential abuse while your
operations run smoothly within defined parameters. For example, if your contact center
typically handles up to 500 concurrent calls during peak hours, you can set your service
limit for concurrent active calls to 600. This provides a buffer for unexpected spikes
while preventing abuse that might result in thousands of simultaneous calls.

For best results, follow these recommendations:

- Set limits 20% above peak historical volumes.
- Implement queue-specific thresholds.
- Configure CloudWatch alerts at 80% utilization.

## Configuring authentication controls

Connect Customer supports three authentication methods:

- **Built-in Connect Customer authentication** –
  Native user management within your Connect Customer instance.
- **AWS Identity and Access Management (IAM)** – Federated access
  through AWS identity management.
- **SAML-based Single Sign-On (SSO)** –
  Centralized security controls through your Identity Provider (IdP).

Although each method serves different needs, SAML-based SSO centralizes your security
controls through your IdP. This centralization supports multi-factor authentication
(MFA), automated password rotation, and comprehensive access monitoring.

For optimal security, follow these recommendations:

- Enforce MFA for all agent logins.
- Set maximum session durations of eight hours.
- Implement IP allowlisting (restricting access to approved network addresses)
  for approved networks.
- Require password rotation every 90 days.

## Detecting and responding to threats

In addition to prevention, Connect Customer provides rapid detection and response capabilities.
Connect Customer continuously monitors for suspicious activities and automatically blocks potential
threats. Machine learning models analyze patterns in real time to identify and stop
suspicious behavior before it impacts your operations.

After Connect Customer detects suspicious activity, the system can automatically block access and
alert your security team. Configure the following threat detection settings:

- **Authentication pattern monitoring** –
  Real-time analysis of login behavior to detect anomalies.
- **Geographic-based access controls** –
  Restrictions based on the geographic location of access attempts.
- **Velocity checks** – Limits on the rate
  of authentication attempts to prevent brute-force attacks.
- **Automated blocking** – Automatic
  suspension of high-risk activities.

## Monitoring with Amazon CloudWatch

Connect Customer integrates with CloudWatch to provide detailed insights into your contact center's
security posture. With CloudWatch, you can do the following:

- Monitor service usage against your configured limits.
- Track security events across your instance.
- Receive real-time alerts when suspicious activities occur.
- Create custom dashboards to visualize security metrics.

For more information, see [Monitoring your Connect Customer instance using CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

## Continuous security improvements

Connect Customer security features are continuously enhanced based on emerging threats, customer
feedback, and evolving compliance requirements. Regular updates introduce new protective
measures and strengthen existing ones to help your contact center maintain robust
security against evolving threats.

## Getting started with fraud prevention

To strengthen your contact center security, complete the following steps:

1. Review your current service limits and adjust them based on your peak
   volumes.
2. Implement SSO integration with your identity provider.
3. Set up CloudWatch monitoring and configure alerts.
4. Configure geographic access controls for your instance.
