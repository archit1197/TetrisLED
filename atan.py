import time
import os
import random
import signal
import sys
import pygame

board_x=8
board_y=8

matrix=[[0 for i in range(0,board_x)] for j in range(0,board_y)]
matrix_2=[[0 for i in range(0,board_x)] for j in range(0,board_y)]
dead_list=[]				#it will store all those passive objects which are now at the bottom, can't be moved further. 
height=[board_x for i in range(board_y)]
	
"""
for i in range(0,8):
	matrix[i][0]=1
	if i!=0:
		matrix[i-1][0]=0
	os.system('clear')
	for j in range(0,8):
		print matrix[j]
	time.sleep(2)
"""
def print_matrix(matri):
	matrix_2=matri
	matrix=[[0 for i in range(0,board_x)] for j in range(0,board_y)]
	setp(matrix,thing)
	for i in range(board_x):
		print matrix[i]
	print "--------"
	

def setp(matrix,object):
	
	try:
		for i in range(len(object.listpoints)):
			if object.listpoints[i][0]<board_x and object.listpoints[i][1]<board_y:
				matrix[object.listpoints[i][0]][object.listpoints[i][1]]=1	

		for j in range(board_y):
			if (height[j]<board_x):
				for k in range(height[j],board_x):
					for i in dead_list:
						if i.check(k,j)==1:
							matrix[k][j]=1
	except:
		abcd=0
	return


class piece:
	def __init__(self,shape,listpoints,orientation):
		self.shape=shape
		self.listpoints=listpoints
		self.orientation=orientation


	def left(self):

		for i in range(0,len(self.listpoints)):
			if self.listpoints[i][1]==0:
				return False	
		for i in range(0,len(self.listpoints)):	
			if((height[self.listpoints[i][1]-1])==self.listpoints[i][0]):
				return False

		for i in range(0,len(self.listpoints)):
			self.listpoints[i][1]-=1
		return True


	def right(self):
		for i in range(0,len(self.listpoints)):
			if self.listpoints[i][1]==board_y-1:
				return False
		for i in range(0,len(self.listpoints)):	
			if((height[self.listpoints[i][1]+1])==self.listpoints[i][0]):
				return False		
		for i in range(0,len(self.listpoints)):
			self.listpoints[i][1]+=1
		return True

	def down(self):
		flag=1
				
		for i in range(0,len(self.listpoints)):	
			if((height[self.listpoints[i][1]])==self.listpoints[i][0]+1):
				flag=0
				
						
		
		
		if (flag==0):
			for i in range(0,len(self.listpoints)):
				y=self.listpoints[i][1]
				minval=height[y]
				for j in range(0,len(self.listpoints)):
					if self.listpoints[j][1]==y:
						minval=min(minval,self.listpoints[j][0])
				height[y]=minval
			matrix_2=matrix
			return False	

		for i in range(0,len(self.listpoints)):
			self.listpoints[i][0]+=1	
		return True
		
	def check(self,i,j):
		ch=0
		for k in range(len(self.listpoints)):
			if self.listpoints[k][0]==i and self.listpoints[k][1]==j:
				ch=1
		return ch 
	
	def rotate(self):
		if self.shape=='l':
			if(self.orientation%4==0):
				if (self.listpoints[2][0]+1<board_x and self.listpoints[2][1]-1>-1 and self.listpoints[0][0]-1>-1 and self.listpoints[0][1]+1<board_y):
					if(matrix[self.listpoints[2][0]+1][self.listpoints[2][1]-1]==0 and matrix[self.listpoints[0][0]-1][self.listpoints[0][1]+1]==0):
						self.listpoints[2][0]+=1
						self.listpoints[2][1]-=1
						self.listpoints[0][0]-=1
						self.listpoints[0][1]+=1
					else:
						return False
				else:
					return False

			elif(self.orientation%4==1):
				if (self.listpoints[2][0]-1>-1 and self.listpoints[2][1]+1<board_y and self.listpoints[0][0]+1<board_x and self.listpoints[0][1]-1>-1):
					if(matrix[self.listpoints[2][0]-1][self.listpoints[2][1]+1]==0 and matrix[self.listpoints[0][0]+1][self.listpoints[0][1]-1]==0):
						self.listpoints[2][0]-=1
						self.listpoints[2][1]+=1
						self.listpoints[0][0]+=1
						self.listpoints[0][1]-=1
					else:
						return False
				else:
					return False 		
			self.orientation=1-self.orientation

		elif self.shape=='s':
			return True

		if self.shape=='t':
			if(self.orientation%4==0):
				if (self.listpoints[2][0]+1<board_x and self.listpoints[2][1]-1>-1 and self.listpoints[0][0]-1>-1 and self.listpoints[0][1]+1<board_y and self.listpoints[3][1]-2>-1):
					if(matrix[self.listpoints[2][0]+1][self.listpoints[2][1]-1]==0 and matrix[self.listpoints[0][0]-1][self.listpoints[0][1]+1]==0 and matrix[self.listpoints[3][0]][self.listpoints[3][1]-2]==0):
						self.listpoints[2][0]+=1
						self.listpoints[2][1]-=1
						self.listpoints[0][0]-=1
						self.listpoints[0][1]+=1
						self.listpoints[3][1]-=2
					else:
						return False
				else:
					return False

			elif(self.orientation%4==1):
				if (self.listpoints[2][0]-1>-1 and self.listpoints[2][1]+1<board_y and self.listpoints[0][0]+1<board_x and self.listpoints[0][1]-1>-1 and self.listpoints[3][0]-2>-1):
					if(matrix[self.listpoints[2][0]-1][self.listpoints[2][1]+1]==0 and matrix[self.listpoints[0][0]+1][self.listpoints[0][1]-1]==0 and matrix[self.listpoints[3][0]-2][self.listpoints[3][1]]==0):
						self.listpoints[2][0]-=1
						self.listpoints[2][1]+=1
						self.listpoints[0][0]+=1
						self.listpoints[0][1]-=1
						self.listpoints[3][0]-=2
					else:
						return False
				else:
					return False	
			elif(self.orientation%4==2):
				if (self.listpoints[2][0]+1<board_x and self.listpoints[2][1]-1>-1 and self.listpoints[0][0]-1>-1 and self.listpoints[0][1]+1<board_y and self.listpoints[3][1]+2<board_y):
					if(matrix[self.listpoints[2][0]+1][self.listpoints[2][1]-1]==0 and matrix[self.listpoints[0][0]-1][self.listpoints[0][1]+1]==0 and matrix[self.listpoints[3][0]][self.listpoints[3][1]+2]==0):
						self.listpoints[2][0]+=1
						self.listpoints[2][1]-=1
						self.listpoints[0][0]-=1
						self.listpoints[0][1]+=1
						self.listpoints[3][1]+=2
					else:
						return False
				else:
					return False

			elif(self.orientation%4==3):
				if (self.listpoints[2][0]-1>-1 and self.listpoints[2][1]+1<board_y and self.listpoints[0][0]+1<board_x and self.listpoints[0][1]-1>-1 and self.listpoints[3][0]+2<board_x):
					if(matrix[self.listpoints[2][0]-1][self.listpoints[2][1]+1]==0 and matrix[self.listpoints[0][0]+1][self.listpoints[0][1]-1]==0 and matrix[self.listpoints[3][0]+2][self.listpoints[3][1]]==0):
						self.listpoints[2][0]-=1
						self.listpoints[2][1]+=1
						self.listpoints[0][0]+=1
						self.listpoints[0][1]-=1
						self.listpoints[3][0]+=2
					else:
						return False
				else:
					return False			

			self.orientation+=1

		return True


	

