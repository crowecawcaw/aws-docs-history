**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Infrastructure security in Amazon Pinpoint

As a managed service, Amazon Pinpoint is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access Amazon Pinpoint through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  Although you can make these API calls from any network location, Amazon Pinpoint supports
  resource-based access policies. These policies can include restrictions based on source IP
  address. To learn more about this type of policy, see [Managing access using policies](security-iam.md#security_iam_access-manage "security-iam.md#security_iam_access-manage").

In addition, you can configure and use various AWS security features to control access
to Amazon Pinpoint resources from any mobile or web apps that you integrate with Amazon Pinpoint. This includes
restrictions on API calls for tasks such as adding endpoints, updating endpoint data,
submitting event data, and reporting usage data.

To use these features, we recommend that you use the AWS Mobile SDKs or AWS Amplify
JavaScript libraries to integrate mobile and web apps with Amazon Pinpoint. For Android or iOS apps,
we recommend that you use the AWS Mobile SDK for Android or the AWS Mobile SDK for iOS, respectively. For
JavaScript-based mobile or web apps, we recommend that you use the AWS Amplify JavaScript
Library for the Web or the AWS Amplify JavaScript Library for React Native. To learn more
about these resources, see [Getting
started with the AWS mobile SDKs](../../../aws-mobile/latest/developerguide/getting-started.md "../../../aws-mobile/latest/developerguide/getting-started.md"), [Getting
started with the AWS Amplify library for the web](../../../aws-mobile/latest/developerguide/web-getting-started.md "../../../aws-mobile/latest/developerguide/web-getting-started.md"), and [Getting started with the AWS Amplify library for react native](../../../aws-mobile/latest/developerguide/react-native-getting-started.md "../../../aws-mobile/latest/developerguide/react-native-getting-started.md").
