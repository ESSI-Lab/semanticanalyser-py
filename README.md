# semanticanalyser-py
A lightweight Python client for the BODC Semantic Analyser API. It helps you discover controlled vocabularies, explore categories, match types and properties, and run term analysis to resolve terms to canonical concepts (with codes and URIs) across BODC vocabularies.

## Key features
- Retrieve semantic categories available from the BODC service
- List vocabularies within a category
- Discover supported match types and match properties
- Analyse free-text terms and obtain matched concepts, codes, and vocabularies
- Simple, Pythonic API with minimal dependencies

## Installation
``` bash
pip install semanticanalyser-py
```
## Quick start
``` python
# Basic usage example
from analyser import SemanticAnalyzer, Matchtype, MatchProperty

analyser = SemanticAnalyzer()  # uses the public BODC endpoint by default

# Explore categories
categories = analyser.get_categories()
print("Categories:", categories)

# Choose a category (e.g., first one) and list vocabularies
if categories:
    cat_code = categories[0]["termCode"]
    vocabs = analyser.get_vocabularies(cat_code)
    for v in vocabs:
        print(v)

# Discover matching options
match_types = analyser.getMatchTypes()         # e.g., ["exact", "broad", ...]
match_props = analyser.getMatchProperties()    # e.g., ["prefLabel", "altLabel", ...]

# Prepare the query
terms = ["dissolved oxygen", "chlorophyll a"]

# Optionally filter or construct match types/properties
# (example below demonstrates using them as returned)
analysis = analyser.analyzeTerms(
    terms=terms,
    matchTypes=match_types,
    matchProperties=match_props
)

if analysis:
    for m in analysis.get_matches():
        print(
            m.getMatchingTerm(),
            m.getMatchProperty(),
            m.getMatchType(),
            m.getTermCode(),
            m.getVocabulary(),
            m.getConceptURI(),
        )
```
## When to use this library
- You need to map free-text terms to standardised BODC concepts and codes
- You want to build tools that browse or integrate with BODC controlled vocabularies
- You’re enriching datasets with semantic metadata (URIs, codes, vocabularies)

## Configuration
- Endpoint: By default, the client targets the public BODC Semantic Analyser API. You can override the endpoint:
``` python
  from analyser import SemanticAnalyzer
  analyser = SemanticAnalyzer(endpoint="https://semantics.bodc.ac.uk/api")
```
## Requirements
- Python: 3.8 or newer
- Dependencies: requests

## Roadmap ideas
- Robust pagination and retry logic
- Additional helpers for filtering results
- CLI utilities
- Async support

## Contributing
Issues and pull requests are welcome. Please:
- Keep changes small and well-documented
- Include tests where practical
- Follow conventional commit messages where possible

## License
