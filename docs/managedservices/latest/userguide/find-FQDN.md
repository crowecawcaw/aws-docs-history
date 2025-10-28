# Find FQDNs in AMS

AWS Managed Services (AMS) access change types (CTs) require the fully qualified domain name, or FQDN, of your AMS-trusted domain, in the form of
`C844273800838.amazonaws.com`. To discover your AWS FQDN, do one of the following:

- AWS Console: Look in the AWS Directory Service console in the **Directory name** column.
- CLI: Use these commands while logged into your domain:

Windows (returns user and FQDN):

```
whoami /upn
```

or (DC+DC+DC=FQDN)

```
whoami /fqdn
```

Linux:

```
hostname --fqdn
```

###### Note

The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your
authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1`
when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.
