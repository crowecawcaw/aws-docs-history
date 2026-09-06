

# Configure your external voice system for integration with conversational analytics
<a name="configure-external-voice-system"></a>

After you [create a conversational analytics connector](create-contact-lens-connector.md) you need to configure your external voice system to point to the connector. Complete the following steps.

1. In the Connect Customer console navigation pane, choose **External voice systems**, **conversational analytics integrations**. You'll see the name of available conversational analytics connectors. Select the one you want to use. The following image shows an example conversational analytics connector named **MyTestConnector**.  
![The conversational analytics integrations page, an example connector named MyTestConnector.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contactlens-connector-name.png)

1. On the connector details page, note the fully qualified host name. This is the name of the host in Connect Customer that will receive the SIPREC audio. The following image shows an example fully qualified host name.  
![The MyTestConnector details page, the fully qualified name of the host that will receive the SIPREC audio.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contactlens-connector-detailspage.png)

1. For information about how to configure your external source system, go to the [Amazon Chime SDK resources](https://aws.amazon.com/chime/chime-sdk/resources/?whats-new-chime-sdk.sort-by=item.additionalFields.postDateTime&whats-new-chime-sdk.sort-order=desc) page, and choose **Configuration Guides**. Scroll down the page to **SIPREC/NBR Configuration Guides**, as shown in the following image.  
![The Configuration Guides on the Amazon Chime SDK resource page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/configuration-guides.png)
**Note**  
If you created credentials for the connector, you need to use the same credentials for your external system.

1. After you configure your external source system, continue to the next step: [enable conversational analytics integration](enable-contactlens-integration.md).