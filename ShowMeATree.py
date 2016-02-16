import math

class BinaryTree:
	key = 0
	depth = 0
	x = 0
	y = 0
	leftChild = None
	rightChild = None
	def __init__(self,root):
		self.key = root
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self,leftChild):
		if(self.leftChild==None):
			self.leftChild = BinaryTree(leftChild)
		else:
			lchild = BinaryTree(leftChild)
			lchild.leftChild = self.leftChild
			self.leftChild = lchild

	def insertRight(self,rightChild):
		if(self.rightChild==None):
			self.rightChild = BinaryTree(rightChild)
		else:
			rchild = BinaryTree(rightChild)
			rchild.rightChild = self.rightChild
			self.rightChild = rchild
	
	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setValue(self,var):
		self.key = var

	def getValue(self):
		return self.key

	def setDepth(self,var):
		self.depth = var

	def getDepth(self):
		return self.depth

	def setCoor(self,x,y):
		self.x = x
		self.y = y

	def setX(self,var):
		self.x = var

	def getX(self):
		return self.x

	def setY(self,var):
		self.y = var

	def getY(self):
		return self.y

	def __str__(self):
		return "%s" %self.key

def showMeATree(root=None):
	queue = []
	order = []

	def calcNodeCoor(parent):
		parentY = parent.getY()
		parentX = parent.getX()
		leftChildX = 0
		rightChildX = 0
		childY = 0
		if parentY == 1:
			leftChildX = parentX - 1
			rightChildX = parentX + 1
			childY = 0
		else:
			leftChildX = parentX - parentY/3*2
			rightChildX = parentX + parentY/3*2
			childY = parentY/3*1

		lchild = parent.getLeftChild()
		rchild = parent.getRightChild()
		if lchild != None:
			lchild.setX(leftChildX)
			lchild.setY(childY)

		if rchild != None:
			rchild.setX(rightChildX)
			rchild.setY(childY)

	def dfs():
		while len(queue) > 0:
			parent = queue.pop(0)
			order.append(parent)

			lchild = parent.getLeftChild()
			if(lchild != None):
				lchild.setDepth(parent.getDepth()+1)
				queue.append(lchild)

			rchild = parent.getRightChild()
			if(rchild != None):
				rchild.setDepth(parent.getDepth()+1)
				queue.append(rchild)

	def PrintNewLine(n):
		limits = int(n)
		for i in range(0,limits,1):
			print("\n",end='')

	def PrintSpace(n):
		limits = int(n)
		for i in range(0,limits,1):
			print(" ",end='')

	if root:
		queue.append(root)
		root.setDepth(0)
		dfs()

	maxDepthNode = order[len(order)-1]

	#root
	maxDepth = maxDepthNode.getDepth()
	if maxDepth == 0:
		order[0].setCoor(0,0)
	else:
		coor = math.pow(3,maxDepth - 1)
		order[0].setCoor(coor,coor)

	curY = order[0].getY()
	curX = -1
	spaceCount = 0

	for node in order:
		if(curY!=node.getY()):#new level
			PrintNewLine(curY - node.getY())
			curY = node.getY()
			curX = -1

		spaceCount = node.getX()-curX-1
		PrintSpace(spaceCount)
		print(node.getValue(),end='')
		calcNodeCoor(node)	
		curX = node.getX()
	print('')

	print('node in order--',end='')
	for node in order:
		print(node.getValue(),end=',')
	print('')

	return order

root = BinaryTree('a')
showMeATree(root)
root.insertLeft('b')
showMeATree(root)
root.insertRight('c')
showMeATree(root)
root.insertLeft('d')
order = showMeATree(root)
root.insertRight('e')
order = showMeATree(root)

for node in order:
	print("%s(%f,%f)" %(node.getValue(),node.getX(),node.getY()))


