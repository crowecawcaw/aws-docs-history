

# Amazon Bedrock troubleshooting
<a name="bedrock-troubleshooting"></a>

The in-UI conversational assistant is served by the companion Agentic Vehicle Experience (AVX) accelerator’s Amazon Bedrock AgentCore text runtime. Bedrock invocation errors (for example, `AccessDeniedException` when the AgentCore runtime calls a foundation model or a cross-account knowledge base) are diagnosed and remediated on the AVX side — see the AVX repository’s troubleshooting guide for the cross-region inference-profile IAM patterns and the ADP Knowledge Base cross-account resource-based policy.

CMS-side symptoms are limited to the wire path between the Fleet Manager UI and the AVX API.

## Problem: Assistant panel reports "not configured"
<a name="problem-assistant-not-configured"></a>

The Fleet Manager UI chat panel opens but reports the assistant as unavailable. The browser network tab shows no requests to `/assistant/chat`.

### Diagnosis
<a name="diagnosis-6"></a>

1. Fetch `/runtimeConfig.json` from the CloudFront-served UI and inspect the `vsaApiEndpoint` field:

   ```
   STAGE=staging
   CLOUDFRONT_URL=$(aws cloudformation describe-stacks \
     --stack-name cms-$STAGE-ui \
     --query "Stacks[0].Outputs[?OutputKey=='CloudFrontURL'].OutputValue" \
     --output text)
   curl -s "$CLOUDFRONT_URL/runtimeConfig.json" | grep -i vsa
   ```

1. If `vsaApiEndpoint` is missing or empty, the ChatAgent has no target endpoint. Populate it and regenerate the runtime config:

   ```
   # Set vsaApiEndpoint in deployment/config/<stage>.env, then:
   make -C deployment regenerate-runtime-config DEPLOYMENT_STAGE=$STAGE
   ```

## Problem: Chat requests return HTTP 401 or 403
<a name="problem-assistant-401-403"></a>

The chat panel sends requests to `/assistant/chat` but receives HTTP 401 or 403 responses.

### Diagnosis
<a name="diagnosis-7"></a>

The Cognito access token is attached to `vsaApiEndpoint`-matching requests by the frontend Fetch Interceptor. Verify in the browser developer tools that the outbound request carries an `Authorization: Bearer <token>` header. If the header is missing, the interceptor is not matching the endpoint — check that `vsaApiEndpoint` in `runtimeConfig.json` matches the origin the interceptor is configured to enrich.

If the header is present but AVX still returns 401 or 403, the CMS Cognito user pool is not trusted by the AVX API’s authorizer. Verify with the AVX operator that the CMS user pool ARN is on the AVX API’s trust list.