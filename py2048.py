import random
import copy

def menu():
	n=5
	w=2048

	print("Welcome to the game!")
	print("MAIN MENU")
	print("1. Play default game")
	print("2. Play custom game")
	print("3. Exit")

	ans=int(input("Enter your choice: "))

	if ans==1:
		game(n,w)
		
	elif ans==2:
		n=int(input("Enter board dimensions: "))
		w=int(input("Enter winning score: "))
		game(n,w)
		
	elif ans==3:
		exit()
		
	else:
		print("Invalid input. Please try again.")
		menu()
		
def game(dim,w_score):
	game_board=[[0 for i in range(dim)] for i in range(dim)]
	game_over=False
	
	while not game_over:
		game_board=random_assign(game_board,dim)
		for row in game_board:
			print(row)
		game_board, game_over= game_play(game_board,dim,w_score)
	
	print("GAME OVER! Back to the menu.")
	menu()
		
		
def random_assign(board,width):
	i=random.randint(0,width-1)
	j=random.randint(0,width-1)
	
	while board[i][j]!=0:
		i=random.randint(0,width-1)
		j=random.randint(0,width-1)
		
	board[i][j]=2
	return board
	
def game_play(game_base,size,win_number):
	ref_board=copy.deepcopy(game_base)
	opt=input("Enter any WASD key to make a move: ")
	ch=opt.lower()
	
	if ch=='w':
		
		for i in range(size):
			for j in range(size-1):
				
				end_loop=False
				if game_base[j][i]==0:
					
					for k in range(j,size):
						
						if game_base[k][i]!=0 and not end_loop:
							game_base[j][i]=game_base[k][i]
							game_base[k][i]=0
							end_loop=True
							
									
		for i in range(size):
			for j in range(size-1):
				
				if game_base[j][i]==game_base[j+1][i]:
					game_base[j][i]=game_base[j][i]+game_base[j+1][i]
					
					for k in range(j+1,size-1):
						game_base[k][i]=game_base[k+1][i]
					
					game_base[size-1][i]=0
					
	elif ch=='a':
		
		for i in range(size):
			for j in range(size-1):
				
				end_loop=False
				if game_base[i][j]==0:
					
					for k in range(j,size):
						
						if game_base[i][k]!=0 and not end_loop:
							game_base[i][j]=game_base[i][k]
							game_base[i][k]=0
							end_loop=True
							
									
		for i in range(size):
			for j in range(size-1):
				
				if game_base[i][j]==game_base[i][j+1]:
					game_base[i][j]=game_base[i][j]+game_base[i][j+1]
					
					for k in range(j+1,size-1):
						game_base[i][k]=game_base[i][k+1]
					
					game_base[i][size-1]=0
	
	elif ch=='s':
		
		for i in range(size):
			for j in reversed(range(1,size)):
				
				end_loop=False
				if game_base[j][i]==0:
					
					for k in reversed(range(j+1)):
						
						if game_base[k][i]!=0 and not end_loop:
							game_base[j][i]=game_base[k][i]
							game_base[k][i]=0
							end_loop=True
							
									
		for i in range(size):
			for j in reversed(range(1,size)):
				
				if game_base[j][i]==game_base[j-1][i]:
					game_base[j][i]=game_base[j][i]+game_base[j-1][i]
					
					for k in reversed(range(1,j)):
						game_base[k][i]=game_base[k-1][i]
					
					game_base[0][i]=0
	
	elif ch=='d':
		
		for i in range(size):
			for j in reversed(range(1,size)):
				
				end_loop=False
				if game_base[i][j]==0:
					
					for k in reversed(range(j+1)):
						
						if game_base[i][k]!=0 and not end_loop:
							game_base[i][j]=game_base[i][k]
							game_base[i][k]=0
							end_loop=True
																
		for i in range(size):
			for j in reversed(range(1,size)):
				
				if game_base[i][j]==game_base[i][j-1]:
					game_base[i][j]=game_base[i][j]+game_base[i][j-1]
					
					for k in reversed(range(1,j)):
						game_base[i][k]=game_base[i][k-1]
					
					game_base[i][0]=0
		

	
	else:
		print("Invalid input. Please try again.")
		game_play(game_base,size,win_number)
		
	if(ref_board==game_base):
		print("Invalid move. Please try again.")
		game_play(game_base,size,win_number)
	

	highest=max([max(row) for row in game_base])
	smallest=min([min(row) for row in game_base])

	if highest==win_number:
		for row in game_base:
			print(row)
		print("You win!!!")
		return game_base, True
	
	elif smallest!=0:
		for i in range(size):
			for j in range(size):
				
				if game_base[i][j]==game_base[i][j+1]:
					return game_base, False
				elif game_base[i][j]==game_base[i][j-1]:
					return game_base, False 
				elif game_base[i][j]==game_base[i+1][j]:
					return game_base, False 
				elif game_base[i][j]==game_base[i-1][j]:
					return game_base, False
				else:
					for row in game_base:
						print(row)
					
					print("You lose!!!")
					return game_base, True
				
	else:
		return game_base, False
	
#Driver Code
menu()

		

			

		
		
