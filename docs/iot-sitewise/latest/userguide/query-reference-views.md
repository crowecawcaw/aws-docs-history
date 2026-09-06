

# Query reference views
<a name="query-reference-views"></a>

This section provides information to help you understand the views in AWS IoT SiteWise, such as process metadata and telemetry data.

The following tables provide the view names and descriptions of the views:


**Data model**  

|  **View name**  |  **View description**  | 
| --- | --- | 
| asset | Contains information about the asset and model derivation. | 
| asset\_property | Contains information about the asset property's structure. | 
| raw\_time\_series | Contains the historical data of the time series. | 
| latest\_value\_time\_series | Contains the latest value of the time series. | 
| precomputed\_aggregates | Contains the automatically computed aggregated asset property values. They are a set of basic metrics calculated over multiple time intervals. | 

The following views list the column names and data types of each view.


**View:asset**  

|  **column name**  |  **datatype**  | 
| --- | --- | 
| asset\_id | string | 
| asset\_name | string | 
| asset\_description | string | 
| asset\_model\_id | string | 
| parent\_asset\_id | string | 
| asset\_external\_id | string | 
| asset\_model\_external\_id | string | 
| hierarchy\_id | string | 


**View:asset\_property**  

|  **column name**  |  **datatype**  | 
| --- | --- | 
| asset\_id | string | 
| property\_id | string | 
| property\_name | string | 
| property\_alias | string | 
| property\_external\_id | string | 
| asset\_composite\_model\_id | string | 
| property\_type | string | 
| property\_data\_type | string | 
| int\_attribute\_value | integer | 
| double\_attribute\_value | double | 
| boolean\_attribute\_value | boolean | 
| string\_attribute\_value | string | 


**View:raw\_time\_series**  

|  **column name**  |  **datatype**  | 
| --- | --- | 
| asset\_id | string | 
| property\_id | string | 
| property\_alias | string | 
| event\_timestamp | timestamp | 
| quality | string | 
| boolean\_value | boolean | 
| int\_value | integer | 
| double\_value | double | 
| string\_value | string | 


**View:latest\_value\_time\_series**  

|  **column name**  |  **datatype**  | 
| --- | --- | 
| asset\_id | string | 
| property\_id | string | 
| property\_alias | string | 
| event\_timestamp | timestamp | 
| quality | string | 
| boolean\_value | boolean | 
| int\_value | integer | 
| double\_value | double | 
| string\_value | string | 


**View:precomputed\_aggregates**  

|  **column name**  |  **datatype**  | 
| --- | --- | 
| asset\_id | string | 
| property\_id | string | 
| property\_alias | string | 
| event\_timestamp | timestamp | 
| quality | string | 
| resolution | string | 
| sum\_value | double | 
| count\_value | integer | 
| average\_value | double | 
| maximum\_value | double | 
| minimum\_value | double | 
| stdev\_value | double | 