# Create a conversational analytics connector to integrate with your external voice system

This topic explains how to create a conversational analytics connector to integrate with
your external voice system. Complete the following steps.

1. Open the Connect Customer console at
   [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/").
2. On the instances page, choose the instance alias. The instance alias is also
   your **instance name**, which appears in your Connect Customer
   URL. The following image shows the **Connect Customer virtual contact center instances** page, with a box
   around the instance alias.

![The Connect Customer virtual contact center instances page, the instance alias.](images/instance.png) 3. In the Connect Customer console, in the navigation pane, choose **External voice
systems**, **conversational analytics integrations**,
and then choose **Create conversational analytics connector**, as
shown in the following image.

![The conversational analytics integrations page, the Create conversational analytics connector button.](images/contact-lens-create-connector.png) 4. On the **conversational analytics connector** page, type a
friendly name for the connector. 5. Under **Connector source type**, use the dropdown menu to
select from a list of available connector source types. Usually this is an
external Session Boarder Controller (SBC) that will initiate the SIPREC session.
The following image shows a sample dropdown list of source types.

![The conversational analytics connector page, the Connect source type dropdown list.](images/contact-lens-connector-source-types.png) 6. Under **Voice system type**, use the dropdown list to select
the voice system used for the call. Usually this is your external contact center
system. The following image shows a sample dropdown list of voice system
types.

![The conversational analytics connector page, the voice system type dropdown list.](images/contact-lens-voice-system-types.png) 7. Enable **Encryption** and **Logging** of the
SIP and Media metric messages.

    * Amazon Chime SDK Voice Connector uses TLS server certificates issued by Amazon Trust Services. Most modern operating systems trust Amazon Trust Services by default. If this is not the case for your SIP infrastructure and you enable encryption, you may need to add the Starfield and Amazon Trust Services root CA certificates, excluding the EU roots, to your trust stores. You can find these certificates [here](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/").
    * Although logging is optional, we recommend you enable it to help you
     debug integration issues.

8. In the **Source IP addresses** section, you can configure a
range of Source IP addresses that are allowed to send voice to this
connector. 9. In the **Credentials - optional** section, we recommend that
you create credentials. They can help authenticate the SIPREC sessions.

###### Note

If you do this, you'll need to provide the same credentials when you
configure your external system. 10. Optionally, add tags to identify, organize, search for, filter, and control
who can access this connector. For more information, see [Add tags to resources in Connect Customer](tagging.md "tagging.md"). 11. Choose **Create conversational analytics connector** to create the
connector. After the connector is created, a success message is
displayed. 12. On the **conversational analytics integrations** page you'll see
the short host name. This is the host that your external voice system will send
SIPREC voice traffic to.

When you configure your external voice system, you'll use the fully qualified
domain name of the host, not this short host name.

![The conversational analytics integrations page, the short host name of the connector.](images/contact-lens-connector-shorthostname.png) 13. You're done creating the conversational analytics connector. Continue to the next
step: [Configure your external
voice system for integration with conversational analytics](configure-external-voice-system.md "configure-external-voice-system.md").
