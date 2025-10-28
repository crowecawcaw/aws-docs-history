# Use an existing Amazon Cognito user pool with a new PCUI instance

Complete the following steps to use an existing Amazon Cognito user pool with a new PCUI instance

###### Use an existing Amazon Cognito user pool with a new PCUI instance

1. In the **CloudFormation console**, select the PCUI stack that contains the Amazon Cognito user pool
   that you want to use with multiple PCUI instances.
2. Navigate to the nested stack that created the Amazon Cognito userpool.
3. Select the **Outputs** tab.
4. Copy the values of the following parameters:
   - `UserPoolId`
   - `UserPoolAuthDomain`
   - `SNSRole`

5. Deploy a new PCUI instance by using the quick-create link, and fill in all `External PCUI Amazon Cognito` parameters with the
   outputs that you copied. This prevents the new PCUI stack from creating a new pool and links it to the existing Amazon Cognito user pool that was
   created from a nested stack. You can deploy subsequent new PCUI instances that have the same parameter values, and you can link them to the Amazon Cognito user
   pool.
