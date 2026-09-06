

# Capacity reservation columns
<a name="table-dictionary-cur2-capacity-reservation"></a>

Capacity reservation columns contain data about capacity reservations that apply to the line item.



| Column name | Description | Data Type | Nullability | Properties | 
| --- | --- | --- | --- | --- | 
| capacity\_reservation\_capacity\_reservation\_arn | **Table configuration:** Added by: INCLUDE CAPACITY RESERVATION DATA<br />The capacity reservation ARN represents the unique identifier of the capacity reservation | String | Nullable | This field is not null when a charge is related to a capacity reservation<br />This field is not null when a charge represents the unused portion of a capacity reservation<br />This field is null when a charge is not related to a capacity reservation | 
| capacity\_reservation\_capacity\_reservation\_status | **Table configuration:** Added by: INCLUDE CAPACITY RESERVATION DATA<br />Indicates whether the line item represents either the consumption or the cancellation (in the case of Future-dated Capacity reservation) of the capacity reservation identified in the capacity\_reservation\_capacity\_reservation\_arn column or when the capacity reservation is unused or when the capacity reservation is reserved.  | String | Nullable | This field is null when capacity\_reservation\_capacity\_reservation\_arn is null<br />This field is not null when capacity\_reservation\_capacity\_reservation\_arn is not null and line\_item\_line\_item\_type is **Usage** or **SavingsPlannedCoveredUsage** or **DiscountedUsage**<br />This field contains one of the allowed values – Reserved, Cancelling, Used or Unused. <br />The status Cancelling is applicable when a Future-dated Capacity Reservation is cancelled by a customer. | 
| capacity\_reservation\_capacity\_reservation\_type | **Table configuration:** Added by: INCLUDE CAPACITY RESERVATION DATA<br />The capacity reservation type field represents the type of capacity reservation purchased. Currently, there are 2 types ODCR and EC2 Capacity Blocks for ML | String | Nullable | This field is null when capacity\_reservation\_capacity\_reservation\_arn is null<br />This field is not null when capacity\_reservation\_capacity\_reservation\_arn is not null and line\_item\_line\_item\_type is **Usage** or **SavingsPlannedCoveredUsage** or **DiscountedUsage**<br />This field contains one of the allowed values – ODCR or EC2 Capacity Blocks for ML | 