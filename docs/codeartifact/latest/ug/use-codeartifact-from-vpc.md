# Use CodeArtifact from a VPC

If you cannot or do not want to enable private DNS on your
`com.amazonaws.`region`.codeartifact.repositories` VPC endpoint that you created in
[Create VPC endpoints for CodeArtifact](create-vpc-endpoints.md "create-vpc-endpoints.md"), you must
use a different configuration for the repositories endpoint to use CodeArtifact from a VPC. Follow the instructions in
[Use the codeartifact.repositories endpoint without private DNS](#use-codeartifact-from-vpc-no-private-dns "#use-codeartifact-from-vpc-no-private-dns") to
configure CodeArtifact if the `com.amazonaws.`region`.codeartifact.repositories` endpoint does not have
private DNS enabled.

## Use the `codeartifact.repositories` endpoint without private DNS

If you cannot or do not want to enable private DNS on your
`com.amazonaws.`region`.codeartifact.repositories` VPC endpoint that you created in
[Create VPC endpoints for CodeArtifact](create-vpc-endpoints.md "create-vpc-endpoints.md"), you must follow these instructions to configure your
package manager with the correct CodeArtifact URL.

1. Run the following command to find a VPC endpoint to use to override the
   hostname.

```
$ aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=com.amazonaws.`region`.codeartifact.repositories \
  --query 'VpcEndpoints[*].DnsEntries[*].DnsName'
```

The output looks like the following.

```
[
  [
    "vpce-0743fe535b883ffff-76ddffff.d.codeartifact.us-west-2.vpce.amazonaws.com"
  ]
]
```

2. Update the VPC endpoint path to include the package format, your CodeArtifact domain name, and CodeArtifact repository name. See the following example.

```
https://vpce-0743fe535b883ffff-76ddffff.d.codeartifact.us-west-2.vpce.amazonaws.com/`format`/d/`domain_name`-`domain_owner`/`repo_name`
```

Replace the following fields from the example endpoint.

    * `format`: Replace with a valid CodeArtifact package format, for example, `npm` or `pypi`.
    * `domain_name`: Replace with the CodeArtifact domain that contains the CodeArtifact repository that hosts your packages.
    * `domain_owner`: Replace with the ID of the owner of the CodeArtifact domain, for example, `111122223333`.
    * `repo_name`: Replace with the CodeArtifact repository that hosts your packages.

The following URL is an example npm repository endpoint.

```
https://vpce-0dc4daf7fca331ed6-et36qa1d.d.codeartifact.us-west-2.vpce.amazonaws.com/npm/d/domainName-111122223333/repoName
```

3. Configure your package manager to use the updated VPC endpoint from the previous step. You must configure the package manager without
   using the CodeArtifact `login` command. For configuration instructions for each package format, see the following documentation.
   - npm: [Configuring npm without using the
     login command](npm-auth.md#configuring-npm-without-using-the-login-command "npm-auth.md#configuring-npm-without-using-the-login-command")
   - nuget: [Configure nuget or dotnet without the login command](nuget-cli.md#nuget-configure-without-login "nuget-cli.md#nuget-configure-without-login")
   - pip: [Configure pip without the login
     command](python-configure-pip.md#python-configure-without-pip "python-configure-pip.md#python-configure-without-pip")
   - twine: [Configure and use twine with CodeArtifact](python-configure-twine.md "python-configure-twine.md")
   - Gradle: [Use CodeArtifact with Gradle](maven-gradle.md "maven-gradle.md")
   - mvn: [Use CodeArtifact with mvn](maven-mvn.md "maven-mvn.md")
