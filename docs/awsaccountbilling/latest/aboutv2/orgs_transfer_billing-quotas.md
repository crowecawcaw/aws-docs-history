# Quotas

Billing transfer quotas are managed using AWS Service Quotas. You can view your current quota values and request increases to some of these values by visiting [Service Quotas console](https://console.aws.amazon.com/servicequotas "https://console.aws.amazon.com/servicequotas"). The following are the default maximums for billing transfer entities.

The following are the _default_ maximums for billing transfer entities.

## Maximum values

**Terms and concepts**

The following are terms and concepts for billing transfers:

- **Inbound billing**: Billing transfers that allow you to manage and pay for another organization’s consolidated bill.
- **Outbound billing**: Billing transfers that allow an account outside your organization to manage and pay your consolidated bill.
- **Bill-transfer chain**: A collection of billing transfers that are interconnected (e.g., Organization A transfers to Organization B, and Organization B transfers to Organization C).

###### Note

- These quotas apply only to actions performed from the AWS Organizations management account.
- AWS Organizations is a global service that is physically hosted in the US East (N. Virginia) Region (`us-east-1`). Therefore, you must use `us-east-1` to access these quotas when using the Service Quotas console, the AWS CLI, or an AWS SDK.

| Description                   | Limit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inbound billing transfers     | 0<br>• The maximum number of external organizations that you can manage and pay for at any given time. This quota is adjustable, and can be increased by using Service Quotas console.<br>\*_Note:_<br>• Only the Management account of an organization can submit this quota increase request. Limit increases can be granted up to 1,000 based on customer qualifications and requirements.<br>Each \*billing transfer invitation<br>• you send counts against this quota. The count is returned if the invitation is declined, canceled, or expired.                                     |
| Outbound billing transfers    | 1 – The maximum number of external organizations that you can have manage and pay for your consolidated bill at any given time. This quota is not adjustable.<br>Each \*billing transfer invitation<br>• you accept counts against this quota. The count is returned if the billing transfer is withdrawn.                                                                                                                                                                                                                                                                                  |
| Length of bill-transfer chain | 1 – The maximum number of interconnections each of your billing transfers can have at any given time. For example: Organization A transfers to Organization B (length 1). This quota is adjustable, and can be increased by using Service Quotas console.<br>\*_Note:_<br>• Only the Management account of an organization can submit this quota increase request. Limit increases can be granted up to 2 based on customer qualifications and requirements. For example, Organization A transfers to Organization B (length 1), and Organization B transfers to Organization C (length 2). |
| Aggregate inbound transfers   | 1,000<br>• The maximum total number of inbound transfers allowed<br>across all your bill-transfer chains. This quota is not<br>adjustable.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
