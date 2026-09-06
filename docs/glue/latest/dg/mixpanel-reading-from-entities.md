

# Reading from Mixpanel entities
<a name="mixpanel-reading-from-entities"></a>

 **Prerequisites** 

You must have a Mixpanel object, such as `Funnels`, `Retention`, or `Retention Funnels`, from which you would like to read data. Additionally, you will need to know the object name.

 **Supported entities** 


| Entity | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Funnels | Yes | No | No | Yes | No | 
| Retention | Yes | No | No | Yes | No | 
| Segmentation | Yes | No | No | Yes | No | 
| Segmentation Sum | Yes | No | No | Yes | No | 
| Segmentation Average | Yes | No | No | Yes | No | 
| Cohorts | Yes | No | No | Yes | No | 
| Engage | No | Yes | No | Yes | No | 
| Events | Yes | No | No | Yes | No | 
| Events Top | Yes | No | No | Yes | No | 
| Events Names | Yes | No | No | Yes | No | 
| Events Properties | Yes | No | No | Yes | No | 
| Events Properties Top | Yes | No | No | Yes | No | 
| Events Properties Values | Yes | No | No | Yes | No | 
| Annotations | Yes | No | No | Yes | No | 
| Profile Event Activity | Yes | No | No | Yes | No | 

 **Example** 

```
mixpanel_read = glueContext.create_dynamic_frame.from_options(
    connection_type="mixpanel",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "/cohorts/list?project_id=2603353",
        "API_VERSION": "2.0",
        "INSTANCE_URL": "https://www.mixpanel.com/api/app/me"
    }
```

 **Mixpanel entity and field details** 



- **Funnel**
  - **Field:** funnel\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** from\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** to\_date / **Data Type:** Date / ****Supported Operators**:** '=’
  - **Field:** length / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** length\_unit / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** interval / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** unit / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** limit / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** data / **Data Type:** Struct / ****Supported Operators**:** 
  - **Field:** meta / **Data Type:** Struct / ****Supported Operators**:** 

- **Retention**
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** unit / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** addiction\_unit / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** from\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** to\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** limit / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** data / **Data Type:** Struct / ****Supported Operators**:** 

- ** Segmentation **
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** from\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** to\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** unit / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** interval / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** limit / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** type / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** series / **Data Type:** List / ****Supported Operators**:** 
  - **Field:** values / **Data Type:** Struct / ****Supported Operators**:** 
  - **Field:** data / **Data Type:** Struct / ****Supported Operators**:** 

- **Segmentation Numeric**
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** on / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** from\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** to\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** unit / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** type / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** series / **Data Type:** List / ****Supported Operators**:** 
  - **Field:** values / **Data Type:** Struct / ****Supported Operators**:** 

- **Segmentation Sum**
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** on / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** from\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** to\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** unit / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** metadata / **Data Type:** Struct / ****Supported Operators**:** 
  - **Field:** results / **Data Type:** Struct / ****Supported Operators**:** 

- ** Segmentation Average **
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** on / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** from\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** to\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** unit / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** metadata / **Data Type:** Struct / ****Supported Operators**:** 
  - **Field:** results / **Data Type:** Struct / ****Supported Operators**:** 

- **Cohorts**
  - **Field:** count / **Data Type:** Integer / ****Supported Operators**:** 
  - **Field:** is\_visible / **Data Type:** Integer / ****Supported Operators**:** 
  - **Field:** description / **Data Type:** String / ****Supported Operators**:** 
  - **Field:** created / **Data Type:** DateTime / ****Supported Operators**:** 
  - **Field:** project\_id / **Data Type:** Integer / ****Supported Operators**:** 
  - **Field:** id / **Data Type:** BigInteger / ****Supported Operators**:** 
  - **Field:** name / **Data Type:** String / ****Supported Operators**:** 
  - **Field:** data\_group\_id / **Data Type:** String / ****Supported Operators**:** 

- **Engage**
  - **Field:** distinct\_id / **Data Type:** String / ****Supported Operators**:** 
  - **Field:**  / **Data Type:** properties / ****Supported Operators**:** Struct

- **Event**
  - **Field:** workspace / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** type / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** unit / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** interval / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** from\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** to\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** series / **Data Type:** List / ****Supported Operators**:** 
  - **Field:** values / **Data Type:** Struct / ****Supported Operators**:** 

- ** Events Top**
  - **Field:** type / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** limit / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** amount / **Data Type:** Integer / ****Supported Operators**:** 
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** 
  - **Field:** percent\_change / **Data Type:** Float / ****Supported Operators**:** 

- ** Event Name**
  - **Field:** data / **Data Type:** List / ****Supported Operators**:** 
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** type / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** limit / **Data Type:** Integer / ****Supported Operators**:** '='

- ** Event Properties**
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** name / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** type / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** unit / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** interval / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** from\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** to\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** limit / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** data / **Data Type:** Struct / ****Supported Operators**:** 
  - **Field:** series / **Data Type:** List / ****Supported Operators**:** 
  - **Field:** values / **Data Type:** Struct / ****Supported Operators**:** 

- ** Event Properties Top**
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** limit / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** data / **Data Type:** Struct / ****Supported Operators**:** 

- ** Event Properties Value**
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** limit / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** name / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** data / **Data Type:** List / ****Supported Operators**:** 

- ** Annotation**
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** 
  - **Field:** date / **Data Type:** DateTime / ****Supported Operators**:** 
  - **Field:** project\_id / **Data Type:** Integer / ****Supported Operators**:** 
  - **Field:** id / **Data Type:** BigInteger / ****Supported Operators**:** 
  - **Field:** description / **Data Type:** String / ****Supported Operators**:** 
  - **Field:** from\_date / **Data Type:** Date / ****Supported Operators**:** BETWEEN

- ** Profile Event Activity**
  - **Field:** workspace\_id / **Data Type:** Integer / ****Supported Operators**:** '='
  - **Field:** distinct\_ids / **Data Type:** String / ****Supported Operators**:** '='
  - **Field:** from\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** to\_date / **Data Type:** Date / ****Supported Operators**:** '='
  - **Field:** event / **Data Type:** String / ****Supported Operators**:** 
  - **Field:** properties / **Data Type:** Struct / ****Supported Operators**:** 

