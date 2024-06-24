import os

count = 0

dirroot= "C:/Archive/development/atria/atria/data1/page"


arr = os.listdir(dirroot)


kuttnerdoc = ""


for a in arr:
	kuttnerfile = open((dirroot + "/" + a),'r')
	textflag=0
	textflagb=3

	pagevalue = ""
	footnotevalue = ""

	count = count + 1
	if count > 5:
		exit()

	for line in kuttnerfile:
		if "structure {type:footnote;}" in line:
			textflag = 1
			#print ("activated - footnote")

		if "</TextRegion>" in line:
			textflag = 0
			#print ("deactivated")

		if textflag == 1:		
			if "<Unicode>" in line:
				#print(textflag, " ", count, ": ", line.strip())
				testline = line
				testline = testline.replace("<Unicode>", "")
				testline = testline.replace("</Unicode>", "")
				testline = testline.strip()
				footnotevalue = footnotevalue + " " + testline
				#print ("cleaned", testline)

		if "type:page-number" in line:
			textflagb = 2
			#print ("activated - number")

		if textflagb == 2:
			if "</TextEquiv>" in line:
				textflagb = 3
				#print ("deactivated - number")

		if textflagb == 2:		
			if "<Unicode>" in line:
				#print(textflag, " ", count, ": ", line.strip())
				testline = line
				testline = testline.replace("<Unicode>", "")
				testline = testline.replace("</Unicode>", "")
				testline = testline.strip()
				pagevalue = testline
				#print ("cleaned", testline)

	print (pagevalue, footnotevalue)