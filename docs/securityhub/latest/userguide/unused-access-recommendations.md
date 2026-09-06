

# Generating policy recommendations for unused access findings
<a name="unused-access-recommendations"></a>

 For unused permissions findings, Security Hub can generate least-privilege policy recommendations that show you a scoped-down replacement policy. The recommendation evaluates each policy attached to the IAM principal and generates a replacement that retains only the permissions the principal has actually used. This capability is provided to all Security Hub customers at no additional cost. 

## How policy recommendations work
<a name="recommendations-how-it-works"></a>

 Policy recommendation generation is an asynchronous operation. To generate and retrieve a recommendation: 

1.  Retrieve the unused permissions finding from Security Hub using the `GetFindingsV2` API operation. Note the `metadata.uid` field from the finding. 

1.  Call `GenerateRecommendedPolicyV2` with the finding's `metadata.uid`. This initiates the recommendation generation, which typically completes within 20 seconds. 

1.  Poll `GetRecommendedPolicyV2` with the same `metadata.uid` until the `status` field returns `SUCCEEDED`. 

1.  The response contains one or more recommendation steps. Each step specifies a `recommendedAction` of either `CREATE_POLICY` (create and attach a scoped-down replacement policy) or `DETACH_POLICY` (detach the over-privileged original policy). For `CREATE_POLICY` steps, the response includes both the `existingPolicy` JSON and the `recommendedPolicy` JSON so you can compare them. 

 You must call `GenerateRecommendedPolicyV2` before calling `GetRecommendedPolicyV2` if a recommendation has not been previously generated for that finding. 

## Who can generate recommendations
<a name="recommendations-who-can-generate"></a>

 Both the account owner and delegated administrators can call these API operations: 
+  **Account owners** can generate and view recommendations for unused permissions findings in their own account. 
+  **Delegated administrators** can generate and view recommendations for any member account's unused permissions findings within their organization. 

 If you are not a delegated administrator and the finding belongs to a different account, the API operation returns an `AccessDeniedException` error. 

## Recommendation lifecycle
<a name="recommendations-lifecycle"></a>
+  Recommendations are cached for 90 days and remain available as long as the finding is active (not Closed). However, calling `GenerateRecommendedPolicyV2` multiple times invalidates the cache and starts a new job that replaces the cached policy. Call `GenerateRecommendedPolicyV2` only once per finding. 
+  The recommendation follows a detach-and-attach pattern. It does not modify your existing IAM policies. You review the recommended policy and manually apply it in the IAM console or through the IAM API. 
+  If the finding is resolved (for example, because the previously unused permissions are now being used), the recommendation is no longer available. 

## Error cases
<a name="recommendations-errors"></a>

 The API operations return errors in the following situations: 
+  The finding has been resolved — `InvalidInputException` (HTTP 400). 
+  The finding is not an unused permissions finding — `InvalidInputException` (HTTP 400). 
+  The IAM principal was created through IAM Identity Center permission set. Policies for permission set principals cannot be directly modified. The recommendation returns a `FAILED` status with an explanation. 
+  The caller is not a delegated administrator and the finding belongs to a different account — `AccessDeniedException` (HTTP 403). 
+  No recommendation has been generated yet and you call `GetRecommendedPolicyV2` without first calling `GenerateRecommendedPolicyV2` — `ResourceNotFoundException` (HTTP 404). 

## Using the console
<a name="recommendations-console"></a>

 In the Security Hub console, you can generate a policy recommendation by viewing an unused permissions finding and choosing the **Remediation** tab. The console displays a loading spinner while the recommendation is being created. When the recommendation is ready, you can choose **Preview** to see a side-by-side comparison of your current policy and the recommended least-privilege replacement. You can copy the recommended policy in JSON format. 

## API reference
<a name="recommendations-api-reference"></a>
+  [GenerateRecommendedPolicyV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GenerateRecommendedPolicyV2.html) — Initiates asynchronous generation of a least-privilege policy recommendation for an unused permissions finding. Takes the finding's `metadata.uid` as input. Returns HTTP 200 with an empty body on success. 
+  [GetRecommendedPolicyV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetRecommendedPolicyV2.html) — Retrieves the generated policy recommendation. Takes the finding's `metadata.uid` as input. Supports pagination with `maxResults` (1–100) and `nextToken` parameters. Returns the recommendation status (`IN_PROGRESS`, `SUCCEEDED`, or `FAILED`), recommendation steps, the resource ARN, and any errors. 

 For detailed API documentation, see the *Security Hub API Reference*. 