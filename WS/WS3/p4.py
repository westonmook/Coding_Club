#Advanced strings
favphrase = "Keep it simple stupid! Occam's Razor"
nfavphrase = favphrase.replace(" ", "_")
print(nfavphrase)
nfp_upper = nfavphrase.upper()
print(nfp_upper)
print("Starts with vowel:", nfp_upper[0] in "AEIOU")
