

# Code examples for CloudFront using AWS SDKs

The following code examples show how to use CloudFront with an AWS software development kit (SDK). 

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see [Using CloudFront with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

**Contents**
+ [Basics](service_code_examples_basics.md)
  + [Actions](service_code_examples_actions.md)
    + [`CreateDistribution`](example_cloudfront_CreateDistribution_section.md)
    + [`CreateFunction`](example_cloudfront_CreateFunction_section.md)
    + [`CreateInvalidation`](example_cloudfront_CreateInvalidation_section.md)
    + [`CreateKeyGroup`](example_cloudfront_CreateKeyGroup_section.md)
    + [`CreatePublicKey`](example_cloudfront_CreatePublicKey_section.md)
    + [`DeleteDistribution`](example_cloudfront_DeleteDistribution_section.md)
    + [`GetCloudFrontOriginAccessIdentity`](example_cloudfront_GetCloudFrontOriginAccessIdentity_section.md)
    + [`GetCloudFrontOriginAccessIdentityConfig`](example_cloudfront_GetCloudFrontOriginAccessIdentityConfig_section.md)
    + [`GetDistribution`](example_cloudfront_GetDistribution_section.md)
    + [`GetDistributionConfig`](example_cloudfront_GetDistributionConfig_section.md)
    + [`ListCloudFrontOriginAccessIdentities`](example_cloudfront_ListCloudFrontOriginAccessIdentities_section.md)
    + [`ListDistributions`](example_cloudfront_ListDistributions_section.md)
    + [`UpdateDistribution`](example_cloudfront_UpdateDistribution_section.md)
+ [Scenarios](service_code_examples_scenarios.md)
  + [Create a multi-tenant distribution and distribution tenant](example_cloudfront_CreateSaasResources_section.md)
  + [Delete signing resources](example_cloudfront_DeleteSigningResources_section.md)
  + [Get started with a basic content distribution network](example_cloudfront_GettingStarted_section.md)
  + [Getting started with web application firewalls](example_wafv2_GettingStarted_052_section.md)
  + [Sign URLs and cookies](example_cloudfront_CloudFrontUtilities_section.md)
+ [CloudFront Functions examples](service_code_examples_cloudfront_functions_examples.md)
  + [Add HTTP security headers](example_cloudfront_functions_add_security_headers_section.md)
  + [Add a CORS header](example_cloudfront_functions_add_cors_header_section.md)
  + [Add a cache control header](example_cloudfront_functions_add_cache_control_header_section.md)
  + [Add a true client IP header](example_cloudfront_functions_add_true_client_ip_header_section.md)
  + [Add an origin header](example_cloudfront_functions_add_origin_header_section.md)
  + [Add index.html to request URLs](example_cloudfront_functions_url_rewrite_single_page_apps_section.md)
  + [Authorize before the cache](example_cloudfront_functions_network_call_agent_authz_section.md)
  + [Authorize with a network call](example_cloudfront_functions_network_call_authorizer_headers_section.md)
  + [Bot check that fails open](example_cloudfront_functions_network_call_bot_check_fail_open_section.md)
  + [Health check and failover](example_cloudfront_functions_network_call_origin_health_failover_section.md)
  + [KeyValueStore read-through config](example_cloudfront_functions_network_call_kvs_config_read_through_section.md)
  + [Make a network call](example_cloudfront_functions_network_call_hello_fetch_section.md)
  + [Markdown for AI agents on demand](example_cloudfront_functions_network_call_markdown_on_demand_section.md)
  + [Normalize query string parameters](example_cloudfront_functions_normalize_query_string_parameters_section.md)
  + [Redirect to a new URL](example_cloudfront_functions_redirect_based_on_country_section.md)
  + [Rewrite a request URI](example_cloudfront_functions_kvs_conditional_read_section.md)
  + [Route through a VPC origin](example_cloudfront_functions_network_call_vpc_private_routing_section.md)
  + [Select origin closer to the viewer](example_cloudfront_functions_select_origin_based_on_country_section.md)
  + [Send events with cf.beacon](example_cloudfront_functions_network_call_beacon_signal_section.md)
  + [Sticky A/B variant](example_cloudfront_functions_network_call_ab_sticky_variant_section.md)
  + [Use key-value pairs](example_cloudfront_functions_kvs_key_value_pairs_section.md)
  + [Validate a Cognito token](example_cloudfront_functions_network_call_cognito_auth_section.md)
  + [Validate a simple token](example_cloudfront_functions_kvs_jwt_verify_section.md)
  + [Virtual waiting room](example_cloudfront_functions_network_call_waiting_room_section.md)