

# FileUniqueness
<a name="dqdl-rule-types-FileUniqueness"></a>

 File Uniqueness allows you to ensure that there are no duplicate files in the data you have received from your data producers. 

 It gathers the following data statistics: 

1.  The number of files that were scanned by the rule 

1.  The Uniqueness Ratio of the files 

```
Dataset.*.FileUniquenessRatio: 1.00, Dataset.*.FileCount: 8
```

 **Find duplicate files in a folder:** 

```
FileUniqueness "s3://bucket/" > 0.5
FileUniqueness "s3://bucket/folder/" = 1
```

 **Inferring folder names directly from data frames to detect duplicates:** 

 You don't always have to provide a file path. For instance, when you are authoring the rule in the AWS Glue Data Catalog, it may be hard to find which folders the catalog tables are using. AWS Glue Data Quality can find the specific folders or files used to populate your data frame. 

**Note**  
 When using inference, file-based rules can only detect files successfully read into the DynamicFrame or DataFrame. 

```
FileUniqueness > 0.5
```

 **Optional File-based Rule Tags:** 

 Tags allow you to control the rule behaviour. 

 **recentFiles** 

 This tag limits the number of files processed by keeping the most recent file first. 

```
FileUniqueness "s3://amzn-s3-demo-bucket/" > 0.5 with recentFiles = 1
```

 **uriRegex** 

**Note**  
 The `uriRegex` tag is available in AWS Glue 5.0 and later. 

 This tag filters files by applying a regex pattern to the file path. Only files whose paths match the pattern are processed. You can also use a negative lookahead to exclude files that match a pattern. 

```
# Match only files with a .csv extension
FileUniqueness "s3://bucket/" > 0.5 with uriRegex = "\.csv$"
# Exclude files ending in .tmp using a negative lookahead
FileUniqueness "s3://bucket/" > 0.5 with uriRegex = "(?!.*\.tmp$).*"
```

 **filterOrder** 

**Note**  
 The `filterOrder` tag is available in AWS Glue 5.0 and later. 

 When you use multiple filter tags such as `recentFiles` and `uriRegex` together, the `filterOrder` tag controls the order in which they are applied. The default order is `recentFiles` first, then `uriRegex`. 

```
FileUniqueness "s3://bucket/" > 0.5 with recentFiles = 5 with uriRegex = "\.csv$" with filterOrder = ["uriRegex","recentFiles"]
```

 **matchFileName** 

 This tag ensures that files don’t have duplicate names. Default behavior is false. 

```
FileUniqueness "s3://amzn-s3-demo-bucket/" > 0.5 with matchFileName = "true"
```

 There are a few considerations: 

1.  In AWS Glue ETL, you must have the **EvaluateDataQuality** Transform immediately after an Amazon S3 or AWS Glue Data Catalog transform. 

1.  This rule will not work in AWS Glue Interactive Sessions. 