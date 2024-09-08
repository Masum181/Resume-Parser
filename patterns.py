


phone_num_patterns = [
    [{'ORTH': "("}, {"SHAPE": "ddd"}, {"ORTH": ")"}, {"SHAPE": "ddd"}, {"ORTH": "-"}, {"SHAPE": "dddd"}], # (123) 456-7890
    [{"TEXT": "+880"}, {"IS_SPACE": True, 'OP':"?"}, {"SHAPE": 'dddd'}, {"ORTH": "-", "OP": '?'}, {"SHAPE": 'dddd', 'LENGTH': 6}], # +880 1738-276219
    [{"SHAPE": 'dddd', 'LENGTH': 5}, {"ORTH": "-", "OP": "?"}, {"SHAPE": 'dddd', 'LENGTH': 6}], # 01738-276219
    [{"SHAPE": 'dddd', 'LENGTH': 11}],
]

# name_pattern = [
#                 [{"POS": "PROPN"}, {"POS": "PROPN"}],
#                 [{"POS": "PROPN"}, {"POS": "PROPN"}, {"POS": "PROPN"}]]

name_pattern = [[{"TEXT": {"REGEX": r"^(Dr|Mr|Mrs|Prof|Rev|Hon|Sir|Dame|Md)\.?$"}, 'OP':"?"}, {"POS": "PROPN"}, {"POS": "PROPN"}, {"POS": 'PROPN', "OP": "*"}]]

# name_pattern = [[
#         {"TEXT": {"REGEX": r"^(Dr|Mr|Mrs|Prof|Rev|Hon|Sir|Dame)\.?$"}, 'OP':"?"}, # optional title
#         {'IS_TITLE': True, 'POS': 'PROPN'}, # First name must be a proper noun
#         {"IS_TITLE": True, 'POS': 'PROPN', 'OP': '?'}, # optional middle name
#         {'IS_PUNCT': True, 'OP': '?'}, # optional punctuation
#         {"IS_TITLE": True, "POS": 'PROPN'},
#         {'TEXT': '-', 'OP': '?'},
#         {'IS_TITLE': True, 'POS':'PROPN', 'OP':'?'},
#         {'TEXT': {'REGEX': r'^(Jr|Sr)$'},'OP': '?'},
#         {"TEXT": {"REGEX": {"NOT_IN": ["LTD", "Inc", "Corp"]}}}
#     ]]

email_pattern = [
    [{"LIKE_EMAIL": True}]
]

url_pattern = [
    [{'LIKE_URL': True}]
]

degree_pattern = [
    [{"LOWER": "bsc"}, {'IS_TITLE': True}],
    [{"LOWER": "bachelor"}, {"LOWER": "of"}, {"IS_TITLE": True}],  # Bachelor of Science, Bachelor of Arts, etc.
    [{"LOWER": "master"}, {"LOWER": "of"}, {"IS_TITLE": True}],    # Master of Science, Master of Arts, etc.
    [{"LOWER": "bachelor's"}, {"LOWER": "degree"}],                # Bachelor's Degree
    [{"LOWER": "master's"}, {"LOWER": "degree"}],                  # Master's Degree
    [{"LOWER": "phd"}],                                            # Ph.D.
    [{"LOWER": "doctor"}, {"LOWER": "of"}, {"LOWER": "philosophy"}],  # Doctor of Philosophy
    [{"LOWER": "doctorate"}, {"LOWER": "in"}, {"IS_TITLE": True}], # Doctorate in Computer Science, etc.
    [{"LOWER": "associate"}, {"LOWER": "degree"}, {"LOWER": "in"}, {"IS_TITLE": True}],  # Associate Degree in XYZ
    [{"LOWER": "associate"}, {"LOWER": "of"}, {"IS_TITLE": True}], # Associate of Science, Associate of Arts, etc.
    [{'TEXT': 'B. Sc.'}, {"LOWER": 'in'}, {'IS_TITLE': True}]
]
cse_pattern = [{'LOWER': {"IN": ['b.', 'bsc', 'bachelor', 'bachelors', 'BSC']}},
           {'POS': 'ADP', 'OP': "?"},
           {'LOWER': {'IN': ['sc', 'science', 'degree']}, 'OP': "?"},
           {'IS_PUNCT': True, 'OP': '?'},
              {'POS': 'ADP'},
              {'LOWER':'computer'},
               {'LOWER': 'science'},
               {'TEXT': {'IN': ['and', 'And', 'AND', '&']}},
               {'LOWER': 'engineering'}
              ]
eee_pattern_and_other = [{'LOWER': {"IN": ['b.', 'bsc', 'bachelor', 'bachelors', 'BSC']}},
           {'POS': 'ADP', 'OP': "?"},
           {'LOWER': {'IN': ['sc', 'science', 'degree']}, 'OP': "?"},
           {'IS_PUNCT': True, 'OP': '?'},
            {'POS': 'ADP'},
            {'IS_TITLE': True},
            {'TEXT': {'IN': ['and', 'And', 'AND', '&']}},
                {'LOWER': 'electronics'},
            {'IS_TITLE': True}
              ]

other_engineering = [{'LOWER': {"IN": ['b.', 'bsc', 'bachelor', 'bachelors', 'BSC']}},
           {'POS': 'ADP', 'OP': "?"},
           {'LOWER': {'IN': ['sc', 'science', 'degree']}, 'OP': "?"},
           {'IS_PUNCT': True, 'OP': '?'},
            {'POS': 'ADP'},
            {'IS_TITLE': True},
            {'IS_TITLE': True}
              ]

diploma_pattern = [
        {'LOWER': 'diploma'},
        {'LOWER': 'in'},
        {'LOWER': 'engineering'}
    ]

degree_pattern.extend([cse_pattern, eee_pattern_and_other, other_engineering, diploma_pattern])

experience_pattern = [
    [{'IS_DIGIT': True}, {'LOWER': 'years'}, {'LOWER': 'of'}, {"LOWER": 'experience'}, {'LOWER': 'in'}, {'IS_TITLE': True, 'OP': '+'}], # x years of experience in [field]
    [{'IS_DIGIT': True},{'ORTH': '+'}, {'LOWER': 'years'}, {'LOWER': 'of'}, {"LOWER": 'experience'}, {'LOWER': 'in'}, {'IS_TITLE': True, 'OP': '+'}],  # x+ years of experience in [field]
    [{"LOWER": "over"},{'IS_DIGIT': True}, {'LOWER': 'years'}, {'LOWER': 'of'}, {"LOWER": 'experience'}, {'LOWER': 'in'}, {'IS_TITLE': True, 'OP': '+'}], # over x years of experience in [field]
    [{'IS_DIGIT':True}, {'LOWER': 'years'}, {'LOWER': 'in'}, {'IS_TITLE': True, 'OP': '+'}], # X years in field
    [{'IS_DIGIT':True},{"ORTH": "+"},{'LOWER': 'years'}, {'LOWER': 'in'}, {'IS_TITLE': True, 'OP': '+'}], # x+ years in filed
    [{'LOWER': 'more'}, {'LOWER': 'than'}, {"IS_DIGIT": True}, {'LOWER': 'years'}, {"LOWER": 'in'}, {"IS_TITLE": True, 'OP': '+'}] # More than x years in field
]

