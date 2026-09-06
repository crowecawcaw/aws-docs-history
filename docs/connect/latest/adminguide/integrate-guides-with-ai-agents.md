

# Integrate agent assist with step-by-step guides
<a name="integrate-guides-with-ai-agents"></a>

To help agents get to solutions faster, you can associate [step-by-step guides](step-by-step-guided-experiences.md) with knowledge base content, such as knowledge articles. Then, when agent assist provides a recommended solution to an agent, it also provides them with the option to start the step-by-step guide that you associated with the content.

This topic explains how to associate step-by-step guides with knowledge base content.

## Step 1: Identify the resources you want to integrate
<a name="identify-resources-to-integrate"></a>

The first step is to gather the information needed to run the integration command in [Step 2: Associate the step-by-step guide with the knowledge base content](#associate-guide-content): 
+ The ID of the knowledge base that contains the content resource you want to associate with step-by-step guides.
+ The ID of the content resource in the knowledge base.
+ The ARN of the step-by-step guide that you want to associate with the content.

The following sections explain how to get this information.

### Get the knowledge base ID
<a name="obtain-knowledgebaseid"></a>

To obtain the ID of knowledge base that you want to associate with step-by-step guides, you can call the [ListKnowledgeBases](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ListKnowledgeBases.html) API or run the `list-knowledge-bases` CLI command.

Following is an example `list-knowledge-bases` command that lists all of the knowledge bases:

```
aws qconnect list-knowledge-bases
```

Identify the knowledge base that contains the content resources you want to associate. Copy and save the `knowledgeBaseId`. You'll use it in [Step 2](#associate-guide-content).

### Get the content ID
<a name="identify-knowledgebase-content"></a>

To list the content resources in the knowledge base, you can call the [ListContents](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ListContents.html) API or run the `list-contents` CLI command. 

Following is an example `list-contents` command that lists the content resources and their content ID.

```
aws qconnect list-contents \
--knowledge-base-id {{knowledgeBaseId}}
```

Identify which content resources you want to associate with a step-by-step guide. Copy and save the `contentId`. You'll use it in [Step 2](#associate-guide-content).

### Get the `flowARN` of the step-by-step guide
<a name="identify-step-by-step-guides-integrate"></a>

You need to get the `flowARN` of the step-by-step guide that you want to associate with the content. There are two ways you can get the `flowARN`: use the Connect Customer admin website or the CLI. 

------
#### [ Connect Customer admin website ]

1. In the Connect Customer admin website, on the navigation menu choose **Routing**, **Flows**.

1. On the **Flows** page, choose the step-by-step guide to open it in the flow designer.

1. In the flow designer, choose **About this flow**, then choose **View ARN**.

1. Copy and save the `flowARN`. It is the entire string, as shown in the following image.  
![Dialog box displaying the complete flowARN (Amazon Resource Name) for a step-by-step guide.](http://docs.aws.amazon.com/connect/latest/adminguide/images/qic-flow-id.png)

   You'll use the `flowARN` in [Step 2](#associate-guide-content).

------
#### [ AWS CLI ]

1. You can call the Connect Customer [ListInstances](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListInstances.html) API or run the `list-instances` CLI command to get the `instanceId` of the instance you want to use.

   Following is an example `list-instances` command:

   ```
   aws connect list-instances
   ```

   Copy and save the `instanceId`.

1. You can call the Connect Customer [ListContactFlows](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListContactFlows.html) API or run the `list-contact-flows` CLI command to determine the step-by-step guide to use. 

   Following is an example `list-contact-flows` command that lists all the flows and step-by-step guides, and their `flowARNs`:

   ```
   aws connect list-contact-flows \
   --instance-id {{instanceId}}
   ```

   Identify the step-by-step guide you want to associate with the knowledge base, and copy and save its `flowARN`. You'll use the `flowARN` in [Step 2](#associate-guide-content). 

------

## Step 2: Associate the step-by-step guide with the knowledge base content
<a name="associate-guide-content"></a>

### Create the content association
<a name="create-content-association"></a>

To complete this step you need the `knowledgeBaseId`, `contentId` and `flowARN` that you obtained in Step 1.

You can call the [CreateContentAssociation](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateContentAssociation.html) API or the run the `create-content-association` CLI command to link the content resource and step-by-step guide. 
+ You can create only one content association for each content resource.
+ You can associate a step-by-step guide with multiple content resources.

Following is an example `create-content-association` command to create a content association between the content resource and a step-by-step guide:

```
aws qconnect create-content-association \
--knowledge-base-id {{knowledgeBaseId}} \
--content-id {{contentId}} \
--association-type AMAZON_CONNECT_GUIDE \
--association '{"amazonConnectGuideAssociation":{"flowId":"{{flowArn}}"}}'
```

For example, the command might look like the following sample when values are added:

```
aws qconnect create-content-association \
--knowledge-base-id {{00000000-0000-0000-0000-000000000000}} \
--content-id {{11111111-1111-1111-1111-111111111111}} \
--association-type AMAZON_CONNECT_GUIDE \
--association '{"amazonConnectGuideAssociation":{"flowId":"arn:aws:connect:{{us-west-2}}:{{111111111111}}:instance/{{22222222-2222-2222-2222-222222222222}}/contact-flow/{{00711358-cd68-441d-8301-2e847ca80c82}}"}}'
```

### Confirm that the content association exists
<a name="confirm-content-association"></a>

You can call the [ListContentAssociations](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ListContentAssociations.html) API or run the `list-content-associations` CLI command to list all of the content associations for the specified content. 

Following is an example `list-content-associations` command that returns a list of content associations so you can verify that the association you created exists:

```
aws qconnect list-content-associations \
--knowledge-base-id {{knowledgebaseId}} \
--content-id {{contentId}}
```

For example, the command might look like the following sample when values are added:

```
aws qconnect list-content-associations \
--knowledge-base-id {{00000000-0000-0000-0000-000000000000}} \
--content-id {{11111111-1111-1111-1111-111111111111}}
```

### Assign permissions so agents can view recommendations and step-by-step guides
<a name="enable-guide-experience"></a>

Assign the following **Agent Applications** security profile permissions to the agents so they can view the knowledge base content and the step-by-step guides.
+ **agent assist - View**: Enables agents to search for and view content. They can also receive automatic recommendations during calls if conversational analytics is enabled.
+ **Custom views - Access**: Enables agents to see step-by-step guides in their agent workspace.

For information about how to add more permissions to an existing security profile, see [Update security profiles in Connect Customer](update-security-profiles.md).