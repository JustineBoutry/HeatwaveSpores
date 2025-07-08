Description of the data and file structure
## 1. Data preparation and processing

This section outlines the steps taken to clean, transform and structure our dataset (daphnia_data.rds) for subsequent analysis. Our dataset comprises various measurements of a sample of biological entities, including spore counts, infection statuses and life cycle metrics such as clutch size, offspring numbers and developmental stages. However, the raw dataset contained missing values that needed to be addressed prior to analysis.

### 1.1 Column descriptions

Below is a detailed explanation of each column in the dataset. This breakdown is intended to provide clarity on the variable names, units, and biological significance.

- ID: A unique identifier for each sample, used to distinguish individual observations.

- Temperature: The experimental temperature (in °C) at which each sample was maintained. The possible values are 20, 30 and 40 °C, which were used to examine the effects of temperature on biological parameters.

- Isolate: Identifier for the specific parasite genotype used in the experiment (e.g. C1, C14, C18, C24). Each genotype represents a distinct biological strain or lineage of the parasite.

- Infection_problem: A binary indicator noting whether any issues were encountered during infection monitoring. Missing values indicate no known issues.

- Clutch: The number of clutch events recorded for each sample, representing reproductive events or cycles.

- Nb_offspring: The total number of offspring produced by each sample across clutch events.

- FirstClutchAge: The age (in days) at which the first clutch was recorded.

- LastClutchAge: The age (in days) at which the last clutch was recorded.

- DeathAge: Age (in days) at death, providing a measure of lifespan for each sample.

- Accidental_death: Indicates whether the death was accidental. Missing values suggest non-accidental or unspecified causes.

- ReddishAge: The age (in days) at which reddish pigmentation was first observed, which is a developmental marker.

- Not_red_age: An alternative developmental marker indicating an age (in days) at which reddish pigmentation was not observed.

- Volume_counted: The volume of the sample (in microlitres) counted under observation and used to standardise spore counts.

- InfectedStatus: The infection status of each sample, with possible values including ‘infected’, ‘not_inf’ (not infected) or ‘lost’ for missing data.

- Number of mature spores: The raw count of mature spores in the sample.

- Number of immature spores (imm): The raw count of immature spores representing early-stage spore development.

- Nb of white spores (whites): The number of white spores, which are mature but may appear different depending on the time elapsed between sample preparation and counting.

- cauliflowers: A categorical indicator (yes/no) of whether cauliflower-like structures were observed in the sample.

- grapes: A categorical indicator (yes/no) of the presence of grape-like structures, which are another morphological feature observed in spore samples.

- Nb of activated spores: The number of activated spores, which often indicates the number in a potentially infectious state.

- mature_load: The calculated load of mature spores, standardised based on ‘Volume_counted’. This represents the density of mature spores in the sample volume.

- imm_load: The load of immature spores, calculated similarly to ‘mature_load’ for standardised comparison.

- ratio: The ratio of mature spores to the total spore load (mature and immature). This metric provides an indication of spore maturation and infection severity.

- Batch: A grouping variable created based on ID, representing experimental batches. This factor enables batch effects to be controlled in the analysis.

- group: A combination of isolation and temperature conditions (e.g. C1840) used to categorise samples in specific experimental settings.

### 1.2 Key Data Processing Steps

In the markdown document Final_analysis.Rmd you will find all the steps of the analyses. However, the main steps followed for each varaible analysed are listed below.

1. Variable Conversion: Several columns required type conversion to facilitate analysis. For example, ‘Volume_counted’ and ‘Nb of white spores’ were converted to numeric values. During this process, some ‘NA’ values were introduced due to incompatible data entries.

2. Factorization: The categorical variables ‘cauliflowers’, ‘grapes’ and ‘group’ were converted into factor variables. Additionally, the ‘Isolate’ and ‘Temperature’ variables were explicitly factored to ensure clear categorical representation.

3. Data Subsetting and Exclusion: Observations with specific conditions, such as an ID of 50, were excluded to maintain data integrity.

4. Calculation of Derived Variables:

- Spore Load Calculations: Two new variables were calculated: ‘mature_load’ and ‘imm_load’, representing the load of mature and immature spores respectively, standardised per unit volume.

- Infection Ratio: The ratio variable was calculated as the proportion of mature spores relative to the total spore load to provide an indicator of infection severity.

5. Grouping and Batching: Observations were assigned to batches for experimental grouping based on their ID. This enables batch effects to be tracked and controlled in downstream analysis.
