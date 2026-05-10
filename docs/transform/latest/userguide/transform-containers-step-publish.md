# Step 5: Publish images

In this step, AWS Transform publishes your container images to Amazon Elastic Container Registry. If you have
not yet configured Amazon ECR access, the agent prompts you to provide your Amazon ECR
repository details at this point.

## What happens during publishing

The agent performs the following tasks for each container image:

1. **Connector configuration** — If you
   have not already configured Amazon ECR access, the agent presents a connector
   form where you provide your Amazon ECR repository ARN and connect to your
   AWS account.
2. **Approval request** — The agent
   presents the list of images to be published and requests your approval.
   You can approve or reject the publishing operation.
3. **Image push** — After approval,
   the agent publishes the container images to your Amazon ECR repository using
   . If you have multiple services, the agent publishes all images
   in a single batch operation.
4. **Vulnerability scanning** — Amazon ECR
   automatically scans the published images for known vulnerabilities.
   The agent reports the scan results. For more comprehensive analysis,
   enable AWS ECR enhanced scanning and AWS GuardDuty Runtime Monitoring.

###### Note

Image publishing runs asynchronously using . If your session is
interrupted during publishing, AWS Transform automatically recovers the operation
when you reconnect.

## What you need to do

- Review the list of images to be published.
- Approve or reject the publishing operation. If you reject, the agent
  skips image publishing and you can proceed to the next step without
  published images.
- Review the vulnerability scan results after publishing completes.

After publishing, the agent provides the image URIs that are used in the
infrastructure deployment steps.
