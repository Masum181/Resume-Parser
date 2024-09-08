import spacy
from spacy.matcher import Matcher
import patterns




nlp = spacy.load("en_core_web_md")
skill_pattern_path = "jz_skill_patterns.jsonl"


ruler = nlp.add_pipe("entity_ruler")
ruler.from_disk(skill_pattern_path)

name_nlp = spacy.blank("en")
ruler  = name_nlp.add_pipe("entity_ruler")
ruler.from_disk("job_title.jsonl")

# phone_num_pattern = r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}|\d{5}[-\.\s]??\d{6}))"

# phone_num_pattern = [{"label": "PHONE_NUMBER", "pattern": [{"TEXT": {"REGEX": phone_num_pattern}}]}]


def find_substring(texts: list):
    output_text = []
    for index, text in enumerate(texts):
        new_array = texts.copy()
        new_array.pop(index)
        for arr in new_array:
            if text in arr:
                output_text.append(arr)
    return list(set(output_text))

def extra_filtering(texts):
    output = []
    for text in texts:
        t = text.lower()
        if 'ltd' in t or 'corp' in t or "inc" in t or 'zone' in t or "technology" in t or 'institute' in t:
            continue
        output.append(text)


    new_text = nlp(" . ".join(output))
    output = []
    for t in new_text.ents:
        if t.label_ == "GPE" or t.label_ == "ORG":
            continue
        output.append(t.text)
    
    return output


def get_skills(doc):
    skills = []
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            skills.append(ent.text)
    
    
    return list(set(skills))

def get_name(doc):
    matcher = Matcher(nlp.vocab)
    matcher.add("NAME", patterns.name_pattern)

    names = []
    for match_id, start, end in matcher(doc):
        names.append(doc[start:end].text)

    text = " || ".join(names)
    name_doc = name_nlp(text)

    filter_text = []
    for ent in name_doc.ents:
        filter_text.append(ent.text.strip())
    final_name = []
    for name in names:
        if name not in filter_text:
            final_name.append(name)
    
    filter_text = find_substring(final_name)
    # new_text = nlp(" | ".join(filter_text))
    # print(new_text)
    # filter_text = []
    # for t in new_text.ents:
    #     if t.label_ == "GPE":
    #         print(t.text)
    #         continue
    #     filter_text.append(t.text)

    return extra_filtering(filter_text)


def get_mobile_num(doc):
    matcher = Matcher(nlp.vocab)
    matcher.add("PHONE_NUMBER", patterns.phone_num_patterns)
    mobile_num = []
    for match_id, start, end in matcher(doc):
        mobile_num.append(doc[start:end].text)
    return list(set(mobile_num))

def get_email_address(doc):
    matcher = Matcher(nlp.vocab)
    matcher.add("EMAIL", patterns.email_pattern)
    emails = []
    for match_id, start, end in matcher(doc):
        emails.append(doc[start:end].text)
    return list(set(emails))


def previous_work(text):
    matcher = Matcher(nlp.vocab)

    pass

def extracting_education(doc):
    matcher = Matcher(nlp.vocab)
    matcher.add("DEGREE", patterns.degree_pattern)

    degrees = []
    for match_id, start, end in matcher(doc):
        degrees.append(doc[start:end].text)
    return list(set(degrees))

def get_experience(doc):
    matcher = Matcher(nlp.vocab)
    matcher.add("EXPERIENCE", patterns.experience_pattern)
    
    experience = []
    for match_id, start, end in matcher(doc):
        experience.append(doc[start:end].text)
    return experience

def get_url(doc):
    matcher = Matcher(nlp.vocab)
    matcher.add("URL", patterns.url_pattern)

    urls = []
    for match_id, start, end in matcher(doc):
        urls.append(doc[start:end].text)
    return urls



