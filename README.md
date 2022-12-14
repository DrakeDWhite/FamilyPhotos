# What is this directory?

This is a final project for Information Organization and Retrieval at University of California, Berkeley. It is intended as the beginning phase of a personal project to digitize all family photos in the White-Fields family. It is also intended to serve as a starting point for building a search engine around faceted metadata and keyword search functionality on this collection.

# How do I run this repository?
1. Download the full directory onto a computer with Python installed.
    - See [the Python website](https://www.python.org/downloads/) to see how this is done. 
2. Run (double-click) FamilyPhotos.py
3. Fill out the search queries (detailed below) for the GUI that shows up. and at that, bish bash bosh, bobs your uncle. your results will open in your default browser window. 
    - *Ironically, I do have a distant Great Uncle Bob, but don't have any photos of him in this collection.*

# How does the search engine work?
![](https://i.imgur.com/K9MKvdr.png)

This is my humble GUI. It's relatively straightforward, but I'll cover each field here in detail.

**Keyword** - optional -  as of now, we only support a single keyword in this field. It can be any keyword you like, and you can hit the "See what keywords are available" button to see a comprehensive list of possible options. These are coded manually to each image.

**Person** - optional - a dropdown that displays all possible people in this collection. You can only choose one at a time.

**Place** - optional - a dropdown that displays all possible places where pictures in this collection have been taken. You can only choose one at a time.

**Decade** - optional - a dropdown that displays all possible decades encompassed by this collection. You can only choose one at a time.


Every filter can be filtered alone, or in tandem with any other of the filters. The program will tell you if there are no results or if what you tried doesn't work, so bash away at the program! and as the tooltext says at the bottom - you can leave all filters blank and see all images in this collection. 

# Write-up
## Why did I make this data collection? 
My family has *a lot* of physical photos. My dad especially, always had a camera and was taking pictures of the family. Once he passed, we had a lot of photos to deal with in his estate, and ended up hanging onto all of them. Nowadays, they take up pretty much an entire study at my mom's place, and as a lot of my family doesn't or hasn't ever had access to these photos, I wanted to put them somewhere for posterity so they wouldn't just collect dust.

In addition - my paternal side of the family has always been small, but after a few deaths in short time, there are essentially only two relatives left on that side (not including my immediate family). So - we'd like to have the photos organized in some cohesive structure to help reminisce, and so those members of the family can also see them.

## Why did I decide to organize them this way?
Well - they were physically organized in almost no way, despite for a vague recollection of chronological order, and even that was somewhat disorganized. There was some first in first out going on as well, seeing as there were literally stacks of photos. Some were on display, very few were in albums, and the vast majority were just tucked away in boxes with hundreds of other photos. 

## Technical specification
Each photo has quite a few pieces of metadata associated with it:
- A series of keywords associated with the photograph and its subjects 
- A series of individual people who are the subjects of each photograph
- One location datum, which is an approximation of a few key locations photos were taken in
- One decade datum, which is an approximation of what decade each photo was taken in. Many photos in our physical collection have indeterminate age, though I chose photos for this collection/project that were able to be identified to streamline the process.

## Search mechanisms
As you can see above, the database and collection supports keyword search, metadata filtering, faceted metadata filtering, and general browsing practices. The collection can support browsing as well as specific information needs and goals, and the myriad of metadata (which I plan to continue expanding, but since its currently manual it's a long process) allows for data foraging and berry-picking models of search. 

## Some limitations
This project has some obvious places for expansion, both in the techincal design as well as data organization. For the sake of the course, I wanted to keep it straightforward and focus my time on pieces that relate to the course. There are quite a few opportunities for improvment in the search process (such as the ability to select multiple people not currently being support, or being able to search for more than one keyword effectively). There are opportunities for NLP and SEO here as well. I plan to continue this project as a personal project, as this is a goal I've had for some time and this project was an excellent way to kickstart it. 

## Designed at scale
None of the variables in this project are static - so all content and options/dropdowns scale around the content within the `Family_key.csv` file. I can adjust keywords and metadata on the fly, and the program will adjust based on what we have input there.

In terms of runtime efficiency - that wasn't the focus at this stage of the project. This was intended as a proof of concept, using a default, rudimentary GUI system called `tkinter` from Python, and the main focus is around the organization and data associated with each image, as well as the tools available for the individual to search for items. 

# Concepts pulled from in class
Most are described throughout this write-up, but for ease of review for grading, here's a list of concepts used (potentially non comprehensive for later stages of this project)
- Models of the information seeking process - berry-picking, browsing, and the general search loop all play a practice here. Since the GUI stays up and can support repeated queries, it also supports dynamic berry-picking models.
- Metadata - this project was directly inspired by creating faceted metadata. Although the structure of the metadata is currently mostly flat in most aspects, it still has a few categories by which an image can be filtered on in different combinations.
- Keywords or tags - keyword searching was an important feature I wanted to include in this project. These keywords are manually generated by their creator (me), based on qualities of a particular image. The system currently only supports single keywords - but as outlined prior, a goal for the future is to include multiple words. I could have easily brute-forced multiple word keywords, but it seemed unneccessary to exhibit mastery of the concept. The keyword search can also be used as a catch-all, as all other metadata (location, people, decade, etc) are included in the possible keywords for each image for a majority of the collection. 