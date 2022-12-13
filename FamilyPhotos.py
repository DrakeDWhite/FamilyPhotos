from tkinter import *
from tkinter import ttk
import csv
import webbrowser


# keywords, but we don't want repetition, so we'll weed them out as we're adding later
keywords = []

# people, but we don't want repetition, so we'll weed them out as we're adding later
people = ['']

# locations, but we don't want repetition, so we'll weed them out as we're adding later
locations = ['']

# decades, but we don't want repetition
decades = ['']

# open the file
with open("Files/Family_key.csv", newline='') as csvfile:
    # split each row
    filereader = csv.reader(csvfile, delimiter=',')

    # make it a list of lists
    contents = list(filereader)

# compile various lists
for i in range(1, len(contents)):

    # turning keywords and people into lists so we can search on them better later
    contents[i][2] = contents[i][2].lower().split(', ')
    contents[i][3] = contents[i][3].lower().split(', ')

    # compile unique keyword list
    for each in (contents[i][2]):
        if str(each).lower() not in keywords:
            keywords.append(str(each).lower())

    # compile unique people list
    for each in (contents[i][3]):
        if str(each) not in people:
            people.append(str(each))

    # compile locations
    if contents[i][4] not in locations:
        locations.append(contents[i][4])

    # compile contents
    if contents[i][5] not in decades:
        decades.append(contents[i][5])

# get our variables for the various data so we can plug them into widgets later
keywords = sorted(keywords)
people = sorted(people)
locations = sorted(locations)
decades = sorted(decades)


# initialize application
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    # start widgets
    def create_widgets(self):  

        ## keyword search
        Label(self, text = "Single keyword (optional):",  font = ('arial', 12)).pack(pady = 5)
        self.item_entry = Entry(self, width = 50)
        self.item_entry.pack(pady = 5, padx = 20)

        # people dropdown
        Label(self, text = "Pick a person (leave blank for none):",  font = ('arial', 12)).pack(pady = 5)
        self.people_options = ttk.Combobox(self)
        self.people_options['values'] = people
        self.people_options['state'] = 'readonly'
        self.people_options.pack()

        # location dropdown
        Label(self, text = "Pick a place (leave blank for none):",  font = ('arial', 12)).pack(pady = 5)
        self.location_options = ttk.Combobox(self)
        self.location_options['values'] = locations
        self.location_options['state'] = 'readonly'
        self.location_options.pack()

        # decade dropdown
        Label(self, text = "Pick a decade (leave blank for none):",  font = ('arial', 12)).pack(pady = 5)
        self.decade_options = ttk.Combobox(self)
        self.decade_options['values'] = decades
        self.decade_options['state'] = 'readonly'
        self.decade_options.pack()

        # submit button
        self.submitBtn = Button(self, text = "Go!", command = self.generate_photos)
        self.submitBtn.pack(pady = 10)

        # the output box, where we'll put all our messages or link to the html page
        self.output_box = Text(self, height = 5, width = 40, state="disabled", wrap=WORD)
        self.output_box.pack() 



    def generate_photos(self):
        # lists for generation
        # these are tiered because the filters are cumulative - so each step of the way. And each entry by the user whittles down our options a bit more

        # could be more efficient, but, /shrug
        self.tier1_list = []
        self.tier2_list = []
        self.tier3_list = []
        self.final_list = []

        # have to enabled and disable textbox to change value
        # clearing it just in case there's anything left over from a previous run
        self.output_box['state'] = "normal"
        self.output_box.delete("1.0", END)
        self.output_box['state'] = "disabled"

        ##########
        ### STEP 1 - keyword filter
        ##########

        # is keyword empty or more than one word?
        if (self.item_entry.get()) and (" " not in self.item_entry.get()):
            # if not, check the third column in each row to see if the user's keyword entry appears there
            for each in contents:
                if self.item_entry.get().lower() in each[2]:
                    # if it is, add the whole item to the tier1 list
                    self.tier1_list.append(each)
            # for each in self.tier1_list:
            #     print(each)
            #     print("\n")
            # print("\n\n")
        # check if they have more than one word
        elif " " in self.item_entry.get():
            # if they do, give them a message saying so
            self.output_box['state'] = "normal"
            self.output_box.insert(END, "Your keyword can only be one word! We'll ignore that field for now.\n")
            self.output_box['state'] = "disabled"
        # otherwise, just dump all of contents into tier 1 list for the next stage
        else:
            self.tier1_list = contents

        ##########
        ### STEP 2 - People filter
        ##########

        # see if they entered anything
        if self.people_options.get():
            # if they did, filter everything we filtered out from keyword search
            for each in self.tier1_list:
                if self.people_options.get() in each[3]:
                    self.tier2_list.append(each)
            # for each in self.tier2_list:
            #     print(each)
            # print()
            # print()
        # if they didn't enter anything for the people filter, just set tier2 list equal to tier1
        else:
            self.tier2_list = self.tier1_list

        ##########
        ### STEP 3 - Location Filter
        ##########

        # check to make sure they selected something
        if self.location_options.get():
            # check for it if so
            for each in self.tier2_list:
                if self.location_options.get() == each[4]:
                    self.tier3_list.append(each)
        # if they didn't select anything for this filter, do no filtering
        else:
            self.tier3_list = self.tier2_list


        ##########
        ### STEP 4 - Decade Filter
        ##########

        # check to make sure they selected something
        if self.decade_options.get():
            # check for it if so
            for each in self.tier3_list:
                if str(self.decade_options.get()) == str(each[5]):
                    self.final_list.append(each)
        # if they didn't select anything for this filter, do no filtering
        else:
            self.final_list = self.tier3_list

        # start on the html
        html = '''
        <html>
            <head>
                <title> Search Results </title>
            </head>
            <body>
                <h1> White-Family Photo Results</h1>
        '''

        # make sure we have some items in the final_list
        # if we don't, no reason to write to a page. Just tell them it's empty.
        if len(self.final_list) == 0:
            self.output_box['state'] = "normal"
            self.output_box.insert(END, "Your search returned no results. Try again!")
            self.output_box['state'] = "disabled"
        else:
            for each in self.final_list:
                html += '''
                <p>
                    <img src ="{0}" width = "500">
                </p>
                <p>
                {1}
                </p>
                <br>
                '''.format(each[1], each[6])
        
            html_out = open("final_results.html", "w")
            html_out.write(html)
            html_out.close()

            webbrowser.open("final_results.html", new=2)


### MAIN                                      
root = Tk()
root.title("White-Fields Family Photo Search")
root.geometry("345x800")
app = Application(root)
root.mainloop()
 