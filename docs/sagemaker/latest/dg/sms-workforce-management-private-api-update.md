# Update OIDC Identity Provider workforce

configuration

You may want to update a workforce created using your own OIDC IdP to specify a
different authorization endpoint, token endpoint, or issuer. You can update any
parameter found in `OidcConfig` using the [`UpdateWorkforce`](../APIReference/API_UpdateWorkforce.md "../APIReference/API_UpdateWorkforce.md") operation.

###### Important

You can only update your OIDC IdP configuration when there are no work teams
associated with your workforce. You can delete a private work team using the
`DeleteWorkteam` operation.
