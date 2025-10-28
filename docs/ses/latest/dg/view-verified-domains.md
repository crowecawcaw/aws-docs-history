# View identities using the SES console

You can use the Amazon SES console to view domain and email address
identities that are verified or are pending verification. You can also view those identifies
for which verification was unsuccessful.

###### To view your domain and email address identities

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the console, use the Region selector to choose the AWS Region for which you
   want to view your list of identities.

###### Note

This procedure only displays a list of identities for the selected
AWS Region. 3. In the navigation pane, under **Configuration**, choose
**Verified identities**. The **Loaded
identities** table displays both domain and email address identities.
The **Status** column displays whether an identity has been
verified, is pending verification, or has failed the verification process -
definitions of all possible status values are as follows:

    * Verified – your identity is
     successfully verified for sending in SES.
    * Failure – SES was unable to
     verify your identity. If it's a domain, it means SES was unable to
     detect the DNS records within 72 hours. If it's an email address, it means
     the verification email that was sent to the email address was not
     acknowledged within 24 hours.
    * Pending – SES is still trying
     to verify the identity.
    * Temporary Failure – for a previously
     verified domain, SES will periodically check for the DNS record
     required for verification. If at some point, SES is unable to detect
     the record, the status would change to *Temporary
     Failure*. SES will recheck for the DNS record for 72
     hours, and if it’s unable to detect the record, the domain status would
     change to *Failure*. If it’s able to detect the record,
     the domain status would change to *Verified*.
    * Not started – you have not yet
     started the verification process.

4. To sort identities by verification status, choose the **Status**
   column.
5. To view an identity’s details page, select the identity that you want to
   view.
