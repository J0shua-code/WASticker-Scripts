import os
# Download cwebp from https://storage.googleapis.com/downloads.webmproject.org/releases/webp/index.html
# Add cwebp to the environment path or paste the binaries in the root folder where the script is

files = os.listdir("input/")

for x in files:
	if ".png" not in x:
		pass
	else:
		query = 'cwebp input/' + x + ' -q 80 -o output/' + x[:-4] + '.webp'
		os.system(query)