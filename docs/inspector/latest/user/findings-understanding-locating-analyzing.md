# Viewing Amazon Inspector findings

You can view findings in the Amazon Inspector console and with the Amazon Inspector [`ListFindings`](../../v2/APIReference/API_ListFindings.md "../../v2/APIReference/API_ListFindings.md") API.
In the Amazon Inspector console, you can view all of your findings in the **Dashboard** and **Findings** screens.
By default, these screens only show your active and critical findings.
However, you can filter through findings or choose to view findings by category.
You can also view some findings in [Security Hub CSPM and Amazon ECR](integrations.md "integrations.md") if you activate these integrations.
The procedures in this section describe how to view findings in Amazon Inspector console and with the Amazon Inspector `ListFindings` API.

Console

###### To view Amazon Inspector findings

1. Sign in using your credentials.
   Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. (Optional) From the navigation pane, choose **Dashboard**.
   The dashboard shows an overview of the coverage for your environment and only your active and critical findings.
3. (Optional) From the navigation pane, choose **Findings**.
   This screen lists all of your active findings.
   You can use filter criteria [to view specific findings](findings-managing-filtering.md "findings-managing-filtering.md").
   To exclude findings from the list, [create a suppression rule](findings-managing-supression-rules.md "findings-managing-supression-rules.md").
   To view details for a finding, choose the name of the finding.
4. (Optional) From the navigation pane, choose one of the following options to view your findings by category:
   - By vulnerability – Shows vulnerabilities with the most critical findings.
   - By account – Shows accounts with the most critical findings.
     This category is only available to delegated administrators.
   - By instance – Shows Amazon EC2 instances with the most critical findings.
     This category does not include information about network availability.
   - By container image – Shows Amazon ECR container images with the most critical findings.
     This category also provides basic information about your container images.
     It even includes details, such as how many Amazon ECS tasks and Amazon EKS pods are deployed.
     From this screen, you can find out how many tasks/pods were running in past 24 hours and stopped.
   - By container repository – Shows container repositories with the most critical findings.
   - By Lambda function – Shows Lambda functions with the most critical findings.

API

###### To view Amazon Inspector findings

- Run the [ListFindings](../../v2/APIReference/API_ListFindings.md "../../v2/APIReference/API_ListFindings.md") API operation.
  In the request, specify [filterCriteria](../../v2/APIReference/API_FilterCriteria.md "../../v2/APIReference/API_FilterCriteria.md") to return specific findings.
