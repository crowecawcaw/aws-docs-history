

# Update OIDC Identity Provider workforce configuration
<a name="sms-workforce-management-private-api-update"></a>

You may want to update a workforce created using your own OIDC IdP to specify a different authorization endpoint, token endpoint, or issuer. You can update any parameter found in `[OidcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OidcConfig.html)` using the [`UpdateWorkforce`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateWorkforce.html) operation.

**Important**  
You can only update your OIDC IdP configuration when there are no work teams associated with your workforce. You can delete a private work team using the `[DeleteWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkteam.html)` operation.