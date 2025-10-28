# Lens format specification in AWS WA Tool

Lenses are defined using a specific JSON format. When you start to create a custom
lens, you have the option to download a template JSON file. You can use this file as
the basis for your custom lenses as it defines the basic structure for the pillars,
questions, best practices, and improvement plan.

## Lens section

This section defines the attributes for the custom lens itself. This is its name
and description.

- `schemaVersion`: The version of the custom lens schema to use. Set by the template,
  do not change.
- `name`: Name of the lens. The name can be up to 128 characters.
- `description`: Text description of the lens. This text is displayed when selecting
  lenses to add during workload creation, or when selecting a lens to
  apply to an existing workload later. The description can be up to 2048
  characters.

```
    "schemaVersion": "2021-11-01",
    "name": "`Company Policy ABC`",
    "description": "`This lens provides a set of specific questions to assess compliance with company policy ABC-2021 as revised on 2021/09/01.`",

```

## Pillars section

This section defines the pillars associated with the custom lens. You can map
your questions to the pillars of the AWS Well-Architected Framework, define
your own pillars, or both.

You can define up to 10 pillars in a custom lens.

- `id`: ID for the pillar. The ID can be between 3 and 128 characters and contain
  only alphanumeric and underscore ("\_") characters. The IDs used in a
  pillar must be unique.

When mapping your questions to the pillars of the Framework, use the
following IDs:

    + `operationalExcellence`
    + `security`
    + `reliability`
    + `performance`
    + `costOptimization`
    + `sustainability`

- `name`: Name of the pillar. The name can be up to 128 characters.

```
     "pillars": [
        {
            "id": "`company_Privacy`",
            "name": "`Privacy Excellence`",
            .
            .
            .
        },
        {
            "id": "`company_Security`",
            "name": "`Security`",
            .
            .
            .
        }
     ]

```

## Questions section

This section defines the questions associated with a pillar.

You can define up to 20 questions in a pillar in a custom lens.

- `id`: ID for the question. The ID can be from 3 to 128
  characters and contain only alphanumeric and underscore ("\_")
  characters. The IDs used in a question must be unique.
- `title`: Title of the question. The title can be up to 128
  characters.
- `description`: Describes the question in more detail. The
  description can be up to 2048 characters.
- `helpfulResource displayText`: Optional. Text that provides
  helpful information about the question. The text can be up to 2048
  characters. Must be specified if `helpfulResource url` is
  specified.
- `helpfulResource url`: Optional. A URL resource that
  explains the question in more detail. The URL must start with
  `http://` or `https://`.

###### Note

When syncing a custom lens workload to Jira, questions display both the "id" and "title" of the question.

The format used in Jira tickets is `[ QuestionID ] QuestionTitle`.

```
"questions": [
    {
        "id": "`privacy01`",
        "title": "`How do you ensure HR conversations are private?`",
        "description": "`Career and benefits discussions should occur on secure channels only and be audited regularly for compliance.`",
        "helpfulResource": {
            "displayText": "`This is helpful text for the first question`",
            "url": "`https://example.com/poptquest01_help.html`"
        },
        .
        .
        .
    },
    {
        "id": "`privacy02`",
        "title": "`Is your team following the company privacy policy?`",
        "description": "`Our company requires customers to opt-in to data use and does not disclose customer data to third parties either individually or in aggregate.`",
        "helpfulResource": {
            "displayText": "`This is helpful text for the second question`",
            "url": "`https://example.com/poptquest02_help.html`"
        },
        .
        .
        .
    }
]

```

## Choices section

This section defines the choices that are associated with a question.

You can define up to 15 choices for a question in a custom lens.

- `id`: ID for the choice. The ID can be between 3 and 128
  characters and contain only alphanumeric and underscore ("\_")
  characters. A unique ID must be specified for each choice in a question.
  Adding a choice with a suffix of `_no` will act as a
  `None of these` choice for the question.
- `title`: Title of the choice. The title can be up to 128
  characters.
- `helpfulResource displayText`: Optional. Text that provides
  helpful information about a choice. The text can be up to 2048
  characters. Must be included if `helpfulResource url` is
  specified.
- `helpfulResource url`: Optional. A URL resource that
  explains the choice in more detail. The URL must start with
  `http://` or `https://`.
- `improvementPlan displayText`: Text that describes how a
  choice can be improved upon. The text can be up to 2048 characters. An
  `improvementPlan` is required for each choice, except for
  a `None of these` choice.
