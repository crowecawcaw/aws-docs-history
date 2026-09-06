

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Using an Amazon Q Business custom plugin
<a name="using-custom-plugin"></a>

Once a custom plugin is deployed, end users can launch it from the menu icon in the Amazon Q Business web experience.

**Note**  
If your [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html) settings allow Amazon Q to automatically orchestrate end user chat queries across plugins and data sources, plugin actions will be automatically activated by Amazon Q for your end user during chat. In that case, your end user won't have to follow the steps below.

![Screenshot showing the Amazon Q Business web experience menu with the custom plugin option highlighted, allowing users to select and activate the plugin.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/1-custom-plugin-select-menu@2x.png)


End users can then type a prompt.

![Screenshot showing a user typing a prompt in the Amazon Q Business chat interface to interact with the custom plugin, demonstrating how users can make requests to the plugin.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/2-custom-plugin-prompt@2x.png)


If it is the first time an end user is accessing the custom plugin or their past login has expired, they will need to authenticate. After authenticating successfully, Amazon Q Business will perform the requested task. For a write API operation, end users will always get a confirmation form that allows them to confirm or correct parameters that were populated based on the request or past actions.

![Screenshot showing a confirmation form displayed by the custom plugin, allowing users to verify and modify parameters before the plugin performs the requested action.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/3-custom-plugin-form@2x.png)


Once the user confirms the action, Amazon Q Business will submit the request and give the user confirmation once it is complete.

![Screenshot showing a success message after the custom plugin has completed the requested action, confirming to the user that their request was processed successfully.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/4-custom-plugin-success@2x.png)
