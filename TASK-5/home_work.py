students_marks={
"anand":92,
"akhil":84,
"benison": 74,
"cenoy":64,
"hafeed": 55,
"jithin":42,
"nithin":28
}

subjects=["anand", "akhil", "benison", "cep",'hafeed','jithin','nithin']
marks=['A+','A','B+','B','C','D','F']
#zip()
mark_sheet=dict(zip(subjects,marks))
print(mark_sheet)

