from xml.dom import minidom

strings_path = "./Strings.xaml"
common_strings_path = "./CommonStrings.xaml"

# Reading xaml files
print("Reading content...")
with open(strings_path, encoding="utf8") as f:
	strings_content = f.read()

with open(common_strings_path, encoding="utf8") as f:
	commmon_strings_content = f.read()
print("Extracted content.")



# Mapping xaml files
print("Mapping Strings.xaml to dictionary...")
xmldoc = minidom.parseString(strings_content)
tags = xmldoc.getElementsByTagName("clr:String")

strings_dictionary = { tags[i].attributes["x:Key"].value: tags[i].childNodes[0].nodeValue for i in range(0, len(tags) - 1, 1)}
print("Done, found strings:", len(strings_dictionary))

print("Mapping CommonStrings.xaml to dictionary...")
xmldoc = minidom.parseString(commmon_strings_content)
tags = xmldoc.getElementsByTagName("clr:String")

common_strings_dictionary = { tags[i].attributes["x:Key"].value: tags[i].childNodes[0].nodeValue for i in range(0, len(tags) - 1, 1)}
print("Done, found strings:", len(common_strings_dictionary))


# Comparing files
print("Getting differences between Strings.xaml and CommonStrings.xaml...")
key_differences_string_to_common_strings = list(set(strings_dictionary.keys()) - set(common_strings_dictionary.keys()))
print("Differences found: ", len(key_differences_string_to_common_strings))


print("Getting differences between CommonStrings.xaml and Strings.xaml...")
key_differences_common_string_to_strings = list(set(common_strings_dictionary.keys()) - set(strings_dictionary.keys()))
print("Differences found: ", len(key_differences_common_string_to_strings))



# Generating differences as dictionary
print("Generating xaml file for Strings.xaml not in CommonStrings.xaml...")

print("Finding missing strings...")
dictionary = {}

for key in key_differences_string_to_common_strings:
	dictionary[key] = strings_dictionary[key]

print("Missing strings count: ", len(dictionary))

# Generating xaml
print("Generating xaml...")

result = ""

root = minidom.Document()

for key, value in dictionary.items():
	node = root.createElement("clr:String")
	node.setAttribute('x:Key', key)

	textNode = root.createTextNode(value)
	node.appendChild(textNode)

	result += "\n"
	result += node.toxml()



# Generating file
print("Generating txt...")
f = open("result.txt", "w+")
f.write(result)
f.close()

print("All good, you will see your strings in current folder, in result.txt")
print("Byeee")

