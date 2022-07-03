# Incident-Level Extract File
# Derived from 33601-Codebook.pdf

# structure
#  original column name
#  original column description
#  postgres column name
DB_COLS = [
    ["INCNUM", "INCIDENT NUMBER", 'incident_number'],
    ["INCDATE", "INCIDENT DATE", 'incident_date'],
    # BH1 - Batch Header 1
    ["B1007", "CITY NAME", 'city_name'],
    ["B1008", "STATE ABBREVIATION", 'state'],
    ["B1009", "POPULATION GROUP", 'pop_group'],
    # V2000s - Offense
    ["V20061", "UCR OFFENSE CODE - 1", 'ucr_offense_code'],
    ["V20071", "OFFENSE ATTEMPTED/COMPLETED - 1", 'offense'],
    ["V20081", "OFFENDER(S) SUSPECTED OF USING 1 - 1", 'offender_suspected_of_using1'],
    ["V20111", "LOCATION TYPE - 1", 'location_type'],
    ["V20121", "NUMBER OF PREMISES ENTERED - 1", 'num_premises_entered'],
    ["V20131", "METHOD OF ENTRY - 1", 'method_of_entry'],
    ["V20141", "TYPE OF CRIMINAL ACTIVITY 1 - 1", 'type_of_criminal_activity'],
    ["V20171", "TYPE WEAPON/FORCE INVOLVED 1 - 1", 'type of weapon_force_involved'],
    ["V20201", "BIAS MOTIVATION - 1", 'bias_motivation'],
    # Property
    ["V30121", "SUSPECTED DRUG TYPE 1 - 1", 'suspected_drug'],
    # Victim
    ["V40181", "AGE OF VICTIM - 1 135", 'age_victim'],
    ["V40191", "SEX OF VICTIM - 1 136", 'sex_victim'],
    ["V40201", "RACE OF VICTIM - 1 136", 'race_victim'],
    ["V40211", "ETHNICITY OF VICTIM - 1 137", 'ethcnity_victim'],
    ["V40221", "RESIDENT STATUS OF VICTIM - 1 137", 'residency_vicitm'],
    ["V40261", "TYPE INJURY 1 - 1", 'injury_type']
    ]
