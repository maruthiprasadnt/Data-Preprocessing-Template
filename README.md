# Data-Preprocessing-Template

Why preprocessing ?

Real world data are generally
Incomplete: lacking attribute values, lacking certain attributes of interest, or containing only aggregate data
Noisy: containing errors or outliers

Inconsistent: containing discrepancies in codes or names
Tasks in data preprocessing
Data cleaning: fill in missing values, smooth noisy data, identify or remove outliers, and resolve inconsistencies.
Data integration: using multiple databases, data cubes, or files.
Data transformation: normalization and aggregation.
Data reduction: reducing the volume but producing the same or similar analytical results.
Data discretization: part of data reduction, replacing numerical attributes with nominal ones.

Data cleaning
Fill in missing values (attribute or class value):
Ignore the tuple: usually done when class label is missing.
Use the attribute mean (or majority nominal value) to fill in the missing value.
Use the attribute mean (or majority nominal value) for all samples belonging to the same class.
Predict the missing value by using a learning algorithm: consider the attribute with the missing value as a dependent (class) variable and run a learning algorithm (usually Bayes or decision tree) to predict the missing value.
Identify outliers and smooth out noisy data:

Normalization/Standardization (Feature Scalling):
Scaling attribute values to fall within a specified range.
Example: to transform V in [min, max] to V' in [0,1], apply V'=(V-Min)/(Max-Min)
Scaling by using mean and standard deviation (useful when min and max are unknown or when there are outliers): V'=(V-Mean)/StDev
Aggregation: moving up in the concept hierarchy on numeric attributes.
Generalization: moving up in the concept hierarchy on nominal attributes.
Attribute construction: replacing or adding new attributes inferred by existing attributes.
