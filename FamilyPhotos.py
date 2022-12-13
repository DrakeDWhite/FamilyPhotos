from tkinter import *
import csv


# keywords, but we don't want repetition, so we'll weed them out as we're adding later
keywords = []

# people, but we don't want repetition, so we'll weed them out as we're adding later
people = []

# locations, but we don't want repetition, so we'll weed them out as we're adding later
locations = []

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
print(contents)


# class Application(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         self.grid()
#         self.create_widgets()


#     def create_widgets(self):
#         self.cost = 0
#         ## title and item
#         Label(self, text = "What would you like delivered? ").grid(row = 0,
#                                                                    column = 0)
#         self.item_entry = Entry(self, width = 50)
#         self.item_entry.grid(row = 0, column = 1, columnspan = 2,
#                               sticky = "W")
        

#         ## delivery options
#         self.delivery = StringVar()
#         self.delivery.set(None)

#         Label(self, text = "Options").grid(row = 1, column = 1)
        
#         Label(self, text = "Delivery Method:").grid(row = 2, column = 0)
        
#         self.drone = Radiobutton(self, text = "Flying Drone ($10)",
#                                  variable = self.delivery,
#                                  value = "flying drone")
#         self.drone.grid(row = 3, column = 0)
        
#         self.car = Radiobutton(self, text = "Self Driving Car ($20)",
#                                variable = self.delivery,
#                                value = "self-driving car")
#         self.car.grid(row = 4, column = 0)
        
#         self.robot = Radiobutton(self, text = "Giant Robot ($1000)",
#                                  variable = self.delivery,
#                                   value = "giant robot")
#         self.robot.grid(row = 5, column = 0)
        
        
#         ##addons

#         self.express_value = BooleanVar()
#         self.not_broken_value = BooleanVar()
#         self.smile_value = BooleanVar()
        
#         Label(self, text = "Addons:").grid(row = 2, column = 2)
#         self.express = Checkbutton(self, text = "Express Delivery (+$30)",
#                                    variable = self.express_value)
#         self.express.grid(row = 3, column = 2)
#         self.not_broken = Checkbutton(self, text = "Mostly Not Broken (+$20)",
#                                    variable = self.not_broken_value)
#         self.not_broken.grid(row = 4, column = 2)
#         self.smile = Checkbutton(self, text = "With a smile (+$1)",
#                                    variable = self.smile_value)
#         self.smile.grid(row = 5, column = 2)
        

#         ##bottom part

#         self.confirm = Button(self, text = "Confirm Delivery", command = self.deliver)
#         self.confirm.grid(row = 6, column = 1)

#         self.results_txt = Text(self, width = 60, height = 8, wrap = WORD)
#         self.results_txt.grid(row = 7, column = 0, columnspan = 3)
                                      