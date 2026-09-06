

# Using the Timestream data source
<a name="timestream-query-editor"></a>

## Query editor
<a name="timestream-query-editor"></a>

 The query editor accepts Timestream syntax in addition to the macros listed previously and any dashboard template variables. 

 Press **Ctrl\+Space** to open the IntelliSense suggestions. 

## Macros
<a name="timestream-macros"></a>

 To simplify syntax and to allow for dynamic parts, such as date range filters, the query can contain macros. 


|  Macro example  |  Description  | 
| --- | --- | 
| *$\_\_database* |  Will specify the selected database. This uses the default from the data source configuration, or the explicit value from the query editor.  | 
| *$\_\_table* |  Will specify the selected database. This uses the default from the datasource config, or the explicit value from the query editor.  | 
| *$\_\_measure* |  Will specify the selected measure. This uses the default from the datasource config, or the explicit value from the query editor.  | 
| *$\_\_timeFilter* |  Will be replaced by an expression that limits the time to the dashboard range  | 
| *$\_\_interval\_ms* |  Will be replaced by a number that represents the amount of time a single pixel in the graph should cover.  | 