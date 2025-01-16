Shark Attacks – README:

File Preparation:
Imorting Pandas Library
Import RE Module
Importing Shark Attacks CSV.file: url='https://www.sharkattackfile.net/spreadsheets/GSAF5.xls'

Data Cleaning:
- delete all rows with Null Values
- Dropping unnecessary columns: ‚Unnamed: 22', 'Unnamed: 21', 'original order', 'Case Number.1', 'href', 'href formula', 'pdf', 'Case Number'
- renaming column name „Species“ 
- renaming column name „Fatal Y/N“ into „Fatal“
- cleaning the „Type“ column: allow only 4 categories: „Watercraft“ = Watercraft + Boat, „Provoked“, „Unprovoked“, „Unverified“ =  Unverified + Unconfirmed + Invalid + Under investigation + Questionable + ?.
- cleaning the „Fatal“ column: allow only 2 categories: „True“ = 'Y', 'y', 'F', Y x 2' and „False“ = N', 'M', nan, 'n', 'Nq', 'UNKNOWN', 2017, ' N', 'N '.
- From "Species" column we only defined the cases with Tiger, Great White or Bull Shark attacks, all others marked as „others“.
- Creating a new dataframe for „Species“ column: White vs Tiger vs Bull sharks or „others“ using a map-function for the species.
- cleaning the „Time“ column: infer_datetime used
- creating a time dictionary with entries from „Time" column 
- For "Time" column we asked ChatGPT to interprete the manyfold differently formatted time values in a uniform style and replaced the "Time" column with it.
- Create a new Column with the „cleaned time“

Exploratory Data Analysis:
- Calculating the total attacks according to Species, calculating the fatal attacks  according to Species
- Grouping the cleaned time into 3 categories: "morning" 6:00 – 12:00, "afternoon" 12:01 – 18:00 & "night" 18:01 – 5:59.
- Creating a new pivoted table containing species and cleaned time




