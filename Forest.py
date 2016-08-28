from sys import exit

cart_gone = False
boat_gone = False
trap_door_open = False


def fork():
	while True:
		if cart_gone and boat_gone:
			dead("With no options remaining, you soon fall asleep and are over taken by the Nightgaunts.")			
		else:
			print "\nYou reach a fork in the road."
			print "The left path goes to what looks like a cabin in the distance."
			print "The right path goes to a series of large hills."
			print "What do you do?"
			
			next = raw_input("> ")
			
			if "left" in next:
				cabin()
			elif "right" in next:
				caves()
			elif next == "Go back" or next == "go back":
				forest()
			else:
				print "\nI don't understand."


def cabin():
	while True:
		print "\nYou come upon an open cabin."
		print "What do you do?"
		
		next = raw_input("> ")
		
		if (next == "Go in cabin") or (next == "go in cabin"):
			inside_cabin()
		elif (next == "Go back") or (next == "go back"):
			fork()
		else:
			print "\nI don't understand"

			
def caves():
	while True:
		print "\nYou come upon a deep cave in the hills."
		print "What do you do?"
		
		next = raw_input("> ")
		
		if (next == "Go in cave") or (next == "go in cave"):
			inside_caves()
		elif (next == "Go back") or (next == "go back"):
			fork()
		else:
			print "\nI don't understand"
			
			
def inside_cabin():
	print "\nThe cabin is empty apart from a trapdoor in the floor."
	print "What do you do?"
	global trap_door_open
	
	while True:
		next = raw_input("> ")
		
		if ((next == "Open trapdoor") or (next == "open trapdoor")) and not trap_door_open:
			print "\nThe trap door is now open"
			trap_door_open = True
		elif (next == "Go back") or (next == "go back"):
			cabin()
		elif ((next == "Go down") or (next == "go down")) and not trap_door_open:
			print "\nThe trap door is closed"
		elif ((next == "Go down") or (next == "go down")) and trap_door_open:
			mines()
		elif (next == "Close trapdoor") or (next == "close trapdoor"):
			print "\nThe trapdoor is closed."
			trap_door_open = False
		else:
			print "\nI don't understand"

			
def inside_caves():
	global boat_gone
	print "\nYou walk into the caves. They are dimly lit by some type of bioluminescent fungus."
	print "There is a strange stench throughout the cave."
	print "Further ahead, a deep stream blocks further progress."
	if not boat_gone:
		print "You can see a small boat tied to a post. It sways in the current."
	print "What do you do?"
	in_boat = False
	
	while True:
		next = raw_input("> ")
	
		if (next == "Go back") or (next == "go back"):
			caves()
		elif ((next == "Get in boat") or (next == "get in boat")) and not boat_gone:
			in_boat = True
			print "\nYou are in the boat."
		elif ((next == "Untie boat") or (next == "untie boat")) and boat_gone:
			print "\nThe boat is already gone"
		elif ((next == "Untie boat") or (next == "untie boat")) and in_boat:
			print "\nThe current takes you in the boat deeper into the cave."
			dark_caves()
		elif ((next == "Untie boat") or (next == "untie boat")) and not in_boat:
			print "\nThe current takes the empty boat further into the cave and out of view."
			boat_gone = True
		elif ((next == "Get in boat") or (next == "get in boat")) and boat_gone:
			print "\nYou lost the boat when you untied it."
		elif ((next == "Go in water") or (next == "go in water")) or ((next == "Go in stream") or (next == "go in stream")) and not in_boat:
			dead("You wade into the water. The current is stronger than you thought.\nYou lose your footing and are pulled under where you drown.")
		elif in_boat and ((next == "Follow stream") or (next == "follow stream")):
			print "\nThe rope is tied."
		elif in_boat and ((next == "Exit boat") or (next == "exit boat")):
			print "\nYou leave the boat."
			in_boat = False
		else:
			print "\nI don't understand."
			
			
def mines():
	global cart_gone
	print "\nYou climb down through the trapdoor and find yourself in some abandoned mines."
	print "The mining tunnel you are in is barely lit from the trapdoor."
	if not cart_gone:
		print "You can see a mining cart with the brake on. It's sitting on a track leading into a dark tunnel."
	print "What do you do?"
	in_cart = False
	
	while True:
		next = raw_input("> ")
	
		if (next == "Go back") or (next == "go back"):
			inside_cabin()
		elif ((next == "Get in cart") or (next == "get in cart")) and not cart_gone:
			in_cart = True
			print "\nYou are in the cart."
		elif ((next == "Release brake") or (next == "release brake")) and cart_gone:
			print "\nThe cart is already gone"
		elif ((next == "Release brake") or (next == "release brake")) and in_cart:
			print "\nYou travel down the tracks in the cart through the darkness"
			ancient_city("The minecart safely brought you past downhill tracks but it will not return.")
		elif ((next == "Release brake") or (next == "release brake")) and not in_cart:
			print "\nThe cart races off alone into the darkness down the tracks."
			cart_gone = True
		elif ((next == "Get in cart") or (next == "get in cart")) and cart_gone:
			print "\nYou sent the cart away when you released the brake."
		elif ((next == "Follow tracks") or (next == "follow tracks")) and not in_cart:
			dead("You blindly try to follow the tracks in the darkness, tripping and falling to your death.")
		elif in_cart and ((next == "Follow tracks") or (next == "follow tracks")):
			print "\nThe brake is on."
		elif in_cart and ((next == "Exit cart") or (next == "exit cart")):
			print "\nYou leave the cart."
			in_cart = False
		else:
			print "\nI don't understand."


