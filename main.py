import random
import keyboard
import os
#from pynput import keyboard as listener

class Player:
	score = 25
	name = ''
	
	
	def __init__(self, name):
		self.name = name
		self.score = 25
	
	
class Game:
	dice1 = 0
	dice2 = 0
	first_roll = True
	player1 = Player('Player 1')
	player2 = Player('Player 2')
	player_turn = player1
	point_rolled = 0
	old_point = 0
	bet_amount = 2
	pot = 0
	turns = 0
	
	def __init__(self):
		self.pot = self.bet_amount * 2
		self.reset_all_points()
		
	def shake_dice(self):
		os.system('clear')
		self.status()
		for i in range(20):
			print('')
		self.dice1 = random.randint(1, 6)	
		self.dice2 = random.randint(1, 6)
		
		self.point_rolled = self.dice1 + self.dice2
		if self.old_point != 0:
			print(f'Point is: {self.old_point}\n\n')
					
		print(f'{self.player_turn.name} \nDice 1 Rolled: {self.dice1}\nDice 2 Rolled: {self.dice2}')
		print(f'{self.player_turn.name} Total point hit is: {self.point_rolled}\n\n')

		
		self.turns += 1
		
		self.processor()
				
	def next_player(self):
		if self.player_turn == self.player1:
			self.player_turn = self.player2
		elif self.player_turn == self.player2:
			self.player_turn = self.player1		

				
	def take_pot(self):
		oldPot = self.pot
		self.pot = 0
		return oldPot
			
	def reset_all_points(self):
		point_rolled = 0
		old_point = 0
		self.take_bets()
		self.first_role = True
		print('New match')
		
			
	def reset_point(self):
		point_rolled = 0
	
	def take_bets(self):
		self.player1.score -= self.bet_amount
		self.player2.score -= self.bet_amount
		self.pot = self.bet_amount * 2
		print(f'Bets of {self.bet_amount} is taken from each player')
		print(f'${self.pot} added to the pot')
		
	def processor(self):
			if (self.point_rolled == 7 or self.point_rolled == 11) and self.first_roll == True:
				self.player_turn.score += self.take_pot()
				print(f'{self.player_turn.name} wins ${self.pot}.  {self.player_turn.name}: {self.point_rolled}')
				self.reset_all_points()
					
			elif (self.point_rolled == 2 or self.point_rolled == 3 or self.point_rolled == 12) and self.first_roll == True:
				print(f'Crapped Out!!  {self.player_turn.name} Loses ${self.pot}.')
				self.next_player()
				self.player_turn.score += self.take_pot()
				self.reset_all_points()
				
			elif self.first_roll == False and self.point_rolled == 7:		
				print(f'Crapped Out!!  {self.player_turn.name} Loses ${self.pot}.')	
				self.next_player()
				self.player_turn.score += self.take_pot()
				self.reset_all_points()
								
			elif self.first_roll == False and self.point_rolled != self.old_point:
				print(f'{self.player_turn.name} missed your point')
				self.reset_point()
				self.next_player()
					
			elif self.first_roll == False and point_rolled == old_point:
				print(f'{self.player_turn.name} wins ${self.pot}.  {self.player_turn.name} Cash: ${self.player_turn.score}')
				self.reset_all_points()
			
			elif self.first_roll == True:
				print(f'no hit')
				self.old_point = self.point_rolled
				print(f'Point is {self.old_point}')
				self.first_role = False
				self.reset_point()
				self.next_player()
				
			else:
				print(f'Shouldnt happen\n\nCurrent Point {self.current_point}\nPoint Played: {self.point_rolled}')
					
					
	def status(self):
		if self.old_point != 0:
			print(f'Current Point is: {self.old_point}')
	
		print(f'\n\nCurrent Turn count: {self.turns}')			
		print(f'Current Player turn: {self.player_turn.name}\n')
		print(f'{self.player1.name} Pocket: {self.player1.score}')
		print(f'{self.player2.name} Pocket: {self.player2.score}')
			
					

####################
control = ''

game = Game()


while control != 'q':
	control = input('Press \'S\' to play, or \'C\' to check game status,  or \'Q\'  to to exit.')
	
	if control == 's':
		game.shake_dice()
		
	elif control == 'q':
		print('Game ended')
		exit()
		
	elif control == 'c':
		game.status()
