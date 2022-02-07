#!/usr/bin/python

#import Dependencies
import argparse
import wikipedia
import json 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--keyword", help="Enter the keyword to  search")
    parser.add_argument("--num_url", help="Numeber of page", type=int)
    parser.add_argument("--output",  help="file type.")

    # Parse arguments
    args = parser.parse_args()

    result=wikipedia.search(args.keyword,args.num_url)
    
    d=[]

    for i in result:
        try:
            re = wikipedia.page(i)
            di={'url':re.url,
                'content':wikipedia.summary(i) 
                }
            d.append(di)
        except wikipedia.exceptions.PageError:
            #print("Page error")
            continue
        except wikipedia.exceptions.DisambiguationError:
            #print("DisambiguationError error")
            continue
                            
    # Python program to write JSON        
    # Serializing json
    json_object = json.dumps(d, indent = 2)

    # Writing to sample.json
    with open(args.output, "w") as outfile:
        outfile.write(json_object)

   

