import pynder

fb_id = "522777200"
fb_token = 'EAAGm0PX4ZCpsBAKdh3yhvwsnyTQj1RBDEcpgxxZACejSS8n3KZAkbTtvW1by9jQBMZAVvZArgKK21d2Grfe4js8CFWwSyA0ZAV2X7BOyNNRmjdMbkZCZCfTJdE7W07ZByqxEhNqZCoZAhLwTZAElSSAawIjZAGlxpLPmtUDIxnYP4V9y5sHKgpSWtuSdxZAhHrYHCNTyhKIX0nOvT7Ey8AFtFav1YsT0YP50vFb2EZAD1dDiwdYr7i0doivmWAWUMxD8rbTtA8I67HDCcGzyQZDZD'

session = pynder.Session(facebook_id=fb_id, facebook_token=fb_token)
users = session.nearby_users()

for user in users :
	print(user)
	user.like()

