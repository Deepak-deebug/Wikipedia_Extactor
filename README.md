
# Wikipedia_Extractor

A script (named **“wiki_extractor.py”**) that performs a Wikipedia search using the provided keyword, and returns urls of “n” related Wikipedia pages. The script should also extract one paragraph from each such page and return the result as a json file


## Getting Started
### Dependencies
    !pip install wikipedia
    !pip install json
### Executing program
#### Input Argument:
* keyword (string argument to define the query string)
* num_urls (integer argument for number of wikipedia pages to extract from)
* output (output json-file name)
#### Code Example  
    python wiki_extractor.py --keyword=”Indian Historical Events” --num_url=100 --output=”out.json” 
    
    
## Sources
https://wikipedia.readthedocs.io/en/latest/quickstart.html
