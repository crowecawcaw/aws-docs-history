

# Channel is suspended
<a name="msk-data-delivery-iceberg-ts-suspended"></a>

## Suspension on a previously working Channel
<a name="msk-data-delivery-iceberg-ts-suspended-working"></a>
+ **Symptom:** Delivery was working, then the Channel becomes `SUSPENDED` and no new data appears at the destination.
+ **Causes:** The destination table created by the Channel may have been deleted.
+ **Resolution:** The Channel is suspended. If needed, create a new Channel.

## Suspension on a Channel that never delivered data
<a name="msk-data-delivery-iceberg-ts-suspended-never"></a>
+ **Symptom:** No data appears at the destination after the Channel is created, and the Channel becomes `SUSPENDED`.
+ **Causes:** The data type of the configured partition column cannot be transformed to a time-based partition.
+ **Resolution:** The Channel is suspended. If needed, create a new Channel.