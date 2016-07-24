import time
import os
import random

board_x=8
board_y=8

matrix=[[0 for i in range(0,board_x)] for j in range(0,board_y)]
matrix_2=[[0 for i in range(0,board_x)] for j in range(0,board_y)]

height=[8 for i in range(board_x)]
	
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
def print_matrix():
	matrix=[[0 for i in range(0,board_x)] for j in range(0,board_y)]
	setp(matrix,thing)
	for i in range(8):
		print matrix[i]
	print "--------"
	time.sleep(1)
	os.system('clear')

def setp(matrix,object):
	
	try:
		for i in range(len(object.listpoints)):
			if object.listpoints[i][0]<8 and object.listpoints[i][1]<8:
				matrix[object.listpoints[i][0]][object.listpoints[i][1]]=1	

		for j in range(8):
			if (height[j]<8):
				for k in range(height[j],8):
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
		

	def rotate(self):
		if(self.shape=='l'):
			if(self.orientation==0):	
				max1=-1
				max2=-1
				i_max2=-1
				i_max1=-1
				for i in range(len(self.listpoints)):
					max1=max(self.listpoints[i][0],max1)
					i_max1=i

				for i in range(len(self.listpoints)):
					if (self.listpoints[i][0]!=max1):
						max2=max(self.listpoints[i][0],max2)	
						i_max2=i

				self.listpoints[i_max1][0]-=1
				self.listpoints[i_max1][1]+=1

				for i in range(len(self.listpoints)):
					if(i!=i_max1 and i!=i_max2):
						self.listpoints[i][0]+=1
						self.listpoints[i][1]-=1

				self.orientation=1-self.orientation

				print self.listpoints

			elif (self.orientation==1):	
				max1=-1
				max2=-1
				i_max2=-1
				i_max1=-1
				for i in range(len(self.listpoints)):
					max1=max(self.listpoints[i][1],max1)
					i_max1=i

				for i in range(len(self.listpoints)):
					if (self.listpoints[i][1]!=max1):
						max2=max(self.listpoints[i][1],max2)	
						i_max2=i

				self.listpoints[i_max1][0]-=1
				self.listpoints[i_max1][1]-=1

				for i in range(len(self.listpoints)):
					if(i!=i_max1 and i!=i_max2):
						self.listpoints[i][0]+=1
						self.listpoints[i][1]+=1

				self.orientation=1-self.orientation
					
				print self.listpoints
		return True


	


line=piece('l',[[0,1],[1,1],[2,1]],0)
square=piece('s',[[0,0],[0,1],[1,0],[1,1]],0)
triangle=piece('t',[[0,0],[0,1],[0,2],[1,2]],0)

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
	x=0
	if(x==0):
		thing=line

	elif(x==1):
		thing=square

	elif(x==2):
		thing=triangle

	return thing	


	

thing=choose_object()
print_matrix()
y=thing.down()
print_matrix()
while(1):
	y=True
	
	

	choice='r'

	if choice=='a':
		x=thing.left()
	elif choice=='s':
		y=thing.down()
	elif choice=='d':
		z=thing.right()
	elif choice=='r':
		w=thing.rotate()	


	print_matrix()
	

	if y==False:
		thing=choose_object()

		
