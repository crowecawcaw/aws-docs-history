# Learn about common RFC parameters

The following are RFC parameters that you are required to submit, and parameters that are commonly used in RFCs:

- Change type information: ChangeTypeId and ChangeTypeVersion. Ror a list of change type IDs and
  version numbers, see
  [Change Type Reference](../ctref/index.md "../ctref/index.md").

Run `list-change-type-classification-summaries` in the CLI with the `query` argument to narrow the results. For example, narrow results to
change types that contain "Access" in the `Item` name.

```
aws amscm list-change-type-classification-summaries --query "ChangeTypeClassificationSummaries [?contains (Item, 'access')].[Category,Subcategory,Item,Operation,ChangeTypeId]" --output table
```

Run `get-change-type-version` and specify the change type ID. The following command gets the CT version for ct-2tylseo8rxfsc.

```
aws amscm get-change-type-version --change-type-id ct-2tylseo8rxfsc
```

- Title: A name for the RFC; this becomes the **Subject** of the RFC in the AMS console RFC
  list and you can search on it with the `GetRfc` command and a filter on `Title`
- Scheduling: If you want a scheduled RFC, you must include the `RequestedStartTime`
  and `RequestedEndTime` parameters, or use the **Schedule this
  change** console option. For an **ASAP** RFC (that runs as
  soon as it's approved), when using the CLI, leave `RequestedStartTime` and
  `RequestedEndTime` null. When using the console, accept the
  **ASAP** option.

If the `RequestedStartTime` is missed, the RFC is rejected.

- Provisioning CTs: The execution parameters, or `Parameters` are the specific settings that are required to
  provision the resource. They vary widely depending on the CT.
- Non-provisioning CTs: CTs that do not provision a resource, such as access CTs or Other | Other, or delete stack,
  have minimal execution parameters and no `Parameters` block.
- Some RFCs also require that you specify a `TimeoutInMinutes`, or how many minutes
  are allowed for the creation of the stack before the RFC is failed. Valid values are 60
  (minutes) up to 360, for long-running UserData. If the execution can't be completed
  before the `TimeoutInMinutes` is exceeded, the RFC fails. However, this
  setting doesn't delay the execution of the RFC.
- RFCs that create instances, such as an S3 bucket or an ELB, generally provide a schema that
  allows you to add up to seven tags (key/value pairs). You can add more tags to your S3
  bucket by submitting an RFC using the Deployment | Advanced stack components | Tag | Create change type (ct-3cx7we852p3af). EC2,
  EFS, RDS, and the multi-tiered (HA Two-Tiered and HA One-Tiered) schemas allow up to
  fifty tags. Tags are specified in the `ExecutionParameters` part of the
  schema. Providing tags can be of great value. For more information, see
  [Tagging Your Amazon EC2 Resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md").

When using the AMS console, you must open the **Additional configuration** area in order to add tags.

###### Tip

Many CT schemas have a `Description` and `Name` field near
the top of the schema. Those fields are used to name the stack or stack component,
they don't name the resource you're creating. Some schemas offer a parameter to name
the resource you're creating, and some do not. For example, the CT schema for Create
EC2 stack doesn't offer a parameter to name the EC2 instance. In order to do so, you
must create a tag with the key "Name" and the value of what you want the name to be.
If you do not create such a tag, your EC2 instance displays in the EC2 console
without a name attribute.

## Use the RFC AWS Region option

The AMS API and CLI (`amscm` and `amsskms`) endpoints are in `us-east-1`. If you federate with Security
Assertion Markup Language (SAML), then scripts are provided to you at onboarding that set your AWS Region to us-east-1. If you use SAML, then you
don't need to specify the `--region` option when you issue a command. If your SAML is configured to use us-east-1 but your account isn't in that AWS Region, then you must specify your account-onboarded Region when you
issue other AWS commands (for example, `aws s3`).

###### Note

Most of the command examples provided in this guide don't include the `--region` option.