def dark_caves():
	print "\nThe caves now are very dark and you can't see."
	print "The boat crashes against an unseen shore and shatters."
	print "You find yourself on dry land, but it is pitch black aside from a far off glow further in the cave."
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if ((next == "Follow glow") or (next == "follow glow")):
			ancient_city("You make your way to the glow, but as you get closer, you slip on a mud covered incline and slide through a hole.")
		elif (next == "Go back") or (next == "go back"):
			print "The boat is useless."
		elif ((next == "Go in water") or (next == "go in water")) or ((next == "Go in stream") or (next == "go in stream")):
			dead("You wade into the water. The current is stronger than you thought.\nYou lose your footing and are pulled under where you drown.")
		else:
			print "\nI don't understand"
			
			
def ancient_city(how):
	print "\n", how, "\nBefore you are the ruins of an ancient city."
	print "There is an old temple before you."
	print "You hear something like distant chanting, but it's getting closer."
	print "What do you do?"
	chanting = 0
	
	while chanting < 4:
		next = raw_input("> ")
		
		if (next == "Go in temple") or (next == "go in temple"):
			old_temple()
		elif chanting == 2:
			print "\nYou don't have much time..."
			chanting += 1
		else:
			print "\nI don't understand."
			if chanting <= 2: 
				print "The chanting is getting closer."
			chanting += 1
	dead("Hooded beings emerge from the darkness beyond the temple.\nThe not quite human creatures drag you off to perform unspeakable rituals on you")


def old_temple():
	print "\nYou enter the ancient city's temple."
	print "There are inhuman carvings on the wall and the lit torches make them dance in grotesque movements."
	print "In the floor is a pit too deep to see the bottom of."
	print "Claw marks are visible on the edges of the pit as well as what appear to be bloodstains."
	print "The chanting outside is getting closer."
	print "What do you do?"
	dagon = 0
	
	while dagon < 4:
		next = raw_input("> ")
		
		if ((next == "Go back") or (next == "go back")) or ((next == "Run") or (next == "run")):
		#Figure this out next-- if next in ["Go back", "go back", "Run", or "run"]:
			dead("You leave the temple only to run into hooded beings emerging from the darkness beyond the temple.\nThe not quite human creatures drag you off to perform unspeakable rituals on you")
		elif ((next == "Jump") or (next == "jump")) or ((next == "Jump in pit") or (next == "jump in pit")):
			dead("You jump into the pit! Before your heart stops in fear, you see unspeakable movement rushing up from the darkness.")
		elif (next == "Escape") or (next == "escape"):
			print "\nThere is no escape from destiny."
			dagon +=1
			if dagon <= 2:
				print "Something is rumbling from the pit. It sounds like it's getting closer"
		elif (next == "Pray") or (next == "pray"):
			print "\nNot a good idea to pray in this foul place."
			dagon +=1
			if dagon <= 2:
				print "Something is rumbling from the pit. It sounds like it's getting closer"
		elif (next == "Hide") or (next == "hide"):
			print "\nThere is nowhere to hide in the temple."
			dagon +=1
			if dagon <= 2:
				print "Something is rumbling from the pit. It sounds like it's getting closer"
		else:
			print "\nI don't understand."
			if dagon <= 2:
				print "Something is rumbling from the pit. It sounds like it's getting closer"
			dagon += 1
	insane()

		
def insane():
	print "\nFrom the depths of the pit arises the elder god Dagon."
	print "The last thing you see before you lose your mind is a group of hooded beings enter the temple."
	print "They are chanting.."
	print "'IA! IA! CTHULHU FHTAGN!"
	print "\nYou have gone insane.\n\nThere are no winners.\n\n"
	raw_input("Press Enter")
	exit(0)
	
def dead(why):
	print "\n", why, "\nYou died!\n\n"
	raw_input("Press Enter")
	exit(0)
	
def forest():
	while True:
		print "\nYou are near a forest you just exited."
		print "It is too dangerous to return."
		print "There is a path ahead of you."
		print "What do you do?"
	
		next = raw_input("> ")
	
		if next == "follow path":
			fork()
		elif (next == "Go in forest") or (next == "go in forest"):
			print "\nThe forest is too dangerous to enter"
		else:
			print "\nI don't understand."
		

forest()