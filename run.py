import requests
import random
import threading
from concurrent.futures import ThreadPoolExecutor

threading = ThreadPoolExecutor(max_workers=int(100000))

def attack():
	token = input('TOKEN : ')
	body = input('MESSAGE : ')
	count = int(input('COUNT : '))
	print()
	
	Ready(token,body,count)
	
	# Working...
	
	
def attack_lines(token, body):
	string = ['[+]','[*]','[-]','[?]']
	all_random = ''.join(random.choice(string))
	res = requests.post('https://notify-api.line.me/api/notify',headers={'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token},data={'message': body})
	if res.status_code == 200:
		print(f'{all_random} ATTACK | STATS 200 OK')
	else:
		print(f'{all_random} ERROR !!')

def Ready(token, body, count):
	for _ in range(int(count)):
		threading.submit(attack_lines, token, body)
		

attack()

# end












# Coding GENIX SHOP