# Restricted network environments

Deadline Cloud provides tools that are used by artists or other users on their local workstations. These tools require access to AWS API and web endpoints to perform their function. If you filter access to specific AWS domains or URL endpoints by using a web content filtering solution such as next-generation firewalls (NGFW) or Secure Web Gateways (SWG), you must add the following domains or URL endpoints to your web-content filtering solution allowlists.

## AWS API endpoints to allowlist

Deadline Cloud client tools, such as the AWS Management Console, monitor, CLI, and integrated submitters, require access to AWS APIs in addition to Deadline Cloud. These endpoints only support IPv4.

- `scheduling.deadline.`[Region]`.amazonaws.com`
- `management.deadline.`[Region]`.amazonaws.com`
- `logs.`[Region]`.amazonaws.com`
- `ec2.`[Region]`.amazonaws.com`
- `s3.`[Region]`.amazonaws.com`
- `sts.`[Region]`.amazonaws.com`
- `identitystore.`[Region]`.amazonaws.com`

## Web domains to allowlist

The Deadline Cloud monitor requires access to the following domains to operate.

For additional information about allowlisting domains for AWS Sign-In, see [Domains to add to your allow list](../../../signin/latest/userguide/allowlist-domains.md "../../../signin/latest/userguide/allowlist-domains.md") in the _AWS Sign-In User Guide_.

- `downloads.deadlinecloud.amazonaws.com`
- `d2ev1rdnjzhmnr.cloudfront.net`
- `prod.log.shortbread.aws.dev`
- `prod.tools.shortbread.aws.dev`
- `prod.log.shortbread.analytics.console.aws.a2z.com`
- `prod.tools.shortbread.analytics.console.aws.a2z.com`
- `global.help-panel.docs.aws.a2z.com`
- ``[Region]`.signin.aws.amazon.com`
- `sso.`[Region]`.amazonaws.com`
- `portal.sso.`[Region]`.amazonaws.com`
- `oidc.`[Region]`.amazonaws.com`
- `assets.sso-portal.`[Region]`.amazonaws.com`

The Deadline Cloud submitter requires access to the following domains to download GUI dependencies.

- `pypi.python.org`
- `pypi.org`
- `pythonhosted.org`
- `files.pythonhosted.org`

## Environment-specific endpoints to allowlist

These domains vary depending on the specific configuration of Deadline Cloud. If additional Deadline Cloud monitors or queues are created, additional domains will need to be allowlisted.

- ``[Directory ID or alias]`.awsapps.com`

This domain is tied to the IAM Identity Center setup and should be the same for all setups in this using the same IAM Identity Center instance. The exact value can be found by the enterprise admin in the IAM Identity Center console under _Settings_ → _AWS access portal URL_.

- ``[Monitor alias]`.`[Region]`.deadlinecloud.amazonaws.com`

This is the domain of the Monitor setup in Deadline Cloud. This is the link that artists will enter into their browser or Deadline Cloud monitor application. If Deadline Cloud is set up in additional accounts or regions in the future this domain will change. This value can be found in the Deadline Cloud console in the _Dashboard_ → _Monitor overview_ → _Monitor details_ → _URL_.

- ``[Bucket name]`.`[Region]`.s3.amazonaws.com`

This is the domain for the job attachments bucket used by Deadline Cloud queues. Each queue can have its own job attachments bucket configured. The exact bucket name can be found in the Deadline Cloud console under _Queues_ → _Queue details_ → _Job attachments_. For more information about job attachments, see the queues documentation.
