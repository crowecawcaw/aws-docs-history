# Updating the API

In this section, you will learn how to use one of the two available options to update the API.

**Upgrading to a newer AWS ParallelCluster version**

Option 1: To remove the existing API, delete the corresponding CloudFormation stack and deploy the
new API as shown above.

Option 2: To update the existing API, run the following commands:

```
`$` `REGION=`<region>``
`$` `API_STACK_NAME=`<stack-name>``  # This needs to correspond to the existing API stack name
`$` `VERSION=3.14.1`
`$` `aws cloudformation update-stack \
   --region ${REGION} \
   --stack-name ${API_STACK_NAME} \
   --template-url https://${REGION}-aws-parallelcluster.s3.${REGION}.amazonaws.com/parallelcluster/${VERSION}/api/parallelcluster-api.yaml \
   --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND`
`$` `aws cloudformation wait stack-update-complete --stack-name ${API_STACK_NAME} --region ${REGION}`
```
