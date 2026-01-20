# AWS Documentation Archive

This repository provides weekly snapshots of AWS documentation converted to Markdown format. It's useful if you need:

- **Markdown versions of AWS docs** for giving context to AI agents, training models, or offline reference
- **Historical tracking** of how AWS documentation changes over time

The repository automatically crawls the AWS documentation index once per week, converts the HTML pages to Markdown, and commits the results. The Git history provides a complete timeline of documentation updates across all AWS services.

## Running the crawler

To run the crawler locally:

```bash
pip install -r requirements.txt
python crawler.py
```

To crawl a specific service:

```bash
python crawler.py --service-url "https://docs.aws.amazon.com/AmazonS3/latest/userguide/"
```

## Licensing and attribution

The content in the `docs/` directory is mirrored from
[docs.aws.amazon.com](https://docs.aws.amazon.com/) and is licensed by Amazon Web
Services as follows:

- **Documentation (guides, tutorials, narrative text, diagrams, etc.)** is
  licensed under the [Creative Commons Attribution-ShareAlike 4.0 International
  License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
- **Sample code, scripts, and code snippets** that accompany the documentation
  are licensed under the [MIT No Attribution License (MIT-0)](https://spdx.org/licenses/MIT-0.html).

These terms are described in the AWS site terms at
[https://aws.amazon.com/terms/](https://aws.amazon.com/terms/). When redistributing
or modifying any files from `docs/`, you must:

1. Attribute the original work to Amazon Web Services in accordance with CC
   BY-SA 4.0, including a link to the source material and to the license.
2. Share any derivative documentation under the same CC BY-SA 4.0 license.
3. Retain the MIT-0 license notice with any redistributed code examples.

No rights are granted with respect to the AWS trademarks, service marks, or
logos that may appear in the archived content.

