# Sample datasets and evaluators

## Supervised Fine tuning (SFT)

- Name: TAT-QA
- License: CC-BY-4.0
- Link: [https://huggingface.co/datasets/next-tat/TAT-QA](https://huggingface.co/datasets/next-tat/TAT-QA "https://huggingface.co/datasets/next-tat/TAT-QA")
- Preprocessing - Formatting

**One Sample**

```
{
    "prompt": "Given a table and relevant text descriptions, answer the following question.\n\nTable:\n<table border=\"1\" class=\"dataframe\">\n  <tbody>\n    <tr>\n      <td></td>\n      <td>2019</td>\n      <td>2018</td>\n    </tr>\n    <tr>\n      <td></td>\n      <td>$'000</td>\n      <td>$'000</td>\n    </tr>\n    <tr>\n      <td>Revenue from external customers</td>\n      <td></td>\n      <td></td>\n    </tr>\n    <tr>\n      <td>Australia</td>\n      <td>144,621</td>\n      <td>129,431</td>\n    </tr>\n    <tr>\n      <td>New Zealand</td>\n      <td>13,036</td>\n      <td>8,912</td>\n    </tr>\n    <tr>\n      <td>Total</td>\n      <td>157,657</td>\n      <td>138,343</td>\n    </tr>\n  </tbody>\n</table>\n\nParagraphs:\n    4. SEGMENT INFORMATION\n\n    During the 2019 and 2018 financial years, the Group operated wholly within one business segment being the operation and management of storage centres in Australia and New Zealand.\n\n    The Managing Director is the Group\u2019s chief operating decision maker and monitors the operating results on a portfolio wide basis. Monthly management reports are evaluated based upon the overall performance of NSR consistent with the presentation within the consolidated financial statements. The Group\u2019s financing (including finance costs and finance income) are managed on a Group basis and not allocated to operating segments.\n\n    The operating results presented in the statement of profit or loss represent the same segment information as reported in internal management information.\n\n    The revenue information above excludes interest income and is based on the location of storage centres.\n\nQuestion: How many business segments were present in 2019 and 2018?\n\nAnswer:",
    "completion": "one",
    "data_idx": "2951"
}
```

## Direct Preference Optimization (DPO)

- Name: Ultrafeedback
- License: MIT
- Link: [https://huggingface.co/datasets/openbmb/UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback "https://huggingface.co/datasets/openbmb/UltraFeedback")
- Preprocessing steps: Formatting and subsampling.

**One Sample**

```
{
    "source": "evol_instruct",
    "prompt": "Can you write a C++ program that prompts the user to enter the name of a country and checks if it borders the Mediterranean Sea? Here's some starter code to help you out:\n#include <iostream>\n#include <string>\nusing namespace std;\nint main() {\n    string country;\n    // prompt user for input\n    cout << \"Enter the name of a country: \";\n    cin >> country;\n    // check if country borders the Mediterranean Sea\n    // [C++ code]\n    return 0;\n}",
    "chosen": "Here's a C++ program that prompts the user to enter the name of a country and checks if it borders the Mediterranean Sea:\n\n#include <iostream>\n#include <string>\n#include <set>\n#include <map>\n#include <algorithm>\n\nusing namespace std;\n\nint main() {\n    // store countries and their bordering seas in a map\n    map<string, set<string>> countries;\n    countries[\"Algeria\"] = {\"Mediterranean Sea\", \"North African Coast\"};\n    countries[\"France\"] = {\"Mediterranean Sea\", \"English Channel\"};\n    countries[\"Italy\"] = {\"Mediterranean Sea\", \"Adriatic Sea\"};\n    countries[\"Malta\"] = {\"Mediterranean Sea\", \"North African Coast\"};\n    countries[\"Spain\"] = {\"Mediterranean Sea\", \"Atlantic Ocean\"};\n    countries[\"Tunisia\"] = {\"Mediterranean Sea\", \"North African Coast\"};\n\n    string country;\n    cout << \"Enter the name of a country: \";\n    cin >> country;\n\n    // check if country is in the map\n    if (countries.find(country)!= countries.end()) {\n        // check if country borders the Mediterranean Sea\n        set<string> borders = countries.at(country);\n        if (borders.find(\"Mediterranean Sea\")!= borders.end()) {\n            cout << country << \" borders the Mediterranean Sea.\" << endl;\n        } else {\n            cout << country << \" does not border the Mediterranean Sea.\" << endl;\n        }\n    } else {\n        cout << country << \" is not a recognized country.\" << endl;\n    }\n\n    return 0;\n}\n\nIn this program, we first define a map called countries that stores each country's name as a key and a set of its surrounding seas as the value. We use a set to store each sea name so that we can easily check if a country borders a certain sea.\n\nWe then present the user with a prompt to enter the name of a country. We use a while loop to ensure that the user enters a valid country name. We check if the country is in the map, and if so, we retrieve its bordering seas from the map.\n\nFinally, we check if the Mediterranean Sea is among the set of borders. If it is, we inform the user that the country borders the Mediterranean Sea. If not, we inform the user that the country does not border the Mediterranean Sea.",
    "chosen-rating": 5.0,
    "chosen-model": "starchat",
    "rejected": "Sure, here is the program using the C++11 algorithm \"cds::algorithm::GreaterEqual\":\n#include <iostream>\n#include <string>\n#include <algorithm>\n#include <vector>\n#include <cctype>\n\nusing namespace std;\n\nint main() {\n    string country;\n    cout << \"Enter the name of a country: \";\n    cin >> country;\n    std::vector<string> vec;\n    vec.push_back(country);\n    size_t index = std::find_if(vec.begin(), vec.end(), [](const string& s) {\n        return std::any_of(s.begin(), s.end(), [](const char& c) {\n            return c == '}}';\n    });\n    if (index != vec.end()) {\n        if ((*index)[0] == 'M') {\n            cout << \"Country is bordered by the Mediterranean Sea.\" << endl;\n        } else {\n            cout << \"Country does not border the Mediterranean Sea.\" << endl;\n        }\n    } else {\n        cout << \"Country is not found.\" << endl;\n    }\n    return 0;\n}",
    "rejected-rating": 1.25,
    "rejected-model": "pythia-12b"
}
```

## Reinforcement Learning from AI Feedback (RLAIF) - Pair-Wise Judging

**Input Dataset**

Source dataset: [https://github.com/WeOpenML/PandaLM](https://github.com/WeOpenML/PandaLM "https://github.com/WeOpenML/PandaLM")

**One Sample**

```
{
    "data_source": "WeOpenML/PandaLM",
    "prompt": [
        {
            "role": "user",
            "content": "Below are two responses for a given task. The task is defined by the Instruction with an Input that provides further context. Evaluate the responses and generate a reference answer for the task.\n\n
            ### Instruction:\nCompare the given products.\n\n### Input:\niPhone 11 and Google Pixel 4\n\n
            ### Response 1:\nThe iPhone 11 has a larger screen size and a longer battery life than the Google Pixel 4.\n\n
            ### Response 2:\nThe iPhone 11 and Google Pixel 4 are both flagship smartphones released in 2018. The iPhone 11 has a 6.1-inch LCD display, while the Google Pixel 4 has a 5.7-inch OLED display. The iPhone 11 has an A13 Bionic chipset, while the Google Pixel 4 has a Qualcomm Snapdragon 845 chipset. The iPhone 11 has a dual-camera system, while the Google Pixel 4 has a single camera system. The iPhone 11 has a longer battery life, while the Google Pixel 4 has a faster processor.\n\n### Evaluation:\n"
        }
    ],
    "ability": "pairwise-judging",
    "reward_model": {
        "style": "llmj",
        "ground_truth": "2\n\n### Reason: Response 2 provides a more detailed and comprehensive comparison of the two products, including their specifications and features. Response 1 only mentions two aspects of the products and does not provide as much information.\n\n### Reference: The iPhone 11 and Google Pixel 4 are both flagship smartphones released in 2018. The iPhone 11 has a 6.1-inch LCD display, while the Google Pixel 4 has a 5.7-inch OLED display. The iPhone 11 has an A13 Bionic chipset, while the Google Pixel 4 has a Qualcomm Snapdragon 845 chipset. The iPhone 11 has a dual-camera system, while the Google Pixel 4 has a single camera system. The iPhone 11 has a longer battery life, while the Google Pixel 4 has a faster processor."
    },
    "extra_info": {
        "split": "train",
        "index": 0,
        "raw_output_sequence": "2\n\n### Reason: Response 2 provides a more detailed and comprehensive comparison of the two products, including their specifications and features. Response 1 only mentions two aspects of the products and does not provide as much information.\n\n### Reference: The iPhone 11 and Google Pixel 4 are both flagship smartphones released in 2018. The iPhone 11 has a 6.1-inch LCD display, while the Google Pixel 4 has a 5.7-inch OLED display. The iPhone 11 has an A13 Bionic chipset, while the Google Pixel 4 has a Qualcomm Snapdragon 845 chipset. The iPhone 11 has a dual-camera system, while the Google Pixel 4 has a single camera system. The iPhone 11 has a longer battery life, while the Google Pixel 4 has a faster processor.\n",
        "llmj": {
            "question": "Below are two responses for a given task. The task is defined by the Instruction with an Input that provides further context. Evaluate the responses and generate a reference answer for the task.\n\n### Instruction:\nCompare the given products.\n\n### Input:\niPhone 11 and Google Pixel 4\n\n### Response 1:\nThe iPhone 11 has a larger screen size and a longer battery life than the Google Pixel 4.\n\n### Response 2:\nThe iPhone 11 and Google Pixel 4 are both flagship smartphones released in 2018. The iPhone 11 has a 6.1-inch LCD display, while the Google Pixel 4 has a 5.7-inch OLED display. The iPhone 11 has an A13 Bionic chipset, while the Google Pixel 4 has a Qualcomm Snapdragon 845 chipset. The iPhone 11 has a dual-camera system, while the Google Pixel 4 has a single camera system. The iPhone 11 has a longer battery life, while the Google Pixel 4 has a faster processor.\n\n### Evaluation:\n",
            "ground_truth": "2\n\n### Reason: Response 2 provides a more detailed and comprehensive comparison of the two products, including their specifications and features. Response 1 only mentions two aspects of the products and does not provide as much information.\n\n### Reference: The iPhone 11 and Google Pixel 4 are both flagship smartphones released in 2018. The iPhone 11 has a 6.1-inch LCD display, while the Google Pixel 4 has a 5.7-inch OLED display. The iPhone 11 has an A13 Bionic chipset, while the Google Pixel 4 has a Qualcomm Snapdragon 845 chipset. The iPhone 11 has a dual-camera system, while the Google Pixel 4 has a single camera system. The iPhone 11 has a longer battery life, while the Google Pixel 4 has a faster processor.",
            "document_in_context": null
        },
        "sample_size": 1980
    }
}

```

## RLAIF - Chain of Thought

**Input Dataset**

Source Data: [https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data](https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data "https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data")

**One Sample**

```
{
    "data_source": "openai/gsm8k",
    "prompt": [
        {
            "role": "system",
            "content": "\nYou are an AI assistant that uses a Chain of Thought (CoT) approach with reflection to answer queries.\n\nFollow these steps:\n- Think through the problem step by step within the ‹thinking> tags.\n- Reflect on your thinking\n\nto check for any errors or improvements within the ‹reflection› tags.\n- Make any necessary adjustments based on your reflection.\n- Provide your final, concise answer within the ‹output> tags.\n\nImportant: The <thinking> and ‹reflection› sections are for your internal reasoning process only.\nDo not include any part of the final answer in these sections.\nThe actual response to the query must be entirely contained within the ‹output› tags.\n\nUse the following format for your response:\n<thinking>\n[Your initial thought process goes here]\n</thinking›\n\n<reasoning>\n[Your step-by-step reasoning goes here. This is your internal thought process, not the final answer. You can create as many reasoning steps as necessary in your process.]\n</reasoning>\n\n‹reflection>\n[Your reflection on your reasoning, checking for errors or improvements. You can create as many reflection steps as necessary in your process.]\n</ reflection>\n\n<adjustment>\n[Any adjustments to your thinking based on your reflection]\n</adjustment>\n\n<output>\n[Your final, concise answer to the query. This is the only part that will be shown to the user.]\n</output>\n"
        },
        {
            "role": "user",
            "content": "A craft store makes a third of its sales in the fabric section, a quarter of its sales in the jewelry section, and the rest in the stationery section. They made 36 sales today. How many sales were in the stationery section?"
        }
    ],
    "ability": "chain-of-thought",
    "reward_model": {
        "style": "llmj-cot",
        "ground_truth": "Thus, there were 36 - 12 - 9 = <<36-12-9=15>>15 sales in the stationery section."
    },
    "extra_info": {
        "split": "train",
        "index": 0,
        "question": "A craft store makes a third of its sales in the fabric section, a quarter of its sales in the jewelry section, and the rest in the stationery section. They made 36 sales today. How many sales were in the stationery section?",
        "short_answer": "15",
        "model_output": "<thinking>\nTo find the number of sales in the stationery section, I need to first calculate the number of sales in the fabric and jewelry sections. The store makes a third of its sales in the fabric section, which is 1/3 of 36 sales. I can calculate this as 36 * 1/3 = 12 sales in the fabric section. The store makes a quarter of its sales in the jewelry section, which is 1/4 of 36 sales. I can calculate this as 36 * 1/4 = 9 sales in the jewelry section. Since the rest of the sales are in the stationery section, I can subtract the sales from the other two sections from the total number of sales to find the number of sales in the stationery section.\n</thinking>\n\n<reasoning>\n1. Calculate the number of sales in the fabric section: 36 * 1/3 = 12\n2. Calculate the number of sales in the jewelry section: 36 * 1/4 = 9\n3. Calculate the number of sales in the stationery section: 36 - 12 - 9 = 15\n</reasoning>\n\n‹reflection>\nUpon reviewing my reasoning, I noticed that my calculations seem correct, but I should ensure that I understand the question correctly. The question asks for the number of sales in the stationery section, and I believe I have correctly calculated that. However, I should double-check my math to make sure it's accurate.\n</reflection>\n\n<adjustment>\nUpon re-examining my math, I am confident that my calculations are correct. The fabric section makes up 1/3 of the sales, the jewelry section makes up 1/4, and the rest is the stationery section. My math checks out, and I am confident in my answer.\n</adjustment>\n\n<output>\n15\n</output>"
    }
}

```

## RLAIF - Faithfulnesss

**Input Dataset**

Source: [https://huggingface.co/datasets/rajpurkar/squad_v2/blob/main/squad_v2/train-00000-of-00001.parquet](https://huggingface.co/datasets/rajpurkar/squad_v2/blob/main/squad_v2/train-00000-of-00001.parquet "https://huggingface.co/datasets/rajpurkar/squad_v2/blob/main/squad_v2/train-00000-of-00001.parquet")

**One Sample**

```
{
    "data_source": "squad_v2",
    "prompt": [
        {
            "role": "system",
            "content": "You are a helpful assistant that answers questions based on the provided context. Only use information from the context."
        },
        {
            "role": "user",
            "content": "Context: Beyoncé Giselle Knowles-Carter (/biːˈjɒnseɪ/ bee-YON-say) (born September 4, 1981) is an American singer, songwriter, record producer and actress. Born and raised in Houston, Texas, she performed in various singing and dancing competitions as a child, and rose to fame in the late 1990s as lead singer of R&B girl-group Destiny's Child. Managed by her father, Mathew Knowles, the group became one of the world's best-selling girl groups of all time. Their hiatus saw the release of Beyoncé's debut album, Dangerously in Love (2003), which established her as a solo artist worldwide, earned five Grammy Awards and featured the Billboard Hot 100 number-one singles \"Crazy in Love\" and \"Baby Boy\".\n\nQuestion: When did Beyonce start becoming popular?"
        }
    ],
    "ability": "faithfulness",
    "reward_model": {
        "style": "llmj-faithfulness",
        "ground_truth": "Beyoncé Giselle Knowles-Carter (/biːˈjɒnseɪ/ bee-YON-say) (born September 4, 1981) is an American singer, songwriter, record producer and actress. Born and raised in Houston, Texas, she performed in various singing and dancing competitions as a child, and rose to fame in the late 1990s as lead singer of R&B girl-group Destiny's Child. Managed by her father, Mathew Knowles, the group became one of the world's best-selling girl groups of all time. Their hiatus saw the release of Beyoncé's debut album, Dangerously in Love (2003), which established her as a solo artist worldwide, earned five Grammy Awards and featured the Billboard Hot 100 number-one singles \"Crazy in Love\" and \"Baby Boy\"."
    },
    "extra_info": {
        "question": "When did Beyonce start becoming popular?",
        "split": "train",
        "index": 0
    }
}

```

## RLAIF - Summarization

**Input Dataset**

Source: Cleaned gsm8k dataset [https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data](https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data "https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data")

**One Sample**

```
{
    "data_source": "cnn_dailymail",
    "prompt": [
        {
            "role": "system",
            "content": "You are a helpful assistant that creates concise, accurate summaries of news articles. Focus on the key facts and main points."
        },
        {
            "role": "user",
            "content": "Summarize the following article:\n\nLONDON, England (Reuters) -- Harry Potter star Daniel Radcliffe gains access to a reported £20 million ($41.1 million) fortune as he turns 18 on Monday, but he insists the money won't cast a spell on him. Daniel Radcliffe as Harry Potter in \"Harry Potter and the Order of the Phoenix\" To the disappointment of gossip columnists around the world, the young actor says he has no plans to fritter his cash away on fast cars, drink and celebrity parties. \"I don't plan to be one of those people who, as soon as they turn 18, suddenly buy themselves a massive sports car collection or something similar,\" he told an Australian interviewer earlier this month. \"I don't think I'll be particularly extravagant. \"The things I like buying are things that cost about 10 pounds -- books and CDs and DVDs.\" At 18, Radcliffe will be able to gamble in a casino, buy a drink in a pub or see the horror film \"Hostel: Part II,\" currently six places below his number one movie on the UK box office chart. Details of how he'll mark his landmark birthday are under wraps. His agent and publicist had no comment on his plans. \"I'll definitely have some sort of party,\" he said in an interview. \"Hopefully none of you will be reading about it.\" Radcliffe's earnings from the first five Potter films have been held in a trust fund which he has not been able to touch. Despite his growing fame and riches, the actor says he is keeping his feet firmly on the ground. \"People are always looking to say 'kid star goes off the rails,'\" he told reporters last month. \"But I try very hard not to go that way because it would be too easy for them.\" His latest outing as the boy wizard in \"Harry Potter and the Order of the Phoenix\" is breaking records on both sides of the Atlantic and he will reprise the role in the last two films.  Watch I-Reporter give her review of Potter's latest » . There is life beyond Potter, however. The Londoner has filmed a TV movie called \"My Boy Jack,\" about author Rudyard Kipling and his son, due for release later this year. He will also appear in \"December Boys,\" an Australian film about four boys who escape an orphanage. Earlier this year, he made his stage debut playing a tortured teenager in Peter Shaffer's \"Equus.\" Meanwhile, he is braced for even closer media scrutiny now that he's legally an adult: \"I just think I'm going to be more sort of fair game,\" he told Reuters. E-mail to a friend . Copyright 2007 Reuters. All rights reserved.This material may not be published, broadcast, rewritten, or redistributed."
        }
    ],
    "ability": "summarization",
    "reward_model": {
        "style": "llmj-summarization",
        "ground_truth": "Harry Potter star Daniel Radcliffe gets £20M fortune as he turns 18 Monday .\nYoung actor says he has no plans to fritter his cash away .\nRadcliffe's earnings from first five Potter films have been held in trust fund ."
    },
    "extra_info": {
        "question": "LONDON, England (Reuters) -- Harry Potter star Daniel Radcliffe gains access to a reported £20 million ($41.1 million) fortune as he turns 18 on Monday, but he insists the money won't cast a spell on him. Daniel Radcliffe as Harry Potter in \"Harry Potter and the Order of the Phoenix\" To the disappointment of gossip columnists around the world, the young actor says he has no plans to fritter his cash away on fast cars, drink and celebrity parties. \"I don't plan to be one of those people who, as soon as they turn 18, suddenly buy themselves a massive sports car collection or something similar,\" he told an Australian interviewer earlier this month. \"I don't think I'll be particularly extravagant. \"The things I like buying are things that cost about 10 pounds -- books and CDs and DVDs.\" At 18, Radcliffe will be able to gamble in a casino, buy a drink in a pub or see the horror film \"Hostel: Part II,\" currently six places below his number one movie on the UK box office chart. Details of how he'll mark his landmark birthday are under wraps. His agent and publicist had no comment on his plans. \"I'll definitely have some sort of party,\" he said in an interview. \"Hopefully none of you will be reading about it.\" Radcliffe's earnings from the first five Potter films have been held in a trust fund which he has not been able to touch. Despite his growing fame and riches, the actor says he is keeping his feet firmly on the ground. \"People are always looking to say 'kid star goes off the rails,'\" he told reporters last month. \"But I try very hard not to go that way because it would be too easy for them.\" His latest outing as the boy wizard in \"Harry Potter and the Order of the Phoenix\" is breaking records on both sides of the Atlantic and he will reprise the role in the last two films.  Watch I-Reporter give her review of Potter's latest » . There is life beyond Potter, however. The Londoner has filmed a TV movie called \"My Boy Jack,\" about author Rudyard Kipling and his son, due for release later this year. He will also appear in \"December Boys,\" an Australian film about four boys who escape an orphanage. Earlier this year, he made his stage debut playing a tortured teenager in Peter Shaffer's \"Equus.\" Meanwhile, he is braced for even closer media scrutiny now that he's legally an adult: \"I just think I'm going to be more sort of fair game,\" he told Reuters. E-mail to a friend . Copyright 2007 Reuters. All rights reserved.This material may not be published, broadcast, rewritten, or redistributed.",
        "split": "train",
        "index": 0,
        "source_id": "42c027e4ff9730fbb3de84c1af0d2c50"
    }
}

```

## RLAIF - Custom Prompt

In this example, we use [RLAIF - Chain of Thought](#model-customize-open-weight-samples-rlaif2 "#model-customize-open-weight-samples-rlaif2") to discuss how a
custom jinja prompt can replace one of the preset prompts.

**Below is an example of a custom prompt for
CoT:**

```
You are an expert logical reasoning evaluator specializing in Chain-of-Thought (CoT) analysis.

Given: A problem prompt and a model's reasoning-based response.

Goal: Assess the quality and structure of logical reasoning, especially for specialized domains (law, medicine, finance, etc.).

Scoring rubric (start at 0.0, then add or subtract):

Core Components:

Structural Completeness (0.3 max)
- Clear problem statement: +0.05
- Defined variables/terminology: +0.05
- Organized given information: +0.05
- Explicit proof target: +0.05
- Step-by-step reasoning: +0.05
- Clear conclusion: +0.05

Logical Quality (0.4 max)
- Valid logical flow: +0.1
- Proper use of if-then relationships: +0.1
- Correct application of domain principles: +0.1
- No logical fallacies: +0.1

Technical Accuracy (0.3 max)
- Correct use of domain terminology: +0.1
- Accurate application of domain rules: +0.1
- Proper citation of relevant principles: +0.1

Critical Deductions:
A. Invalid logical leap: -0.3
B. Missing critical steps: -0.2
C. Incorrect domain application: -0.2
D. Unclear/ambiguous reasoning: -0.1

Additional Instructions:
- Verify domain-specific terminology and principles
- Check for logical consistency throughout
- Ensure conclusions follow from premises
- Flag potential domain-specific compliance issues
- Consider regulatory/professional standards where applicable

Return EXACTLY this JSON (no extra text):
{
    "score": <numerical score 0.0-1.0>,
    "component_scores": {
        "structural_completeness": <score>,
        "logical_quality": <score>,
        "technical_accuracy": <score>
    },
    "steps_present": {
        "problem_statement": <true/false>,
        "variable_definitions": <true/false>,
        "given_information": <true/false>,
        "proof_target": <true/false>,
        "step_reasoning": <true/false>,
        "conclusion": <true/false>
    },
    "reasoning": "<explain scoring decisions and identify any logical gaps>",
    "domain_flags": ["<any domain-specific concerns or compliance issues>"]
}

### (Prompt field from dataset)
Problem Prompt: {{ prompt }}

Model's Response: {{ model_output }}

### Ground truth (if applicable):
{{ ground_truth }}

```

## Reinforcement Learning from Verifiable Rewards (RLVR) - Exact Match

**Input Dataset**

Source: [https://huggingface.co/datasets/openai/gsm8k](https://huggingface.co/datasets/openai/gsm8k "https://huggingface.co/datasets/openai/gsm8k")

**Sample**

```
{
  "data_source": "openai/gsm8k",
  "prompt": [
    {
      "content": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May? Let\'s think step by step and output the final answer after \\"####\\".",
      "role": "user"
    }
  ],
  "ability": "math",
  "reward_model": {
    "ground_truth": "72",
    "style": "rule"
  },
  "extra_info": {
    "answer": "Natalia sold 48\\/2 = <<48\\/2=24>>24 clips in May.\\nNatalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.\\n#### 72",
    "index": 0,
    "question": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?",
    "split": "train"
  }
}

```

## RLVR - Code Execution

**Input Dataset**

Source: [https://huggingface.co/datasets/open-r1/codeforces](https://huggingface.co/datasets/open-r1/codeforces "https://huggingface.co/datasets/open-r1/codeforces")

**Sample**

````
{
  "data_source": "codeforces",
  "prompt": [
    {
      "content": "\nWhen tackling complex reasoning tasks, you have access to the following actions. Use them as needed to progress through your thought process.\n\n[ASSESS]\n\n[ADVANCE]\n\n[VERIFY]\n\n[SIMPLIFY]\n\n[SYNTHESIZE]\n\n[PIVOT]\n\n[OUTPUT]\n\nYou should strictly follow the format below:\n\n[ACTION NAME]\n\n# Your action step 1\n\n# Your action step 2\n\n# Your action step 3\n\n...\n\nNext action: [NEXT ACTION NAME]\n\n",
      "role": "system"
    },
    {
      "content": "Title: Zebras\n\nTime Limit: None seconds\n\nMemory Limit: None megabytes\n\nProblem Description:\nOleg writes down the history of the days he lived. For each day he decides if it was good or bad. Oleg calls a non-empty sequence of days a zebra, if it starts with a bad day, ends with a bad day, and good and bad days are alternating in it. Let us denote bad days as 0 and good days as 1. Then, for example, sequences of days 0, 010, 01010 are zebras, while sequences 1, 0110, 0101 are not.\n\nOleg tells you the story of days he lived in chronological order in form of string consisting of 0 and 1. Now you are interested if it is possible to divide Oleg's life history into several subsequences, each of which is a zebra, and the way it can be done. Each day must belong to exactly one of the subsequences. For each of the subsequences, days forming it must be ordered chronologically. Note that subsequence does not have to be a group of consecutive days.\n\nInput Specification:\nIn the only line of input data there is a non-empty string *s* consisting of characters 0 and 1, which describes the history of Oleg's life. Its length (denoted as |*s*|) does not exceed 200<=000 characters.\n\nOutput Specification:\nIf there is a way to divide history into zebra subsequences, in the first line of output you should print an integer *k* (1<=\u2264<=*k*<=\u2264<=|*s*|), the resulting number of subsequences. In the *i*-th of following *k* lines first print the integer *l**i* (1<=\u2264<=*l**i*<=\u2264<=|*s*|), which is the length of the *i*-th subsequence, and then *l**i* indices of days forming the subsequence. Indices must follow in ascending order. Days are numbered starting from 1. Each index from 1 to *n* must belong to exactly one subsequence. If there is no way to divide day history into zebra subsequences, print -1.\n\nSubsequences may be printed in any order. If there are several solutions, you may print any of them. You do not have to minimize nor maximize the value of *k*.\n\nDemo Input:\n['0010100\\n', '111\\n']\n\nDemo Output:\n['3\\n3 1 3 4\\n3 2 5 6\\n1 7\\n', '-1\\n']\n\nNote:\nnone\n\nWrite Python code to solve the problem. Present the code in \n```python\nYour code\n```\nat the end.",
      "role": "user"
    }
  ],
  "ability": "code",
  "reward_model": {
    "ground_truth": "{\"inputs\": [\"0010100\", \"111\", \"0\", \"1\", \"0101010101\", \"010100001\", \"000111000\", \"0101001000\", \"0000001000\", \"0101\", \"000101110\", \"010101010\", \"0101001010\", \"0100101100\", \"0110100000\", \"0000000000\", \"1111111111\", \"0010101100\", \"1010000\", \"0001110\", \"0000000000011001100011110101000101000010010111000100110110000011010011110110001100100001001001010010\", \"01010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010\", \"0010011100000000\"], \"outputs\": [\"3\\n1 1\\n5 2 3 4 5 6\\n1 7\", \"-1\", \"1\\n1 1\", \"-1\", \"-1\", \"-1\", \"3\\n3 1 6 7\\n3 2 5 8\\n3 3 4 9\", \"4\\n5 1 2 3 4 5\\n3 6 7 8\\n1 9\\n1 10\", \"8\\n1 1\\n1 2\\n1 3\\n1 4\\n1 5\\n3 6 7 8\\n1 9\\n1 10\", \"-1\", \"-1\", \"1\\n9 1 2 3 4 5 6 7 8 9\", \"2\\n5 1 2 3 4 5\\n5 6 7 8 9 10\", \"2\\n5 1 2 3 8 9\\n5 4 5 6 7 10\", \"-1\", \"10\\n1 1\\n1 2\\n1 3\\n1 4\\n1 5\\n1 6\\n1 7\\n1 8\\n1 9\\n1 10\", \"-1\", \"2\\n3 1 8 9\\n7 2 3 4 5 6 7 10\", \"-1\", \"-1\", \"22\\n1 1\\n1 2\\n1 3\\n1 4\\n1 5\\n1 6\\n1 7\\n1 8\\n7 9 24 25 26 27 28 29\\n7 10 13 14 17 18 23 30\\n11 11 12 15 16 19 22 31 32 33 34 35\\n3 20 21 36\\n3 37 46 47\\n9 38 39 40 45 48 57 58 75 76\\n17 41 42 43 44 49 50 51 54 55 56 59 72 73 74 77 80 81\\n9 52 53 60 71 78 79 82 83 84\\n7 61 64 65 66 67 70 85\\n5 62 63 68 69 86\\n3 87 88 89\\n3 90 91 92\\n5 93 94 95 96 97\\n3 98 99 100\", \"1\\n245 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 ...\", \"8\\n3 1 8 9\\n5 2 3 4 7 10\\n3 5 6 11\\n1 12\\n1 13\\n1 14\\n1 15\\n1 16\"]}",
    "style": "rule"
  },
  "extra_info": {
    "index": 49,
    "split": "train"
  }
}

````

**Reward Function**

Reward Function: [https://github.com/volcengine/verl/tree/main/verl/utils/reward_score/prime_code](https://github.com/volcengine/verl/tree/main/verl/utils/reward_score/prime_code "https://github.com/volcengine/verl/tree/main/verl/utils/reward_score/prime_code")

## RLVR - Math Answer

**Input Dataset**

Source: Cleaned gsm8k dataset [https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data](https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data "https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data")

**Sample**

```
[
    {
        "content": "\nYou are an AI assistant that uses a Chain of Thought (CoT) approach with reflection to answer queries...",
        "role": "system"
    },
    {
        "content": "A craft store makes a third of its sales in the fabric section, a quarter of its sales in the jewelry section, and the rest in the stationery section. They made 36 sales today. How many sales were in the stationery section?",
        "role": "user"
    },
    {
        "content": "\nTo find the number of sales in the stationery section, I need to first calculate the number of sales in the fabric and jewelry sections...\n\n\n<reasoning>\n1. Calculate the number of sales in the fabric section: 36 * 1/3 = 12\n2. Calculate the number of sales in the jewelry section: 36 * 1/4 = 9\n3. Calculate the number of sales in the stationery section: 36 - 12 - 9 = 15\n</reasoning>\n\n<reflection>\nUpon reviewing my reasoning, I noticed that my calculations seem correct...\n</reflection>\n\n<adjustment>\nUpon re-examining my math, I am confident that my calculations are correct...\n</adjustment>\n\n<output>\n15\n</output>",
        "role": "assistant"
    }
]

```

**Reward Calculation**

Reward Function: [https://github.com/volcengine/verl/blob/main/verl/utils/reward_score/gsm8k.py](https://github.com/volcengine/verl/blob/main/verl/utils/reward_score/gsm8k.py "https://github.com/volcengine/verl/blob/main/verl/utils/reward_score/gsm8k.py")

## RLVR - Custom Lambda

**Input Dataset**

Source: Cleaned gsm8k dataset [https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data](https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data "https://huggingface.co/datasets/thesven/gsm8k-reasoning/tree/main/data")

**Sample**

```
[
  {
    "content": "\nYou are an AI assistant that uses a Chain of Thought (CoT) approach with reflection to answer queries.\n\nFollow these steps:\n- Think through the problem step by step within the ‹thinking> tags.\n- Reflect on your thinking\n\nto check for any errors or improvements within the ‹reflection› tags.\n- Make any necessary adjustments based on your reflection.\n- Provide your final, concise answer within the ‹output> tags.\n\nImportant: The <thinking> and ‹reflection› sections are for your internal reasoning process only.\nDo not include any part of the final answer in these sections.\nThe actual response to the query must be entirely contained within the ‹output› tags.\n\nUse the following format for your response:\n<thinking>\n[Your initial thought process goes here]\n</thinking›\n\n<reasoning>\n[Your step-by-step reasoning goes here. This is your internal thought process, not the final answer. You can create as many reasoning steps as necessary in your process.]\n</reasoning>\n\n‹reflection>\n[Your reflection on your reasoning, checking for errors or improvements. You can create as many reflection steps as necessary in your process.]\n</ reflection>\n\n<adjustment>\n[Any adjustments to your thinking based on your reflection]\n</adjustment>\n\n<output>\n[Your final, concise answer to the query. This is the only part that will be shown to the user.]\n</output>\n",
    "role": "system"
  },
  {
    "content": "A craft store makes a third of its sales in the fabric section, a quarter of its sales in the jewelry section, and the rest in the stationery section. They made 36 sales today. How many sales were in the stationery section?",
    "role": "user"
  },
  {
    "content": "<thinking>\nTo find the number of sales in the stationery section, I need to first calculate the number of sales in the fabric and jewelry sections. The store makes a third of its sales in the fabric section, which is 1/3 of 36 sales. I can calculate this as 36 * 1/3 = 12 sales in the fabric section. The store makes a quarter of its sales in the jewelry section, which is 1/4 of 36 sales. I can calculate this as 36 * 1/4 = 9 sales in the jewelry section. Since the rest of the sales are in the stationery section, I can subtract the sales from the other two sections from the total number of sales to find the number of sales in the stationery section.\n</thinking>\n\n<reasoning>\n1. Calculate the number of sales in the fabric section: 36 * 1/3 = 12\n2. Calculate the number of sales in the jewelry section: 36 * 1/4 = 9\n3. Calculate the number of sales in the stationery section: 36 - 12 - 9 = 15\n</reasoning>\n\n‹reflection>\nUpon reviewing my reasoning, I noticed that my calculations seem correct, but I should ensure that I understand the question correctly. The question asks for the number of sales in the stationery section, and I believe I have correctly calculated that. However, I should double-check my math to make sure it's accurate.\n</reflection>\n\n<adjustment>\nUpon re-examining my math, I am confident that my calculations are correct. The fabric section makes up 1/3 of the sales, the jewelry section makes up 1/4, and the rest is the stationery section. My math checks out, and I am confident in my answer.\n</adjustment>\n\n<output>\n15\n</output>",
    "role": "assistant"
  }
]

```

**Sample Reward Calculation**

```
# RLVR Evaluator for OSS

# lambda_grader.py
import json
import re
import uuid
from typing import Any, Dict, List

def custom_reward(assistant_answer: str, ground_truth: str) -> float:
    """
    Add custom reward computation here

    Example:-
    Reward = fraction of ground-truth words that are correct
    in the correct position.

    Example:
      gt:   "the cat sat"
      ans:  "the dog sat"

      word-by-word:
        "the" == "the"  -> correct
        "dog" != "cat"  -> wrong
        "sat" == "sat"  -> correct

      correct = 2 out of 3 -> reward = 2/3 ≈ 0.67
    """
    ans_words = assistant_answer.strip().lower().split()
    gt_words = ground_truth.strip().lower().split()

    if not gt_words:
        return 0.0

    correct = 0
    for aw, gw in zip(ans_words, gt_words):
        if aw == gw:
            correct += 1

    return correct / len(gt_words)


# Lambda utility functions
def _ok(body: Any, code: int = 200) -> Dict[str, Any]:
    return {
        "statusCode": code,
        "headers": {
            "content-type": "application/json",
            "access-control-allow-origin": "*",
            "access-control-allow-methods": "POST,OPTIONS",
            "access-control-allow-headers": "content-type",
        },
        "body": json.dumps(body),
    }

def _assistant_text(sample: Dict[str, Any]) -> str:
    """Extract assistant text from sample messages."""
    for m in reversed(sample.get("messages", [])):
        if m.get("role") == "assistant":
            return (m.get("content") or "").strip()
    return ""

def _sample_id(sample: Dict[str, Any]) -> str:
    """Generate or extract sample ID."""
    if isinstance(sample.get("id"), str) and sample["id"]:
        return sample["id"]

    return str(uuid.uuid4())

def _ground_truth(sample: Dict[str, Any]) -> str:
    """Extract ground truth from sample or metadata if available"""

    if isinstance(sample.get("reference_answer"), str) and sample["reference_answer"]:
        return sample["reference_answer"].strip()

    md = sample.get("metadata") or {}
    gt = md.get("reference_answer", None) or md.get("ground_truth", None)
    if gt is None:
        return ""
    return str(gt).strip()


def _score_and_metrics(sample: Dict[str, Any]) -> Dict[str, Any]:
    sid = _sample_id(sample)
    solution_text = _assistant_text(sample)

    # Extract ground truth
    gt = _ground_truth(sample)

    metrics_list: List[Dict[str, Any]] = []

    # Custom rlvr scoring
    if solution_text and gt:

        # Compute score
        reward_score = custom_reward(
            assistant_answer=solution_text,
            ground_truth=gt
        )

        # Add detailed metrics
        metrics_list.append({
            "name": "custom_reward_score",
            "value": float(reward_score),
            "type": "Reward"
        })

        # The aggregate reward score is the custom reward score
        aggregate_score = float(reward_score)

    else:
        # No solution text or ground truth - default to 0
        aggregate_score = 0.0
        metrics_list.append({
            "name": "default_zero",
            "value": 0.0,
            "type": "Reward"
        })
    print("detected score", {
        "id": sid,
        "aggregate_reward_score": float(aggregate_score),
        "metrics_list": metrics_list,
    })
    return {
        "id": sid,
        "aggregate_reward_score": float(aggregate_score),
        "metrics_list": metrics_list,
    }

def lambda_handler(event, context):
    """AWS Lambda handler for custom reward lambda grading."""
    # CORS preflight
    if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
        return _ok({"ok": True})

    # Body may be a JSON string (API GW/Function URL) or already a dict (Invoke)
    raw = event.get("body") or "{}"
    try:
        body = json.loads(raw) if isinstance(raw, str) else raw
    except Exception as e:
        return _ok({"error": f"invalid JSON body: {e}"}, 400)

    # Accept top-level list, {"batch":[...]}, or single sample object
    if isinstance(body, dict) and isinstance(body.get("batch"), list):
        samples = body["batch"]
    else:
        return _ok({
            "error": "Send a sample object, or {'batch':[...]} , or a top-level list of samples."
        }, 400)

    try:
        results = [_score_and_metrics(s) for s in samples]
    except Exception as e:
        return _ok({"error": f"Custom scoring failed: {e}"}, 500)

    return _ok(results)


```

**Sample reward function code**

```
# RLVR Evaluator for OSS
# lambda_grader.py

import json
import re
import uuid from typing
import Any, Dict, List

def custom_reward(assistant_answer: str, ground_truth: str) -> float:
    """
    Add custom reward computation here

    Example:-
    Reward = fraction of ground-truth words that are correct
    in the correct position.

    Example:
      gt:   "the cat sat"
      ans:  "the dog sat"

      word-by-word:
        "the" == "the"  -> correct
        "dog" != "cat"  -> wrong
        "sat" == "sat"  -> correct

      correct = 2 out of 3 -> reward = 2/3 ≈ 0.67
    """
    ans_words = assistant_answer.strip().lower().split()
    gt_words = ground_truth.strip().lower().split()

    if not gt_words:
        return 0.0

    correct = 0
    for aw, gw in zip(ans_words, gt_words):
        if aw == gw:
            correct += 1

    return correct / len(gt_words)


# Lambda utility functions
def _ok(body: Any, code: int = 200) -> Dict[str, Any]:
    return {
        "statusCode": code,
        "headers": {
            "content-type": "application/json",
            "access-control-allow-origin": "*",
            "access-control-allow-methods": "POST,OPTIONS",
            "access-control-allow-headers": "content-type",
        },
        "body": json.dumps(body),
    }

def _assistant_text(sample: Dict[str, Any]) -> str:
    """Extract assistant text from sample messages."""
    for m in reversed(sample.get("messages", [])):
        if m.get("role") == "assistant":
            return (m.get("content") or "").strip()
    return ""

def _sample_id(sample: Dict[str, Any]) -> str:
    """Generate or extract sample ID."""
    if isinstance(sample.get("id"), str) and sample["id"]:
        return sample["id"]

    return str(uuid.uuid4())

def _ground_truth(sample: Dict[str, Any]) -> str:
    """Extract ground truth from sample or metadata if available"""

    if isinstance(sample.get("reference_answer"), str) and sample["reference_answer"]:
        return sample["reference_answer"].strip()

    md = sample.get("metadata") or {}
    gt = md.get("reference_answer", None) or md.get("ground_truth", None)
    if gt is None:
        return ""
    return str(gt).strip()


def _score_and_metrics(sample: Dict[str, Any]) -> Dict[str, Any]:
    sid = _sample_id(sample)
    solution_text = _assistant_text(sample)

    # Extract ground truth
    gt = _ground_truth(sample)

    metrics_list: List[Dict[str, Any]] = []

    # Custom rlvr scoring
    if solution_text and gt:

        # Compute score
        reward_score = custom_reward(
            assistant_answer=solution_text,
            ground_truth=gt
        )

        # Add detailed metrics
        metrics_list.append({
            "name": "custom_reward_score",
            "value": float(reward_score),
            "type": "Reward"
        })

        # The aggregate reward score is the custom reward score
        aggregate_score = float(reward_score)

    else:
        # No solution text or ground truth - default to 0
        aggregate_score = 0.0
        metrics_list.append({
            "name": "default_zero",
            "value": 0.0,
            "type": "Reward"
        })
    print("detected score", {
        "id": sid,
        "aggregate_reward_score": float(aggregate_score),
        "metrics_list": metrics_list,
    })
    return {
        "id": sid,
        "aggregate_reward_score": float(aggregate_score),
        "metrics_list": metrics_list,
    }

def lambda_handler(event, context):
    """AWS Lambda handler for custom reward lambda grading."""
    # CORS preflight
    if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
        return _ok({"ok": True})

    # Body may be a JSON string (API GW/Function URL) or already a dict (Invoke)
    raw = event.get("body") or "{}"
    try:
        body = json.loads(raw) if isinstance(raw, str) else raw
    except Exception as e:
        return _ok({"error": f"invalid JSON body: {e}"}, 400)

    # Accept top-level list, {"batch":[...]}, or single sample object
    if isinstance(body, dict) and isinstance(body.get("batch"), list):
        samples = body["batch"]
    else:
        return _ok({
            "error": "Send a sample object, or {'batch':[...]} , or a top-level list of samples."
        }, 400)

    try:
        results = [_score_and_metrics(s) for s in samples]
    except Exception as e:
        return _ok({"error": f"Custom scoring failed: {e}"}, 500)

    return _ok(results)

```

**Sample reward prompt**

```
You are an expert RAG response evaluator specializing in faithfulness and relevance assessment.
Given: Context documents, a question, and response statements.
Goal: Evaluate both statement-level faithfulness and overall response relevance to the question.

Scoring rubric (start at 0.0, then add or subtract):

Core Components:

Faithfulness Assessment (0.6 max)
Per statement evaluation:
- Direct support in context: +0.2
- Accurate inference from context: +0.2
- No contradictions with context: +0.2
Deductions:
- Hallucination: -0.3
- Misrepresentation of context: -0.2
- Unsupported inference: -0.1

Question Relevance (0.4 max)
- Direct answer to question: +0.2
- Appropriate scope/detail: +0.1
- Proper context usage: +0.1
Deductions:
- Off-topic content: -0.2
- Implicit/meta responses: -0.2
- Missing key information: -0.1

Critical Flags:
A. Complete hallucination
B. Context misalignment
C. Question misinterpretation
D. Implicit-only responses

Additional Instructions:
- Evaluate each statement independently
- Check for direct textual support
- Verify logical inferences
- Assess answer completeness
- Flag any unsupported claims

Return EXACTLY this JSON (no extra text):
{
    "statements_evaluation": [
        {
            "statement": "<statement_text>",
            "verdict": <0 or 1>,
            "reason": "<detailed explanation>",
            "context_support": "<relevant context quote or 'None'>"
        }
    ],
    "overall_assessment": {
        "question_addressed": <0 or 1>,
        "reasoning": "<explanation>",
        "faithfulness_score": <0.0-1.0>,
        "relevance_score": <0.0-1.0>
    },
    "flags": ["<any critical issues>"]
}

## Current Evaluation Task

### Context
{{ ground_truth }}

### Question
{{ extra_info.question }}

### Model's Response
{{ model_output }}
```
