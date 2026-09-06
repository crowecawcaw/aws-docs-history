

# Creating a network of bots for your Lex V2 bots
<a name="network-of-bots"></a>

Network of Bots enables enterprises to deliver a unified user experience across multiple bots. With Network of Bots, enterprises can add multiple bots to a single network to enable flexible and independent bot lifecycle management. The network exposes a single unified interface to the end-user and routes the request to the appropriate bot based on user input.

Teams can collaborate to create a network of bots to meet various business needs by maintaining and adding bots to the network as improved bots are deployed to production. Developers can simplify and speed up deployment and improvements by integrating multiple bots into a single network.

 Network of bots is currently only available in the en-US language. 

**Note**  
 Currently, a network of bots is limited to one account. You cannot add bots from other accounts. 

![A sample network of bots](http://docs.aws.amazon.com/lexv2/latest/dg/images/nob/nob-main.png)


## Create a network of bots for your Lex V2 bots
<a name="network-of-bots-create"></a>

Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home). Choose **Network of bots** from the side menu. You must have built at least one bot in order to create a network of bots. 

**Step 1: Configure network of bot settings**

1. In the **Details** section, enter the name of your network and give it an optional description.

1. In the **IAM permissions** section, choose an AWS Identity and Access Management (IAM) role that provides Amazon Lex V2 permission to access other AWS services, such as Amazon CloudWatch. You can have Amazon Lex V2 create the role, or you can choose an existing role with CloudWatch permissions. See [Identity and access management for Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/security-iam.html) for more information. 

1. In the **Children's Online Privacy Protection Act (COPPA)** section, choose the appropriate response. See [DataPrivacy](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DataPrivacy.html) for more information. 

1. In the **Idle session timeout** section, choose the duration that Amazon Lex V2 keeps a session with a user open. Amazon Lex V2 maintains session variables for the duration of the session so that your bot can resume a conversation with the same variables. See [ Setting the session timeout](https://docs.aws.amazon.com/lexv2/latest/dg/context-mgmt-session-timeout.html) for more information.

1. In the **Add language settings** section, choose a voice for your bot to interact with users. You can type a phrase in **Voice sample** and select **Play** to listen to the voice.

1. In the **Advanced settings** section, optionally add tags that help identify the bot. Tags can be used to control access and monitor resources. See [Tagging resources](https://docs.aws.amazon.com/lexv2/latest/dg/tagging.html) for more information.

1. Choose **Next** to create the bot network and move to adding bots.

**Step 2: Add bots**

1.  In the **Bots** section, select **\+ Add bots**. 

1.  An **Add bots** modal will pop up. Choose a bot to add from the **Bot** dropdown menu and the alias of the bot that you want to use from the **Alias** dropdown menu.

   The alias must point to a numbered version of the bot and not to the draft version. You may add up to 5 bots. A bot may be added to up to 25 different networks. 

1.  Select **\+ Add bot** to add more bots to your network. To remove a bot, select **Remove** next to the bot that you want to remove. When you are done adding bots, choose **Save** to close the modal. 

1.  Select **Save** to finish creating your network. 

## Manage your network of bots for your Lex V2 bots
<a name="network-of-bots-manage"></a>

 After creating your network of bots, you will be taken to a page where you can manage and build your network. Or you can reach this page by selecting **Network of bots** in the side menu, and choosing the name of the network to manage. 

1.  To edit information for your network, select **Edit** above the **Details** section. To delete the network, select **Delete** above the **Details** section. 

1.  In the **Bots** section, you can add more bots by selecting **\+ Add bots**. You can also add bots if you navigate to the **Bots** page in the side menu in the Amazon Lex V2 console. Toggle the radio button next to the bot you want to add, and select **Add to a network of bots** from the **Actions** dropdown menu.

   From the **Network of bots** dropdown menu in the modal that pops up, choose the network to which you want to add the bot. Then choose the alias of the bot that you want to use from the **Bot alias** dropdown menu. Select **Add** to add the bot to the network that you chose. 

1.  You can remove bots from your network by toggling the radio button next to a bot and choosing **Remove**. 

1.  When you are done configuring your network, select **Build** in the upper-right to build your network. It may take a few minutes to build. If the build is successful, a green success banner appears at the top of the page. 

1.  Once the network is built, you can select **Test** in the upper-right for a chat window to appear in the bottom right corner. You can use this chat window to converse with your network's bots and make sure the conversation flows and transitions are configured correctly. 

**Note**  
 If you add, remove, or update bots within your network, you must rebuild the network.

## Versions of your network of bots for Lex V2
<a name="network-of-bots-versions"></a>

 You can create different versions of your network of bots. To manage versions, choose your network from the side menu in the Amazon Lex V2 console and select **Versions**. 

1.  Select **Create Version** to make a new version of your network of bots. You can add an optional description. Choose **Create** to create the version. 

1.  When you toggle the radio button next to a version of your network of bots, you can select **Associate alias with version** to point an alias to this version. 

1.  To manage a version of your network, select the name of the version in the **Versions** section. In the following page, you can edit details of the version and manage the bots within the version and its associated alias. 

## Aliases for your network of bots for Lex V2
<a name="network-of-bots-aliases"></a>

 You can use aliases to deploy your networks. To manage aliases, choose your network from the side menu in the Amazon Lex V2 console and select **Aliases**. 

1.  Select **Create alias** to make a new alias. 

1.  Give the alias a name and an optional **Description** in the **Alias details** section. You can choose a version to associate the alias with the **Associate with a version** section and add tags in the **Tags** section. Choose **Create** to create the alias. 

1.  To manage an alias for your network, select the name of the alias in the **Aliases** section. In the following page, you can edit details of the alias and manage its tags, channel integrations, and resource-based policy. You can also view the history of its association with versions of the network. 

## Channel integrations for your Lex V2 network of bots
<a name="network-of-bots-channelintegrations"></a>

 To integrate your network of bots with a messaging platform, choose your network of bots from the side menu in the Amazon Lex V2 console. Then select **Channel integrations**. 

1.  Select **Add channel** to integrate your network with a new channel. 

1.  In the **Platform** section, choose the platform that you want to deploy your bot to in **Select platform**. An IAM role will be created. Choose a key from the dropdown menu under **KMS key** to protect your information. 

1.  In the **Integration configuration** channel, enter the **Name** and an optional **Description**. Choose an **Alias** from the dropdown menu. 

1.  Get your account SID and authentication token from the platform and fill out the **Account SID** and **Authentication token** fields. See [Integrating your bots](https://docs.aws.amazon.com/lexv2/latest/dg/integrating.html) for more information. 

1.  Select **Create** to complete the channel integration. 

**Note**  
Network of bots is currently not available in Connect Customer voice or chat.