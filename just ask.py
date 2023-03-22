import os
import csv
import openai
openai.api_key = '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'
model_engine = 'text-davinci-003'
print("\\\ ENTER WIHOUT TYPING ANYTHING TO EXIT FROM THE TERMINAL //")
print("\t \t \t \t \\\ ENJOY YOUR TIME HERE //")
for i in range(1,50):
	prompt = input(" \t \n Please enter your query : ")
	#if(prompt == "shutdown"):
  	#os.system("shutdown /s /t 1")
	if(len(prompt) >= 1):
		completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
		response = completion.choices[0].text 
		print(response)
		with open('INPUT.txt', 'a') as f:
			f.write("\t  INPUT QUERY : ")
		with open('INPUT.txt', 'a') as f:
			f.write(prompt) 
		with open('OUTPUT.txt', 'a') as f:
			f.write(response)
	else:
		print('\t')
		print("Sorry to see you go -) ")
		print('\t')
		break
exit()	
				
