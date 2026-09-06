

# DRHCSEC06-BP02 Control access to locations where AWS Outposts are deployed using systems like keys and biometrics
<a name="drhcsec06-bp02"></a>

 This practice verifies that only authorized personnel can gain physical access to AWS Outposts racks or servers. 

 **Desired outcome:** Reduced risk of data stored on Outposts becoming unreadable due to lack of access to the encryption key. 

 **Common anti-patterns:** 
+  Uncontrolled or untraceable physical access to the Outpost 

 **Benefits of establishing this best practice:** Reduce security risk by minimizing ability to physically interact with the hardware. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-25"></a>
+  Controlling physical access to AWS Outposts racks and servers is of particular importance because the [Nitro Security Key (NSK)](https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html#encryption-rest) plays a key role in the [encryption at rest](https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html#encryption-rest) and protection of data. As a result, purposeful or inadvertent destruction can lead to irrevocable loss of customer data. For a deeper understanding of the AWS Nitro system and how the NSK fits into it, see [The components of the Nitro System](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/the-components-of-the-nitro-system.html). 
+  Review [Tamper monitoring on AWS Outposts equipment](https://docs.aws.amazon.com/outposts/latest/userguide/infrastructure-security.html#w154aac25c21c17) section of the AWS User Gude for Outposts Racks. 
+  Maintain video surveillance of access points to locations where AWS Outposts are deployed so that physical access can be monitored and made available for event forensics. 

## Resources
<a name="resources-10"></a>

 **Related documentation:** 
+  [Encryption at rest](https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html#encryption-rest) 
+  [The Security Design of the AWS Nitro System](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/the-components-of-the-nitro-system.html) 
+  [Infrastructure Security in AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/infrastructure-security.html) 