

# Cost optimization recommendations columns
<a name="table-dictionary-cor-columns"></a>


| Column name | Description | Data type | Null value allowed | 
| --- | --- | --- | --- | 
| account\_id | The account ID that the recommendation is for. | string | No | 
| account\_name | The account name that the recommendation is for. | string | No | 
| action\_type | The type of action you can take by adopting the recommendation. | string | No | 
| currency\_code | The currency code used for the recommendation. | string | No | 
| current\_resource\_details | The details for the resource in JSON string format. | string | Yes | 
| current\_resource\_summary | A description of the current resource. | string | Yes | 
| current\_resource\_type | The type of resource. | string | Yes | 
| estimated\_monthly\_cost\_after\_discount | The estimated monthly cost of the current resource after discounts. For Reserved Instances and Savings Plans, it refers to the cost for eligible usage. | double | Yes | 
| estimated\_monthly\_cost\_before\_discount | The estimated monthly cost of the current resource before discounts. For Reserved Instances and Savings Plans, it refers to the cost for eligible usage. | double | No | 
| estimated\_monthly\_savings\_after\_discount | The estimated monthly savings amount for the recommendation after discounts. | double | Yes | 
| estimated\_monthly\_savings\_before\_discount | The estimated monthly savings amount for the recommendation before discounts. | double | No | 
| estimated\_savings\_percentage\_after\_discount | The estimated savings percentage after discounts relative to the total cost over the cost calculation lookback period. | double | Yes | 
| estimated\_savings\_percentage\_before\_discount | The estimated savings percentage before discounts relative to the total cost over the cost calculation lookback period. | double | No | 
| implementation\_effort | The effort required to implement the recommendation. | string | No | 
| last\_refresh\_timestamp | The time when the recommendation was last generated. | timestamp | No | 
| recommendation\_ID | The ID for the recommendation. | string | No | 
| recommendation\_lookback\_period\_in\_days | The lookback period that's used to generate the recommendation. | integer | No | 
| recommendation\_source | The source of the recommendation. | string | No | 
| recommended\_resource\_details | The details about the recommended resource in JSON string format. | string | Yes | 
| recommended\_resource\_summary | A description of the recommended resource. | string | Yes | 
| recommended\_resource\_type | The resource type of the recommendation. | string | Yes | 
| region | The AWS Region of the resource. | string | Yes | 
| resource\_arn | The Amazon Resource Name (ARN) of the resource. | string | Yes | 
| restart\_needed | Whether or not implementing the recommendation requires a restart. | boolean | No | 
| rollback\_possible | Whether or not implementing the recommendation can be rolled back. | boolean | No | 
| tags | A list of tags associated with the resource for which the recommendation exists. | map | Yes | 