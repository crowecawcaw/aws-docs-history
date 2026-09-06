

# JOIN
<a name="recipe-actions.JOIN"></a>

Performs a join operation on two datasets.

**Parameters**
+ `joinKeys` — A JSON-encoded string representing a list of columns from each dataset to act as join keys.
+ `joinType` — The type of join to perform. Must be one of: `INNER_JOIN` \| `LEFT_JOIN `\| `RIGHT_JOIN` \| `OUTER_JOIN `\| `LEFT_EXCLUDING_JOIN` \| `RIGHT_EXCLUDING_JOIN` \| `OUTER_EXCLUDING_JOIN`
+ `leftColumns` — A JSON-encoded string representing a list of columns from the current active dataset.
+ `rightColumns` — A JSON-encoded string representing a list of columns from another (secondary) dataset to join to the current one.
+ `secondInputLocation` — An Amazon S3 URL that resolves to the data file for the secondary dataset.
+ `secondaryDatasetName` — The name of the secondary dataset.

**Example**  
  

```
{
    "Action": {
        "Operation": "JOIN",
        "Parameters": {
            "joinKeys": "[{\"key\":\"assembly_session\",\"value\":\"assembly_session\"},{\"key\":\"state_code\",\"value\":\"state_code\"}]",
            "joinType": "INNER_JOIN",
            "leftColumns": "[\"year\",\"assembly_session\",\"state_code\",\"state_name\",\"all_votes\",\"yes_votes\",\"no_votes\",\"abstain\",\"idealpoint_estimate\",\"affinityscore_usa\",\"affinityscore_russia\",\"affinityscore_china\",\"affinityscore_india\",\"affinityscore_brazil\",\"affinityscore_israel\"]",
            "rightColumns": "[\"assembly_session\",\"vote_id\",\"resolution\",\"state_code\",\"state_name\",\"member\",\"vote\"]",
            "secondInputLocation": "s3://databrew-public-datasets-us-east-1/votes.csv",
            "secondaryDatasetName": "votes"
        }
    }
}
```