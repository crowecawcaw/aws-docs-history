# What is a customer profile in

Amazon Connect?

A _customer profile_ is a record that stores contact history
combined with information about customers, such as account number, additional
information, birth date, email, multiple addresses, name, and party type. An
_account-based profile_ is expected to have underlying
sub-profiles.

After you enable Amazon Connect Customer Profiles, a unique customer profile is created for every contact.
This allows you to create a customer profile that has all the information agents need
during customer interactions in a single place at no charge.

To access customer profiles in your flows, use the [Customer profiles](customer-profiles-block.md "customer-profiles-block.md")
block. [Agents access customer profiles](customer-profile-access.md "customer-profile-access.md") in
their agent workspace.

You can use the paid features of Customer Profiles to enrich your customer profiles by [ingesting data from external
applications](integrate-external-apps-customer-profiles.md "integrate-external-apps-customer-profiles.md"). See [pricing](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/") for details.

You can also add custom fields and objects to the customer profiles by using the
[Amazon Connect Customer Profiles APIs](../../../customerprofiles/latest/APIReference/Welcome.md "../../../customerprofiles/latest/APIReference/Welcome.md").

## How is customer profile data

stored?

Amazon Connect stores contact history in unique customer profiles. It parses data ingested
from external applications and stores it as customer profile attributes.

Amazon Connect does not replace or update the data in the external application. If a data
source is removed, the data from the external application is no longer available in
the customer profile for every voice contact.

For information about how customer profile data are secured, see [Data protection in Amazon Connect](data-protection.md "data-protection.md").

For more information about how to access the data that is stored in a customer
profile, see [Access Customer
Profiles in the agent workspace](customer-profile-access.md "customer-profile-access.md") or [Use the Customer
Profiles API](use-customerprofiles-api.md "use-customerprofiles-api.md").
