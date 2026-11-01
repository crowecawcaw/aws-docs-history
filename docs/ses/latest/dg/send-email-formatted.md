

# Sending formatted email using the Amazon SES API
<a name="send-email-formatted"></a>

You can send a formatted email by using the AWS Management Console or by calling the Amazon SES API through an application directly, or indirectly through an AWS SDK, the AWS Command Line Interface, or the AWS Tools for Windows PowerShell.

The Amazon SES API provides the `SendEmail` operation. To send a formatted email, you specify a From: address, at least one destination address (To:, CC:, or BCC:), and Simple (formatted) content: a message subject and a message body—text, HTML, or both. For more information, see the [SendEmail](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html) operation in the Amazon SES API v2.

**Note**  
The email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. For more information, see [RFC 3492](https://tools.ietf.org/html/rfc3492).

For examples of how to compose a formatted message using various programming languages, see [Code examples](send-an-email-using-sdk-programmatically.md#send-an-email-using-sdk-programmatically-examples).

For tips on how to increase your email sending speed when you make multiple calls to `SendEmail`, see [Increasing throughput with Amazon SES](troubleshoot-throughput-problems.md).