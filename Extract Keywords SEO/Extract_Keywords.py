from rake_nltk import Rake
rake_nltk_var = Rake()
 
text = """Compatibility of systems of linear constraints
        over the set of natural numbers. Criteria of compatibility of a system
        of linear Diophantine equations, strict inequations, and nonstrict
        inequations are considered. Upper bounds for components of a minimal
        set of solutions and algorithms of construction of minimal generating
        sets of solutions for all types of systems are given. These criteria
        and the corresponding algorithms for constructing a minimal supporting
        set of solutions can be used in solving all the considered types of
        systems and systems of mixed types."""
    
rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
keyword_extracted_with_scores = rake_nltk_var.get_ranked_phrases_with_scores()

print("\n*******List of Keyword Extracted*******")
print(*keyword_extracted, sep = "\n") 
print("\n*******List of Keyword Extracted with Scores*******")
print(*keyword_extracted_with_scores, sep = "\n") 