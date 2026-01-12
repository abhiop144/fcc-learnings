import re 
"""
The re module in Python provides support for regular expressions (regex).
This library is used for complex string manipulation tasks such as searching, 
validating input, and extracting or replacing specific patterns within text.
"""

# Sample dataset representing patient records to be validated
medical_records = [ 
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    """
    Checks individual field values against specific business rules.
    Returns a list of keys that failed validation.
    """
    constraints = {
        # patient_id: must be a string starting with 'p' followed by one or more digits
        # re.IGNORECASE allows 'P' or 'p'
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\d+', patient_id, re.IGNORECASE), 
        
        # age: must be an integer and at least 18
        'age': isinstance(age, int) and age >= 18,
        
        # gender: must be a string and either 'male' or 'female'
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        
        # diagnosis: must be a string or None (empty)
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        
        # medications: must be a list containing only strings
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        
        # last_visit_id: must be a string starting with 'v' followed by digits
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE) 
    }

    # Return only the keys where the value (the check) was False
    return [key for key, value in constraints.items() if not value]


def validate(data):
    """
    Main validation function that iterates through the dataset.
    Checks for structural errors (types/keys) and content errors (values).
    """
    # Check if the overall data is a list or tuple
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False
    # The set of keys that every record MUST have
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    # Loop through each record with its index for error reporting
    for index, dictionary in enumerate(data):
        
        # Ensure the record is actually a dictionary
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        # Ensure the dictionary has the exact keys required (no more, no less)
        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        # Check the values within the dictionary using the constraints function
        # **dictionary "unpacks" the dict into the function arguments
        invalid_records = find_invalid_records(**dictionary)
        
        # Report specific field errors found by find_invalid_records
        for key in invalid_records:
            print(
                f"Unexpected format '{key}: {dictionary.get(key)}' at position {index}."
            )
            is_invalid = True
            
    # Final verdict
    if is_invalid:
        return False
    
    print('Valid format.')
    return True

# Run the validation
validate(medical_records)
