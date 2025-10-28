# Variation in operations between the AWS Control Tower

console and APIs for baselines

When you change the governance status of an OU, the AWS Control Tower console performs more
operations for you automatically, compared to changing governance by means of the APIs
for baselines.

###### Differences

- **Registering and provisioned products**

When you register an OU through the console, AWS Control Tower creates Service Catalog products
for the OU's member accounts, as part of enrolling each account. When you
register an OU by means of the `EnableBaseline` API and the
`AWSControlTowerBaseline`, AWS Control Tower does not create provisioned
products for the member accounts in the OU.

- **Deregister an OU**

Any time you deregister an OU, you must first remove all member accounts and
nested OUs. Then, AWS Control Tower removes all controls that are applied to the
OU.

    + If you select **Delete OU** the OU from the console,
     AWS Control Tower proceeds to deregister and then delete the OU from your
     organization.
    + However, if you deregister the OU by calling the
     `DisableBaseline` API to remove the
     `AWSControlTowerBaseline` from the OU, AWS Control Tower does not
     delete the OU from your organization, the OU is still present in the
     organization, unregistered.
