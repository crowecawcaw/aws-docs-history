# Amazon Connect Voice ID end of

support

After careful consideration, we decided to end support for Amazon Connect Voice ID,
effective May 20, 2026. Amazon Connect Voice ID will no longer accept new customers
beginning May 20, 2025. As an existing customer with an account signed up for the service
before May 20, 2025, you can continue to use Amazon Connect Voice ID features. After May 20,
2026, you will no longer be able to use Amazon Connect Voice ID.

This page provides instructions and best practices for Amazon Connect IT administrators and users
to transition Voice ID to alternate solutions to meet your business needs. This might
include solutions from AWS Partners available on the AWS Marketplace, such as [Pindrop®](https://aws.amazon.com/marketplace/pp/prodview-f7rqlwjby3er4 "https://aws.amazon.com/marketplace/pp/prodview-f7rqlwjby3er4"), or
do-it-yourself solutions with AWS End User Messaging SMS.

## Do-it-yourself solutions with AWS End User Messaging SMS

You can improve contact center security by enabling One-Time-Pin (OTP) based
authentication for your contact center with AWS End User Messaging SMS. You can reference a solution
example for enabling OTPs using AWS End User Messaging SMS to create one for your contact center. For more
information about this solution, see the following blog post: [Build a Secure One-Time Password Architecture with AWS](https://aws.amazon.com/blogs/messaging-and-targeting/build-a-secure-one-time-password-architecture-with-aws/ "https://aws.amazon.com/blogs/messaging-and-targeting/build-a-secure-one-time-password-architecture-with-aws/"). For more
information about AWS End User Messaging SMS, see [What is AWS End User Messaging SMS?](../../../sms-voice/latest/userguide/what-is-sms-mms.md "../../../sms-voice/latest/userguide/what-is-sms-mms.md")

## Managing your Voice ID data

You can get information about all your Voice ID domains in your AWS accounting
using the Voice ID `ListDomains` API in conjunction with the
`DescribeDomain` API. For more information about managing your
Amazon Connect Voice ID domains, see [Manage Amazon Connect Voice ID domains](voiceid-domain-operations.md "voiceid-domain-operations.md").

For a specific Voice ID domain, you can download data about enrolled callers using
the `ListSpeakers` API and registered fraudsters using
`ListFraudsters` API. For more information about speaker and fraudster
management, see [Amazon Connect Voice ID speaker,
watchlist, and fraudster management APIs](voiceid-speaker-fraudster-management-apis.md "voiceid-speaker-fraudster-management-apis.md"). You can ensure that all
your customer data on Voice ID is deleted by using the Voice ID
`DeleteDomain` API. You need to perform this operation for every
Voice ID domain in every AWS Region and every account.