- `improvementPlan url`: Optional. A URL resource that can
  help with improvement. The URL must start with `http://` or
  `https://`.
- `additionalResources type`: Optional. The type of
  additional resources. Value can be either `HELPFUL_RESOURCE`
  or `IMPROVEMENT_PLAN`.
- `additionalResources content`: Optional. Specifies the `displayText`
  and `url` values for the additional resource. Up to five additional helpful
  resources and up to five additional improvement plan items can be specified for a choice.
  - `displayText`: Optional. Text that describes the helpful resource or
    improvement plan. The text can be up to 2048 characters. Must be
    included if `url` is specified.
  - `url`: Optional. A URL resource for the helpful resource or
    improvement plan. The URL must start with `http://` or
    `https://`.

###### Note

When syncing a custom lens workload to Jira, choices display the "id" of the question and choice, as well as the "title" of the choice.

The format used is `[ QuestionID | ChoiceID ] ChoiceTitle`.

```
    "choices": [
         {
             "id": "`choice_1`",
             "title": "`Option 1`",
             "helpfulResource": {
                 "displayText": "`This is helpful text for the first choice`",
                 "url": "`https://example.com/popt01_help.html`"
             },
             "improvementPlan": {
                 "displayText": "`This is text that will be shown for improvement of this choice.`",
                 "url": "`https://example.com/popt01_iplan.html`"
             }
         },
         {
             "id": "`choice_2`",
             "title": "`Option 2`",
             "helpfulResource": {
                 "displayText": "`This is helpful text for the second choice`",
                 "url": "`https://example.com/hr_manual_CORP_1.pdf`"
             },
             "improvementPlan": {
                 "displayText": "`This is text that will be shown for improvement of this choice.`",
                 "url": "`https://example.com/popt02_iplan_01.html`"
             },
             "additionalResources":[
                {
                  "type": "HELPFUL_RESOURCE",
                  "content": [
                    {
                      "displayText": "`This is the second set of helpful text for this choice.`",
                      "url": "`https://example.com/hr_manual_country.html`"
                    },
                    {
                      "displayText": "`This is the third set of helpful text for this choice.`",
                      "url": "`https://example.com/hr_manual_city.html`"
                    }
                  ]
                },
                {
                  "type": "IMPROVEMENT_PLAN",
                  "content": [
                    {
                      "displayText": "`This is additional text that will be shown for improvement of this choice.`",
                      "url": "`https://example.com/popt02_iplan_02.html`"
                    },
                    {
                      "displayText": "`This is the third piece of improvement plan text.`",
                      "url": "`https://example.com/popt02_iplan_03.html`"
                    }
                    {
                      "displayText": "`This is the fourth piece of improvement plan text.`",
                      "url": "`https://example.com/popt02_iplan_04.html`"
                    }
                  ]
                }
              ]
         },
         {
              "id": "option_no",
              "title": "None of these",
              "helpfulResource": {
                "displayText": "`Choose this if your workload does not follow these best practices.`",
                "url": "`https://example.com/popt02_iplan_none.html`"
              }

            }

```

## Risk Rules section

This section defines how the choices selected determine the risk level.

You can define a maximum of three risk rules per question, one for each level
of risk.

- `condition`: A Boolean expression of the choices that maps
  to a risk level for the question, or `default`.

There must be a `default` risk rule for each
question.

- `risk`: Indicates the risk associated with the condition.
  Valid values are `HIGH_RISK`, `MEDIUM_RISK`, and
  `NO_RISK`.

The order of your risk rules is significant. The first `condition`
that evaluates to `true` sets the risk for the question. A common
pattern for implementing risk rules is to start with your least risky (and
typically most granular) rules and work your way down to your most risky (and
least specific) rules.

For example:

```
 "riskRules": [
       {
         "condition": "`choice_1 && choice_2 && choice_3`",
         "risk": "`NO_RISK`"
       },
       {
         "condition": "`((choice_1 || choice_2) && choice_3) || (!choice_1 && choice_3)`",
         "risk": "`MEDIUM_RISK`"
       },
       {
         "condition": "`default`",
         "risk": "`HIGH_RISK`"
       }
 ]

```

If the question has three choices (`choice_1`,
`choice_2`, and `choice_3`), these risk rules result
in the following behavior:

- If all three choices are selected, there is no risk.
- If either `choice_1` or `choice_2` is selected
  **and**
  `choice_3` is selected, there is medium risk.
- If `choice_1` is **not**
  selected but `choice_3` is selected, there is also medium
  risk.
- If none of these prior conditions were true, there is high
  risk.
