'''river = {
    "nile": "egypt",
    "yamaxun": "baxi",
    "yangzi": "china",
    "mixixibi": "milu"
}
for river_name in river.keys():
    print(river_name)
for river_country in river.values():
    print(river_country)
for river_name, river_country in river.items():
    print("the " + river_name + " runs through "+river_country)
'''
# favorite_languages = {"jen": "python", "sarah": "c",
#                      "edward": "ruby", "phil": "python"}
favorite_languages = {}
favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"
print(favorite_languages)
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    if name in friends:
        print("thank you "+name)
    else:
        print(name+" please join us")
