# Grant access with filters in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio enables fine-grained access control by translating the defined row and
column filters into appropriate grants for AWS Lake Formation and Amazon Redshift.
Below is an explanation of how Amazon SageMaker Unified Studio materializes these filters for both AWS Glue
tables and Amazon Redshift.

## AWS Glue tables

When a subscription to an AWS Glue table with row and/or column filters is
approved, Amazon SageMaker Unified Studio materializes the subscription by creating grants in AWS Lake
Formation with Data Cell Filters, ensuring that the members of the subscriber
project are only able to access the rows and columns they are allowed to access
based on the filters applied to the subscription.

Amazon SageMaker Unified Studio first translates the row and columns filters applied in Amazon SageMaker Unified Studio to
AWS Lake Formation Data Cell Filters. If multiple row and columns filters are
used, Amazon SageMaker Unified Studio unions all the columns and all the row filter conditions to compute
effective permissions at both row and column level. Amazon SageMaker Unified Studio then creates a single
AWS Lake Formation data cell filter using effective row and column permissions.

After the data cell filter is created, Amazon SageMaker Unified Studio shares the subscribed table with
the subscriber project by creating read-only (SELECT) permissions in AWS Lake
Formation using this data cell filter.

## Amazon Redshift

When a subscription to an Amazon Redshift table/view with row and/or column
filters is approved, Amazon SageMaker Unified Studio materializes the subscription by creating
scoped-down late binding views in Amazon Redshift, ensuring that the members of the
subscriber project are only able to access the rows and columns they are allowed to
access based on the row and column filters applied to the subscription.

Amazon SageMaker Unified Studio first translates the row and columns filters applied to a subscription
in Amazon SageMaker Unified Studio to an Amazon Redshift late binding view. If multiple row and columns
filters are used, Amazon SageMaker Unified Studio unions all the columns and all the row filter
conditions from to compute effective permissions at both row and column level.
Amazon SageMaker Unified Studio then creates the late binding view using effective row and column
permissions.

After the late binding view is created, Amazon SageMaker Unified Studio shares this view with the
members of subscriber project by creating read-only (SELECT) permissions in Amazon
Redshift.
