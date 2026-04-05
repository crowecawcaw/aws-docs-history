# Common Error Types

This section lists common error types that this AWS service may return. Not all services return all error types listed here. For errors specific to an API action for this service, see the topic for that API action.

**AccessDeniedException**

You don't have permission to perform this action. Verify that your IAM policy includes the required permissions.

HTTP Status Code: 403

**ExpiredTokenException**

The security token included in the request has expired. Request a new security token and try again.

HTTP Status Code: 403

**IncompleteSignature**

The request signature doesn't conform to AWS standards. Verify that you're using valid AWS credentials and that your request is properly formatted. If you're using an SDK, ensure it's up to date.

HTTP Status Code: 400

**InternalFailure**

The request can't be processed right now because of an internal server issue. Try again later. If the problem persists, contact AWS Support.

HTTP Status Code: 500

**InvalidParameterCombination**

Parameters that must not be used together were used together. Remove one of the conflicting parameters and try again.

HTTP Status Code: 400

**InvalidParameterValue**

A value that you provided for a parameter isn't valid. Check the parameter constraints and try again.

HTTP Status Code: 400

**InvalidQueryParameter**

The AWS query string is malformed or doesn't adhere to AWS standards. Verify the query string format and try again.

HTTP Status Code: 400

**MalformedQueryString**

The query string contains a syntax error. Verify the query string and try again.

HTTP Status Code: 404

**MissingAction**

The request is missing the Action parameter. Add the Action parameter and try again.

HTTP Status Code: 400

**MissingAuthenticationToken**

The request must contain a valid AWS access key ID or X.509 certificate. Verify that your credentials are included in the request.

HTTP Status Code: 403

**MissingParameter**

A required parameter for the specified action isn't included in the request. Add the missing parameter and try again.

HTTP Status Code: 400

**NotAuthorized**

You don't have permissions to perform this action. Verify that your IAM policy includes the required permissions.

HTTP Status Code: 401

**OptInRequired**

Your AWS account needs a subscription for this service. Verify that you've enabled the service in your account.

HTTP Status Code: 403

**RequestExpired**

The request has expired. This can happen if the request took more than 15 minutes to reach the service, the date stamp is more than 15 minutes in the future, or a pre-signed URL has expired. Generate a new request with a current timestamp and try again.

HTTP Status Code: 400

**ServiceUnavailable**

The service is temporarily unavailable. Try again later.

HTTP Status Code: 503

**ThrottlingException**

Your request rate is too high. The AWS SDKs automatically retry requests that receive this exception. Reduce the frequency of requests.

HTTP Status Code: 400

**UnrecognizedClientException**

The X.509 certificate or AWS access key ID you provided doesn't exist in our records. Verify that you're using valid credentials and that they haven't expired.

HTTP Status Code: 403

**ValidationError**

The input doesn't meet the required format or constraints. Check that all required parameters are included and that values are valid.

HTTP Status Code: 400
