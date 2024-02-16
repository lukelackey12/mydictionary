"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
import json

with open('school_data.json', 'r') as infile:
    list_of_schools = json.load(infile)

# Define the conference numbers for ACC, Big 12, Big Ten, and SEC
conference_numbers = {372, 108, 107, 130}

print("\nSchools with a graduation rate for Women over 75%:")
print()
for school in list_of_schools:
    # Check if the school's conference number is in the specified set
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference_numbers:
        graduation_rate_women = school["Graduation rate  women (DRVGR2020)"]
        if int(graduation_rate_women) > 75:
            print(f"University: {school['instnm']}")
            print(f"Graduation rate for Women: {graduation_rate_women}%")
            print()

print("\nSchools with a total price for in-state students living off campus over $50,000:")
print()
for school in list_of_schools:
    # Check if the school's conference number is in the specified set
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference_numbers:
        total_price_off_campus = school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
        if total_price_off_campus is not None and total_price_off_campus > 50000:
            print(f"University: {school['instnm']}")
            print(f"Total price for in-state students living off-campus: ${total_price_off_campus:,.2f}")
            print()
