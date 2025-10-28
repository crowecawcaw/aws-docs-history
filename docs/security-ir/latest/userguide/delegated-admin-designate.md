# Designating a delegated administrator for AWS Security Incident Response

This section provides steps to designate a delegated administrator in the AWS Security Incident Response
organization.

As a manager of the AWS organization, make sure that you read through the
[Considerations and
recommendations](considerations_important.md "considerations_important.md") on how a delegated Security Incident Response administrator account operates. Before
proceeding, ensure that you have [Permissions required to designate a
delegated Security Incident Response administrator account](organizations_permissions.md "organizations_permissions.md").

Choose a preferred access method to designate a delegated Security Incident Response administrator account for your organization. Only a
management can perform this step.

Console

1. Open the Security Incident Response console at https://console.aws.amazon.com/security-ir/

To sign in, use the management credentials for your
AWS Organizations organization. 2. By using the AWS Region selector in the upper-right corner of
the page, select the Region in which you want to designate the
delegated Security Incident Response administrator account for your organization. 3. Follow the setup wizard to create your membership, including the delegated administrator account.

API/CLI

- Run CreateMembership using
  the credentials of the AWS account of the organization's
  management.
  - Alternatively, you can use AWS Command Line Interface to do this. The
    following AWS CLI command designates a delegated Security Incident Response administrator account.
    Following are the string options available for configuring your membership:

  ````

                                        {
                                          "customerAccountId": "stringstring",
                                          "membershipName": "stringstring",
                                          "customerType": "Standalone",
                                          "organizationMetadata": {
                                            "organizationId": "string",
                                            "managementAccountId": "stringstring",
                                            "delegatedAdministrators": [
                                              "stringstring"
                                            ]
                                          },
                                          "membershipAccountsConfigurations": {
                                            "autoEnableAllAccounts": true,
                                            "organizationalUnits": [
                                              "string"
                                            ]
                                          },
                                          "incidentResponseTeam": [
                                            {
                                              "name": "string",
                                              "jobTitle": "stringstring",
                                              "email": "stringstring"
                                            }
                                          ],
                                          "internalIdentifier": "string",
                                          "membershipId": "stringstring",
                                          "optInFeatures": [
                                            {
                                              "featureName": "RuleForwarding",
                                              "isEnabled": true
                                            }
                                          ]
                                        }

  ```If AWS Security Incident Response is not enabled for your delegated Security Incident Response administrator account, it won't be able to take
  any action. If not already done so, make sure to enable AWS Security Incident Response for
  the newly designated delegated Security Incident Response administrator account.
  ````
