import pynder

# Find facebook token: https://gist.github.com/rtt/10403467#gistcomment-1846343

fb_id = ""
fb_token = ''

num_liked = 0

session = pynder.Session(facebook_id=fb_id, facebook_token=fb_token)
users = session.nearby_users()

for user in users :
	user.like()
	print("Just liked ", user, ", I have no liked ", str(num_liked), " babes in total.")
	num_liked += 1

# def like_users() :
# 	for user in users :
# 		print("Starting over")
# 		try : 
# 			user.like()
# 			print("Just liked ", user, ", I have no liked ", str(num_liked), " babes in total.")
# 			num_liked += 1
# 		except :
# 			print("I crashed: ")
# 			like_users()


# like_users()