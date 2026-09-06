

# Assessment and planning
<a name="dotnet-bp-assessment-planning"></a>

After you start a transformation job, AWS Transform analyzes your code and produces an assessment report and transformation plan. Use the following best practices to get the most from this phase.

## Review assessment and ask questions to set your expectations
<a name="dotnet-bp-review-assessment"></a>

Review the assessment findings carefully to understand which projects will be challenging to transform and why. The agent presents projects with a complexity level (low, medium, high, critical) and explains why they have that rating.

Ask questions to understand more about challenging areas. For example:
+ Ask the agent what its confidence level is in a project transformation or use case.
+ Ask the agent what post-transformation tasks will likely be needed with an AI code companion.

## Review the plan and discuss options with the agent
<a name="dotnet-bp-review-plan"></a>

The agent provides a transformation plan for your review. You can discuss and modify this plan. Start by understanding your options. Ask the agent what alternatives there are to any part of the plan.

For example, the transformation plan might propose transforming WCF services to ASP.NET Web APIs. However, your organization prefers to stay with WCF. You ask the agent for options, and learn that an alternative is to transform them to CoreWCF.

## Upload steering documents to tailor a plan for your organization
<a name="dotnet-bp-steering-docs"></a>

The original transformation plan is created without an understanding of your organization's requirements and preferences. You can inform the agent of organizational conventions, application specifications, preferred technology stack, and preferred coding pattern examples.

After uploading a steering document, explain it to give the agent context. With the additional info from steering documents, the agent can prepare a plan tailored to how your organization likes to work.

## Freely customize the plan
<a name="dotnet-bp-customize-plan"></a>

The .NET agent is flexible and you can freely customize the transformation plan, within the domain of .NET to .NET transformation. You can ask for plan changes in chat, or if you prefer you can work with markdown files. Review and refine the plan until satisfied.

If a plan needs to be reviewed by multiple stakeholders, you can download the plan as a markdown file, share it, and later upload a customized plan.

For example, you review the transformation plan, and decide you want the class library projects transformed to .NET Standard instead of .NET 10. In chat you say, "Revise the plan to transform all class libraries to .NET Standard 2.0" and the agent presents you with a revised plan.