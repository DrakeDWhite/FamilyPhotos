from tkinter import *
from tkinter import ttk
import csv


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
    #for row in filereader:
        # separate each item in each row
        # for i in range(len(row)):
            # print them, for tracing
            # print(row[i])

        #print("\n\n")
    contents = list(filereader)

# compile various lists
for i in range(1, len(contents)):
    # compile unique keyword list
    contents[i][2] = contents[i][2].split(', ')
    for each in (contents[i][2]):
        if str(each).lower() not in keywords:
            keywords.append(str(each).lower())
    # compile unique people list
    for each in (contents[i][3]).split(", "):
        if str(each) not in people:
            people.append(str(each))
    # compile locations
    if contents[i][4] not in locations:
        locations.append(contents[i][4])
    # compile contents
    if contents[i][5] not in decades:
        decades.append(contents[i][5])


keywords = sorted(keywords)
people = sorted(people)
locations = sorted(locations)
decades = sorted(decades)

# tracing
# for each in contents:
#     print(each[2])
#print("Keywords:", keywords)
#print("People: ", people)
#print(len(people))
#print("Locations:", locations)
#print("Decades:", decades)

# initialize application
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):  
        # start variables
        # the person filter
        self.person_filter = ""
        # will determine how many rows of people we have buttons (columns = 4)
        person_rows = len(people) // 4
        # the location
        self.location_filter = ""
        # the decade
        self.decade_filter = ""
        # keyword search 
        self.search_term = ''

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
        submitBtn = Button(self, text = "Go!", command = self.generate_photos)
        submitBtn.pack(pady = 10)

        output_box = Text(self, height = 3, width = 40, state = 'disabled')
        output_box.pack() 

        # lists for generation
        self.tier1_list = []
        self.tier2_list = []
        self.tier3_list = []
        self.tier4_list = []

    def generate_photos(self):
        if (self.item_entry.get()) and (" " not in self.item_entry.get()):
            for each in contents:
                if self.item_entry.get() in each[2]:
                    print(each)
                    self.tier1_list.append(each)
            print(self.tier1_list)
        else:
            print("no!")


                                      
root = Tk()
root.title("White-Fields Family Photo Search")
root.geometry("345x800")
app = Application(root)
root.mainloop()
 