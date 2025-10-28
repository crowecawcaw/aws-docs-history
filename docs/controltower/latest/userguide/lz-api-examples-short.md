# View the status of your landing zone operations

The `ListLandingZoneOperations` API allows you to view the status of AWS Control Tower operations that perform actions on your landing zone.

For more information about this API operation, see [ListLandingZoneOperations](../APIReference/API_ListLandingZoneOperations.md "../APIReference/API_ListLandingZoneOperations.md").

## ListLandingZoneOperations

**Example input and output for `ListLandingZoneOperations`**.

This example shows how to call the API with no parameters.

```
aws controltower --region us-east-1 list-landing-zone-operations

{
    "landingZoneOperations": [
        {
            "operationIdentifier": "873fe98d-1ecc-4154-b593-86e4a95ebfXX",
            "operationType": "CREATE",
            "status": "FAILED"
        },
        {
            "operationIdentifier": "0016d43d-a307-4ad8-a2a2-b427b8eb1cXX",
            "operationType": "DELETE",
            "status": "SUCCEEDED"
        },
        {
            "operationIdentifier": "002b8b5a-6bb7-4c40-89cd-5822a73d13XX",
            "operationType": "CREATE",
            "status": "SUCCEEDED"
        },
        {
            "operationIdentifier": "008886a0-f7a2-4df3-90e8-6e9f936507XX",
            "operationType": "CREATE",
            "status": "FAILED"
        }
    ]
}
```

This example shows how to call the API and specify the maximum number of results.

```
aws controltower --region us-east-1 list-landing-zone-operations --max-results 1

{
    "landingZoneOperations": [
        {
            "operationIdentifier": "873fe98d-1ecc-4154-b593-86e4a95ebfXX",
            "operationType": "CREATE",
            "status": "FAILED"
        }
    ],
    "nextToken": "AAMAATFMzwP0QysYY8npWgstfcHGQBj-XCC18ISyd9mkQmzLR7ZFMket4F0aWv8tUTtnsTWOnfblUp_Q9U-nX9_6lEsLHs0RlhceDKskHr0_3fm8KdPTa6ofxMt5SPw8WF7-Jsvw2rJVvhj4DHDipo-y1HVK_eZ__Z3-OzInm403cIHxhbjGPgqCX6FeKr8lwgTDKOejkLYZ9w7J5aqPAKLfVP8KKNda5g0VfMj1wdl4J2nwnHI-UuCTIZ5nUEgXgUHaFq6Ma1pLDfGefZQJn5HmDhhgd5yvqzSRH1BtrHpdV_N1EVP8u3JJr3eWQHe9jNB02lihD4Mdcbm3SJg1tWWw2bxp0cgClepI-1Dxt3FAZ5XMVjDxHQHxdKkrazHunMgBFvwfzauC3Ah0WqJg9dkEP22l5HI9qZ7LtDbYZEb5hCskVmjxFsbbwia_OrL2X8ZDeHZStJkxbC3CPIjFMQuldBlzF6L19GSpHE7XIMlTBzzwWtg92sGlpz0An1Smh12jZDe__u2rx8NSkAT97B0bKtmI2TKjutOx7NYUxOhc5qio8dAJbcMgDkf1m5BjK9R7GKdrVv5EDY5Q6uE8gxM2wGnUr_NkpGqR1aEjLIRfZYKN9so_x4vZZPhwtp1NIv256mIGvMYzNivLZ4FE9RPJFh7rSNwFvWnRSVwFLDkOoqXZV9OUYsXdn3W3FMqBzbG6g2KvMXKrKdbrnJHxGgyNYSbS3ogkQYGeuz-VXRwTUIBInrit4HslNtPE8-IC1gxCjGoYPGtuWBPumK-pUPE="
}
```

This example shows how to call the API and obtain a paginated result with `nextToken`.

```
aws controltower --region us-east-1 list-landing-zone-operations --next-token AAMAATFMzwP0QysYY8npWgstfcHGQBj-XCC18ISyd9mkQmzLR7ZFMket4F0aWv8tUTtnsTWOnfblUp_Q9U-nX9_6lEsLHs0RlhceDKskHr0_3fm8KdPTa6ofxMt5SPw8WF7-Jsvw2rJVvhj4DHDipo-y1HVK_eZ__Z3-OzInm403cIHxhbjGPgqCX6FeKr8lwgTDKOejkLYZ9w7J5aqPAKLfVP8KKNda5g0VfMj1wdl4J2nwnHI-UuCTIZ5nUEgXgUHaFq6Ma1pLDfGefZQJn5HmDhhgd5yvqzSRH1BtrHpdV_N1EVP8u3JJr3eWQHe9jNB02lihD4Mdcbm3SJg1tWWw2bxp0cgClepI-1Dxt3FAZ5XMVjDxHQHxdKkrazHunMgBFvwfzauC3Ah0WqJg9dkEP22l5HI9qZ7LtDbYZEb5hCskVmjxFsbbwia_OrL2X8ZDeHZStJkxbC3CPIjFMQuldBlzF6L19GSpHE7XIMlTBzzwWtg92sGlpz0An1Smh12jZDe__u2rx8NSkAT97B0bKtmI2TKjutOx7NYUxOhc5qio8dAJbcMgDkf1m5BjK9R7GKdrVv5EDY5Q6uE8gxM2wGnUr_NkpGqR1aEjLIRfZYKN9so_x4vZZPhwtp1NIv256mIGvMYzNivLZ4FE9RPJFh7rSNwFvWnRSVwFLDkOoqXZV9OUYsXdn3W3FMqBzbG6g2KvMXKrKdbrnJHxGgyNYSbS3ogkQYGeuz-VXRwTUIBInrit4HslNtPE8-IC1gxCjGoYPGtuWBPumK-pUPE=

{
    "landingZoneOperations": [
        {
            "operationIdentifier": "0016d43d-a307-4ad8-a2a2-b427b8eb1cXX",
            "operationType": "DELETE",
            "status": "SUCCEEDED"
        },
        {
            "operationIdentifier": "002b8b5a-6bb7-4c40-89cd-5822a73d13XX",
            "operationType": "CREATE",
            "status": "SUCCEEDED"
        },
        {
            "operationIdentifier": "008886a0-f7a2-4df3-90e8-6e9f936507XX",
            "operationType": "CREATE",
            "status": "FAILED"
        }
    ]
}
```

This example shows how to call the API with a filter.

```
aws controltower --region us-east-1 list-landing-zone-operations --filter '{"types":["CREATE"],"statuses":["FAILED"]}'

{
    "landingZoneOperations": [
        {
            "operationIdentifier": "873fe98d-1ecc-4154-b593-86e4a95ebfXX",
            "operationType": "CREATE",
            "status": "FAILED"
        },
        {
            "operationIdentifier": "008886a0-f7a2-4df3-90e8-6e9f936507XX",
            "operationType": "CREATE",
            "status": "FAILED"
        }
    ]
}

```
