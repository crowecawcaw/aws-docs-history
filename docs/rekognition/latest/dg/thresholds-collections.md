# Using similarity thresholds for

associating and matching faces

Similarity thresholds are used for both associating and matching faces. What follows
is guidance for using similarity thresholds for both use cases.

## Using similarity thresholds for

associating faces

When associating faces using the [AssociateFaces](../APIReference/API_AssociateFaces.md "../APIReference/API_AssociateFaces.md") operation, it’s important to ensure that faces being
associated with a user are all from the same person. To help, the
`UserMatchThreshold` parameter specifies the minimum user match
confidence required for the new face to be associated with a `UserID`
containing at least one `FaceID` already. This helps ensures that the
`FaceIds` are associated with the right `UserID`. The
value ranges from 0-100 and the default value is 75.

## Using similarity thresholds to match

faces

We allow you to control the results of all search operations ([CompareFaces](../APIReference/API_CompareFaces.md "../APIReference/API_CompareFaces.md"), [SearchFaces](../APIReference/API_SearchFaces.md "../APIReference/API_SearchFaces.md"),
[SearchFacesByImage](../APIReference/API_SearchFacesByImage.md "../APIReference/API_SearchFacesByImage.md"), [SearchUsers](../APIReference/API_SearchUsers.md "../APIReference/API_SearchUsers.md"),
[SearchUsersByImage](../APIReference/API_SearchUsersByImage.md "../APIReference/API_SearchUsersByImage.md")) by providing a similarity threshold as an input
parameter.

`FaceMatchThreshold`, is the similarity threshold input attribute for
`SearchFaces` and `SearchFacesByImage`, and it controls how
many results are returned based on the similarity to the face being matched. The
similarity threshold attribute for `SearchUsers` and
`SearchUsersByImage` is `UserMatchThreshold`, and it controls
how many results are returned based on the similarity to the user vector being matched.
The threshold attribute is `SimilarityThreshold` for
`CompareFaces`.

Responses with a `Similarity` response attribute value that's lower than
the threshold aren't returned. This threshold is important to calibrate for your use
case, because it can determine how many false positives are included in your match
results. This controls the recall of your search results—the lower the threshold, the
higher the recall.

All machine learning systems are probabilistic. You should use your judgment in
setting the right similarity threshold, depending on your use case. For example, if
you're looking to build a photos app to identify similar-looking family members, you
might choose a lower threshold (such as 80%). On the other hand, for many law
enforcement use cases, we recommend using a high threshold value of 99% or above to
reduce accidental misidentification.

In addition to `FaceMatchThreshold` and `UserMatchThreshold`,
you can use the `Similarity` response attribute as a means to reduce
accidental misidentification. For instance, you can choose to use a low threshold (like
80%) to return more results. Then you can use the response attribute Similarity
(percentage of similarity) to narrow the choice and filter for the right responses in
your application. Again, using a higher similarity (such as 99% and above) reduces the
risk of misidentification.
