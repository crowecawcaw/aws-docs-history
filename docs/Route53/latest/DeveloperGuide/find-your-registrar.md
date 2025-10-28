# Finding your registrar and other information about

your domain

To view domain information by using the [GetDomainDetail](../APIReference/API_domains_GetDomainDetail.md "../APIReference/API_domains_GetDomainDetail.md") API, you can use any of the SDKs or AWS CLI. For more
information, see [get-domain-detail](../../../cli/latest/reference/route53domains/get-domain-detail.md "../../../cli/latest/reference/route53domains/get-domain-detail.md").

###### To view information

about domains with `get-domain-detail` CLI

- Use the following CLI:

```

aws route53domains get-domain-detail \
    --region us-east-1 \
    --domain-name `example.com`

```

###### Note

This command only runs in us-east-1 AWS Region.

All the information about your domain will be listed in the output, including
the registrar, registration date, privacy setting, etc.
