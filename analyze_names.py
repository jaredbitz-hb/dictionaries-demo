"""
analyze_names.py

Run this file in the interpreter (python3 -i analyze_names.py)
and then call any of the functions to demo them!
"""

def load_data(filename):
    """Load the rows of the CSV file [filename]"""
    result = []

    csv_file = open(filename)
    for row in csv_file:
        data = row.rstrip().split(',')
        # Tuples are more efficient than lists - less overhead
        data_tuple = tuple(data)
        result.append(data_tuple)
    csv_file.close()

    return result

def lookup_names_1910():
    """
    Builds a dictionary where you can look up the number of any baby born in 1910
    """
    names_ca = load_data('names_CA.csv') # Load all the rows of the CSV
    names_1910 = [row for row in names_ca if row[1] == '1910'] # Filter just the names from 1910

    # Build a dictionary where we can look up the count for each name
    names_dict = {}
    for row in names_1910:
        name = row[0]
        year = row[1]
        count = row[2]

        names_dict[name] = count

    # Let the user ask for different names over and over
    while True:
        name = input("Enter a name (type 'quit' to exit): ")
        if name == 'quit':
            break

        print(names_dict.get(name, 0))
        # The above code is equivalent to:
        # if name in names_dict:
        #   print(names_dict[name])
        # else:
        #   print(0)
    
def count_total_names():
    """
    Builds a dictionary where you can look up the total number
    of babies born with any name
    """
    names_ca = load_data('names_CA.csv') # Load all the rows of the CSV

    # Build a dictionary where we can look up the count for each name
    names_dict = {}
    for row in names_ca:
        name = row[0]
        year = row[1]
        count = row[2]

        # If the key 'name' is in the dict already, add this new count to it
        # Otherwise, names_dict.get() will return 0, so we're just setting the value to 'count'
        names_dict[name] = names_dict.get(name, 0) + int(count)

    # Let the user ask for different names over and over
    while True:
        name = input("Enter a name (type 'quit' to exit): ")
        if name == 'quit':
            break

        print(names_dict.get(name, 0))

def build_nested_dictionary():
    """
    Creates a set of nested dictionaries where you can look up the count
    for any name in any year, such as data['Thaddeus']['1998']
    """
    names_ca = load_data('names_CA.csv') # Load all the rows of the CSV

    # Build a dictionary where we can look up the count for each name
    data = {}
    for row in names_ca:
        name = row[0]
        year = row[1]
        count = row[2]

        # If we haven't seen this name yet, create an empty dict to hold
        # its counts
        if name not in data:
            data[name] = {}

        data[name][year] = count

    # Let the user ask for different names over and over
    while True:
        name = input("Enter a name (type 'quit' to exit): ")
        year = input("Enter a year: ")
        if name == 'quit':
            break

        print(data.get(name, {}).get(year, 0))
