AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# FAQs about the replication

process

The following section aims to answer some FAQs related to the replication tool, and the replication process.

**Question:** If I replicate my AWS Cloud9 environment on CodeCatalyst, will my AWS Cloud9 environment be impacted?

**Answer:** No, the replication of your environment will only copy over your code resources to AWS Cloud9 in CodeCatalyst enabling you to continue working.
Your code resources and environment on AWS Cloud9 will not be affected in any way.

**Question:** If I want to rollback, will my AWS Cloud9 environment be impacted?

**Answer:** No, you can delete the CodeCatalyst Dev Environment, source repositories, project and space and it will have no affect on your
AWS Cloud9 environment.

**Question:** Will the new location be
compliant with standards like HIPAA, SOC, etc?

**Answer:** The Dev Environment on CodeCatalyst is
currently not compliant with these standards. Compliance with these
standards is on the roadmap.

**Question:** Where will my code resources go?

**Answer:** Your code resources will be copied to source repositories within your project in CodeCatalyst.

**Question:** Will my usage be limited?

**Answer:** As part of the replication process you will create Dev Environments that have 16 GB within the free tier. This means
you can have a maximum of 4 Dev Environments. For more information on pricing, storage and the different tiers available, see [Amazon CodeCatalyst -
Pricing](https://codecatalyst.aws/explore/pricing "https://codecatalyst.aws/explore/pricing").

**Question:** Where will my compute go?

**Answer:** There will be no change to your existing compute. It will remain as is.

**Question:** Can I use my existing AWS account credentials in CodeCatalyst, and will they be automatically transferred?

**Answer:** You can configure your AWS account credentials manually in CodeCatalyst. They will not be automatically transferred.

**Question:** How much will this cost?

**Answer:** You can get started using CodeCatalyst
for free. For more information on pricing and the different tiers available,
see [Amazon CodeCatalyst -
Pricing](https://codecatalyst.aws/explore/pricing "https://codecatalyst.aws/explore/pricing").

**Question:** Is the data replication process and data storage in CodeCatalyst safe?

**Answer:** Yes, we will use git push with https to copy the code resources and CodeCatalyst securely stores data within the service. All data is
encrypted in transit and at rest. For more information on data protection in CodeCatalyst, see [Data
protection in Amazon CodeCatalyst](../../../codecatalyst/latest/userguide/data-protection.md "../../../codecatalyst/latest/userguide/data-protection.md") in the _Amazon CodeCatalyst User Guide_.

**Question:** Which replication approach should I choose?

**Answer:** The replication tool offers two
approaches; you can copy your code resources from AWS Cloud9 to CodeCatalyst by pushing
them to a single CodeCatalyst source repository, or each subfolder translates into
a distinct CodeCatalyst source repository. We recommend using the first approach
as it doesn't require prior knowledge of CodeCatalyst concepts such as source
repositories. This approach is a good starting point to explore the AWS Cloud9
experience in CodeCatalyst, while working with a similar setup you are used to in
AWS Cloud9.

The second option is best chosen when you are using the subfolders located
under the root AWS Cloud9 environment folder independently. With this approach,
any files under the root folder will not be replicated. For more information
on source repositories in CodeCatalyst, see [Source repositories in CodeCatalyst](../../../codecatalyst/latest/userguide/source.md "../../../codecatalyst/latest/userguide/source.md") in the
_Amazon CodeCatalyst User Guide_.

**Question:** What is the personal access token
generated in the replication process and why do I need it? Can I generate it
again if I lose it?

**Answer:** The personal access token is
associated with your user identity in CodeCatalyst. It is required as a password
when you push local changes with git to CodeCatalyst source repositories. For more
information on the token and how to generate it, see [Managing
personal access tokens in Amazon CodeCatalyst](../../../codecatalyst/latest/userguide/ipa-tokens-keys.md "../../../codecatalyst/latest/userguide/ipa-tokens-keys.md") in the _Amazon CodeCatalyst
User Guide_.

**Question:** What happens if there is an error during the replication process?

**Answer:** If an error occurs when using the replication tool you should first try the tool again. If the error relates to
the source repositories, you can manually push your code resources to the CodeCatalyst source repositories once they have been replicated. This should work as the local repositories
have already been configured to work with CodeCatalyst upstream. If an issue persists, please create and submit a support case. For information on
creating a support case, see [Creating support cases and case
management](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md").

**Question:** Why do I need to authenticate and give permissions to the replication tool using my AWS BuilderID?

**Answer:** During the replication process the
replication tool needs to read and write multiple resources (projects,
Dev Environments, source repositories) in CodeCatalyst and copy local contents on the
behalf of the user, so it requires your permission to do this.

**Question:** Will there be a change in latency
if I move to CodeCatalyst?

**Answer:** Depending on the actions you are doing you may see a reduction in latency. This is due to the CodeCatalyst server being hosted in
the PDX region.

**Question:** Will all my installed software transfer over?

**Answer:** No, only your code resources will be transferred. Binaries, configurations and installed software
will not be transferred.
