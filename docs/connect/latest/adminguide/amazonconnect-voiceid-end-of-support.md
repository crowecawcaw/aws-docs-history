

# Amazon Connect Customer Voice ID end of support
<a name="amazonconnect-voiceid-end-of-support"></a>

After careful consideration, we decided to end support for Amazon Connect Customer Voice ID, effective May 20, 2026. Amazon Connect Customer Voice ID will no longer accept new customers beginning May 20, 2025. As an existing customer with an account signed up for the service before May 20, 2025, you can continue to use Amazon Connect Customer Voice ID features. After May 20, 2026, you will no longer be able to use Amazon Connect Customer Voice ID.

This page provides instructions and best practices for Connect Customer IT administrators and users to transition Voice ID to alternate solutions to meet your business needs. This might include solutions from AWS Partners available on the AWS Marketplace, such as [Pindrop®](https://aws.amazon.com/marketplace/pp/prodview-f7rqlwjby3er4), or do-it-yourself solutions with AWS End User Messaging SMS.

## Do-it-yourself solutions with AWS End User Messaging SMS
<a name="diy-end-user-messaging"></a>

You can improve contact center security by enabling One-Time-Pin (OTP) based authentication for your contact center with AWS End User Messaging SMS. You can reference a solution example for enabling OTPs using AWS End User Messaging SMS to create one for your contact center. For more information about this solution, see the following blog post: [Build a Secure One-Time Password Architecture with AWS](https://aws.amazon.com/blogs/messaging-and-targeting/build-a-secure-one-time-password-architecture-with-aws/). For more information about AWS End User Messaging SMS, see [What is AWS End User Messaging SMS?](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-sms-mms.html) 

## Managing your Voice ID data
<a name="manage-voiceid-data"></a>

You can get information about all your Voice ID domains in your AWS accounting using the Voice ID `ListDomains` API in conjunction with the `DescribeDomain` API. For more information about managing your Connect Customer Voice ID domains, see [Manage Connect Customer Voice ID domains](voiceid-domain-operations.md). 

For a specific Voice ID domain, you can download data about enrolled callers using the `ListSpeakers` API and registered fraudsters using `ListFraudsters` API. For more information about speaker and fraudster management, see [Connect Customer Voice ID speaker, watchlist, and fraudster management APIs](voiceid-speaker-fraudster-management-apis.md). You can make sure that all your customer data on Voice ID is deleted by using the Voice ID `DeleteDomain` API. You need to perform this operation for every Voice ID domain in every AWS Region and every account. 