import configparser
config = configparser.ConfigParser()

print('Creating files...')

# Creates all the information inside of the file.
config['TOKENS'] = {'BotToken': 'Your token here, https://discord.com/developers'}
config['PREFIXES'] = {'BotPrefix': 'Your prefix here.'}

try:
    with open('secrets.cfg', 'x') as secrets:
        config.write(secrets)
except FileExistsError:
    print('Files already exist!')
finally:
    print('Done.')
