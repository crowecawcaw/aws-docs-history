# Index capacity

An index is a structured corpus of documents that allows for efficient searching, sorting,
and data access. Amazon Quick Suite uses an index to store, prepare, sync any files you upload to
your Quick Suite spaces. It then uses this indexed data to generate agent-driven
responses during chat conversations.

You must purchase data storage capacity for your Quick Suite index.
Quick Suite automatically creates an index when you sign up in your home region, and
auto-provisions 50 MB default index capacity with auto-scaling enabled (a mechanism where
your index capacity is adjusted automatically based on usage). In any other region, an admin
has to explicitly provision index capacity. The minimum index capacity you can purchase is
25 MB. The maximum is 10,000 MB.

The Amazon Quick Suite admin console displays both your purchased index capacity and your index
capacity usage. You can switch between manual and auto-scaled index capacity modes as per
your needs. When you are buying capacity manually, you can also release unused capacity. If
you want to release all provisioned index capacity, you could do so after deleting
corresponding data—like file uploads in spaces and knowledge bases— in your
Amazon Quick Suite instance.

###### Topics

- [Total index capacity](#index-data-capacity "#index-data-capacity")
- [To view index capacity usage](#used-index-data-capacity "#used-index-data-capacity")
- [Release unused index capacity](#release-index-data-capacity "#release-index-data-capacity")
- [Switch between capacity modes](#switch-capacity-modes "#switch-capacity-modes")

## Total index capacity

You must purchase data storage capacity for your Amazon Quick Suite index to ingest data
from knowledge bases and upload files to spaces. In the index capacity page, the first
horizontal bar shows your total index capacity. This is the current capacity available
in your index to support file uploads and knowledge bases. When you first signup, the
capacity shown here is the auto-provisioned 50 MB in the home region. When auto-scaling
mode is **ON**, this capacity automatically adjusts to reflect the
latest available capacity based on your ingestion needs. When manual mode is
**ON**, this total capacity represents the actual capacity you have
purchased for your account based on your estimate of the ingestion needs.

###### Note

With auto-scaling enabled, Amazon Quick Suite may temporarily provision capacity above
your maximum purchase limit during periods of high concurrent usage to maintain
performance. However, you are only charged for capacity up to your configured
maximum purchase limit, not for any temporary over-provisioning that occurs.

###### To manage purchase options

1. Log in to the Amazon Quick Suite console.
2. Select **Manage Quick Suite**.
3. From the admin console left navigation menu, select
   **Subscriptions**, and then select **Index
   capacity**.
4. In **Index capacity**, from **Total index
   capacity** select **Manage capacity**, and do the
   following:
   1. In **Manage purchase options**, do one of the
      following:
      1. To automatically scale index capacity as per usage, select
         **Auto-scale (Recommended)**. This
         automatically adjusts index capacity in 25 MB increments based
         on your usage, purchasing or releasing as needed. Then, in
         **Maximum purchase limit** set the limit at
         which auto-purchase stops. The value of the maximum purchase
         limit must be 10,000. Maximum purchase limit cannot be lower
         that current used capacity.
      2. To manually purchase capacity, select
         **Manual**. Then, in **Index
         capacity**, set the total capacity you want your
         index to hold. The capacity must be between 25-10,000 MB and you
         can increase it in 25 MB increments. When you want to lower the
         current capacity held by the index, it can't be lowered below
         the used capacity. Since capacity is managed in 25 MB
         increments, you can only decrease to the next 25 MB unit above
         your current usage. For example, if your index has 200 MB
         capacity with 110 MB consumed, you can reduce capacity to 125 MB
         but not to 100 MB since part of the 100-125 MB unit is already
         in use.

   2. Select **Confirm**.

## To view index capacity usage

The Amazon Quick Suite admin console diplays both your purchased index capacity and your
index capacity usage. The following procedure shows you how to view them.

###### To view index data capacity usage

1. Log in to the Amazon Quick Suite console.
2. Select **Manage Quick Suite**.
3. From the left navigation menu, select **Subscriptions**, and
   then select **Index capacity**.
4. In **Index capacity**, you'll find your capacity usage under
   **Index capacity usage**. First bar shows you total
   purchased capacity and second bar shows you index capacity usage.

## Release unused index capacity

The Amazon Quick Suite admin console diplays both your purchased index capacity and your
index capacity usage. If you've manually provisioned capacity, you can choose to release
unused index capacity. If you've
enabled auto-scaling for your index, you don't need to release index capacity as
Amazon Quick Suite automatically scales index capacity to your usage.The following procedure
shows you how to release unused index capacity.

###### Note

To release any provisioned index capacity, you must delete all datasets and files
uploaded to spaces. Then, follow the steps to release unused index capacity.

###### To release index data capacity

1. Log in to the Amazon Quick Suite console.
2. Select **Manage Quick Suite**.
3. From the left navigation menu, select **Subscriptions**, and
   then select **Index capacity**.
4. In **Index capacity**, select **Manage
   capacity**.
5. In **Manage index capacity**, reduce the **Index
   capacity** to your desired value.

## Switch between capacity modes

You can switch between manual and auto-scale index capacity modes at any time. When
switching from auto-scale to manual, your current capacity becomes your fixed manual
capacity. When switching from manual to auto-scale, you set a maximum purchase limit and
Amazon Quick Suite automatically adjusts capacity based on usage.

To switch from auto-scale to manual capacity

1. Log in to the Amazon Quick Suite console.
2. Select **Manage Quick Suite**.
3. From the admin console left navigation menu, select
   **Subscriptions**, and then select
   **Index capacity**.
4. In **Index capacity**, from **Total index
   capacity** select **Manage
   capacity**.
5. In **Manage index capacity**, select
   **Manual**.
6. In **Index capacity**, set your desired manual
   capacity. The value must be between 25-10,000 MB in 25 MB increments
   and can't be less than current usage.
7. Select **Confirm**.

To switch from manual to auto-scale capacity

1. Log in to the Amazon Quick Suite console.
2. Select **Manage Quick Suite**.
3. From the admin console left navigation menu, select
   **Subscriptions**, and then select
   **Index capacity**.
4. In **Index capacity**, from **Total index
   capacity** select **Manage
   capacity**.
5. In **Manage index capacity**, select
   **Auto-scale (Recommended)**.
6. In **Maximum purchase limit**, set your maximum
   purchase limit. The value must be between 25-10,000 MB in 25 MB
   increments and can't be less than current usage.
7. Select **Confirm**.
