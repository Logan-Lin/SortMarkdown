# Sort markdown files

## Introduce

This is just a tiny program that can sort Markdown files using header tags ('#')

For example, this format is what I used to take English notes:

    # Hard to remember words
    
    ### vigorous
    
    1. Vigorous physical activities involve using a lot of energy, usually to do short and repeated actions.
    2. A vigorous person does things with great energy and enthusiasm. A vigorous campaign or activity is done with great energy and enthusiasm.
    3. A vigorous person is strong and healthy and full of energy.
    
    > - Very vigorous exercise can increase the risk of heart attacks…
    > - African dance is vigorous, but full of subtlety.
    
    ### predominantly
    
    1. You use predominantly to indicate which feature or quality is most noticeable in a situation.
    
    > - His audience consists predominantly of groups of rugby-club revealers.
    > - Although it is predominantly a teenage problem, acne can occur in early childhood…
    
This program can sort these vocabularies based on its headers (start with `###`).
    
File structure before sorting:

    # ...
    
    ### vigorous
    
    vigorous block
    
    ### predominantly
    
    predominantely block
    
    ### debris
    
    debris block
    
File structure after sorting:

    # ...
    
    ### debris
    
    debris block
    
    ### predominantly
    
    predominantly block
    
    ### vigorous
    
    vigorous block

## Usage

You can use command line argument to indicate input, output file name and 
how many '#' your header tag have.. Standard format is like:

    python SortMarkdown.py --input <input_filename> --output <output_filename> --header 2

Default input filename is 'input', output filename is 'output', and header tag number is '3'.