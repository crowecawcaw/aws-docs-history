# Creating custom IAM

policy statements to administer Amazon Neptune

Administrative policy statements let you control what an IAM user can do to manage
a Neptune database.

A Neptune administrative policy statement grants access to one or more [administrative actions](neptune-iam-admin-actions.md "neptune-iam-admin-actions.md") and [administrative resources](iam-admin-resources.md "iam-admin-resources.md") that Neptune supports.
You can also use [Condition Keys](iam-admin-condition-keys.md "iam-admin-condition-keys.md") to make the administrative
permissions more specific.

###### Note

Because Neptune shares functionality with Amazon RDS, administrative actions,
resources, and service-specific condition keys in administrative policy statements use
an `rds:` prefix by design.

###### Topics

- [IAM actions for administering Amazon Neptune](neptune-iam-admin-actions.md "neptune-iam-admin-actions.md")
- [IAM resource types for administering Amazon Neptune](iam-admin-resources.md "iam-admin-resources.md")
- [IAM condition keys for administering Amazon Neptune](iam-admin-condition-keys.md "iam-admin-condition-keys.md")
- [Creating IAM administrative
  policy statements for Amazon Neptune](iam-admin-policy-examples.md "iam-admin-policy-examples.md")
