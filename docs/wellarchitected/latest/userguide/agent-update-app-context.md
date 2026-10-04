

AWS Well-Architected Agent is in preview release and is subject to change.

# Updating application context
<a name="agent-update-app-context"></a>

Application context tells AWS WA Agent what your applications are, what they do, and what infrastructure they run on. AWS WA Agent uses this information to scope recommendations to the resources that belong to each application and to personalize guidance based on your architecture, criticality, and constraints.

The more context you provide, the more targeted your recommendations become. A profile with application overviews, architecture descriptions, criticality levels, and resource tags produces recommendations that account for your specific environment and priorities as opposed to generic recommendations.

**Important**  
You must have at least one application context defined per profile to generate scheduled recommendations.

Follow these guidelines when defining application context:
+ Create one context entry per logical application, not per resource or per team. For example, if you have an order processing system that spans multiple services, define it as a single application context.
+ Set the criticality level. It directly affects recommendation prioritization. Mission-critical applications receive higher-priority findings than test or development workloads.
+ Use resource tags to scope your applications. If multiple applications share the same accounts, tags are how AWS WA Agent distinguishes which resources belong to which application.

## Console
<a name="agent-update-app-context-console"></a>

**To add application context**

1. Choose **Agent profiles** in the left-hand navigation. Then, on the profile to add the application context, choose **Profile Details**.

1. Select the **Application context** tab. Then, choose **Add application context**.

1. Enter details for the application. For additional customization, expand the **Additional details** dropdown.

   Application context includes the following fields:
   + **Application name:** Name of your application.
   + **Application overview:** Overview of what your application does.
   + **Accounts in this application:** Any AWS accounts this application includes or uses.
   + **Regions:** AWS Regions where this application resides or operates in.
   + **Tags:** Key value pairs included in this application. Tags have two different filtering behaviors depending on what's selected:
     +  **Only the tag is selected:** Includes every resource carrying that tag (and any type of tag) within the selected AWS accounts or AWS Regions.
     +  **Tag selected with services or resource types:** Displays the intersection of the tag with the services or resources. All resources returned in the filter must have that selected tag and be a part of one of the selected services or resource types. 
   + **Additional details:**
     + **Services:** Which services your application uses. Selecting a service automatically selects all of its associated resources.
**Note**  
 When adding or updating a service in an application context, use the CloudFormation canonical service name. For example, for `AWS::DynamoDB::Table CloudFormation`, the service name is `DynamoDB`. 
     + **Resources:** Additional resources your application uses outside of the ones auto-included by the service dropdown. Some resource types are not supported. For more information, see [Unsupported resource types](agent-quotas.md#agent-unsupported-resources).
     + **Industry:** What industry your application serves.
     + **Type:** The type of application.
     + **Criticality:** How critical this application is to your organization.
     + **Architecture overview:** Plain-text overview of your architecture.
     + **Additional context:** Any further context you want AWS WA Agent to consider during reviews and recommendations.

1. After entering your context, choose **Add application**. You will see the new application context in the **All applications** list.

1. After adding application context, it can take up to 24 hours to generate scheduled recommendations based on this new context.

## CLI
<a name="agent-update-app-context-cli"></a>

To add application context:

```
aws wellarchitected create-agent-context \
    --profile-arn "{{profile-arn}}" \
    --title "{{My application}}" \
    --context-type APPLICATION \
    --content '{"applicationOverview":"{{Description}}","criticality":"{{MISSION_CRITICAL}}"}'
```

**Note**  
 When adding or updating a service in an application context, use the CloudFormation canonical service name. For example, for `AWS::DynamoDB::Table CloudFormation`, the service name is `DynamoDB`. 

To update existing application context:

```
aws wellarchitected update-agent-context \
    --profile-arn "{{profile-arn}}" \
    --context-id "{{context-id}}" \
    --title "{{Updated application name}}" \
    --content '{"applicationOverview":"{{Updated description}}"}'
```

To delete application context:

```
aws wellarchitected delete-agent-context \
    --profile-arn "{{profile-arn}}" \
    --context-id "{{context-id}}"
```