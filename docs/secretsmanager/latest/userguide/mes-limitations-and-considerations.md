

# Limitations and considerations
<a name="mes-limitations-and-considerations"></a>

Managed external secrets does not support ephemeral secrets with lifespans less than four hours. Secrets associated with public key infrastructure certificates are also not supported.

 The managed external secrets are supported only for partners that have onboarded with AWS Secrets Manager. For a complete list, see [Integration Partners](mes-partners.md). Don't see your partner on the list? [Tell them to Onboard to AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/mes-onboarding/secrets-manager-mes-onboarding.html) 

If you update or rotate secret values directly from the partner client service outside of the Secrets Manager rotation engine, the synchronization between systems may break. While Secrets Manager provides console warnings and programmatic prevention for manual secret value updates, you can still modify values directly in your third party application. To re-establish synchronization after out-of-band updates, you must update the secret value to reflect the correct secret and then invoke the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) API to ensure continued successful rotations. 