'''
line=piece('l',[[0,1],[1,1],[2,1]],1)
square=piece('s',[[0,0],[0,1],[1,0],[1,1]],0)
triangle=piece('t',[[0,0],[0,1],[0,2],[1,2]],0)
'''
"""
for i in range(9):
	
	matrix=[[0 for i in range(0,board_x)] for j in range(0,board_y)]
	setp(matrix,square)
	for j in range(0,8):
		print matrix[j]
	
	print "--------"
	x=square.right()
	print x
"""
def choose_object():

	x=random.randrange(0,3,1)
	
	if(x==0):
		thing=piece('l',[[0,1],[1,1],[2,1]],1)

	elif(x==1):
		thing=piece('s',[[0,0],[0,1],[1,0],[1,1]],0)

	elif(x==2):
		thing=piece('t',[[0,0],[0,1],[0,2],[1,2]],0)

	return thing	


	

thing=choose_object()

count=0
while(1):
	y=True
	
	ends=0
	print_matrix(matrix)
	#choice=input("Enter Choice: ")	
	#choice=sys.stdin.read(1)
	def signal_handler(signum, frame):
		raise Exception("Timed out!")

	signal.signal(signal.SIGALRM, signal_handler)
	signal.alarm(1)   # one seconds
	try:
		choice=raw_input("Enter choice: ")

	except Exception, msg:
		choice='s'

	if choice=='a':
		x=thing.left()
		y=thing.down()
	elif choice=='s':
		y=thing.down()
	elif choice=='d':
		z=thing.right()
		y=thing.down()
	elif choice=='r':
		w=thing.rotate()
		y=thing.down()


	print_matrix(matrix)
	os.system('clear')


	if y==False:
		dead_list.append(thing)
		thing=choose_object()


	count+=1
	for i in range(len(height)):
		if height[i]==0:
			ends=1
			break
	
	if ends==1:
		break

print "Your game has ended."
print "Your final score:",count
print ".....Thank you......"


		
