# Creating blueprints for images

Amazon Bedrock Data Automation (BDA) allows you to create custom blueprints for image
modalities. You can use blueprints to define the desired output format and extraction logic for
your input files. By creating custom blueprints, you can tailor BDA's output to meet your
specific requirements. Within one project, you can apply a single image blueprint.

## Defining data fields for images

BDA allows you to define the specific fields you want to identify from your images by
creating a blueprint. This acts as a set of instructions that guide BDA on what information to
extract and generate from your images.

### Blueprint fields examples for advertisement images

Here are some examples of blueprint fields to analyze advertisement images.

|                               |                                                                                                                                                 |                     |          |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Field**                     | **Instruction**                                                                                                                                 | **Extraction Type** | **Type** |
| product_type                  | What is the primary product or service being advertised? Ex: Clothing, Electronics, Food & Beverage                                             | inferred            | string   |
| product_placement             | How is the product placed in the advertisement image, e.g., centered, in the background, held by a person, etc.?                                | inferred            | string   |
| product_size                  | Product size is small if size is less than 30% of the image, medium if it is between 30 to 60%, and large if it is larger than 60% of the image | inferred            | string   |
| image_style                   | Classify the image style of the ad. For example, product image, lifestyle, portrait, retro, infographic, none of the above.                     | inferred            | string   |
| image_background              | Background can be" solid color, natural landscape, indoor, outdoor, or abstract.                                                                | inferred            | string   |
| promotional_offer             | Does the advertisement include any discounts, offers, or promotional messages?                                                                  | inferred            | boolean  | ### Examples of blueprint fields for media search Here are some examples of blueprint fields to generate metadata from images for media search. |
|                               |                                                                                                                                                 |                     |          |
| ---                           | ---                                                                                                                                             | ---                 | ---      |
| **Field**                     | **Instruction**                                                                                                                                 | **Extraction Type** | **Type** |
| person_counting               | How many people are in the image?                                                                                                               | inferred            | number   |
| indoor_outdoor_classification | Is the image indoor or outdoor?                                                                                                                 | inferred            | string   |
| scene_classification          | Classify the setting or environment of the image. Ex: Urban, Rural, Natural, Historical, Residential, Commercial, Recreational, Public Spaces   | inferred            | string   |
| animal_identification         | Does the image contain any animals?                                                                                                             | inferred            | boolean  |
| animal_type                   | What type of animals are present in the image?                                                                                                  | inferred            | string   |
| color_identification          | Is the image in color or black and white?                                                                                                       | inferred            | string   |
| vehicle_identification        | Is there any vehicle visible in the image?                                                                                                      | inferred            | string   |
| vehicle_type                  | What type of vehicle is present in the image?                                                                                                   | inferred            | string   |
| watermark_identification      | Is there any watermark visible in the image?                                                                                                    | inferred            | boolean  |
