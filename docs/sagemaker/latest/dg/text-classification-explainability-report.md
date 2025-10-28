# Explainability report

Amazon SageMaker Autopilot provides an explainability report to help explain how a best model candidate makes
predictions for text classification problems. This report can assist ML engineers, product
managers, and other internal stakeholders in understanding the characteristics of the model.
Both consumers and regulators rely on transparency in machine learning to trust and interpret
decisions made on model predictions. You can use these explanations for auditing and meeting
regulatory requirements, establishing trust in the model, supporting human decision-making,
and debugging and improving model performance.

The Autopilot explanatory functionality for text classification uses the axiomatic
attribution method _Integrated Gradients_. This approach
relies on an implementation of [Axiomatic
Attribution for Deep Network](https://arxiv.org/pdf/1703.01365.pdf "https://arxiv.org/pdf/1703.01365.pdf").

Autopilot generates the explainability report as a JSON file. The report includes analysis
details that are based on the validation dataset. Each sample used to generate the report
contains the following information:

- `text`: The input text content explained.
- `token_scores`: The list of scores for every token in the text.
- - `attribution`: The score depicting the importance of the token.
  - `description.partial_text`: The partial substring that represents the
    token.
- `predicted_label`: The label class predicted by the best model
  candidate.
- `probability`: The confidence with which the `predicted_label`
  was predicted.
  You can find the Amazon S3 prefix to the explainability artifacts generated for the best
  candidate in the response to `DescribeAutoMLJobV2` at `BestCandidate.CandidateProperties.CandidateArtifactLocations.Explainability`.

The following is an example of analysis content that you could find in the explainability
artifacts.

```
{
    "text": "It was a fantastic movie!",
    "predicted_label": 2,
    "probability": 0.9984835,
    "token_scores": [
        {
            "attribution": 0,
            "description": {
                "partial_text": "It"
            }
        },
        {
            "attribution": -0.022447118861679088,
            "description": {
                "partial_text": "was"
            }
        },
        {
            "attribution": -0.2164326456817965,
            "description": {
                "partial_text": "a"
            }
        },
        {
            "attribution": 0.675,
            "description": {
                "partial_text": "fantastic"
            }
        },
        {
            "attribution": 0.416,
            "description": {
                "partial_text": "movie!"
            }
        }
    ]
}
```

In this sample of the JSON report, the explanatory functionality evaluates the text
`It was a fantastic movie!` and scores the contribution of each of its token to
the overall predicted label. The predicted label is `2`, which is a strong positive
sentiment, with a probability of 99.85%. The JSON sample then details the contribution of each
individual token to this prediction. For example, the token `fantastic` has a
stronger attribution than the token `was`. It is the token that contributed the
most to the final prediction.
