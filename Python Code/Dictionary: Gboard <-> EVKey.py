working =r"""
#input here
"""

def program(working):

	gboard_format = "# Gboard Dictionary version:1"
	EVKey_format = "<<Đây là dòng làm dấu Unicode, không được sửa hoặc xoá dòng này>>"

	if "# Gboard Dictionary version:1" in working:
		final = working.replace(gboard_format,EVKey_format).replace("	\n","\n").replace("	","||")
	elif "<<Đây là dòng làm dấu Unicode, không được sửa hoặc xoá dòng này>>" in working:
		final = working.replace(EVKey_format,gboard_format).replace("\n","	\n").replace("||","	")
	else:
		final = "Không hợp lệ!"
	print(final)

program(working)
