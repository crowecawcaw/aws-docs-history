# Copying adapters

Adapter Versions can be copied from one AWS account to another within AWS Regions.

In order to copy an adapter, you must have created an adapter in the destination AWS
account using the Console or API. You are not required to train an adapter version, but
the meta data (Adapter name and description) for the adapter must exist. This is to
ensure you/your organization have access to the destination account.

###### Note

Your source and destination AWS accounts must be in the same AWS region to successfully
copy an adapter. Please check the account regions before attempting to copy.

Once you have created an adapter, submit a support ticket with the following
details. You will need a support subscription before submitting the ticket:

```

**Region: xxx**

**Source:**
AWS Account:
Adapter ID:
Adapter Version:

**Destination:**
AWS Account:
Adapter ID:

```

Once the adapter is copied over, you can use the destination adapter
ID and version to make inference calls. You can test the inference API
output using the same set of queries you used to train the source adapter.
The destination adapter will return the same results as the source adapter.
