

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Managing phone numbers in Amazon Chime
<a name="phone-numbers"></a>

You use Use the Amazon Chime console to provision phone numbers. When you provision numbers, you request them from a pool of numbers managed by Amazon Chime. When you unassign and then delete numbers, they return to the pool. When you port numbers, you port them into and out of Amazon Chime.

**Note**  
When you use the Amazon Chime console, you can only provision Amazon Chime Business Calling numbers. If you need international numbers, you use Amazon Chime Voice Connectors and SIP media applications. To do that, you must first create an Amazon Chime SDK administrative account. For more information, refer to the following topics in the *Amazon Chime SDK Administrator Guide*:  
[Prerequisites](https://docs.aws.amazon.com/chime-sdk/latest/ag/prereqs.html)
[Managing phone number inventory](https://docs.aws.amazon.com/chime-sdk/latest/ag/phone-inventory.html)
[Managing Voice Connectors](https://docs.aws.amazon.com/chime-sdk/latest/ag/voice-connectors.html)
[Managing SIP media applications](https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-sip-applications.html)

The topics in the following sections explain how to provision and manage Amazon Chime phone numbers.

**Topics**
+ [Provisioning phone numbers](provision-phone.md)
+ [Porting existing phone numbers](porting.md)
+ [Assigning Amazon Chime Business Calling phone numbers](assign-cbc-numbers.md)
+ [Unassigning Amazon Chime Business Calling phone numbers](unassign-cbc-numbers.md)
+ [Using outbound calling names](calling-name.md)
+ [Deleting phone numbers](delete-phone.md)
+ [Restoring deleted phone numbers](restore-phone.md)