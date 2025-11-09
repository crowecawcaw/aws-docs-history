# RxNorm linking

Use the **InferRxNorm** operation to identify medications that are listed in a patient record as entities. The operation also links those entities to concept identifiers (RxCUI) from [the RxNorm database from the National Library of Medicine](https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html "https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html "). The source for each RxCUI is the 2022-11-07 RxNorm and RxTerms Release. Each RxCUI is unique for different strengths and dose forms. Amazon Comprehend Medical lists the top potentially matching RxCUIs for each medication that it detects in descending order by confidence score. Use the RxCUI codes for downstream analysis that is not possible with unstructured text. Related information such as strength, frequency, dose, dose form, and route of administration are listed as attributes in JSON format.

You can use **InferRxNorm** for the following scenarios:

- Screening for medications the patient has taken.
- Preventing potentially negative reactions between newly prescribed drugs and drugs the patient is currently taking.
- Screening for inclusion in clinical trials based on drug history using the RxCUI.
- Checking whether the dosage and frequency of a drug is appropriate.
- Screening for uses, indications, and side effects of drugs.
- Managing population health.

## Important notice

The **InferRxNorm** operation of Amazon Comprehend Medical is not a substitute for professional medical advice, diagnosis, or treatment. Identify the right confidence threshold for your use case, and use high confidence thresholds in situations that require high accuracy. Only use Amazon Comprehend Medical operations in patient care scenarios _after_ reviewing for accuracy and receiving sound judgment by trained medical professionals.

## RxNorm category

**InferRxNorm** detects entities in the `MEDICATION` category. It also detects additional related information that is linked as attributes or traits.

## RxNorm types

The types of entities in the `Medication` category are

- `BRAND_NAME`: The copyrighted brand name of the medication or therapeutic agent.
- `GENERIC_NAME`: Non-brand name, ingredient name, or formula mixture of the medication or therapeutic agent.

## RxNorm attributes

- `DOSAGE`: The amount of medication ordered.
- `DURATION`: How long the medication should be
  administered.
- `FORM`: The form of the medication.
- `FREQUENCY`: How often to administer the medication.
- `RATE`: The administration rate of the medication (primarily for medication infusions or IVs).
- `ROUTE_OR_MODE`: The administration method of a
  medication.
- `STRENGTH`: The medication strength.

## RxNorm traits

- `NEGATION`: Any indication that the patient is _not_ taking a medication.
- `PAST_HISTORY`: An indication that a medication detected is from the patient’s past (prior to current encounter).

## Input and response examples

###### Note

For specific API input and response syntax, see
[InferRxNorm](../api/API_InferRxNorm.md "../api/API_InferRxNorm.md")
in the _Amazon Comprehend Medical API Reference_.

The following example input text shows how the `InferRxNorm` operation works. To view all
input text, scroll over the **Copy** button.

```
"fluoride topical ( fluoride 1.1 % topical gel ) 1 application Topically daily Brush onto teeth before bed time , spit , do not rinse, eat or drink for 20-30 minutes"
```

The `InferRxNorm` operation returns the following output in JSON format:

```
{
    "Entities": [
        {
            "Id": 1,
            "Text": "fluoride",
            "Category": "MEDICATION",
            "Type": "GENERIC_NAME",
            "Score": `Float`,
            "BeginOffset": 19,
            "EndOffset": 27,
            "Attributes": [],
            "Traits": [],
            "RxNormConcepts": [
                {
                    "Description": "fluorine",
                    "Code": "1310123",
                    "Score": `Float`
                },
                {
                    "Description": "sodium fluoride",
                    "Code": "9873",
                    "Score": `Float`
                },
                {
                    "Description": "magnesium fluoride",
                    "Code": "1435860",
                    "Score": `Float`
                },
                {
                    "Description": "sulfuryl fluoride",
                    "Code": "2289224",
                    "Score": `Float`
                },
                {
                    "Description": "acidulated phosphate fluoride",
                    "Code": "236",
                    "Score": `Float`
                }
            ]
        }
    ],
    "ModelVersion": "3.2.0.20221107"
}
```

Using the following input text, the `InferRxNorm` operation recognizes the negation trait, too.

```
'patient is not on warfarin'
```

The `InferRxNorm` operation returns the following output in JSON format:

```
{
    "Entities": [
        {
            "Id": 1,
            "Text": "warfarin",
            "Category": "MEDICATION",
            "Type": "GENERIC_NAME",
            "Score": `Float`,
            "BeginOffset": 18,
            "EndOffset": 26,
            "Attributes": [],
            "Traits": [
                {
                    "Name": "NEGATION",
                    "Score": `Float`
                }
            ],
            "RxNormConcepts": [
                {
                    "Description": "warfarin",
                    "Code": "11289",
                    "Score": `Float`
                },
                {
                    "Description": "warfarin sodium 2 MG Oral Tablet",
                    "Code": "855302",
                    "Score": `Float`
                },
                {
                    "Description": "warfarin sodium 10 MG Oral Tablet",
                    "Code": "855296",
                    "Score": `Float`
                },
                {
                    "Description": "warfarin sodium 2 MG Oral Tablet [Coumadin]",
                    "Code": "855304",
                    "Score": `Float`
                },
                {
                    "Description": "warfarin sodium 10 MG Oral Tablet [Jantoven]",
                    "Code": "855300",
                    "Score": `Float`
                }
            ]
        }
    ],
    "ModelVersion": "3.2.0.20221107"
}
```
