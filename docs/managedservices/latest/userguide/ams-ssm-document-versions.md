# AMS Advanced SSM document versions

SSM documents support versioning. AMS Advanced SSM documents can't be modified from the
customer’s account and can't be re-shared. They're centrally managed and maintained by AMS Advanced in order to operate the account.

Version numbers are incremented with each document update in a specific AWS Region. As
new Regions become available, the same document content in two Regions can have different
version numbers; this is typical and doesn't mean their behavior will be different. If you
want to compare two AMS Advanced SSM documents, we recommend comparing their hashes with the AWS CLI:

```

      aws ssm describe-document \
      --name AWSManagedServices-*`DOCUMENTNAME`* \
      --output text --query "Document.Hash"

```

Two SSM documents are identical if their hashes match.
