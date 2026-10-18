

# RevisionWeight
<a name="API_RevisionWeight"></a>

Specifies a revision and its traffic weight for an endpoint. You can assign weights to up to two revisions to split traffic for canary or blue-green deployments.

## Contents
<a name="API_RevisionWeight_Contents"></a>

 ** revisionId **   <a name="lambdaweb-Type-RevisionWeight-revisionId"></a>
The identifier of the revision.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** weight **   <a name="lambdaweb-Type-RevisionWeight-weight"></a>
The percentage of traffic to route to this revision. Minimum value of 1, maximum value of 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: Yes

## See Also
<a name="API_RevisionWeight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/RevisionWeight) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/RevisionWeight) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/RevisionWeight) 