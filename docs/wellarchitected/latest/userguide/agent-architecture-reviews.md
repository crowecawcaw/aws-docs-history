

AWS Well-Architected Agent is in preview release and is subject to change.

# Conducting architecture reviews
<a name="agent-architecture-reviews"></a>

Architecture reviews analyze your infrastructure as code (IaC) templates against the AWS Well-Architected Framework and return deployment-ready updated templates with best-practice fixes applied. Unlike resource and application recommendations, architecture reviews target templates before deployment, enabling you to identify and resolve issues before they reach production.

Unlike Resource and Application recommendations, AWS WA Agent, Architecture type recommendations are not automatically generated. You must manually conduct an architecture review to generate them.

## Supported input formats
<a name="agent-review-supported-inputs"></a>

You provide an Amazon S3 URI containing your infrastructure as code (IaC) templates for an architecture review. AWS CDK and Terraform projects are supported. The following input types are accepted:
+ **.zip file:** A compressed archive of your IaC project files. The .zip file cannot exceed 25 MB.
+ **Amazon S3 folder:** A folder in Amazon S3 containing your IaC project files. The total folder size cannot exceed 100 MB, and no individual file can exceed 1 MB.

AWS WA Agent validates submitted files and rejects requests that contain malicious content or files that exceed these size limits. Binary and media files are excluded from the review.

## Conducting a review
<a name="agent-conduct-review"></a>

### Console
<a name="agent-conduct-review-console"></a>

**To conduct an architecture review**

1. In the AWS WA Agent dashboard, choose **Architecture review**.

1. In Review details, enter a name for your architecture review. The name must contain only letters, numbers, hyphens (-), and underscores (\_). Spaces and special characters are not permitted.

1. Upload your file using an S3 URI. Then, choose an **Object version**. You can also choose **Browse S3** to explore files in your S3 buckets.
**Note**  
 AWS WA Agent expects that your S3 buckets are in the same AWS Region as your agent profile. If you cannot find your IaC files, verify that they're in an S3 bucket in the same Region as your profile. 

1.  Select the consent checkbox to allow AWS WA Agent to access the contents of the file. Without selecting this checkbox, you cannot run an architecture review. 

1. Select the **Well-Architected Framework** lens. This is the only lens available for architecture reviews at this time.

1. Select which pillars you want to review.

1. Choose **Start review**.

### CLI
<a name="agent-conduct-review-cli"></a>

Use the `StartAgentRecommendationGeneration` API to start an architecture review. Only the `ARCHITECTURE` recommendation type is supported for on-demand generation. Resource and application recommendations are generated exclusively through the scheduled refresh cycle and cannot be triggered on demand.

The following parameters control the review request:

`--name` (optional)  
The name of the architecture review. The name can be 1 to 128 characters and must contain only letters, numbers, hyphens (-), and underscores (\_). Spaces and special characters are not permitted.

`--types` (required)  
The recommendation types to generate. Specify `ARCHITECTURE`.

`--scope` (required)  
A JSON object that defines what the review covers. Required for architecture reviews.    
`pillars` (required)  
A list of Well-Architected pillars to review. Valid values: `COST_OPTIMIZATION`, `SECURITY`, `RESILIENCE`, `PERFORMANCE`.  
`goalIds` (optional)  
A list of up to 10 optimization goal IDs to prioritize the review against. You can retrieve goal IDs using `ListAgentGoals`. For information about creating goals, see [Editing goals](agent-edit-goals.md).  
`items` (optional)  
A per-pillar filter that narrows the review to specific items. Each object has two required members: `pillar` (a single pillar value) and `ids` (a list of item IDs to process for that pillar, such as best practice IDs like `SEC02-BP02`, AWS service names, or resource ARNs). When `items` is omitted, all items are processed for the selected pillars.

`--additional-context` (optional)  
A JSON object specifying the IaC template location and lens selection. An architecture review analyzes an IaC template, so you provide the template location through this parameter.    
`s3Uri` (required)  
The Amazon S3 URI of the IaC template, .zip archive, or folder to review.  
`s3VersionId` (optional)  
The object version ID of the Amazon S3 object.  
`lensArns` (required)  
A list of lens ARNs to review against. Only the Well-Architected Framework lens (`arn:aws:wellarchitected::aws:lens/wellarchitected`) is supported for architecture reviews at this time.

```
aws wellarchitected start-agent-recommendation-generation \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}" \
    --types ARCHITECTURE \
    --name "{{my-architecture-review}}" \
    --scope '{
  "pillars": ["COST_OPTIMIZATION", "SECURITY"]
}' \
    --additional-context '{
  "s3Uri": "s3://{{your-bucket}}/{{your-template.yaml}}",
  "s3VersionId": "{{optional-version-id}}",
  "lensArns": ["arn:aws:wellarchitected::aws:lens/wellarchitected"]
}'
```

To monitor the status of an architecture review, use `GetAgentRecommendationGeneration` or `ListAgentRecommendationGenerations`:

```
aws wellarchitected list-agent-recommendation-generations \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}"
```

## Architecture review limits
<a name="agent-review-limits"></a>

Architecture reviews are limited to 5 reviews per day per profile. You can run reviews consecutively while daily quota remains. Architecture reviews are not subject to the weekly scheduled recommendation generation cycle.

## Viewing review results
<a name="agent-review-results"></a>

You can monitor the status of the review as it progresses or return to the AWS WA Agent dashboard by choosing **Go to dashboard**. The Reviews tab on the dashboard shows all your in-progress and completed reviews.

The generated recommendations include code in the same language as your source template. For example, if you upload a Terraform file, the updated template is returned as Terraform.