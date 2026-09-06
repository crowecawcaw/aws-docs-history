

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Enable access to the new AMS Tools account
<a name="tools-account-enable"></a>

Once the tools account is created, AMS provides you with an account ID. Your next step is to configure access to the new account. Follow these steps.

1. Update the appropriate Active Directory groups to the appropriate account IDs.

   New AMS-created accounts are provisioned with the ReadOnly role policy as well as a role to allow users to file RFCs.

   The Tools account also has an additional IAM role and user available:
   + IAM role: `AWSManagedServicesMigrationRole`
   + IAM user: `customer_cloud_endure_user`

1. Request policies and roles to allow service integration team members to set up the next level of tools.

   Navigate to the AMS console and file the following RFCs:

   1. Create KMS key. Use either [Create KMS Key (auto)](https://docs.aws.amazon.com/managedservices/latest/ctref/ex-kms-key-create-auto-col.html) or [Create KMS Key (managed automation)](https://docs.aws.amazon.com/managedservices/latest/ctref/ex-kms-key-create-rr-col.html).

      As you use KMS to encrypt ingested resources, using a single KMS key that is shared with the rest of the Multi-Account Landing Zone application accounts, provides security for ingested images where they can be decrypted in the destination account. 

   1. Share the KMS key.

      Use the Management \| Advanced stack components \| KMS key \| Share (managed automation) change type (ct-05yb337abq3x5) to request that the new KMS key be shared with your application accounts where ingested AMIs will reside.

Example graphic of a final account setup:

![AWS architecture diagram showing Migration VPC, IAM, and Permissions with various components and connections.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/WIGS_Account_ExpandedV1.png)
