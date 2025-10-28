# Find AMS account settings

Account settings that are used to create AMS RFCs, set schedules, and determine who receives notifications.

Some settings are created during onboarding and require a service request to change. You
should make a note of these account details because you will use them when communicating with AMS:

- **Credentials**: If you need to retrieve your AMS user name or password,
  contact your local IT administrator--AMS uses your corporate Active Directory.
- **Cloud Service Delivery Manager (CSDM)**: This person is your liaison with AMS and is available to answer service questions.
  You are given this person's contact information at onboarding and should keep it available to all in your organization who interact with AMS.
  You can expect to receive monthly reports on your AMS service from this person.
- **Console access**: You access the AMS console at a URL set up specifically for your account. You can get the
  URL from your CSDM.
- **AMS CLI**: You can obtain the AMS CLI through the AMS console **Developer's resources** page, or the
  distributables package that you get from your CSDM. After you have the distributables package, follow the steps outlined in
  [Installing or upgrading the AMS CLI](understand-sent-api.md#install-sent-cli "understand-sent-api.md#install-sent-cli").
- **Maintenance window**: Your maintenance window determines when
  patching happens for your EC2 instances. The AWS Managed Services Maintenance Window (or Maintenance Window) performs maintenance activities for AWS Managed Services (AMS) and recurs the second Thursday of every month from
  3 PM to 4 PM Pacific Time. AMS may change the maintenance window with 48 hours notice. You may have chosen a
  different window at onboarding--keep a record of your chosen maintenance window.
- **Monitoring**: AMS provides a set of CloudWatch metrics by default, but you can also request additional metrics. If you do, keep record of those.
- **Logs**: By default, your logs are stored at ams-a-`ACCOUNT_ID`-log-management-`REGION`
  where `REGION` is the region where the log was generated.
- **Mitigation**: At onboarding, AMS records the mitigation action of your
  choice in case a malware attack against your resources is identified. For example,
  contact certain people. Keep this information available to all in your organization who interact with AMS.
- **Region**: You can look at the VPC details page in the AMS console. You can also run this command after you have installed the
  AMS SKMS CLI (this command uses a SAML profile, remove if your authentication method is different):

```
aws --profile saml amsskms get-vpc --vpc-id `VPC_ID`
```

###### Important

###### Note

The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your
authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1`
when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.
