
### Challenge 1 - Percy Replacement:
def percy_replacer(string_about_percy):
    return string_about_percy.replace('Percy', 'Ron')

### Challenge 2 - String Interpolation:
def weasley_invitation(name,day,date,month):
  return "The family of {name} Weasley proudly invite you to celebrate their graduation from Hogwarts on {day} the {date} of {month}. Festivities will be held at The Burrow. See you then!".format(name="Ron", day="Sunday", date="18", month="May")

### Challenge 3 - Seating Location
def seating_location(last_name):
    location = "middle section."
    if last_name[0] == "W":
        location = "front row."
    elif last_name[0] == "A":
        location = "rear section."
    elif last_name[0] == "B":
        location = "rear section."
    elif last_name[0] == "C":
        location = "rear section."
    elif last_name[0] == "D":
        location = "rear section."
    elif last_name[0] == "E":
        location = "rear section."
    elif last_name[0] == "F":
        location = "rear section."
    elif last_name[0] == "G":
        location = "rear section."
    return "You have a reserved seat in the {area}".format(area = location)

###Challenge 4 - All Together
def create_invitation(first_name, last_name, message):
    return "DEAR " + first_name.upper() + ",\n" + message + "\nP.S. " + seating_location(last_name)
