# Overview

I am very interested in how countries, cultures, communities, and families care for the elderly. In the US, there will be more people aged over 65 than under 18 for the first time in US history by 2034 ([US Census Bureau, 2018](https://www.census.gov/newsroom/press-releases/2018/cb18-41-population-projections.html)). Many other countries have aging populations as well, with citizens living longer and having fewer children. This raises lots of economic questions: Has this generation saved adequately for retirement? Can the labor force adjust to compensate for their exit? Do we have enough long-term care facilities for a growing patient population? Many of these questions center around one larger theme: Who is going to care for the elderly?

This personal project is for data exploration. I want to see what I can do with existing data on one measure of age-related demographics: the old age dependency ratio. As defined by the World Bank, the old age dependency ratio is the ratio of "older dependents" (people older than 64) to the working-age population (people ages 15-64). This measure is tightly related to the "care burden" placed on people in the labor force to care for the previous generation, whether that is through welfare systems or care within families.

# Visualizations

* [global_map.py](https://github.com/mayalroy/dependency_ratio_viz/blob/main/global_map.py)&mdash;This script takes in country border data from [Natural Earth](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/) and dependency ratio data from the [World Bank](https://data.worldbank.org/indicator/SP.POP.DPND.OL) and creates a GIF showing how countries' old age depency ratios changed between 1960 and 2019. My handling of the geographic data is heavily based on [this tutorial](https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0) from Towards Data Science.

![Alt text](https://github.com/mayalroy/dependency_ratio_viz/blob/main/output/global_age_dependency_time.gif)
