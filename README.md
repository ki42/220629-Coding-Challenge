# 220629-Coding-Challenge

Psudo code:

Get this:
https://en.wikipedia.org/wiki/List_of_programming_languages

Scrape this page and extract all the links to individual programming languages from it,
-They aren't the first links... find out the section they start in. 

**** Store the HTML... in memory or in a file structure?

If object, two fields: URL and HTML
If file structure, set the file name to the URL save the HTML (can the file name be that long?  <260, Is there a meta field I can put it in?)

For each the HTML files or objects,

get from the infobox:

 paradigm,
 first appeared,
 and file extensions.
 
 **** Does the user want them as a single field or broken apart in to sub seprates, each file extension separate? (CSV = Problem, they are comma separated already)
 
If all three not null then

Also get:

Name: the name of the language (from the URL is fine) 
   Helper function to parse name from URL (or better location)
( Then I would put into the output file :- the three values from the infobox
**** Do we need to know it came from the info box? If yes, subsection it in JSON, if we don't care... 
     Infobox     (Sub if needed - can't in CSV) 
	       paradigm:
		     first appears:
	       file extentions:	)
Header sections count: (underline separator count) return number (One counter function with varibles in or two counter functions...)
Inside the article section count <url> tags return number Section Count: 

add it to a structured output file (JSON, CSV) - If CSV - create readme for field names

Else
Do nothing

exit loop

Close file, if needed

