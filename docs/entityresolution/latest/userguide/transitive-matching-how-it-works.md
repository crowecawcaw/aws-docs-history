

# How transitive matching works
<a name="transitive-matching-how-it-works"></a>

Transitive matching uses the following match ID resolution process for each match group on the current rule:
+ The system checks if any record in the group already has a match ID from an earlier rule level.
+ If a match ID exists, the entire group inherits that earlier match ID.
+ If multiple candidates exist, the smallest match ID from the earliest rule level is selected.
+ If no prior match exists, the group is assigned a new match ID.