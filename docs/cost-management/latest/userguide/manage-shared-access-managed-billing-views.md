# Understanding AWS managed billing views

AWS managed billing views are created when you map accounts to Billing Conductor billing groups or use billing transfer.

There are two types of AWS managed billing views: Billing group views, and billing transfer billing views.

###### The two types of billing transfer billing views:

- My view - Shows the billing data that your bill transfer account is financially responsible for
- Showback/chargeback view - Shows billing data configured for showback or chargeback purposes
  AWS creates and manages these billing views, so you can't update or delete them directly. The **Cost Management Preferences** billing view tab currently shows only custom views, not AWS managed views.

To update an AWS managed view name, update the name of its associated resource (billing group or billing transfer). AWS managed views persist even if their associated resource is deleted or withdrawn.
