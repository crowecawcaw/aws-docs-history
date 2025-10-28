# Limiting permissions to

include or exclude AWS Resilience Hub recommendations

AWS Resilience Hub enables you to restrict permissions to include or exclude
recommendations per application. You can restrict permissions to include or exclude
recommendations per application using the following IAM trust policy. In this
IAM trust policy, `caller_IAM_role` (associated with your AWS user
account) is used in the current account to call the APIs for AWS Resilience Hub.
